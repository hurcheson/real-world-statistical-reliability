---
title: Candidate Registry
version: 0.26.0
last_updated: 2026-09-21
status: active
---

# Candidate Registry

## Status vocabulary

- **IDEA FAMILY** — broad problem family, not yet a prosecute-able research question.
- **IDEA** — specific but untested lead.
- **SCREENING** — lightweight but evidence-based prior-art/importance/feasibility check.
- **PROSECUTION** — intensive novelty and feasibility audit against nearest neighbors and active work.
- **SURVIVES** — sufficient evidence to prepare an execution protocol.
- **PARKED** — potentially valuable but not appropriate now.
- **KILLED** — do not pursue without materially new evidence.
- **EXECUTION** — promoted into an active research project.

## Registry

| ID | Candidate | Status | Why |
|---|---|---|---|
| C001 | Imputation → BP variability → downstream inference | **KILLED** | Core principle substantially covered by downstream-aware imputation and variability/inference literature; residual contribution too narrow for primary project |
| C002 | Informative observation → latent BP variability → clinical outcome | **PARKED / NO-GO** | Active neighboring PhD/methods work, explicit future-work statements, difficult identification, high computational burden and competition |
| C003 | Reliability/calibration under distribution shift | **IDEA FAMILY** | Important but generic form is mature/crowded; useful as evaluation layer, not yet a paper |
| C004 | Missingness/observation-process shift and predictive reliability | **IDEA FAMILY** | Deep mapping found active theory/algorithms and clinical-presence work; sharpened into C008 for screening |
| C005 | Distribution shift × uncertainty quantification | **IDEA FAMILY — DEPRIORITIZED** | Conformal/UQ under covariate shift has mature theory and healthcare applications; poor first-project frontier without sharper mechanism |
| C006 | Distribution shift × subgroup calibration/heterogeneity | **IDEA FAMILY** | Important but active and sample-intensive; may become secondary aim under a specific shift mechanism |
| C007 | When to recalibrate/update a deployed model under drift | **IDEA FAMILY — DEPRIORITIZED** | Dynamic updating and post-deployment monitoring are active/mature; mechanism-specific updating may remain useful |
| C008 | Measurement-process-aware external-validation stress testing | **PARKED / NO-GO FOR FIRST PROJECT** | Scientifically valid but poor first-project competitive geometry: direct 2025–2026 neighbors plus unusually broad expertise/data burden relative to expected differentiation |
| C009 | Cross-source auxiliary-scale mismatch in nonprobability calibration | **PARKED / NO-GO FOR FIRST PROJECT** | Stage-2 sensitivity prosecution produced an exact joint mismatch/proxy-reliability decision map, but the mismatch-only sensitivity and generic partial-ID pieces have strong prior art, RANDS cannot anchor defensible measurement bounds, and the residual interaction is too narrow for the first project |
| C010 | Selection-aware response-quality filtering in nonprobability survey inference | **PARKED / NO-GO FOR FIRST PROJECT** | Four-channel prosecution found a real filtering × selection decision, but direct filter-before-reweighting evidence exists, exclusion-selection theory and measurement×representativeness methods are mature, and screen FP/FN behavior is weakly identified without validation |
| C011 | Precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation | **PARKED / NO-GO FOR FIRST PAPER** | Only 2016 remains fully manuscript-reproducible; reopen only with materially new authoritative operational provenance |
| C012 | Decision-preserving disclosure control | **KILLED / NO-GO FOR FIRST PAPER** | Useful nonlinear certification utility, but it remains a task-specific objective inside established optimal-release/risk–utility/workload-aware frameworks |
| C013 | Release-provenance and temporal-interpretability audit of repeated PLACES/500 Cities estimates | **SURVIVES / CONTROLLED EXECUTION DESIGN** | Nine-work corpus, finalized provenance crosswalk and three contrasting archive reproductions establish a distinct, feasible downstream reliability audit |

---

# C001 dossier summary

## Core question

Do time-series imputation methods that minimize pointwise reconstruction error also preserve blood-pressure variability measures and downstream inference?

## Initial strengths

- natural connection across Vatcheva research streams;
- public-data feasibility;
- applied-statistics depth;
- simulation-friendly.

## Fatal/major threats

- task-oriented imputation evaluation already treats downstream performance as distinct from reconstruction;
- physiological-sensor literature already studies propagation of missingness into derived metrics and regression;
- BP variability measurement design and naive variability estimation are established methodological issues.

## Verdict

**KILLED as primary project.**

---

# C002 dossier summary

## Core question

When measurement times are health-dependent, how biased are within-person BP variability estimates and their outcome associations, and can observation-process-aware location-scale/joint models recover valid inference?

## Initial strengths

- genuine EHR reliability issue;
- deeper than simple imputation;
- directly statistical;
- clinically meaningful.

## Major threats

- informative-observation methods are mature;
- three-process joint models have long existed;
- BPV/location-scale authors explicitly identify informative visiting as an extension;
- active 2024–2026 PhD work targets within-subject variability under irregular/informative observation;
- realistic EHR observation includes both visit occurrence and biomarker selection;
- identification may rely strongly on unverifiable parametric/shared-latent assumptions;
- method development could become dissertation-scale.

## Verdict

**PARKED / NO-GO for first project.**

## Narrow frontier that technically remained

Joint modeling of a latent, possibly time-varying within-subject scale process when both observation/measurement intensity and a terminal-event process depend on that scale.

This is recorded as a possible future methodological frontier, not an approved project.

---

# C008 dossier — parked first-project lead

## Working title

**Measurement-process-aware external-validation stress testing for clinical prediction models**

## 1. Concise question

> When does predictive information encoded by missingness, measurement intensity, or other observation-process features improve internal model performance but make predicted risk non-transportable, and how should external validation diagnose that failure?

## 2. Why it matters

Routine clinical data contain both:

- patient/biological information;
- information generated by local care processes and data infrastructure.

A model can exploit both. If source-specific workflow signals do not transport, internal accuracy may reward a shortcut that produces unsafe target probabilities.

A useful external-validation procedure should detect this before deployment and distinguish it from ordinary case-mix or base-rate change.

## 3. Closest prior work identified so far

Reference IDs are in `11_REFERENCE_LEDGER.md`.

### General robustness/stress testing

- **R005:** Subbaswamy, Adams & Saria — user-specified conditional shift robustness/stability analysis, including clinical-practice shifts.

### Measurement heterogeneity and missing predictors

- **R016–R017:** Luijken et al. — predictor measurement heterogeneity/procedure changes can alter external performance and calibration.
- **R018–R020:** Hoogland/Sperrin/Tsvetanova lineage — missing-predictor handling in validation should be compatible with deployment.

### Informative observation / missingness shift

- **R021–R023:** healthcare presence/observation process is informative.
- **R024:** robust prediction under missingness shift.
- **R026:** clinical presence shift explicitly formalized and modeled.

### Direct empirical competitors

- **R027:** Yamamoto et al. 2026 — closest current preprint. Observation-process features in MIMIC-IV/eICU sepsis prediction improve internal discrimination but are associated with worse external calibration/transportability.
- **R031:** Patel & Beedala 2026 — MIMIC-IV→eICU ICU mortality external validation including calibration, recalibration, decision curves and subgroup analyses.

### Lifecycle neighbor

- **R030:** Kopanitsa 2026 — deployed systems show calibration drift and workflow telemetry signals such as missingness/latency.

## 4. Active competitors / groups

Highest surveillance priority:

1. Manchester clinical prediction / missing-data / clinical-presence cluster [R020, R026, R055].
2. Johns Hopkins Saria/Subbaswamy context-shift robustness [R005, R053].
3. Charité CLAIM/Rockenschaub missingness-shift and ICU-validation work [R024, R029, R058].
4. Utrecht/Birmingham prediction-model methodology [R012, R015–R018, R056–R057].
5. MIT Healthy ML / Michigan MLD3 for broad deployment/shortcut robustness [R037, R052, R054].

## 5. Explicit differentiation — hypotheses to prosecute, not claims

C008 is only worth pursuing if at least one consequential differentiator survives.

### D1 — Shift attribution rather than generic external degradation

Try to distinguish:

- case-mix/base-rate shift;
- predictor-value/measurement-procedure shift;
- observation-process shift.

Threat: R005 may already provide enough general machinery that this is an application rather than a contribution.

### D2 — Controlled observation-process stress testing

Construct clinically motivated perturbations to measurement availability/frequency while holding patient values/outcomes as fixed as the design permits.

Threat: artificial masking can be scientifically unrealistic; prior stress-testing/domain-generalization work may already cover this.

### D3 — General evaluation framework

Evaluate across multiple tasks/environments/model classes rather than one sepsis task.

Threat: breadth can become a benchmark paper without a clear scientific estimand.

### D4 — Actionable failure diagnosis

Distinguish failures potentially repairable by recalibration from failures suggesting unstable workflow features/refit/non-use.

Threat: this can drift into mature model-updating literature without new identification.

## 6. Identification / estimand

**Not yet fixed. This is the most important unresolved scientific issue.**

Possible targets are different:

1. causal effect of changing measurement policy on predictive performance;
2. descriptive decomposition of observed source-target degradation;
3. controlled perturbation sensitivity to an observation-process intervention;
4. worst-case reliability over a prespecified family of plausible process shifts.

C008 must choose one before promotion to PROSECUTION.

## 7. Data feasibility

### Primary substrate

- **eICU-CRD [R043]:** multi-hospital/unit data with documented interface-dependent availability; strongest natural test bed for observation-process heterogeneity.
- **MIMIC-IV [R042]:** mature single-system source/target comparator.

### Optional independent environments

- HiRID [R045];
- AmsterdamUMCdb [R046];
- BlendedICU harmonization pipeline [R047–R048], while preserving source provenance.

### Prototype

- eICU demo [R044] for SQL/schema development only.

## 8. Computational scope

Plausibly manageable if framed as an evaluation/failure-analysis study rather than a new deep-learning architecture.

Likely requirements:

- reproducible cohort extraction;
- site/unit environment construction;
- multiple standard model classes;
- calibrated external-validation metrics;
- controlled stress-test generator;
- bootstrap/cluster-aware uncertainty;
- sensitivity analyses across tasks/sites.

Avoid dissertation-scale joint latent-process modeling for the first project.

## 9. Likely audience / venue family

If primarily methodological/evaluation:

- clinical prediction / biostatistics / biomedical informatics journals;
- ML-for-health venues if the stress-test framework has methodological generality;
- broader clinical-AI evaluation venue if deployment implications are strong.

Venue should not be selected until the contribution type is fixed.

## 10. Kill criteria for screening

Kill or sharply reshape C008 if:

1. R005 + R027 (or follow-up work) already provide the proposed attribution/stress-testing contribution;
2. process-shift environments cannot be defined reproducibly from public/credentialed data;
3. the only feasible experiment is arbitrary missing-value masking;
4. the result reduces to “calibration is worse externally”;
5. decision implications cannot be distinguished from generic recalibration/update guidance;
6. a credible claim would require causal assumptions unsupported by the data;
7. the differentiator is merely “more datasets/models/metrics.”

## 11. Promotion criteria

Move to **PROSECUTION** only if:

- a precise estimand is chosen;
- a nearest-neighbor matrix shows a meaningful uncaptured claim;
- realistic stress-test/environment definitions are feasible;
- calibration/utility outcomes and uncertainty are prespecified;
- data access is realistic;
- scope remains executable as a first project.

## Current verdict

**PARKED / NO-GO FOR FIRST PROJECT.**

**Confidence:** high for the first-project decision.

The scientific question remains legitimate. It is parked because the nearest 2025–2026 work, required domain stack, and execution burden produce poor expected value for the program's first independent project. Reopen only if supervision/resources materially change or a much narrower differentiator emerges.

---


# C009 dossier — parked after stage-2 prosecution

## Working title

**Cross-source auxiliary-scale mismatch in nonprobability calibration: bias decomposition and identification**

## 1. Concise question

> When a probability reference and a nonprobability sample encode a nominally shared adjustment variable through different measurement processes, can we distinguish bias caused by calibrating to a benchmark on the wrong measurement scale from residual selection bias caused by using a noisy proxy, and what information is required to identify or sensitivity-analyze each component?

## 2. Why the broad formulation failed

The v0.3 formulation was too broad. The prosecution found established ancestors that already cover:

- calibration to erroneous or closely related but non-identical auxiliary controls [R113];
- differential measurement error in propensity-score covariates [R114];
- generic IPW with error-prone covariates [R089];
- finite-population data integration with measurement error in multiple data sources [R115].

Therefore C009 cannot claim that source-specific covariate error, wrong calibration controls, or measurement-error-plus-selection are themselves new.

## 3. Narrowed possible contribution

The surviving object is specific to the P/NPS reference-calibration structure. In the binary toy model developed in `13_C009_IDENTIFICATION_PROSECUTION.md`, naive calibration bias separates exactly into:

1. a **cross-source benchmark-scale mismatch** term; and
2. a **residual proxy-selection** term.

The decomposition makes clear that:

- using the wrong-scale probability benchmark can add bias even if the NPS is otherwise representative;
- using the correct B-scale benchmark does not necessarily remove selection bias when ignorability holds only given latent `X`;
- a representative bridge sample administered on the NPS measurement scale can fix the first component without identifying latent `X`;
- two fallible measurements alone do not automatically create a validation design.

This is a provisional contribution hypothesis, not a novelty claim.

## 4. Identification status

The minimal model has now been classified.

### No validation information

**Not point identified in general.** A constructive example in `13_C009_IDENTIFICATION_PROSECUTION.md` gives the same observed P/NPS distributions under two latent parameterizations with target means 0.38 and 0.50.

### Known source-specific misclassification rates

**Point identified under the toy assumptions** when both measurement maps are informative and latent classes occur in the NPS. Target prevalence, NPS latent prevalence and latent outcome-stratum means can be recovered.

### Bridge measuring both fallible versions only

**Not automatically identifying.** A two-by-two joint table for two fallible binary measurements in one population has fewer degrees of freedom than prevalence plus four accuracy parameters [R119].

### Representative bridge on the NPS measurement scale

Identifies the correct B-scale target benchmark `q_B^P`, so it can remove the wrong-scale calibration component. It does not by itself eliminate residual proxy-selection bias.

### Gold-standard validation

Can identify the source-specific error maps under appropriate sampling assumptions.

## 5. Closest prior work after both prosecution stages

Highest priority:

- **R120 — Hartman & Huang (2024):** survey-weight sensitivity for partially observed confounders; with calibration/raking, varies an unknown target-population covariate mean. This substantially subsumes the `delta`-only target-margin sensitivity operation.
- **R121 — Molinari (2008):** generic sharp partial identification under restrictions on discrete misclassification matrices, including lower bounds on correct reporting.
- **R122 — Imai & Yamamoto (2010):** nonparametric identification and sensitivity analysis under differential measurement error.
- **R123 — Rudolph & Stuart (2018):** adapts unobserved-confounding sensitivity analyses to covariate measurement error in propensity methods.
- **R124 — Lockwood & McCaffrey (2016):** necessary/sufficient conditions for matching/weighting with functions of error-prone covariates, including discrete misclassification and group-specific functions.
- **R113 — Chambers (2008):** wrong/non-identical auxiliary controls in calibration; strongest direct ancestor for the benchmark-mismatch component.
- **R114 — Hong, Rudolph & Stuart (2017):** differential covariate measurement error in propensity methods.
- **R089 — McCaffrey et al. (2013):** corrected IPW with error-prone covariates.
- **R115 — Kim & Tam (2021):** finite-population data integration with measurement error and unknown big-data selection.
- **R116–R119:** identification and two-survey/bridge-sample boundary results.
- **R087/R088/R085:** empirical measurement nonequivalence and recent P/NPS selection×measurement neighbors.

The stage-2 comparison and final verdict are in `13_C009_IDENTIFICATION_PROSECUTION.md`.

## 6. RANDS feasibility after provenance audit

RANDS 10 remains a credible **illustration/sensitivity substrate**, not a gold-standard validation source [R092–R096].

Useful documented features:

- paired AmeriSpeak probability and Cint-Lucid opt-in nonprobability samples;
- probability sample includes web and phone while NPS is web-only;
- NPS balancing weights use age, race/Hispanic ethnicity, education, marital status and metropolitan status;
- probability-sample technical documentation states that demographic questions for opt-in panelists were added after pretest, establishing different provenance for at least some adjustment information.

Limit: final coding comparability does not establish latent measurement equivalence, and no source-specific gold error rates are supplied.

## 7. Computational scope

Still excellent if the contribution survives:

- analytic derivation;
- bounded-mismatch/partial-identification calculations;
- moderate simulation;
- one public RANDS illustration;
- no GPU or large infrastructure.

## 8. Final sensitivity-utility gate result

The second prosecution produced a real decision diagnostic but did **not** clear the project gate.

What survived mathematically:

- `delta=q_A-q_B^P` controls wrong-reference-scale mismatch;
- `kappa=Corr(X,W_B|R=1)^2` in the binary toy model controls proxy attenuation;
- the target mean satisfies `mu = mu_B + ((d_obs-delta) Delta_W)/kappa`;
- exact thresholds identify when naive calibration under-corrects, is exactly right by cancellation, over-corrects but helps, becomes worse than no calibration, or moves in the wrong direction.

What failed as a first-project contribution:

1. the `delta`-only sensitivity operation is substantially a special case of Hartman & Huang [R120];
2. bounded-misclassification partial identification is generic prior art [R121];
3. differential measurement-error sensitivity/error-prone weighting are already developed in adjacent literatures [R122–R124, R114, R089];
4. RANDS does not identify or empirically bound `delta` or `kappa` tightly enough to make the sensitivity analysis data-anchored;
5. the toy sensitivity envelope widens quickly when minimum correct-classification assumptions are weakened;
6. no nontrivial multivariable theorem has yet emerged that would lift the contribution above a narrow interaction-specific lemma.

## 9. Reopening conditions

Reopen C009 only if one of the following changes the evidence base:

- a representative bridge or validation source directly informs the B-scale target margin or latent-X error maps;
- construct-specific reliability studies support defensible, tight bounds for a real P/NPS adjustment variable;
- a multivariable/multicategory extension yields a distinctive theorem/diagnostic beyond existing calibration and misclassification theory;
- a concrete substantive application shows that the joint `delta`-`kappa` boundary changes an important inferential decision and is not covered by the nearest literature.

## Current verdict

**PARKED / NO-GO FOR FIRST PROJECT.**

**Confidence:** moderately high.

C009 is not being discarded as mathematically empty. Stage 2 found a clean joint mismatch/proxy-reliability lemma and exact decision zones. The first-project standard is higher: the generic sensitivity and partial-identification components have strong prior art, the remaining interaction is narrow, and the currently available public substrate cannot anchor the sensitivity parameters well enough. C009 should therefore be preserved for possible reuse or revival, but the program should move to the next candidate inside D013 rather than build a full C009 simulation/application project now.

---

# Rule for adding new candidates

Each new candidate must eventually receive:

1. concise question;
2. why it matters;
3. closest prior work;
4. active competitors;
5. explicit differentiation;
6. identification/estimand;
7. data feasibility;
8. computational scope;
9. likely audience/venue;
10. verdict with confidence.

---

# C010 dossier — parked after four-channel prosecution

## Core question

When a nonprobability survey excludes cases flagged as low-quality/bogus and recalibrates the retained cases, when does screening reduce population-estimation error versus add selection bias, and how should imperfect screen performance affect threshold choice and uncertainty?

## Four-channel result

- **Literature-generated:** strong evidence that bogus/careless response and representativeness interact, but direct exclusion-before-reweighting work already exists [R125–R128].
- **Theory-generated:** filtering is a second selection event. Under ideal calibration on `X`, error separates into retained response contamination plus residual selection among retained cases.
- **Data-generated:** Pew/Gallup studies show screening can improve some data-quality metrics while removing valid cases, changing demographic composition, or worsening specific benchmark estimates [R129–R133].
- **Decision-generated:** analysts genuinely must choose whether/how aggressively to filter before weighting; AAPOR and practitioner activity confirm current demand [R139–R140].

## Broad novelty failure

R127 directly demonstrates that excluding satisficers before recalculating weights can reduce average absolute bias across four nonprobability online panels. C010 therefore cannot claim the generic “quality filtering + weighting improves opt-in inference” proposition.

## Narrowed surviving object

Treat pass/fail screening as an imperfect classifier layered on the original NPS participation mechanism and analyze the downstream estimand rather than only classification accuracy. The post-filter calibrated error can be organized as:

`retained response contamination + residual selection among retained cases`.

The interesting residual question is whether the post-filter calibration structure yields a distinctive identification/partial-identification or estimand-targeted threshold rule under false-positive/false-negative screening.

## Major threats

- Mathur [R128] already formalizes selection bias from attention-check exclusion.
- Sen & Lahiri [R126] directly study measurement error and representativeness in nonprobability surveys.
- careless-response detection/cleaning has mature review literature [R135–R138].
- no-gold-standard classifier accuracy is an established latent-class/partial-identification problem [R141, R121].
- public data can illustrate filtering effects but do not generally identify true respondent-level quality status.

## Data/compute

Compute burden is low. Pew 2020 [R133–R134] is a plausible public illustration substrate after account access. R127 is directly aligned but its underlying data are not publicly shareable. The main constraint is validation information, not computation.

## Reopening conditions

Reopen only with credible respondent-quality validation labels/design, a structure-specific identification theorem or materially tighter bounds, a genuinely new estimand-targeted threshold decision rule, or a high-value agency application whose validation information anchors classifier error.

## Current verdict

**PARKED / NO-GO FOR FIRST PROJECT.**

**Confidence:** moderately high.

Full record: `14_C010_RESPONSE_QUALITY_FILTERING_PROSECUTION.md`.

---

# C011 dossier — survived OF-45 national empirical prosecution

## 1. Concise question

> When HUD applies its post-2016 `<50%` ACS relative-margin-of-error screen to Qualified Census Tract designation, how much precision is purchased by excluding noisier small-area estimates, how is the resulting eligibility/designation burden distributed by tract population after accounting for substantive-threshold proximity, and how does the statutory 20% cap reallocate designation to other tracts?

## 2. Why it matters

QCT designation is part of the federal Low-Income Housing Tax Credit geography and can affect the basis treatment of housing investment [R267]. HUD explicitly tightened its ACS reliability screen in 2016 [R271], while Treasury separately recognizes that ACS precision rules can disadvantage lower-population geographies [R268]. A rule intended to prevent sampling-error anomalies is therefore also a selective coverage intervention with real allocation consequences.

The D033 2026 replay shows that this is not a theoretical edge case: changing only the MoER threshold changes 2,825 final QCT statuses relative to the looser-screen counterfactual and removes eligibility from 2,043 records.

## 3. Closest prior work

- **R269:** HUD/Census already establishes that QCT misclassification is worse for smaller tracts, that false inclusion/exclusion trade off, and that the 20% cap complicates error handling. C011 cannot claim those generic facts.
- **R270:** ACS threshold-based program eligibility instability is already documented outside the current precision-screen evaluation.
- **R274:** selective classification can improve average reliability while magnifying disparities; this is an abstract ancestor.
- **R278:** Soltas is the closest active empirical neighbor. He reconstructs QCT assignment, incorporates high-sampling-error disqualifications and the cap, and simulates ACS noise for LIHTC identification. He does not evaluate the post-2016 precision gate as the policy object.

## 4. Active competitors / monitoring set

The primary active-monitoring target is Soltas [R278] and any follow-on LIHTC/QCT work that turns the sampling-error disqualification itself into an estimand. HUD PD&R/Census methodology changes to QCT designation and Treasury small-area eligibility guidance are also monitoring sources [R267–R272]. Discovery-mode searching is no longer justified unless this monitoring surfaces direct occupation.

## 5. Explicit differentiation

C011 does **not** ask whether ACS noise can change QCT assignment. It evaluates a specific modern reliability intervention: the 2016 tightening from `<100%` to `<50%` relative MoE.

The contribution is a reproducible national **precision-screen failure/decision analysis** that (i) isolates the screen with a same-data counterfactual, (ii) quantifies population-conditioned selective coverage after controlling for substantive-threshold distance, (iii) separates direct eligibility loss from ranking/cap displacement, including strict nonlocal gains, and (iv) states exactly which claims about latent classification accuracy are not identified.

## 6. Identification / estimands

Primary identified policy map:

`D_y(c) = HUD_QCT_algorithm(observed year-y tract estimates, MoEs, income limits, populations; c)`.

Primary contrast:

`D_y(0.50) - D_y(1.00)`.

Decomposition targets:

1. release-level precision-screen passage;
2. income/poverty criterion eligibility;
3. union eligibility;
4. ranking changes among eligible records;
5. direct final designation losses;
6. final changes among still-eligible records; and
7. strict nonlocal cap/ranking changes for records whose own screen indicators are unchanged.

Population-burden target: loss probability/rate as a function of tract population conditional on two-of-three substantive-threshold distance.

**Not identified without additional assumptions:** correctness relative to latent true tract income/poverty status or the true false-inclusion/false-exclusion reduction. Consecutive ACS 5-year releases overlap and marginal MoEs do not identify their joint error covariance or a fixed latent tract state [R276–R277].

## 7. Data feasibility

**PASS.** The public HUD all-tract workbook is available annually [R272]. The project-local 2026 file [R280] contains 85,390 QCT records and reproduces the official algorithm exactly. A full project can extend the same within-year replay to historical annual QCT workbooks without requiring confidential data.

## 8. Computational scope

**LOW / FEASIBLE.** The core analysis is deterministic tabular replay over roughly 85k records per year plus modest regression/stratification. No large-model training, GPU compute or restricted cluster is required. The main technical requirement is careful versioned rule reconstruction and reproducibility, not computational scale.

## 9. Likely audience / venue

Primary audiences: survey/small-area estimation and official statistics; applied statistics/data science concerned with decision reliability; housing/public-finance and policy researchers using QCT/LIHTC geography.

Plausible venues after execution quality is known include *Journal of Survey Statistics and Methodology*, *Journal of Official Statistics*, *Statistics and Public Policy*, or an applied housing/public-finance outlet. Venue choice should follow the final balance between methodological generalization and QCT-specific policy evidence.

## 10. Verdict with confidence

> **SURVIVES / NARROWED EXACT-YEAR PAPER / FIRST-PAPER PRIORITY RETAINED.**

**Confidence:** moderate.

The candidate survived its later D035 reconstruction stop under D036, but with a lower ceiling than at promotion. The admissible paper is now restricted to the exact confirmatory years 2016, 2020, 2021 and 2022, with 2026 retained as development context. The contribution remains consequential and differentiated, but temporal generalizability is limited and reconstruction-selection is the principal inferential limitation.

## D033 empirical anchor

Using the 2026 all-tract workbook [R280]:

- exact `c=0.50` reconstruction: **0 mismatches / 85,390 records**;
- eligible records: 19,253 at `c=1.00` vs 17,210 at `c=0.50`;
- final QCTs: 15,797 vs 14,496;
- final-status changes: 2,063 losses + 762 gains;
- smallest-to-largest old-eligible population-decile loss: 21.8% vs 5.3%;
- adjusted odds ratio per population doubling: 0.447 (95% CI 0.383–0.522);
- cap-binding areas: 144 vs 104;
- strict nonlocal gains with unchanged own screen indicators: 332 across 87 areas / 32 states.

Full empirical record: `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`, D033.

---

## Historical pipeline status after OF-19–OF-23 triage

The bounded opportunity slate was screened collapse-first in `15_OF19_OF23_COLLAPSE_TRIAGE.md`.

**No C011 has been assigned.** OF-19, OF-20, OF-21 and OF-23 were parked in broad/generic form. OF-22 retains a narrower intermittent-probability-anchor drift question as **WATCHLIST / SHARPEN BEFORE CANDIDATE**, but it has not satisfied the candidate acceptance gate.

Candidate numbering is intentionally non-automatic: the next identifier is created only when a new or sharpened opportunity earns promotion.

## Pipeline status after fresh D013 opportunity generation

The fresh four-channel pass is recorded in `16_D013_FRESH_OPPORTUNITY_GENERATION.md`.

**C011 remains unassigned.** The program now has one pre-candidate priority lead:

> **OF-30 — finite-benchmark certification / benchmark-to-target transportability — PRIORITY SCREENING.**

OF-30 has not earned a candidate dossier because direct novelty and certificate identification remain unresolved. Its next gate is intentionally bounded to nearest-neighbor literature, benchmark-holdout data feasibility, and theory differentiation.

OF-31 remains a mechanism inside OF-30. OF-32 is watchlist-only. OF-33 and OF-34 are parked in broad form.

Candidate numbering remains non-automatic. If and only if OF-30 survives its screening gate, it may be promoted as C011 with a formal candidate dossier.

## Pipeline status after OF-30 bounded screening

The bounded gate is complete in `17_OF30_BOUNDED_SCREENING.md`.

**C011 remains unassigned.**

OF-30 is now **PARKED AFTER BOUNDED SCREENING**. It passed the data-feasibility gate but failed the first-project theory/novelty gate: survey-level versus statistic-level bias is already explicit in R-indicator/outcome-specific selection-bias work [R161–R164], and the natural formal repairs lead to existing function-class balance or generic benchmark-prediction theory [R165, R168].

OF-31 is not promoted separately. Its valid contribution is a protocol requirement—nested tuning/certification/validation and grouped holdout—not a distinct candidate.

The next candidate identifier remains C011 and will be assigned only when a fresh/sharpened opportunity clears the Charter gate.

## Pipeline status after cross-field review-first reconnaissance

The bounded cross-field pass is recorded in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md` and governed by D022.

**C011 remains unassigned.** No new candidate dossier has been created.

The sole current pre-candidate prosecution lead is:

> **OF-35 — prediction-evaluation ranking reliability under interval censoring / imperfect assessment — PRIORITY PROSECUTION LEAD.**

The lead is deliberately framed as a model-selection/evaluation-reliability problem rather than a new scoring-rule proposal. Direct interval-censored prediction-evaluation methods already exist [R182–R185], and right-censoring work already demonstrates ranking reversals and dependent-censoring evaluation failures [R179–R180]. OF-35 can become C011 only if the interval-censoring/assessment-process structure yields a distinct failure law, estimand or decision result after nearest-neighbor prosecution.

Synthetic-data inference is retained as a high-competition watchlist area [R170–R173]. The broad meta-analysis content-coverage lead is collapsed by tolerance-interval ancestors [R174–R175].

## Pipeline status after OF-35 bounded prosecution

The prosecution is complete in `19_OF35_INTERVAL_CENSORING_RANKING_PROSECUTION.md`.

**C011 remains unassigned.** No execution project has been created.

OF-35 is **PARKED / NO-GO FOR FIRST PROJECT**. The direct overlap is now too strong: Yang et al. already generate exact-event oracle and observed-data metrics for three competing interval-censored prediction models [R183], while Bahrini et al. directly study censoring-induced survival-model ranking distortion using oracle event times [R189]. Current interval-censoring scoring theory and informative Case-K model-selection/model-averaging work further crowd the only plausible narrowing [R190–R192].

The residual OF-38 question—sensitivity/partial ranking under genuinely informative Case-K assessment—is watchlist-only and too theory-heavy/occupied to justify automatic C011 promotion.

The next candidate identifier remains C011 and will be assigned only after a fresh review-first opportunity clears the novelty, mechanism, feasibility and decision gates.

## Pipeline status after D024 cross-field opportunity generation II

D024 is recorded in the consolidated D024 record in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

**C011 remains unassigned. No execution project has been created.**

The sole current pre-candidate prosecution lead is:

> **OF-39 — calibration of Bradley–Terry diagnostics under outcome-adaptive comparison scheduling — PRIORITY PROSECUTION LEAD / NOT C011.**

The candidate gate is intentionally strict. Hamilton & Tawn already establish adaptive-schedule non-ancillarity and a scheduler-replay bootstrap for Bradley–Terry estimation [R195]; Wu et al. already provide the diagnostics [R196]; and response-adaptive GOF has a classical ancestor [R197]. OF-39 earns C011 only if the bounded prosecution establishes a distinct diagnostic-calibration failure/result tied to the endogenous paired-comparison graph and a principled remedy or validity argument.

Other D024 leads remain outside the candidate registry:

- **OF-40:** source-aware spatial-fusion validation — WATCHLIST;
- **OF-41:** partial identification of probabilistic validation under misclassified outcomes — THEORY WATCHLIST;
- **OF-42:** count-time-series parametric GOF under underreporting — PARKED/SECONDARY;
- **OF-43:** conditional extremes × covariate measurement error — THEORY WATCHLIST.

The next candidate identifier remains **C011** and will be assigned only after a lead clears the Charter novelty, mechanism, feasibility and decision gates.

## Pipeline status after D025 OF-39 prosecution

**C011 remains unassigned. No execution project has been created.**

OF-39 survived its bounded prosecution only after narrowing. The live object is no longer the generic proposition that adaptive scheduling invalidates Bradley–Terry diagnostics. The prosecution instead isolated a finite-sample distinction between **joint adaptive/replay calibration** and **conditioning on the non-ancillary final comparison graph**.

This is not yet a candidate dossier because scheduler replay is already prior art for estimation [R195], sparse GLM GOF is a separate classical threat [R214], and no distinct validity theorem or empirical adaptive-scheduler illustration has yet been established.

The next candidate identifier remains **C011**. OF-39 may receive it only after the exact-enumeration/theorem gate in the consolidated OF-39 prosecution in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

## Pipeline status after D026 exact OF-39 theorem gate

**C011 remains unassigned. No execution project has been created.**

OF-39 is no longer the active pre-candidate lead. Exact four-object enumeration proved the finite-sample mechanism: conditioning on an outcome-generated final graph truncates the Bradley–Terry null path space, and frozen-final-graph exact calibration can differ materially from scheduler replay even with known parameters.

The contribution gate nevertheless fails. Hamilton & Tawn [R195] already establish adaptive-schedule non-ancillarity and scheduler replay for estimation; the exact truncation law is a direct finite-state consequence of that mechanism, while exact replay validity is generic. Yi & Wang [R197] occupies the broad adaptive-GOF principle.

> **OF-39 — PARKED / MECHANISM ESTABLISHED, DISTINCT CONTRIBUTION NOT ESTABLISHED.**

Reopening conditions are recorded in the consolidated OF-39 exact gate in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`. The next candidate identifier remains **C011**, to be assigned only after a future lead independently clears the Charter gates.



## Pipeline status after D028 OF-44 bounded screening

**C011 remains unassigned. No execution project has been created.**

> **OF-44 — downstream inferential reliability under heterogeneous 1997↔2024 SPD-15 bridging — PARKED / NO-GO FOR FIRST PROJECT.**

The substantive reliability problem remains important [R222–R225], but P1 found that the proposed sharp sensitivity/robustness object is already contained at the abstract level in direct misclassification partial-identification machinery for restricted transition matrices and arbitrary functionals [R228], with additional direct rate-ratio matrix-method ancestry [R229]. P2 found public national bridge inputs but insufficient public dual-coded evidence to constrain the key geography/nativity/time bridge heterogeneity needed for a defensible first-project analysis [R223–R224, R230].

P3 and P4 were deliberately not run after P1 failed. OF-44 can be reopened only if a new structural restriction, estimand, design, or newly public validation substrate creates a contribution not mechanically inherited from generic misclassification-matrix sensitivity analysis.

The modeled-gridded-population/PPS uncertainty lead was **collapsed before registration** because its abstract object is established imperfect frame/measure-of-size sampling [R219–R221].

The next candidate identifier remains **C011**.


## Pipeline status after D029 review-first generation IV

**C011 remains unassigned. No execution project has been created.**

D029 screened seven cross-field routes and registered **no new OF identifier**. Each route failed before candidate formation because the exact reliability problem was already directly studied, had mature statistical ancestry, or had unfavorable active-work competition [R231–R246].

This is a valid pipeline state, not a reason to lower the acceptance gate. No route from D029 enters SCREENING, PROSECUTION or EXECUTION.

The next candidate identifier remains **C011** and must not be assigned by quota. The next discovery pass will deliberately diversify away from repeatedly sampled biomedical prediction/evidence-synthesis/harmonization neighborhoods.

## Pipeline status after D030 diversified review-first reconnaissance

**C011 remains unassigned. No execution project has been created.**

D030 deliberately sampled five distant statistical domains—official statistics, experimental design, statistical computing/numerical reliability, environmental/spatial statistics and social-science measurement—and again registered **no new OF identifier** [R247–R260]. Each plausible seam failed before candidate formation because the exact reliability object was already systematized, directly studied, classically inherited or under unfavorable active competition.

This second null does **not** justify lowering the candidate gate. It changes the discovery mode. The next pass must use theory-, data- and decision-generated channels and require independent-channel convergence before opportunity registration.

The next candidate identifier remains **C011** and must not be assigned by quota.

## Pipeline status after D031 independent-channel triangulation

**C011 remains unassigned. No execution project has been created.**

> **OF-45 — reliability-versus-coverage consequences of HUD's post-2016 ACS precision screen in Qualified Census Tract designation — PRIORITY BOUNDED PROSECUTION / NOT C011.**

OF-45 is the first opportunity registered after the D029–D030 null sequence because **three independent discovery channels converge**: a live agency decision tension between reliability screening and lower-population geographic coverage [R267–R268], public all-tract inputs plus exact designation logic [R271–R272], and a first-principles selective-coverage mechanism whose pass probability is precision-dependent.

The registration does not claim that ACS sampling error in QCT designation is new. HUD's own earlier analysis already established population-dependent misclassification, false-inclusion/false-exclusion tradeoffs and 20% cap complications [R269]; Brown and Scardamalia document threshold-program instability across ACS releases [R270]; selective-classification work provides an abstract disparity ancestor [R274]; and Soltas directly simulates QCT designation changes from ACS sampling variation while reconstructing HUD's assignment rule [R273].

The only live contribution is the **post-2016 policy-screen evaluation**: isolate what tightening the reliability threshold from <100% MoER to approximately <=50% changed in tract-level screen coverage and final designation, including low-population burden and cap displacement, while distinguishing directly identifiable designation effects from model-dependent claims about true classification error.

**Promotion gate before C011:** OF-45 must survive exact public-data reconstruction, population-gradient diagnostics, cap-displacement accounting, and a defensible treatment of dependence across overlapping ACS releases. If the observed consequences are negligible, explained entirely by substantive-threshold proximity, or require unverifiable latent-truth assumptions to make the central claim, park OF-45.

The next candidate identifier remains **C011** and must not be assigned until this gate is complete.

## Pipeline status after D032 OF-45 rule/identification gate

**C011 remains unassigned. No execution project has been created.**

> **OF-45 — PRIORITY BOUNDED PROSECUTION / EMPIRICAL MAGNITUDE GATE UNRESOLVED / NOT C011.**

D032 clears two pieces of prosecution and narrows the third. The historical/current screen can be reconstructed exactly enough for a same-data policy replay [R271, R275, R272]. The design-identifiable estimand is the change in eligibility/ranking/designation induced by replacing `c=0.50` with `c=1.00` while holding the modern algorithm and data fixed. Actual reduction in latent false inclusion/false exclusion is not identified from marginal MoEs because consecutive ACS 5-year releases overlap and should not be treated as independent [R276–R277].

The May 2026 Soltas version remains the closest active empirical neighbor [R278]. It prevents novelty claims based on QCT reconstruction or generic ACS-noise simulation but still does not evaluate the precision screen itself as the policy object.

The decisive promotion evidence is still missing: the nationwide all-tract artifact must be replayed to establish effect magnitude, conditional population gradient and cap-mediated displacement. A Florida ArcGIS mirror [R279] confirms the expected input schema but cannot substitute for the national test.

**Promotion/kill status:** unchanged in substance. Do not assign C011 until the national replay shows consequential screen-induced coverage/designation effects that survive conditioning on substantive-threshold proximity. Park OF-45 if those effects are negligible or if the only central claim left is a model-dependent latent-accuracy statement.

## Pipeline status after D033 OF-45 national empirical gate

**C011 is now assigned. No execution project has yet been created.**

> **C011 — precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation — SURVIVES / PRE-EXECUTION.**

The exact national 2026 replay clears the promotion gate that D031/D032 intentionally left unresolved. The `c=0.50` implementation reproduces all published QCT flags; the tighter screen has consequential eligibility/designation effects; the lower-population burden persists after substantive-threshold conditioning; and the 20% cap creates nonlocal designation reallocation. The central claim remains the identified precision/coverage policy effect, not latent-truth accuracy.

Primary-project discovery now stops under the Charter. The next action is to freeze the C011 execution protocol and only then move to repository-backed execution.

## Pipeline status after D034 C011 protocol freeze

> **C011 — precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation — SURVIVES / PROTOCOL FROZEN / REPOSITORY-READY.**

The prospective protocol is frozen in `20_C011_EXECUTION_PROTOCOL.md`. The already-seen 2026 national replay is the development/anchor year; 2016–2025 are reserved as the confirmatory replication set. Primary annual estimands, threshold-distance adjustment, five-way designation decomposition, robustness analyses and stop criteria are fixed before historical outcomes are inspected.

The core contribution remains the identified precision/coverage/designation policy effect. Latent true-classification accuracy is excluded from the core protocol and cannot be introduced without a separate amendment.

Repository initialization is now authorized, but C011 does not enter full `EXECUTION` until the canonical snapshot, locked environment, 2026 exact-replay fixture and baseline tests are committed and passing.

## Pipeline status after D035 confirmatory reconstruction stop

> **C011 — precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation — EXECUTION PAUSED / REPLICATION-VIABILITY STOP TRIGGERED / SCOPE REASSESSMENT REQUIRED.**

The frozen 2016–2025 confirmatory program does not clear its pre-specified reconstruction-viability gate. Exact Tier-A replay was achieved for **2016, 2020, 2021 and 2022**. Years **2017, 2018, 2019 and 2023** remain non-exact diagnostics with their `c=1.00` counterfactuals unopened. Because only 2024 and 2025 remain, the maximum possible total is now **6/10**, below the required 7/10.

This does **not** show that the policy mechanism is absent. In the four exact confirmatory years, ELR ranges from 1.537% to 3.955%, CHR from 3.771% to 6.146%, the standardized bottom-versus-top population burden contrast is positive in every year, and strict nonlocal cap-mediated changes occur in every year. The protocol's consequentiality weakening criterion is not met because median CHR remains well above 2%.

The failure is instead that the decade-wide confirmatory claim cannot be supported under the frozen exact-reconstruction requirement using currently available public operational inputs. The non-exact years expose historical provenance gaps rather than a common effect-size null.

C011 is therefore **not automatically parked**. Its next gate is a bounded scope reassessment with only three admissible outcomes:

1. narrow to a transparently validated-year QCT paper if novelty/decision value remains sufficient without decade-generalization language;
2. conditionally reopen reconstruction only if new authoritative operational material independently resolves at least one non-exact year to Tier A; or
3. park C011 as the first project and return to discovery if neither route is strong enough.

Do not inspect 2024–2025, weaken the zero-mismatch gate, or use non-exact-year counterfactuals before that reassessment.


## Pipeline status after D036 narrowed-scope freeze

> **C011 — precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation — SURVIVES / NARROWED EXACT-YEAR PAPER / FIRST-PAPER PRIORITY RETAINED.**

D036 selects the narrowed-paper path after the D035 7/10 reconstruction stop. The original decade-wide confirmatory claim is permanently abandoned under the present evidence base; this status does not reinterpret the four exact years as a random or representative subset of 2016–2025.

### Admissible manuscript evidence

- 2026: development/anchor only.
- 2016, 2020, 2021, 2022: exact confirmatory evidence.
- 2017, 2018, 2019, 2023: provenance/diagnostic only; no counterfactual inference.
- 2024, 2025: unopened.

The exact-year mechanism is recurring: eligibility loss is positive, BRD is positive and strict nonlocal designation displacement occurs in every exact confirmatory year. Exact-year medians/ranges may be reported descriptively **among validated years only**, not as estimates of the full 2016–2025 distribution.

### Principal limitation

Admission is reconstruction-based. The non-exact years were not excluded after observing weak counterfactual effects—their `c=1.00` gates remained closed—but reconstructability may correlate with operational complexity, geography and cap behavior. The paper therefore makes no missing-at-random or representativeness claim and must display all ten frozen years' reconstruction status in the main text.

Further reverse engineering of non-exact years is closed unless genuinely new authoritative operational evidence appears. The narrowed project remains first-paper priority because no currently vetted alternative has a stronger demonstrated contribution/feasibility combination.

## Pipeline status after D037 final reproducibility adjudication

> **C011 — precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation — PARKED / NO-GO FOR FIRST PAPER UNDER CURRENT EVIDENCE / REOPEN ONLY WITH MATERIALLY NEW AUTHORITATIVE OPERATIONAL PROVENANCE.**

D037 supersedes D036 as the controlling manuscript disposition. The final reproducibility artifact at Git commit `bdab3ffa12af914c7cfa9e549d26c14043baa0b8` found only 2016 fully reproducible and manuscript-admissible. The historical Tier-A classifications for 2020, 2021 and 2022 remain part of the execution record but are not current manuscript evidence because their operational implementations cannot be independently regenerated from retained provenance. The 2026 development result is likewise not manuscript-supporting counterfactual evidence.

C011 is not scientifically falsified: the 2016 replay fully reproduces the precision-screen mechanism. But one admissible year cannot sustain D036's recurrence claim, and the project will not be reduced to a one-year paper for momentum. The decade claim closed under D035; the narrowed four-year manuscript now closes under D037.

Routine reconstruction and reverse engineering are closed. Reopen only with materially new authoritative operational provenance—such as original HUD code, historical operational scripts, preserved intermediate ranking/allocation files, original validated C011 artifacts/configurations, or equivalent first-party documentation—not with additional manipulation of the same public inputs.

## C012 dossier — killed after final narrowed prosecution

### Object prosecuted

Select disclosure-safe aggregate releases to maximize the number or value of ranking, top-*k* and threshold decisions that are invariant over the compatible confidential-table fiber.

### Useful results preserved

The certification utility is monotone under nested feasible sets, generally neither submodular nor supermodular, can exhibit safe-release synergy, can certify decisions without identifying cells, and can choose releases disjoint from cell-width-optimal choices.

### Binding failure

The action space, risk constraint and release optimizer are inherited from established disclosure-control and workload-aware publication frameworks. Substituting a nonlinear task utility did not yield a new privacy guarantee, mechanism, identification theory, approximation result, scalable algorithm or inferential contribution. D038 is final. No execution protocol or further narrowing is authorized.

Authoritative record: `21_C012_DECISION_PRESERVING_DISCLOSURE_PROSECUTION.md`.

## C013 dossier — PLACES temporal provenance and interpretability

### Core question

After replacing nominal release time with documented BRFSS source time, removing deterministic carry-forwards, harmonizing definitions and geography/population rules, and respecting reported uncertainty, does a published repeated-release PLACES analysis retain its temporal contrast, ordering, hotspot/set classification or decision statement?

### Contribution boundary

C013 is not a new small-area estimator and does not estimate true local change. It is a reproducible audit of the temporal information actually present in repeated public releases and of how downstream claims change when provenance restrictions are enforced.

### Promotion evidence

- nine eligible temporal-use works under a documented search and deduplication rule;
- a verified 2016–2025 measure/release/source-year crosswalk;
- exact copy blocks in rotating mammography, high-cholesterol and colorectal-screening measures;
- within-study negative controls with distinct source years;
- three bounded reproductions spanning annual trajectory, longitudinal association and pre/post spatial use; and
- no located direct collision combining corpus, crosswalk, exact-copy diagnostics and conclusion-level sensitivity.

### Execution status

**SURVIVES / CONTROLLED EXECUTION DESIGN.** The frozen protocol is `23_C013_CONTROLLED_EXECUTION_PROTOCOL.md`. Stage 0 provenance archiving and crosswalk construction are authorized. Manuscript drafting is not.

Authoritative prosecution: `22_C013_PLACES_TEMPORAL_PROSECUTION.md`.

## Change log

### 0.26.0 — 2026-09-21

- Registered C013 as **SURVIVES / CONTROLLED EXECUTION DESIGN** and added its bounded dossier.

### 0.25.0 — 2026-09-17

- Added C012 and its final **KILLED / NO-GO FOR FIRST PAPER** disposition.

### 0.24.0 — 2026-09-17
- Added D037 and parked C011 as the first-paper project under the final manuscript reproducibility adjudication.
- Preserved the 2016 mechanism result, distinguished historical Tier-A status from manuscript admissibility, and limited reopening to materially new authoritative operational provenance.

### 0.23.0 — 2026-09-09
- Added D036 narrowed-paper disposition and changed C011 to **SURVIVES / NARROWED EXACT-YEAR PAPER / FIRST-PAPER PRIORITY RETAINED**.
- Froze the admissible exact-year evidence set and reconstruction-selection limitation; routine historical rescue is closed.

### 0.22.0 — 2026-09-09
- Added D035 execution disposition for C011: 7/10 replication viability is mathematically unattainable under the frozen program after 2023 remains non-exact.
- Reclassified C011 to **EXECUTION PAUSED / REPLICATION-VIABILITY STOP TRIGGERED / SCOPE REASSESSMENT REQUIRED** rather than automatically parking the candidate.

### 0.21.0 — 2026-09-08
- Added D034 protocol-freeze state for C011 and marked it **SURVIVES / PROTOCOL FROZEN / REPOSITORY-READY**.
- Reserved 2016–2025 for confirmation and made passing repository/2026 regression tests the condition before full EXECUTION.

### 0.20.0 — 2026-09-08
- Promoted OF-45 to **C011 — SURVIVES / PRE-EXECUTION** after the D033 national empirical gate.
- Added the formal ten-part C011 candidate dossier and exact empirical anchor.
- Ended discovery-mode searching for the primary project; next step is protocol freeze, then repository-backed execution.

### 0.20.0 — 2026-09-08

- Added D032 bounded-gate state for OF-45.
- Kept OF-45 pre-candidate and C011 unassigned because the national empirical magnitude gate remains unresolved.
- Recorded the identified policy-replay estimand and the nonidentified latent-accuracy boundary.

### 0.19.0 — 2026-09-08

- Recorded D031 and OF-45 as a pre-candidate **PRIORITY BOUNDED PROSECUTION** lead.
- Kept C011 unassigned and execution unauthorized.
- Added the exact public-data/identification promotion-and-kill gate for the post-2016 QCT precision-screen question.

### 0.18.0 — 2026-09-08

- Recorded D030 as a second valid null-generation pass across five deliberately diversified domains.
- Created no OF-45 and no C011.
- Changed the next discovery mode to bounded theory/data/decision-channel triangulation.

### 0.17.0 — 2026-09-08

- Recorded D029 as a valid null-generation pass: no OF registration and no C011.
- Preserved the acceptance gate and redirected discovery toward deliberately diversified statistical domains.

### 0.16.0 — 2026-09-08

- Parked OF-44 after D028 bounded screening; no C011 assigned.
- Recorded P1 theorem-level occupation, P2 public-data limitation, and P3/P4 stop-rule application.

### 0.15.0 — 2026-09-08

- Added D027 pipeline state and OF-44 as the sole bounded-screening lead; C011 remains unassigned.
- Recorded collapse of the generic gridded-population/PPS uncertainty lead.

### 0.14.0 — 2026-09-08

- Recorded D026: OF-39 parked after exact enumeration proved the mechanism but not a distinct contribution.
- Kept C011 unassigned and removed OF-39 from active pre-candidate status.

### 0.13.0 — 2026-09-08

- Recorded D025 prosecution state: OF-39 survives narrowed, but C011 remains unassigned.
- Added exact-enumeration/theorem gate as the condition for any future candidate promotion.

### 0.12.0 — 2026-09-08

- Recorded the D024 pipeline state and OF-39 as a pre-candidate prosecution lead.
- Kept C011 unassigned and OF-40–OF-43 outside the candidate registry pending their stated reopening gates.

### 0.11.0 — 2026-09-07

- Parked OF-35 after bounded prosecution and kept C011 unassigned.
- Preserved OF-38 only as a theory-heavy watchlist residue.

### 0.10.0 — 2026-09-07

- Recorded OF-35 as the sole current pre-candidate prosecution lead after cross-field reconnaissance.
- Kept C011 unassigned and preserved synthetic-data inference as watchlist rather than candidate.

### 0.9.0 — 2026-09-07

- Recorded OF-30 as parked after screening and kept C011 unassigned.

### 0.8.0 — 2026-09-07

- Recorded OF-30 as the new pre-candidate **PRIORITY SCREENING** lead.
- Kept C011 unassigned pending a bounded novelty/data/theory gate.
- Recorded OF-31–OF-34 as sub-lead/watchlist/parked rather than forcing new candidates.

### 0.7.0 — 2026-09-07

- Recorded that OF-19–OF-23 triage produced no C011.
- Kept OF-22 as a watchlist residue rather than a candidate.
- Reaffirmed that candidate IDs are assigned only after promotion gates are met.

### 0.6.0 — 2026-09-07

- Added C010 to the registry.
- Completed four-channel prosecution and classified C010 **PARKED / NO-GO FOR FIRST PROJECT**.
- Preserved the post-filter error decomposition and reopening conditions.

### 0.5.0 — 2026-09-07

- Completed C009 stage-2 bounded-mismatch/partial-identification prosecution.
- Reclassified C009 as **PARKED / NO-GO FOR FIRST PROJECT**.
- Added the `delta`-`kappa` decision result and the new nearest neighbors R120–R124.

### 0.4.0 — 2026-09-07

- C009 narrowed and moved to PROSECUTION.

### 0.3.0 — 2026-09-07

- Parked C008 / no-go for first project after explicit competitive-geometry reassessment.
- Added C009 as the new priority SCREENING lead from the survey-data-integration map.
- Added full C009 dossier, nearest neighbors, identification warning, public-data substrate, kill/promotion criteria.

### 0.2.0 — 2026-09-07

- Added `IDEA FAMILY` to the formal status vocabulary.
- Reassessed C003–C007 after field mapping.
- Added C008 as the first priority SCREENING candidate.
- Added full C008 dossier with competitors, hypotheses, identification warning, data feasibility, kill and promotion criteria.
