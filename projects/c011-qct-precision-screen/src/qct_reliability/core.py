from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

import numpy as np
import pandas as pd


def sha256_file(path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def half_up_3(numerator: float, denominator: float) -> float:
    if not denominator:
        return 0.0
    value = Decimal(str(numerator)) / Decimal(str(denominator))
    return float(value.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))


def screen_vector(est: np.ndarray, moe: np.ndarray, threshold: float) -> np.ndarray:
    est = np.asarray(est, dtype=float)
    moe = np.asarray(moe, dtype=float)
    return np.isfinite(est) & np.isfinite(moe) & (est > 0) & (moe < threshold * est)


def assert_monotone(loose: np.ndarray, tight: np.ndarray) -> None:
    if np.any(tight & ~loose):
        raise AssertionError("tight-screen pass must be a subset of loose-screen pass")


def average_rank(values: np.ndarray) -> np.ndarray:
    return pd.Series(values).rank(method="average", ascending=True).to_numpy()


@dataclass(frozen=True)
class AllocationResult:
    designated: np.ndarray
    cap: int
    designated_population: int


def greedy_allocate(eligible, score, population, area_population) -> AllocationResult:
    """HUD skip-and-continue allocation with population as final tie break."""
    eligible = np.asarray(eligible, dtype=bool)
    score = np.asarray(score, dtype=float)
    population = np.asarray(population, dtype=np.int64)
    cap = math.floor(float(area_population) * 0.20 + 0.5)
    order = np.lexsort((np.arange(len(score)), -population, -score))
    chosen = np.zeros(len(score), dtype=bool)
    total = 0
    for i in order:
        if eligible[i] and total + population[i] <= cap:
            chosen[i] = True
            total += int(population[i])
    return AllocationResult(chosen, cap, total)


def decomposition(q100, q050, e050, screen_changed):
    q100 = np.asarray(q100, bool); q050 = np.asarray(q050, bool)
    e050 = np.asarray(e050, bool); changed = np.asarray(screen_changed, bool)
    loss = q100 & ~q050; gain = ~q100 & q050
    parts = {
        "L1": loss & ~e050,
        "L2": loss & e050 & changed,
        "L3": loss & e050 & ~changed,
        "G1": gain & changed,
        "G2": gain & ~changed,
    }
    churn = q100 ^ q050
    if sum(int(v.sum()) for v in parts.values()) != int(churn.sum()):
        raise AssertionError("decomposition does not partition churn")
    return parts
