---
title: Canonical Source Update Protocol
version: 0.3.0
last_updated: 2026-09-08
status: active
---

# Canonical Source Update Protocol

## Goal

Keep the ChatGPT Project useful as a compact research memory without filling it with duplicate files or stale versions.

## Principle

Project-source Markdown files are **living canonical documents**, not an immutable Git history.

Detailed version history will eventually belong in Git.

## File metadata

Every canonical file should contain:

- `version`;
- `last_updated`;
- `status`.

Use semantic-ish versions pragmatically:

- `0.1.0` — initial canonical draft;
- `0.2.0` — material content change;
- `0.2.1` — small correction;
- `1.0.0` — stable enough to anchor an execution project.

## When to update

Do **not** update files after every conversational thought.

Update after a material event such as:

- candidate verdict changes;
- new research direction is chosen;
- deep literature prosecution completes;
- a field-map section materially changes;
- a methodological lesson changes future procedure;
- a project is promoted to execution;
- an important factual correction is made.

Minor exploratory discussion remains in chat until it earns promotion into canonical state.

## Project-source replacement workflow

Because uploaded Project files should be treated as reference sources rather than a version-control system:

1. Ask ChatGPT to regenerate the **complete revised canonical file**, not merely a patch.
2. Review the revised file.
3. Download/save the revised file.
4. In Project Sources, delete the old canonical file.
5. Upload the revised file using the **same canonical filename**.
6. Confirm the header has the new version and date.
7. Keep only one active Project-source copy of each canonical filename.

Do not keep `FIELD_MAP_v2.md`, `FIELD_MAP_v3.md`, etc. in Project Sources unless there is a special reason. That wastes source capacity and creates ambiguity about which file is authoritative.

## Change log inside a file

For important files, optionally add a compact section:

```markdown
## Change log

### 0.3.0 — 2026-09-08
- Applied D034: resolved the repository name to `real-world-statistical-reliability` and froze the baseline-before-confirmation Git sequence for C011.

### 0.2.0 — 2026-09-15
- Added calibration/shift branch.
- Reclassified candidate C004 from IDEA to PROSECUTION.
```

Keep it short. Git will later preserve full diffs.

## Source-of-truth rule

At any point:

- the Project chat history is the **raw provenance**;
- the canonical Markdown files are the **compressed current state**;
- GitHub, once created, becomes the **durable version history and execution record**.

## Avoid conflicting state

If a canonical file and an older chat disagree:

1. prefer the most recently updated canonical file for current state;
2. inspect the decision ledger for why;
3. use the chat only to reconstruct provenance;
4. if uncertain, explicitly flag the inconsistency before proceeding.

## Batch-update rule

After a deep research iteration, update all affected canonical files in one batch.

Example:

A candidate moves from SCREENING to KILLED.

Update:

- `03_DECISION_LEDGER.md`;
- `04_CANDIDATE_REGISTRY.md`;
- `02_RESEARCH_PRINCIPLES_AND_LESSONS.md` if a new general lesson emerged;
- `09_OPEN_QUESTIONS.md` if a new parked lead emerged.

This keeps state coherent.

## Citation/evidence rule

Canonical research claims should increasingly link to primary sources or a structured evidence ledger.

Before any claim is used in:

- manuscript;
- proposal;
- thesis;
- presentation;
- faculty pitch;

re-verify it against the current primary source.


## Project source-cap consolidation rule

The ChatGPT Project has a hard source-count ceiling. When the canonical record approaches that ceiling, **do not create another standalone Markdown dossier by default**.

Instead:

1. identify a coherent historical chain or thematic family whose separate filenames no longer need independent retrieval;
2. merge those records into an existing canonical composite file, preserving enough provenance that no scientific decision or evidence trail is lost;
3. record the retired filenames and their destination in `MANIFEST.json` and the README;
4. update active cross-references to the surviving canonical path;
5. remove the retired files from Project Sources only after the consolidated replacement has been saved/uploaded;
6. use the newly freed source slots only for genuinely distinct future canonical objects.

Prefer merging completed **generation → prosecution → gate** chains over merging foundational files such as the Charter, Decision Ledger, Candidate Registry, Principles, Update Protocol or Reference Ledger.

**Current application (D027):** the former files 20–22 (D024 and the OF-39 prosecution/exact gate) are preserved inside `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md` and retired as separate canonical sources. This frees three Project-source slots once the source replacements are applied.

## Transition to GitHub

D034 resolves the previously deferred repository transition for the first surviving project.

Initialize the program repository as **`real-world-statistical-reliability`**. Preserve the canonical research memory under `research/canonical/`, and place the first execution project under `projects/c011-qct-precision-screen/`.

Transition sequence:

1. commit the complete canonical snapshot plus `20_C011_EXECUTION_PROTOCOL.md`;
2. create the C011 project skeleton, locked environment and tests;
3. implement the already-seen 2026 replay as a regression fixture and require zero official-QCT mismatches;
4. only after baseline tests pass, add/acquire 2016–2025 historical sources and inspect confirmatory outputs;
5. use Git commits/branches for durable execution history and protocol amendments;
6. periodically export major GitHub-state summaries back into the ChatGPT Project.

Do not commit raw public XLSX binaries to ordinary Git history by default. Commit source URLs, retrieval metadata and cryptographic hashes; use deterministic acquisition/registration scripts.

The Project remains the conversational research room; Git becomes the reproducible laboratory.

## AI startup rule

A future AI session should begin by reading:

1. `00_RESEARCH_CHARTER.md`;
2. `03_DECISION_LEDGER.md`;
3. `04_CANDIDATE_REGISTRY.md`;
4. `02_RESEARCH_PRINCIPLES_AND_LESSONS.md`;
5. relevant field/literature files;
6. when C011 execution is active, `20_C011_EXECUTION_PROTOCOL.md` before touching historical outcomes or analysis code.

Only then should it generate/prosecute new candidates or continue execution under the applicable frozen protocol.

## Change log

### 0.2.0 — 2026-09-08

- Added the Project source-cap consolidation rule and recorded the D027 merge of files 20–22 into file 18.
