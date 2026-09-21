# Repository difference inventory before C013 edits

Base: `main` at `712701002bf51d94e49bc15e7c3651382d0f3bb0`.

Observed before branch edits:

- `research/canonical/` used transport-prefixed names such as `04-03_DECISION_LEDGER.md`, rather than canonical filenames.
- Repository canonical records were predominantly v0.23-era (2026-09-09) and did not contain D038/D039, C012 final prosecution, C013 prosecution, or the frozen C013 protocol.
- `research/canonical/MANIFEST.json` and canonical `README.md` were absent.
- The retired `16-20_C011_EXECUTION_PROTOCOL.md` remained in the repository canonical directory even though v0.28.0 retires it from active Project Sources.
- Root README correctly reflected D037/C011 parked status but remained C011-centric and did not identify C013 as the active controlled-execution branch.
- Existing executable code/tests were under `projects/c011-qct-precision-screen/`; no C013 project scaffold existed.
- Existing C011 dependency system is per-project `pyproject.toml` with Python >=3.12 and pytest as a test extra; C013 follows the same maintainable per-project pattern while keeping Stage 0 dependencies standard-library-only.

The v0.28.0 Project Sources are authoritative for synchronization. No repository-only C011/C012/O001 status is permitted to supersede D037-D039.
