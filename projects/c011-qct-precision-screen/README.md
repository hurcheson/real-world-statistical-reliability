# C011 — QCT precision-screen reliability

This repository state consolidates the post-D036 reproducibility investigation.

Run:

```bash
python -m pip install -e .
pytest
python scripts/01_register_data.py
python scripts/02_audit_workbooks.py
```

Raw HUD workbooks are immutable and excluded from Git. Their hashes and source URLs are
recorded in `data/manifest.csv` and `provenance/raw_input_manifest.json`.

The frozen protocol is copied under `protocol/`; it must not be edited.
