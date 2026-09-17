from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from qct_reliability.annual import (population_burden, precision_summary,
    record_keys, replay_2016, set_digest, summarize_pair)
from qct_reliability.io import read_hud_workbook


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = Path(args.output); output.mkdir(parents=True, exist_ok=True)
    frame = read_hud_workbook(root / "data/raw/qct_data_2016.xlsx")
    keys = record_keys(frame)
    official = pd.to_numeric(frame.qct, errors="coerce").fillna(0).astype(bool).to_numpy()
    variant_results = []
    selected = None
    for variant in ("ratio_full", "ratio_round7", "stored_then_raw"):
        loose = replay_2016(frame, 1.00, variant); tight = replay_2016(frame, .50, variant)
        summary, digests = summarize_pair(frame, loose, tight)
        summary.update({"year": 2016, "variant": variant,
            "official_qct_050": int(official.sum()),
            "reconstructed_qct_050": int(tight.designated.sum()),
            "mismatches_050": int((official != tight.designated).sum()),
            **{f"{name}_digest": value for name, value in digests.items()}})
        variant_results.append(summary)
        if variant == "ratio_full": selected = (loose, tight, summary)
    pd.DataFrame(variant_results).to_csv(output / "implementation_variants.csv", index=False, lineterminator="\n")
    loose, tight, summary = selected
    quintiles, strata, brd = population_burden(frame, loose, tight)
    summary["BRD"] = brd
    pd.DataFrame([summary]).to_csv(output / "annual_result.csv", index=False, lineterminator="\n")
    pd.DataFrame(quintiles).assign(year=2016).to_csv(output / "population_quintiles.csv", index=False, lineterminator="\n")
    pd.DataFrame(strata).assign(year=2016).to_csv(output / "brd_strata.csv", index=False, lineterminator="\n")
    precision = []
    for criterion in ("income", "poverty"):
        p100 = precision_summary(frame, loose, criterion, ("11", "12", "13"))
        p050 = precision_summary(frame, tight, criterion, ("11", "12", "13"))
        p100["year"] = p050["year"] = 2016
        p050["newly_rejected"] = p100["pass_count"] - p050["pass_count"]
        p100["newly_rejected"] = 0
        precision.extend((p100, p050))
    pd.DataFrame(precision).to_csv(output / "precision_purchased.csv", index=False, lineterminator="\n")
    record = pd.DataFrame({"qct_id": keys, "official_qct_050": official.astype(int),
        "E100": loose.eligible.astype(int), "E050": tight.eligible.astype(int),
        "Q100": loose.designated.astype(int), "Q050": tight.designated.astype(int)})
    record.to_csv(output / "analysis_records.csv", index=False, lineterminator="\n")
    record.loc[record.official_qct_050 != record.Q050].to_csv(output / "reconstruction_mismatches.csv", index=False, lineterminator="\n")
    (output / "digests.json").write_text(json.dumps({
        "E100": set_digest(keys, loose.eligible), "E050": set_digest(keys, tight.eligible),
        "Q100": set_digest(keys, loose.designated), "Q050": set_digest(keys, tight.designated),
    }, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__": main()
