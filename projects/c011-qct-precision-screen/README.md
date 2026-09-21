# C011 — QCT precision-screen reliability

This repository state consolidates the post-D036 reproducibility investigation.

Run:

```bash
python -m pip install -e .
pytest
python scripts/01_register_data.py
python scripts/02_audit_workbooks.py
PYTHONPATH=src python scripts/03_run_2016.py --output outputs/determinism/run1/2016
PYTHONPATH=src python scripts/03_run_2016.py --output outputs/determinism/run2/2016
diff -qr outputs/determinism/run1/2016 outputs/determinism/run2/2016
python scripts/04_build_final_outputs.py
python scripts/05_build_manuscript_figures.py
python scripts/06_verify_manuscript.py
```

Raw HUD workbooks are immutable and excluded from Git. Their hashes and source URLs are
recorded in `data/manifest.csv` and `provenance/raw_input_manifest.json`.

The frozen protocol is copied under `protocol/`; it must not be edited.

Only 2016 currently clears the complete manuscript reproducibility gate. See the repository-
root `C011_FINAL_REPRODUCIBILITY_ADJUDICATION.md` for the scientific disposition of all years.
The repaired manuscript package preserves that D037 disposition: it is a manuscript-grade
technical record, not a renewed multi-year or first-paper claim.
