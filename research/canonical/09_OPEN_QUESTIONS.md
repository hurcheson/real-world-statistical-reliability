---
title: Open Questions
version: 0.26.0
last_updated: 2026-09-21
status: active
---

# Open Questions

This file contains leads, not approved projects.

Do not treat an item here as a validated research gap.

Reference IDs point to `11_REFERENCE_LEDGER.md`.

## Current program-level questions

### Active C013 execution questions

These questions are governed by `23_C013_CONTROLLED_EXECUTION_PROTOCOL.md`; they are execution questions for a surviving candidate, not invitations to broaden its claim.

1. How many distinct BRFSS source waves are present for each `release × measure × geography` sequence?
2. Which adjacent releases are deterministic carry-forwards, rare revised carry-forwards, or genuinely new source waves?
3. Which definition, eligibility-population, geography-vintage, poststratification and confidence-interval changes break comparability?
4. After common-geography restriction and source-year alignment, which published temporal claims survive, narrow, change classification or become non-adjudicable?
5. How stable are ranks and policy-relevant sets after carry-forward removal and uncertainty-aware restriction?
6. Can a compact admissibility checklist and machine-readable crosswalk prevent future misuse without implying that PLACES estimates recover true local trends?

### Closed candidate questions

- C011 is parked under D037; routine reconstruction is closed.
- C012 is killed under D038; another decision-utility narrowing is prohibited.

1. Which reliability failure modes in clinical ML are both important and insufficiently resolved?
2. Where do statistical prediction-model methodology and modern distribution-shift ML fail to communicate?
3. Which reliability metrics remain stable under common real-world shifts, and which fail first?
4. When can calibration degrade while discrimination remains apparently acceptable?
5. How should changes in **measurement/observation process** between source and target environments be diagnosed and handled?
6. How can external validation distinguish patient case-mix shift from changes in the way data are measured or recorded?
7. Can uncertainty methods reliably signal when a model is being used outside its valid domain?
8. When should a deployed model be recalibrated, revised, stripped of unstable features, or abandoned?
9. How should subgroup reliability be evaluated when the subgroup distribution and measurement process both shift?
10. Which widely used external-validation practices give falsely reassuring conclusions?
11. Can a simple statistical diagnostic outperform more complex adaptation methods for realistic health-data shifts?
12. How much reliability degradation can be diagnosed before target outcome labels mature?

---

# Mapped candidate families

## OF-01 — Distribution shift × calibration

**Status after mapping pass 1:** important but **crowded in generic form**.

### What is established

- Calibration is distinct from discrimination and central to trustworthy absolute risk [R010–R012].
- Temporal/site shifts often produce calibration degradation [R009, R027, R030–R031].
- Cross-institutional MIMIC/eICU calibration and recalibration are active 2026 topics [R027, R031].

### Remaining useful question

Not “does calibration drift?” but:

> **Which shift mechanism produced the calibration failure, and what action is warranted?**

**Priority:** Medium as a component; Low as a stand-alone generic project.

---

## OF-02 — Distribution shift × missingness / observation process

**Status after mapping pass 1:** scientifically central, but generic missingness-shift methods are crowded.

### What is established

- Missingness/observation patterns can be predictive [R021–R023].
- Missingness mechanisms can shift [R024–R025].
- Clinical presence shift has been explicitly formalized [R026].
- Observation-process features can improve internal discrimination but worsen external calibration [R027].

### Remaining useful question

> **How should external validation attribute reliability loss to observation-process dependence rather than simply report source/target degradation?**

This generated C008/OF-06.

**Priority:** High for focused screening; Low for generic “missingness shift” algorithm development.

---

## OF-03 — Distribution shift × uncertainty

**Status after mapping pass 1:** **crowded / theoretically mature** for a first project.

### What is established

- Conformal prediction under covariate shift has foundational methods [R034].
- Doubly robust prediction-set calibration under shift is active [R035].
- Health-specific transport with weighted conformal methods has already been demonstrated [R036].

### Remaining useful question

Potentially only if tied to a distinct real-world shift mechanism not covered by standard covariate-shift assumptions.

**Priority:** Low for first project.

---

## OF-04 — Distribution shift × subgroup heterogeneity

**Status after mapping pass 1:** important, active, and sample-intensive.

### What is established

- Large subpopulation-shift benchmarks already exist [R037].
- Fairness can fail to transfer and shift structure matters [R038].

### Remaining useful question

Potentially:

> Does observation-process shift create subgroup-specific calibration/utility failures that overall external validation hides?

This becomes OF-11 below.

**Priority:** Medium, likely as a secondary aim after a primary mechanism is established.

---

## OF-05 — Drift detection → model updating

**Status after mapping pass 1:** generic form is crowded.

### What is established

- Dynamic updating methods/pipelines are mature [R039–R041].
- Post-deployment telemetry and calibration drift are active [R030].

### Remaining useful question

> Can a diagnosed shift mechanism determine whether recalibration, refitting, feature removal, or non-use is the defensible action?

This becomes OF-12.

**Priority:** Medium for later work; Low as generic first project.

---

# New opportunity portfolio from mapping pass 1

## OF-06 / C008 — Measurement-process-aware external-validation stress testing

**Priority:** **HIGH — current priority lead**  
**Candidate status:** SCREENING  
**Gap status:** **NOT ESTABLISHED**

### Question

> When does predictive information encoded by missingness, measurement intensity, or observation-process features improve internal performance but make predicted risk non-transportable, and how should external validation diagnose that failure?

### Why it could matter

A model may exploit local workflow information that is useful at the development site but unreliable elsewhere. Deployment decisions need a way to distinguish stable patient signal from source-specific process dependence.

### Direct threats

- General robustness/stability stress testing already exists [R005].
- Predictor measurement heterogeneity is established [R016–R017].
- Deployment-compatible missing-data handling is established [R018–R020].
- Clinical presence shift is explicitly formalized [R026].
- Yamamoto 2026 directly connects observation-process features to worse MIMIC/eICU calibration/transportability [R027].
- Patel/Beedala 2026 already combine external calibration, recalibration, DCA and subgroup analyses across MIMIC/eICU [R031].

### Differentiation that must survive prosecution

At least one consequential combination of:

1. explicit observation-process **attribution/decomposition**;
2. controlled, clinically motivated stress tests;
3. general framework across multiple tasks/environments;
4. interpretable transportability-penalty quantity;
5. diagnostic output that informs deployment/update action.

### Current verdict

**SCREENING. Do not code substantive analyses yet.**

---

## OF-07 — Decompose external failure into mechanism-specific components

**Priority:** High–Medium  
**Status:** IDEA

### Question

Can external reliability degradation be decomposed into contributions associated with:

- case mix;
- outcome prevalence;
- predictor-value distribution;
- measurement procedure;
- observation process?

### Main threat

Without strong design assumptions, “attribution” can be mistaken for causal decomposition. Existing conditional-shift stress-testing work [R005] may already cover important parts.

### Needed before promotion

Define whether the target is causal, perturbational, sensitivity-based, or descriptive.

---

## OF-08 — Workflow-signal gain versus transportability penalty

**Priority:** High as C008 sub-aim; Low–Medium stand-alone  
**Status:** IDEA

### Question

How much internal predictive gain comes from workflow/observation features, and how much external calibration/utility is lost when those features are unstable?

### Threat

R027 already demonstrates the core qualitative tradeoff in sepsis mortality.

### Possible role

Use as a quantitative diagnostic inside C008 rather than claiming the concept itself as novel.

---

## OF-09 — Measurement-process-aware internal-external validation / environment stress testing

**Priority:** Medium–High  
**Status:** IDEA

### Question

Can internal-external cross-validation across hospitals/units be structured around measurement-process environments rather than geography alone?

### Why interesting

A model could be tested across environments defined by data-collection policies, interface availability or measurement-intensity profiles.

### Threat

Internal-external cross-validation, leave-one-site-out validation, domain generalization and distributionally robust optimization are mature families. Prior art must be prosecuted before promotion.

---

## OF-10 — Clinical-utility degradation attributable to observation-process shift

**Priority:** Medium–High  
**Status:** IDEA

### Question

Can measurement-process dependence produce clinically meaningful net-benefit loss even when AUROC remains acceptable?

### Threat

R031 already includes decision-curve analysis in cross-institutional validation. Differentiation must be **mechanism attribution**, not merely adding DCA.

---

## OF-11 — Subgroup × observation-process shift

**Priority:** Medium  
**Status:** IDEA

### Question

Do changes in clinical measurement/workflow create subgroup-specific calibration or utility failures hidden by overall external performance?

### Why important

Observation/measurement processes can themselves vary by demographic, socioeconomic or disease factors [R028].

### Threats

- fairness-transfer literature is active [R038];
- high-dimensional subgroup/site interactions require substantial sample sizes;
- risk of post-hoc fishing.

---

## OF-12 — Shift mechanism → update action

**Priority:** Medium  
**Status:** IDEA

### Question

Given a diagnosed external failure, when is the defensible action:

- intercept recalibration;
- slope + intercept recalibration;
- full refit;
- feature removal;
- abstention/non-use?

### Threat

Generic dynamic updating is mature [R039–R041]. The contribution would have to be mechanism-specific.

---

## OF-13 — Target-risk estimation under observation-process shift + delayed/selective labels

**Priority:** Medium  
**Status:** IDEA

### Question

Can target performance be estimated when both covariate/observation mechanisms and label availability differ?

### Threat

R033 directly studies target risk under joint covariate shift and selective labels. Theory/identification burden is high.

### Program fit

Potential later methodological project, not preferred first execution candidate.

---

## OF-14 — Label-free workflow monitoring using missingness and latency

**Priority:** Low–Medium  
**Status:** IDEA / crowded

### Question

Can changes in input availability, missingness and latency serve as early warning signals before outcome labels arrive?

### Threat

R030 provides direct 2026 post-deployment evidence for this strategy across four systems.

### Verdict

Do not promote generic form.

---

## OF-15 — Harmonization can mask measurement-process reliability failures

**Priority:** Medium exploratory  
**Status:** IDEA

### Question

When multi-database harmonization maps heterogeneous data into common variables, can it erase exactly the provenance differences needed to diagnose measurement-process shift?

### Basis

BlendedICU intentionally harmonizes multiple ICU sources [R047–R048].

### Important qualification

The masking hypothesis is **our inference**, not a demonstrated result from R047.

### Needed

Search OMOP/common-data-model literature on provenance, missingness and transportability before treating this as a candidate.

---

## OF-16 — Generic robust predictor under missingness shift

**Priority:** Low  
**Status:** DEPRIORITIZED IDEA FAMILY

### Reason

R024–R026 show theoretical, algorithmic and clinical-presence approaches are already active.

---

## OF-17 — Generic conformal/UQ method under shift

**Priority:** Low  
**Status:** DEPRIORITIZED IDEA FAMILY

### Reason

R034–R036 and the CMU/StatML ecosystem indicate a dense, mature frontier for a first project.

---

# Parked historical leads

The following are retained for later, not for present investigation:

- partial-identification/sensitivity analysis for variability under informative observation;
- diagnostics for when informative observation materially corrupts variability estimates;
- two-stage EHR recording (visit vs biomarker selection) when the estimand is variability.

These emerged during C002 prosecution and were deliberately not pursued.

---

# Immediate open questions for C008 screening

1. What exact estimand is meant by “observation-process contribution” to reliability degradation?
2. Does R005 already supply the necessary shift-stress-testing machinery once observation variables are explicitly modeled?
3. How much of C008 is already present in supplementary/follow-up work to R027?
4. Can clinically realistic observation-process interventions be defined without arbitrary random masking?
5. Does eICU site/unit metadata permit reliable construction of measurement-process environments?
6. Can source/target physiology be held sufficiently comparable to make a process-shift analysis interpretable?
7. Should the first task be mortality, sepsis, deterioration, length of stay, or another endpoint where observation processes matter differently?
8. Is a multi-task benchmark scientifically stronger, or does it dilute mechanism-specific interpretability?
9. Which reliability outcome should be primary: calibration slope, flexible calibration error, proper score, net benefit, or a mechanism-specific degradation quantity?
10. What result would cause C008 to be killed immediately?

---


# Active opportunity portfolio after field pivot

The earlier OF-01–OF-17 records remain historical products of the ML-reliability map. They are not deleted, but C008 and its neighborhood are no longer the current first-project priority.

## OF-18 — Cross-source auxiliary-scale mismatch in P/NPS calibration

**Linked candidate:** C009  
**Priority:** **PARKED — NO-GO FOR FIRST PROJECT**

Stage-2 prosecution resolved the immediate open gate.

What the prosecution established:

- the binary toy model admits an exact two-parameter sensitivity representation `mu = mu_B + ((d_obs-delta) Delta_W)/kappa`;
- `delta=q_A-q_B^P` is the wrong-reference-scale mismatch;
- `kappa=Corr(X,W_B|R=1)^2` under the toy assumptions is the fraction of the true latent-X correction recovered by correct-scale proxy calibration;
- the representation yields explicit thresholds for sign reversal, exact cancellation, over/under-correction, and when calibration is worse than no adjustment;
- bounded source-specific misclassification can be propagated to a sensitivity envelope, but the envelope broadens rapidly as correctness bounds weaken.

Why it is parked:

1. Hartman & Huang [R120] substantially cover the `delta`-only operation by varying the unknown target-population margin of a partially observed weighting covariate.
2. Molinari [R121] already provides generic partial-identification machinery for discrete misclassification under lower-bound restrictions on correct reporting.
3. Differential measurement-error sensitivity and error-prone weighting have strong prior art [R122–R124, R114, R089].
4. RANDS documents a real P/NPS provenance/mode contrast and balancing on shared demographics, but supplies no gold X or source-specific validation rates capable of anchoring `delta`/`kappa` [R092–R096].
5. External survey-reliability evidence is construct- and subgroup-specific; it does not justify one transferable tight correctness bound for RANDS adjustment variables.

The remaining joint mismatch×proxy-attenuation lemma is worth preserving, but it is not currently large or empirically anchored enough to justify the program's first execution project.

**Reopen if:** a representative bridge/validation dataset, defensible construct-specific measurement bounds, or a genuinely nontrivial multivariable extension becomes available.

**Prosecution record:** `13_C009_IDENTIFICATION_PROSECUTION.md`.

## OF-19 — Sensitivity analysis under nonignorable NPS participation

**Status:** **PARKED IN BROAD FORM — NO C011**  
**Priority:** LOW unless sharpened

Direct 2025–2026 NPS nonignorability/sensitivity work occupies the generic contribution [R080, R144, R146], while R143 supplies a strong adjacent ancestor from nonignorable probability-sampling/nonresponse inference.

**Reopen only if:** a specific interacting failure mechanism changes the sensitivity object, identification structure or decision in a way not covered by current nonignorable-NPS methods.

## OF-20 — Regression/association parameters under data integration

**Status:** **PARKED IN GENERIC FORM — NO C011**  
**Priority:** LOW–MEDIUM if mechanism-specific

Direct regression data-integration/model-calibration work already exists [R086]. “Associations can fail differently than means” is not sufficient differentiation.

**Reopen only if:** a precise population association/regression estimand has a mechanism-specific identification or robustness result that existing integration methods do not provide.

## OF-21 — Safe/selective borrowing from NPS

**Status:** **PARKED IN BROAD FORM — NO C011**  
**Priority:** LOW unless a distinct loss/uncertainty structure emerges

Test-and-pool methods already use the probability design to decide whether to borrow the NPS or retain probability-only inference, with MSE-targeted tuning and robust intervals [R073]. Current efficient DR-combination work further crowds the space [R074].

**Reopen only if:** a specific measurement/coverage/selection failure induces a borrowing decision not reducible to existing pretest, shrinkage or robust-combination methods.

## OF-22 — Drift in nonprobability participation mechanisms across repeated survey waves

**Status:** **WATCHLIST / SHARPEN BEFORE CANDIDATE — NO C011**  
**Priority:** MEDIUM as a narrowed residue

The broad claim is directly occupied. Jackson et al. [R142] explicitly study a recurring hybrid P/NPS tracking poll, show that the characteristics explaining NPS selection can change across waves, and show that stale raking can distort trends.

The remaining potentially interesting question is narrower:

> With NPS observed every wave but a probability/reference sample available only intermittently, what can be detected or bounded about participation-mechanism drift between anchor waves, and when should stale adjustment be rejected?

This is **not yet a candidate**. Promotion requires a repeated-wave estimand, explicit anchor schedule, minimal temporal identification assumptions, an observable diagnostic/bound tied to inferential error, public/reproducible data, and a theorem-level distinction from R142 plus refreshment-sample methods [R145].

## OF-23 — Overlap/undercoverage diagnostics tied to inferential decisions

**Status:** **PARKED IN BROAD FORM — NO C011**  
**Priority:** LOW unless a new estimand/decision loss emerges

Deterministic-undercoverage methods already use positivity/convex-hull structure [R071], while BLS/peer-reviewed thresholding work directly excludes low-overlap NPS units to reduce estimation error [R079].

**Reopen only if:** a different inferential target or decision loss yields an action rule not reducible to existing undercoverage/thresholding machinery.

## OF-24 — Total-survey-error quality failures × selection adjustment

**Status:** **PROSECUTED AS C010 — PARKED / NO-GO FOR FIRST PROJECT**

**Historical priority:** MEDIUM

This opportunity was sharpened into C010: selection-aware response-quality filtering in nonprobability survey inference. The four-channel prosecution confirmed that quality filtering can act as a second selection mechanism and that real screening rules can change benchmark accuracy and sample composition.

The broad contribution failed because direct filter-before-reweighting work already exists [R127], selection bias from attention-check exclusion is formally analyzed [R128], and generic NPS measurement-error × representativeness methods are current [R125–R126]. The remaining no-gold-standard classifier/threshold problem is scientifically real but not sufficiently distinct or identified for the first project [R141, R121].

Reopen only with credible respondent-quality validation data/design or a genuinely new post-filter calibration identification/decision result. See `14_C010_RESPONSE_QUALITY_FILTERING_PROSECUTION.md`.

## OF-25 — Reference/control-total uncertainty

**Priority:** LOW–MEDIUM

How much inferential uncertainty is understated when calibration controls/reference distributions are themselves estimated? Classical survey theory exists; requires a modern data-integration-specific failure mode.

## OF-26 — CDF/quantile integration

**Priority:** **DEPRIORITIZED**

Direct 2026 probability/NPS CDF/quantile methodology exists [R084].

## OF-27 — Nonprobability samples for small-area estimation

**Priority:** **DEPRIORITIZED for first project**

A very current August 2026 review/comparative simulation already maps and extends the area [R107].

## OF-28 — Multiple reference probability surveys

**Priority:** **DEPRIORITIZED**

Direct 2026 framework exists [R083].

## OF-29 — Generic measurement error + representativeness

**Priority:** **DEPRIORITIZED in generic form**

Direct 2026 work exists [R085]. The narrower adjustment-variable measurement interface was prosecuted via C009 and is now **PARKED / NO-GO FOR FIRST PROJECT** after stage 2; preserve it only as a possible revival path.


## OF-30 — Finite-benchmark certification / benchmark-to-target transportability

**Status:** **PARKED AFTER BOUNDED SCREENING — NO C011**  
**Priority:** LOW / REOPEN ONLY WITH NEW STRUCTURE

Working question:

> When does low observed bias on a finite benchmark set legitimately certify low bias for unbenchmarked target outcomes, and how should benchmark sets be chosen to minimize false certification?

Why it survived fresh generation:

- Pew explicitly warns that performance on its government-benchmarked variables need not imply the same bias for political-attitude targets [R150].
- NCHS RSS uses benchmark bias operationally and moved in Round 4 toward benchmarks related to main survey content [R148].
- Multiple benchmark-rich data substrates exist for held-out pseudo-target validation [R151–R153].
- The theory object is distinct from another adjustment estimator: finite benchmark success cannot universally certify an unrestricted target class.
- Agencies/vendors must choose benchmark content and decide whether a panel/method/release is “good enough” for outcomes without truth.

**Promotion gate:** direct nearest-neighbor search for benchmark-validity/generalization frameworks; audit enough independent benchmark outcomes for nested/leave-domain-out validation; establish a nontrivial identification/bound/design or reproducible failure law that changes benchmark selection or quality certification.

**Kill if:** the exact certificate/generalization framework already exists, the theory reduces to trivial decomposition plus standard cross-validation, the held-out design is not credible, or no real decision changes.

Full generation record: `16_D013_FRESH_OPPORTUNITY_GENERATION.md`.

## OF-31 — Adaptive benchmark reuse / quality-assessment overfitting

**Status:** **PARKED WITH OF-30 — NOT AN INDEPENDENT CANDIDATE**  
**Priority:** LOW

If benchmark outcomes are used to tune calibration/weighting/provider choice and then the same outcomes certify the winner, the reported quality may be optimistically selected. A nested benchmark-holdout design can test this.

Do not promote separately unless survey-specific structure escapes generic model-selection/cross-validation theory [R149].

## OF-32 — Target/control-universe mismatch in calibration

**Status:** **WATCHLIST / HIGH PRIOR-ART THREAT**  
**Priority:** LOW–MEDIUM

The Census Bureau reports that March and May 2026 HTOPS weights used controls including Group Quarters even though the survey target excluded them, producing target/control-universe misalignment [R156]. This is a strong production failure signal but likely overlaps erroneous-control calibration theory and C009-adjacent wrong-reference logic.

Reopen only with a sharper P/NPS-specific identification/decision result and a usable corrected-data validation design.

## OF-33 — Cross-vendor respondent overlap and false diversification

**Status:** **PARKED IN BROAD FORM**  
**Priority:** LOW

RAND's six-panel WEA study required cross-panel deduplication and observed more self-reported prior completion in a nonprobability aggregator [R157]; older vendor work documents substantial overlap [R158]. However, current multi-vendor averaging/subset work directly studies common/redundant vendor error [R159].

Reopen only if actual identity overlap yields a distinctive covariance/identification result with obtainable linkage information.

## OF-34 — Statistical source redundancy under source loss/quality change

**Status:** **PARKED IN BROAD FORM**  
**Priority:** LOW

Broad decisions about which source to retain, drop or adapt under changing source quality are already represented in current multiple-source adaptive-survey design [R160].

Reopen only with a mechanism-specific inferential loss or constraint not reducible to existing multi-source adaptation/combination work.

## OF-30 screening resolution

The bounded gate in `17_OF30_BOUNDED_SCREENING.md` is complete.

- **Nearest-neighbor:** heavily crowded by R-indicators, statistic-specific bias measures and outcome-specific selection-bias diagnostics [R161–R164].
- **Data:** viable for grouped/nested validation using Pew and NCHS [R166, R169].
- **Theory:** failed. Unrestricted benchmark-to-target certification is impossible in an elementary way; useful restrictions map to existing function-class bias bounds or predictive benchmark-selection models [R165, R168].

**Reopen OF-30 only if** a genuinely survey-specific identification/decision structure appears that cannot be expressed by those ancestors. Do not reopen merely to run random benchmark cross-validation or demonstrate that benchmark rankings vary.

## OF-35 — Prediction-evaluation ranking reliability under interval censoring / imperfect assessment

**Status:** **PARKED / NO-GO FOR FIRST PROJECT**  
**Priority:** CLOSED unless reopening conditions change

The bounded prosecution is complete in `19_OF35_INTERVAL_CENSORING_RANKING_PROSECUTION.md`.

The broad question is directly threatened on both sides. Yang et al. already fit three competing prediction models and compare interval-censored evaluation procedures against exact-event-time oracle metrics [R183]. Bahrini et al. (ICML 2026) directly quantify censoring-induced distortion of survival-model rankings using standard versus oracle true-event-time evaluation [R189]. Interval-censored scoring validity/monitoring assumptions are also an active 2026 frontier [R190].

Wrong-winner probability and selection regret remain useful summaries, but without new theory they are transformations of differential score error already generated by these designs.

**Reopen only if:** a distinct interval-censoring result emerges—e.g., an identification theorem, sensitivity region, ranking bound or decision rule tied to Case-K monitoring—that is not a censoring-type substitution and is not occupied by R190–R192.


## OF-36 — Synthetic-data inferential reliability

**Status:** **WATCHLIST / HIGH COMPETITION**  
**Priority:** MEDIUM

Recent review and empirical work establish a real validity problem for inference from synthetic data [R170–R171], but June–August 2026 work is rapidly adding formal guarantees and analysis frameworks [R172]. Complex-survey synthetic inference is also already developed [R173].

Reopen only with a narrow decision/failure object that is not generic “inferential utility” and that survives an active-work scan immediately before prosecution.

## OF-37 — Multiverse defensibility and inference implementation

**Status:** **WATCHLIST / META-RESEARCH**  
**Priority:** LOW–MEDIUM

Formal multiverse inference is already available [R176], so a generic method-extension claim is unsafe. A 2026 audit nevertheless finds formal inference and explicit defensibility checks uncommon in applied multiverse studies [R177].

Reopen only if a concrete statistical decision, diagnostic or defensibility criterion emerges that is more than an uptake/descriptive audit.

## OF-38 — Sensitivity of model choice to informative Case-K assessment

**Status:** **WATCHLIST / THEORY-HEAVY — NOT C011**  
**Priority:** LOW–MEDIUM

Residual question from OF-35:

> When the monitoring/assessment process for Case-K interval-censored outcomes is genuinely informative, what model-ranking conclusions remain identifiable or robust as the non-informative monitoring assumptions used by evaluation procedures are relaxed?

The only promising contribution would be stronger than an empirical benchmark: a parameterized sensitivity region, partial ranking/identification result, bound or decision rule. The area is already active in informative interval-censoring regression, variable selection and model averaging [R191–R192], while current ICML work studies interval-censoring scoring assumptions [R190].

**Do not promote** unless a tractable mathematical object survives direct searches against those literatures and can be executed at first-project scale.

## OF-39 — Calibration of Bradley–Terry diagnostics under outcome-adaptive comparison scheduling

**Status:** **PARKED / MECHANISM ESTABLISHED, DISTINCT CONTRIBUTION NOT ESTABLISHED**  
**Priority:** LOW / REOPEN ONLY ON NEW THEOREM OR EMPIRICAL LEVER

The broad question has been prosecuted. Predictable adaptive scheduling does not automatically destroy Bradley–Terry asymptotics because null score increments retain a martingale-difference structure. However, the **final adaptive graph is non-ancillary** [R195], so treating it as a fixed design can target the wrong conditional null law.

Bounded freeze-versus-replay simulations found a genuine endogeneity effect beyond graph topology alone, and scheduler replay improved null calibration. Sparse-cell GOF [R214], existing replay-bootstrap prior art [R195], and general adaptive-design asymptotics [R197, R215–R216] prevent immediate promotion.

**Refined question:**

> How should Bradley–Terry diagnostics be calibrated when the comparison graph is generated outcome-adaptively, and what inferential error is created by conditioning on or resampling the final graph as though it were ancillary?

The exact gate is complete. A four-object enumeration shows a support-level difference between the true adaptive conditional law and the frozen-final-graph product law, and an oracle Pearson statistic is exactly miscalibrated by frozen conditioning at some nominal levels. This proves the mechanism but does not rescue the candidate: the truncation law is a direct consequence of Hamilton & Tawn's non-ancillarity result [R195], and exact scheduler replay is a generic reference construction rather than a new Bradley–Terry theorem.

**Reopen only if:** a fitted-parameter diagnostic theorem, a new calibration/bound when full scheduler replay is unavailable, a design-versus-diagnostic-power theorem with an actionable scheduling rule, or a uniquely informative documented adaptive system creates statistical content not mechanically inherited from R195/R197.

Exact gate and prior prosecution are preserved in the consolidated D024→OF-39 chain inside `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

## OF-40 — Source-aware deployment validation for multisource spatial data fusion

**Status:** **WATCHLIST / EMPIRICAL-METHODOLOGICAL**  
**Priority:** MEDIUM

Question: which deployment error is a CV procedure estimating when co-located/correlated information from a different source remains in training? Current sensor-fusion reviews flag validation/generalizability weaknesses [R199], but correlated and geospatial CV theory already occupies the broad leakage problem [R200–R201].

**Reopen only if:** a precise source-availability deployment estimand cannot be reduced to existing correlated/geospatial CV targets and public multisource data permit direct validation.

## OF-41 — Partial identification of probabilistic prediction performance under outcome misclassification without a gold standard

**Status:** **WATCHLIST / THEORY-HEAVY**  
**Priority:** MEDIUM

Potential targets include true Brier score, calibration quantities and pairwise model ordering when outcome sensitivity/specificity are only bounded. Direct validation correction [R202], general misclassification partial identification [R203], imperfect-reference-test bounds [R204] and weak-supervision/model-evaluation work [R205, R212] create substantial prior-art pressure.

**Reopen only if:** a genuinely new sharp result for continuous risk-score/calibration functionals, useful sensitivity geometry and valid inference for the identified set can be established.

## OF-42 — Full parametric goodness-of-fit for count time series under time-varying underreporting

**Status:** **PARKED / SECONDARY**  
**Priority:** LOW–MEDIUM

The broad failure principle is already occupied: conventional dependence tests can fail under underreporting and robust bootstrap tests exist [R206], against a mature count-time-series diagnostics literature [R187].

**Reopen only if:** a specific full-parametric INAR/INGARCH GOF statistic has a genuinely new null law under reporting distortion and is not a routine extension of R206.

## OF-43 — Extreme conditional quantiles with covariate measurement error

**Status:** **WATCHLIST / THEORY-HEAVY**  
**Priority:** LOW–MEDIUM

Conditional extreme-quantile methodology is active [R207], while ordinary quantile regression under covariate measurement error has strong established methods and theory [R208–R209].

**Reopen only if:** a tractable special case yields a clean identification/asymptotic result and first-project-scale simulation, or relevant specialist collaboration becomes available.



## OF-44 — Downstream inferential reliability under heterogeneous 1997↔2024 SPD-15 bridging

**Status:** **PARKED / NO-GO FOR FIRST PROJECT**  
**Priority:** REOPEN ONLY ON NEW STRUCTURE OR DATA

P1 failed because generic direct-misclassification partial-identification theory already gives sharp regions for arbitrary real functionals under restrictions on a categorical misclassification/transition matrix [R228], while matrix methods already cover corrected standardized rate ratios under polychotomous misclassification [R229]. The intended sign/ranking/trend tipping certificate is therefore not currently a distinct theorem.

P2 was reproducible only at the national/aggregate level. Public bridge factors, programs and mock data exist [R223], but the important geographic/nativity/time heterogeneity is not publicly identified by a simultaneous dual-format validation sample; Census describes linked 2015 NCT↔2020 Census evidence and Phase-2 subnational development as internal/ongoing routes [R224]. Public content-test reports provide aggregate form comparisons, not the required stratum-specific transition matrices [R230].

**Reopen only if:**

1. Phase-2 or another public source releases stratum-specific bridge/dual-coded data adequate to constrain heterogeneity; or
2. a new structural restriction yields a theorem/decision rule not obtainable as a direct corollary of generic matrix partial identification; or
3. an application supplies a scientifically necessary bridge-validation design with a contribution beyond sensitivity analysis itself.

Per the stop rule, the planned P3 toy theorem and P4 consequentiality check were not run.


## D029 discovery status — no new open opportunity registered

D029 does **not** add OF-45 or any other opportunity identifier. Seven candidate routes were screened at the review/problem-sentence/ancestor gate and collapsed before registration [R231–R246].

The absence of a new OF entry is intentional. The active open-question portfolio remains OF-01–OF-44 with their existing statuses; C011 remains unassigned.

**Next discovery question:** can a deliberately diversified review-first pass across statistical domains that have not dominated prior reconnaissance expose a reliability object that survives exact problem-sentence search, classical-ancestor search, active-work competition and first-project feasibility simultaneously?

## D030 discovery status — diversified review-first search also returns null

D030 does **not** add OF-45 or any other opportunity identifier. Five deliberately distant domains were screened and all collapsed before registration [R247–R260].

This strengthens the evidence that simply sampling more current review literatures is now a low-yield discovery strategy for the first-project search. The open-question portfolio remains OF-01–OF-44 with their existing statuses; **C011 remains unassigned**.

**Next discovery question:** can a reproducible public-data anomaly or concrete agency/practitioner decision, independently supported by a first-principles statistical mechanism, expose a reliability object that survives later literature/ancestor prosecution?

**Registration rule for the next pass:** require convergence of at least two of the theory-, data- and decision-generated channels before creating OF-45.

## OF-45 — Reliability-versus-coverage consequences of HUD's post-2016 ACS precision screen in QCT designation

**Status:** **PROMOTED TO C011 / PRE-CANDIDATE QUESTION CLOSED**  
**Priority:** HIGH

### Problem sentence

HUD designates Qualified Census Tracts using noisy ACS income/poverty estimates, rejects inputs with large relative margins of error, requires eligibility in at least two of three overlapping ACS releases, and may then apply a 20% population cap. Since 2016 the reliability screen has been materially stricter than in earlier QCT designations [R267, R271]. Treasury separately warns that incorporating ACS sampling error into tract-level eligibility proxies can systematically disadvantage lower-population areas [R268].

**Open question:** under the post-2016 QCT regime, what reliability gain is attributable to the tighter MoER screen, what population-dependent exclusion burden does the screen create, and how do the two-of-three and population-cap steps translate screen failures into final designation changes?

### What is already known and cannot be claimed as novelty

- Smaller tracts have higher QCT misclassification risk under ACS sampling error [R269].
- False inclusion and false exclusion cannot both be eliminated, and the 20% cap complicates error handling [R269].
- Threshold-based program eligibility can be unstable across ACS releases [R270].
- Abstention/selective classification can improve average accuracy while magnifying group disparities [R274].
- QCT sampling variation and high-error disqualifications already appear in current LIHTC empirical work [R273].

### Surviving possible contribution

A reproducible **current-policy failure analysis / benchmark** that isolates the post-2016 MoER screen from the substantive poverty/income thresholds and from the 20% cap:

1. reconstruct current QCT designation from HUD public all-tract data [R272];
2. replay the same tracts under the pre-2016 MoER threshold (<100%) and current threshold (approximately <=50%) while holding other rules fixed where possible [R271];
3. measure screen coverage/exclusion by tract population and substantive-threshold distance;
4. quantify nonlocal designation displacement created by the 20% cap; and
5. separate directly observed policy-counterfactual changes from model-based/sensitivity claims about latent true classification error.

### Immediate prosecution questions

1. Can the 2016/current rule be reconstructed exactly enough from archived HUD inputs to isolate the MoER-threshold change rather than concurrent rule/data changes?
2. How large is the screen-only exclusion rate under the current rule, and how strongly does it vary with tract population after conditioning on poverty/income proximity?
3. How many final designations change because of the cap after screen-induced eligibility changes, including gains by tracts that were not themselves screen failures?
4. Can covariance across overlapping ACS 5-year releases be obtained or bounded well enough for a defensible two-of-three reliability analysis?
5. What part of “reliability gain” is identified from public data, and what part requires a latent-error model or sensitivity analysis?
6. Does Soltas [R273] or another current housing/public-finance study already estimate the precision-screen tradeoff itself rather than merely use sampling variation for identification?

### Kill conditions

Park OF-45 if any of the following holds:

- current-versus-old MoER replay changes few eligibility/designation decisions;
- the apparent lower-population burden disappears after conditioning on substantive-threshold distance or other mechanical rule components;
- cap-mediated displacement is negligible;
- the only interesting “reliability gain” requires unverifiable assumptions about latent truth or independent ACS releases;
- or nearest-neighbor prosecution reveals a direct post-2016 evaluation of the same screen tradeoff.

### Promotion condition

Consider C011 only if public-data reconstruction shows a consequential population-dependent coverage/designation effect, the correlated-error/latent-truth boundary can be stated rigorously, and the contribution remains distinct from the direct QCT, threshold-instability, selective-classification and LIHTC neighbors [R269–R274].

### D032 prosecution update

Resolved:

- The pre-2016 reliability test can be represented as relative MoE `<100%` (90% interval excludes zero), while the 2016+ standard is approximately `<=50%` [R271, R275, R277].
- A same-data replay under `c=1.00` versus `c=0.50` identifies the **policy-screen effect** without pretending to reconstruct a historical before/after causal effect.
- Consecutive ACS 5-year releases are overlapping period estimates; independence across the three releases is not defensible [R276]. True error reduction is therefore model/sensitivity dependent.
- The May 2026 Soltas paper remains adjacent rather than directly occupying the screen-evaluation estimand [R278].

Still unresolved and now decisive:

1. Nationwide count/share of tract-release inputs newly rejected at `c=0.50` relative to `c=1.00`.
2. Nationwide eligibility and final-QCT changes under the same-data replay.
3. Population gradient after conditioning flexibly on distance to the substantive income and poverty thresholds.
4. Number and geography of **cap-mediated displacement** cases where a tract's final status changes although it did not itself newly fail the precision screen.
5. Whether these policy effects are large enough to support a first-project contribution without relying on latent-truth accuracy claims.

The public national workbook exists [R272], but its binary artifact was not ingestible in the current runtime. A Florida mirror [R279] is useful only for schema validation and must not be substituted for the national prosecution result.

## D033 closure of OF-45 and open questions for C011

The national empirical magnitude gate is now resolved from the project-local HUD workbook [R280]. The `c=0.50` algorithm reproduces all 85,390 published QCT flags, and the same-data `c=1.00` replay shows material, population-dependent eligibility/designation changes plus cap-mediated nonlocal displacement. OF-45 is therefore **closed as a pre-candidate opportunity and promoted to C011**.

The following questions are no longer open for candidate promotion:

- whether the national effect is negligible — **no**;
- whether the population gradient disappears after substantive-threshold conditioning — **no**;
- whether cap-mediated displacement is negligible — **no**;
- whether the contribution must rely on latent-truth accuracy — **no**, provided the project stays on the identified precision/coverage estimand.

### C011 pre-execution questions to freeze, not rediscover

1. **Primary horizon:** Should the confirmatory paper use 2016–2026 annual within-year replays as the primary generalization set, with 2026 as the validated anchor?
2. **Primary population-burden estimand:** Fix the exact substantive-threshold-distance definition and adjustment specification before multi-year execution.
3. **Cap decomposition:** Pre-specify direct eligibility loss, own-screen ranking/cap change, and strict nonlocal displacement so categories remain mutually interpretable.
4. **Precision frontier:** Decide whether a threshold grid beyond the historical anchors 0.50 and 1.00 is confirmatory secondary analysis or exploratory mechanism analysis.
5. **Latent-accuracy sensitivity:** Decide whether to omit it entirely from the core paper or include a clearly secondary correlated-error sensitivity appendix. It must not be required for the headline contribution.
6. **Generality claim:** Determine whether the paper remains a QCT policy benchmark or develops a broader selective-precision-screen framework; any abstraction must be earned by the empirical mechanism rather than asserted.
7. **Execution stop criteria:** Define what multi-year evidence would materially weaken the candidate—for example, if the 2026 effect is an isolated year or if the adjusted population gradient reverses in most historical years.

These are execution-design questions. They do not reopen broad opportunity discovery.

## D034 closure of C011 pre-execution design questions

The seven D033 pre-execution questions are now frozen rather than left open:

1. **Primary horizon:** 2026 is development/anchor; **2016–2025** are confirmatory replication years.
2. **Population burden:** primary loss rates are by population quintile; the threshold-adjusted burden contrast standardizes bottom-versus-top quintile differences over old eligibility type and operative substantive-threshold-distance quintile.
3. **Cap decomposition:** changed final statuses partition into `L1/L2/L3/G1/G2`, including strict nonlocal categories requiring unchanged own screen indicators.
4. **Precision frontier:** `0.50` versus `1.00` is confirmatory; the `0.25–1.00` grid is exploratory.
5. **Latent accuracy:** omitted from the core paper; any sensitivity appendix requires a separate prospective amendment.
6. **Generality:** QCT-first empirical paper; broader framework only if earned after replication.
7. **Stop criteria:** exact-reconstruction viability, consequentiality, population-gradient direction, strict nonlocality, novelty and identification stops are fixed in `20_C011_EXECUTION_PROTOCOL.md`.

These are no longer open research-design questions. Remaining work is operational execution under the frozen protocol: repository initialization, historical source acquisition/rule reconstruction, exact validation and then confirmatory replay.

## D036 C011 narrowed-manuscript questions

The five D035 scope questions are **closed** by D036:

1. **Validated-year contribution:** CLOSED — yes; C011 survives as a narrowed exact-year paper.
2. **Reconstruction-selection risk:** CLOSED AS DESIGN DISPOSITION — treat it as the principal limitation; do not model unavailable years as missing at random.
3. **Authoritative recovery path:** CLOSED AS ROUTINE TASK — reopen only on genuinely new authoritative operational material.
4. **Reopening condition:** CLOSED — the original 7/10 design is not being rescued; 2024–2025 remain unopened.
5. **First-project decision:** CLOSED — retain C011 as first-paper priority.

The live questions are now manuscript-positioning/robustness questions only:

1. **Main-table freeze:** What is the smallest exact-year table set that shows ELR, CHR, BRD and strict nonlocal displacement without implying decade representativeness?
2. **Reconstruction-status disclosure:** How should the main-text 2016–2025 admissibility table present Tier A, non-exact and unopened years so reconstruction selection is immediately visible?
3. **Population-burden presentation:** Which already-authorized standardized BRD display best communicates the lower-population burden without overinterpreting four annual realizations?
4. **Decomposition presentation:** Which L1/L2/L3/G1/G2 summaries most clearly separate direct screen effects from own-screen-mediated and strict nonlocal allocation propagation?
5. **Precision-purchased framing:** How should the observable improvement in accepted precision profile be reported while keeping latent classification accuracy explicitly nonidentified?
6. **Venue positioning:** Does the final package read most naturally as official-statistics/statistical-policy reliability, applied statistics, or housing-policy methodology?
7. **Novelty monitoring:** Has a direct competitor appeared that makes the post-2016 precision screen's selective coverage and cap-propagation consequences the central estimand? Monitoring only; do not reopen discovery mode absent such evidence.

No live question authorizes additional reconstruction of 2017–2019/2023 or inspection of 2024–2025.

## D037 closure of the narrowed C011 manuscript and bounded derivative lead

The D036 manuscript questions are **closed** by the final manuscript-grade reproducibility adjudication at Git commit `bdab3ffa12af914c7cfa9e549d26c14043baa0b8`. Only 2016 currently meets the complete reproducibility standard. The earlier historical Tier-A results for 2020, 2021 and 2022 remain execution diagnostics, not manuscript-admissible evidence; 2026 remains development/anchor only and supplies no admissible counterfactual result. D037 therefore parks C011 as the first-paper project without treating the mechanism as scientifically falsified.

Routine reconstruction or reverse engineering of the same public inputs is not an open question. Reopening C011 requires materially new authoritative operational provenance.

### Bounded derivative opportunity — not C012 and not a validated gap

> Does C011's forensic execution reveal a publishable and distinct problem about reproducibility, auditability and preservation of operational provenance in public administrative/statistical decision algorithms?

**Status:** BOUNDED LITERATURE/NOVELTY PROSECUTION REQUIRED / NOT C012  
**Priority:** NEXT PROGRAM TASK BEFORE BROAD OPPORTUNITY GENERATION

The next task is a bounded literature/novelty prosecution of this derivative opportunity. It must establish importance, closest prior art, distinct contribution, feasible evidence and competition before any candidate identifier is assigned. A negative prosecution should close the lead and return the program to broad opportunity generation; it must not be rescued by relabeling C011's internal execution history as a new candidate.

## Change log

### 0.26.0 — 2026-09-21

- Added the active C013 controlled-execution questions and closed C011/C012 questions.

### 0.25.0 — 2026-09-17

- Recorded closure of C012 after its final narrowed prosecution.

### 0.24.0 — 2026-09-17
- Closed the D036 narrowed-manuscript questions under D037.
- Added the bounded derivative reproducibility/auditability/provenance lead as the next prosecution task, explicitly not C012 and not yet a validated gap.

### 0.23.0 — 2026-09-09
- Closed the D035 scope-reassessment questions under D036.
- Replaced historical-reconstruction questions with narrowed-manuscript evidence, disclosure, decomposition, framing and venue questions.

### 0.22.0 — 2026-09-09
- Added D035 scope-reassessment questions after the pre-specified 7/10 reconstruction stop became mathematically binding.
- Closed further annual replay as the next action; 2024–2025 remain unopened pending scope reassessment.

### 0.21.0 — 2026-09-08
- Closed the D033 C011 pre-execution design questions by freezing the prospective protocol in file 20.
- Converted the next open work from design choice to repository-backed implementation and exact historical validation.

### 0.20.0 — 2026-09-08
- Closed OF-45's empirical promotion questions after D033 and promoted the lead to C011.
- Replaced the unresolved magnitude gate with bounded pre-execution questions for protocol freeze.

### 0.20.0 — 2026-09-08

- Added D032 partial prosecution result and narrowed OF-45 to the design-identifiable same-data screen counterfactual.
- Marked national empirical magnitude/cap-displacement questions as the decisive unresolved gate.
- Kept C011 unassigned.

### 0.19.0 — 2026-09-08

- Added OF-45 from D031 independent-channel triangulation.
- Classified it as **PRIORITY BOUNDED PROSECUTION / NOT C011**.
- Recorded the narrowed post-2016 QCT precision-screen problem sentence, anti-novelty boundaries, and exact kill/promotion conditions.

### 0.18.0 — 2026-09-08

- Recorded D030 as a second null-generation pass; intentionally added no OF identifier.
- Replaced the diversified-review question with an independent-channel convergence question grounded in L027/L038.

### 0.17.0 — 2026-09-08

- Recorded D029 as a null-generation pass; intentionally added no OF identifier.
- Added the diversified-field discovery question while keeping C011 unassigned.

### 0.16.0 — 2026-09-08

- Parked OF-44 after P1/P2 bounded screening and recorded explicit reopening conditions.

### 0.15.0 — 2026-09-08

- Added OF-44 as the sole D027 priority bounded-screening opportunity; C011 remains unassigned.
- Redirected OF-39 historical file references to the consolidated file 18.

### 0.14.0 — 2026-09-08

- Parked OF-39 after the exact-enumeration theorem gate: phenomenon proved, distinct contribution not established.
- Replaced promotion/kill criteria with narrow reopening conditions.

### 0.13.0 — 2026-09-08

- Updated OF-39 after bounded prosecution: survives only in narrowed finite-sample calibration form; C011 remains unassigned.
- Added exact-enumeration theorem gate and clarified sparse-GOF/adaptive-inference kill threats.

### 0.12.0 — 2026-09-08

- Added OF-39–OF-43 from D024 cross-field opportunity generation II.
- Designated OF-39 as the sole priority prosecution lead without assigning C011.
- Recorded OF-40/41/43 as watchlists and OF-42 as parked/secondary after adjacent-mechanism prior-art checks.

### 0.11.0 — 2026-09-07

- Parked OF-35 after bounded prosecution; no C011.
- Added OF-38 as a theory-heavy informative-assessment sensitivity watchlist only.

### 0.10.0 — 2026-09-07

- Added OF-35 as the sole priority prosecution lead from cross-field review-first reconnaissance.
- Added OF-36 synthetic-data inferential reliability and OF-37 multiverse defensibility as watchlists, not candidates.

### 0.9.0 — 2026-09-07

- Resolved OF-30 screening as parked; preserved reopening conditions.

### 0.8.0 — 2026-09-07

- Added OF-30–OF-34 from fresh four-channel generation.
- Elevated OF-30 to **PRIORITY SCREENING** while keeping C011 unassigned.
- Retained OF-31 as an internal mechanism, OF-32 as watchlist, and parked OF-33/OF-34 in broad form.

### 0.7.0 — 2026-09-07

- Completed collapse-first triage of OF-19–OF-23.
- Parked OF-19, OF-20, OF-21 and OF-23 in broad/generic form; retained OF-22 only as a sharpen-before-candidate watchlist residue.
- Recorded explicit reopening/promotion gates and kept C011 unassigned.

### 0.6.0 — 2026-09-07

- Prosecuted OF-24 as C010 using the four-channel protocol.
- Marked OF-24/C010 **PARKED / NO-GO FOR FIRST PROJECT**.
- Recorded validation/theory conditions required for reopening.

### 0.5.0 — 2026-09-07

- Completed the OF-18/C009 stage-2 sensitivity-utility gate and marked it **PARKED / NO-GO FOR FIRST PROJECT**.
- Recorded the `delta`-`kappa` decision result, prior-art constraints, and reopening conditions.
- Updated OF-29 so it no longer describes C009 as active.

### 0.4.0 — 2026-09-07

- Narrowed OF-18/C009 after stage-1 identification and nearest-neighbor prosecution.
- Replaced the broad measurement-mismatch question with the benchmark-scale versus residual-proxy formulation.

### 0.3.0 — 2026-09-07

- Marked prior ML opportunity portfolio as historical/deprioritized for first-project selection.
- Added OF-18–OF-29 from the survey-data-integration map.
- Linked OF-18 to C009 as the priority screening question.


### 0.2.0 — 2026-09-07

- Reassessed OF-01–OF-05 after deep field mapping.
- Added OF-06–OF-17 opportunity portfolio.
- Promoted OF-06/C008 to priority SCREENING lead.
- Explicitly recorded nearest threats and anti-novelty evidence.
- Added immediate prosecution questions.
