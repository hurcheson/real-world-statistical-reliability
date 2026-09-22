---
title: C013 Controlled Execution Protocol — PLACES Temporal Provenance and Interpretability
version: 1.0.0
last_updated: 2026-09-21
status: frozen-before-substantive-execution
candidate: C013
decision: D039
---

# C013 Controlled Execution Protocol

## 1. Protocol status and firewall

This protocol is frozen after the O002-A1 prosecution and before production execution of C013. The prosecution evidence is preserved in `22_C013_PLACES_TEMPORAL_PROSECUTION.md`.

Authorized now:

- archive public CDC release metadata and query manifests;
- build and validate the machine-readable provenance crosswalk;
- independently recode the eligible corpus under the frozen codebook;
- execute the three prespecified case studies and sensitivity analyses;
- produce machine-readable results and an execution adjudication.

Not authorized before the execution gate:

- manuscript, abstract or press-style drafting;
- contacting study authors, CDC or prospective faculty collaborators;
- adding case studies because their results appear favorable;
- treating release differences as estimates of true local health change;
- calling a named paper erroneous without exact model/data reproduction and a fair alternative;
- silently relaxing a stop rule, comparability rule or inclusion criterion.

Protocol amendments must be dated, justified, and committed before the affected result is inspected. Amendments cannot convert an observed failure into a new primary analysis.

## 2. Candidate and contribution

### 2.1 Candidate

> **C013 — release-provenance and temporal-interpretability audit of repeated CDC PLACES/500 Cities estimates.**

### 2.2 Core question

For a published repeated-release analysis, after replacing nominal release time with documented BRFSS source time, removing deterministic carry-forwards, harmonizing measure definitions and geography/population rules, and respecting reported uncertainty, does the study retain the temporal contrast, ordering, hotspot/set classification or decision statement it claims?

### 2.3 Contribution claim permitted if execution succeeds

C013 may claim that repeated PLACES releases contain measure-specific amounts of temporal information and that a reproducible provenance audit can change the admissibility or interpretation of some downstream temporal conclusions while preserving others.

### 2.4 Claims prohibited

C013 may not claim that:

- PLACES is defective or generally unusable;
- all repeated-release analyses are invalid;
- a difference between source waves is true local change;
- marginal confidence-interval overlap is a formal paired difference test;
- CDC's local-trend warning is newly discovered;
- any named analysis is wrong when only a bounded public-archive reproduction is available; or
- the corpus is metaphysically complete beyond the frozen search rules and date.

## 3. Primary estimand and outcome classification

### 3.1 Primary estimand

For eligible work \(i\), let \(C_i\) be its principal temporal claim or decision classification under the published nominal-release analysis and \(C_i^P\) the classification after the complete provenance-aware restriction. The primary estimand is the distribution of transitions

\[
C_i \rightarrow C_i^P,
\]

where \(C_i^P\) is coded as:

1. **retained** — the temporal support and conclusion class remain materially intact;
2. **narrowed** — a defensible temporal statement remains but with fewer waves, weaker resolution or reduced scope;
3. **changed** — direction, timing, rank/set, hotspot or decision classification materially changes;
4. **unsupported by the public archive** — the claimed temporal support is absent after provenance correction; or
5. **non-adjudicable** — essential release, model, weighting, spatial or harmonization information is unavailable.

The classification is about public evidentiary support, not author intent or misconduct.

### 3.2 Secondary estimands

- nominal release count versus distinct source-wave count;
- proportion of adjacent pairs that are exact or near-exact carry-forwards;
- change in slope, endpoint contrast, peak/trough timing or autoregressive support after deduplication;
- Spearman and Kendall rank stability across genuinely distinct source waves;
- Jaccard similarity and churn of prespecified priority sets;
- proportion of unit-level marginal intervals that do not overlap, reported descriptively only;
- comparability-break counts caused by definition, eligibility-population, geography, poststratification or interval-method changes.

## 4. Corpus protocol

### 4.1 Search cutoff

The primary corpus is frozen at **2026-09-21**. One documented update search is allowed immediately before submission if the execution survives. New works found at that update enter an appendix unless they satisfy the original rules and can be coded before the analysis lock without changing case selection.

### 4.2 Search surfaces

- OpenAlex title/abstract discovery;
- PubMed and PubMed Central;
- Crossref DOI metadata;
- publisher full text and supplements where publicly accessible;
- dissertation/repository, preprint and conference-abstract sources;
- CDC release documentation and Socrata catalog metadata;
- backward and forward citation checks from eligible works and nearest methodological ancestors.

### 4.3 Inclusion criteria

A work is eligible if it:

1. uses at least two distinct PLACES/500 Cities releases for an outcome, covariate, index or classification; or
2. explicitly interprets cross-release differences as change, trend, longitudinal association, pre/post effect, persistence, temporal hotspot or projection.

### 4.4 Exclusion criteria

Exclude:

- single-release PLACES outcomes even when another exposure is longitudinal;
- work using PLACES only as a baseline or cross-sectional covariate;
- studies whose temporal outcome comes from another source and PLACES is a single contextual layer;
- agency/method descriptions from the downstream application corpus;
- general estimated-dependent-variable theory from the application corpus;
- duplicate preprint/published versions, retaining the most complete version; and
- title/abstract records whose multi-release use cannot be verified.

### 4.5 Frozen primary corpus

The nine prosecution-eligible works E1–E9 are the starting corpus. Peer-reviewed articles form the primary paper corpus; the conference abstract, preprint and dissertation form the active-work appendix. Eligibility changes require a written rule-based adjudication, not an outcome-based judgment.

### 4.6 Independent coding

Two human coders must independently code eligibility, temporal role, release/source mapping, provenance disclosure, decision language and primary fragility. AI assistance may extract candidate text but does not count as a human coder. Disagreements are adjudicated with reasons preserved. Report raw agreement and an appropriate chance-corrected coefficient when category counts permit.

If a second human coder is unavailable, execution may build the archive and crosswalk but the corpus-level manuscript gate cannot pass.

## 5. Provenance crosswalk

### 5.1 Unit of record

One record per:

`release × Socrata dataset × geography level × measure ID × data-value type × BRFSS source year`.

### 5.2 Required fields

- release year and product name;
- Socrata dataset ID and catalog URL;
- retrieval timestamp, query text and raw-response hash;
- geography level and geography vintage;
- measure ID, display name and exact definition;
- target population and age/sex eligibility;
- data-value type: crude, age adjusted, count or other;
- BRFSS source year or years;
- carried-forward flag and carry-forward predecessor;
- exact-copy percentage on common geographies;
- common-geography count and coverage change;
- poststratification population base;
- confidence-interval method era;
- definition-comparability flag;
- geography/population-comparability flag;
- documentation source and verification note.

### 5.3 Carry-forward classes

- **exact carry-forward:** 100% equality of point estimates and interval bounds on common geographies;
- **revised carry-forward:** same documented source wave with at least 99.5% exact equality and only isolated small revisions;
- **new source wave:** documented source year changes and the file is not an exact/revised carry-forward;
- **ambiguous:** documentation and empirical comparison conflict or source year cannot be resolved.

The 99.5% revised threshold is a file-diagnostic label, not a statistical equivalence claim. Sensitivity analyses must repeat with exact-only classification.

### 5.4 Comparability breaks

A temporal segment must split when any of the following changes materially:

- measure wording or target behavior;
- age/sex/eligibility population;
- geographic boundary/vintage without defensible common-unit linkage;
- 500 Cities versus national PLACES coverage;
- poststratification population basis relevant to the estimand; or
- interval-construction method when interval comparisons are reported.

## 6. Public-data archive and reproducibility

### 6.1 CDC dataset anchors

Tract releases used in the prosecution:

`9z78-nsfp`, `vurf-k5wr`, `rja3-32tc`, `6vp6-wxuq`, `4ai3-zynv`, `373s-ayzu`, `nw2y-v4gm`, `em5e-5hvn`, `ai6z-tcin`, `cwsq-ngmh`.

County releases used as needed:

`dv4u-3x3q`, `pqpp-u99h`, `duw2-7jbt`, `h3ej-a9ec`, `fu4u-a9bh`, `swc5-untb`.

### 6.2 Raw-data rules

- Preserve every API query in a manifest before analysis.
- Save raw responses or immutable content-addressed snapshots when licensing permits.
- Record SHA-256 hashes, row counts, schema and retrieval time.
- Never overwrite a raw snapshot.
- Separate raw, interim, derived and publication-facing outputs.
- A rerun against live data must be labeled as such and compared with the frozen snapshot.

### 6.3 Repository target

Use `projects/c013-places-temporal-provenance/` with:

- `protocol/` — this frozen protocol and amendments;
- `data/manifests/` — query, source and hash manifests;
- `data/raw/` — ignored or content-addressed raw snapshots;
- `data/interim/` — normalized release panels;
- `data/derived/` — crosswalk and case-study panels;
- `src/c013_places/` — reusable ingestion, linkage and audit functions;
- `config/` — release IDs, measures, geographies and case specifications;
- `tests/` — schema, invariant and regression tests;
- `outputs/tables/`, `outputs/figures/`, `outputs/machine/`;
- `docs/coding/` — codebook, dual-coding forms and adjudications; and
- `adjudication/` — final execution verdict and claim–evidence matrix.

## 7. Prespecified case studies

No more than three case studies may enter the primary execution.

### 7.1 Case A — Rahman mammography trajectory

**Role:** primary deterministic pseudo-wave case.

**Population/data:** Kansas and Missouri tracts, `MAMMOUSE`, crude prevalence, releases 2016–2024, common-geography pair restriction.

**Primary tests:**

- release count versus distinct source-wave count;
- exact-copy percentage for every adjacent pair;
- median absolute change and rank stability;
- marginal-interval nonoverlap, descriptive only;
- peak/stability language after one-row-per-source-wave restriction;
- loss of temporal support for annual AR(1) interpretation and projection.

**Fairness boundary:** reproduce the public outcome panel and temporal support, not the complete unavailable Bayesian model.

### 7.2 Case B — Nguyen Washington, DC outcomes

**Role:** within-study positive and negative controls.

**Population/data:** tracts present in every 2016–2021 release; obesity, diabetes, high cholesterol, cancer and poor mental health.

**Primary tests:**

- distinct source-wave count by measure;
- exact copied adjacent pairs;
- release-time versus source-time linear slope;
- endpoint contrast;
- marginal-interval overlap summary;
- classification of which outcomes retain versus lose temporal support.

**Expected falsification value:** the audit fails as a discriminating method if it labels the four annually sourced outcomes as deterministic carry-forwards merely because CDC cautions against local trends.

### 7.3 Case C — Al Qady county colorectal screening

**Role:** bounded pre/post reproducibility and definition-discontinuity case.

**Population/data:** common counties; `COLON_SCREEN`; crude and age-adjusted prevalence; release-pair mappings 2020/2021, 2022/2023 and 2024/2025.

**Primary tests:**

- equality within each two-release period;
- one-observation-per-source-wave versus two-release averaging;
- age-adjusted and crude median contrasts under both natural public-archive mappings;
- target-age definition comparability;
- whether the reported +1.6-point median can be reproduced.

**Fairness boundary:** spatial clusters, SVI gradients and hotspot counts are non-adjudicable without the full release mapping, spatial weights and code. The allowed conclusion is bounded non-reproduction, not error.

Hunyadi remains a corpus-level study, not a fourth primary case. It may replace Case C only through a dated protocol amendment made before its full supplement/code and outcome reconstruction are inspected, and only if the replacement clearly improves reproducibility access.

## 8. Analysis rules

### 8.1 Common geography

All pairwise numerical comparisons use the intersection of valid geographic identifiers. Entry/exit and coverage expansion are reported separately. Crosswalks between geography vintages must be documented; no implicit name-only linkage is permitted when stable IDs differ.

### 8.2 Source-wave deduplication

For each measure/geography/source-year block, retain one canonical release observation. If repeated releases differ slightly, preserve both for revision diagnostics but use the earliest frozen release in the primary one-wave analysis; repeat with the latest release as sensitivity.

### 8.3 Definition harmonization

Primary temporal contrasts require identical measure wording and target population. Definition-changing contrasts are reported separately and cannot support a retained-change classification.

### 8.4 Uncertainty

Marginal confidence intervals may describe published uncertainty and overlap. They cannot be combined as independent repeated estimates because cross-release joint covariance is unavailable. No paired significance test will be fabricated from marginal intervals.

### 8.5 Rank and set stability

Rank analyses report Spearman and Kendall correlations. Policy-set analyses must prespecify the threshold, quantile or top-*k* rule and report Jaccard similarity plus entry/exit counts. Copied-wave rank stability is labeled deterministic.

### 8.6 Missingness and revisions

Report missingness by release, measure and geography. Do not impute PLACES outcomes for primary analyses. Rare file revisions are documented, not silently rounded away.

## 9. Sensitivity suite

Run in this order:

1. common-geography restriction;
2. stable-definition and stable-population restriction;
3. source-year alignment;
4. exact carry-forward removal;
5. exact-plus-revised carry-forward removal;
6. earliest-versus-latest canonical carried release;
7. crude versus age-adjusted comparison where both exist;
8. marginal-interval descriptive check;
9. rank and decision-set stability; and
10. model-boundary classification: exact reproduction, bounded reproduction or non-adjudicable.

The order is fixed so that a later analytic choice cannot conceal an earlier comparability failure.

## 10. Quality-control tests

Minimum automated tests:

- every configured Socrata ID resolves or fails with an explicit archived error;
- expected key fields exist and types are stable;
- `release × measure × geography × data-value-type` keys are unique after documented deduplication;
- source years fall within documented release history;
- exact-copy classifications recompute from raw point estimates and bounds;
- common-geography counts match case-study output;
- copied pairs have zero median change and rank correlation one when exactly equal;
- definition-changing contrasts cannot be labeled retained;
- no result table reports a formal paired *p*-value derived only from marginal CIs;
- all tables trace to a configuration, raw-query hash and code commit.

Two clean runs from the same frozen inputs must produce byte-identical machine-readable outputs, excluding timestamp-only metadata.

## 11. Execution stages and gates

### Stage 0 — provenance archive and crosswalk

Deliver:

- source/query manifest;
- frozen raw hashes;
- normalized release schema;
- machine-readable provenance crosswalk;
- schema/invariant tests; and
- discrepancy log against CDC documentation.

**Stop:** if source-year mapping for the primary measures cannot be resolved or the archive cannot be reproduced from public sources.

### Stage 1 — corpus recoding

Deliver:

- frozen codebook;
- independent dual-human coding;
- disagreement/adjudication log;
- final inclusion/exclusion flow; and
- corpus table linked to evidence passages.

**Stop:** corpus-level claims cannot proceed without a second human coder.

### Stage 2 — controlled case studies

Deliver the three configured reproductions and complete sensitivity suite. All unavailable model details are marked and bounded.

**Stop:** do not substitute a new case after observing an unfavorable result.

### Stage 3 — claim adjudication

For every proposed claim, produce:

- evidence;
- exact reproducibility level;
- limitation;
- counterexample/negative control; and
- permitted wording.

### Stage 4 — paper gate

Advance to manuscript design only if all of the following hold:

1. the crosswalk is independently verifiable and machine-readable;
2. at least two measure families show consequential source-wave/carry-forward effects;
3. at least one contrasting outcome survives the deterministic-copy audit;
4. at least one downstream conclusion materially narrows, changes or becomes unsupported after the prespecified restriction;
5. the contribution remains distinct after the one-time literature update;
6. the central result does not depend on claiming true local change;
7. corpus coding meets the independent-human requirement; and
8. all primary outputs rerun deterministically from frozen inputs.

If any of 1, 3, 5, 6, 7 or 8 fails, park or kill C013. If only 2 or 4 fails, kill the first-paper claim because the audit lacks consequentiality.

## 12. Final execution verdict

The execution adjudication must return exactly one of:

- **C013 — ADVANCE TO MANUSCRIPT DESIGN**, or
- **C013 — PARK / NO-GO FOR FIRST PAPER UNDER EXECUTION EVIDENCE**.

The adjudication must not be replaced with an indefinite “promising” status.

## 13. Frozen immediate action

The immediate authorized action after canonical v0.28.0 is:

> Build Stage 0: the content-addressed public-data archive, query manifest, machine-readable provenance crosswalk and automated validation tests. Do not draft the manuscript or expand the case-study slate.

