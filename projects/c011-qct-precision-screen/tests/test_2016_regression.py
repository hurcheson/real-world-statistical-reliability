from pathlib import Path

import pandas as pd

from qct_reliability.annual import replay_2016, summarize_pair
from qct_reliability.io import read_hud_workbook


def test_2016_exact_and_counterfactual_identity():
    root = Path(__file__).resolve().parents[1]
    frame = read_hud_workbook(root / "data/raw/qct_data_2016.xlsx")
    official = pd.to_numeric(frame.qct, errors="coerce").fillna(0).astype(bool).to_numpy()
    signatures = []
    for arithmetic in ("ratio_full", "ratio_round7", "stored_then_raw"):
        tight = replay_2016(frame, .50, arithmetic)
        loose = replay_2016(frame, 1.00, arithmetic)
        assert int((official != tight.designated).sum()) == 0
        result, digests = summarize_pair(frame, loose, tight)
        signatures.append((result["E100"], result["E050"], result["Q100"], result["Q050"],
                           result["L1"], result["L2"], result["L3"], result["G1"], result["G2"],
                           tuple(sorted(digests.items()))))
    assert len(set(signatures)) == 1
    assert signatures[0][:9] == (17042, 16368, 14057, 13619, 473, 159, 19, 71, 142)
