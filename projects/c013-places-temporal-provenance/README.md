# C013 PLACES Temporal Provenance

This directory contains the completed **Stage 0 — provenance archive and crosswalk** for the frozen C013 controlled-execution protocol. It is not a manuscript workspace, and Stage 0 completion does not authorize manuscript or conference-abstract drafting.

## Controlling Stage 0 artifacts

- `protocol/C013_CONTROLLED_EXECUTION_PROTOCOL.md` + `protocol/PROTOCOL_SHA256` — frozen execution protocol.
- `config/dataset_anchors.json` — 16 frozen CDC/Socrata release anchors.
- `data/manifests/retrieval_manifest.jsonl` — 64 content-addressed metadata/count/sample/coverage retrieval records.
- `outputs/machine/measure_coverage.jsonl` — 839 observed release × measure × value-type × source-year coverage cells.
- `outputs/machine/provenance_crosswalk.jsonl` — final 839-record machine-readable provenance crosswalk.
- `data/manifests/carry_forward_query_manifest.jsonl` — 262 row-level query records for 131 adjacent-release same-source-wave comparisons.
- `outputs/machine/carry_forward_diagnostics.jsonl` — 131 frozen carry-forward diagnostics.
- `data/raw_archives/c013-carry-forward-raw-pages.tar.gz` — compressed raw CSV pages used by those diagnostics, tracked with SHA-256 in `outputs/machine/carry_forward_raw_archive.json`.
- `adjudication/stage0a_discrepancy_log.json` — discrepancy/correction ledger.
- `STAGE0A_EXECUTION_REPORT.md` — authoritative Stage 0 completion report; the filename is retained for continuity with the earlier checkpoint.

## Corrected carry-forward result

The controlling, reproducible Stage 0 diagnostic is:

- **115 exact carry-forwards**
- **0 revised carry-forwards**
- **16 ambiguous pairs**
- **708 new-source-wave cells**

The 16 ambiguous pairs split into:

- 8 intentionally unlinked product/geography-vintage transitions, where direct common-geography equality is not a valid operation; and
- 8 linked 2023→2024 county BP/cholesterol value-type pairs whose exact-copy percentages are far below the frozen 99.5% revised-carry-forward threshold.

An earlier 118-exact / 13-ambiguous run is superseded. It preceded the tightened tract-linkage rules and must not be cited.

## Execution boundary

Stage 0 is complete. The next protocol stage is **Stage 1 — corpus recoding**, which requires independent dual-human coding. No automatic transition to Stage 1, case-study expansion, manuscript drafting, or abstract drafting is authorized by this directory.
