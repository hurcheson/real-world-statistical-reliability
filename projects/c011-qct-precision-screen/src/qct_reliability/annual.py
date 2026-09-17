from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .core import average_rank, decomposition, greedy_allocate


def _num(frame: pd.DataFrame, column: str) -> np.ndarray:
    return pd.to_numeric(frame[column], errors="coerce").to_numpy(dtype=float)


def _half_up_positive(values: np.ndarray, digits: int) -> np.ndarray:
    scale = 10 ** digits
    return np.floor(values * scale + 0.5) / scale


def record_keys(frame: pd.DataFrame) -> np.ndarray:
    values = pd.to_numeric(frame["qct_id"], errors="coerce")
    return values.map(lambda x: "" if pd.isna(x) else str(int(x)).zfill(12)).to_numpy()


def set_digest(keys: np.ndarray, mask: np.ndarray) -> str:
    payload = "\n".join(sorted(keys[np.asarray(mask, bool)])) + "\n"
    return hashlib.sha256(payload.encode()).hexdigest()


@dataclass
class Replay:
    threshold: float
    income_values: np.ndarray
    poverty_values: np.ndarray
    income_pass: np.ndarray
    poverty_pass: np.ndarray
    income_eligible: np.ndarray
    poverty_eligible: np.ndarray
    eligible: np.ndarray
    income_average: np.ndarray
    poverty_average: np.ndarray
    designated: np.ndarray
    area_code: np.ndarray
    area_binding: dict[str, bool]


def _income_release(frame, suffix, threshold, arithmetic):
    estimate = _num(frame, f"b19013est1_{suffix}")
    moe = _num(frame, f"b19013me1_{suffix}")
    adjusted = _num(frame, f"adj_inc_lim_{suffix}")
    passed = np.isfinite(estimate) & np.isfinite(moe) & np.isfinite(adjusted)
    passed &= (estimate > 0) & (moe < threshold * estimate)
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = adjusted / estimate
    if arithmetic == "ratio_round7":
        raw = np.round(raw, 7)
    elif arithmetic == "stored_then_raw":
        stored = _num(frame, f"inc_factor_{suffix}")
        raw = np.where(np.isfinite(stored) & (stored > 0), stored, raw)
    elif arithmetic != "ratio_full":
        raise ValueError(arithmetic)
    return np.where(passed, raw, 0.0), passed


def _poverty_release(frame, suffix, threshold):
    denominator = _num(frame, f"b17001est1_{suffix}")
    denominator_moe = _num(frame, f"b17001me1_{suffix}")
    numerator = _num(frame, f"b17001est2_{suffix}")
    numerator_moe = _num(frame, f"b17001me2_{suffix}")
    passed = np.isfinite(denominator) & np.isfinite(denominator_moe)
    passed &= np.isfinite(numerator) & np.isfinite(numerator_moe)
    passed &= (denominator > 0) & (numerator > 0)
    passed &= (denominator_moe < threshold * denominator)
    passed &= (numerator_moe < threshold * numerator)
    with np.errstate(divide="ignore", invalid="ignore"):
        rate = _half_up_positive(numerator / denominator, 3)
    return np.where(passed, rate, 0.0), passed


def replay_2016(frame: pd.DataFrame, threshold: float, arithmetic="ratio_full") -> Replay:
    suffixes = ("11", "12", "13")
    income, income_pass, poverty, poverty_pass = [], [], [], []
    for suffix in suffixes:
        values, passed = _income_release(frame, suffix, threshold, arithmetic)
        income.append(values); income_pass.append(passed)
        values, passed = _poverty_release(frame, suffix, threshold)
        poverty.append(values); poverty_pass.append(passed)
    income = np.column_stack(income); poverty = np.column_stack(poverty)
    income_pass = np.column_stack(income_pass); poverty_pass = np.column_stack(poverty_pass)
    income_eligible = (income >= 1.0).sum(axis=1) >= 2
    poverty_eligible = (poverty >= 0.250).sum(axis=1) >= 2
    eligible = income_eligible | poverty_eligible
    income_average = np.round(np.divide(income.sum(1), income_pass.sum(1),
        out=np.zeros(len(frame)), where=income_pass.sum(1) > 0), 6)
    poverty_average = np.round(np.divide(poverty.sum(1), poverty_pass.sum(1),
        out=np.zeros(len(frame)), where=poverty_pass.sum(1) > 0), 3)
    population = pd.to_numeric(frame["p0010001"], errors="coerce").fillna(0).to_numpy(dtype=np.int64)
    area_population = _num(frame, "Area_pop")
    area_code = frame["cbsa"].astype("string").fillna("__MISSING__").to_numpy(dtype=str)
    designated = np.zeros(len(frame), dtype=bool)
    binding: dict[str, bool] = {}
    groups = pd.Series(np.arange(len(frame))).groupby(pd.Series(area_code), sort=False).groups
    for area, positions in groups.items():
        if area == "__MISSING__":
            continue
        idx = np.asarray(list(positions), dtype=int)
        income_rank = average_rank(income_average[idx])
        poverty_rank = average_rank(poverty_average[idx])
        score = (income_rank + poverty_rank) / 2
        score += 10_000 * (income_eligible[idx] & poverty_eligible[idx])
        score[~eligible[idx]] = 0
        cap = math.floor(float(area_population[idx[0]]) * 0.20 + 0.5)
        eligible_population = int(population[idx][eligible[idx]].sum())
        binding[area] = eligible_population > cap
        result = greedy_allocate(eligible[idx], score, population[idx], area_population[idx[0]])
        designated[idx] = result.designated
    return Replay(threshold, income, poverty, income_pass, poverty_pass,
                  income_eligible, poverty_eligible, eligible, income_average,
                  poverty_average, designated, area_code, binding)


def summarize_pair(frame: pd.DataFrame, loose: Replay, tight: Replay) -> tuple[dict, dict]:
    keys = record_keys(frame)
    population = pd.to_numeric(frame["p0010001"], errors="coerce").fillna(0).to_numpy(dtype=np.int64)
    changed_screen = np.any(loose.income_pass != tight.income_pass, axis=1)
    changed_screen |= np.any(loose.poverty_pass != tight.poverty_pass, axis=1)
    parts = decomposition(loose.designated, tight.designated, tight.eligible, changed_screen)
    losses = loose.designated & ~tight.designated
    gains = ~loose.designated & tight.designated
    churn = losses | gains
    strict = parts["L3"] | parts["G2"]
    changed_areas = {loose.area_code[i] for i in np.flatnonzero(strict)}
    states = {key[:2] for key in keys[strict]}
    result = {
        "records": len(frame), "E100": int(loose.eligible.sum()), "E050": int(tight.eligible.sum()),
        "eligibility_losses": int((loose.eligible & ~tight.eligible).sum()),
        "ELR": float((loose.eligible & ~tight.eligible).sum() / loose.eligible.sum()),
        "income_E100": int(loose.income_eligible.sum()), "income_E050": int(tight.income_eligible.sum()),
        "poverty_E100": int(loose.poverty_eligible.sum()), "poverty_E050": int(tight.poverty_eligible.sum()),
        "Q100": int(loose.designated.sum()), "Q050": int(tight.designated.sum()),
        "designation_losses": int(losses.sum()), "designation_gains": int(gains.sum()),
        "churn": int(churn.sum()), "CHR": float(churn.sum() / loose.designated.sum()),
        "NDR": float((tight.designated.sum() - loose.designated.sum()) / loose.designated.sum()),
        **{name: int(mask.sum()) for name, mask in parts.items()},
        "strict_nonlocal": int(strict.sum()),
        "strict_nonlocal_share": float(strict.sum() / churn.sum()),
        "strict_nonlocal_areas": len(changed_areas), "strict_nonlocal_states": len(states),
        "binding_100": int(sum(loose.area_binding.values())), "binding_050": int(sum(tight.area_binding.values())),
        "binding_to_nonbinding": sum(loose.area_binding.get(a, False) and not tight.area_binding.get(a, False) for a in loose.area_binding),
        "nonbinding_to_binding": sum(not loose.area_binding.get(a, False) and tight.area_binding.get(a, False) for a in loose.area_binding),
    }
    digests = {
        "E100": set_digest(keys, loose.eligible), "E050": set_digest(keys, tight.eligible),
        "Q100": set_digest(keys, loose.designated), "Q050": set_digest(keys, tight.designated),
        "decomposition": hashlib.sha256("\n".join(
            f"{name},{key}" for name, mask in parts.items() for key in sorted(keys[mask])
        ).encode()).hexdigest(),
    }
    return result, digests


def population_burden(frame: pd.DataFrame, loose: Replay, tight: Replay):
    population = pd.to_numeric(frame["p0010001"], errors="coerce").fillna(0).to_numpy()
    admitted = np.flatnonzero(loose.eligible)
    loss = (loose.eligible & ~tight.eligible)[admitted]
    pop = population[admitted]
    pop_quintile = np.asarray(pd.qcut(pop, 5, labels=False, duplicates="drop"))
    income_margin = np.sort(loose.income_values, axis=1)[:, -2] - 1.0
    poverty_margin = np.sort(loose.poverty_values, axis=1)[:, -2] / 0.25 - 1.0
    eligibility_type = np.where(loose.income_eligible & loose.poverty_eligible, "both",
        np.where(loose.income_eligible, "income", "poverty"))
    margin = np.where(eligibility_type == "both", np.maximum(income_margin, poverty_margin),
        np.where(eligibility_type == "income", income_margin, poverty_margin))[admitted]
    margin_quintile = np.asarray(pd.qcut(margin, 5, labels=False, duplicates="drop"))
    etype = eligibility_type[admitted]
    quintiles = [{"population_quintile": q + 1, "eligible_100": int((pop_quintile == q).sum()),
                  "losses": int(loss[pop_quintile == q].sum()),
                  "loss_rate": float(loss[pop_quintile == q].mean())} for q in range(5)]
    strata, brd = [], 0.0
    for category in ("income", "poverty", "both"):
        for q in range(5):
            stratum = (etype == category) & (margin_quintile == q)
            bottom = stratum & (pop_quintile == 0); top = stratum & (pop_quintile == 4)
            bottom_rate = float(loss[bottom].mean()) if bottom.any() else None
            top_rate = float(loss[top].mean()) if top.any() else None
            weight = float(stratum.mean())
            difference = None if bottom_rate is None or top_rate is None else bottom_rate - top_rate
            if difference is not None:
                brd += weight * difference
            strata.append({"eligibility_type": category, "margin_quintile": q + 1,
                "weight": weight, "bottom_n": int(bottom.sum()), "top_n": int(top.sum()),
                "bottom_loss_rate": bottom_rate, "top_loss_rate": top_rate,
                "risk_difference": difference})
    return quintiles, strata, float(brd)


def precision_summary(frame: pd.DataFrame, replay: Replay, criterion: str, suffixes):
    if criterion == "income":
        ratios = np.column_stack([_num(frame, f"b19013me1_{s}") / _num(frame, f"b19013est1_{s}") for s in suffixes])
        passed = replay.income_pass
    elif criterion == "poverty":
        ratios = np.column_stack([np.maximum(
            _num(frame, f"b17001me1_{s}") / _num(frame, f"b17001est1_{s}"),
            _num(frame, f"b17001me2_{s}") / _num(frame, f"b17001est2_{s}")) for s in suffixes])
        passed = replay.poverty_pass
    else:
        raise ValueError(criterion)
    accepted = ratios[passed & np.isfinite(ratios)]
    return {"criterion": criterion, "threshold": replay.threshold, "pass_count": int(passed.sum()),
            "accepted_relative_moe_mean": float(np.mean(accepted)),
            "accepted_relative_moe_median": float(np.median(accepted)),
            "accepted_relative_moe_q1": float(np.quantile(accepted, .25)),
            "accepted_relative_moe_q3": float(np.quantile(accepted, .75)),
            "accepted_relative_moe_p90": float(np.quantile(accepted, .90))}
