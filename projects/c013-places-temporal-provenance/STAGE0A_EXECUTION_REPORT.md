# C013 Stage 0 Completion Report

**Status:** authoritative Stage 0 completion record  
**Date:** 2026-09-21  
**Repository:** `hurcheson/real-world-statistical-reliability`  
**Branch:** `codex/c013-stage0-provenance`  
**Base `main` commit:** `712701002bf51d94e49bc15e7c3651382d0f3bb0`  
**Frozen protocol:** `C013_CONTROLLED_EXECUTION_PROTOCOL.md` v1.0.0  
**Frozen protocol SHA-256:** `fa87dc628428b9c9b613f20f2fa80769fe16d153e1f749962fc32b2ceb126629`

> The filename is retained for continuity with the earlier Stage 0A checkpoint. This document supersedes the earlier “Stage 0A incomplete” status.

## 1. Canonical-state verification

The Project Sources were normalized to canonical filenames and verified against `research/canonical/MANIFEST.json` v0.28.0.

- canonical files listed in the manifest: **24**
- manifest file count including `MANIFEST.json`: **25**
- recomputed canonical SHA-256 matches: **24/24**
- controlling decision: **D039**
- C011 remains **PARKED / NO-GO FOR FIRST PAPER** under D037
- C012 remains **KILLED / NO-GO FOR FIRST PAPER** under D038
- C013 remains the controlled-execution candidate

No scientific content in the v0.28.0 canonical source set was altered.

## 2. Stage 0 deliverables completed

Stage 0 required a source/query manifest, frozen raw hashes, normalized release schema, machine-readable provenance crosswalk, schema/invariant tests, and discrepancy logging. All are now present.

### Frozen source archive

The 16 configured CDC/Socrata release anchors all resolve in the networked execution environment.

The final source archive contains:

- **64** content-addressed retrieval records:
  - metadata
  - row count
  - one-row schema/sample
  - grouped measure/source-year coverage
- **839** observed release × measure × value-type × source-year coverage cells
- direct first-party raw metadata for all 16 anchors, including `rja3-32tc`, `ai6z-tcin`, and `fu4u-a9bh`

The previously open browser/runtime raw-byte limitations are therefore resolved.

### Final provenance crosswalk

`outputs/machine/provenance_crosswalk.jsonl` contains **839 validated records** covering the observed metadata-level cells.

The final crosswalk preserves:

- nominal release year separately from BRFSS source year;
- dataset ID and product;
- geography level and geography-vintage comparability;
- exact CDC measure definition text;
- data-value type;
- predecessor relation;
- carry-forward status;
- common-geography and exact-copy diagnostics where linkage is valid;
- explicit comparability-break flags where direct linkage is not scientifically defensible.

The earlier 128-record sentinel crosswalk is retained only as a scaffold/regression fixture and is not the controlling Stage 0 crosswalk.

## 3. Carry-forward diagnostics

The frozen candidate rule identified **131** adjacent-release cells with the same documented source year. All 131 were evaluated with row-level public CDC/Socrata queries.

The controlling corrected result is:

- **115 exact carry-forwards**
- **0 revised carry-forwards**
- **16 ambiguous pairs**
- **708 new-source-wave crosswalk cells**

The 16 ambiguous pairs have two distinct causes.

### 3.1 Eight intentionally unlinked transitions

Eight tract pairs are marked ambiguous because direct equality under a common geography ID is not a valid operation across the relevant design break:

- four 2019→2020 tract BP/cholesterol cells cross the 500 Cities → PLACES product-scope transition;
- four 2023→2024 tract BP/cholesterol cells cross the 2010 → 2020 Census tract-vintage transition.

For these records, `common_geography_count` and `exact_copy_percentage` remain null by design rather than being fabricated from incompatible identifiers.

### 3.2 Eight linked 2023→2024 county pairs

Eight county BP/cholesterol value-type pairs share source year 2021 and are linkable across common county FIPS, but they are not exact or near-exact copies.

Across **3,069 common counties**, observed exact-copy percentages range from **0% to about 1.21%**, far below the frozen **99.5%** revised-carry-forward threshold.

These remain `ambiguous` with respect to the frozen carry-forward taxonomy: same documented source wave, but neither exact nor revised carry-forward under the prespecified empirical rule.

## 4. Comparator correction and superseded result

An earlier full comparator run produced **118 exact / 13 ambiguous / 0 revised**. That result is **superseded**.

Subsequent inspection identified invalid direct linkage assumptions across tract transitions where product scope or Census geography vintage changes. The comparator was corrected in the branch history, including:

- `22ef1ef` — enforce defensible tract linkage;
- `29f4f73` — mark non-linkable tract transitions ambiguous;
- follow-up validation commits enforcing linked/unlinked invariants.

After the correction, two independent full executions produced the same diagnostic SHA-256 and the same classification totals:

> **115 exact / 16 ambiguous / 0 revised**

The superseded 118/13 result must not be cited or used downstream.

## 5. Frozen evidence and hashes

The completed Stage 0 machine state has the following controlling hashes:

| Artifact | SHA-256 |
|---|---|
| `data/manifests/retrieval_manifest.jsonl` | `0d1214ad54f06a344fd3e2164171f49c925241f162d2e1302fdefc0a622693d9` |
| `data/manifests/carry_forward_query_manifest.jsonl` | `3bd30aead1914390ccbd4e80dbb404e21b9b42406bffc0ca916e0e30e6853fc0` |
| `outputs/machine/preliminary_provenance_crosswalk.jsonl` | `81f7b98a9e30392e65a21d5c59a9ca192fdccda9ee66fbfbe751aa985801b98e` |
| `outputs/machine/provenance_crosswalk.jsonl` | `eba5d59f5a6ed83bc7661104e97c3ed0b7aca6c4cf95fdae4b3c0330f1f59311` |
| `outputs/machine/carry_forward_diagnostics.jsonl` | `500c0531a6a63ac8f0bbaf63b4ccc92b59de8f5b6c762b7b7d5972adc1c584b7` |
| `data/raw_archives/c013-carry-forward-raw-pages.tar.gz` | `5faadb4018cb26608b7fc6bf77a8f4fc9557e61fbf9b87e32e73777fee6f0814` |

The compressed raw row-level archive is **45,807,132 bytes** and is tracked in the branch because GitHub Actions lacked permission to create a release asset.

## 6. Dataset-identity finding

The Stage 0 audit verified a material mutable-catalog issue:

- `cwsq-ngmh` is the 2025 tract release; 2024 is preserved as `ai6z-tcin`.
- `swc5-untb` is the 2025 county release; 2024 is preserved as `fu4u-a9bh`.

Release identity is therefore bound to dataset ID + title + retrieval evidence + content hash, not to an assumed persistent human-readable catalog page.

## 7. Validation and reproducibility

Permanent GitHub Actions verification on the completed state reports:

- C013 tests: **15 passed**
- C011 invariant tests: **4 passed**
- C011 2016 regression: explicitly skipped when the intentionally excluded immutable workbook is absent
- retrieval records: **64**
- preliminary crosswalk: **128**
- final crosswalk: **839**
- carry-forward rows: **131**
- exact carry-forwards: **115**
- revised carry-forwards: **0**
- ambiguous carry-forwards: **16**
- row-level diagnostic records: **131**
- row-level query-manifest records: **262**
- raw evidence archive hash/size: verified
- fresh-directory deterministic validation rerun: passed

The corrected full diagnostic output was independently reproduced with the same SHA-256:

`500c0531a6a63ac8f0bbaf63b4ccc92b59de8f5b6c762b7b7d5972adc1c584b7`

The row-query manifest includes retrieval timestamps, so its byte-level hash is tied to the frozen successful retrieval run rather than expected to remain identical under a new network retrieval.

## 8. Discrepancy status

The machine-readable discrepancy record is `adjudication/stage0a_discrepancy_log.json`.

All Stage 0 execution blockers are resolved:

- raw HTTP archival — resolved;
- complete anchor-level counts/coverage — resolved;
- direct metadata for archive IDs — resolved;
- full crosswalk expansion — resolved;
- exact/common-geography carry-forward diagnostics — resolved;
- comparator-linkage correction — resolved and reproducibly verified.

The remaining ambiguous cells are scientific classifications under the frozen rules, not unresolved Stage 0 execution failures.

## 9. Workflow freeze

One-time acquisition and construction workflows are now **manual-dispatch only**:

- network archive;
- metadata crosswalk build;
- carry-forward smoke diagnostics;
- full carry-forward diagnostics.

Only the read-only Stage 0 verification workflow remains automatic on branch pushes. This prevents time-stamped source manifests from being silently regenerated after the evidence freeze.

## 10. Stage 0 stop-rule adjudication

The frozen protocol requires Stage 0 to stop if primary source-year mapping cannot be resolved or if the public archive cannot be reproduced.

Neither stop condition remains active.

- source-year mapping is represented across the full observed coverage;
- all configured anchors resolve;
- raw source evidence and query hashes are frozen;
- carry-forward diagnostics are reproducible;
- final crosswalk and schemas validate.

## 11. Exact readiness decision

> **C013 STAGE 0 — COMPLETE.**

Stage 0 has satisfied the frozen provenance/archive/crosswalk gate.

No Stage 1 work was started in this execution. The next protocol stage is **Stage 1 — corpus recoding**, which requires independent dual-human coding and its own evidence/adjudication workflow.

Stage 0 completion does **not** authorize manuscript design, manuscript drafting, conference-abstract drafting, case-study expansion, or a final C013 paper verdict.
