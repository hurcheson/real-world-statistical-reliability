---
title: Survey Data Integration / Nonprobability Inference — Field Map
version: 0.8.0
last_updated: 2026-09-07
status: canonical historical field map — D013 superseded for active discovery by D022
---

# Survey Data Integration / Nonprobability Inference — Deep Field Map

> **Current program status (D022, 2026-09-07):** This map remains canonical and scientifically valid as the survey-data-integration branch, but D013 is no longer the exclusive active first-project discovery neighborhood. Cross-field review-first reconnaissance and OF-35 are now the active bounded prosecution path. See `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

## 1. Why this map exists

The first program neighborhood — ML/clinical-prediction reliability under observation-process shift — produced a scientifically serious lead (C008), but the production-grade map revealed unusually unfavorable **first-project competitive geometry**: several well-resourced groups were already publishing close 2025–2026 work, while a defensible contribution would require simultaneous competence in EHR data generation, clinical prediction, calibration, missing-data/observation processes, transportability and causal or stress-test identification.

This map therefore evaluates a different statistics neighborhood on its own merits:

> **Finite-population inference by integrating probability and nonprobability data sources, with special attention to selection bias, measurement incompatibility and robustness of adjustment.**

The purpose is not to find an empty literature. The purpose is to decide whether this neighborhood contains an important, technically coherent and finishable first research problem under the acceptance gate in `00_RESEARCH_CHARTER.md`.

This is a structured field map, not a PRISMA systematic review. Source IDs refer to `11_REFERENCE_LEDGER.md`.

---

# 2. Core statistical problem

Let the finite target population be

\[
U=\{1,\ldots,N\}.
\]

For unit \(i\), let \(Y_i\) denote a study variable and \(X_i\) a vector of auxiliary variables relevant to both selection and/or prediction.

A common modern data-integration setup contains:

- a **probability/reference sample** \(A\), with known design inclusion probabilities \(\pi_i^A\) and design weights \(d_i^A=1/\pi_i^A\), usually containing \(X\) and sometimes \(Y\);
- a **nonprobability sample** \(B\), such as an opt-in web panel, administrative source, convenience cohort or digital trace source, with unknown participation probabilities \(\pi_i^B\), usually containing \((X,Y)\).

The target may be a finite-population mean

\[
\mu_Y = N^{-1}\sum_{i\in U}Y_i,
\]

a total, proportion, distribution function, quantile, regression/association parameter or domain/small-area quantity.

Probability sampling provides a design-based route to finite-population inference. Nonprobability data can be much larger, cheaper and timelier, but its unknown selection mechanism destroys that design guarantee. Data integration tries to recover useful information from \(B\) using the probability/reference information in \(A\). [R061–R064, R067]

## 2.1 Why the field matters now

Recent high-level reviews identify data integration and nonprobability samples as continuing frontiers in survey theory, driven by declining response rates, cost pressure and expanding administrative/digital/opt-in sources. Official-statistics agencies are actively researching the same problem rather than treating it as solved. [R061–R063, R100–R102]

The fundamental trade-off is:

> **Borrow more information and gain precision/timeliness, but accept stronger assumptions about selection, transportability, measurement and overlap.**

This is a durable statistical problem rather than a transient software/model trend.

---

# 3. The inferential assumptions that organize the field

The literature uses different formulations, but most methods rely on some combination of the following.

## A1 — A valid probability/reference design

The reference source must support valid finite-population inference for the variables used from it. If the reference survey itself has severe nonresponse, undercoverage or measurement error, that uncertainty enters the integration problem.

## A2 — Common population / target alignment

The probability and nonprobability sources must correspond to a well-defined common target population, period and eligibility definition, or differences must be modeled explicitly.

## A3 — Ignorable nonprobability participation / transportability

A common quasi-randomization assumption is

\[
P(\delta_i^B=1\mid X_i,Y_i)=P(\delta_i^B=1\mid X_i),
\]

where \(\delta_i^B\) indicates membership in \(B\). Outcome-model approaches express an equivalent transportability requirement, e.g. that the conditional relationship learned in \(B\) applies to the target/reference population. These assumptions are generally not testable from the nonprobability sample alone. [R063–R069]

## A4 — Positivity / overlap / coverage

Units with relevant \(X\) values must have nonzero probability of appearing in the nonprobability source, and practical overlap must be adequate. Deterministic undercoverage is a distinct failure mode. [R071, R079]

## A5 — Model adequacy

Propensity/pseudo-weighting methods require an adequate participation model; prediction/mass-imputation methods require an adequate outcome model. Doubly robust methods relax this to correctness of at least one of two model components; multiply robust methods introduce several candidate models. [R068–R072]

## A6 — Shared-variable comparability

The standard mathematical setup usually treats \(X\) as **the same covariate vector observed in both sources**. Calibration literally balances the nonprobability sample's observed \(X\) to probability-sample totals/distributions of \(X\). Recent applied work often says that variables should be harmonized before they enter the participation model. [R064, R083, R090]

This assumption is less innocuous than it looks. Probability and nonprobability panels can differ in measurement properties; mode and source characteristics can change how constructs are measured; sensitivity methods themselves can require variables that are identically/comparably measured. [R065–R066, R082, R087]

**This A6 interface is the main candidate seam generated by the map.**

---

# 4. Established method families

## 4.1 Quasi-randomization / propensity / pseudo-weighting

Estimate the unknown nonprobability participation mechanism using the probability sample as a reference, then weight units in \(B\) approximately by inverse participation probabilities. Chen, Li & Wu provide a major modern framework; BLS continues to compare quasi-randomization estimators. [R068, R077]

**Strength:** directly targets selection bias and retains survey-weighting interpretation.

**Weakness:** sensitive to participation-model misspecification, overlap and whether the adjustment covariates actually capture the selection-outcome relationship.

## 4.2 Calibration weighting

Choose weights for \(B\) so weighted auxiliary totals/distributions agree with probability/reference totals. Modern work continues to unify and generalize calibration weighting. [R064, R076, R091]

**Strength:** operationally familiar in survey statistics; can avoid direct inversion of tiny estimated propensities.

**Weakness:** balance on the wrong, noisy or noncommensurate variables can create an illusion of representativeness.

## 4.3 Outcome modeling / mass imputation

Fit \(E(Y\mid X)\) or a richer conditional model in \(B\), then impute/predict \(Y\) for the probability sample. [R069]

**Strength:** can exploit strong predictive structure and subject-matter knowledge.

**Weakness:** requires transportability of the outcome model and adequate support.

## 4.4 Doubly and multiply robust integration

Combine propensity and outcome components so consistency can survive misspecification of one component (or, in multiply robust procedures, all but one member of model sets). [R068, R072, R074]

**Strength:** weaker reliance on one exact model.

**Weakness:** “double robustness” does not automatically protect against a violated data-source linkage assumption such as incompatible covariate measurement.

## 4.5 Empirical-likelihood and semiparametric approaches

Pseudo empirical likelihood, empirical likelihood under nonignorable selection, copula models and other semiparametric strategies provide alternative inferential machinery. [R070, R080, R090]

## 4.6 Safe/selective borrowing

Rather than always using \(B\), test or estimate whether the nonprobability source is sufficiently comparable to be worth pooling. Gao & Yang's pretest framework is a major example; 2025 preprints extend efficient combination of probability-only and doubly robust estimates. [R073–R075]

This is an important conceptual principle: **more data should not automatically mean more borrowing.**

---

# 5. Active 2023–2026 frontier and anti-gap findings

The field is active. Several superficially attractive project ideas are already directly occupied.

## 5.1 Generic “new weighting estimator” — crowded

Quasi-randomization, calibration, empirical likelihood, copula, doubly/multiply robust, Bayesian and ML-assisted estimators all have substantial recent work. [R068–R080, R090–R091]

**Anti-gap conclusion:** do not start by inventing another generic estimator unless it fixes a clearly specified failure mode.

## 5.2 Nonignorable selection — important but highly active

Sensitivity analysis remains essential because ignorability is unverifiable, but this is not an empty space. Hammon & Zinn validate a sensitivity index; Liu et al. give 2026 nonignorable-inference methodology; Changbao Wu presented current 2026 work on nonignorable participation. [R080–R082]

**Anti-gap conclusion:** “relax MAR/ignorability” is too generic for a first project.

## 5.3 Multiple reference surveys — direct 2026 method

Landsman et al. develop participation-bias correction using multiple reference surveys and an active funded project continues that line. [R083]

**Anti-gap conclusion:** do not claim that using more than one reference source is open.

## 5.4 Distribution functions / quantiles — direct 2026 method

Flood & Mostafa develop finite-population CDF and quantile estimators under probability/nonprobability integration. [R084]

**Anti-gap conclusion:** a generic extension from means to quantiles is already occupied.

## 5.5 Measurement error + representativeness — direct 2026 work, but not identical to the lead

Sen & Lahiri jointly address response measurement error and representativeness using multiple probability/nonprobability surveys. [R085]

**Anti-gap conclusion:** “nonprobability surveys have both selection bias and measurement error” is not novel.

However, their target is measurement error in survey responses/composite estimation. It does not by itself settle the distinct question of **source-specific error in the shared covariates that drive the participation adjustment**.

## 5.6 Regression parameters — active

Wang, Kim & Kim develop survey data integration for regression analysis. [R086]

**Anti-gap conclusion:** do not assume association/regression targets are untouched merely because much of the field emphasizes means/totals.

## 5.7 Small-area estimation — rapidly active

A very recent August 2026 review/comparative simulation maps nonprobability samples for small-area estimation and extends several approaches. [R107]

**Anti-gap conclusion:** small-area NPS is not a low-competition escape hatch.

---

# 6. The strongest candidate seam: cross-source measurement mismatch in adjustment variables

## 6.1 Why this seam emerged

Three pieces of evidence meet at the same interface:

1. Standard integration methods assume common/shared auxiliary variables \(X\) are observed across sources and use them to estimate participation or calibrate distributions. [R064, R068–R069, R090]
2. Empirical survey-methodology work demonstrates that probability and nonprobability panels can exhibit **measurement non-equivalence**, and field reviews explicitly identify mode/source measurement differences as a core data-integration challenge. [R065–R066, R087]
3. Close 2025 work that jointly handles selection and misclassification states an explicit assumption that the covariates used in the participation model are **measured without error in both samples**. [R088]

The statistical interface is therefore:

> What if \(X\), the variable that is supposed to repair selection bias, is not actually the same measured object in the probability and nonprobability sources?

This is not a claim that no literature exists. Classical/general IPW with error-prone covariates already exists and is an important methodological ancestor. [R089]

The unresolved screening question is whether the **two-source finite-population integration problem with source-specific measurement maps** yields a consequential result beyond directly transplanting that older measurement-error machinery.

## 6.2 Formalizing the problem

Introduce a latent or target-scale auxiliary variable \(X_i\), but observe

\[
X_{Ai}^{*} = g_A(X_i,U_{Ai})
\]

in the probability source and

\[
X_{Bi}^{*} = g_B(X_i,U_{Bi})
\]

in the nonprobability source.

The source-specific measurement maps can represent:

- classical/random measurement error;
- binary misclassification;
- differential misclassification;
- category coarsening or different cut points;
- mode effects (phone vs web, interviewer vs self-administered);
- question-wording/response-scale differences;
- profile-variable versus questionnaire measurement;
- temporal/source coding changes.

Naive calibration may enforce

\[
\sum_{i\in B}w_iX_{Bi}^{*}
\approx
\sum_{i\in A}d_i^AX_{Ai}^{*},
\]

which need not correspond to balance on the latent/target-scale \(X\). A participation model trained to distinguish \(A\) and \(B\) may also learn **measurement-source differences** rather than population selection differences.

That creates a potentially important failure mode:

> an estimator can achieve excellent observed covariate balance and still move *away* from valid population inference because the balancing variables are not commensurate.

This statement is a hypothesis to derive/test, not yet a theorem or established empirical fact.

## 6.3 Identifiability warning

This is the central threat to C009.

If \(X\) is latent and each source observes only one noisy/source-specific version, then the true population distribution of \(X\), the nonprobability selection mechanism and the measurement mechanisms may not be separately identifiable from \((X_A^*,X_B^*,Y_B)\) alone.

Potential identifying information includes:

- a **bridge/validation sample** measuring both versions on the same units;
- repeated measurements or multiple indicators;
- known or externally estimated sensitivity/specificity or reliability parameters;
- administrative/gold-standard covariates for a subset;
- structural restrictions on \(g_A,g_B\);
- partial-identification bounds;
- explicit sensitivity parameters rather than point identification.

Therefore the first scientific task is not “build a corrected weighting algorithm.” It is to determine **what can be learned under each information regime**.

## 6.4 Closest-neighbor matrix

| Neighbor | What it already does | Why it threatens C009 | Possible remaining distinction |
|---|---|---|---|
| Yang & Kim review [R064] | Defines common-X probability/nonprobability integration; calibration/IPW/MI/DR | Standard setup already mature | Makes the common-X assumption visible but does not solve source-specific measurement mismatch |
| McCaffrey et al. [R089] | IPW with error-prone covariates | Could make a correction a direct transplant | Not specifically finite-population two-source integration where *different sources observe different versions* of adjustment X |
| Einarsson et al. [R087] | Empirical measurement equivalence across probability/nonprobability panels | Establishes phenomenon, so “measurement differs” is not novel | Does not develop the finite-population selection-adjustment consequences/correction/sensitivity framework |
| Salvatore [R065] | Identifies measurement differences and source quality as data-integration challenges | Conceptual gap already recognized | Does not settle an estimand/identification framework for error in participation-adjustment X |
| Dharma et al. [R088] | Corrects selection plus misclassification of hard-to-reach status | Very close selection×measurement neighbor | Participation covariates are explicitly assumed measured without error in both sources |
| Sen & Lahiri [R085] | Corrects measurement error and representativeness jointly | Direct 2026 competition at high level | Focuses on response/outcome measurement/composite estimation, not clearly differential error in shared participation covariates |
| Hammon & Zinn [R082] | Sensitivity to nonignorable selection; requires suitable comparable auxiliaries | Could absorb problem as “poor proxy” sensitivity | Does not isolate measurement-source mismatch in the auxiliary variables themselves |
| Landsman et al. [R083] | Multiple reference surveys; harmonize auxiliary variables | Adds practical harmonization layer | Harmonization is assumed/required, not a statistical treatment of residual measurement mismatch |

## 6.5 Candidate contribution hierarchy

The project should move through these levels in order and stop as soon as one level is sufficiently consequential.

### Level 1 — Failure characterization

Derive how source-specific error in adjustment variables propagates into bias/variance of one or more canonical estimators (e.g. calibration and CLW-type pseudo-weighting).

A useful result would identify when error **cancels**, when it only costs efficiency, and when it creates systematic bias despite apparent balance.

### Level 2 — Sensitivity / robustness analysis

If point correction is not identified, parameterize plausible measurement mismatch and report a sensitivity region for the target estimand.

This may be more honest and more generally useful than pretending a latent true \(X\) can be recovered.

### Level 3 — Diagnostic

Develop a diagnostic for *observable incompatibility* across sources that has a defined relationship to estimator risk. Mere two-sample testing is not enough; the diagnostic must inform inferential reliability.

### Level 4 — Correction under validation information

If a bridge/validation sample exists, derive a corrected estimator and variance procedure.

### Level 5 — General framework

Only if Levels 1–4 reveal a genuinely reusable structure should the project generalize across calibration, IPW and DR estimators.

---

# 7. Candidate generated by the map

## C009 — Cross-source measurement mismatch in nonprobability-sample adjustment

**Status:** **SCREENING — PRIORITY LEAD**

### Working question

> How robust are probability/nonprobability survey-integration procedures to source-specific measurement mismatch in the auxiliary variables used to model participation or calibrate weights, and what can be identified or sensitivity-analyzed when those variables are not truly commensurate?

### Minimal defensible contribution

A publishable project need not invent a universal estimator. A sufficient contribution could be:

> a formal bias/identification analysis plus a practical sensitivity framework showing when apparently successful covariate balance is unreliable because the probability and nonprobability sources measure the adjustment variables differently.

### Why this is preferable to the obvious alternatives

- It attacks a **failure mode of existing methods**, not another generic estimator.
- It links two established literatures — nonprobability-sample integration and measurement error/equivalence — at an assumption boundary documented by both.
- It can be studied with analytic derivations, moderate simulation and public survey data.
- It does not require GPUs, protected EHRs or a large engineering stack.
- It naturally admits a kill decision if it reduces to a trivial application of classical error-prone-IPW theory.

### Current confidence

**Moderate.** The seam is credible, but differentiation and identification are not yet sufficient for PROSECUTION/SURVIVES.

---

# 8. Public data substrates

## 8.1 CDC/NCHS RANDS — unusually strong first substrate

The Research and Development Survey (RANDS) is specifically designed for survey-methodology work. Public-use data and documentation exist for rounds 1–10. Rounds 8–10 contain both probability and nonprobability samples. [R092]

RANDS 10 provides:

- probability AmeriSpeak sample: **5,017** completes, web and phone administration; [R093]
- nonprobability Cint-Lucid opt-in web sample: **5,420** completes; [R094]
- overlapping NHIS questions, cognitive probes and health/well-being content; [R093–R094]
- technical sampling/weighting documentation; [R095–R096]
- a supplied nonprobability balancing weight based on age, race/Hispanic ethnicity, education, marital status and metropolitan status, using the probability sample as benchmark. [R096]

This is valuable because the design deliberately exposes probability/nonprobability and mode differences in a public, documented environment.

### Important caveat

RANDS does **not** automatically prove that the five adjustment variables are measured differently across sources, nor does it provide a latent gold standard for all variables. It is a substrate for:

- variable-provenance auditing;
- mode/source comparability checks where repeated/parallel measures support them;
- controlled measurement-mismatch stress tests;
- validation of observable diagnostics;
- empirical illustration after the theoretical estimand is fixed.

It should not be used to claim an unknowable “true” selection-versus-measurement decomposition.

## 8.2 RANDS 9

RANDS 9 similarly supplies a probability sample (**7,055** completes) and nonprobability sample (**8,973** adults), with public documentation and common survey content. [R097–R098]

This creates a second round for replication/temporal robustness without changing institutions or acquiring restricted data.

## 8.3 Other public reference sources

Potential secondary probability/reference substrates include ACS PUMS, CPS, NHANES and other federal surveys. They are useful for synthetic finite-population construction or external control totals, but exact variable harmonization must be audited rather than assumed.

---

# 9. Software / reproducibility substrate

The field has mature R infrastructure rather than requiring bespoke compute systems:

- `survey` — complex survey designs, calibration and design-based inference [R108];
- `nonprobsvy` — methods for nonprobability survey inference [R109];
- `nonprobsampling` — current nonprobability-sampling tools [R110];
- `svrep` — replicate-weight and simulation support [R111];
- public code from the Waterloo nonprobability-sampling program for participation-probability estimation [R112].

A first project is therefore computationally compatible with a laptop/workstation and reproducible simulation pipelines.

---

# 10. Research-group / competition architecture

This neighborhood has strong researchers, but the competition pattern is materially more navigable than the prior clinical-ML lead.

High-relevance clusters are recorded in `07_RESEARCH_GROUP_RADAR.md`. Key examples:

1. **Waterloo — Changbao Wu / Pengfei Li**: doubly robust, empirical likelihood, undercoverage and 2026 nonignorable NPS inference. [R080–R081, R103–R104]
2. **Iowa State — Jae Kwang Kim**: mass imputation, calibration/data integration; active 2026 Bregman-projection work. [R069, R086, R105]
3. **North Carolina State — Shu Yang**: test-and-pool/safe borrowing, data integration and generalizability. [R073]
4. **Michigan ISR — Michael Elliott / Yajuan Si**: probability/nonprobability integration and practical computational tools. [R106]
5. **BLS OSMR — Savitsky/Gershunskaya/Beresovsky et al.**: unknown overlap, thresholding and quasi-randomization comparisons. [R077–R079, R102]
6. **U.S. Census Bureau statistical research**: probability/nonprobability integration is an explicit FY2025–FY2027 current subproject. [R100–R101]
7. **Maryland — Partha Lahiri / Aditi Sen**: direct measurement-error + representativeness work. [R085]
8. **Toronto / Institute for Work & Health — Landsman et al.**: multiple-reference and selection/misclassification work. [R083, R088]
9. **NCHS RANDS**: agency-led survey-measurement/data-combination substrate. [R092, R099]
10. **Oregon State survey-statistics cluster**: copula/pseudo-weighting with common auxiliary variables. [R090]

### Competitive interpretation

This is **not** a weak field. But a small project can plausibly contribute by understanding one assumption/failure mode deeply, because the field values analytic results, simulation, finite-population reasoning and reproducible survey applications. It does not require racing foundation-model-scale benchmarks.

---

# 11. Opportunity portfolio generated by the map

Scores are screening judgments, not final novelty claims.

| Lead | Opportunity | Importance | Feasibility | Competition | Current verdict |
|---|---|---:|---:|---:|---|
| OF-18 / C009 | Cross-source auxiliary-scale mismatch in P/NPS calibration | High | High | Moderate | **PARKED / NO-GO FOR FIRST PROJECT** after stage-2 sensitivity prosecution |
| OF-19 | Sensitivity/diagnostics under nonignorable selection | High | High | High | Keep, but crowded [R080–R082] |
| OF-20 | Regression/association targets under NPS integration | High | High | Moderate-high | Keep only if sharper than R086/R083 |
| OF-21 | Safe/selective borrowing when NPS can hurt | High | High | Moderate-high | Active [R073–R075] |
| OF-22 | Repeated-survey drift in NPS participation mechanisms | Moderate-high | High | Moderate | Map later; do not assume open |
| OF-23 | Overlap/undercoverage diagnostics tied to decision rules | High | High | Moderate-high | Active [R071, R079] |
| OF-24 | Survey-quality/bot/satisficing error jointly with selection adjustment | High | Moderate-high | Moderate-high | **Prosecuted as C010; PARKED / NO-GO FOR FIRST PROJECT** after direct filter-before-reweighting prior art and weak screen-error identification |
| OF-25 | Reference/control-total uncertainty propagated through integration | Moderate | High | Moderate | Mature ancestry; only pursue with sharp failure mode |
| OF-26 | Distribution/CDF/quantile targets | High | High | High | **DEPRIORITIZE**; direct 2026 paper [R084] |
| OF-27 | Small-area NPS integration | High | Moderate | High | **DEPRIORITIZE**; current 2026 map [R107] |
| OF-28 | Multiple probability reference surveys | High | High | High | **DEPRIORITIZE**; direct 2026 method [R083] |
| OF-29 | Generic response measurement error + representativeness | High | High | High | **DEPRIORITIZE**; direct 2026 work [R085] |

---

# 12. Acceptance-gate assessment of the field

This evaluates the **neighborhood**, not whether C009 has survived.

| Charter criterion | Assessment | Evidence / reasoning |
|---|---|---|
| Importance | **PASS — strong** | Official-statistics and methodological reviews identify NPS/data integration as continuing frontiers [R061–R063, R100–R102] |
| Prior-art map | **PASS — strong for field selection** | Core frameworks plus 2023–2026 frontier and anti-gap results mapped [R064–R091] |
| Differentiation | **FIELD PASS / C009 narrowed** | Broad C009 novelty fails against erroneous-control, differential-propensity-error and finite-population measurement-error ancestors [R089, R113–R115]; only the P/NPS-specific decomposition/information-regime object continues |
| Consequentiality | **PASS — plausible** | Adjustment variables determine whether selection correction is valid; measurement mismatch can undermine the correction itself |
| Identifiability | **FIELD PASS / C009 partially resolved** | Minimal no-validation model is not point identified; known error rates identify the toy target; representative B-scale bridge resolves benchmark mismatch but not necessarily residual latent selection; stage-2 sensitivity utility remains open |
| Data feasibility | **PASS — excellent** | Public paired probability/nonprobability RANDS rounds and federal surveys [R092–R100] |
| Computational feasibility | **PASS — excellent** | Moderate simulations and survey computation; mature R ecosystem [R108–R112] |
| Scope feasibility | **PASS — good** | A one-failure-mode theory/simulation/application paper can be bounded tightly |
| Competition risk | **PASS — moderate** | Strong groups and current papers, but less direct preprint race than C008; candidate must monitor Waterloo/Maryland/Toronto/agency work |
| Audience | **PASS — strong** | Survey Methodology, JSSAM, Journal of Official Statistics, JRSS A, AStA/Statistical Methods & Applications, applied biostatistics/public-opinion audiences |

## Field-level verdict

> **PASS for first-project research neighborhood.**

This field is not easier intellectually; it is **better matched to our constraints**. The required expertise is concentrated around finite-population inference, sampling, selection, calibration, measurement error and sensitivity analysis. Data and compute are realistic. A contribution can be complete without industrial-scale infrastructure.

---

# 13. C009 prosecution result — completed through stage 2

The complete C009 prosecution is recorded in `13_C009_IDENTIFICATION_PROSECUTION.md`.

## Stage-1 result

The broad C009 novelty framing failed against established work on erroneous/non-identical calibration controls [R113], differential measurement error in propensity methods [R114], generic error-prone IPW [R089], and finite-population data integration with measurement error [R115]. The candidate was narrowed to the P/NPS-specific interaction between wrong-scale target benchmarks and residual proxy-selection bias.

## Stage-2 result

The bounded-mismatch / partial-identification gate produced an exact binary sensitivity representation:

\[
\mu=\mu_B+\frac{(d_{obs}-\delta)\Delta_W}{\kappa},
\]

where

- `delta=q_A-q_B^P` is wrong-reference-scale mismatch; and
- `kappa=Corr(X,W_B|R=1)^2` under the toy assumptions is the fraction of the latent-X correction recovered by correct-scale proxy calibration.

This yields explicit thresholds for sign reversal, exact cancellation, over/under-correction, and whether naive calibration is better or worse than no adjustment.

However, the second gate also found decisive constraints:

1. Hartman & Huang [R120] substantially cover the `delta`-only unknown-target-margin sensitivity operation for calibration weights.
2. Molinari [R121] already establishes generic partial-identification machinery under bounded discrete misclassification.
3. Differential measurement-error sensitivity and weighting with error-prone covariates have strong prior art [R122–R124, R114, R089].
4. RANDS documents source/mode/provenance differences but provides no gold-standard X or source-specific error rates from which defensible `delta`/`kappa` regions can be estimated [R092–R096].
5. The toy target-mean sensitivity envelope broadens rapidly as minimum correct-classification assumptions weaken.
6. No multivariable theorem has yet emerged that clearly escapes standard calibration and misclassification machinery.

## Final C009 status

**C009: PARKED / NO-GO FOR FIRST PROJECT.**

This is not a declaration that the joint `(delta,kappa)` lemma is mathematically empty. It is a project-selection decision: the residual contribution is too narrow and insufficiently anchored for the first execution project.

## Reopening conditions

Reopen only with materially better information or theory, such as:

- a representative B-scale bridge sample;
- gold-standard or strong validation data for the shared adjustment variable;
- defensible construct-specific measurement bounds tight enough to make the sensitivity region informative;
- a nontrivial multivariable/multicategory theorem; or
- a substantive application in which the joint mismatch/proxy-reliability boundary changes a real inferential decision beyond the nearest sensitivity literature.

---

# 14. C010 prosecution result and recommended next step

OF-24 was prosecuted as **C010 — selection-aware response-quality filtering in nonprobability survey inference** using the four-channel discovery protocol.

## Result

**C010: PARKED / NO-GO FOR FIRST PROJECT.**

The prosecution confirmed a real inferential mechanism: after removing cases according to a response-quality screen and recalibrating the retained NPS sample, error can be separated conceptually into **retained response contamination** plus **residual selection among retained cases**. This makes quality filtering part of the selection process rather than neutral data cleaning.

However:

1. Slamowicz et al. [R127] directly show that excluding satisficers before recalculating weights can reduce bias in four NPPs, so the broad empirical contribution is occupied.
2. Mathur [R128] already formalizes selection bias from attention-check exclusion.
3. Kennedy et al. and Sen & Lahiri [R125–R126] directly occupy the response-error/measurement-error × representativeness interface.
4. Pew and Gallup [R129–R131] show that real screening rules can remove valid cases, change composition, and sometimes worsen target estimates, establishing importance but not a new method.
5. Without validated quality labels, false-positive/false-negative operating characteristics are not generally identified; generic latent-class and partial-identification ancestors already exist [R141, R121].

Full record: `14_C010_RESPONSE_QUALITY_FILTERING_PROSECUTION.md`.

## Recommended next scientific action

The bounded OF-19–OF-23 triage is complete and **did not produce C011**.

Do not force a candidate from the exhausted slate. Run a fresh **four-channel opportunity-generation pass** inside the D013 neighborhood, using the failure records from C009, C010 and `15_OF19_OF23_COLLAPSE_TRIAGE.md` as boundary conditions.

The next opportunity should be promoted only if it has:

1. a precise estimand and identifiable/bounded failure mechanism;
2. direct prior-art differentiation that survives a collapse search;
3. a concrete decision that changes with the result;
4. public or realistically obtainable validation data for the key assumptions; and
5. a scope compatible with the first execution project.

OF-22's intermittent-probability-anchor drift question may be revisited during that pass, but it has **not** yet earned candidate status.

## Historical state immediately after OF-19–OF-23 triage

- C008: **PARKED / NO-GO for first project**.
- Active neighborhood: **survey data integration / finite-population P/NPS inference**.
- C009: **PARKED / NO-GO FOR FIRST PROJECT**.
- C010: **PARKED / NO-GO FOR FIRST PROJECT**.
- OF-19: broad form parked.
- OF-20: generic form parked.
- OF-21: broad form parked.
- OF-22: **WATCHLIST / SHARPEN BEFORE CANDIDATE**; broad form collapsed by direct recurring-hybrid prior art [R142].
- OF-23: broad form parked.
- C011: **unassigned**.
- No execution project has been selected.

Full triage record: `15_OF19_OF23_COLLAPSE_TRIAGE.md`.

# 15. Fresh D013 opportunity-generation result

The fresh pass required new opportunity classes rather than further narrowing the crowded C009/C010/OF-19–OF-23 territory.

## Priority screening lead: OF-30

**OF-30 — finite-benchmark certification / benchmark-to-target transportability** asks:

> When does low observed bias on a finite benchmark set legitimately certify low bias for unbenchmarked target outcomes, and how should benchmark sets be chosen to minimize false certification?

This lead is attractive because four channels converge:

- **literature:** Pew explicitly warns that benchmark error may not transfer to political-attitude targets [R150], while survey benchmarking lacks one commonly used methodological framework [R154];
- **theory:** finite benchmark balance does not control an unrestricted target residual;
- **data:** Pew multi-source benchmarking studies and NCHS RSS provide many benchmark variables for held-out validation [R148–R153];
- **decision:** agencies/vendors choose benchmark content and must decide whether benchmark performance justifies a quality/release claim.

NCHS's Round-4 move toward content-related benchmarks provides particularly strong decision-channel evidence [R148]. However, NCHS also performs sophisticated benchmark-guided calibration-variable selection [R149], so OF-30 cannot be promoted on the basis of “choose calibration variables using benchmarks.”

## Other generated directions

- **OF-31 — adaptive benchmark reuse / quality-assessment overfitting:** retain as a mechanism inside OF-30; high generic post-selection-theory threat.
- **OF-32 — target/control-universe mismatch:** concrete 2026 HTOPS production failure [R156], but high erroneous-control/C009 prior-art threat; watchlist only.
- **OF-33 — cross-vendor respondent overlap:** empirically real [R157–R158] but broad diversification question crowded by current multi-vendor averaging work [R159]; parked.
- **OF-34 — source redundancy under source loss/quality change:** broad form crowded by multiple-source adaptive survey design [R160]; parked.

## Current promotion gate

**C011 remains unassigned.** OF-30 may be promoted only after:

1. direct nearest-neighbor search finds no equivalent benchmark-to-target certification framework;
2. Pew/NCHS benchmark outcomes support a credible held-out/leave-domain-out validation design; and
3. the theory yields a nontrivial bound/design/decision result or reproducible failure law beyond standard cross-validation and outcome-specific adjustment.

Full pass record: `16_D013_FRESH_OPPORTUNITY_GENERATION.md`.

# 16. OF-30 bounded-screening result

The priority-screening gate is complete. **OF-30 is parked and C011 remains unassigned.**

The screening changed the field map in three ways:

1. **R-indicator / nonresponse-bias-indicator work is now a hard nearest-neighbor constraint.** Survey methodology already distinguishes a whole-survey representativeness score from bias in a specific survey variable, and validation studies show imperfect transport from auxiliary-based quality signals to other outcomes [R161–R164].
2. **Benchmark-rich validation remains feasible.** Pew's 28-variable six-source study and NCHS RSS Round 7's 53 benchmark outcomes can support nested leave-domain-out diagnostics [R166, R169]. This is useful data infrastructure, but not by itself a novelty claim.
3. **The natural theory routes are occupied.** Restricting the target to a function class leads toward calibration/worst-case-bias/kernel-balancing theory [R165]; modeling a finite benchmark score matrix to predict unseen benchmarks leads toward generic benchmark-subset selection [R168].

### New anti-gap constraint

Do not propose generic **survey quality certification**, **representative benchmark selection**, or **benchmark-to-unseen-outcome transport** as a fresh gap unless a mechanism-specific identification/decision result survives these ancestors.

### Next action

Return to fresh four-channel opportunity generation inside D013. C011 remains non-automatic.

Full record: `17_OF30_BOUNDED_SCREENING.md`.

## Change log

### 0.8.0 — 2026-09-07

- Marked the survey-data-integration map as canonical historical/current-branch reference after D022 reopened cross-field discovery.
- Linked the active bounded prosecution path to `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

### 0.7.0 — 2026-09-07

- Recorded OF-30 bounded-screening result and new anti-gap constraint.

### 0.6.0 — 2026-09-07

- Added the fresh D013 opportunity-generation result.
- Recorded OF-30 as priority screening and OF-31–OF-34 dispositions.
- Replaced “fresh generation” as the next action with a bounded OF-30 screening gate.

### 0.5.0 — 2026-09-07

- Completed OF-19–OF-23 collapse-first triage; no opportunity earned C011.
- Retained only the narrowed intermittent-anchor OF-22 residue as WATCHLIST / SHARPEN BEFORE CANDIDATE.
- Replaced bounded-slate triage with fresh four-channel opportunity generation as the next scientific action.

### 0.4.0 — 2026-09-07

- Prosecuted OF-24 as C010 using the four-channel protocol.
- Recorded the filter-induced selection decomposition and direct prior-art constraints R125–R141.
- Parked C010 as **NO-GO FOR FIRST PROJECT**.
- Narrowed remaining triage to OF-19–OF-23.

### 0.3.0 — 2026-09-07

- Completed C009 stage-2 bounded-mismatch / partial-identification prosecution.
- Recorded the `delta`-`kappa` decision surface and new nearest neighbors R120–R124.
- Parked C009 as **NO-GO FOR FIRST PROJECT** while retaining the survey-data-integration neighborhood.
- Replaced the C009 execution gate with a bounded next-candidate triage recommendation.

### 0.2.0 — 2026-09-07

- Added C009 prosecution result and next gate.

