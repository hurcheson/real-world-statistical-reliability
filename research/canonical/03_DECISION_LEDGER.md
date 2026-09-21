---
title: Decision Ledger
version: 0.26.0
last_updated: 2026-09-21
status: active
---

# Decision Ledger

This file records major decisions and why they were made.

---

## D001 — Use one real research case before building a generalized system

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Do not begin by constructing a generic automated research-intelligence platform.

Use one real problem end-to-end, then make repeated components reusable.

### Rationale

The project owner identified a recurring tendency to build systems that are never actually used.

### Revisit if

At least two or three completed research workflows reveal stable repeated steps that justify automation.

---

## D002 — Start the original exploration from Dr. Kristina P. Vatcheva's work

**Date:** 2026-09-07  
**Status:** HISTORICAL

### Decision

Use Dr. Vatcheva's publications as the first test case for evidence-driven research-question discovery.

### Outcome

This produced two serious candidate projects and, more importantly, the novelty-prosecution workflow.

---

## D003 — Reject C001 as the primary project

**Candidate:** Imputation → blood-pressure variability → downstream inference  
**Date:** 2026-09-07  
**Status:** FINAL unless new evidence changes it

### Decision

Do not execute C001 as the main project.

### Reason

The conceptual contribution became too close to existing task-oriented imputation, physiological-sensor missingness, variability-measurement, and downstream-inference literature.

### What would justify reopening

A sharply different estimand, new theoretical result, or unique dataset/design that creates a consequential contribution not captured by existing work.

---

## D004 — Park C002 and classify it as no-go for the first project

**Candidate:** Informative observation → within-person BP variability → outcome modeling  
**Date:** 2026-09-07  
**Status:** PARKED

### Decision

Do not pursue as the first primary project.

### Reason

- core methods already exist in adjacent literatures;
- leading BPV/location-scale papers explicitly identify similar extensions;
- active PhD work directly targets within-subject variability under irregular/informative observation;
- full EHR formulation is methodologically complex;
- identification burden is high;
- competition/scooping risk is high relative to likely novelty.

### What would justify reopening

A methodological-statistics advisor explicitly chooses to supervise the frontier, or a substantially narrower high-value question emerges.

---

## D005 — Stop optimizing for a completely untouched gap

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Use **defensible contribution** rather than “nobody has done this” as the novelty standard.

### Reason

Completely untouched questions are neither necessary nor sufficient for publication. Productive research programs develop meaningful extensions, boundary conditions, validations, methods, and robustness results within active fields.

---

## D006 — Select a research neighborhood before selecting the first paper

**Date:** 2026-09-07  
**Status:** SUPERSEDED by D013 on 2026-09-07

### Decision

Adopt the neighborhood:

> **Reliability and transportability of statistical/ML models under imperfect real-world data.**

### Reason

It aligns Applied Statistics, Data Science, modern ML, public biomedical data, and a broad family of persistent real-world reliability problems.

### Important limitation

This is not yet a specific research question or approved execution project.

---

## D007 — Make persistent Markdown records the research memory

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Maintain compact canonical Markdown records in the ChatGPT Project, later mirrored into Git.

### Reason

Avoid repeated searching, forgotten decisions, token waste, and resurrection of killed ideas.

### Rule

Future research sessions should read the canonical records before new mapping or candidate generation.

---

## D008 — Keep ChatGPT Project lightweight; Git handles detailed version history later

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Use a small set of living canonical files in the Project. Do not create a new source file for every minor thought.

When GitHub execution begins, Git becomes the durable fine-grained version-history layer.

### Rationale

Project source limits and source clutter make duplicate version files inefficient.

---

## D009 — Use measurement / observation-process shift as the first deep field-mapping spine

**Date:** 2026-09-07  
**Status:** HISTORICAL — completed; no longer current neighborhood

### Decision

Within the broader reliability/transportability neighborhood, make the first deep field map around:

> **external predictive reliability under measurement / observation-process shift.**

### Reason

This spine connects calibration, missingness, workflow/informative observation, external validation, subgroup reliability, and deployment monitoring without committing to a single model architecture.

The first deep map also showed that the relevant literature is split across clinical prediction methodology, robust/distribution-shift ML, informative-observation/missingness, and post-deployment monitoring. Mapping the interface is more informative than mapping “distribution shift” as one undifferentiated field.

### Important limitation

This is a **mapping priority**, not an execution-project selection.

---

## D010 — Promote C008 to SCREENING, but do not begin substantive analysis

**Date:** 2026-09-07  
**Status:** SUPERSEDED by D012

### Candidate

**C008 — Measurement-process-aware external-validation stress testing for clinical prediction models**

### Decision

Treat C008 as the current **priority screening lead**.

Do not promote it to PROSECUTION, SURVIVES, or EXECUTION yet.

### Reason

The field map found a plausible under-connected interface: external-validation rigor plus explicit observation-process shift plus calibration/decision utility plus robustness/stress testing.

However, the map also found unusually close prior art and active competition, especially:

- general conditional/context shift stress testing;
- predictor measurement heterogeneity;
- deployment-compatible missing-data validation;
- missingness-shift robustness;
- clinical presence shift;
- 2026 MIMIC/eICU work directly linking observation-process features to external calibration loss;
- 2026 MIMIC/eICU calibration, recalibration, decision-curve and subgroup validation.

Therefore the correct next move is **adversarial nearest-neighbor prosecution**, not coding.

### Promotion condition

C008 may move to PROSECUTION only after:

1. a precise estimand/evaluation object is fixed;
2. the nearest-neighbor matrix demonstrates a consequential uncaptured claim;
3. realistic observation-process stress tests/environments are feasible;
4. data access and scope remain appropriate for a first project.

### Kill condition

Kill or reshape C008 quickly if the differentiator reduces to:

- another MIMIC/eICU external validation;
- more metrics/models/datasets;
- arbitrary missing-value masking;
- another demonstration of calibration drift;
- a causal attribution claim unsupported by the design.

---

## D011 — Maintain a structured reference/search evidence ledger for deep mapping

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Add `11_REFERENCE_LEDGER.md` as a canonical evidence record for deep field mapping and candidate prosecution.

### Reason

The project now requires traceability beyond narrative Markdown. The ledger records:

- stable reference IDs;
- primary URLs/DOIs;
- evidence type;
- what each source establishes;
- what it does not establish;
- representative search queries;
- search limitations;
- active-preprint status.

### Rule

The ledger supports research discovery and reproducibility, but manuscript/proposal claims must still be re-verified against current primary sources.

---


## D012 — Park C008 as a no-go for the first project and reopen field selection

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Move C008 from SCREENING to **PARKED / NO-GO FOR FIRST PROJECT** and reopen the first-project research neighborhood.

### Reason

The first deep map did not show that observation-process reliability is unimportant. It showed unfavorable **competitive geometry and expertise burden** for a first independent project:

- multiple 2025–2026 direct neighbors already occupy the central empirical/methodological objects;
- credible differentiation would require a broad stack spanning clinical prediction, EHR processes, missingness, transportability, calibration, causal/stress-test reasoning and multi-database execution;
- the technical ramp and competitive risk are disproportionate to the expected marginal contribution under current resources.

This is an application of the charter's kill/park rule, not a judgment that one must avoid fields with famous researchers.

### Reopen C008 if

A narrower contribution emerges with materially lower burden, or supervision/resources make the frontier attractive.

---

## D013 — Adopt survey data integration / nonprobability inference as the active first-project neighborhood

**Date:** 2026-09-07  
**Status:** SUPERSEDED FOR ACTIVE DISCOVERY BY D022

### Decision

For first-project discovery, adopt:

> **Finite-population inference from integrated probability and nonprobability data sources, with emphasis on selection, measurement compatibility and robustness of adjustment.**

This supersedes D006 as the **active first-project neighborhood** while preserving D006 and its field map as research history.

### Evidence

The second deep field map (`12_SURVEY_DATA_INTEGRATION_FIELD_MAP.md`) found:

- durable importance in official statistics and survey methodology [R061–R063, R100–R102];
- a coherent statistical core rather than a broad multi-domain ML stack;
- public paired probability/nonprobability data through RANDS [R092–R099];
- laptop/workstation computational feasibility and mature R tooling [R108–R112];
- active but navigable competition;
- several obvious ideas already occupied, allowing an evidence-based narrowing rather than artificial gap hunting.

### Scope limitation

This is a research neighborhood, not an execution-project approval.

---

## D014 — Promote C009 to SCREENING only

**Date:** 2026-09-07  
**Status:** SUPERSEDED BY D016

### Candidate

**C009 — Cross-source measurement mismatch in nonprobability-sample adjustment**

### Decision

Treat C009 as the **priority SCREENING lead**. Do not move to PROSECUTION or substantive execution yet.

### Reason

Standard P/NPS integration relies on shared auxiliary variables, while empirical evidence shows measurement equivalence can fail across P/NP panels [R087]. Close selection×misclassification work explicitly retains an assumption that participation covariates are measured without error in both sources [R088]. This creates a plausible interface with measurement-error/IPW theory [R089].

### Promotion condition

Before PROSECUTION:

1. fix a finite-population estimand;
2. formalize a source-specific measurement model;
3. classify identification under no-validation / known-error / bridge-validation information;
4. derive the naive estimator's target/bias;
5. test mathematical equivalence against R089 and older calibration-with-error literature;
6. audit RANDS variable provenance for a credible empirical demonstration.

### Kill condition

Kill/reshape if the result is a trivial application of existing error-prone-IPW/calibration theory, requires unrealistic gold-standard data, or cannot support informative sensitivity analysis.

---

## D015 — Keep the historical project/container name until an execution project survives

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Broaden the scientific charter to **real-world statistical reliability**, but do not spend effort renaming repositories/projects or rebuilding infrastructure while no execution project exists.

### Reason

The active scientific neighborhood has moved beyond ML, but D001's anti-overengineering principle still applies. Rename/migrate the external repository when a specific project survives and execution begins.



## D016 — Narrow C009 and advance only the interaction-specific formulation to PROSECUTION

**Date:** 2026-09-07  
**Status:** SUPERSEDED BY D017

### Decision

The broad C009 framing — “cross-source measurement mismatch in nonprobability-sample adjustment” as a generally unaddressed problem — **fails the nearest-neighbor novelty test** and must not be used as a novelty claim.

Preserve the C009 identifier for lineage, but narrow its active formulation to:

> **P/NPS calibration under cross-source auxiliary-scale mismatch: separate wrong-benchmark-scale bias from residual proxy-selection bias, then characterize identification/sensitivity by information regime.**

Advance this narrowed formulation to **PROSECUTION — NARROWED**. Do **not** promote to `SURVIVES` or `EXECUTION`.

### Evidence

- Chambers [R113] directly studies erroneous and closely related but non-identical auxiliary controls in survey calibration and shows that substitution can induce substantial bias.
- Hong, Rudolph & Stuart [R114] directly study differential measurement error in propensity-score covariates.
- McCaffrey et al. [R089] establish corrected IPW with error-prone covariates.
- Kim & Tam [R115] combine finite-population data integration with measurement-error problems.
- The C009 toy prosecution nevertheless yields an exact P/NPS-specific decomposition of wrong-scale benchmark bias versus residual proxy-selection bias and a corrected information-regime taxonomy; the full derivation is in `13_C009_IDENTIFICATION_PROSECUTION.md`.
- Targeted searches did not surface the exact decomposition as a primary P/NPS inferential object. Absence is not established.

### Identification correction

The earlier shorthand “bridge sample observing both measurement versions” was too permissive. Two fallible binary measurements on the same units, without gold-standard X or additional restrictions/populations, are generally not sufficient to identify prevalence plus both measurement models [R119].

A representative bridge sample administered on the NPS measurement scale can identify the correct B-scale target benchmark and therefore resolve the wrong-scale benchmark component, but not necessarily residual latent-X selection bias.

### Next gate

C009 may move to `SURVIVES` only if bounded-mismatch/partial-identification work shows that the narrowed decomposition produces a **decision-relevant and non-vacuous diagnostic** that remains meaningfully distinct from R113/R114/R089.

### Execution consequence

No substantive project execution is authorized yet. Large simulations, generalized estimator development and repository build-out remain deferred.

---

## D017 — Park C009 as a no-go for the first project after sensitivity-utility prosecution

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Do **not** promote C009 to `SURVIVES` or `EXECUTION`.

Classify C009 as **PARKED / NO-GO FOR FIRST PROJECT** after completing the bounded-mismatch / partial-identification sensitivity prosecution.

Preserve the following stage-2 result as a reusable lemma inside the program:

> In the binary latent-X model, let `delta=q_A-q_B^P` denote wrong-reference-scale mismatch and let `kappa` denote the fraction of the latent-X selection correction recovered by calibration on the B-side proxy. Then
>
> `mu = mu_B + ((d_obs-delta) Delta_W)/kappa`,
>
> with `kappa = Corr(X,W_B | R=1)^2` under the toy assumptions.

This identity yields exact decision thresholds for sign reversal, under-correction, exact correction, over-correction, and when calibration becomes worse than leaving the NPS unadjusted.

### Why this is not enough for promotion

1. **The mismatch-only sensitivity operation is already substantially occupied.** Hartman & Huang [R120] study survey-weight sensitivity when a variable is observed in the survey sample but not in the target population; for calibration/raking, their analysis varies the unknown target-population mean as the sensitivity parameter. Reparameterizing the unknown B-scale target margin as `q_B^P=q_A-delta` makes C009's `delta`-only analysis a special binary instance of that operation.
2. **Generic bounded-misclassification partial identification is established.** Molinari [R121] develops sharp identification regions for functionals of distributions under restrictions on misclassification matrices, including lower bounds on correct-report probabilities. C009 cannot claim bounded misclassification -> partial identification as a new methodological idea.
3. **Differential measurement-error sensitivity and error-prone weighting are established.** Imai & Yamamoto [R122], Rudolph & Stuart [R123], Hong et al. [R114], McCaffrey et al. [R089], and Lockwood & McCaffrey [R124] occupy much of the generic measurement-error/sensitivity/weighting territory.
4. **The residual distinctive object is too narrow and insufficiently anchored.** The joint `delta`-`kappa` decision surface is clean and P/NPS-specific, but RANDS supplies no gold-standard X, source-specific error rates, or representative B-scale target administration from which defensible `delta`/`kappa` ranges can be estimated.
5. **Sensitivity usefulness degrades quickly without strong measurement information.** In the stage-2 toy stress test, the feasible target-mean envelope is narrow under very high minimum sensitivity/specificity but broadens rapidly as those lower bounds weaken. Available RANDS documentation and general survey-reliability evidence do not justify importing one tight universal bound for the actual adjustment variables.
6. **The multivariable extension is not yet a differentiating theorem.** At present it appears likely to become moment-target perturbation plus established misclassification/calibration machinery rather than a distinct full-paper contribution.

### Reopen C009 if

Reopen only if at least one materially new condition appears:

- a public or accessible P/NPS dataset contains a representative bridge administration of the NPS measurement protocol in the target population, repeated source-specific measurements, or gold-standard validation for a key adjustment variable;
- construct-specific validation evidence supports defensible bounds tight enough to make the decision regions empirically informative;
- a multivariable/multicategory extension produces a nontrivial theorem or diagnostic not reducible to existing calibration and partial-identification machinery; or
- a citation-chain review uncovers a sharper applied gap in which the joint `delta`-`kappa` interaction changes an actual survey-inference decision and is not already covered by R120–R124 and the earlier ancestors.

### Execution consequence

C009 should not consume the program's first-project execution budget. The active neighborhood D013 remains in force; candidate generation/prosecution should move to the next opportunity within survey data integration / nonprobability inference.

---

## D018 — Park C010 after four-channel response-quality filtering prosecution

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Classify **C010 — selection-aware response-quality filtering in nonprobability survey inference** as **PARKED / NO-GO FOR FIRST PROJECT**.

Do not begin a C010 simulation/application execution program. Preserve the theoretical decomposition and explicit reopening conditions, then return to bounded triage of OF-19–OF-23 within D013.

### Why

1. **The problem is important and current.** Commercial online nonprobability surveys face bogus/careless responding, and current Pew/Gallup work shows that screening rules materially change sample composition and estimates [R125, R129–R131].
2. **The broad empirical contribution is directly occupied.** Slamowicz et al. [R127] already exclude satisficers before recalculating survey weights and report lower average absolute bias across four nonprobability panels than weighting alone.
3. **The selection mechanism is not conceptually new.** Mathur [R128] formally shows that attention-check exclusion can induce selection bias and gives conditions/adjustment strategies for valid analysis.
4. **Measurement error × representativeness is an active NPS methods area.** Kennedy et al. [R125] motivate it directly and Sen & Lahiri [R126] develop a 2026 method targeting both sources of error.
5. **The useful C010 decomposition is not enough.** After ideal calibration on `X`, post-filter error can be separated into retained response contamination and residual selection among `S=1,C=1` cases. This is a valuable diagnostic but currently looks like a synthesis of established measurement-error and selection logic rather than a standalone theorem.
6. **The distinctive classifier-error parameters are weakly identified.** True respondent quality is rarely observed, so false-positive/false-negative rates require validation, strong latent-class assumptions, or sensitivity/partial-identification machinery already mature in adjacent literatures [R141, R121].
7. **Data feasibility is asymmetric.** Public data such as Pew 2020 [R133–R134] can support empirical illustrations of filtering effects, but the strongest direct datasets do not provide a universal gold-standard quality label, and the Social Research Centre data underlying R127 are not publicly shareable.

### Reopen C010 if

- a public/accessibly validated NPS dataset supplies credible respondent-quality truth or adjudication plus multiple screening scores and population benchmarks;
- the post-filter calibration structure yields a nontrivial identification or sharp partial-identification result beyond generic selection/misclassification theory;
- an estimand-targeted screening-threshold rule is derived that remains valid under explicit classifier uncertainty; or
- an official-statistics/practitioner decision provides a defensible validation design and a high-value inferential choice not already answered by the nearest literature.

### Execution consequence

D013 remains active. OF-24 is no longer a live unprosecuted opportunity; it is represented by parked C010. The next candidate-generation/prosecution pass should compare OF-19–OF-23 without automatically assigning C011.

---

## D019 — OF-19–OF-23 collapse-first triage completed; no C011 assigned

**Date:** 2026-09-07  
**Status:** Active

### Decision

Complete the bounded triage ordered by D018 **without promoting any of OF-19–OF-23 to C011**.

Classify:

- **OF-19:** PARKED in broad form;
- **OF-20:** PARKED in generic form;
- **OF-21:** PARKED in broad form;
- **OF-22:** **WATCHLIST / SHARPEN BEFORE CANDIDATE** after collapse of the broad temporal-drift claim;
- **OF-23:** PARKED in broad form.

C011 remains deliberately unassigned.

### Why

1. OF-19 is directly crowded by current nonignorable-NPS inference and sensitivity work [R080, R144], with additional 2026 uncertainty/non-identifiability work [R146]; R143 is a strong adjacent ancestor from nonignorable probability-sampling/nonresponse inference rather than a direct NPS method.
2. OF-20's generic regression/association formulation is already represented by direct model-calibration data-integration methods [R086].
3. OF-21's core decision—borrow the NPS when compatible, otherwise retain the probability sample—is explicitly the object of test-and-pool estimation [R073], with current efficient-combination work further crowding the space [R074].
4. OF-22's broad claim is directly occupied by a recurring hybrid tracking-poll study that asks whether NPS selection mechanisms change over time and shows stale raking can distort trends [R142].
5. OF-23's generic overlap-to-action formulation is directly constrained by deterministic-undercoverage methods [R071] and low-overlap thresholding that excludes NPS units to reduce error [R079].
6. The strongest residue is OF-22 under **intermittent probability anchors**, but no theorem-level differentiation, identification restriction and public repeated P/NPS validation design have yet been established. Refreshment-sample methodology and active 2026 testing work are also strong ancestors [R145].

### Execution consequence

D013 remains active, but the current OF-19–OF-23 slate is exhausted as a source of immediate first-project candidates. The next research step is a fresh four-channel opportunity-generation pass inside survey data integration / NPS inference, using the C009, C010 and OF-19–OF-23 failure records as explicit boundary conditions.

Do not automatically revive OF-25/OF-26 and do not assign C011 until a newly sharpened opportunity passes the Charter gate.

Full record: `15_OF19_OF23_COLLAPSE_TRIAGE.md`.

## D020 — Advance OF-30 to priority screening; keep C011 unassigned

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

The fresh four-channel opportunity-generation pass inside D013 is complete enough to establish a new **screening priority**, but not a candidate.

Advance:

> **OF-30 — finite-benchmark certification / benchmark-to-target transportability**

as **PRIORITY SCREENING**.

Do **not** assign C011 yet.

Retain OF-31 (adaptive benchmark reuse / quality-assessment overfitting) as a mechanism inside OF-30, retain OF-32 (target/control-universe mismatch) as watchlist-only, and park OF-33/OF-34 in broad form.

### Why OF-30 is the only priority lead

1. **Four-channel convergence:** benchmarking literature, a clear identification warning, benchmark-rich data, and a real production decision all point at the same problem [R148–R155].
2. **A decision exists before method invention:** agencies/vendors must decide which benchmarks to use and whether observed benchmark performance certifies unbenchmarked outcomes.
3. **Public/obtainable validation is plausible:** Pew benchmarking studies provide multiple known-truth variables across probability and opt-in sources; NCHS RSS provides an official-statistics cross-design replication environment [R148, R151–R153].
4. **The object is not another generic NPS estimator:** it concerns validity/transportability of a finite benchmark-based quality certificate.
5. **Novelty remains unproven:** direct benchmark-validity/generalization literature may contain an equivalent framework, and the baseline linear discrepancy decomposition is not by itself a publishable theorem.

### Bounded next gate

Before C011 can be assigned, complete only:

1. direct nearest-neighbor prosecution around benchmark validity/selection/generalization and survey-quality certification;
2. a variable-level feasibility audit for held-out or leave-domain-out benchmark validation in Pew/NCHS data; and
3. a theory screen asking whether the certificate problem yields a nontrivial bound/design/decision result beyond standard cross-validation and outcome-specific adjustment logic.

### Kill condition

Do not promote OF-30 if a direct equivalent framework exists, the held-out benchmark design is not scientifically credible, or the residual result does not change a benchmark-selection/panel-certification/release decision.

### Execution consequence

No substantive simulation/application project is authorized. The next move is a bounded **OF-30 screening pass**, not another broad prosecution and not infrastructure build-out.

Full record: `16_D013_FRESH_OPPORTUNITY_GENERATION.md`.

## D021 — Park OF-30 after bounded screening; keep C011 unassigned

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Complete the bounded OF-30 gate ordered by D020 and classify:

> **OF-30 — finite-benchmark certification / benchmark-to-target transportability**

as **PARKED AFTER BOUNDED SCREENING — NO C011**.

Do not promote OF-31 independently. It remains a useful nested-validation warning but is too close to generic post-selection/cross-validation logic.

### Gate results

1. **Nearest-neighbor novelty — partial / heavily crowded.** R-indicator work already treats the tension between a survey-level quality indicator and statistic-specific nonresponse bias, including empirical validation of whether an indicator predicts bias in other survey variables [R161–R164].
2. **Data feasibility — pass.** Pew provides 28 benchmark variables across six online sources and NCHS RSS Round 7 benchmarks 53 outcomes across health domains [R166, R169]. A grouped/nested holdout design is feasible if calibration/tuning outcomes are not reused as certification targets.
3. **Theory/decision differentiation — fail.** With no restriction linking an unbenchmarked target to the benchmark set, certification is impossible except as an elementary identification warning. Adding a target function class moves the problem toward existing calibration/worst-case-bias/kernel-balancing theory [R161, R165]; adding an outcome-superpopulation/covariance model moves it toward standard predictive validation or benchmark-subset prediction [R168].

### Why this is a park rather than a kill of the substantive problem

The empirical question remains important: provider/method rankings may depend on benchmark content, and benchmark scores should not be treated as universal evidence of target accuracy [R169]. But the current residual contribution is better characterized as a rigorous validation protocol or empirical methods note than as the novel first statistical-method project required by the Charter.

### Preserved protocol

For any future benchmark-based quality evaluation:

- separate calibration/tuning, certificate-selection and final validation outcomes;
- prefer leave-domain-out/grouped holdout to random item splitting;
- define the intended outcome universe/class before claiming transport;
- do not interpret a survey-level quality score as statistic-level reliability without an explicit linking assumption.

### Execution consequence

**C011 remains unassigned. No substantive execution project is authorized.**

Return to fresh four-channel opportunity generation inside D013 with the OF-30 failure mode added as a hard constraint. Do not automatically revive OF-22/OF-25/OF-26 or relabel OF-30.

Full screening record: `17_OF30_BOUNDED_SCREENING.md`.

## D022 — Adopt review-first cross-field reconnaissance and advance OF-35 to bounded prosecution

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Do not force another first-project opportunity inside the D013 survey-data-integration neighborhood.

Adopt **review-first cross-field statistical reconnaissance** as the current discovery mode and advance only:

> **OF-35 — prediction-evaluation ranking reliability under interval censoring / imperfect assessment**

as **PRIORITY PROSECUTION LEAD — NOT C011**.

D013 remains canonical research history and a future branch, but it is superseded as the exclusive active first-project discovery neighborhood.

### Why

1. Repeated D013 opportunity searches generated useful anti-gap knowledge but no candidate that cleared the first-project novelty/theory gate.
2. Review-first reconnaissance successfully exposed both genuine frontiers and false openings: synthetic-data inference is important but highly competitive [R170–R173]; the apparent stronger-coverage meta-analysis opening collapses to tolerance-interval ancestors [R174–R175]; generic multiverse inference is already formally occupied [R176–R177].
3. The interval-censoring literature contains multiple valid prediction-evaluation estimators but no novelty claim is assumed [R181–R185]. This creates a concrete prosecution target around **model-ranking/selection reliability**, not metric invention.
4. Right-censoring work already shows evaluation-score ranking reversals and dependent-censoring failure [R179–R180], providing both a methodological ancestor and a hard differentiation test.
5. Simulation/software feasibility is favorable through established interval-censored regression tooling [R186].

### Bounded OF-35 gate

Before assigning C011:

1. prosecute full-text nearest neighbors R182–R185 specifically for model-ranking reversals, wrong-winner probability or selection regret;
2. formalize the relation to right-censoring ranking-reversal/dependent-censoring work R179–R180;
3. define an oracle exact-event-time ranking estimand and the observed-data evaluation procedures;
4. identify an interval-censoring-specific assessment mechanism that creates more than generic noise inflation;
5. confirm a small simulation and public/open illustration path.

### Kill condition

Park OF-35 if a direct equivalent already maps cross-method oracle ranking failures for interval-censored outcomes, if the result is merely a right-censoring extension with no new structure, or if the substantive conclusion is only that sparser observation increases variance.

### Execution consequence

**C011 remains unassigned. No full simulation/application project is authorized.** The next move is the bounded OF-35 prosecution recorded in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

## D023 — Park OF-35 after direct ranking-reliability prosecution

**Date:** 2026-09-07  
**Status:** ACTIVE

### Decision

Complete the bounded OF-35 prosecution ordered by D022 and classify:

> **OF-35 — prediction-evaluation ranking reliability under interval censoring / imperfect assessment**

as **PARKED / NO-GO FOR FIRST PROJECT — NO C011**.

Retain only the narrower **OF-38 — sensitivity of model choice to informative/non-ignorable Case-K assessment** as a **WATCHLIST / THEORY-HEAVY** residual, not a candidate.

### Why

1. Yang et al. already simulate three competing prediction models, calculate AUC/Brier/EPCE using latent true event times as the ideal reference, and compare model-based/IPCW/naive interval-censored evaluations [R183]. Wrong-winner probability would largely summarize differences already generated by that design.
2. Bahrini et al. (ICML 2026) directly study how censoring rate/mechanism distort survival-model metrics and **model rankings** by comparing standard censored-data evaluation with oracle true-event-time evaluation [R189]. This occupies the broad problem sentence that motivated OF-35.
3. Yanagisawa & Akiyama (ICML 2026) explicitly study interval-censoring monitoring assumptions and introduce strictly proper scoring/calibration machinery under stated assumptions [R190], so the theoretical evaluation-validity frontier is also active.
4. Informative Case-K model selection/model averaging is already an active methodology area [R191–R192]. A simple shift from right censoring to interval censoring therefore does not establish a distinct first-project contribution.
5. The proposed wrong-winner/regret estimands are useful decision summaries but, without new theory or identification, are transformations of differential score error rather than a new method.

### Why no toy simulation

A toy simulation is unnecessary for the gate decision. R189 already establishes that censoring can destabilize model rankings, while R183 supplies the interval-censoring oracle-versus-observed simulation ingredients. Additional computation would demonstrate plausibility rather than novelty.

### Execution consequence

**C011 remains unassigned. No substantive execution project is authorized.** Return to review-first cross-field opportunity generation with a strengthened active-work rule: search the *decision/problem sentence* across adjacent data-missingness/censoring mechanisms and neighboring ML/statistics venues before promoting a mechanism-specific variant.

Full prosecution record: `19_OF35_INTERVAL_CENSORING_RANKING_PROSECUTION.md`.

## D024 — Complete cross-field opportunity generation II; prosecute OF-39 only

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Complete the second review-first cross-field generation pass and designate:

> **OF-39 — calibration of Bradley–Terry diagnostics under outcome-adaptive comparison scheduling**

as the **sole PRIORITY PROSECUTION LEAD — NOT C011**.

Keep OF-40, OF-41 and OF-43 on watchlists, park OF-42 in broad form, keep **C011 unassigned**, and authorize no execution project.

### Why OF-39 survives generation

1. Hamilton & Tawn show that adaptive comparison scheduling can make the realized Bradley–Terry schedule non-ancillary and materially alter estimation; they already provide a scheduler-replay bootstrap for parameter bias [R195].
2. Wu et al. provide a concrete, established Bradley–Terry diagnostic framework [R196]. The bounded search did not find a direct paper establishing the null calibration of those diagnostics when the comparison graph is generated sequentially from previous outcomes.
3. The target is exact and falsifiable: Type-I calibration of diagnostic p-values under a correctly specified Bradley–Terry model, integrating over both outcomes and the adaptive scheduler.
4. Simulation and software/data substrates are modest and reproducible [R195–R196, R210–R211].

### Principal novelty threat

Yi & Wang already study goodness-of-fit under response-adaptive allocation [R197]. Therefore the generic principle that adaptivity changes GOF inference is **not** a contribution. OF-39 survives only if the paired-comparison graph and the specific diagnostic law create a nontrivial result not directly inherited from general adaptive-design theory.

### Why the other leads do not advance

- **OF-40:** broad spatial/correlated validation leakage is covered by existing CV theory [R199–R201].
- **OF-41:** no-gold-standard performance identification has strong misclassification/partial-identification ancestors [R202–R205, R212].
- **OF-42:** underreporting-induced diagnostic failure and robust dependence tests are directly established [R187–R206].
- **OF-43:** the exact intersection may be narrower, but it is theory-heavy and sits between active extreme-quantile and mature measurement-error literatures [R207–R209].

### Next bounded action

Prosecute OF-39 in four gates:

1. audit the exact null/reference-law derivations of the Wu et al. diagnostics;
2. audit Yi & Wang and adjacent adaptive-design inference for a theorem that transfers directly;
3. run a minimal null simulation **only if** the theoretical seam remains;
4. if distortion exists, test scheduler-replay versus graph-conditioned calibration and require a principled validity result before considering C011.

## D025 — OF-39 survives bounded prosecution, narrowed to finite-sample adaptive calibration

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Complete the four-gate OF-39 prosecution and classify OF-39 as:

> **SURVIVES / NARROWED / HOLD BEFORE C011**

Keep **C011 unassigned** and authorize no execution project.

### What survived

The final adaptive comparison graph is non-ancillary [R195]. A frozen-graph null calibration therefore need not reproduce the conditional experiment induced by an outcome-adaptive scheduler. Bounded simulations showed a material adaptive-versus-frozen difference and substantially better nominal behavior from scheduler replay.

### What collapsed

The broad claim that adaptivity automatically invalidates Bradley–Terry diagnostics asymptotically is not defensible. Under the correct conditional Bradley–Terry model, score/residual increments are martingale differences with predictable variance; response-adaptive likelihood theory [R197] and modern adaptive-data inference [R215–R216] make asymptotic validity plausible under adequate exploration.

### Why no C011 yet

- scheduler replay is already an established principle in Hamilton & Tawn [R195];
- sparse-binomial/GLM goodness-of-fit is an independent classical problem [R214];
- no new bootstrap/martingale validity theorem has yet been proved;
- diagnostic power under Swiss matching is strongly alternative-dependent;
- a documented adaptive real-data scheduler has not yet been secured.

### Next bounded action

Run an exact small-state enumeration of a fully specified adaptive paired-comparison scheduler. The promotion question is whether a clean proposition can distinguish the true joint/replay diagnostic law from the false fixed-final-graph reference in a way that is not already contained in R195 or R197.

Full prosecution record: the consolidated OF-39 prosecution in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

## D026 — Exact OF-39 theorem gate proves mechanism but fails novelty; park OF-39

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Complete the exact-enumeration/theorem gate and classify OF-39 as:

> **PARKED / MECHANISM ESTABLISHED, DISTINCT CONTRIBUTION NOT ESTABLISHED**

Keep **C011 unassigned** and authorize no execution project.

### Exact result

A four-object, two-round Swiss-style Bradley–Terry experiment with merits `(3,1,2,1)` was enumerated without Monte Carlo. The final graph is `G_A` exactly when the two first-round outcomes agree and `G_B` when they differ. Consequently, conditioning on the adaptive final graph truncates the null outcome space. The frozen-final-graph product Bernoulli law assigns positive probability to outcome paths that could not have generated the observed graph.

For the exact oracle Pearson residual sum, the conditional statistic-law total-variation distance is `5/12` on `G_A` and `37/144` on `G_B`. At nominal `alpha=0.10`, the frozen exact tail procedure rejects with probability `17/144`, compared with `23/240` for exact joint scheduler replay.

Full exact record: the consolidated OF-39 exact gate in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

### Why the candidate still fails

The finite-sample phenomenon is real, but the theorem-level mechanism is a direct consequence of the non-ancillarity already established by Hamilton & Tawn [R195]. Their adaptive bootstrap already replays the scheduler while preserving only ancillary scheduling components. Exact replay validity with known parameters is a generic identical-experiment result, and Yi & Wang [R197] already occupy the broad response-adaptive GOF principle. Applying Wu et al.'s diagnostic statistic [R196] to the same replay principle is therefore an implementation transfer rather than a sufficiently distinct contribution.

A targeted September 2026 check also found active paired-comparison lack-of-fit theory on fixed/sparse graphs [R217], increasing pressure on the secondary diagnostic-power axis.

### Program consequence

Do not expand OF-39 simulations or force C011. Return the next executable action to **review-first cross-field opportunity generation**. OF-39 may be reopened only under the explicit conditions in the exact-gate record.


## D027 — Review-first generation yields OF-44 for bounded screening; consolidate discovery records

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Complete the next review-first cross-field opportunity-generation pass without forcing C011. Register exactly one surviving opportunity:

> **OF-44 — downstream inferential reliability under heterogeneous 1997↔2024 SPD-15 bridging — PRIORITY BOUNDED SCREENING / NOT C011.**

Keep **C011 unassigned** and authorize no execution project.

### Evidence logic

The live SPD-15 transition supplies a documented, consequential reliability problem: current federal bridge tools are explicitly initial/basic [R223], while Census advisory material flags geographic, age/time and other heterogeneity; lack of an ideal simultaneous dual-format survey; and small-factor/small-area issues [R224]. Independent 2025 work shows that race/ethnicity procedural discontinuities can materially alter demographic and mortality statistics [R225].

The broad method claim is nevertheless blocked. Earlier federal race bridging already used regression models with demographic/geographic variation and evaluated downstream vital rates [R226], while general misclassification sensitivity/Bayesian methods already propagate uncertainty in classification parameters [R227]. OF-44 therefore survives only as a narrow decision-reliability question: whether downstream subgroup rates, disparities, trends or rankings can be certified or can reverse under scientifically constrained bridge heterogeneity.

A second apparently promising lead — using uncertainty in modeled gridded-population counts inside PPS survey designs — is collapsed before registration because imperfect measures of size/frame information are established survey-sampling objects [R219–R221].

### Next bounded action

Run OF-44 P1–P4:

1. nearest-neighbor/theorem search for downstream bounds and transition-matrix heterogeneity;
2. public-data feasibility audit, explicitly separating public bridge factors/test data from restricted linked Census data;
3. smallest formal tipping/bounding result for a rate/disparity/trend/ranking functional;
4. reproducible consequentiality check.

Kill before C011 if the theorem is a direct misclassification-sensitivity special case, key heterogeneity is not publicly constrainable, or plausible perturbations do not change a decision-relevant conclusion.

### Source-cap action

To respect the ChatGPT Project 25-source limit, fold the former standalone D024/OF-39 chain (`20_...`, `21_...`, `22_...`) into `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md` and retire those three filenames from the canonical source set. This preserves their content while freeing three canonical source slots.


## D028 — OF-44 bounded gate fails on theorem novelty; public heterogeneity is insufficient for first-project rescue

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Park **OF-44** as **NO-GO FOR FIRST PROJECT**. Keep **C011 unassigned** and authorize no execution project. Do not run the planned P3 toy theorem or P4 consequentiality experiment after P1 fails.

### P1 — exact nearest-neighbor/theorem prosecution

**FAIL.** Molinari's direct-misclassification framework represents categorical error through a misclassification-probability matrix, allows general restrictions on that matrix, and derives sharp identification regions for arbitrary real functionals of the target distribution [R228]. Conditioning on observed strata extends the same object to heterogeneous bridge matrices. A bridge-robustness set `{T(B): B in H}`, its extrema, and the zero/order crossing condition for sign or ranking reversal are therefore direct specializations unless OF-44 adds structure not present in the generic matrix-identification problem.

This pressure is reinforced by direct epidemiologic matrix-method work for standardized rate ratios under polychotomous misclassification [R229] and by the already-recorded probabilistic misclassification-sensitivity literature [R227]. Under L050/L052/L061, relabeling the extrema as a robustness certificate or tipping condition is not enough.

### P2 — public-data feasibility

**PARTIAL / INSUFFICIENT FOR FIRST PROJECT.** The Phase-1 factors, executable code and example datasets are public [R223], so national reproduction is feasible. However, Census explicitly warns that national factors should not be used as subnational factors, describes future/Phase-2 state and county work, notes possible nativity and time heterogeneity, and states that the most useful 2015 NCT-to-2020 Census comparison comes from linked respondents rather than an ideal simultaneous dual-format survey [R224]. Public content-test reports provide aggregate format comparisons [R230], but they do not identify the stratum-specific transition matrices required to constrain geography/nativity/time heterogeneity sharply.

### Stop rule

Because P1 already collapses the proposed theorem contribution, **P3 and P4 are not executed**. This follows L052: computation is not used to rescue a lead after novelty has failed.

### Program consequence

OF-44 remains scientifically consequential as a federal data-comparability problem, but the current contribution path is too generic and too dependent on nonpublic heterogeneity information to justify C011. Return to **review-first cross-field opportunity generation**.


## D029 — Review-first generation IV returns a valid null result; diversify the next search neighborhood

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Complete the post-OF-44 review-first cross-field generation pass with **no new registered opportunity**. Keep **C011 unassigned** and authorize no execution project.

### Evidence logic

Seven routes were screened and killed before OF registration:

1. informative cluster size × prediction validation is already prediction-specific in Coley et al. and Pavlou et al. [R231–R232];
2. meta-analysis extraction/application error robustness is already covered by explicit error taxonomies, empirical correction studies and fragility analysis [R233–R235];
3. population-denominator uncertainty is directly modeled and evaluated in small-area inference [R236–R237];
4. multiple-imputation/internal-validation ordering is already an explicit methodological literature [R238–R239];
5. noisy protected attributes are directly treated in fairness theory, including current AUC fairness work [R240–R241];
6. LLM evidence-extraction error propagation is under active end-to-end study as of August–September 2026 [R242–R244];
7. multisite harmonization leakage has direct empirical and pipeline-safe methods, including 2026 work [R245–R246].

Under L042/L047/L051, turning any of these into a new OF number merely because the program can state a decision-reliability framing would weaken the novelty standard. The correct output of this pass is therefore a null generation result.

### Program consequence

The repeated direct-occupation pattern is itself actionable search evidence. The next pass should diversify fields rather than continue resampling biomedical prediction/evidence synthesis and harmonization.

**Next executable action:** bounded review-first reconnaissance in more distant statistical domains (official statistics, experimental design, statistical computing/numerical reliability, environmental/spatial statistics, social-science measurement), preserving the same problem-sentence and ancestor kill gates. Do not search for C011 directly.

## D030 — Diversified review-first reconnaissance returns a second valid null; switch discovery channel

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Complete the bounded five-domain reconnaissance mandated by D029 with **no new registered opportunity**. Keep **C011 unassigned** and authorize no execution project.

### Domains and bounded dispositions

1. **Official statistics — multi-source quality propagation:** **COLLAPSE BEFORE REGISTRATION.** The 2026 UNECE multi-source-statistics handbook already makes quality management an integrated-system problem [R247]. Earlier National Academies and ONS frameworks explicitly treat quality/error across multiple linked sources and downstream processed statistical products [R248–R249]. A generic “trace upstream source uncertainty to downstream official statistics” framing is therefore not a distinct statistical object.
2. **Experimental design — adaptive randomization under missing/mismeasured inputs:** **COLLAPSE / ACTIVE.** Current RAR reviews name missing data and measurement/classification error as design-specific challenges [R250], while 2026 theory directly treats missing covariates under covariate-adaptive randomization [R251]. Earlier RAR literature already studies misclassification and adaptive-design inference [R252].
3. **Statistical computing / numerical reliability — implementation/default sensitivity:** **COLLAPSE / HIGH ACTIVE-WORK COMPETITION.** Wang's September 2026 accepted manuscript directly catalogs cross-software hidden implementation choices and demonstrates significance reversals on boundary datasets [R253]. Statistical-software reliability testing and computational-stability diagnostics have mature classical ancestry [R254–R255].
4. **Environmental/spatial statistics — uncertainty of spatial aggregates:** **COLLAPSE BEFORE REGISTRATION.** Wadoux and Heuvelink already provide a scalable method for uncertainty of spatial averages/totals accounting for autocorrelated map errors [R256]; their 2025 follow-up argues that the remaining problem is widespread failure to use existing methods [R257]. This is an adoption/reliability-practice problem, not an unoccupied method cell.
5. **Social-science measurement — mixed-mode survey bias under uncertain mode effects:** **COLLAPSE / HIGH ACTIVE-WORK COMPETITION.** A January 2026 systematic review identifies external-evidence requirements for suitable mode-effect adjustments [R258], but the same active program already develops DAG-based bias diagnosis/quantitative bias analysis and August 2026 randomized evidence on item and association distortions [R259–R260].

### Interpretation

D030 is stronger search evidence than D029 alone. The program deliberately diversified away from the previously saturated biomedical-prediction/evidence-synthesis neighborhood and still found that the most plausible reliability objects were directly occupied, classically inherited, or under unfavorable current competition.

Under L042 and L047, this remains a valid null result. Under L027 and L038, however, **another review-first field sweep is no longer the highest-value next move**. Literature-generated discovery has now been sampled broadly enough to justify switching independent discovery channels.

### Program consequence

- **No OF-45 is created.**
- **C011 remains unassigned.**
- **No execution project is authorized.**
- No new general lesson is added: L027, L031, L034, L038, L042, L046–L052 already prescribe the response.

**Next executable action:** run a **bounded non-literature triangulation pass** using theory-generated, data-generated and decision-generated channels. Start from reproducible public-data anomalies and concrete agency/practitioner decisions, derive the statistical mechanism independently, and require convergence of at least two independent discovery channels before assigning any new OF identifier. Only then run the literature/ancestor/active-work prosecution. Do not search for C011 directly and do not begin substantive project execution.

## D031 — Independent-channel triangulation registers OF-45; current QCT precision-screen tradeoff advances to bounded prosecution

**Date:** 2026-09-08  
**Status:** ACTIVE

### Decision

Complete the bounded theory/data/decision-channel triangulation mandated by D030. Register **OF-45** as the sole surviving opportunity from the pass, but **do not assign C011** and do not authorize substantive project execution.

> **OF-45 — reliability-versus-coverage consequences of HUD's post-2016 ACS precision screen in Qualified Census Tract designation — PRIORITY BOUNDED PROSECUTION / NOT C011.**

### Four-workflow triangulation result

1. **EPA AirNow → AQS provisional/final data states:** theory and operational evidence converge, but the generic object collapses against mature real-time/vintage-data and reference-observation-error literatures [R261–R262]. No opportunity is registered.
2. **FDA FAERS duplicate reports:** the operational reliability problem is direct, but duplication is already synthesized and an FDA-linked full-database deduplication pipeline is operating in current safety review [R263–R264]. No opportunity is registered.
3. **CMS Overall Hospital Quality Star Ratings under missing measure groups:** the decision mechanism is explicit in the 2026 methodology, while existing evaluation already reports instability for hospitals with fewer measures, especially smaller/rural hospitals [R265–R266]. No opportunity is registered.
4. **HUD QCT ACS precision screen:** decision, data and theory channels converge on a narrower modern object that survives bounded ancestor/active-work prosecution [R267–R274]. Register OF-45.

### Why OF-45 clears the registration gate

**Decision channel.** HUD's current QCT rule rejects income/poverty inputs whose margin-of-error ratio is about 50% or worse and requires criterion satisfaction in at least two of three ACS 5-year releases [R267]. Treasury guidance for ACS-based geographic proxies states that accounting for sampling error can systematically disadvantage lower-population areas and permits disregarding sampling error in the interest of equity [R268]. The agencies therefore expose a real reliability-versus-coverage decision tension.

**Data channel.** HUD publishes all-tract designation inputs, including estimates and margins of error, and a reproducible designation algorithm [R272]. The post-2016 rule change is documented: prior QCT designations accepted MoERs below 100%, whereas the 2016 regime tightened the screen to roughly 50% [R271]. This creates a public policy counterfactual that can be reconstructed without privileged microdata.

**Theory channel.** A hard precision screen is a selective-coverage mechanism. Because ACS sampling error decreases with effective sample size, the probability of passing the reliability screen can vary structurally with tract population/sample size even at comparable latent need. The two-of-three rule compounds selection across overlapping ACS releases, and the 20% population cap can propagate removal of one tract into designation changes for other tracts.

### Prior-art narrowing

The following are **not** novel claims for OF-45:

- ACS sampling error can misclassify QCT eligibility, with higher risk for smaller tracts [R269].
- false inclusion and false exclusion trade off, and the statutory 20% cap complicates error handling [R269].
- ACS threshold-based program eligibility can change across releases [R270].
- abstention/selection rules that improve average predictive reliability can magnify subgroup disparities in abstract classification settings [R274].
- current LIHTC work already reconstructs QCT assignment and simulates sampling-driven designation changes using HUD margins of error [R273].

The surviving object is therefore narrower:

> **Under HUD's post-2016 QCT regime, what did tightening the MoER reliability screen from <100% to approximately <=50% buy in classification reliability, what population-dependent exclusion burden did it introduce, and how do the two-of-three rule and 20% population cap propagate that screen into final designations?**

Soltas [R273] is the closest current empirical neighbor found in this pass: he uses the QCT rule and ACS sampling variation as identifying variation for housing-subsidy effects. He does not make the precision-screen reliability/distributional tradeoff the estimand.

### Identification and feasibility warning

The public HUD files are sufficient to identify **screen-induced eligibility/designation changes** under exact policy counterfactuals such as MoER <100% versus <=50%, including downstream cap displacement. They do **not** directly reveal the latent true tract income/poverty status. Therefore actual false-inclusion/false-exclusion reduction from the tighter screen is not design-identified from point estimates and margins of error alone.

In addition, consecutive ACS 5-year releases overlap heavily, so a two-of-three error calculation cannot defensibly assume independent release errors. Any claim about reliability gain must either use a justified covariance/replicate-data construction or be presented as a transparent sensitivity/model-based result.

### Program consequence

- **OF-45 is created** as a **PRIORITY BOUNDED PROSECUTION** lead.
- **C011 remains unassigned.**
- **No execution project is authorized.**
- The contribution class, if it survives, is most plausibly **failure analysis / empirical benchmark + theory decomposition**, not a claim to have discovered ACS threshold noise.

**Next executable action:** run an **OF-45 bounded data + identification gate**. Reproduce the current and historical HUD QCT rules from public all-tract inputs; isolate the counterfactual effect of the MoER threshold (<100% versus <=50%) on eligibility and final designation; quantify population-linked screen coverage and cap-mediated displacement; and derive a correlated-error sensitivity analysis for the overlapping two-of-three ACS rule. Kill OF-45 if the modern screen produces negligible distributional/designation consequences, if the apparent population gradient vanishes after conditioning on proximity to the substantive thresholds, or if the claimed reliability benefit cannot be characterized without indefensible latent-truth assumptions. Promote only if the screen creates consequential, reproducible population-dependent coverage/displacement and the final contribution remains distinct from [R269–R274].

## D032 — OF-45 bounded rule/identification gate narrows the claim; empirical magnitude gate remains unresolved

**Date:** 2026-09-08

### Mandate

Execute the D031 OF-45 public-data + identification gate without assigning C011 by momentum. Reconstruct the historical/current reliability rules, determine what is and is not identified under overlapping ACS releases, recheck the closest active neighbor, and run the nationwide threshold replay if the public all-tract artifact can be ingested.

### Results

1. **Historical/current rule reconstruction — PASS.** The 2015 QCT procedure used three overlapping ACS 5-year releases and rejected a release-level income/poverty input when its 90% confidence interval included zero [R275]. Because ACS publishes 90% MoEs with `MOE = 1.645 * SE` [R277], this is equivalent to requiring relative MoE `<100%` for a positive estimate. HUD's 2016 notice then tightened the standard to approximately `<=50%` [R271]. The modern algorithm sets unreliable criterion values to zero, requires criterion satisfaction in at least two of three releases, averages passing values for ranking, and applies the 20% population cap [R267, R272]. Thus a clean **same-data screen counterfactual** can hold the modern substantive/ranking/cap rule fixed while changing only `c` from 0.50 to 1.00.

2. **Identification boundary — PASS / NARROW.** The public inputs and deterministic algorithm identify changes in screen passage, eligibility, ranking and final designation under alternative `c`. They do **not** identify each tract's latent true poverty/income state or the actual false-inclusion/false-exclusion reduction. ACS consecutive 5-year releases overlap heavily, and Census explicitly advises against treating overlapping 5-year estimates as ordinary independent comparisons [R276]. A two-of-three reliability calculation therefore cannot use an independence/binomial argument. Any latent-accuracy claim requires a transparent joint-error and temporal-state sensitivity model; marginal MoEs alone are insufficient.

3. **Closest active neighbor — SURVIVES, NARROWED.** The current May 2026 Soltas version still precisely reconstructs the QCT assignment rule, includes high-sampling-error disqualification and the 20% cap, and simulates ACS sampling variation from marginal normal errors implied by published MoEs [R278]. Its estimand remains LIHTC supply/incidence and the QCT rule is an identifying mechanism, not an evaluation of the post-2016 precision screen's own coverage/designation tradeoff. This does not kill OF-45, but it blocks any novelty claim based merely on reconstructing QCT assignment or simulating ACS noise.

4. **Public-data transport — scientific feasibility confirmed; current runtime ingestion incomplete.** HUD continues to publish the nationwide all-tract workbook [R272]. A Florida Housing Finance Corporation ArcGIS mirror independently exposes the expected HUD-derived tract-level schema, including three releases of `B17001` and `B19013` estimates/MoEs, population, income limits, area population and QCT status [R279], but it is geographically limited and is **not** used as national evidence. The nationwide HUD Excel binary could not be ingested through the current tool path. This is an execution-environment limitation, not evidence for or against OF-45.

### Identification model to preserve

For criterion/release `t`, let `S_t(c)` indicate that the relevant relative MoE(s) pass threshold `c`; let `C_t` indicate that the substantive income or poverty cutoff is crossed. The design-identifiable object is the deterministic policy map

`D(c) = HUD_algorithm({S_t(c), C_t, ranking inputs, populations}_{t=1}^3)`.

The contrast `D(0.50) - D(1.00)` and its decomposition into direct screen failures versus cap-mediated gains/losses are observable once the all-tract inputs are ingested. By contrast, an accuracy contrast relative to latent tract states requires assumptions on both the joint error covariance of overlapping releases and real temporal change in tract conditions.

A useful scale interpretation follows from [R277]: MoER `<=50%` corresponds to coefficient of variation approximately `<=0.50/1.645 = 30.4%`, whereas `<100%` corresponds to CV `<60.8%`.

### Decision

- **OF-45 remains PRIORITY BOUNDED PROSECUTION / NOT C011.**
- **C011 remains unassigned.**
- **No execution project is authorized.**
- The gate is **not complete** because the decisive empirical magnitude questions—national screen-only exclusions, conditional population gradient, and cap displacement—have not been measured.
- Do not promote or kill OF-45 from the identification result alone.

**Next executable action:** obtain the nationwide HUD all-tract QCT artifact through a binary-capable path and immediately run the deterministic replay under `c=0.50` and `c=1.00`, validating the `c=0.50` reconstruction against HUD's published QCT flag. Report (i) release/criterion screen failures, (ii) eligibility changes, (iii) final designation changes, (iv) population-gradient estimates conditional on substantive-threshold distance, and (v) cap-mediated displacement. Only after those quantities are known apply the D031 kill/promotion rule.

## D033 — Nationwide OF-45 replay clears the empirical gate; promote as C011 at SURVIVES / PRE-EXECUTION

**Date:** 2026-09-08

### Mandate

Execute the unresolved national same-data `c=0.50` versus `c=1.00` QCT precision-screen replay using the project-local HUD all-tract workbook, validate the reconstruction against HUD's published 2026 `qct` flag, quantify population-linked screen/eligibility effects and cap-mediated displacement, then apply the D031/D032 kill-or-promote rule without using latent-truth accuracy claims.

### Data provenance and exact validation

The project source `qct_data_2026.xlsx` [R280] contains **85,390 QCT records representing 85,385 unique Census tract IDs**; five tract IDs are split into two HUD records because of the New England HMFA treatment. The workbook combines 2020 Census population/household inputs with 2017–2021, 2018–2022 and 2019–2023 ACS income/poverty estimates and 90% margins of error.

The replay implementation reconstructs HUD's 2026 algorithm [R272] at `c=0.50`: income and poverty precision screening, two-of-three eligibility, average ranking inputs, the both-criteria rank bonus, area grouping, and the 20% population-cap fill rule. It reproduces the published final `qct` flag for **all 85,390 records with zero mismatches**. The release-level derived income ratios and poverty rates also reproduce the workbook fields (within workbook floating precision for income ratios and exactly for the rounded poverty rates).

### Same-data precision-screen counterfactual

Holding all observed 2026 data, substantive thresholds, ranking rules, geography and population-cap machinery fixed, replace only HUD's current `<50%` relative-MoE rule with the earlier `<100%` rule [R271].

| Quantity | `c=1.00` | `c=0.50` | Tightening effect |
|---|---:|---:|---:|
| Income release inputs passing precision screen | 250,287 | 238,673 | -11,614 (-4.64% of `c=1` passers) |
| Poverty release inputs passing precision screen | 235,206 | 95,091 | -140,115 (-59.57% of `c=1` passers) |
| Income-criterion eligible records | 15,545 | 13,620 | -1,925 |
| Poverty-criterion eligible records | 11,850 | 9,175 | -2,675 |
| Eligible under either criterion | 19,253 | 17,210 | **-2,043 (-10.61%)** |
| Final QCT designations | 15,797 | 14,496 | **-1,301 (-8.24% net)** |

The net designation count understates decision churn. Relative to `c=1.00`, the current screen produces **2,063 designation losses and 762 designation gains**, for **2,825 changed final statuses** (17.88% of the `c=1.00` designation count). The losing records contain 6,241,099 persons by `P1`; gaining records contain 3,009,615.

The poverty result is mechanically informative: of the 140,115 poverty release inputs that pass `<100%` but fail `<50%`, **139,854** fail the current screen only because the poverty-count numerator (`B17001est2`) fails the 50% relative-MoE threshold; 220 fail both numerator and denominator, and only 41 fail the denominator alone. The stricter rule therefore acts especially strongly on uncertainty in the estimated number of persons in poverty.

### Population-gradient gate

Among the 19,253 records eligible under `c=1.00`, the raw probability of losing eligibility under `c=0.50` falls from **21.8% in the smallest population decile to 5.3% in the largest**.

This gradient does not disappear after conditioning on proximity to the substantive QCT thresholds. Define each criterion's two-of-three substantive margin from its second-highest `c=1.00` release value: income margin `= second-highest income ratio - 1`; poverty margin `= second-highest poverty rate / 0.25 - 1`. In five strata of overall substantive-threshold distance, the eligibility-loss rates for the smallest versus largest population quintiles are respectively:

- 28.5% vs 7.9%;
- 23.3% vs 6.3%;
- 19.3% vs 4.4%;
- 14.8% vs 3.6%;
- 11.4% vs 2.4%.

As a diagnostic regression robustness check, among the `c=1.00` eligible records a clustered logistic model controls flexibly for separate income- and poverty-threshold margins (decile indicators), old eligibility type, state fixed effects and metro status, with standard errors clustered by QCT cap area. A doubling of tract population is associated with an odds ratio of **0.447** for losing eligibility (95% CI **0.383–0.522**). This is a descriptive policy-mechanism diagnostic, not a causal population effect.

### Cap/ranking displacement gate

There are **442** QCT cap areas represented in the workbook. Under `c=1.00`, 144 exceed the 20% eligible-population cap; under `c=0.50`, only 104 do. **Forty areas cease to be cap-binding solely because the precision screen removes enough eligible population.** Final QCT status changes in 306 of the 442 areas.

The 2,063 designation losses decompose into:

- **1,534** records that directly lose eligibility under the tighter screen; and
- **529** records that remain eligible but lose designation through changed ranking/cap competition.

All **762 gains** are necessarily ranking/cap-mediated because tightening the precision screen cannot create eligibility. Most importantly, **332 gaining records across 87 cap areas in 32 states have no change in any of their own release-level precision-screen pass/fail indicators**. Their QCT status changes strictly because the tighter screen alters other records in the same allocation system. This establishes a nonlocal policy effect rather than merely a tract-local abstention effect.

### Identification boundary retained

The replay identifies a **precision/coverage/designation tradeoff**. It does not identify whether the tighter screen makes each designation more correct relative to latent tract truth. The overlap among consecutive ACS 5-year releases and the absence of cross-release covariance/latent temporal states remain exactly the D032 limitation [R276–R277]. Accordingly, C011 must not headline a latent false-inclusion/false-exclusion reduction without an explicit sensitivity model.

The observable precision profile does tighten mechanically. Among accepted income release inputs, mean relative MoE falls from 0.232 to 0.212. For accepted poverty inputs, the mean of the binding numerator/denominator relative MoE falls from 0.561 to 0.396. These are precision changes in the accepted set, not accuracy estimates.

### Novelty/competition disposition

The targeted post-result recheck continues to surface HUD's policy documents and the same QCT/noise literature rather than a direct evaluation of the post-2016 precision gate. The May 2026 Soltas paper [R278] remains the closest active empirical neighbor: it reconstructs QCT assignment and uses ACS sampling variation for LIHTC identification, but does not estimate the precision screen's population-conditioned coverage and cap-displacement consequences as the policy object.

### Decision

The D031 promotion conditions are met:

- **consequentiality:** PASS — 10.61% eligibility loss and 17.88% final-status churn relative to the looser-screen counterfactual;
- **population dependence after threshold-distance control:** PASS;
- **cap-mediated/nonlocal displacement:** PASS;
- **identification boundary:** PASS / NARROW — policy effects identified, latent accuracy not identified;
- **data/computational feasibility:** PASS — exact national replay from public data;
- **nearest-neighbor differentiation:** PASS, with the contribution kept narrow.

Therefore:

> **Promote OF-45 to C011 — precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation — SURVIVES / PRE-EXECUTION.**

C011 is the first post-C010 candidate to clear deep prosecution. This is **not yet EXECUTION**: the execution protocol must be frozen and the reproducible repository baseline created before substantive project work begins. Discovery-mode literature searching for the primary project should now stop; relevant literature moves to monitoring mode under the Charter stop rule.

**Next executable action:** freeze the C011 execution protocol in chat: primary/secondary estimands, multi-year replication plan, decomposition definitions, robustness/sensitivity analyses, tables/figures, falsification/stop criteria and repository layout. After that protocol is fixed, initialize the Git repository and reproducible analysis environment; that repository/desktop stage is the point at which Work mode becomes useful.

## D034 — Freeze C011 prospective execution protocol; authorize repository baseline, not historical-result inspection

**Date:** 2026-09-08

### Mandate

Resolve the D033 pre-execution design questions before any multi-year historical replay is inspected, and specify the repository baseline that will preserve the prospective boundary in code and Git history.

### Decision

Freeze `20_C011_EXECUTION_PROTOCOL.md` as the controlling execution design for C011.

Key prospective choices are:

1. **Development versus confirmation:** 2026 is the already-seen development/anchor year. QCT years **2016–2025** are the primary confirmatory replication set.
2. **Primary identified estimands:** annual union-eligibility loss, final-status churn, a threshold-distance-adjusted lower-versus-higher population burden contrast, and strict nonlocal designation displacement.
3. **Finite-population framing:** exact annual policy counts/rates are primary; conventional tract-level null-hypothesis p-values are not required for deterministic national policy contrasts.
4. **Population-burden adjustment:** standardize bottom-versus-top population-quintile loss differences over `c=1.00` eligibility type and quintiles of operative substantive-threshold distance. Model-based state/metro adjustment is secondary robustness.
5. **Cap decomposition:** every changed designation must partition exactly into `L1` direct eligibility loss, `L2` own-screen ranking/cap loss, `L3` strict nonlocal loss, `G1` own-screen ranking/cap gain, or `G2` strict nonlocal gain.
6. **Precision frontier:** only `0.50` versus `1.00` is confirmatory. A `0.25–1.00` threshold grid is exploratory mechanism analysis.
7. **Latent accuracy:** excluded from the core project. Any correlated-error/temporal-state sensitivity analysis requires a separate prospective amendment and cannot rescue a weak core result.
8. **Generality:** the first paper is QCT-first. A broader selective-precision-screen framework may be discussed only after the empirical mechanism is established; no generic theorem is required.
9. **Validation gate:** a historical year enters the primary confirmatory summary only after exact reproduction of its official `c=0.50` QCT flag. Fewer than 7/10 exact historical reconstructions triggers a scope reassessment.
10. **Stop/weakening rules:** the protocol pre-specifies consequentiality, population-gradient, strict-nonlocality, novelty and identification stop criteria.

### Repository decision

Resolve D015's deferred naming decision prospectively. The program repository will be:

> **`real-world-statistical-reliability`**

C011 will live under `projects/c011-qct-precision-screen/`, while the full canonical research history is imported under `research/canonical/`. Raw HUD binaries are not committed to ordinary Git history by default; provenance URLs/checksums and deterministic fetch/register scripts are committed.

The first repository baseline must establish the frozen protocol and 2026 regression fixture **before any 2016–2025 result is inspected**. Required tests include exact 2026 reconstruction, screen/eligibility monotonicity, exact five-category decomposition, strict-nonlocal invariants and deterministic output hashes.

### Status consequence

> **C011 — SURVIVES / PROTOCOL FROZEN / REPOSITORY-READY.**

This is still not full `EXECUTION`: repository initialization and the tested 2026 baseline come first. Primary-project discovery remains closed.

**Next executable action:** move to repository-backed execution: initialize `real-world-statistical-reliability`, import the canonical snapshot and frozen C011 protocol, create the C011 project skeleton/environment/tests, and implement the 2026 replay as a passing regression fixture. Stop before inspecting 2016–2025 confirmatory outputs until that baseline is green. This is the first step for which Work/GitHub tooling is materially useful.

## D035 — C011 replication-viability stop triggers; pause decade generalization and require scope reassessment

**Date:** 2026-09-09  
**Status:** HISTORICAL / EXECUTION STOP RETAINED; CURRENT C011 SCOPE CONTROLLED BY D036

### Trigger

The frozen C011 protocol requires exact (`Tier A`) reconstruction of at least **7 of the 10** confirmatory years 2016–2025 before manuscript-level multi-year generalization. A year is Tier A only at **zero record-level mismatches** under the official `c=0.50` replay; non-exact years remain diagnostic and their `c=1.00` counterfactual stays unopened.

Execution produced the following prospective validation state before the stop became mathematically binding:

- **Tier A:** 2016, 2020, 2021, 2022.
- **NON_EXACT_DIAGNOSTIC / counterfactual unopened:** 2017, 2018, 2019, 2023.
- **Unopened:** 2024, 2025.

Once 2023 failed Tier A after its final bounded public-data identification attempt, the maximum possible total became **6/10**, even if both 2024 and 2025 were exact. The pre-specified reconstruction-viability stop is therefore triggered.

### What failed — and what did not

This is primarily a **historical operational-reconstruction/public-data feasibility failure**, not evidence that the C011 policy mechanism disappeared. The non-exact years fail for different provenance reasons: historical cap-geography/denominator ambiguity (2017–2018), an incomplete Alabama operational workbook affecting allocation reconstruction (2019), and unresolved 2010→2020 contributor-population shares required for the 2023 >10% reliability veto.

The 2023 bounded reconstruction is especially informative: 85,368 of 85,400 records had all four older-release reliability decisions independently identified with zero oracle disagreements; only 32 target tracts / 85 target×criterion decisions remained unresolved across 13 states. This is strong evidence of near-reconstruction, but the frozen zero-mismatch/fully-identified gate does not permit promotion.

### Exact-year evidence retained

The validated confirmatory years continue to support the mechanism:

| Year | ELR | CHR | BRD | Strict nonlocal changes |
|---|---:|---:|---:|---:|
| 2016 | 3.955% | 6.146% | +12.239 pp | 161 |
| 2020 | 1.576% | 3.771% | +3.98 pp | 166 |
| 2021 | 1.537% | 4.123% | +3.97 pp | 183 |
| 2022 | 1.898% | 4.738% | +4.475 pp | 169 |

Across these four exact years, the median ELR is about **1.74%** and the median CHR about **4.43%**. Therefore the pre-specified consequentiality weakening rule (`median ELR <2%` **and** `median CHR <2%`) is **not** triggered. BRD is positive in every validated year, and strict nonlocal changes are present in every validated year.

These results may inform scope reassessment, but they do **not** override the failed 7/10 reconstruction criterion.

### Decision

1. **Pause the planned 2016–2025 multi-year generalization claim.**
2. **Do not inspect 2024 or 2025 under the original confirmatory program.** Their inspection cannot restore 7/10 unless at least one currently non-exact earlier year is first independently resolved to Tier A.
3. **Do not retroactively weaken the zero-mismatch gate, introduce a reconstruction tolerance, or use unresolved historical oracle fields to generate counterfactuals.**
4. Reclassify C011 to:

> **C011 — EXECUTION PAUSED / REPLICATION-VIABILITY STOP TRIGGERED / SCOPE REASSESSMENT REQUIRED.**

This status is deliberately not `PARKED` or `NO-GO`: the identified mechanism remains consequential in the exact years, but the originally frozen decade-generalization design cannot be completed from the currently available public operational record.

### Scope-reassessment gate

Before any manuscript-level inference or further historical inspection, evaluate three paths:

- **S1 — Narrow validated-year paper:** assess whether a transparently limited QCT-first paper using the 2026 development anchor plus the four exact confirmatory years has sufficient novelty/decision value without claiming decade-wide confirmation. This would be a post-stop narrowed scope, not completion of the original confirmatory design.
- **S2 — Authoritative-source recovery:** reopen a non-exact year only if genuinely new, independent operational material becomes available (for example HUD code, corrected workbooks, contributor-weight files, or equally authoritative source data) that can resolve the exact reconstruction without tuning to final QCT flags. If at least one non-exact year becomes Tier A, mathematical viability can be restored conditionally, after which 2024–2025 may be reconsidered under a dated scope decision.
- **S3 — Park C011 as first project:** if S1 is too weak for a first-project contribution and S2 has no realistic authoritative-data path, preserve C011 as a documented empirical/reproducibility result and return the primary-project pipeline to opportunity generation.

### Next executable action

Run a **bounded C011 scope reassessment**, not additional annual replay. The reassessment must use only the already-frozen exact-year results and documented non-exact provenance unless a genuinely new authoritative source is introduced.


## D036 — C011 survives the reconstruction stop under a narrowed exact-year scope; first-paper priority retained

**Date:** 2026-09-09  
**Status:** SUPERSEDED BY D037

### Mandate

Resolve the D035 scope-reassessment gate without reopening the failed 2016–2025 decade-confirmation program, weakening the zero-mismatch rule, inspecting 2024–2025, or using counterfactuals from non-exact years.

### Decision

Select **S1 — narrowed validated-year paper** and reject S3 (park C011) for now. S2 (authoritative-source recovery) is closed as a routine execution path and becomes a reopening condition only if genuinely new first-party/equivalent operational material appears.

Reclassify C011 to:

> **C011 — SURVIVES / NARROWED EXACT-YEAR PAPER / FIRST-PAPER PRIORITY RETAINED.**

The original 2016–2025 decade-generalization claim remains abandoned under D035. This is a post-stop scope reduction, not completion or amendment of the original prospective design.

### Frozen narrowed evidence set

- **Development/anchor only:** 2026.
- **Exact confirmatory evidence:** 2016, 2020, 2021, 2022.
- **Provenance/diagnostic only; counterfactual unopened:** 2017, 2018, 2019, 2023.
- **Unopened:** 2024, 2025.

No effect estimate from a non-exact year may enter the inferential evidence set. The main paper must show the admissibility status of all ten frozen historical years so readers can evaluate reconstruction selection.

### Strongest admissible claim

Among the four 2016–2025 QCT designation years that passed the prospectively specified zero-mismatch public-data reconstruction gate, HUD's tighter relative-MoE screen consistently reduced otherwise available eligibility, imposed a larger standardized eligibility-loss burden on lower-population records, and propagated through the 20% population cap to alter final QCT designations for records whose own precision-screen indicators did not change. The same qualitative mechanism appears in the separately designated 2026 development anchor. These results establish recurrence of a selective precision-screen-and-allocation mechanism in exactly reconstructable years; they do **not** establish its prevalence, average magnitude or representativeness across 2016–2025.

### Claims permanently unavailable under the present evidence base

Do not claim:

1. decade-wide confirmation or representative 2016–2025 replication;
2. replacement of the failed 7/10 criterion by a post-hoc 4/4 consistency claim;
3. a typical/average post-2016 annual effect from the exact-year subset;
4. that positive BRD or strict nonlocal displacement occurs in most post-2016 years;
5. any counterfactual evidence from 2017–2019 or 2023;
6. any use of 2024–2025 to improve the apparent replication record;
7. improved latent true-classification accuracy, universal fairness, or a generic statistical theorem.

### Reconstruction-selection limitation

Exact-year inclusion was determined prospectively by reconstructability, not by observed counterfactual effect; non-exact years' `c=1.00` outcomes were never opened. This materially reduces ordinary outcome-driven cherry-picking. It does **not** imply that reconstructability is ignorable. Historical file completeness, geography stability and operational complexity may themselves relate to cap binding or the reliability mechanism. No missing-at-random assumption or statistical correction for unavailable annual counterfactuals is justified. The correct treatment is transparent partial scope.

### Novelty and first-paper decision

The narrowed contribution remains differentiated as a statistical-policy reliability/decomposition study rather than a new general statistical method. The exact-year finite-population replays, selective population burden and strict nonlocal allocation decomposition remain scientifically consequential. Bounded monitoring found no direct occupation of the precision-screen-as-policy estimand. C011 therefore remains the program's first-paper priority rather than being exchanged for an unproven alternative candidate.

### Authoritative recovery rule

Further reconstruction of 2017–2019 or 2023 is **closed** unless genuinely new authoritative operational material appears, such as HUD implementation code, corrected workbooks, archived contributor-weight/crosswalk files, or equivalent first-party evidence. More reverse engineering of the same public inputs is not authorized. 2024–2025 remain unopened under this narrowed paper.

`20_C011_EXECUTION_PROTOCOL.md` remains unchanged as the immutable record of the original prospective design and its failed reconstruction-viability gate.

### Next executable action

Build a **manuscript-quality exact-year evidence package** from already admissible outputs. Freeze the main tables/figures, reconstruction-status table, exact-year descriptive summaries, decomposition presentation, robustness already authorized by the frozen protocol, and explicit reconstruction-selection limitations before drafting the paper. Do not reopen historical reconstruction or primary-project opportunity generation unless manuscript positioning or a new direct competitor later defeats the narrowed project.

## D037 — Final manuscript reproducibility adjudication parks C011 as the first-paper project

**Date:** 2026-09-17  
**Status:** ACTIVE / CONTROLLING C011 MANUSCRIPT DISPOSITION

### New evidence and historical integrity

The final reproducibility artifact at Git commit `bdab3ffa12af914c7cfa9e549d26c14043baa0b8` is the controlling execution record for manuscript admissibility. This durable adjudication supplied evidence unavailable when D036 was made. D035 and D036 remain historically valid records of the decisions supported by the evidence then available; D037 supersedes D036 rather than rewriting it.

### Decision

> **C011 — PARKED / NO-GO FOR FIRST PAPER UNDER CURRENT EVIDENCE / REOPEN ONLY WITH MATERIALLY NEW AUTHORITATIVE OPERATIONAL PROVENANCE.**

C011 is not scientifically falsified. The precision-screen mechanism remains demonstrated in the fully reproducible 2016 replay, and prior historical execution reported Tier-A results for 2020, 2021 and 2022. However, final manuscript-grade adjudication found that only 2016 currently satisfies the complete reproducibility standard. The D036 four-year recurrence claim is therefore no longer manuscript-supportable. D035 already closed the original decade-generalization claim; D037 now also closes the narrowed four-year manuscript and routine reconstruction/reverse engineering.

The original policy-mechanism paper must not be reduced to a one-year manuscript merely to preserve publication momentum. The program objective is a strong, defensible paper, not the thinnest paper that can survive missing artifacts.

### Final year classification

| Year | Historical status / role | Current reproducibility | Manuscript admissible | Controlling reason or result |
|---|---|---|---|---|
| 2016 | Prior Tier A | Fully reproducible | **YES** | `c=.50` mismatches 0; deterministic duplicate runs; counterfactual equivalence across three defensible arithmetic variants. `E1/E.50 = 17,042 / 16,368`; `Q1/Q.50 = 14,057 / 13,619`; churn `864`; decomposition `473 / 159 / 19 / 71 / 142`; strict nonlocal `161`; reproducible BRD `0.12239634180436126`. |
| 2020 | Prior Tier A | Unresolved | **NO** | Exact allocation-area construction and `c=1.00` arithmetic cannot be recovered sufficiently from retained provenance. |
| 2021 | Prior Tier A | Unresolved | **NO** | Bedford City official outcome requires an undocumented blank-geography/exclusion behavior not independently supported by retained public provenance. |
| 2022 | Prior Tier A | Unresolved | **NO** | Two-record Los Angeles cap-boundary ordering cannot be reconciled with retained public numerical/tie provenance without unsupported special treatment. |
| 2026 | Development/anchor | `c=.50` exactly reconstructable; `c=1.00` not currently manuscript reproducible | **NO** | Historical `Q1=15,797` was not confirmed. Regenerated `Q1=15,798` was not promoted because the complete operational implementation was not independently resolved. It is neither confirmatory nor manuscript-supporting counterfactual evidence. |

### Reopening rule

C011 is parked rather than killed because genuinely new authoritative operational provenance could change manuscript admissibility. Qualifying evidence includes:

- original HUD implementation code;
- authoritative historical operational scripts;
- preserved intermediate ranking/allocation files;
- original validated C011 execution artifacts/configurations that independently establish the missing operations;
- equivalent first-party operational documentation.

Do not reopen C011 merely because more reverse engineering of the same public inputs is possible.

### Next executable action

Before returning to broad opportunity generation, conduct a bounded literature/novelty prosecution of the derivative question preserved in `09_OPEN_QUESTIONS.md`: whether C011's forensic execution reveals a publishable, distinct problem about reproducibility, auditability and preservation of operational provenance in public administrative/statistical decision algorithms. This is not yet C012 and not yet a validated gap.

## D038 — C012 killed after final narrowed prosecution

**Candidate:** Decision-preserving disclosure control  
**Date:** 2026-09-17  
**Status:** FINAL / KILLED

### Decision

> **C012 — KILLED / NO-GO FOR FIRST PAPER.**

### Reason

- Broad suppression-aware decision identification was already substantially occupied by disclosure-control, partial-identification and uncertain-ranking literatures.
- The single permitted narrowing to decision-preserving disclosure control was prosecuted.
- Decision-certification utility showed valid properties and useful empirical behavior.
- The release-design problem nevertheless remained an instance of established optimal tabular release, risk–utility and workload-aware task optimization.
- No new disclosure guarantee, release mechanism, inferential theory, scalable algorithm or independently publishable statistical object survived.
- The contribution therefore collapses to a task-specific utility inside an existing framework.

### Preserved findings

- monotonicity under nested feasible sets;
- non-submodularity and non-supermodularity;
- safe-release synergy;
- decision identification without cell identification; and
- divergence between decision-certification and cell-width utility.

These are reusable lessons, not grounds for reopening C012. C012 receives no execution protocol and must not be narrowed again.

## D039 — O002-A1 survives full prosecution; register C013 and freeze controlled execution design

**Candidate:** Release-provenance and temporal-interpretability audit of repeated CDC PLACES/500 Cities estimates  
**Date:** 2026-09-21  
**Status:** ACTIVE / SURVIVES / CONTROLLED EXECUTION DESIGN

### Decision

> **REGISTER NEXT AVAILABLE CANDIDATE AND ADVANCE TO CONTROLLED EXECUTION DESIGN.**

O002-A1 is registered as **C013**.

### Evidence supporting promotion

- A rule-defined eligible corpus of nine temporal PLACES/500 Cities applications was verified and deduplicated.
- The 2016–2025 `release × measure × BRFSS source-year` crosswalk shows rotating source years, carry-forwards, definition changes, geography/population changes and a 2023 interval-method discontinuity.
- In the Rahman mammography reconstruction, four nominal adjacent annual pairs were 100% identical tract by tract and nine releases collapsed to five source waves.
- In the Nguyen Washington, DC reconstruction, high cholesterol contained only four distinct source years and two exact copied pairs, while obesity, diabetes, cancer and poor mental health supplied distinct-source negative controls.
- In the Al Qady colorectal-screening reconstruction, each nominal two-year period collapsed to one source wave; the reported +1.6-point median was not reproduced under either natural archive mapping, and the longer mapping crossed a 50–75 to 45–75 definition change.
- No direct prior study was located that combines a temporal-use corpus, finalized release/measure crosswalk, exact-copy detection and conclusion-level sensitivity analysis.

### Binding scope

C013 audits temporal admissibility and downstream conclusion sensitivity. It does not estimate true local health trends, accuse authors of misconduct, invalidate cross-sectional uses, or treat release differences as true change. Named-paper claims remain bounded by exact reproducibility and public-method availability.

### Next authorized action

Freeze `23_C013_CONTROLLED_EXECUTION_PROTOCOL.md`, then begin only its Stage 0 provenance archive and crosswalk build. Manuscript and conference-abstract drafting remain unauthorized until the execution evidence gate passes.

## Change log

### 0.26.0 — 2026-09-21

- Added D039, registered C013 and authorized controlled execution design.

### 0.25.0 — 2026-09-17

- Added D038 and killed C012 after its final permitted narrowing.

### 0.24.0 — 2026-09-17
- Added D037 from the final reproducibility artifact at Git commit `bdab3ffa12af914c7cfa9e549d26c14043baa0b8`.
- Superseded D036 as the controlling C011 manuscript disposition and parked C011 as the first-paper project without characterizing it as scientifically falsified.
- Recorded final manuscript admissibility by year, closed routine reverse engineering, and established the authoritative-provenance reopening rule.

### 0.23.0 — 2026-09-09
- Added D036: C011 survives as a narrowed exact-year paper; decade generalization remains abandoned, first-paper priority is retained, and routine historical reconstruction is closed.
- Froze the admissible evidence set and reconstruction-selection limitation; 2024–2025 remain unopened and file 20 remains unchanged.

### 0.22.0 — 2026-09-09
- Added D035: the C011 7/10 exact-reconstruction viability stop is triggered after 2023 remains non-exact.
- Paused decade generalization, preserved exact-year evidence, and required a bounded scope reassessment before manuscript inference or 2024–2025 inspection.

### 0.21.0 — 2026-09-08
- Added D034: froze the prospective C011 execution protocol and separated 2026 development from 2016–2025 confirmation.
- Authorized the repository-baseline stage under `real-world-statistical-reliability` while keeping historical-result inspection blocked until baseline tests pass.

### 0.20.0 — 2026-09-08
- Added D033 national OF-45 replay and exact zero-mismatch validation against the 2026 HUD QCT flag.
- Recorded consequential precision-screen effects, conditional population gradient and cap-mediated nonlocal displacement.
- Promoted OF-45 to **C011 — SURVIVES / PRE-EXECUTION** while preserving the latent-accuracy identification boundary.

### 0.20.0 — 2026-09-08

- Added D032: rule reconstruction and identification boundary passed, nearest-neighbor recheck survived, nationwide empirical magnitude gate unresolved.
- Kept OF-45 in bounded prosecution and C011 unassigned; no scientific pass/fail inferred from binary-artifact transport limitations.
- Narrowed the next action to nationwide same-data `c=0.50` versus `c=1.00` replay and cap/population-gradient measurement.

### 0.19.0 — 2026-09-08

- Added D031: bounded theory/data/decision triangulation across four public high-stakes workflows.
- Registered OF-45 as the sole priority bounded-prosecution lead while keeping C011 unassigned.
- Narrowed OF-45 to the post-2016 HUD QCT MoER-screen reliability-versus-coverage tradeoff and set a public-data/identification kill gate.

### 0.18.0 — 2026-09-08

- Added D030: five deliberately diversified domains all collapsed before registration.
- Recorded a second valid null-generation pass; no OF-45 and no C011.
- Switched the next discovery action from further review-first field sweeps to bounded theory/data/decision-channel triangulation under L027/L038.

### 0.17.0 — 2026-09-08

- Added D029: seven review-first routes collapsed before registration; valid null-generation result.
- Kept C011 unassigned and redirected the next pass toward deliberately diversified statistical fields.

### 0.16.0 — 2026-09-08

- Added D028: OF-44 parked after direct partial-identification/matrix-method overlap and insufficient public heterogeneity evidence.
- Applied the stop rule before P3/P4 and kept C011 unassigned.

### 0.15.0 — 2026-09-08

- Added D027: review-first generation produced OF-44 as a bounded-screening lead, not C011.
- Collapsed the generic gridded-population/PPS-uncertainty idea against imperfect-frame/MOS ancestors.
- Consolidated the D024→OF-39 standalone records into file 18 to free project-source slots.

### 0.14.0 — 2026-09-08

- Added D026: exact enumeration proves OF-39's finite-sample conditional-law failure but the novelty gate fails.
- Parked OF-39, kept C011 unassigned, and returned the next action to review-first cross-field opportunity generation.


### 0.13.0 — 2026-09-08

- Added D025: OF-39 survives bounded prosecution but remains below C011.
- Narrowed the live claim to finite-sample joint-adaptive versus fixed-final-graph diagnostic calibration.
- Set exact enumeration/theorem prosecution as the next gate.

### 0.12.0 — 2026-09-08

- Added D024: completed review-first cross-field opportunity generation II.
- Selected OF-39 as the sole priority prosecution lead while keeping C011 unassigned.
- Recorded OF-40–OF-43 dispositions and the four-part OF-39 bounded prosecution plan.

### 0.11.0 — 2026-09-07

- Added D023: OF-35 parked after direct ranking-reliability prosecution; C011 remains unassigned.
- Retained OF-38 only as a theory-heavy informative-assessment sensitivity watchlist.
- Returned next action to review-first cross-field generation with problem-sentence active-work search.

### 0.10.0 — 2026-09-07

- Added D022: review-first cross-field reconnaissance supersedes D013 as the exclusive active discovery neighborhood.
- Advanced OF-35 to bounded prosecution while keeping C011 unassigned and execution unauthorized.
- Marked D013 superseded for active discovery while preserving its map and decisions as canonical history.

### 0.9.0 — 2026-09-07

- Added D021 and parked OF-30 after the bounded novelty/data/theory screen.
- Kept C011 unassigned and returned next action to fresh D013 opportunity generation.

### 0.8.0 — 2026-09-07

- Added D020 after fresh D013 four-channel opportunity generation.
- Advanced OF-30 to **PRIORITY SCREENING** without assigning C011.
- Set a bounded nearest-neighbor/data/theory gate before any candidate promotion.

### 0.7.0 — 2026-09-07

- Added D019: completed collapse-first triage of OF-19–OF-23 and assigned no C011.
- Parked OF-19/20/21/23 in broad form; retained OF-22 only as WATCHLIST / SHARPEN BEFORE CANDIDATE.
- Set fresh four-channel opportunity generation—not forced candidate promotion—as the next step.

### 0.6.0 — 2026-09-07

- Added D018: C010 four-channel prosecution completed; candidate parked as **NO-GO FOR FIRST PROJECT**.
- Preserved the post-filter response-contamination + retained-selection decomposition and reopening conditions.
- Set OF-19–OF-23 as the remaining bounded triage set.

### 0.5.0 — 2026-09-07

- Added D017: completed C009 bounded-mismatch/partial-identification prosecution and parked C009 as **NO-GO FOR FIRST PROJECT**.
- Preserved the joint `delta`-`kappa` decision lemma while recording the Hartman-Huang and misclassification/sensitivity prior-art constraints.
- Marked D016 superseded by D017.

### 0.4.0 — 2026-09-07

- Added D016: broad C009 framing fails as stated; narrowed P/NPS-specific formulation advances to **PROSECUTION — NARROWED** only.
- Corrected the bridge-sample identification assumption.

### 0.3.0 — 2026-09-07

- D012 parked C008 and reopened field selection.
- D013 adopted survey data integration / nonprobability inference as the active first-project neighborhood.
- D014 promoted C009 to SCREENING only.
- D015 broadened the scientific umbrella while deferring infrastructure renaming.
- Marked D006/D009/D010 as superseded/historical where appropriate.

### 0.2.0 — 2026-09-07

- Added D009: first deep map focuses on measurement/observation-process shift.
- Added D010: C008 promoted to SCREENING only; substantive analysis explicitly deferred.
- Added D011: structured reference/search evidence ledger becomes canonical.
