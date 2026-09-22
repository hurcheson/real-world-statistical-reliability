# C013 Stage 1 Frozen Corpus-Coding Codebook

**Version:** 1.0.0  
**Frozen:** 2026-09-21, before independent Stage 1 coding  
**Protocol:** C013 Controlled Execution Protocol v1.0.0  
**Protocol SHA-256:** `fa87dc628428b9c9b613f20f2fa80769fe16d153e1f749962fc32b2ceb126629`  
**Status:** preparation complete; no Stage 1 coding judgments entered

## 1. Purpose and firewall

This codebook operationalizes Stage 1 of the frozen C013 protocol. It is deliberately neutral with respect to the earlier prosecution's paper-specific coding. Coder A and Coder B must not inspect the prior E1–E9 coding table, each other's forms, or any adjudicated Stage 1 result until both independent forms are locked.

The coding target is the **published/publicly accessible evidentiary record of each work**, not author intent, competence, or misconduct.

The Stage 1 coders do **not** decide whether C013 advances to manuscript design. They independently code corpus eligibility and the prespecified descriptive dimensions. Case-study execution remains Stage 2.

## 2. Evidence hierarchy and access

Use the most complete lawful version available in this order:

1. final peer-reviewed full text plus supplements;
2. repository-author manuscript or other lawful full text;
3. complete conference abstract/preprint/dissertation;
4. complete indexed abstract;
5. metadata record only.

Record the actual level used in `evidence_access`. **Not accessible is not the same as not reported.** If access prevents a determination, use the explicit access-limited category instead of inferring absence.

Prefer section/page/table/figure locations plus a paraphrase. If a direct quotation is needed, keep it brief.

## 3. Eligibility

### Inclusion

Code **eligible** if either condition is directly verified:

- **IC1 — multirelease use:** the work uses at least two distinct PLACES/500 Cities releases for an outcome, covariate, index, or classification; or
- **IC2 — cross-release interpretation:** the work explicitly interprets cross-release differences as change, trend, longitudinal association, pre/post effect, persistence, temporal hotspot, or projection.

Code `eligibility_basis` as `IC1_multirelease_use`, `IC2_crossrelease_interpretation`, or `both`.

### Exclusion

Use one rule-based exclusion reason:

- `single_release`
- `baseline_or_cross_sectional_only`
- `temporal_outcome_from_other_source`
- `agency_or_methods_description`
- `general_theory`
- `duplicate_version`
- `multirelease_use_unverified`
- `other`

Use `uncertain_access` when the available record is too incomplete to verify the rule, and `uncertain_scope` when the text is available but the PLACES/500 Cities temporal role cannot be resolved.

## 4. Temporal role

Choose exactly one `temporal_role_primary`:

- `two_wave_change` — a contrast between two time points/releases;
- `multiwave_trend` — three or more time points used to describe or estimate a trajectory;
- `pre_post_change` — explicit before/after or intervention/pandemic-period contrast;
- `longitudinal_association` — repeated PLACES outcomes/covariates enter longitudinal association models;
- `persistence_or_autoregression` — temporal persistence, lag, AR structure, or related dependence is central;
- `rank_hotspot_or_set` — time-varying rank, hotspot, cluster, priority set, or membership is central;
- `projection_or_forecast` — repeated releases support forward projection;
- `composite_index_temporal` — repeated releases are combined into a time-indexed composite/index;
- `contextual_temporal_layer` — PLACES varies over nominal time but is not itself the formal time-series outcome;
- `other`;
- `not_assessable`.

Record secondary roles with `|` separators only when substantively present.

## 5. Release/source mapping

Code only what the work reports, then separately use the frozen Stage 0 crosswalk to evaluate mapping completeness. Do not silently replace the paper's labels with crosswalk labels.

Record:

- product reported: 500 Cities, PLACES, both, other, unclear;
- nominal time labels verbatim;
- nominal release count if determinable;
- release years reported;
- Socrata dataset IDs reported;
- BRFSS/source years reported;
- measure names/IDs;
- `year_semantics`: source year, release year, mixed/measure-specific, unlabeled year, unclear, or not assessable.

`source_mapping_completeness`:

- **complete** — the paper plus cited release information permits the temporal PLACES observations to be mapped to source years for the measures used;
- **partial** — some but not all release/source mapping is recoverable;
- **absent** — the accessible work provides nominal time labels but no usable source-year/release mapping;
- **unclear_due_access** — access limits prevent the judgment.

The Stage 0 crosswalk is a neutral reference for whether a stated release/source relation is resolvable. Coders must not use prior paper-specific C013 conclusions.

## 6. Provenance disclosure

First code the objective disclosure checklist (`yes/no/unclear/not_assessable`):

- dataset/product named;
- release years named;
- dataset IDs named;
- BRFSS/source years named;
- model-based-estimate status acknowledged;
- carry-forward/measure rotation acknowledged;
- definition changes acknowledged where relevant;
- geography/population changes acknowledged where relevant;
- uncertainty/dependence limitation acknowledged where relevant.

Then assign one overall category:

- **none** — PLACES/500 Cities provenance is effectively unspecified;
- **minimal** — dataset/product is named but temporal provenance is not operationally described;
- **partial** — some release/source or modeling provenance is reported, but the temporal panel cannot be reconstructed from the report;
- **substantial** — most temporal provenance needed for interpretation is explicit, with only limited gaps;
- **complete_reconstructible** — the accessible work identifies the release/source/measure mapping sufficiently for an independent reader to reconstruct the temporal PLACES panel;
- **not_assessable_access** — access limits prevent assessment.

Do not penalize a paper for failing to discuss a comparability issue that is demonstrably irrelevant to its measures/time span. Explain relevance in the note.

## 7. Decision-facing language

Code the strongest directly supported level:

1. `none` — no temporal substantive conclusion;
2. `descriptive_scientific` — reports temporal pattern/association without action implication;
3. `interpretive_implication` — interprets the pattern as substantively meaningful;
4. `action_or_planning` — links findings to planning, targeting, outreach, surveillance, or action;
5. `allocation_or_prioritization` — explicitly supports resource allocation, ranking, prioritization, or selection;
6. `policy_or_intervention` — explicitly recommends or evaluates policy/intervention decisions;
7. `not_assessable_access`.

Also record audience and whether explicit causal language is present. This is a textual classification, not an assessment of whether the recommendation is good.

## 8. Primary fragility

The primary fragility is the **single provenance-aware issue most capable of altering the admissibility or interpretation of the work's principal temporal PLACES claim**, based on the accessible paper and frozen Stage 0 reference. It is not a verdict that the work is wrong.

Allowed categories:

- `none_identified`
- `release_source_misalignment`
- `carry_forward_pseudowaves`
- `mixed_source_year_composite`
- `definition_noncomparability`
- `geography_population_noncomparability`
- `uncertainty_dependence`
- `rank_or_set_instability`
- `temporal_model_support`
- `reproducibility_information_gap`
- `multiple_no_single_primary`
- `not_assessable_access`

If more than one issue is present, choose the one that first breaks or most directly changes the principal temporal claim under the protocol's fixed restriction order. Record the rest in `secondary_fragilities`. If no single issue can be selected without running a Stage 2 reproduction, use `multiple_no_single_primary` and explain.

## 9. Coder confidence

- **high** — evidence is explicit and category boundary is clear;
- **moderate** — evidence supports the code but interpretation is required;
- **low** — incomplete access or material ambiguity remains.

Confidence does not override the substantive category.

## 10. Independence and lock

Each coder completes all E1–E9 rows independently. No discussion of individual codes is allowed before both forms are complete.

Before comparison:

1. set every row's `coding_status` to `complete_locked`;
2. ensure all nine work IDs are present exactly once;
3. run the Stage 1 validator;
4. compute and record the SHA-256 of each completed CSV;
5. do not edit a locked file after viewing the other coder's codes. Any correction after lock must be a separately logged amendment preserving the original hash.

## 11. Agreement analysis

Report field-specific reliability; do not average fields into a single score.

- eligibility: raw agreement + Cohen's kappa when estimable;
- temporal role and primary fragility: raw agreement + Cohen's kappa when at least two categories are represented;
- source-mapping completeness, provenance disclosure, and decision-language level: raw agreement + linearly weighted Cohen's kappa when ordinal categories are estimable;
- release years, source years, and dataset IDs: exact-set agreement descriptively;
- access-limited rows are reported separately and excluded from an ordinal kappa when the access category is nonordinal.

If kappa is not estimable because one or both coders use only one category, report raw agreement and the reason kappa is undefined. Do not substitute an arbitrary coefficient.

## 12. Adjudication

Only after both independent forms are locked may the coders compare results.

Every disagreement must produce an adjudication row recording:

- work ID and field;
- Coder A value;
- Coder B value;
- evidence considered;
- consensus value or `unresolved`;
- reason for the decision;
- whether the decision changed corpus inclusion.

Primary adjudication is joint consensus by the two coders. If they cannot reach consensus, leave the field unresolved or obtain a third independent human adjudicator. Coder A may not unilaterally overwrite Coder B.

## 13. Stage 1 completion boundary

Stage 1 is complete only after:

- both nine-work forms are independently locked;
- agreement statistics are generated;
- all disagreements are adjudicated or explicitly unresolved;
- the final inclusion/exclusion flow is generated;
- the corpus table links every retained coding decision to evidence locations.

No manuscript or abstract drafting is authorized by Stage 1 preparation or by a partially completed coding exercise.
