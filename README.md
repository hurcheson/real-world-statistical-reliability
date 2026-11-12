# Real-World Statistical Reliability

A reproducible research archive focused on how statistical conclusions can be affected by **data quality, measurement choices, and implementation details**.

## Archived study: C011

The repository includes a technical investigation of **HUD Qualified Census Tract (QCT) precision-screen reproducibility**. It documents the data sources, immutable inputs, analysis scripts, checks, and scientific decisions so the limits of the evidence are visible.

**Research disposition:** This line of work is **parked** as a first-paper candidate. The **2016 replay** is the only year currently meeting the full manuscript reproducibility gate; this is **not** a verified multi-year result or a claim of publication.

## Repository guide

- `research/canonical/` — canonical research decisions and documentation.
- `projects/c011-qct-precision-screen/` — executable analysis and [project-level instructions](projects/c011-qct-precision-screen/README.md).
- `projects/c011-qct-precision-screen/data/manifest.csv` and associated provenance records — source details and hashes for raw HUD workbooks, which are excluded from Git.
- `projects/c011-qct-precision-screen/C011_FINAL_REPRODUCIBILITY_ADJUDICATION.md` — controlling status and limitations (consult the repository's actual path if the file is relocated).

## How to evaluate the work

Start with the [C011 project instructions](projects/c011-qct-precision-screen/README.md), then inspect the frozen protocol, provenance files, tests and final adjudication before interpreting any results. Reproducing one year does not validate all years, and technical completeness should not be confused with peer-reviewed publication.

This public archive documents a research process, including negative findings and explicit stopping decisions. It is not presented as a finished scientific paper.
