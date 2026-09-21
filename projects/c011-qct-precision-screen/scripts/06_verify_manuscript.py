from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "qct_data_2016.xlsx"
EXPECTED_SHA256 = "75ae56ca258aabde75081739c401aa619886f0463a525d7cf786effbe9ba991f"
EXPECTED = {
    "records": 74272,
    "E100": 17042,
    "E050": 16368,
    "eligibility_losses": 674,
    "Q100": 14057,
    "Q050": 13619,
    "designation_losses": 651,
    "designation_gains": 213,
    "churn": 864,
    "L1": 473,
    "L2": 159,
    "L3": 19,
    "G1": 71,
    "G2": 142,
    "strict_nonlocal": 161,
    "strict_nonlocal_areas": 75,
    "strict_nonlocal_states": 31,
    "binding_100": 175,
    "binding_050": 162,
    "binding_to_nonbinding": 13,
    "nonbinding_to_binding": 0,
    "mismatches_050": 0,
}
EXPECTED_BRD = 0.12239634180436126
EXPECTED_QUINTILES = [(3409, 362), (3409, 133), (3411, 95), (3405, 49), (3408, 35)]
MANUSCRIPT = ROOT / "manuscript"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_once(destination: Path) -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "03_run_2016.py"), "--output", str(destination)],
        cwd=ROOT,
        env={**__import__("os").environ, "PYTHONPATH": str(ROOT / "src")},
        check=True,
    )


def file_digests(directory: Path) -> dict[str, str]:
    return {p.name: sha256(p) for p in sorted(directory.iterdir()) if p.is_file()}


def main() -> None:
    assert RAW.stat().st_size == 27_467_633
    assert sha256(RAW) == EXPECTED_SHA256
    with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
        first_path, second_path = Path(first), Path(second)
        run_once(first_path)
        run_once(second_path)
        assert file_digests(first_path) == file_digests(second_path)
        result = pd.read_csv(first_path / "annual_result.csv").iloc[0]
        for name, expected in EXPECTED.items():
            assert int(result[name]) == expected, (name, result[name], expected)
        assert abs(float(result["BRD"]) - EXPECTED_BRD) < 1e-15
        assert int(result["L1"] + result["L2"] + result["L3"] + result["G1"] + result["G2"]) == 864
        assert int(result["L3"] + result["G2"]) == 161
        quintiles = pd.read_csv(first_path / "population_quintiles.csv")
        observed = list(zip(quintiles["eligible_100"].astype(int), quintiles["losses"].astype(int)))
        assert observed == EXPECTED_QUINTILES
        records = pd.read_csv(first_path / "analysis_records.csv")
        assert len(records) == 74_272
        assert int((records["official_qct_050"] != records["Q050"]).sum()) == 0
    manuscript_text = "\n".join(path.read_text(encoding="utf-8") for path in MANUSCRIPT.glob("*.md"))
    for forbidden in ("85,390", "RMoE ≤", "c ≤ 0.50", "1,842", "3,287", "3,530"):
        assert forbidden not in manuscript_text, forbidden
    for required in ("74,272", "17,042", "16,368", "14,057", "13,619", "0.122396"):
        assert required in manuscript_text, required
    print("PASS: workbook identity, determinism, locked results, official replay, and manuscript factual lint")


if __name__ == "__main__":
    main()
