---
title: Cross-Field Statistics Reconnaissance — Review-First Opportunity Search
version: 0.8.0
last_updated: 2026-09-08
status: active composite reconnaissance record — D033 national empirical gate complete; OF-45 promoted to C011; pre-execution
---

# Cross-Field Statistics Reconnaissance — Review-First Opportunity Search

## 1. Purpose

Repeated mechanism-first opportunity searches inside the survey-data-integration neighborhood produced useful lessons but no first-project candidate. This pass therefore changed the discovery order rather than weakening the novelty standard:

> **current statistical field → recent review/guidance → current methods → recurring limitations/contradictions/failure modes → classical ancestors → active-work scan → only then formulate a lead.**

The aim was not to find an untouched topic. It was to locate a research conversation in which a student-scale contribution could be a method, theory result, failure map, evaluation framework, robustness analysis or decision-relevant empirical finding.

This is a bounded reconnaissance, not a systematic review and not candidate approval. Source IDs refer to `11_REFERENCE_LEDGER.md`.

## 2. Screening criteria

Each field was screened for:

1. **current methodological activity** — preferably a 2024–2026 review plus recent methods papers;
2. **a consequential statistical failure or decision**, rather than a decorative metric extension;
3. **nearest-prior-art visibility** — enough literature to prosecute novelty rather than speculate;
4. **student-scale feasibility** — simulation/public data and laptop/workstation computation;
5. **competitive geometry** — whether the obvious contribution is already being solved by multiple active groups;
6. **a definable promotion/kill gate** before any C011 assignment.

## 3. Field-level disposition

| Field | What the recent literature says | Bounded disposition |
|---|---|---|
| Synthetic-data inference/evaluation | A 2026 *Annual Review* frames usefulness, privacy and model reliability as active trade-offs [R170]. Current papers show severe inferential failures for deep generators [R171] and introduce new validity frameworks [R172]. Complex-survey combining rules are already developed [R173]. | **WATCHLIST / HIGH COMPETITION.** Scientifically important, but moving too quickly for the safest first prosecution. |
| Random-effects meta-analysis prediction intervals | A 2026 comprehensive study shows that nominal mean coverage can hide a poor distribution of realized coverage probabilities [R174]. | **BROAD LEAD COLLAPSED.** The natural “high-confidence content coverage” repair is an established tolerance-interval object in meta-analysis [R175]. |
| Multiverse/specification uncertainty | Formal post-selection inference already exists for broad GLM multiverses [R176], while a 2026 audit of 613 applied studies finds formal inference and explicit defensibility checks uncommon [R177]. | **WATCHLIST.** Strong implementation/meta-research conversation, but “invent inference for multiverses” is occupied. |
| Proper scoring / survival-model evaluation | Proper scoring rules are an active 2026 statistics frontier [R178]. New right-censoring and dependent-censoring work explicitly studies evaluation validity and ranking failures [R179–R180]. | **USE AS ANCESTOR/LENS.** Obvious right-censoring score construction is crowded, but it motivates a sharper imperfect-observation evaluation question. |
| Interval-censored regression and prediction evaluation | A 2026 *Annual Review* maps interval-censored regression and open challenges [R181]. Prediction-accuracy estimators already exist and are expanding rapidly [R182–R185]. | **PRIORITY PROSECUTION LEAD.** The remaining question is not another score; it is reliability of model ranking/selection when the assessment process is imperfect. |
| Count time-series diagnostics | A 2026 *Annual Review* maps formal and graphical goodness-of-fit methods [R187], with recent general time-series GOF work [R188]. | **SAMPLED / NOT PRIORITY.** Legitimate field, but the bounded pass did not expose a comparably sharp first-project decision seam. |

## 4. Important negative results

### 4.1 Synthetic-data inference is real but competitively hot

The August 2026 review by Liu and Reiter makes clear that synthetic-data usefulness cannot be separated from privacy and reliability [R170]. Decruyenaere et al. show that naive analyses of deep-generative synthetic clinical trials can produce large false-positive distortions and that simple standard-error correction does not generally solve the deep-generator problem [R171]. At the same time, Tan and Zrnic introduce task-exchangeability guarantees for valid inference from synthetic data [R172].

This is strong evidence of a real statistical frontier, but it is also an active-work warning. A broad project titled “valid inference from synthetic data” would enter a rapidly moving literature with high scoop risk. The complex-survey variant is not an escape hatch: Mathur, Si and Reiter already derive fully synthetic complex-survey procedures and repeated-sampling combining-rule behavior [R173].

### 4.2 The meta-analysis lead failed the classical-ancestor check

Mátrai et al. show that average nominal prediction-interval coverage can conceal an unfavorable distribution of realized coverage probabilities, especially with few studies [R174]. A tempting contribution was therefore to require an interval to contain a specified fraction of the random-effects distribution with high confidence.

That property is essentially a **statistical tolerance interval**. Brannick et al. already adapt content tolerance intervals to random-effects meta-analysis and study their coverage [R175]. The broad opportunity therefore collapses before candidate creation.

This is a reusable search lesson: a recent paper's “stronger guarantee” language can point to an older statistical object rather than a new gap.

### 4.3 Multiverse inference is no longer an empty formal-method cell

PIMA already provides post-selection inference for broad multiverse analyses with generalized linear models and family-wise error control [R176]. The 2026 audit of 613 implementations shows that formal inference is still used in only 10.5% of applications and explicit attention to specification defensibility in only 3.9% [R177].

That leaves a genuine methodological-practice conversation, but the broad formal-inference claim is occupied. A future contribution would need to focus on defensibility, diagnostics, decision rules or uptake rather than simply adding “inference to multiverse analysis.”

## 5. Priority prosecution lead — OF-35

### 5.1 Working question

> **When exact event times are unavailable because outcomes are observed intermittently, do commonly used prediction-performance estimators preserve the oracle ranking of competing survival models under realistic assessment mechanisms?**

More sharply:

> **How often, and under which inspection/assessment mechanisms, does interval-censored model evaluation select a different “best” model from the one that would be selected if the latent exact event times were observed?**

Status: **PRIORITY PROSECUTION LEAD — NOT C011**.

### 5.2 Why this is not “invent another Brier score”

The direct metric-estimation literature is already substantial:

- Wu and Cook develop imputation, IPW and AIPW estimators for prediction error and AUC with interval-censored validation data, explicitly modeling the event, recurrent assessment and loss-to-follow-up processes [R182].
- Yang et al. compare model-based and IPCW approaches for time-dependent AUC, Brier score and predictive cross-entropy under interval censoring and competing risks, including model misspecification and different interval-censoring patterns [R183].
- Kim develops dynamic predictive-accuracy measures for interval-censored failure times with longitudinal markers [R184].
- Tseng and Wang's August 2026 EcoSta work proposes a semiparametric interval-censored Brier-score framework with Murphy decomposition and extensions for sparse inspection schedules, measurement error and incomplete covariate histories [R185].

Therefore a simple “new interval-censored Brier score” claim is unsafe.

The proposed object is instead **evaluation reliability as a model-selection decision**.

### 5.3 Proposed estimands / failure summaries

Let `M_1,...,M_K` be competing prediction models and let `S*(M_k)` denote the target prediction score computed under a fully observed latent event-time oracle in simulation. Let `S_j(M_k)` be an estimator of that score from interval-censored observations under evaluation procedure `j`.

Potential primary quantities are:

1. **pairwise ranking-reversal probability**  
   `P(sign[S_j(M_a)-S_j(M_b)] != sign[S*(M_a)-S*(M_b)])`;
2. **wrong-winner probability**  
   probability that the empirically best model differs from the oracle-best model;
3. **selection regret**  
   oracle-score loss from selecting the winner under an imperfect evaluation procedure;
4. **rank stability** as assessment frequency, interval width, informative visiting, loss-to-follow-up and nuisance-model misspecification vary;
5. **failure decomposition** separating score-estimation bias/variance from differential error that changes model ordering.

These are decision quantities. A procedure can have small average metric error yet still be poor at selecting between two close models if its differential error is systematic or highly variable.

### 5.4 Why there may be a contribution

The nearest literature already studies estimator bias, efficiency, misspecification and censoring patterns [R182–R185]. That is precisely why OF-35 is **not** being called novel.

The possible residual contribution is a systematic cross-method answer to a different practical question:

> **Which evaluation procedure can be trusted to choose among competing prediction models when the outcome-assessment process itself is sparse, misspecified or informative?**

The right-censoring literature supplies strong methodological ancestors. Jonkers et al. show that forecast-dependent plug-in weighted scores can exhibit ranking reversals under right censoring [R179]. Lillelund, Qi and Greiner show that dependent censoring can invalidate standard IPCW Brier-score evaluation and develop a semi-synthetic framework with known event times [R180]. OF-35 must therefore establish what is genuinely interval-censoring-specific rather than repackaging those results.

### 5.5 Candidate simulation axes

Keep the first design deliberately small:

- event model: correctly specified versus misspecified prediction model pair;
- inspection schedule: dense → sparse;
- interval widths: narrow → broad;
- assessment mechanism: noninformative versus outcome/covariate-informative visits;
- loss-to-follow-up: absent versus present;
- nuisance model for assessment/censoring: correct versus misspecified;
- evaluation procedures: a minimal set spanning imputation, IPW/AIPW and model-based approaches from the direct literature;
- target metric: start with one proper accuracy metric plus one discrimination metric only if necessary.

The first prosecution should not become a 20-method benchmark.

### 5.6 Feasibility

The computation is simulation-scale rather than deep-learning-scale. `icenReg` provides interval-censored regression, prediction, imputation, example datasets and interval-censoring simulation functions [R186]. This makes a laptop/workstation-scale feasibility check straightforward.

The strongest scientific claims would be simulation-based because the latent exact event times provide the oracle ranking. A real interval-censored dataset can illustrate how substantive model choice changes across evaluation procedures, but it cannot by itself reveal the oracle winner when exact event times are unobserved.

## 6. Nearest threats to OF-35

| Threat | Why it matters | Required response |
|---|---|---|
| Wu & Cook [R182] | Already studies multiple evaluation estimators and visit-process structure. | Read full simulations and supplementary material for any explicit model-ranking/selection analysis. |
| Yang et al. [R183] | Direct 2026 comparison of model-based vs IPCW metrics under misspecification and censoring patterns. | Test whether their simulations already quantify wrong-winner/ranking reversals across competing models. |
| Tseng & Wang [R185] | Active 2026 work adds Brier/Murphy decomposition under sparse schedules and measurement error. | Avoid metric-construction novelty; monitor manuscript/software when available. |
| Jonkers et al. [R179] | Establishes ranking reversals under right-censored scoring procedures. | Specify the interval-censoring/assessment-process distinction and mathematical relation. |
| Lillelund et al. [R180] | Shows evaluation failure under dependent right censoring with known-event-time semi-synthetic design. | Determine whether OF-35 is a direct extension or contains a different identification/assessment problem. |

## 7. Promotion / kill gate

OF-35 may become C011 only if all of the following survive:

1. **Direct nearest-neighbor gate:** no paper already provides the same cross-method map of oracle ranking reversals / wrong-model selection for interval-censored outcomes.
2. **Distinct-mechanism gate:** the contribution is not merely “apply the right-censoring ranking-reversal idea to interval censoring.” The recurrent assessment/inspection process must create a distinct statistical structure or decision problem.
3. **Estimand gate:** wrong-winner probability / selection regret is formally defined and scientifically interpretable.
4. **Design gate:** a small simulation can isolate assessment frequency, informativeness and nuisance misspecification without becoming a sprawling benchmark.
5. **Data gate:** at least one reproducible public/open illustration is adequate, even if the oracle claims remain simulation-based.
6. **Decision gate:** the result changes how an analyst chooses an evaluation estimator, inspection-sensitivity analysis or prediction model.

**Kill OF-35** if a direct equivalent already maps these ranking failures, if the interval-censoring case adds no structure beyond existing right-censoring work, or if conclusions reduce to “more censoring makes estimates noisier.”

## 8. Program consequence

This reconnaissance changes the **search strategy** and current first-project neighborhood, not the Charter.

- Survey-data integration remains valuable program history and a possible future branch, but it is no longer the exclusive active discovery neighborhood.
- C011 remains unassigned.
- OF-35 is the only lead authorized for the next bounded prosecution.
- Synthetic-data inference remains a high-value watchlist but should not displace OF-35 unless its competitive geometry materially changes.
- Meta-analysis content-coverage and generic multiverse-inference formulations should not be revived under new wording.

## 9. Next bounded action

Do **not** start a full simulation study yet.

The next action is a narrow OF-35 prosecution:

1. full-text nearest-neighbor extraction from R182–R185;
2. explicit comparison to right-censoring ranking-reversal ancestors R179–R180;
3. define the oracle-ranking estimand and the exact inspection-process regimes;
4. run only a toy feasibility simulation if needed to determine whether ranking reversals can be nontrivial;
5. promote to C011 only after those four checks survive.
## 10. Subsequent prosecution resolution

The bounded prosecution ordered here is complete in `19_OF35_INTERVAL_CENSORING_RANKING_PROSECUTION.md`. OF-35 did **not** clear the novelty/distinct-mechanism gates and is now **PARKED / NO-GO FOR FIRST PROJECT**.

The decisive new evidence was a 2026 ICML study that directly compares standard censored-data survival-model evaluation with oracle exact-event-time evaluation and measures preservation of model rankings [R189], combined with the realization that Yang et al. already fit three competing interval-censored prediction models and calculate exact-event reference AUC/Brier/EPCE for each [R183]. A second ICML 2026 paper also occupies the theoretical interval-censored scoring/monitoring-assumption frontier [R190].

C011 remains unassigned. The only retained residue is OF-38, a theory-heavy watchlist question about sensitivity of model choice to violations of informative Case-K monitoring assumptions.

---

## Consolidated historical chain — D024 through D026 / OF-39

To respect the ChatGPT Project source ceiling, the three former standalone records `20_D024_CROSS_FIELD_OPPORTUNITY_GENERATION_II.md`, `21_OF39_ADAPTIVE_DIAGNOSTIC_PROSECUTION.md`, and `22_OF39_EXACT_ENUMERATION_THEOREM_GATE.md` are preserved below and retired as separate canonical sources. References to those filenames inside the preserved historical text are archival path labels, not active canonical paths.

### Merged source record — D024 cross-field opportunity generation II

> Historical filename: `20_D024_CROSS_FIELD_OPPORTUNITY_GENERATION_II.md`. This filename is retired from the canonical source set; the preserved record follows.

# D024 Cross-Field Opportunity Generation II

## 1. Purpose

This record executes the review-first cross-field opportunity-generation step authorized after D023 parked OF-35.

The goal is **not** to manufacture C011. It is to search current statistical literatures for a problem that is important, methodologically distinct, feasible at first-project scale, and not already occupied once the underlying **problem sentence / decision target** is searched across adjacent mechanisms.

The strengthened discovery rule from L051 is applied throughout:

1. search the mechanism-specific phrase;
2. rewrite it as an abstract statistical problem sentence;
3. search neighboring mechanisms and disciplines for the same estimand, decision or failure mode;
4. search classical ancestors before interpreting a modern implementation gap as novelty;
5. distinguish a new summary/metric from a genuinely new inferential object;
6. allow the correct output to be **no candidate**.

Search date: 2026-09-08.

## 2. Screening frame

A lead is retained only if it can be stated in terms of a concrete statistical object such as:

- null calibration / Type-I error;
- coverage or confidence-set validity;
- identification region or sharp bound;
- prediction-error estimand under a specified deployment regime;
- model-selection error / regret;
- diagnostic power under a defined alternative;
- a formal robustness/sensitivity parameter.

A lead is downgraded if its proposed contribution is only:

- “apply method A to setting B”;
- a new name for an output already produced by nearest work;
- a larger simulation grid;
- another metric without a new validity result;
- a mechanism-specific restatement of a general theorem;
- a topic whose active-work velocity makes a first project unusually easy to scoop.

## 3. Fields and routes screened

The pass screened more routes than the final opportunity slate. The most important negative screens are recorded because they constrain future searches.

### 3.1 Record-linkage uncertainty in downstream inference — screened out as primary lead

The problem is important, but the competitive geometry is unfavorable. Current work spans linkage-error-aware regression, causal inference, proximal approaches and dedicated 2026 conference activity. This is not an empty interface awaiting a first statistical treatment.

**Disposition:** do not promote a generic “propagate record-linkage uncertainty” project. Reopen only with a sharply different estimand or data regime.

### 3.2 Clinical prediction validation with outcome misclassification — broad correction route screened out

Zou et al. (2026) already develop validation corrections for TPR, FPR, PPV, NPV and AUC using a chart-reviewed gold-standard subset [R202]. They explicitly identify calibration/Brier-type extensions as future work.

A simple extension to decision-curve/net-benefit analysis is not strong enough: net benefit at a threshold is algebraically determined by prevalence, TPR and FPR, so the closest work already contains most required components.

The only potentially distinct residue is **partial identification of probabilistic prediction performance/calibration without a gold standard**, but that residue is threatened by general misclassification partial-identification theory [R203], imperfect-reference diagnostic bounds [R204], and recent weak-supervision performance bounds [R205].

**Disposition:** retain only as a theory-heavy watchlist (OF-41); do not treat “no gold standard” itself as novelty.

### 3.3 Count-time-series diagnostics under underreporting — broad route collapsed

Hudecová's 2026 review establishes goodness-of-fit and structure assessment as a coherent current count-time-series topic [R187]. Initial screening suggested a gap around distinguishing latent-process misspecification from reporting-process distortion.

That broad claim collapses against Wei, Wang & Xia (2024), who show that ordinary serial/cross-dependence tests can be invalid under time-varying underreporting and develop underreporting-robust tests with bootstrap calibration [R206].

A narrower question about **full parametric INAR/INGARCH goodness-of-fit under reporting error** remains distinguishable, but it is now an extension of an existing robustness-testing program rather than a clean first opening.

**Disposition:** OF-42 secondary/parked.

### 3.4 Forecast evaluation with noisy/revised targets — screened out

Older forecast-evaluation work already shows that noisy verification can favor the wrong forecast and develops error-corrected proper scores. Recent measurement-error scoring work extends that logic. The abstract problem sentence “does an imperfectly observed target distort forecast ranking?” is therefore already occupied.

**Disposition:** no opportunity created.

### 3.5 Animal-tracking / multi-resolution behavioral inference — screened but not promoted

A 2026 review and recent GPS/video HMM validation work show that multi-device, temporal-resolution and latent-state interpretation problems are real. However, current domain-specific work already studies state disagreement across resolutions and the area imposes substantial ecological/domain overhead.

**Disposition:** interesting field, poor first-project geometry for this program.

### 3.6 Adaptive paired-comparison estimation — broad bias route collapsed, diagnostic-validity route survives

Hamilton & Tawn (2026) show that adaptive comparative-judgment scheduling can substantially increase bias in Bradley–Terry parameter estimates and, crucially, establish that under an adaptive schedule the observed comparison schedule is **not ancillary**; observed and expected information no longer coincide in the usual way [R195]. They propose a schedule-replaying parametric bootstrap for bias correction.

Therefore the broad claim “adaptive matchmaking/scheduling biases Bradley–Terry ratings” is occupied.

However, Wu, Niezink & Junker (2022) provide a widely applicable Bradley–Terry diagnostic framework—overdispersion tests and object/subject diagnostics—developed under the standard pairwise-comparison formulation [R196]. The bounded search did not find a paper directly establishing the null calibration of these diagnostics when the **pairs themselves are selected adaptively using previous outcomes**.

This creates OF-39 below.

### 3.7 Spatial / multisource data-fusion validation — important but general ancestors are strong

Oduori et al.'s 2026 systematic review of 82 low-cost-sensor data-fusion studies reports unresolved validation standards and generalizability, with random k-fold validation still common and spatial/temporal leakage a recognized risk [R199].

The appealing problem sentence is:

> When multiple sources observe the same latent spatial process, can holding out records while leaving correlated/co-located information from another source in training make deployment performance look too good?

But general correlated-data cross-validation theory already provides suitability criteria and bias corrections [R200], and geospatial CV work develops explicit target-aware spatial validation strategies [R201]. Multisource fusion therefore does not get novelty merely by adding a source label.

A distinct contribution would have to formalize **source-availability deployment estimands** (e.g., same-site/new-source, new-site/same-source, new-site/new-source) and show that common fusion CV schemes estimate the wrong target. That is potentially useful but currently looks closer to a deployment-taxonomy/validation-design paper than a new statistical method.

**Disposition:** OF-40 watchlist/empirical-methodological; not priority prosecution.

### 3.8 Extreme conditional quantiles with covariate measurement error — technically plausible, first-project unfavorable

The 2026 Annual Review documents rapid modern development in conditional extreme-quantile analysis [R207]. Classical and semiparametric quantile-regression methodology already treats covariate measurement error [R208–R209].

The exact intersection—tail extrapolation for extreme conditional quantiles under classical covariate measurement error—did not surface as a direct occupied result in the bounded search. But the likely contribution is asymptotic/identification-heavy and would require simultaneously extending two technically mature literatures.

**Disposition:** OF-43 theory-heavy watchlist, not first prosecution.

## 4. Opportunity slate

### OF-39 — Calibration of Bradley–Terry diagnostics under outcome-adaptive comparison scheduling

**Status:** PRIORITY PROSECUTION LEAD — NOT C011  
**Priority:** HIGH

#### Problem sentence

> If the next pair to compare is chosen using previous comparison outcomes, do standard Bradley–Terry lack-of-fit and overdispersion diagnostics still have their advertised null distributions when the Bradley–Terry model is actually true?

#### Mechanism

Let the history before round `t` be `H_{t-1}` and let the pair selected at round `t` be

`A_t = g_t(H_{t-1}, U_t)`,

where `g_t` is an adaptive scheduling rule (e.g., Swiss/near-strength matching) and `U_t` denotes any randomization used by the scheduler.

Given pair `A_t=(i,j)`, the Bradley–Terry null specifies

`P(Y_t = 1 | A_t=(i,j), H_{t-1}) = logistic(beta_i - beta_j)`.

Under a fixed/random schedule independent of previous outcomes, existing diagnostic reference calculations treat the comparison structure as given. Under an adaptive schedule, Hamilton & Tawn show that the realized schedule is not ancillary [R195]. The question is whether that endogeneity changes the null law of diagnostic statistics used in the Wu et al. framework [R196].

#### Primary estimand / validity target

For a diagnostic p-value `p_naive`, define null calibration error at nominal level `alpha`:

`Delta(alpha) = P_beta(p_naive <= alpha) - alpha`,

where probability integrates over both comparison outcomes and the adaptive schedule generated from them.

The basic failure target is **Type-I error distortion under a correctly specified Bradley–Terry model**.

Secondary targets:

- distributional distortion of object-residual diagnostics;
- false lack-of-fit rates versus number of rounds/items/adaptivity;
- power under genuine misspecification after valid calibration;
- rank/reliability consequences of false diagnostic rejection.

#### Candidate correction

A schedule-replay parametric bootstrap would simulate the **entire adaptive experiment**, not hold the final realized graph fixed:

1. fit the Bradley–Terry model;
2. preserve only genuinely ancillary initialization (e.g., first randomized round);
3. simulate outcomes under fitted Bradley–Terry strengths;
4. rerun the same adaptive scheduling algorithm after each simulated round;
5. refit the model and recompute the diagnostic statistic;
6. use the joint schedule+outcome bootstrap distribution for calibration.

Hamilton & Tawn already use this replay principle for bias correction [R195]. Therefore “use a parametric bootstrap” alone is **not** the contribution. A viable contribution requires showing which diagnostics fail, why, and under what conditions the replayed procedure restores valid inference.

#### Direct prior-art threats

1. **Hamilton & Tawn 2026 [R195]** — direct adaptive Bradley–Terry estimation neighbor; establishes non-ancillarity and already uses schedule-replay bootstrap.
2. **Wu, Niezink & Junker 2022 [R196]** — direct diagnostic-method neighbor; supplies the diagnostics to test.
3. **Yi & Wang 2007 [R197]** — important abstract ancestor: goodness-of-fit testing under response-adaptive clinical-trial allocation already exists. This means the generic principle “adaptive data collection changes GOF inference” is not new.
4. **Gao, Shen & Zhang 2023 [R198]** — modern Bradley–Terry uncertainty-quantification theory under random comparison graphs; constrains any broad UQ claim.

#### Why it still survives generation

The surviving object is more specific than the generic ancestor: the random **comparison graph itself is generated sequentially from previous pair outcomes**, and the proposed target is the calibration of an established Bradley–Terry diagnostic framework. The bounded search found no direct paper proving validity or invalidity of those diagnostics under such scheduling.

This is enough for **prosecution**, not enough for candidate promotion.

#### Feasibility

- Hamilton & Tawn provide an explicit Swiss-style adaptive simulation design [R195].
- Wu et al. provide reproducible diagnostic code [R196].
- A 2025 meta-analysis assembled 101 comparative-judgment sessions with open materials/code and records whether adaptivity was used; this provides a possible empirical substrate [R210].
- The CJ RAVE 2026 dataset supplies an additional open contemporary pairwise-comparison dataset, though its scheduling mechanism must be checked before use [R211].
- Simulation is laptop/workstation scale: dozens/hundreds of objects, rounds and bootstrap replicates rather than deep-learning training.

#### Kill criteria

Kill OF-39 if any of the following occurs:

1. a direct adaptive-paired-comparison paper already establishes the null law/calibration of the Wu diagnostics;
2. standard diagnostics are conditionally or asymptotically valid under predictable/adaptive scheduling, leaving no material failure;
3. Yi & Wang's response-adaptive GOF theory directly subsumes the relevant Bradley–Terry diagnostics with no nontrivial adaptation;
4. replay bootstrap is a mechanically obvious implementation with no theorem, no meaningful calibration failure and no new diagnostic insight;
5. realistic levels of adaptivity produce negligible Type-I distortion;
6. the only result is “more adaptive schedules change p-values,” without a principled validity result.

#### Promotion criteria

Promote toward C011 only if prosecution establishes **all** of:

1. a clearly non-negligible null-calibration failure for at least one widely used diagnostic under realistic adaptive schedules;
2. a mathematical explanation tied to the adaptive comparison graph/non-ancillarity rather than generic finite-sample noise;
3. a correction or reference procedure with justified validity (theorem, conditional argument or strong asymptotic/bootstrap result);
4. diagnostic power remains useful after calibration;
5. current literature contains no direct equivalent;
6. a reproducible simulation and at least one plausible empirical illustration are available.

---

### OF-40 — Source-aware deployment validation for multisource spatial data fusion

**Status:** WATCHLIST / EMPIRICAL-METHODOLOGICAL  
**Priority:** MEDIUM

#### Problem sentence

> In multisource spatial fusion, which deployment error is a CV procedure actually estimating when correlated/co-located information from a different source remains in the training set?

Potential deployment regimes:

- new records at already-covered sites/sources;
- new sites with existing source types;
- an existing site when one source is unavailable;
- entirely new sites and new source availability patterns.

#### Threats

R199 documents validation/generalizability gaps in current low-cost-sensor fusion practice, but R200–R201 already provide general correlated/geospatial CV theory. The gap cannot be “spatial leakage exists.”

#### Reopen condition

Only prosecute if a precise **source-availability estimand** can be shown not to reduce to existing correlated/geospatial CV target definitions and if real public multisource data permit side-by-side deployment validation.

---

### OF-41 — Partial identification of probabilistic prediction performance under outcome misclassification without a gold standard

**Status:** WATCHLIST / THEORY-HEAVY  
**Priority:** MEDIUM

#### Problem sentence

> If binary validation outcomes are misclassified and sensitivity/specificity are not point known, what can be sharply learned about probabilistic prediction performance and calibration?

Possible targets include:

- true Brier score;
- calibration-in-the-large;
- calibration slope/intercept;
- calibration curve bands;
- pairwise model ordering under bounded misclassification.

#### Threats

Zou et al. already correct major validation metrics using chart-review data [R202]. Molinari's general misclassification framework can derive identification regions for broad distributional functionals [R203]. Obradović's 2024 imperfect-reference work derives sharp bounds for diagnostic sensitivity/specificity and related policy quantities [R204]. NeurIPS 2024 work already frames no-ground-truth model evaluation as partial identification [R205]. Semi-supervised model evaluation can estimate metrics including calibration error using unlabeled data under modeling assumptions [R212].

#### Reopen condition

A viable contribution needs a genuinely new **sharp closed-form/optimization result for continuous risk-score functionals**, useful sensitivity geometry, and inference for the identified set—not merely applying Molinari's framework to Brier score.

---

### OF-42 — Full parametric goodness-of-fit for count time series under time-varying underreporting

**Status:** PARKED / SECONDARY  
**Priority:** LOW–MEDIUM

#### Problem sentence

> Can an analyst distinguish latent INAR/INGARCH misspecification from a time-varying observation/reporting process when using model diagnostics?

#### Threats

R187 establishes mature count-time-series GOF methodology. R206 directly shows underreporting can invalidate dependence tests and develops robust bootstrap tests. The broad failure principle is therefore occupied.

#### Reopen condition

Only with a specific parametric GOF statistic whose null distribution under underreporting requires new theory and whose behavior is not a direct extension of R206.

---

### OF-43 — Extreme conditional quantiles with covariate measurement error

**Status:** WATCHLIST / THEORY-HEAVY  
**Priority:** LOW–MEDIUM

#### Problem sentence

> How does classical covariate measurement error propagate into tail extrapolation for conditional extreme quantiles, and when can the extreme conditional quantile be identified/estimated reliably?

#### Threats

Conditional extreme-quantile methods are moving rapidly [R207], while ordinary quantile regression with measurement error has a mature methodological foundation [R208–R209]. The exact intersection may be less developed, but a meaningful contribution likely requires substantial new asymptotic theory and possibly deconvolution/replicate/instrument structure.

#### Reopen condition

Only if a tractable special case yields a clean theorem and simulation design suitable for first-project scale, or if a collaborator with extreme-value/measurement-error expertise joins.

## 5. Comparative ranking

| Lead | Importance | Distinctness after adjacent search | Feasibility | Competition / scoop risk | First-project fit | D024 disposition |
|---|---|---|---|---|---|---|
| OF-39 adaptive Bradley–Terry diagnostic calibration | High | **Moderate; unresolved but ancestor-threatened** | **High** | Moderate-high | **Best** | **PRIORITY PROSECUTION** |
| OF-40 source-aware spatial-fusion validation | High | Low-moderate | High | High/general ancestor | Moderate | WATCHLIST |
| OF-41 partial-ID probabilistic validation under misclassification | Very high | Moderate but heavily ancestor-threatened | Moderate | High | Low-moderate | THEORY WATCHLIST |
| OF-42 count GOF under underreporting | High | Low-moderate | High | Moderate | Moderate | PARKED/SECONDARY |
| OF-43 extreme quantiles × measurement error | High | Moderate | Low-moderate | High | Low | THEORY WATCHLIST |

## 6. D024 decision

**OF-39 is the sole priority prosecution lead.**

This does **not** assign C011.

The reason for selecting OF-39 for prosecution is not that it has the strongest novelty claim—it does not yet. It has the best combination of:

- a precise null-validity target;
- direct methodological importance;
- two current literatures that expose the seam (adaptive estimation and model diagnostics);
- modest computation;
- reproducible code/data substrates;
- clear kill criteria;
- and a bounded path to a decisive answer.

The principal novelty threat is already known: response-adaptive GOF testing is an older statistical ancestor [R197]. Therefore prosecution must ask whether the **adaptive paired-comparison graph** creates a genuinely distinct diagnostic problem, not merely whether a bootstrap can be attached to an existing test.

## 7. Next bounded prosecution plan for OF-39

The next step should be a compact four-part prosecution:

### P1 — Diagnostic-law audit

Reconstruct the exact null reference distributions/approximations used by Wu et al. for:

- overdispersion;
- object residuals / object-level diagnostics;
- subject diagnostics where applicable.

Determine which derivations condition on a comparison graph/design that is independent/ancillary and which may remain valid under predictable designs.

### P2 — General-ancestor audit

Read Yi & Wang (2007) and adjacent response-adaptive GOF/inference work closely enough to determine whether it already supplies a theorem that transfers directly to paired comparisons.

If yes, kill or narrow immediately.

### P3 — Minimal null simulation

Only if P1–P2 leave a real seam:

- simulate under the exact Bradley–Terry null;
- compare random, Swiss, and one stronger outcome-adaptive schedule;
- evaluate empirical Type-I error for nominal 0.01/0.05/0.10;
- vary number of objects, rounds and strength dispersion;
- hold the diagnostic model correctly specified.

The first question is existence/magnitude of **false lack-of-fit**, not power.

### P4 — Replay calibration

If naive diagnostics fail materially:

- test joint schedule+outcome parametric bootstrap calibration;
- compare against a graph-conditioned bootstrap to isolate the role of schedule endogeneity;
- only then consider power and a theorem/validity argument.

## 8. Anti-claims after D024

Do **not** claim any of the following are untouched:

- adaptive paired-comparison bias;
- Bradley–Terry diagnostics in general;
- goodness-of-fit under adaptive experimental allocation in general;
- spatial leakage in cross-validation;
- correlated-data CV bias;
- outcome-misclassification bias in prediction validation;
- partial identification of classifier performance without ground truth in general;
- underreporting-induced distortion of time-series dependence tests;
- quantile-regression measurement-error correction;
- conditional extreme-quantile methodology generally.

## 9. Program consequence

D024 improves the program's opportunity-search protocol in two ways.

First, it shows that **review-first search can still produce a prosecution-worthy lead after repeated collapses**, but only after abstract neighboring-mechanism searches eliminate superficially attractive variants.

Second, it suggests a useful new discovery pattern:

> **When data collection is adaptive, estimation may be corrected before model checking is.**

This pattern is not itself a novelty claim. It is a search heuristic: whenever current work shows that a design is non-ancillary or outcome-dependent and has already repaired estimation, separately inspect the validity of downstream diagnostics, uncertainty statements and model-selection procedures.

C011 remains unassigned. No execution project is authorized until OF-39 survives its bounded prosecution.


### Merged source record — D025 OF-39 adaptive diagnostic prosecution

> Historical filename: `21_OF39_ADAPTIVE_DIAGNOSTIC_PROSECUTION.md`. This filename is retired from the canonical source set; the preserved record follows.

# OF-39 — Adaptive Bradley–Terry diagnostic prosecution

## 1. Prosecution question

OF-39 entered prosecution with the claim:

> If the next pair to compare is chosen using previous comparison outcomes, do standard Bradley–Terry lack-of-fit and overdispersion diagnostics retain their advertised null behavior when the Bradley–Terry outcome model itself is correct?

The prosecution deliberately separates four issues that can otherwise be conflated:

1. **outcome-model correctness** — whether the Bradley–Terry conditional probability model is true;
2. **graph sparsity/topology** — whether many pair cells have small counts even under a nonadaptive design;
3. **outcome–schedule endogeneity** — whether the realized comparison graph depends on prior outcomes;
4. **estimation/penalization** — whether finite or bias-reduced score estimates are used before diagnostics.

The result is narrower than the original opportunity statement but does not collapse it.

## 2. Verdict

**Status:** **SURVIVES BOUNDED PROSECUTION — NARROWED / HOLD BEFORE C011**

**C011 remains unassigned. No execution project is authorized.**

The broad claim that adaptive scheduling generically destroys Bradley–Terry diagnostic asymptotics is **not supported**. However, the prosecution found a specific finite-sample calibration problem: conditioning or resampling as though the final adaptive comparison graph were ancillary can target the wrong null distribution. A scheduler-replay bootstrap can materially improve calibration in the tested regimes.

This is enough to preserve OF-39 as the strongest live lead, but not enough to promote it. The remaining contribution must be a principled finite-sample/conditional-calibration result, not merely a simulation paper or a transfer of Hamilton & Tawn's replay bootstrap.

## 3. Gate P1 — audit of the Wu et al. diagnostic law

Wu, Niezink & Junker [R196] write the standard Bradley–Terry analysis in grouped-pair form: for a fixed comparison count `V_ij`, the win count `W_ij` is treated as

`W_ij ~ Bin(V_ij, p_ij)`,  with  `p_ij = logistic(beta_i - beta_j)`.

Their pair Pearson residual is

`R_ij = (W_ij - V_ij p_hat_ij) / sqrt(V_ij p_hat_ij (1-p_hat_ij))`,

and their object residual combines the pair residuals. They explicitly note that the asymptotic normal approximation for `R_ij` requires the relevant `V_ij` to grow.

### What changes under adaptive scheduling

Let `I_t(ij)` indicate that pair `(i,j)` is scheduled at round/time `t`, with `I_t(ij)` measurable from the previous history. Under a correctly specified Bradley–Terry model,

`E[Y_t - p_ij | H_{t-1}, I_t(ij)=1] = 0`.

Therefore

`M_ij(T) = sum_t I_t(ij) (Y_t - p_ij)`

is a martingale sum with predictable quadratic variation

`<M_ij>_T = p_ij(1-p_ij) sum_t I_t(ij) = p_ij(1-p_ij) V_ij`.

This matters. It means outcome-adaptive scheduling does **not** automatically destroy asymptotic normality: under adequate exploration/repetition and regularity, martingale central-limit arguments can recover the same standardized limit. Yi & Wang's response-adaptive likelihood results [R197] and modern adaptive-data inference [R215] reinforce that broad conclusion.

### But the fixed-final-graph binomial statement is no longer generally valid

Hamilton & Tawn show that the final adaptive schedule is non-ancillary [R195]. Conditioning on the complete realized `V` therefore reveals information about previous outcomes. In general,

`Law(W_ij | final V_ij)`

need not equal the ordinary binomial law used when `V_ij` is fixed independently of outcomes.

This produces the first important refinement:

> **Sequential martingale validity and fixed-final-design conditional validity are different objects.**

The prosecution therefore rejects the broad asymptotic-failure claim but retains a finite-sample conditional-calibration seam.

## 4. Gate P2 — adjacent adaptive-design theory

The nearest abstract ancestor remains Yi & Wang [R197], who establish asymptotic likelihood-ratio and MLE results for a wide class of response-adaptive clinical-trial designs. Their result prevents any claim that “adaptive allocation makes ordinary GOF impossible.”

Additional pressure comes from:

- Glickman & Jensen [R213], who developed adaptive paired-comparison design directly for Bradley–Terry-style tournaments;
- Farrington [R214], who shows that Pearson GOF itself needs special treatment in sparse GLM settings, independently of adaptivity;
- Lin, Khamaru & Wainwright [R215], who show that adaptive data collection can change standard estimator asymptotics and formulate explicit exploration conditions in generalized regression settings;
- Deshpande et al. [R216], who provide another general demonstration that adaptive collection can create persistent inferential distortions and motivate martingale-based corrections.

**Gate result:** Yi & Wang does not directly subsume the Wu object/overdispersion diagnostics on an outcome-generated paired-comparison graph, but the general martingale/adaptive-inference literature prevents a broad novelty claim. OF-39 survives only as a specific diagnostic-calibration problem.

## 5. Gate P3 — minimal null-calibration experiments

These simulations are exploratory prosecution tools, not paper-ready evidence. They were used only after the theory audit left a live seam.

### 5.1 Hamilton-like sparse regime

Configuration:

- `n = 100` items;
- `16` rounds, one comparison per item per round;
- deterministic normal-quantile strengths with mean 0 and SD 2, matching Hamilton & Tawn's main simulation scale [R195];
- Swiss scheduling: first round random, later rounds pair items with similar cumulative wins;
- `alpha = 0.3` adjustment for stable fitting, following the adaptive-schedule recommendation studied by Hamilton & Tawn;
- `200` outer simulations.

Three designs were compared:

1. **Random:** every round randomly paired;
2. **Frozen Swiss graph:** generate a Swiss graph from one outcome path, then regenerate fresh independent Bradley–Terry outcomes on that exact graph;
3. **Adaptive Swiss:** outcomes actively determine later pairings.

Using a grouped Pearson statistic with the usual fixed-design chi-square reference, empirical 5% rejection was approximately:

| Design | Rejection rate |
|---|---:|
| Random | 1.0% |
| Frozen Swiss graph | 2.5% |
| Adaptive Swiss | 12.5% |

The absolute rates should **not** be read as a validated test comparison because the setting is extremely sparse and uses penalized estimation; Farrington-type sparse-GOF effects [R214] are a major confound. The useful contrast is adaptive versus frozen: the graph is identical in topology/counts, but the adaptive version retains the outcome–schedule dependence and produces materially different tails.

This is evidence that endogeneity is not reducible to graph sparsity alone.

### 5.2 Repeated-comparison regime: freeze versus replay bootstrap

A smaller regime was used to test calibration without the most extreme sparsity:

- `n = 10`;
- `60` rounds;
- normal-quantile strengths with SD 1;
- Swiss adaptive scheduling;
- `alpha = 0.3` fitting;
- `200` outer null simulations;
- `50` bootstrap replicates per outer simulation.

Two null calibrations were compared:

- **Frozen-schedule bootstrap:** hold the full realized adaptive pair sequence fixed and regenerate outcomes;
- **Scheduler-replay bootstrap:** preserve the first-round ancillary pairing, regenerate outcomes, and rerun the Swiss rule after every round.

Empirical rejection:

| Nominal level | Frozen schedule | Scheduler replay |
|---|---:|---:|
| 5% | 3.5% | 4.5% |
| 10% | 6.5% | 10.5% |

Median bootstrap p-value was approximately `0.588` for the frozen procedure and `0.471` for replay.

The replay procedure is close to nominal in this bounded experiment; freezing the final adaptive schedule is systematically conservative.

### Why the two bootstraps differ

A frozen bootstrap simulates

`Y* ~ product Bernoulli(p_hat | observed final schedule)`

as if the final schedule were ancillary. But under outcome-adaptive scheduling the actual conditional law

`Law(Y | final schedule)`

includes the selection constraint that those outcomes helped produce that schedule. The frozen bootstrap therefore does not reproduce the true conditional experiment. Replaying the scheduler instead approximates the **joint** outcome-plus-design law that generated the statistic.

That is the central surviving mechanism.

## 6. Gate P4 — power check

A calibrated test is not useful if adaptive scheduling removes all diagnostic power. Two deliberately different departures were therefore tried in the repeated-comparison regime.

### Global nonlinear response departure

Replacing the Bradley–Terry logit difference `d` by `d^3` produced very low power for the replay-calibrated Pearson statistic (about 3% at a nominal 5% level in the bounded experiment).

This is informative rather than merely disappointing: a Swiss scheduler concentrates comparisons among similarly performing items, where a global nonlinear response function can be difficult to distinguish from a rescaled Bradley–Terry model.

### Local cyclic departure

A three-item rock–paper–scissors-type perturbation among middle-strength items produced nontrivial but still moderate replay-calibrated power:

- cycle shift `gamma = 1.5`: about 15% power at 5%;
- cycle shift `gamma = 3.0`: about 38% power at 5% and 72% at 10%.

Thus the diagnostic is not powerless, but adaptive scheduling can strongly reshape **which misspecifications are detectable**.

This creates a second possible contribution axis—diagnostic-power geometry under an information-seeking scheduler—but that axis is not yet prosecuted against optimal-design/model-discrimination literature and must not be claimed as novel.

## 7. Promotion-gate audit

| Criterion | Result |
|---|---|
| Non-negligible calibration effect under realistic adaptivity | **PARTIAL PASS** — adaptive versus frozen differences are material, but ordinary sparse chi-square calibration is itself imperfect |
| Mechanistic explanation specific to endogenous comparison graph | **PASS at conceptual level** — final schedule is non-ancillary; frozen resampling targets the wrong conditional experiment |
| Justified correction/reference procedure | **PARTIAL / NOT YET** — scheduler replay works empirically, but the replay principle is already Hamilton & Tawn prior art and no new validity theorem has been proved |
| Useful power after calibration | **MIXED** — detectable cyclic departures, weak power for a global nonlinear departure under Swiss matching |
| No direct equivalent in current literature | **PROVISIONAL PASS** — bounded searches found adaptive estimation, adaptive GOF ancestors and general adaptive inference, but no direct Wu-diagnostic calibration paper |
| Reproducible simulation + plausible empirical illustration | **SIMULATION PASS / EMPIRICAL OPEN** — simulation is straightforward; real-data use requires a dataset with sufficiently specified adaptive scheduling |

Because every criterion is not yet satisfied, **do not assign C011**.

## 8. Refined OF-39 statement

The surviving problem is now:

> **How should Bradley–Terry model diagnostics be calibrated when the comparison graph is generated outcome-adaptively, and what is lost by conditioning on or resampling the final graph as though it were ancillary?**

The strongest possible contribution would combine:

1. a finite-sample or asymptotic distinction between joint adaptive calibration and fixed-final-graph calibration;
2. a theorem/validity result for a replay or martingale-based reference law;
3. explicit separation of adaptive endogeneity from sparse-cell GOF distortion;
4. power characterization showing which model departures an information-seeking scheduler makes hard to detect;
5. an empirical illustration with a fully documented scheduler.

## 9. Next bounded action

Do **not** broaden the field again yet. The next action is a short theory gate:

1. construct the smallest exact adaptive Bradley–Terry experiment (e.g. 4–6 objects and a few rounds) where all outcome paths can be enumerated;
2. derive the exact `Law(W,V)` and show explicitly how `Law(W|V)` differs from the fixed-design binomial law;
3. compare exact fixed-graph and replay reference distributions for one diagnostic statistic;
4. determine whether this yields a nontrivial proposition beyond Hamilton & Tawn's estimation result and Yi & Wang's generic adaptive-GOF theory;
5. only then decide whether OF-39 becomes C011 or is parked.

This exact-enumeration theorem gate is cheaper and more decisive than expanding simulation grids.

## 10. Evidence used

Primary anchors: [R195–R197, R213–R216]. The D024 generation context remains in `20_D024_CROSS_FIELD_OPPORTUNITY_GENERATION_II.md`.

## 11. Exact-enumeration theorem gate closure

The required next gate has now been executed in `22_OF39_EXACT_ENUMERATION_THEOREM_GATE.md`.

A four-object, two-round Swiss-style experiment was enumerated exactly. The final graph imposes outcome-path compatibility constraints, so the true `Law(Y | final graph)` is a truncated product law rather than the ordinary frozen-design Bernoulli product law. For an oracle Pearson residual sum using the true Bradley–Terry probabilities, the exact conditional diagnostic laws differ materially; at nominal `alpha=0.10`, frozen-final-graph exact calibration rejects with probability `17/144`, while exact scheduler replay rejects with probability `23/240`.

This proves the finite-sample mechanism while eliminating sparse-cell chi-square approximation and parameter-estimation confounding.

The novelty gate nevertheless fails. Hamilton & Tawn [R195] already establish the non-ancillarity of the adaptive schedule and the need to replay the scheduler while conditioning only on ancillary scheduling components. The exact truncation formula is a direct finite-state consequence of that principle, and exact replay validity with known parameters is generic rather than Bradley–Terry-specific. Yi & Wang [R197] further prevents a broad adaptive-GOF novelty claim.

**Final disposition:** **PARK OF-39 / MECHANISM ESTABLISHED, DISTINCT CONTRIBUTION NOT ESTABLISHED.**

**C011 remains unassigned. No execution project is authorized.**

Do not expand the OF-39 simulation grid. Reopen only if a statistic-specific fitted-parameter theorem, a new computable calibration target when scheduler replay is unavailable, a nontrivial design-versus-diagnostic-power theorem, or a uniquely informative documented adaptive system survives direct prosecution.


### Merged source record — D026 OF-39 exact-enumeration/theorem gate

> Historical filename: `22_OF39_EXACT_ENUMERATION_THEOREM_GATE.md`. This filename is retired from the canonical source set; the preserved record follows.

# OF-39 — Exact-enumeration / theorem gate

## 1. Gate question

D025 left one bounded question before any C011 promotion:

> Can a smallest fully enumerated adaptive Bradley–Terry experiment yield a nontrivial diagnostic-calibration proposition that is genuinely distinct from Hamilton & Tawn's adaptive-schedule estimation result [R195] and generic response-adaptive goodness-of-fit theory [R197]?

This gate is intentionally exact. It does not use Monte Carlo, asymptotic chi-square calibration, or estimated Bradley–Terry parameters.

## 2. Verdict

**Status:** **PHENOMENON PROVED / NOVELTY GATE FAILS — PARK OF-39**

**C011 remains unassigned. No execution project is authorized.**

The exact enumeration proves a strong finite-sample fact: once later pairings are functions of earlier outcomes, conditioning on the completed comparison graph can truncate the null outcome space. A frozen-final-graph reference can therefore differ from the true conditional law even when the Bradley–Terry model is exactly correct, the parameters are known, and the diagnostic reference is computed exactly.

However, the theorem-level mechanism is not sufficiently distinct for candidate promotion. Hamilton & Tawn already establish that the completed adaptive schedule is non-ancillary and that an adaptive bootstrap must replay the scheduler while conditioning only on genuinely ancillary scheduling components [R195]. The exact conditional-law formula below is a direct finite-state consequence of that fact. Exact replay validity with known parameters is also a generic identical-experiment/exact-test result, while Yi & Wang already establish that goodness-of-fit under response-adaptive designs is a classical inferential problem [R197].

The gate therefore establishes the phenomenon but **collapses the contribution claim**.

## 3. Smallest exact adaptive experiment used

Use four objects with Bradley–Terry merits

`theta = (theta_1, theta_2, theta_3, theta_4) = (3, 1, 2, 1)`.

For pair `(i,j)` with `i < j`,

`P(i beats j) = theta_i / (theta_i + theta_j)`.

The required probabilities are therefore

| Pair | Null win probability for lower-index object |
|---|---:|
| `(1,2)` | `3/4` |
| `(3,4)` | `2/3` |
| `(1,3)` | `3/5` |
| `(2,4)` | `1/2` |
| `(1,4)` | `3/4` |
| `(2,3)` | `1/3` |

### Scheduler

Round 1 is fixed and ancillary:

- `(1,2)`;
- `(3,4)`.

Round 2 is deterministic Swiss-style adaptation:

- the two round-1 winners play each other;
- the two round-1 losers play each other.

Let `Y12=1` mean object 1 beats 2 and `Y34=1` mean object 3 beats 4.

There are only two possible completed graphs:

- `G_A = {(1,2),(3,4),(1,3),(2,4)}` if `Y12 = Y34`;
- `G_B = {(1,2),(3,4),(1,4),(2,3)}` if `Y12 != Y34`.

Thus the final graph is an outcome-generated random variable.

## 4. Exact joint law and conditional-law failure

The first-round joint probabilities are

| `(Y12,Y34)` | Probability | Final graph |
|---|---:|---|
| `(0,0)` | `1/12` | `G_A` |
| `(0,1)` | `1/6` | `G_B` |
| `(1,0)` | `1/4` | `G_B` |
| `(1,1)` | `1/2` | `G_A` |

Hence

`P(G_A)=7/12`, and `P(G_B)=5/12`.

Conditioning on the **adaptive** final graph gives

| Conditional law | Nonzero states |
|---|---|
| `Law(Y12,Y34 | G_A)` | `(0,0): 1/7`, `(1,1): 6/7` |
| `Law(Y12,Y34 | G_B)` | `(0,1): 2/5`, `(1,0): 3/5` |

A frozen-graph analysis instead regenerates the two round-1 outcomes independently with their original Bradley–Terry probabilities, assigning

- `(0,0): 1/12`;
- `(0,1): 1/6`;
- `(1,0): 1/4`;
- `(1,1): 1/2`;

even after the final graph has been fixed.

The discrepancy is therefore not just a changed probability: the true conditional law and the frozen law have different support. For example, under `G_A`, the frozen law assigns positive mass to `(0,1)` and `(1,0)`, although those outcomes could not have produced `G_A`.

For the complete outcome-path law, the total-variation distance between the true conditional law and the frozen law is exactly

- `5/12` for `G_A`;
- `7/12` for `G_B`.

## 5. General finite-state proposition

### Proposition 1 — adaptive final-design conditioning is a truncated product law

Fix the ancillary randomization seed or initial schedule. Let an adaptive scheduler choose comparison `I_t` at time `t` as a deterministic function of the past outcome history `Y_<t`, and let the completed schedule be `V=v(Y)`.

For a realized schedule `v=(i_1,...,i_T)`, define the compatibility set

`C(v) = { y in {0,1}^T : replaying the scheduler on y produces v }`.

Under a correctly specified Bradley–Terry model with known parameter `beta`, let

`L_v(y; beta) = product_t p_{i_t}(beta)^{y_t} [1-p_{i_t}(beta)]^{1-y_t}`.

Then

`P_beta(Y=y | V=v) = 1{y in C(v)} L_v(y;beta) / P_beta(V=v)`.

The frozen-final-design reference is instead

`P_beta^F(Y=y | v) = L_v(y;beta)`

on every binary outcome vector on the fixed schedule.

Therefore the two laws are equal only when the scheduler-compatibility restriction is null for the relevant experiment/statistic. In particular, if `C(v)` is a strict subset with positive frozen probability outside it, frozen-final-design conditioning is invalid.

### Proof

Under sequential Bradley–Terry sampling, the joint probability of any outcome path is the product of its conditional Bernoulli probabilities along the comparisons selected by the scheduler. Conditional on observing completed schedule `v`, only outcome paths that would replay to `v` remain possible. Bayes' rule therefore restricts the product likelihood to `C(v)` and renormalizes by `P_beta(V=v)`. A frozen design omits this compatibility indicator, so equality fails whenever the omitted region has positive probability. `□`

### Interpretation

This proposition cleanly separates two statements that can otherwise be confused:

1. the sequential residual/score increment can still be a martingale difference under the null;
2. the completed adaptive schedule can nevertheless be non-ancillary, so the law conditional on that completed schedule is not the ordinary fixed-design product law.

The proposition is exact and finite-sample; no sparse-cell asymptotics are involved.

## 6. Exact diagnostic-reference comparison

To avoid parameter-estimation and chi-square confounding, use the **oracle Pearson residual sum**

`Q = sum_{(i,j): V_ij=1} (Y_ij - p_ij)^2 / [p_ij(1-p_ij)]`,

where the true Bradley–Terry probabilities are used.

This is the known-parameter analogue of summing squared pair Pearson residuals from the diagnostic framework of Wu et al. [R196]. If frozen-final-graph calibration fails here, estimation or asymptotic approximation cannot be the cause.

### Conditional on `G_A`

| `Q` | True adaptive `P(Q | G_A)` | Frozen-graph `P_F(Q | G_A)` |
|---:|---:|---:|
| `5/2` | `18/35` | `3/10` |
| `10/3` | `12/35` | `1/5` |
| `4` | `0` | `3/20` |
| `29/6` | `0` | `1/10` |
| `31/6` | `0` | `1/10` |
| `6` | `0` | `1/15` |
| `20/3` | `3/35` | `1/20` |
| `15/2` | `2/35` | `1/30` |

The total-variation distance between these two **diagnostic-statistic** laws is exactly `5/12`.

### Conditional on `G_B`

| `Q` | True adaptive `P(Q | G_B)` | Frozen-graph `P_F(Q | G_B)` |
|---:|---:|---:|
| `5/3` | `0` | `1/4` |
| `19/6` | `3/10` | `1/4` |
| `13/3` | `1/5` | `1/6` |
| `14/3` | `3/20` | `1/16` |
| `35/6` | `1/5` | `1/6` |
| `7` | `1/15` | `1/36` |
| `22/3` | `1/20` | `1/24` |
| `17/2` | `1/30` | `1/36` |
| `10` | `0` | `1/144` |

The total-variation distance between these two diagnostic-statistic laws is `37/144`.

### Exact joint replay law

Replaying the scheduler from the ancillary first-round design produces the exact joint null reference

| `Q` | Replay probability |
|---:|---:|
| `5/2` | `3/10` |
| `19/6` | `1/8` |
| `10/3` | `1/5` |
| `13/3` | `1/12` |
| `14/3` | `1/16` |
| `35/6` | `1/12` |
| `20/3` | `1/20` |
| `7` | `1/36` |
| `22/3` | `1/48` |
| `15/2` | `1/30` |
| `17/2` | `1/72` |

Using ordinary upper-tail exact p-values under the true adaptive null:

- frozen-final-graph calibration rejects with probability `17/144 = 0.118055...` at nominal `alpha=0.10`;
- exact scheduler replay rejects with probability `23/240 = 0.095833...` at nominal `alpha=0.10`.

The replay test is slightly conservative because the statistic is discrete. The frozen procedure is anti-conservative at this nominal level.

This is an exact finite-sample calibration failure: no Monte Carlo error, no fitted-parameter error, and no chi-square approximation are present.

## 7. Full 16-path enumeration

Every possible path is listed below. `z` gives round-2 outcomes in the edge order shown.

| `Y12` | `Y34` | Graph | Round-2 edges | `z` | Exact path probability | `Q` |
|---:|---:|---|---|---|---:|---:|
| 0 | 0 | `G_A` | `(1,3),(2,4)` | `0,0` | `1/60` | `15/2` |
| 0 | 0 | `G_A` | `(1,3),(2,4)` | `1,0` | `1/40` | `20/3` |
| 0 | 0 | `G_A` | `(1,3),(2,4)` | `0,1` | `1/60` | `15/2` |
| 0 | 0 | `G_A` | `(1,3),(2,4)` | `1,1` | `1/40` | `20/3` |
| 0 | 1 | `G_B` | `(1,4),(2,3)` | `0,0` | `1/36` | `7` |
| 0 | 1 | `G_B` | `(1,4),(2,3)` | `1,0` | `1/12` | `13/3` |
| 0 | 1 | `G_B` | `(1,4),(2,3)` | `0,1` | `1/72` | `17/2` |
| 0 | 1 | `G_B` | `(1,4),(2,3)` | `1,1` | `1/24` | `35/6` |
| 1 | 0 | `G_B` | `(1,4),(2,3)` | `0,0` | `1/24` | `35/6` |
| 1 | 0 | `G_B` | `(1,4),(2,3)` | `0,1` | `1/48` | `22/3` |
| 1 | 0 | `G_B` | `(1,4),(2,3)` | `1,0` | `1/8` | `19/6` |
| 1 | 0 | `G_B` | `(1,4),(2,3)` | `1,1` | `1/16` | `14/3` |
| 1 | 1 | `G_A` | `(1,3),(2,4)` | `0,0` | `1/10` | `10/3` |
| 1 | 1 | `G_A` | `(1,3),(2,4)` | `0,1` | `1/10` | `10/3` |
| 1 | 1 | `G_A` | `(1,3),(2,4)` | `1,0` | `3/20` | `5/2` |
| 1 | 1 | `G_A` | `(1,3),(2,4)` | `1,1` | `3/20` | `5/2` |

The path probabilities sum exactly to 1.

Reproducible exact-arithmetic script: `of39_exact_enumeration.py`.

## 8. Theorem/novelty prosecution

### What the gate establishes

1. **Endogeneity exists beyond graph sparsity.** The failure occurs with exact finite-state references and known parameters.
2. **The completed graph can change support.** `Law(Y | V)` is a scheduler-compatible truncation of the fixed-design product law.
3. **Frozen-final-graph exact calibration can fail.** The oracle Pearson statistic has materially different conditional reference laws, and the frozen exact p-value is anti-conservative at a standard nominal level in this example.
4. **Exact replay is valid for the joint adaptive experiment.** Reproducing the same null data-generating process and scheduler produces the correct exact reference law, up to ordinary discreteness.

### Why this does not clear C011

The hard novelty test is not whether the phenomenon is real; it is whether the proposition contributes statistical content not already inherited from adjacent theory.

- Hamilton & Tawn [R195] explicitly establish that later adaptive comparisons are not ancillary and that their parametric bootstrap must replay the adaptive scheduling scheme while holding only the ancillary initial round fixed. Proposition 1 is a finite-state spelling-out of that same non-ancillarity mechanism.
- The exact-replay validity statement with known parameters is generic: an independent replicate from the same null experiment supplies the correct reference distribution for any statistic. It is not Bradley–Terry-specific.
- Yi & Wang [R197] already establish goodness-of-fit theory for dependent response-adaptive designs, blocking a broad claim that adaptive GOF itself is new.
- Wu et al. [R196] supply the Pearson/object diagnostic objects; substituting those statistics into an already-established replay mechanism is an implementation transfer, which the program has already ruled insufficient under L055.
- A targeted September 2026 check also found active paired-comparison lack-of-fit theory on fixed/sparse graphs [R217], increasing competition around the secondary power/detectability axis even though that work does not address outcome-adaptive schedules.

Therefore the exact proposition is useful as a program theorem and methodological warning, but it is **too mechanically implied by known non-ancillarity plus standard exact resampling to anchor a first research project**.

## 9. Final disposition

> **OF-39 — PARKED / MECHANISM ESTABLISHED, DISTINCT CONTRIBUTION NOT ESTABLISHED.**

Do **not** assign C011.

Do **not** expand the OF-39 simulation grid.

Do **not** promote “scheduler replay for diagnostics” as the contribution.

### Reopen only if one of the following survives a fresh, direct prosecution

1. a genuinely statistic-specific theorem for fitted Bradley–Terry diagnostics under adaptive scheduling that is not a generic replay-bootstrap corollary;
2. an estimand or conditional-validity target for which full scheduler replay is unavailable and a new computable correction/bound is required;
3. a nontrivial design-versus-diagnostic-power theorem showing how information-seeking scheduling changes detectability and yielding a scheduler design rule rather than another calibration transfer;
4. a documented real adaptive system exposing a failure that existing adaptive-design and paired-comparison theory cannot explain mechanically.

These are reopening conditions, not current execution tasks.

## 10. Program consequence

The exact-enumeration gate has done its job: it converted a plausible simulation signal into a clean theorem, then showed that the theorem does **not** clear the program's novelty threshold.

The next executable action should return to **review-first cross-field opportunity generation**, with C011 still unassigned rather than forced.

## 11. Evidence

Primary anchors: [R195–R197, R213–R217].

The immediate predecessor is `21_OF39_ADAPTIVE_DIAGNOSTIC_PROSECUTION.md`.

---

## D027 review-first cross-field opportunity generation III — 2026-09-08

### Decision status

**Completed. One opportunity survives to bounded screening; C011 remains unassigned. No execution project is authorized.**

The pass followed L047/L051: begin from current reviews and live institutional limitations, abstract the statistical object, search classical ancestors and adjacent mechanisms, and allow the output to be no candidate.

### A. Review-first channels examined

#### A1. Humanitarian statistics and modeled population frames

A 2026 humanitarian-statistics review highlights data gaps/biases, dynamic population data and decision consequences [R218]. A gridded-population survey-sampling review had already identified uncertainty in cell-level modeled population counts and the possible use of that uncertainty in survey design as a strategic research need [R219].

The apparently fresh question — *what happens when uncertain modeled population counts are used as PPS measures of size?* — does not survive abstraction. Imperfect frame information and imperfect measures of size in PPS/complex designs are established survey-sampling objects [R220–R221]. The humanitarian/gridded setting may still support an application or domain-specific comparison, but the broad methodological claim is an implementation transfer.

**Disposition:** no OF number; collapse before opportunity registration.

#### A2. Informative observation / degraded observation-process ideas

Current longitudinal/functional and point-process work already treats informative observation times, joint visiting processes, imperfect detection/displacement and related identifiability problems. These are scientifically relevant but competitively dense and do not presently offer a first-project-scale distinct object stronger than the existing program watchlists.

**Disposition:** no new OF number.

#### A3. Live federal race/ethnicity standards transition

The 2024 revision of Statistical Policy Directive No. 15 changes the federal race/ethnicity collection standard, including a combined question and a new MENA minimum category [R222]. The federal Bridging Data Tools explicitly describe their current program as an **initial/basic bridge** and state that more robust methods are expected as additional 2024-standard data become available [R223].

The Census Scientific Advisory Committee record creates a more precise reliability seam [R224]:

- national Phase-1 factors should not be used as though subnational composition were homogeneous;
- age, nativity/place of birth, geography and time can plausibly change bridge behavior;
- Census does not have a clean contemporary survey in which the same respondents received both the 1997 and 2024 question formats simultaneously;
- linked 2015 National Content Test / 2020 Census records have a five-year gap and design differences;
- small bridge factors can yield very small/fractional estimates and become more problematic for small areas;
- Census itself is exploring alternative/model-based bridge methods.

A 2025 population-health analysis independently demonstrates that recent Census race/ethnicity processing changes can produce consequential discontinuities in demographic, socioeconomic and mortality analyses [R225].

However, *bridging categories* is not new. The earlier 1977→1997 transition used regression-based race bridging and explicitly evaluated resulting vital rates, with geographic/demographic variation in allocation probabilities [R226]. Nor is generic uncertainty propagation through a misclassification/transition matrix new: quantitative bias and Bayesian sensitivity methods already propagate uncertainty in classification parameters into downstream estimands [R227].

Therefore the surviving opportunity cannot be “invent a bridge” or “put uncertainty around bridge factors.”

### B. Surviving opportunity

## OF-44 — Downstream inferential reliability under heterogeneous 1997↔2024 SPD-15 bridging

**Status:** **PRIORITY BOUNDED SCREENING / NOT C011**  
**Priority:** HIGH among current leads, but below candidate status.

### Core question

> When a fixed/national bridge between 1997 and 2024 SPD-15 categories is applied to data whose transition behavior varies by geography, age, time or data system, which downstream conclusions about subgroup rates, disparities, trends or rankings are robust, and which can reverse under bridge heterogeneity that is compatible with available evidence?

### Statistical object

Let `B0` denote a published/reference bridge matrix and `Bs` a stratum-specific bridge for stratum `s`. For a downstream functional `T` — e.g. a subgroup rate, rate ratio/difference, trend contrast, or ordering — the screening target is not a generic corrected point estimate. It is one of:

1. an identified/sensitivity set `{T(Bs): Bs in H}` under a scientifically interpretable heterogeneity class `H`;
2. a sharp or computable tipping condition for sign/ranking/trend reversal;
3. a robustness certificate showing that a conclusion is invariant over `H`;
4. if sampling/bridge-estimation uncertainty is estimable, calibrated uncertainty that separates ordinary sampling error from bridge uncertainty rather than conflating the two.

The contribution must be stronger than plugging a standard probabilistic-bias-analysis engine into one federal table.

### Why this survives generation

- **Importance:** the standards transition is live and affects federal statistical comparability [R222–R224].
- **Documented assumption pressure:** official advisory material explicitly flags geography, age/time behavior, lack of ideal dual-format validation, and small-factor issues [R224].
- **Consequence:** recent empirical work shows race/ethnicity coding discontinuities alter mortality and other downstream statistics [R225].
- **Feasibility signal:** official bridge factors, code and example datasets are public [R223], so an initial mathematical and aggregate-data audit is workstation-scale.
- **Distinct target:** robustness of *downstream decisions/functionals* under bridge heterogeneity is narrower than bridge construction itself.

### Principal novelty threats

1. Earlier race bridging already models demographic/geographic variation and compares downstream vital rates [R226].
2. Misclassification/measurement-error sensitivity analysis already supplies generic matrix/bias machinery [R227].
3. Census is actively developing Phase-2/alternative bridge methods [R224], creating direct competition and possible data-access asymmetry.
4. If the proposed result is only a numerical sensitivity table for chosen perturbations, it fails L050/L051 and should be killed.

### Bounded screening gate before C011

**P1 — exact prior-art prosecution.** Search race-bridging, categorical harmonization, measurement-error and transition-matrix literatures for sharp downstream bounds, sign/ranking reversal conditions, and uncertainty propagation under estimated/heterogeneous bridge matrices. Kill if the desired theorem is a direct special case.

**P2 — data-feasibility audit.** Determine which dual-coded, linked, test, or aggregate validation substrates are publicly reproducible. Distinguish public bridge factors/example data from restricted Census linked data. Kill first-project status if the key heterogeneity object cannot be constrained or meaningfully stress-tested with public evidence.

**P3 — formal toy theorem.** Before any large empirical study, derive the smallest nontrivial case (two periods / two or three groups) and ask whether bounded deviations from `B0` give a sharp tipping condition for a disparity/trend/ranking conclusion. If the algebra reduces immediately to standard misclassification sensitivity formulas with no new decision structure, kill.

**P4 — consequentiality check.** Using only reproducible public inputs, test whether plausible bridge heterogeneity can change a substantive conclusion rather than merely widen decimals. If no sign/order/trend conclusion can change under defensible perturbations, deprioritize.

### Promotion rule

OF-44 may become C011 only if P1–P4 jointly establish:

- a distinct statistical object beyond existing bridge/misclassification machinery;
- a reproducible validation/sensitivity substrate;
- a nontrivial decision consequence;
- and a bounded first-project contribution that is not dependent on privileged Census microdata.

### C. D027 disposition

- **OF-44** is the sole new registered opportunity and advances to **PRIORITY BOUNDED SCREENING**.
- The gridded-population/PPS uncertainty idea is collapsed before registration because its abstract object is established imperfect-MOS/frame sampling.
- Informative-observation and degraded-observation leads remain too occupied for this pass.
- **C011 remains unassigned.**
- **Next executable action:** run the four-part OF-44 bounded screening gate above, beginning with P1 prior-art prosecution and P2 public-data feasibility in parallel.


# D028 / OF-44 bounded screening result

## P1 — exact nearest-neighbor/theorem prosecution

**Verdict: FAIL.** The proposed abstract object is already contained in generic misclassification partial identification. Molinari [R228] writes the discrete-category problem as a linear system governed by a misclassification-probability matrix, allows general restrictions on that matrix, and obtains sharp identification regions for arbitrary real functionals, with conditional/outcome extensions. Therefore, for a bridge matrix `B_s` constrained to `H`, the set `{T(B_s): B_s in H}` and the corresponding zero/order crossing conditions are not, by themselves, a new theorem. Direct matrix-method work for standardized rate ratios under polychotomous misclassification adds further pressure [R229].

The standards-transition semantics do not change this algebraic inheritance. A distinct contribution would require additional structure — e.g. a new coupling restriction across strata/time, nonstandard sampling/inference, or a decision problem whose optimal rule is not mechanically recoverable from the generic identified set. None is currently established.

## P2 — public-data feasibility

**Verdict: PARTIAL / INSUFFICIENT FOR FIRST PROJECT.** Reproducing Phase-1 national bridging is straightforward from public factors, Python/SAS programs and examples [R223]. Public content-test reports also quantify aggregate changes under combined versus separate question formats [R230].

But the key OF-44 sensitivity object is bridge **heterogeneity**, not the national point bridge. Official Census material states that national factors should not be treated as subnational factors, discusses future state/county factors, flags nativity and time variation, and says the useful 2015 NCT↔2020 Census evidence comes from linked respondents with a five-year gap rather than an ideal simultaneous dual-format survey [R224]. The public aggregate reports do not supply the same-person stratum-specific transition cells needed to constrain geography/nativity/time `B_s` sharply.

## Gate disposition

Because **P1 fails**, the project stop rule applies. **P3 (toy tipping/bounding theorem) and P4 (consequentiality experiment) are not run.** Running them would only reproduce a phenomenon already inherited from generic matrix sensitivity analysis and would not restore novelty.

> **OF-44 — PARKED / NO-GO FOR FIRST PROJECT. C011 remains unassigned.**

### Reopen only if

- public Phase-2 or other dual-coded data identify meaningful stratum-specific transition variation;
- a new structural restriction creates a non-generic identified set or inference problem; or
- a substantive application requires a validation/design contribution beyond ordinary bridge sensitivity analysis.

**Next executable action:** return to review-first cross-field opportunity generation; do not force C011.


# D029 / review-first cross-field opportunity generation IV

## Search discipline

This pass resumes discovery after OF-44 failed its first novelty gate. It follows L046–L052 strictly: begin from current reviews/methods, formulate a possible reliability object only after the field problem is visible, search the exact problem sentence and classical statistical ancestor, and **do not assign an OF identifier to a route that is already directly occupied**.

The goal is not a quota of opportunities. A null-generation result is acceptable if every screened route fails before registration.

## Routes screened

### 1. Informative cluster size × prediction validation

**Disposition: COLLAPSE BEFORE REGISTRATION.** The proposed seam — whether visit-level/person-level splitting and validation target the intended prospective prediction performance when cluster size is informative — is already explicit in prediction-specific work. Coley et al. compare visit- versus person-level splitting/cross-validation against a prospective validation set [R231]. Pavlou et al. directly study prediction accuracy, calibration and discrimination under informative cluster size/confounding by cluster [R232].

No distinct reliability object remains merely by reframing the estimand or validation split.

### 2. Meta-analysis extraction/application errors × downstream robustness

**Disposition: COLLAPSE BEFORE REGISTRATION.** A 2024 systematic review catalogs data-extraction/manipulation, analysis and interpretation errors in pairwise meta-analysis [R233]. Xu et al. empirically re-extract adverse-event data and quantify changes in meta-analytic conclusions after correction [R234]. Fragility methods already formalize how small event-status changes can reverse statistical significance [R235].

A generic “tipping point for extraction errors” would therefore be a new summary of an occupied sensitivity/fragility problem rather than a distinct contribution.

### 3. Population-denominator uncertainty × small-area rates/disparities

**Disposition: COLLAPSE BEFORE REGISTRATION.** Peterson et al. explicitly embed heterogeneous population-at-risk uncertainty in Bayesian spatial disease mapping using classical/Berkson measurement-error models [R236]. Nethery et al. directly compare denominator sources and quantify induced bias in small-area disparity estimates [R237].

The broad reliability question — how denominator uncertainty changes rates, rankings or disparities — is already methodologically explicit.

### 4. Multiple imputation × internal validation ordering

**Disposition: COLLAPSE BEFORE REGISTRATION.** The exact ordering problem is now a named methodological literature. Awounvo et al. systematically review MI-before versus MI-during internal validation in clinical prediction modeling [R238]. Wahl et al. previously compared validation-then-imputation and imputation-then-validation strategies by simulation and found optimistic bias for some orderings [R239].

There is no basis to register a new opportunity from “imputation leakage” without an additional structure not present in these methods.

### 5. Noisy protected attributes × fairness reliability

**Disposition: COLLAPSE BEFORE REGISTRATION.** Celis et al. provide a general fair-classification framework with provable guarantees under noisy protected attributes [R240], and Wu et al. extend the problem directly to AUC fairness with noisy protected groups [R241].

Thus the generic measurement-error/fairness bridge is already an active ML theory object, not an unoccupied cross-field statistical seam.

### 6. LLM-assisted evidence synthesis × end-to-end error propagation

**Disposition: COLLAPSE / HIGH ACTIVE-WORK COMPETITION.** A September 2026 systematic review now synthesizes LLM data-extraction accuracy and reliability in evidence synthesis [R242]. A 2025 study-within-reviews quantifies AI-assisted extraction errors at scale [R243]. More importantly for novelty, an August 2026 preprint explicitly studies end-to-end propagation of AI extraction errors into pooled effects and heterogeneity across 20 case studies [R244].

Even if the active-work paper is not definitive, it occupies the exact problem sentence strongly enough that this is poor first-project competition geometry.

### 7. Multisite harmonization × validation leakage

**Disposition: COLLAPSE BEFORE REGISTRATION.** Marzi et al. explicitly demonstrate that harmonizing a full multisite MRI dataset before model splitting leaks test information and propose a pipeline-safe harmonizer [R245]. Nieto et al. 2026 studies leakage under site/class imbalance and proposes a leakage-free alternative [R246].

The proposed “harmonization before validation can inflate performance” reliability warning is therefore already a direct contribution, not a new opportunity.

## D029 disposition

**Result: VALID NULL GENERATION PASS.**

- **No new OF identifier is created.**
- **C011 remains unassigned.**
- **No execution project is authorized.**
- The screened routes were killed at the review/problem-sentence/ancestor gate rather than carried forward as cosmetically novel “apply A to B” ideas.
- No new general lesson is added to `02_RESEARCH_PRINCIPLES_AND_LESSONS.md`; L042, L046–L052 and L061 already govern this outcome.

This null result is evidence about the search neighborhood: repeated sampling from biomedical prediction, evidence synthesis, data harmonization and adjacent ML reliability is producing high direct-occupation rates.

## Next executable action after D029

Run a **diversified review-first reconnaissance** outside the repeatedly sampled biomedical-prediction/evidence-synthesis neighborhoods. Begin with a bounded set of current 2025–2026 reviews/guidance from more distant statistical domains — for example official statistics, experimental design, statistical computing/numerical reliability, environmental/spatial statistics, and social-science measurement — and apply the same no-registration-until-survival rule.

Do **not** search for C011 directly. Search for unresolved statistical reliability objects; C011 is assigned only if one independently survives the Charter gates.

# D030 / diversified review-first reconnaissance across distant statistical domains

## Search discipline

D029 required an explicit test of whether repeated nulls were an artifact of over-sampling a narrow set of biomedical-prediction/evidence-synthesis neighborhoods. D030 therefore sampled five deliberately more distant domains and retained the same **no-registration-until-survival** rule.

The pass is bounded: one consequential reliability seam per domain was taken far enough to test the exact problem sentence, classical ancestor/current method, active-work geometry and first-project plausibility. A route that failed there was not given an OF identifier.

## Domain 1 — official statistics: multi-source quality propagation

**Possible seam:** when a foundational administrative/source dataset changes or degrades, can statistical agencies quantify how source-specific uncertainty propagates through a network of linked/integrated statistical products strongly enough to support release/revision decisions?

**Disposition: COLLAPSE BEFORE REGISTRATION.** The 2026 UNECE HLG-MOS handbook explicitly says quality management for multi-source statistics must shift from assessing individual datasets to ensuring quality across the entire integrated system [R247]. The National Academies' 2017 multi-source quality framework already treats linkage errors and fitness-for-use of component sources in relation to final federal statistics [R248]. ONS's multiple-source error framework explicitly distinguishes target linked, source, linked, aligned and processed data and uses the error structure to inform integrated-data design [R249].

The generic object is therefore already conceptualized as system-level multi-source statistical quality. A student-scale project would need a much narrower estimand/decision with new identification or inferential structure; D030 did not find one that survived the initial gate.

## Domain 2 — experimental design: adaptive randomization with missing or mismeasured inputs

**Possible seam:** adaptive allocation can feed early outcome/covariate error back into later design decisions, potentially altering both patient allocation and final inference.

**Disposition: COLLAPSE / ACTIVE.** Current RAR reviews explicitly list measurement/classification error and missing data as adaptive-design challenges [R250]. Current 2026 theory treats inference for covariate-adaptive randomization with missing covariates [R251], while earlier work/reviews already record misclassification-specific adaptive-allocation results and randomization-based repair of adaptive-inference problems [R252].

The feedback mechanism is real, but the broad problem sentence is neither empty nor competitively quiet enough for registration without a sharper structure.

## Domain 3 — statistical computing / numerical reliability: implementation decisions that change inference

**Possible seam:** can apparently equivalent statistical analyses cross a scientific decision threshold because software defaults, numerical algorithms or implementation choices differ?

**Disposition: COLLAPSE / HIGH ACTIVE-WORK COMPETITION.** Wang's accepted 2026 *American Statistician* article directly catalogs 37 hidden implementation/default decisions across SPSS, R, SAS, Stata and Python and demonstrates significance flips on constructed boundary datasets [R253]. The problem also has deep ancestry: McCullough's software-reliability benchmark program dates to 1998–1999 [R254], and Altman, Gill and McDonald provide computational-stability diagnostics for model results [R255].

Thus even the decision-reversal framing is directly occupied. A narrower hardware/precision certificate would still inherit classical numerical-stability theory and faces current reproducibility competition.

## Domain 4 — environmental/spatial statistics: uncertainty of spatial aggregates

**Possible seam:** map makers often report pointwise uncertainty while policy decisions depend on regional totals/averages whose uncertainty depends on spatially correlated prediction errors.

**Disposition: COLLAPSE BEFORE REGISTRATION.** Wadoux and Heuvelink 2023 directly derive and test scalable uncertainty calculations for spatial averages and totals that account for spatial autocorrelation in map errors [R256]. Their 2025 follow-up documents that uncertainty of spatial aggregates is still frequently computed incorrectly, while explicitly emphasizing that methods already exist [R257].

The consequential failure is real, but the obvious methodological repair is established. The remaining gap is mainly adoption/implementation unless a new decision or data structure is supplied.

## Domain 5 — social-science measurement: mixed-mode survey effects under partial information

**Possible seam:** mixed-mode surveys can combine mode-specific measurement error with nonrandom mode selection, while analysts may lack external evidence about mode-effect magnitude needed by preferred adjustment methods.

**Disposition: COLLAPSE / HIGH ACTIVE-WORK COMPETITION.** Tomova, Silverwood and Wright's January 2026 systematic review states this external-evidence bottleneck directly [R258]. But the same active research program already develops DAG-based diagnosis and quantitative bias-analysis guidance for mode effects plus mode selection [R259], and an August 2026 randomized study examines mixed-mode effects on both item measurements and variable correlations [R260].

This is exactly the sort of review-generated opening that should be killed early when the review authors are already prosecuting the next methodological step.

## D030 disposition

**Result: VALID SECOND NULL GENERATION PASS.**

- **No OF-45 is created.**
- **C011 remains unassigned.**
- **No execution project is authorized.**
- All five deliberately diversified domains were screened without weakening the Charter gate.

D030 rules out a simple explanation for D029: the null was not only due to repeatedly sampling biomedical/ML-adjacent literatures. Current review-first discovery across distant domains also has a high direct-occupation rate.

## Next executable action after D030

Stop repeating broad review-first field sweeps. Per L027/L031/L034/L038, switch to a **bounded independent-channel triangulation pass**:

1. **Data-generated:** audit a small number of public, high-stakes statistical workflows/datasets for reproducible anomalies, instability, failed replication, subgroup/site/time reversals or sensitivity to realistic data imperfections.
2. **Decision-generated:** collect concrete agency/practitioner release, calibration, validation, weighting, revision, monitoring or “use/do-not-use” decisions where uncertainty currently changes action.
3. **Theory-generated:** for each serious anomaly/decision, write the estimand, mechanism, identification assumptions and simplest counterexample/decomposition before searching for a method.
4. **Convergence rule:** create a new OF identifier only when at least two independent channels point to the same reliability object. Then apply the ordinary literature, classical-ancestor and active-work kill gates.

Do **not** search for C011 directly. Do **not** begin substantive project execution until a lead survives the Charter gates.

# D031 / independent theory-data-decision triangulation

## Search discipline

D030 ended two consecutive review-first null passes and explicitly required a change in discovery channel rather than a lower novelty threshold. D031 therefore began from **public operational decisions and data states**, derived the statistical mechanism before literature search, and required at least two independent discovery channels to converge before any new OF identifier could be assigned.

The pass was bounded to four high-stakes public workflows. A route that converged but collapsed under classical/direct prior art remained unregistered.

## Route A — provisional operational data versus later quality-assured data

**Operational observation.** EPA's public AirData workflow temporarily fills recent periods with preliminary AirNow observations and replaces them with AQS observations as they become available; EPA explicitly distinguishes the preliminary and certified/quality-assured roles [R261].

**Theory-generated object.** A model, threshold or monitoring rule can be operated on a provisional data state but later evaluated on a revised/final state. If the revision process is informative, final-state validation may not estimate operational reliability at decision time.

**Disposition: COLLAPSE BEFORE REGISTRATION.** The general object is mature real-time/vintage-data reliability: Croushore and Stark show that data vintages and revisions can alter econometric results, policy analysis and forecasting [R262]. The EPA example is a useful domain illustration, not a distinct first-project object.

## Route B — HUD QCT precision screening of noisy ACS estimates

### Decision channel

HUD's current Qualified Census Tract designation uses noisy ACS tract estimates inside hard poverty/income eligibility thresholds. It also applies a **data-quality reject rule**: median-income and poverty inputs fail the relevant calculation when their margin-of-error ratios are around 50% or larger; the substantive criterion must hold in at least two of three ACS 5-year releases; and a 20% population cap can then determine final designations [R267, R272].

Treasury guidance on ACS-based geographic proxies exposes the competing decision principle directly: because sampling error is inversely related to sample size, incorporating the margin of error can systematically disadvantage lower-population tracts, and Treasury permits grantees to disregard it in the interest of equity [R268].

This is not a generic statement that uncertainty matters. It is an explicit policy tension between **rejecting noisy estimates to improve reliability** and **maintaining coverage of lower-population geographies**.

### Data channel

HUD provides public all-tract extracts with the estimates and margins of error used for QCT designation plus a public algorithm [R272]. Crucially, there is a documented historical intervention in the reliability rule: for the 2016 QCTs HUD tightened the accepted MoER from **below 100%** in prior designations to roughly **50% or less** [R271].

Therefore a policy-counterfactual replay is feasible in principle: hold the substantive thresholds and designation logic fixed where the archival rule permits, then compare tract eligibility/designation under the old and current precision screens.

### Theory channel

For tract `i` and release `t`, write a target estimate `Y_it` with uncertainty scale `sigma_it`, a substantive eligibility indicator `E_it`, and a reliability indicator

`R_it(c) = 1{ MoE_it / |Y_it| <= c }`,

with historical `c` near 1 and current `c` near 0.5 for the relevant inputs.

The key mechanism is **selective coverage**:

1. the probability of `R_it(c)=1` depends on precision/effective sample size and therefore can vary with tract population even at comparable latent need;
2. stricter `c` can lower classification error among retained observations while excluding more low-precision tracts;
3. the two-of-three rule combines decisions across heavily overlapping ACS 5-year releases, so independent-release calculations are inappropriate without justification;
4. the 20% population cap creates **nonlocal displacement**: removing one otherwise eligible tract can change which different tract is ultimately designated.

### Direct ancestors and anti-novelty constraints

The broad problem is old. HUD/Census analysis already showed QCT misclassification risk is higher for smaller tracts and near the cutoff, explicitly discussed false inclusion versus false exclusion, and noted complications from the 20% cap [R269]. Brown and Scardamalia study instability of ACS-based threshold program eligibility across multi-year releases [R270]. Generic selective-classification theory also shows that abstention intended to improve average reliability can magnify disparities across groups [R274].

These facts kill any OF-45 claim such as “small-area sampling error causes unstable eligibility” or “reliability screening can trade coverage for accuracy.”

### Active-work prosecution

Soltas [R273] is the strongest current neighbor located. His LIHTC analysis:

- reconstructs HUD's QCT assignment rule;
- explicitly includes high-ACS-sampling-error disqualifications and the 20% cap;
- uses HUD-reported margins of error to simulate sampling-driven assignment changes; and
- finds sampling variation supplies substantial year-to-year designation variation used for causal identification.

But the paper's estimand is the effect/incidence of LIHTC subsidies. The **MoER screen itself** is a component of assignment, not the object being evaluated. D031 found no direct study asking what the post-2016 tightening of the reliability screen bought in error control versus what population-linked exclusion/displacement it induced.

### OF-45 registration

> **OF-45 — Reliability-versus-coverage consequences of HUD's post-2016 ACS precision screen in Qualified Census Tract designation.**
>
> **Status:** PRIORITY BOUNDED PROSECUTION / NOT C011.

**Narrow problem sentence:**

> Under HUD's post-2016 QCT regime, what reliability gain did tightening the MoER screen from <100% to approximately <=50% buy, what population-dependent exclusion burden did it create, and how do the two-of-three rule and 20% population cap propagate the screen into final designations?

### What is directly identifiable from public data

With archived HUD inputs and exact algorithms, the project should be able to identify:

- which tract-release inputs fail the precision screen;
- tract eligibility under exact policy replays;
- the change in eligibility when `c` is changed from the historical to current rule;
- final designation changes after applying the population cap; and
- population-stratified/selective-coverage and cap-displacement summaries.

These are **policy-counterfactual rule effects**, not estimates of latent truth.

### What is not directly identified

The true tract income/poverty status corresponding to each noisy ACS estimate is not observed. Thus the actual reduction in false inclusions/false exclusions caused by the tighter screen cannot be read directly from HUD point estimates and MoEs. Consecutive ACS 5-year products also share four of five calendar years, so release errors are correlated.

A central next-gate requirement is therefore to separate:

- design-identifiable designation/coverage consequences; from
- model/sensitivity-dependent statements about underlying classification reliability.

If no defensible correlated-error/latent-truth analysis exists, OF-45 must be narrowed further or parked rather than oversold.

## Route C — duplicate adverse-event reports in FAERS

**Decision/data observation.** Duplicate spontaneous reports can distort safety-signal calculations and must be identified before reliable data mining.

**Disposition: COLLAPSE / DIRECT ACTIVE WORK.** A 2024 scoping review already synthesizes duplication in pharmacovigilance databases [R263]. Kreimeyer et al. 2025 provide a full-database network-based FAERS deduplication pipeline evaluated on expert-adjudicated data and operating at FDA [R264]. No OF identifier is warranted.

## Route D — missing measure groups in CMS hospital star ratings

**Decision observation.** CMS computes the Overall Hospital Quality Star Rating from available measure groups, redistributes weights when a group is absent and compares hospitals within peer groups based on the number of available groups [R265].

**Disposition: COLLAPSE BEFORE REGISTRATION.** AHA/KNG evaluation already reports that star ratings remain more volatile for hospitals reporting fewer measures, especially smaller, rural and critical-access hospitals, and frames this as an equity issue [R266]. The broad instability object is directly occupied.

## D031 disposition

- **OF-45 is created** from Route B only.
- Routes A, C and D collapse before registration.
- **C011 remains unassigned.**
- **No execution project is authorized.**
- D031 validates the independent-channel rule: unlike the D029–D030 review-first nulls, a decision/data/theory convergence exposed a narrower object that survived enough prior-art prosecution to justify an OF identifier, while the same gate still killed three tempting routes.

## Next executable action after D031

Run the **OF-45 bounded data + identification gate** before any candidate promotion:

1. **Exact reconstruction:** obtain archived all-tract HUD QCT inputs and reproduce the current designation algorithm, including reliability screens, two-of-three criterion, ranking and 20% cap.
2. **Historical-screen replay:** implement the pre-2016 MoER `<100%` rule and the post-2016 approximately `<=50%` rule while controlling for other rule changes as explicitly as the archive allows.
3. **Coverage/distribution audit:** quantify screen-only failures and designation changes by tract population and by distance from the substantive income/poverty thresholds. Do not label a raw population association as inequity without this decomposition.
4. **Cap propagation:** measure how screen-induced removals change final designations of other tracts under the 20% cap.
5. **Identification boundary:** determine whether ACS replicate/covariance information can support correlated-error analysis across overlapping releases; otherwise construct an explicit sensitivity family and state that true error reduction is not identified.
6. **Nearest-neighbor recheck:** prosecute housing/public-finance and small-area decision literatures specifically for post-2016 MoER-screen evaluation, not generic QCT sampling variation.

**Kill OF-45** if modern-screen consequences are negligible, the population gradient disappears after conditioning on substantive-threshold proximity, cap displacement is immaterial, or the core reliability claim depends on indefensible latent-truth assumptions. **Promote toward C011 only** if a consequential population-dependent coverage/designation effect is reproducible and the bounded contribution remains distinct from [R269–R274].

# D032 / OF-45 bounded rule-and-identification gate

## Exact rule reconstruction

The historical comparison is sharper than a generic “old versus new QCT” before/after. The 2015 procedure already used three overlapping ACS 5-year releases and a release-level reliability check: income or poverty inputs whose 90% confidence interval included zero were not usable [R275]. For positive estimates, `estimate - MOE > 0` is equivalent to `MOE / estimate < 1`, i.e. relative MoE `<100%`. HUD's 2016 notice then tightened the screen to approximately `<=50%` [R271].

The modern algorithm [R272] provides a deterministic same-data intervention:

- choose `c` in relative-MoE space;
- reject income release `t` when `MOE(B19013_t) / B19013_t` fails `c`;
- reject poverty release `t` when either numerator or denominator relative MoE fails `c`;
- apply the modern two-of-three substantive criterion;
- average passing values for ranking;
- run the area-level 20% cap rule.

This replay isolates the **screen threshold** while holding data, substantive cutoffs, geography and cap machinery fixed. It should not be described as the total historical effect of changing from 2015 to 2016, because other implementation details and ACS vintages also differ.

Using ACS `MOE = 1.645 * SE` [R277], the current 50% relative-MoE rule corresponds to CV about 30.4%, versus about 60.8% under the old 100% rule.

## Identification boundary

The observable target is

`D(c) = HUD_algorithm(all-tract observed estimates, MoEs, income limits, populations; c)`.

With the national input table, `D(0.50)` and `D(1.00)` are deterministic and their difference can be decomposed into:

1. direct release-level screen changes;
2. tract eligibility changes;
3. ranking changes among remaining eligible tracts; and
4. nonlocal cap-mediated designation gains/losses.

This is sufficient for a policy reliability/coverage analysis.

It is **not** sufficient to estimate how many classifications become correct relative to latent tract truth. Census explicitly recommends against comparisons that treat overlapping 5-year estimates as distinct independent periods because most component data are shared [R276]. Marginal MoEs identify marginal standard errors [R277], but not the covariance among the three overlapping releases. In addition, the underlying tract income/poverty state can change across calendar years. Any latent-accuracy analysis must therefore specify both a joint error model and a temporal-state model; it belongs in sensitivity analysis, not in the design-identified headline result.

## Nearest-neighbor recheck

The May 2026 Soltas paper remains the closest empirical neighbor [R278]. It explicitly:

- reconstructs the QCT rank/assignment mechanism;
- includes high-sampling-error disqualifications and the 20% cap; and
- simulates sampling variation using normal errors whose marginal standard deviations are derived from HUD/Census MoEs.

This eliminates reconstruction and generic “ACS noise changes QCT assignment” from the novelty set. The paper still uses QCT variation to identify LIHTC responses; it does not evaluate the post-2016 precision screen as the policy object or estimate its population-conditioned coverage and cap-displacement consequences. OF-45 therefore survives this recheck only in its already narrow formulation.

## Empirical replay status

HUD publicly lists the nationwide all-tract workbook [R272], but the current runtime could not ingest the Excel binary. A Florida Housing Finance Corporation mirror exposes the expected all-tract schema—including three release-specific `B17001` and `B19013` estimates/MoEs and the ranking/cap inputs [R279]—but its extent is Florida and it is not a valid substitute for the national gate. No national magnitude claim is made from it.

Accordingly, D032 does **not** apply the OF-45 kill/promotion rule yet. The decisive quantities remain unmeasured: national screen-only exclusion, population gradient conditional on substantive-threshold proximity, and cap-mediated displacement.

## D032 disposition

- Rule reconstruction: **PASS**.
- Identification boundary: **PASS / NARROW**.
- Nearest-neighbor recheck: **SURVIVES NARROWLY**.
- National empirical magnitude gate: **UNRESOLVED**.
- **OF-45 remains PRIORITY BOUNDED PROSECUTION / NOT C011.**
- **C011 remains unassigned.**
- **No execution project is authorized.**

## Next executable action after D032

Acquire the nationwide HUD all-tract QCT workbook through a binary-capable path, then execute the same-data `c=0.50` versus `c=1.00` replay. First validate that the `c=0.50` implementation reproduces HUD's published `qct` designation. Then report direct screen failures, eligibility changes, final designation changes, conditional population gradients and cap-mediated displacement. Apply the original D031 kill/promotion rule only after this empirical magnitude table exists.

# D033 / OF-45 national empirical magnitude gate

## Data and reconstruction

The national HUD all-tract workbook is now available as project source `qct_data_2026.xlsx` [R280]. It contains 85,390 QCT records (85,385 unique tract IDs; five tract IDs are represented by two split records) across the United States and Puerto Rico.

A direct implementation of the 2026 HUD algorithm [R272] using the workbook's raw ACS estimate/MoE fields, adjusted income limits, tract populations and cap-area populations reproduces the official `qct` indicator with **zero mismatches across all 85,390 records** at the current `c=0.50` screen. This clears the algorithm-validation prerequisite before any counterfactual is interpreted.

## Same-data `c=1.00` versus `c=0.50` replay

The intervention changes only the relative-MoE screen and holds all 2026 observed data and downstream policy machinery fixed.

| Quantity | `<100%` screen | `<50%` screen | Difference from tightening |
|---|---:|---:|---:|
| Income release inputs passing | 250,287 | 238,673 | -11,614 |
| Poverty release inputs passing | 235,206 | 95,091 | -140,115 |
| Income eligible | 15,545 | 13,620 | -1,925 |
| Poverty eligible | 11,850 | 9,175 | -2,675 |
| Eligible by either criterion | 19,253 | 17,210 | **-2,043 (-10.61%)** |
| Final QCT | 15,797 | 14,496 | **-1,301 (-8.24%)** |

Final-status churn is **2,825 records**: 2,063 designations under the looser screen are lost under the current screen, while 762 records not designated under the looser screen become designated after tightening because ranking/cap competition changes.

The poverty screen is the dominant release-level mechanism. Of the 140,115 old-pass/current-fail poverty inputs, 139,854 fail the current rule because the poverty-count numerator alone crosses the 50% relative-MoE boundary; 220 fail both numerator and denominator and 41 fail the denominator alone.

## Conditional population gradient

Among the 19,253 `c=1.00` eligible records, current-screen eligibility loss is 21.8% in the smallest population decile and 5.3% in the largest.

Define two-of-three substantive-threshold distance using the second-highest old-screen release value for each criterion. Across increasing quintiles of overall threshold distance, eligibility-loss rates in the smallest versus largest population quintiles are:

| Threshold-distance quintile | Smallest population quintile | Largest population quintile |
|---:|---:|---:|
| 1 | 28.5% | 7.9% |
| 2 | 23.3% | 6.3% |
| 3 | 19.3% | 4.4% |
| 4 | 14.8% | 3.6% |
| 5 | 11.4% | 2.4% |

Thus the lower-population burden persists even among records similarly distant from the substantive QCT cutoffs.

A robustness model among old-screen eligible records uses log population plus decile indicators for separate income and poverty two-of-three margins, old eligibility type, state fixed effects and metro status, clustering standard errors by cap area. The odds ratio for eligibility loss per population doubling is **0.447 (95% CI 0.383–0.522)**. This is a descriptive mechanism diagnostic and is not interpreted causally.

## Cap-mediated displacement

Of 442 cap areas, 144 bind under `<100%` and 104 bind under `<50%`; 40 areas move from binding to nonbinding after the stricter precision screen.

Designation losses decompose into 1,534 direct eligibility losses and 529 losses among records that remain eligible but move below the cap/ranking allocation. All 762 designation gains are mediated by ranking/cap reallocation. Of those gains, **332 across 87 areas and 32 states have no change in any of their own release-level precision-screen indicators**. These are strict nonlocal effects of screening other records in the same cap system.

This result is substantively stronger than a local selective-classification analogy: the screen changes the decision received by units whose own measured precision and substantive eligibility inputs are unchanged.

## Precision versus accuracy

The tighter rule improves the precision profile of accepted inputs by construction. Mean accepted income relative MoE changes from 0.232 to 0.212; the mean binding relative MoE for accepted poverty inputs changes from 0.561 to 0.396.

Those quantities do **not** establish improved correctness of QCT assignment. The D032 overlapping-release identification boundary remains. C011's headline estimand is the observable precision/coverage/designation tradeoff and its propagation through the cap.

## D033 disposition

The empirical gate is no longer unresolved:

- algorithm validation: **PASS — 0 mismatches**;
- consequentiality: **PASS**;
- conditional population gradient: **PASS**;
- cap/nonlocal displacement: **PASS**;
- identification boundary: **PASS / NARROW**;
- data and compute feasibility: **PASS**;
- nearest-neighbor distinction: **SURVIVES**.

> **OF-45 is promoted to C011 — SURVIVES / PRE-EXECUTION.**

No further primary-project opportunity generation is authorized while C011 remains viable. Literature moves from discovery to monitoring mode.

## Frozen pre-execution protocol skeleton

Before repository-backed execution, fix the following prospectively:

1. **Primary dataset family:** annual HUD all-tract QCT workbooks, with 2026 as the validated anchor and 2016–2026 as the intended multi-year replication range where annual rule reconstruction passes.
2. **Primary contrast:** within each year, change only `c` from 0.50 to 1.00 under that year's published algorithm/data.
3. **Primary outcomes:** release screen passage, criterion eligibility, union eligibility, final QCT, direct final loss, final change while still eligible, and strict nonlocal displacement.
4. **Population-burden analysis:** pre-specify two-of-three threshold-margin definitions; report stratified nonparametric rates first and adjusted models second.
5. **Cap analysis:** record whether each area binds under each screen; decompose status changes by binding transition and own-screen-change status.
6. **Precision analysis:** describe accepted-input relative-MoE distributions; do not label them accuracy.
7. **Sensitivity:** historical anchor comparison is confirmatory; any denser threshold grid is secondary/exploratory unless pre-specified before multi-year extraction.
8. **Latent truth:** excluded from the primary estimand. Any correlated-error/temporal-state model is secondary sensitivity analysis with explicit assumptions.
9. **Falsification/stop rule:** downgrade or park if the 2026 population/cap effect proves highly atypical across reconstructible years, if annual algorithm validation fails materially, or if new direct prior work occupies the precision-screen evaluation itself.
10. **Reproducibility:** preserve raw-source checksums, year-specific rule metadata, exact validation counts and a deterministic end-to-end script before producing manuscript figures.

**Next executable action:** turn this skeleton into the formal C011 execution protocol and repository specification. Repository initialization is the first stage where Work/GitHub tooling is materially useful.

## Change log

### 0.8.0 — 2026-09-08
- Added D033 exact national OF-45 replay from the project-local 2026 HUD all-tract workbook.
- Recorded zero-mismatch reconstruction, material eligibility/designation effects, conditional population gradient and nonlocal cap displacement.
- Promoted OF-45 to C011 and froze the pre-execution protocol skeleton.

### 0.8.0 — 2026-09-08

- Added D032 OF-45 bounded rule/identification prosecution.
- Resolved the same-data screen estimand and nonidentified latent-accuracy boundary; nearest-neighbor survived narrowly.
- Left the national empirical magnitude gate unresolved and C011 unassigned.

### 0.7.0 — 2026-09-08

- Added D031 independent theory/data/decision triangulation across four public workflows.
- Collapsed provisional/final data-state, FAERS-duplication and CMS-star routes before registration.
- Registered OF-45 as the sole priority bounded-prosecution lead and recorded its direct ancestors, closest active neighbor, identification boundary and next public-data gate.

### 0.6.0 — 2026-09-08

- Added D030 diversified five-domain review-first reconnaissance.
- Recorded a second valid null-generation result: no OF-45, no C011, no execution project.
- Replaced further broad review-first sweeps with bounded theory/data/decision-channel triangulation as the next executable action.

### 0.5.0 — 2026-09-08

- Added D029 review-first cross-field opportunity generation IV.
- Recorded seven pre-registration collapses and a valid null-generation result; no OF identifier and no C011.
- Set the next action to a diversified review-first pass outside repeatedly sampled biomedical-prediction/evidence-synthesis neighborhoods.

### 0.4.0 — 2026-09-08

- Added D028 / OF-44 bounded-screening result.
- Recorded P1 failure, P2 partial/insufficient feasibility, and stop-rule cancellation of P3/P4.
- Reclassified OF-44 as parked; C011 remains unassigned.
