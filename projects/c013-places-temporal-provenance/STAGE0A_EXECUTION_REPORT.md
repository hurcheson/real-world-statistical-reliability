# C013 Stage 0A Execution Report

**Date:** 2026-09-21  
**Protocol:** `C013_CONTROLLED_EXECUTION_PROTOCOL.md` v1.0.0, frozen before substantive execution  
**Repository:** `hurcheson/real-world-statistical-reliability`  
**Repository base commit:** `712701002bf51d94e49bc15e7c3651382d0f3bb0` (`main`)  
**Branch:** `codex/c013-stage0-provenance`  
**Verified execution-tree commit:** `76304c7eddc176be7ba15853bc9860ab0ae10e40`  
**Report-finalization note:** a Git commit cannot contain its own SHA without changing that SHA; the externally verified branch HEAD after this report update is therefore reported in the user handoff.  

## 1. Verified canonical state

- Canonical version: **0.28.0**.
- Manifest file count: **25 including `MANIFEST.json`**.
- All **24 manifest-listed SHA-256 checksums** were recomputed against the uploaded Project Sources after removing upload-only suffixes such as `(1)`, `(2)`, `(3)`, `(4)`: **24/24 matched byte-for-byte**.
- D039 is controlling. C013 is **SURVIVES / CONTROLLED EXECUTION DESIGN**.
- C011 remains **PARKED / NO-GO FOR FIRST PAPER** under D037.
- C012 remains **KILLED / NO-GO FOR FIRST PAPER** under D038.
- Stage 0 provenance archiving and crosswalk construction are authorized. Manuscript and conference-abstract drafting remain prohibited.

No canonical checksum failure was found. No scientific correction was made to the v0.28.0 Project Sources. Filename normalization is the only canonical synchronization transformation.

## 2. Repository state before editing

`main` at the base commit was still structurally organized around C011. The pre-edit difference inventory is preserved at `docs/coding/REPOSITORY_DIFFERENCE_INVENTORY.md`. In particular, `research/canonical/` used transport-prefixed filenames, lacked the v0.28.0 manifest and C012/C013 records, and retained the now-retired C011 protocol in the active canonical directory. The repository's executable dependency pattern is per-project `pyproject.toml`; C013 follows that pattern.

## 3. Stage 0A scaffold and implemented controls

Created the frozen-protocol structure under `projects/c013-places-temporal-provenance/`, including protocol, raw/manifest/interim/derived data areas, reusable package code, config, tests, machine/tabular outputs, evidence records, and adjudication.

The frozen protocol is copied byte-for-byte under `protocol/` and protected by a recorded SHA-256 plus an automated integrity test.

Machine-readable controls implemented:

- retrieval/query manifest schema and validation;
- provenance-crosswalk schema and validation;
- frozen carry-forward categories (`exact carry-forward`, `revised carry-forward`, `new source wave`, `ambiguous`);
- 100% exact and >=99.5% revised thresholds plus exact-only sensitivity;
- structured comparability-break vocabulary;
- composite-key uniqueness checks;
- immutable snapshot write behavior;
- canonical v0.28.0 consistency test.

## 4. Dataset anchors encoded

All 16 frozen dataset anchors are encoded in `config/dataset_anchors.json`: ten tract/500 Cities anchors for 2016–2025 and six county PLACES anchors for 2020–2025. Dataset IDs are validated against the Socrata identifier pattern.

A material provenance result emerged during live verification: `cwsq-ngmh` and `swc5-untb` currently identify the **2025** tract and county releases, while `ai6z-tcin` and `fu4u-a9bh` are catalogued as archive IDs for **2024**. Stage 0 therefore must bind release identity to dataset ID, retrieval date, source title, and content hash rather than assume a long-lived human-readable catalog page is immutable.

## 5. Official source retrieval ledger

The browser/search layer could inspect official CDC/Socrata/HHS metadata, but the execution runtime could not receive the raw HTTP response bytes. Therefore the files under `data/raw/metadata/` are explicitly labeled **browser-mediated extracted official metadata snapshots**, not raw HTTP payloads. Each stored representation is immutable and SHA-256 hashed. The network-enabled acquisition script is committed for raw-byte retry.

| Dataset | Official/canonical metadata locator | Status | Row count captured | Stored snapshot SHA-256 | Notes |
|---|---|---|---:|---|---|
| 9z78-nsfp | https://data.cdc.gov/api/views/9z78-nsfp | success-metadata | 810103 | `99b2782b16ee…` | direct metadata; 2013/2014 BRFSS; corrected dataset contains 810,103 rows in metadata cache; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| vurf-k5wr | https://data.cdc.gov/api/views/vurf-k5wr | success-metadata | 810103 | `6ecea96ab771…` | direct metadata; 2015 main; 7 measures from 2014; metadata cache 810,103 rows; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| rja3-32tc | https://data.cdc.gov/api/views/rja3-32tc | partial-success | not captured | `55ce3dd0665b…` | HHS archive metadata; direct metadata endpoint inaccessible in browser layer; 2016 main; BP/cholesterol family from 2015; direct metadata endpoint not rendered, verified via HHS/DataLumos archive metadata; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| 6vp6-wxuq | https://data.cdc.gov/api/views/6vp6-wxuq | partial-success | not captured | `f777c6090921…` | direct metadata; 2017 main; seven rotating measures from 2016; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| 4ai3-zynv | https://data.cdc.gov/api/views/4ai3-zynv | partial-success | not captured | `d94fdd9bcb5f…` | direct metadata; 23 measures BRFSS 2018; 4 BP/cholesterol measures 2017; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| 373s-ayzu | https://data.cdc.gov/api/views/373s-ayzu | partial-success | not captured | `71da94805156…` | direct metadata; 22 measures BRFSS 2019; 7 rotating measures 2018; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| nw2y-v4gm | https://data.cdc.gov/api/views/nw2y-v4gm | partial-success | not captured | `ed9cbacce349…` | direct metadata; 25 measures BRFSS 2020; 4 BP/cholesterol measures 2019; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| em5e-5hvn | https://data.cdc.gov/api/views/em5e-5hvn | partial-success | not captured | `b982fce9bc07…` | direct metadata; 29 measures BRFSS 2021; 7 rotating measures 2020; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| ai6z-tcin | https://catalog.data.gov/dataset/places-local-data-for-better-health-census-tract-data-2024-release-4eb6e | partial-success | not captured | `90a5b50c4e2a…` | archived 2024 dataset ID; catalog metadata; Archive identifier first published 2025-12-04; 2024 release mapping from frozen prosecution: 36 main measures 2022; 4 BP/cholesterol measures 2021; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| cwsq-ngmh | https://data.cdc.gov/api/views/cwsq-ngmh | success-metadata | 3047284 | `17dc3ca1f4e2…` | current mutable dataset ID; direct metadata; Current live ID: 35 measures BRFSS 2023; 5 rotating measures BRFSS 2022; metadata cache 3,047,284 rows; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| dv4u-3x3q | https://data.cdc.gov/api/views/dv4u-3x3q | success-metadata | 176008 | `e650bab774fb…` | direct metadata; 23 measures BRFSS 2018; 4 BP/cholesterol measures 2017; metadata cache 176,008 rows; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| pqpp-u99h | https://data.cdc.gov/api/views/pqpp-u99h | partial-success | not captured | `8089a6f178de…` | direct metadata; 22 measures BRFSS 2019; 7 rotating measures 2018; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| duw2-7jbt | https://data.cdc.gov/api/views/duw2-7jbt | partial-success | not captured | `07eba613f24d…` | direct metadata; 25 measures BRFSS 2020; 4 BP/cholesterol measures 2019; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| h3ej-a9ec | https://data.cdc.gov/api/views/h3ej-a9ec | partial-success | not captured | `d0053dd82695…` | direct metadata; 29 measures BRFSS 2021; 7 rotating measures 2020; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| fu4u-a9bh | https://catalog.data.gov/dataset/places-local-data-for-better-health-county-data-2024-release-cb149 | partial-success | not captured | `06e2cac92800…` | archived 2024 dataset ID; catalog metadata; Archive identifier first published 2025-12-04; 2024 release source mapping per frozen prosecution: 2022 main; 2021 BP/cholesterol; raw HTTP byte transfer unavailable in current browser/runtime bridge. |
| swc5-untb | https://data.cdc.gov/api/views/swc5-untb | partial-success | not captured | `8c6ad5254933…` | current mutable dataset ID; direct metadata; Current live ID: 35 measures BRFSS 2023; 5 rotating measures BRFSS 2022; raw HTTP byte transfer unavailable in current browser/runtime bridge. |

Row counts were captured only where the official metadata representation exposed a trustworthy cached count in the material actually inspected. Missing counts were not guessed. Full measure-coverage grouped queries are deferred because the direct SODA query endpoint was not accessible through the current browsing/runtime bridge.

## 6. Documents and sections actually inspected

### CDC PLACES FAQ
Inspected the methodology/validation and using-data material covering the 2023 confidence-interval change, use of confidence intervals, ranking limitations, and the explicit warning that the current model does not support local trend tracking. Also inspected the statement that subcounty estimates use fixed 2020/2010 census population bases while county estimates use annual population estimates but do not include time as a model variable.

### CDC PLACES Methodology
Inspected the MRP inputs, county versus subcounty population bases, 2010-to-2020 census transition, and Monte Carlo construction of point estimates/95% intervals.

### CDC Current Release Notes / historical release notes
Inspected 2025 source-year/carry-forward notes and the visible historical notes for 2020–2024, including rotating measures, 2024 population/geography changes, cervical-screening availability, and revised cholesterol-screening information.

### CDC measure definitions
Inspected the current colorectal-cancer-screening definition, target population ages 45–75, change from the older age threshold, and the explicit CDC note that estimates after the 2021 recommendation/question changes are not comparable with previous years.

### Official Socrata/HHS catalog metadata
Inspected title/description/source-year/schema material for all anchors where direct metadata rendered; for `rja3-32tc`, `ai6z-tcin`, and `fu4u-a9bh`, direct metadata rendering failed and HHS/data.gov catalog evidence was used instead. These three remain partial retrievals until raw direct responses are archived.

### Canonical C013 prosecution and protocol
Read the binding decision, scope/fairness boundary, 2016–2025 source-year map, exact-copy case evidence, frozen Stage 0 rules, crosswalk fields, carry-forward thresholds, comparability breaks, and stop rules.

**Inspection qualification:** the sources above were inspected for the listed sections/facts. Stage 0A does **not** claim that every historical CDC page, every full Socrata JSON document, or every downstream paper/supplement was fully archived and read in this execution window. That deeper inspection remains required before corpus adjudication.

## 7. Preliminary crosswalk

`outputs/machine/preliminary_provenance_crosswalk.jsonl` contains **128 records** over eight prespecified sentinel measures across the frozen release/geography anchors. Its purpose is to validate the record model and documented measure-specific BRFSS time mapping before the full Stage 0B expansion. It is not presented as the complete PLACES measure corpus.

Populated now:

- release/product/dataset/geography;
- source-year mapping for sentinel measures;
- preliminary geography/poststratification/CI eras;
- known product/geography/definition break flags;
- carry-forward-source-year relationship.

Deliberately unresolved until row-level archive construction:

- complete release-specific exact definitions and eligibility for every measure;
- exact-copy percentages for every adjacent pair;
- common-geography counts and empirical coverage changes;
- definitive exact/revised carry-forward classifications where only same-source-year documentation is currently available;
- full measure coverage for every anchor;
- unresolved historical geography-vintage details at county level.

No field was populated by treating release year as source year.

## 8. Discrepancies and warnings

The machine-readable log is `adjudication/stage0a_discrepancy_log.json`. Material items:

1. Current live 2025 IDs versus separate 2024 archive IDs require immutable release bindings.
2. Raw HTTP bytes could not be transferred from the web inspection layer into the local execution runtime.
3. Direct metadata rendering failed for three archive anchors; catalog metadata was available but is not an equivalent raw-byte archive.
4. Exact/revised carry-forward classification is intentionally left `ambiguous` where empirical exact-copy diagnostics have not yet been run.
5. Historical source pages are mutable; publication-grade claims require frozen primary-source copies.

## 9. Tests

### New C013 tests

Command:

```text
cd projects/c013-places-temporal-provenance
python --version
pytest -q
```

Environment: Python 3.13.5; pytest 9.0.2; standard-library runtime dependencies only.

Result: **14 passed, 0 failed, 0 skipped**.

Coverage includes all required Stage 0A invariant classes requested in the execution brief: required fields, composite key, categories, dataset ID, SHA-256, UTC parsing, missing/conflicting source-year handling, exact/revised thresholds, comparability logic, duplicate retrieval semantics, raw immutability, protocol integrity, v0.28.0 consistency, and deterministic fixture serialization.

### GitHub branch verification

Permanent GitHub Actions workflow `.github/workflows/c013-stage0.yml` completed successfully on verified execution-tree commit `76304c7eddc176be7ba15853bc9860ab0ae10e40` (run `35659291238`, Python 3.12). Results:

- C013 tests: **14 passed**;
- machine-state validation: `{'retrieval_records': 16, 'crosswalk_records': 128}`;
- preliminary crosswalk SHA-256: `81f7b98a9e30392e65a21d5c59a9ca192fdccda9ee66fbfbe751aa985801b98e`;
- retrieval manifest SHA-256: `5cb27117dcf71c380adf86ff4cb45faffb74e206f7e1dcfbb8d259494ec12621`;
- fresh-directory deterministic rerun: passed;
- C011 invariant tests: **4 passed**;
- C011 regression test: permanently skipped when the excluded immutable workbook is absent, with an explicit CI message.

An earlier explicit regression attempt (workflow run `35659052433`) produced exactly one failure: `FileNotFoundError` for `projects/c011-qct-precision-screen/data/raw/qct_data_2016.xlsx`; the same run reported `C011_RAW_PRESENT=false`. This is preserved as an environment/provenance-input limitation rather than hidden as a pass.

### Existing C011 repository tests

The repository contains `test_invariants.py` and `test_2016_regression.py`. The regression test requires the excluded immutable workbook `projects/c011-qct-precision-screen/data/raw/qct_data_2016.xlsx` (27,467,633 bytes in the prior C011 archive), which is intentionally not in ordinary Git history. The branch workflow attempts the existing suite and preserves the exact result. If that raw workbook is unavailable to GitHub Actions, the regression failure is an environment/provenance-input absence, not a C013 code failure.

## 10. Fresh-directory reproducibility rerun

Commands executed locally:

```text
TMP=$(mktemp -d /mnt/data/c013-cleanroom-XXXX)
cp -a projects/c013-places-temporal-provenance "$TMP/project"
cd "$TMP/project"
PYTHONPATH=src python scripts/validate_stage0.py > run1.txt
PYTHONPATH=src python scripts/validate_stage0.py > run2.txt
cmp run1.txt run2.txt
sha256sum outputs/machine/preliminary_provenance_crosswalk.jsonl data/manifests/retrieval_manifest.jsonl
```

Both validation runs returned:

```text
{'retrieval_records': 16, 'crosswalk_records': 128}
```

The two validation outputs were byte-identical. Machine-output hashes at the time of the clean-room run:

```text
81f7b98a9e30392e65a21d5c59a9ca192fdccda9ee66fbfbe751aa985801b98e  outputs/machine/preliminary_provenance_crosswalk.jsonl
5cb27117dcf71c380adf86ff4cb45faffb74e206f7e1dcfbb8d259494ec12621  data/manifests/retrieval_manifest.jsonl
```

The clean-room validation demonstrates deterministic validation/serialization of the archived Stage 0A representations. It does **not** substitute for a second independent network retrieval of source bytes.

## 11. Network acquisition attempt

Command:

```text
PYTHONPATH=src python scripts/retrieve_socrata.py
```

Local result: exit code 1 with DNS/network resolution unavailable in the execution container. The web inspection layer remained available separately. This is why no raw-response SHA is falsely claimed. The committed script is ready for a network-enabled rerun and uses content-addressed filenames to prevent overwrite.

## 12. Checksum inventory

`outputs/machine/checksum_inventory.sha256` records SHA-256 digests for the Stage 0A files generated before the inventory itself. Canonical checksums remain governed by `research/canonical/MANIFEST.json` and all 24 were independently verified.

## 13. Files created or changed

- synchronized `research/canonical/` v0.28.0 snapshot using canonical filenames;
- root README/.gitignore adjustments for active C013 work and metadata-snapshot policy;
- complete C013 Stage 0A project scaffold;
- frozen protocol copy/hash;
- dataset-anchor configuration;
- retrieval/crosswalk schemas and field definitions;
- validation/ingestion/acquisition code;
- 16 metadata-extract snapshots;
- 16-record retrieval manifest;
- 128-record preliminary crosswalk (JSONL + CSV);
- structured evidence ledger and side findings;
- discrepancy log;
- 14-test suite;
- this report.

## 14. Scientific and technical blockers

**Resolvable blocker A — raw byte provenance.** The current tool bridge did not allow official HTTP response bytes to be saved locally. Before Stage 0B is declared reproducible, rerun `scripts/retrieve_socrata.py` in a network-enabled environment and register raw content hashes.

**Resolvable blocker B — complete per-anchor query coverage.** Row counts and grouped measure/source-year coverage were not reproducibly queried for every dataset anchor in this environment.

**Resolvable blocker C — direct archive-anchor metadata.** `rja3-32tc`, `ai6z-tcin`, and `fu4u-a9bh` need direct first-party raw metadata snapshots even though archive/catalog evidence resolved their identities.

**Resolvable blocker D — full crosswalk.** Stage 0A intentionally stops at a sentinel-measure preliminary crosswalk. Stage 0B must expand to every eligible measure/value type and compute common-geography/exact-copy diagnostics from archived rows.

These are execution/provenance gaps, not reasons to alter D039 or the frozen scientific design.

## 15. Exact readiness decision

**STAGE 0A INCOMPLETE — RESOLVABLE BLOCKERS**
