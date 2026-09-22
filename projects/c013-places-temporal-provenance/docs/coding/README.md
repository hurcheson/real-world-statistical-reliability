# C013 Stage 1 Coding Workspace

**Current status:** PREPARED — INDEPENDENT CODING NOT YET STARTED  
**Coder A:** Hurcheson  
**Coder B:** to be recruited  
**Frozen corpus:** E1–E9  
**Protocol SHA-256:** `fa87dc628428b9c9b613f20f2fa80769fe16d153e1f749962fc32b2ceb126629`

This directory is the neutral Stage 1 packet. It intentionally excludes the prosecution's prior E1–E9 coding results.

## What each coder receives

- `C013_STAGE1_CODEBOOK.md`
- `STAGE1_CORPUS_REGISTRY.json`
- `STAGE1_SOURCE_MANIFEST.json`
- their own CSV form only

Coder A uses `CODER_A_FORM.csv`. Coder B uses `CODER_B_FORM.csv`.

## Independence rules

Do not open the other coder's form. Do not discuss individual papers or classifications until both forms are locked. Do not inspect the paper-specific coding table in the earlier C013 prosecution before lock. The frozen Stage 0 provenance crosswalk may be used because it is a dataset-level reference, not a paper-specific answer key.

## Coding workflow

For each E1–E9 work, read the most complete lawful source available, record the evidence locations, complete every required field, and mark access limitations explicitly. Finish all nine works before comparison.

When all nine rows are complete, set `coding_status=complete_locked`, run:

`python scripts/validate_stage1_forms.py docs/coding/CODER_A_FORM.csv`

or the corresponding Coder B path from the C013 project root.

The completed form must then be hashed with SHA-256 before either coder sees the other's file.

## What happens after both locks

The analysis layer will compute raw agreement and the prespecified chance-corrected coefficients, create a disagreement matrix, and populate `ADJUDICATION_TEMPLATE.csv`. The two humans then adjudicate disagreements with reasons preserved.

**Do not start Stage 2 case-study execution from this folder.**
