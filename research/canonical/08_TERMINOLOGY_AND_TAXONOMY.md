---
title: Terminology and Taxonomy
version: 0.6.0
last_updated: 2026-09-07
status: active
---

# Terminology and Taxonomy

Different communities can study similar reliability problems under different names. This file exists to prevent false novelty caused by terminology mismatch.

## Umbrella concept

**Real-world model reliability**

A model is reliable when its predictions, uncertainty, calibration, and decision utility remain trustworthy under the conditions in which it is actually used.

---

# 1. Distribution-shift family

## Dataset shift / distribution shift

General condition:

\[
P_{source}(X,Y) \neq P_{target}(X,Y).
\]

This notation is useful but can be too coarse for EHR data because the **recording process** can itself change.

## Covariate shift

Typically:

\[
P_s(X) \neq P_t(X)
\]

while:

\[
P_s(Y\mid X) = P_t(Y\mid X).
\]

Do not call a source/target problem “covariate shift” unless the conditional-stability assumption is scientifically defensible.

## Label / prior shift

Typically:

\[
P_s(Y) \neq P_t(Y)
\]

with assumptions on stability of \(P(X\mid Y)\).

## Concept / conditional shift

\[
P_s(Y\mid X) \neq P_t(Y\mid X).
\]

## Temporal drift

Distribution or model-performance change across time.

## Site / geographic shift

Distribution change across hospitals, regions, health systems, units, countries or other environments.

## Subpopulation shift

Change in the proportions or behavior of subgroups/environments. The modern robust-ML literature uses this more specifically than generic “site shift.”

---

# 2. Transportability and external validation

## External validation

Evaluation of an existing model in data meaningfully distinct from its development data.

Forms include:

- geographic/site validation;
- temporal validation;
- domain/environment validation;
- setting/population validation.

## Generalizability / transportability

Related terms include:

- external validity;
- external validation;
- model transport;
- target-population performance;
- cross-site generalization.

**Warning:** causal-inference and prediction-model communities use “transportability” differently. Always specify whether the target is an outcome distribution, causal estimand, or predictive-performance property.

---

# 3. Measurement and observation-process terminology

This section is central after field-mapping pass 1.

## Measurement process

The mechanism by which a clinical construct is converted into a recorded predictor value.

May include:

- instrument/assay;
- units;
- thresholds/detection limits;
- abstraction/coding;
- timing relative to clinical events;
- frequency;
- preprocessing or aggregation.

## Predictor measurement heterogeneity

The same intended predictor is measured differently across settings.

This can change model calibration/performance even when the clinical construct has the same meaning [Reference Ledger: R016–R017].

## Observation process

The mechanism determining **whether, when, and how often** a patient or variable is observed/recorded.

Examples:

- healthcare visits;
- laboratory ordering;
- vital-sign charting;
- monitoring frequency;
- clinician documentation;
- device/interface availability;
- data latency.

Let \(R\) denote observation/recording information. A useful schematic is:

\[
P(R\mid Z,X,Y,H),
\]

where \(Z\) is patient state and \(H\) can include site/workflow history.

## Observation-process shift

Working project definition:

> A change between source and target environments in the mechanism governing whether, when, how often, or through which workflow/infrastructure variables are recorded.

Schematically:

\[
P_s(R\mid Z,X,Y,H) \neq P_t(R\mid Z,X,Y,H).
\]

This is broader than a simple change in missing-data rate.

## Measurement-process shift

Working umbrella term for changes in either:

1. **how a construct is measured**; and/or
2. **whether/when/how frequently it is observed**.

Use the narrower term when possible:

- **measurement-procedure shift** for changed instruments/definitions/units;
- **observation-process shift** for changed presence/timing/frequency/availability.

## Informative presence

Healthcare-system inclusion/contact itself is associated with patient characteristics or outcomes.

## Informative observation

The fact/timing/frequency that a variable is observed carries information about patient state/outcome.

## Clinical presence

Recent terminology for the interaction between the patient and healthcare system reflected through observation timing and missingness. Jeanselme et al. use **clinical presence shift** for changes in this process across settings [R026].

**Novelty warning:** “clinical presence shift” is therefore not available as a new term for this project.

## Workflow signal / process signal

Project shorthand for predictive information carried by healthcare processes rather than stable biology alone, e.g. test-order counts or charting intensity.

Use cautiously: workflow and physiology can be entangled.

## Data-interface availability

Whether a database receives a data type may depend on local technical interfaces. eICU documentation makes this especially relevant [R043].

A missing database field can therefore mean:

- not clinically measured;
- measured but not interfaced;
- measured elsewhere/not captured;
- not applicable;
- structurally unavailable.

These mechanisms should not be collapsed without evidence.

---

# 4. Missingness terminology

## Classical missingness mechanisms

- MCAR;
- MAR;
- MNAR / non-ignorable missingness.

## Missingness pattern

Which variables are missing for an observation/patient/time point.

## Missingness rate

Marginal frequency of missing values. A rate change alone does not identify a mechanism change.

## Missingness shift

Project working definition:

> The distribution or mechanism of missingness differs between development and target environments.

Potential forms include:

- changed marginal missingness rate;
- changed variable-specific missingness;
- changed correlation among missingness indicators;
- changed dependence of missingness on observed variables;
- changed dependence on unobserved values/outcomes;
- changed structural availability because of workflow/infrastructure.

Rockenschaub et al. explicitly distinguish ignorable and non-ignorable missingness shifts [R024].

## Deployment-compatible missing-data handling

Validation missing-data handling should reflect the strategy that will be available when the model is applied to new individuals [R018–R020].

This is distinct from choosing an imputation method solely to recover associations or population parameters.

---

# 5. Reliability outcomes

## Discrimination

Ability to rank/separate outcomes.

Common metrics:

- AUROC;
- AUPRC.

## Calibration

Agreement between predicted probabilities and observed outcome frequencies.

Key objects:

- calibration-in-the-large / intercept;
- calibration slope;
- flexible calibration curve;
- subgroup calibration;
- recalibration.

AUC/discrimination and calibration are distinct.

## Proper scoring rules

Examples:

- Brier score;
- log score/log loss.

These combine aspects of calibration/refinement but should not replace explicit calibration plots/parameters when absolute-risk use matters.

## Clinical utility

Performance in decision terms rather than prediction accuracy alone.

Examples:

- decision-curve analysis;
- net benefit;
- threshold-specific utility/cost.

## Reliability degradation

For metric \(M\):

\[
\Delta M = M_{target} - M_{source}.
\]

Interpret direction according to metric; a single scalar should not replace a multidimensional external-validation profile.

## Transportability penalty

**Provisional project term**, not yet a standard estimand.

Potential future meaning:

> loss of target reliability associated with dependence on a source-specific process feature or shift mechanism.

Do not use as formal terminology until C008 defines it mathematically and checks prior art.

---

# 6. Model updating

Related terms:

- recalibration;
- intercept update;
- logistic recalibration;
- model revision;
- refitting;
- dynamic updating;
- continuous updating;
- transfer learning;
- domain adaptation.

Important distinction:

**Detecting shift** does not determine the correct **update action**.

Different failure mechanisms may justify different actions:

- base-rate change → possibly intercept recalibration;
- scale/relationship change → slope/full recalibration or refit;
- invalid workflow feature → feature removal/redevelopment may be required;
- unsupported target domain → abstention/non-use may be safer than updating.

---

# 7. Uncertainty terminology

Related concepts:

- aleatoric uncertainty;
- epistemic uncertainty;
- prediction intervals;
- credible intervals;
- conformal prediction;
- coverage;
- weighted conformal prediction;
- selective prediction;
- abstention;
- out-of-distribution detection.

**Shift warning:** standard conformal guarantees rely on exchangeability; covariate-shift variants add specific assumptions [R034–R036].

---

# 8. Heterogeneity and fairness

Related concepts:

- subgroup performance;
- subgroup calibration;
- subpopulation shift;
- fairness transfer;
- intersectional evaluation;
- site-by-subgroup interaction;
- worst-group performance.

Overall external performance can hide subgroup failure, but subgroup analyses require adequate sample size and careful multiplicity control.

---

# 9. Shift attribution terminology

## Shift detection

Evidence that source and target distributions differ.

## Shift characterization

Description of **how** they differ.

## Shift attribution

A stronger claim that a particular shift mechanism accounts for some reliability change.

### Warning

Attribution may be:

- causal;
- decomposition-based;
- perturbational/stress-test based;
- descriptive.

Never use “caused by observation-process shift” if the design only demonstrates association with a site difference.

## Controlled stress test

A prespecified intervention/perturbation to the data-generating or recording representation intended to evaluate sensitivity while holding other elements as fixed as possible.

Examples might include policy-motivated changes to measurement frequency or variable availability.

Random masking is not automatically a realistic observation-process stress test.

---

# 10. Provenance and harmonization

## Data provenance

Information about where, when, why and through what process a value entered the dataset.

For C008, provenance can be part of the signal needed to study reliability.

## Harmonization

Mapping heterogeneous source data into common variables/schemas.

Harmonization is essential for multi-database analysis, but it can also remove distinctions in measurement definitions or collection processes.

**Project inference:** when measurement-process shift is the object of study, preserve both harmonized analysis variables and source-specific provenance metadata.

---

# Research warning

Never infer a gap from a phrase that produces few search results.

Before declaring novelty, search the **underlying statistical object** using terminology from adjacent disciplines, including:

- predictor measurement heterogeneity;
- missing predictors at external validation;
- informative presence/observation;
- clinical presence shift;
- missingness shift;
- context-of-use shift;
- robustness/stability analysis;
- workflow/data-quality drift;
- model transportability/generalizability.

---


# Active taxonomy — survey data integration / nonprobability inference

The earlier ML-reliability terminology remains historical/secondary. For the active first-project neighborhood use the following terms precisely.

## Probability sample

A sample selected through a known probability design with nonzero inclusion probabilities, allowing design-based finite-population inference under the stated design/nonresponse adjustments.

## Nonprobability sample (NPS)

A sample whose population-unit participation/inclusion probabilities are unknown by design — e.g. opt-in panels, convenience samples or some administrative/digital sources. Large `n` does not make it representative.

## Probability/reference sample

A probability sample used to provide representative auxiliary information about the target population when adjusting or integrating a nonprobability sample.

## Finite-population inference

Inference about fixed population quantities such as totals, means, proportions or finite-population distributions, where sampling/design mechanisms are part of the inferential basis.

## Auxiliary / adjustment variable

A covariate `X` used to explain nonprobability participation, calibrate weights, predict missing study outcomes, improve efficiency or diagnose representativeness.

For C009, distinguish the **target/latent construct** `X` from source-specific observed versions `X_A*` and `X_B*`.

## Quasi-randomization

An inferential framework that models nonprobability participation as if generated by an underlying stochastic mechanism and estimates participation/propensity probabilities using reference information.

## Pseudo-weight

An estimated weight for a nonprobability unit, often based on an estimated participation probability or calibration equation. It is not a design weight arising from a known probability sample design.

## Calibration weighting

Choose weights so weighted auxiliary totals/moments in the sample equal reference/population totals/moments. For P/NPS integration, calibration validity depends on the reference information and the meaning/quality of the calibration variables.

## Mass imputation

Fit an outcome model using the nonprobability source and impute/predict study outcomes for units in the probability sample, under a transportability/ignorability condition.

## Doubly robust (DR) integration

An estimator combining a participation/propensity model and an outcome model, consistent if at least one of the required model components is correctly specified under the surrounding identifying assumptions.

**Caution:** DR does not mean robust to every data defect; in particular, it need not protect against noncommensurate measurement of the shared variables used by both models.

## Ignorable participation / selection at random

A condition of the form

`P(B=1 | X,Y) = P(B=1 | X)`

so nonprobability participation does not depend on `Y` after conditioning on `X`. Analogous to MAR. Generally unverifiable from the NPS alone.

## Nonignorable participation

Selection into the nonprobability sample still depends on the study variable or unobserved factors after conditioning on available auxiliaries.

## Positivity / overlap

For relevant covariate profiles, there must be adequate probability of appearing in the nonprobability source. Deterministic undercoverage is a structural violation.

## Undercoverage

A portion of the target population has absent or effectively zero representation in the available source. Distinguish stochastic low propensity from deterministic absence.

## Measurement equivalence

The same construct has comparable measurement properties across groups, modes or data sources. It is stronger than merely sharing a variable name or category label.

## Harmonization

Operational/statistical transformation of source variables into a common definition/coding. Harmonization can reduce obvious incompatibility but does **not** guarantee measurement equivalence or remove residual error.

## Cross-source auxiliary-scale mismatch

Current program term for narrowed C009: the probability/reference source and the nonprobability source encode a nominally shared **adjustment variable** through different measurement processes, so the reference benchmark may not be the target benchmark for the NPS measurement scale.

This is narrower than generic cross-source measurement error. It concerns the calibration/participation-adjustment interface.

## Differential measurement error across sources

Measurement error whose distribution/mechanism differs by source. This is more precise than generic measurement error when `X_A*` and `X_B*` have different sensitivity/specificity, variance, bias, coding or mode effects.

## Bridge sample

A source or subsample deliberately connecting measurement systems or data sources. A bridge sample must be described by **what it actually observes and what target population it represents**.

A bridge that only measures two fallible versions of a binary construct on the same units does **not** automatically identify the latent construct or both measurement-error mechanisms. A representative bridge that administers the NPS measurement protocol can identify the target benchmark on the NPS scale even without gold-standard `X`.

## Validation sample

A source/subsample containing sufficiently informative reference measurements or design information to identify the measurement-error parameters required by the analysis. A gold-standard `X` plus source-specific measurements is one example.

Do not use “bridge” and “validation” as synonyms.

## Sensitivity analysis

Quantify how target inference changes across a scientifically plausible range of unverifiable selection or measurement parameters. Sensitivity analysis is an inferential result, not a fallback to vague caveats.

## Safe / selective borrowing; test-and-pool

Use nonprobability information only when evidence supports sufficient comparability; otherwise retain a probability-only estimator. Distinguish from always-pool DR estimators.

## Data defect correlation (DDC)

A framework for representing how outcome values correlate with inclusion/response indicators, emphasizing that large samples can still have large bias when selection is outcome-related.

## Latent response validity / quality (`Q`)

An unobserved analysis-specific state representing whether a respondent's answers are sufficiently valid for the inferential target. It is not assumed to be a universal personality trait or a single objective truth across all survey questions.

Use this term cautiously: most real studies observe **signals of quality**, not `Q` itself.

## Response-quality screen (`C`)

An observed rule, classifier or threshold that determines whether a respondent is retained for analysis. Examples include attention/trap checks, speeding/straightlining rules, fraud-detection systems or identity/record matching.

For C010 notation, `C=1` means the case passes/is retained.

## Post-filter selection

The effective selection mechanism after both original participation and quality filtering. For a nonprobability survey, the retained analytic sample is characterized by `S=1,C=1`, not by `S=1` alone.

This term emphasizes that filtering changes who remains in the sample and can therefore change representativeness.

## False-positive exclusion

A valid/sufficiently high-quality case is incorrectly failed by the screen (`Q=1,C=0`) and removed. Its primary inferential risk is not retained measurement error but induced selection, loss of overlap and variance inflation.

## False-negative retention

A problematic/invalid case incorrectly passes the screen (`Q=0,C=1`) and remains. Its primary inferential risk is retained response contamination, potentially combined with selection effects.

## Recalibration after filtering

Re-estimating survey weights/calibration weights using only the retained `S=1,C=1` cases so their observed adjustment-variable distribution matches target benchmarks.

Recalibration does not guarantee removal of filter-induced selection bias unless the retained sample is conditionally representative for the target estimand given the calibration information.

## Inferentially targeted screening threshold

A screening cutoff chosen to optimize or control downstream estimand error/robustness rather than respondent-level classification accuracy alone. The relevant tradeoff can include retained contamination, false-positive selection, overlap, weight variability and sampling variance.

## Selection-mechanism drift

A change across survey waves in the conditional process determining inclusion/participation in the nonprobability sample, e.g. a change in `P(S_t=1 | X_t,Y_t,...)` or in the subset of variables that meaningfully predicts participation.

Do not infer selection-mechanism drift merely because weighted NPS estimates change over time; genuine population change, measurement change and recruitment/vendor changes are alternative explanations.

## Recurring hybrid P/NPS survey

A repeated survey program that fields probability and nonprobability components in the same or comparable waves and combines them for estimation. Side-by-side probability data can serve as an empirical anchor for diagnosing wave-specific NPS selection differences.

## Probability/reference anchor wave

A wave in a repeated NPS program for which a defensible probability/reference sample is available with sufficient common variables to evaluate or re-estimate the participation adjustment.

An **intermittent-anchor design** has NPS observations on more waves than it has probability/reference anchors. Inference between anchors requires explicit temporal assumptions; the label does not itself imply identifiability.

## Change log

### 0.6.0 — 2026-09-07

- Added selection-mechanism drift, recurring hybrid P/NPS survey and probability/reference anchor-wave terminology from OF-22 triage.
- Added the warning that observed temporal change does not by itself identify participation drift.

### 0.5.0 — 2026-09-07

- Added C010 terminology: latent response validity, response-quality screen, post-filter selection, false-positive exclusion, false-negative retention, recalibration after filtering, and inferentially targeted screening threshold.

### 0.4.0 — 2026-09-07

- Narrowed the C009 term to cross-source auxiliary-scale mismatch.
- Separated bridge samples from validation samples and recorded the stage-1 identification correction.

### 0.3.0 — 2026-09-07

- Added active survey-data-integration/NPS taxonomy.
- Defined cross-source measurement mismatch, harmonization vs measurement equivalence, and identification-related terms for C009.


### 0.2.0 — 2026-09-07

- Added explicit measurement-process and observation-process taxonomy.
- Distinguished measurement-procedure shift from observation-process shift.
- Added informative presence, informative observation and clinical presence terminology.
- Expanded missingness-shift mechanisms.
- Added shift detection/characterization/attribution distinctions.
- Added provenance/harmonization terminology and causal-language warning.
