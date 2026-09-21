---
title: OF-35 Interval-Censoring Ranking Reliability — Bounded Prosecution
version: 0.1.0
last_updated: 2026-09-07
status: complete — OF-35 parked / no C011
---

# OF-35 Interval-Censoring Ranking Reliability — Bounded Prosecution

## 1. Prosecution question

OF-35 entered prosecution with the question:

> **When interval-censored outcomes are used to evaluate competing survival prediction models, when do observed-data evaluation procedures preserve versus reverse the model ranking that would be obtained from latent exact event times?**

The proposed decision summaries were pairwise ranking reversal, wrong-winner probability and selection regret under sparse/informative assessment and nuisance-model misspecification.

This prosecution tested whether that object was sufficiently distinct from the nearest interval-censoring and survival-evaluation literature to become C011.

## 2. Verdict

**OF-35 is PARKED / NO-GO FOR FIRST PROJECT. C011 remains unassigned.**

The central reason is not that ranking reliability is unimportant. It is that the proposed broad contribution is now too close to current work on both sides of the intended bridge:

1. **interval-censored prediction evaluation already contains the core oracle-versus-observed simulation ingredients** [R182–R183];
2. **a 2026 survival-evaluation paper directly studies censoring-induced distortion of model rankings using oracle event times** [R189];
3. **2026 interval-censoring work explicitly develops strictly proper scoring/calibration machinery and studies monitoring assumptions** [R190];
4. **informative case-K interval-censoring already has active model-selection/model-averaging methodology** [R191–R192].

A paper whose main novelty is to relabel the existing simulation output as “wrong-winner probability” or “selection regret” would not clear the Charter's contribution-strength standard.

## 3. Direct-neighbor extraction

### 3.1 Wu & Cook — R182

Wu & Cook develop imputation, IPW and AIPW estimators for prediction error and AUC when validation outcomes are case-K interval censored. Their weighting model jointly represents the event process, recurrent assessment process and loss to follow-up.

Their simulations already manipulate the observation process and explicitly study misspecification of the visit/assessment model. In particular, they generate non-Markov renewal assessments while fitting Poisson-process assessment models and report bias/variance consequences for prediction-error and AUC estimators.

**Consequence:** the OF-35 axis “assessment-process misspecification changes evaluation” is occupied at the per-metric-estimator level. The remaining novelty cannot merely be another robustness simulation.

### 3.2 Yang et al. — R183

Yang et al. are the strongest interval-censoring direct threat. Their 2026 simulation:

- fits **three competing prediction models**: one correctly specified and two misspecified;
- computes AUC, Brier score and EPCE using the **true latent event times** as an ideal/reference evaluation;
- evaluates the same models using model-based, IPCW and naive interval-censored procedures;
- compares these estimators across repeated simulated datasets;
- separately varies biopsy/inspection frequency and compares observed-data metrics with the exact-event reference.

They summarize per-model metric error primarily through bias/variability/RMSE rather than wrong-winner probability. That distinction is real but not, by itself, a sufficient contribution: their design already produces the oracle and observed score vectors required to calculate OF-35's proposed ranking summaries.

**Consequence:** a cross-method “how often does the winner flip?” benchmark would be a secondary transformation of a very recent direct simulation unless it is accompanied by a genuinely new theorem, identification result, sensitivity analysis or decision rule.

### 3.3 Bahrini et al. — R189

The 2026 ICML paper *When Can We Trust Survival Model Evaluation?* is the decisive conceptual ancestor. It uses controlled semi-synthetic data with known true event times, imposes different right-censoring rates/mechanisms, evaluates the same trained models under standard censored-data metrics and oracle exact-event-time metrics, and studies both **metric bias and preservation of model ranking**.

Its official implementation states that the standard-versus-`true_time` gap is used to isolate distortion in metric values and model rankings and reports fragility of top-1 “best model” conclusions as censoring increases.

**Consequence:** the broad research sentence “does censoring make evaluation choose the wrong survival model relative to an oracle?” is already a current research contribution. Interval censoring can support a new paper only if its recurrent inspection/partial-observation structure yields a nontrivial result that is not a censoring-type substitution.

### 3.4 Yanagisawa & Akiyama — R190

The 2026 ICML paper *A Strictly Proper Scoring Rule and a Calibration Metric for Interval-Censored Data Analysis* directly enters the theoretical interval-censoring evaluation frontier. Its abstract studies the relationship between independent monitoring and non-informative censoring, distinguishes Case-1 from Case-K interval censoring, and proposes a strictly proper score under a stated assumption plus a calibration metric under non-informative censoring.

Strict propriety does **not** automatically imply preservation of every pairwise ranking produced by a different exact-event-time score. Nevertheless, this paper occupies the theoretical question of when interval-censored observed-data scoring is statistically valid and how monitoring assumptions matter.

**Consequence:** “derive a theoretically valid score under interval censoring” and “the inspection assumptions themselves are unexplored” are not safe residual claims.

### 3.5 Informative case-K model selection — R191–R192

Cheng, Wang & Wang develop semiparametric model averaging prediction for **informatively interval-censored case-K data**, construct multiple candidate joint models, compare their method with information-criterion/model-selection alternatives, and establish asymptotic optimality of the weights under conditions [R191]. Du & Zhao develop simultaneous variable selection and estimation under informative case-K interval censoring and explicitly model/assess informativeness [R192].

These papers are not evaluation-metric papers, but they matter for competitive geometry: the narrower escape route “model choice under informative interval censoring” already has an active methodological literature.

## 4. Why wrong-winner probability is not enough

Orient a performance measure so that larger values are better. For two prediction models, define the oracle gap

`Delta* = U*(M_a) - U*(M_b)`

and, for observed-data evaluation procedure `j`,

`Delta_j = U_j(M_a) - U_j(M_b) = Delta* + E_j`,

where

`E_j = [U_j(M_a)-U*(M_a)] - [U_j(M_b)-U*(M_b)]`

is the **differential evaluation error** between the two models.

A ranking reversal is simply

`I(Delta* × Delta_j < 0)`.

For `Delta* > 0`, its probability is

`P(E_j < -Delta*)`.

For two models, selection regret is therefore

`|Delta*| × I(Delta* × Delta_j < 0)`.

This decomposition is useful, but it exposes the novelty problem. Once a study already simulates `U*(M)` and `U_j(M)` for several competing models, wrong-winner probability is primarily a tail summary of differential metric error. A new paper needs new scientific content about the distribution, identification, bounds, guarantees or control of `E_j`; merely reporting the indicator does not create a distinct method.

## 5. Gate-by-gate result

| OF-35 gate | Result | Reason |
|---|---|---|
| Direct nearest-neighbor | **FAIL / near-direct occupation** | Yang et al. already use multiple models + exact-event oracle + observed interval-censored metrics [R183]; Bahrini et al. directly study oracle ranking preservation under censoring [R189]. |
| Distinct interval-censoring mechanism | **NOT ESTABLISHED** | Case-K monitoring does have special structure, but current theory already studies monitoring assumptions/proper scoring [R190], while informative case-K inference/model choice is active [R191–R192]. No first-project-scale distinct theorem has yet emerged. |
| Estimand | **PASS BUT DERIVATIVE** | Wrong-winner probability and regret are interpretable, but are direct functions of differential score error; this alone is insufficient novelty. |
| Bounded design | **PASS** | A small oracle simulation is feasible, and Yang/Bahrini effectively demonstrate the design template. |
| Public/open path | **PASS** | R189 provides public code/data structure; multiple interval-censored software/data substrates also exist. |
| Decision consequence | **PASS IN PRINCIPLE** | Ranking instability can change “best model” conclusions, but this consequence is already central in R189. |

Because the two scientific novelty gates fail or remain unestablished, the candidate is not promoted.

## 6. Why no toy simulation was run

The reconnaissance authorized a toy simulation only **if needed to decide whether the ranking effect could be nontrivial**. The literature now answers that question affirmatively: censoring can distort model rankings [R189], and Yang et al. already provide the interval-censoring oracle-versus-observed ingredients [R183].

Running a small simulation at this stage would therefore demonstrate plausibility, not novelty. Under the project protocol, computation should not be used to rescue a failed novelty gate.

## 7. Residual seam — preserve, do not promote

A narrower question remains intellectually legitimate:

> **How sensitive is the identity of the preferred prediction model to violations of the monitoring/assessment assumptions required for interval-censored evaluation, especially under genuinely informative Case-K observation?**

A stronger statistical version might seek a sensitivity region, partial-order/partial-identification result, or bound on model-ranking conclusions as the assessment mechanism departs from non-informative assumptions.

This is recorded as **OF-38 — WATCHLIST / THEORY-HEAVY**, not as C011, because:

- informative interval-censoring regression, variable selection and model averaging are already active [R191–R192];
- interval-censored scoring validity and monitoring assumptions are now active at ICML 2026 [R190];
- a credible result may require identification/sensitivity theory substantially deeper than the student-scale first project currently sought.

Reopen OF-38 only if a sharply parameterized sensitivity model yields a tractable bound or decision rule not already implied by the existing informative-censoring literature.

## 8. Program consequence

1. **Park OF-35 in its current form.** Do not create C011.
2. Preserve ranking reliability as a general lesson and evaluation lens, not as a novelty claim.
3. Preserve OF-38 as a watchlist-only residual.
4. Return to **review-first cross-field opportunity generation**, with an added hard constraint: search the problem sentence (“oracle vs observed evaluation; model ranking; best-model consistency”) across adjacent censoring types and ML/statistics venues before treating a mechanism substitution as an opportunity.
5. Synthetic-data inference remains a high-competition watchlist; it does not automatically become the next lead.

## 9. Evidence discipline

This prosecution uses three evidence levels:

- **Primary/current direct evidence:** R182–R183 and R191–R192 are peer-reviewed methodological papers; R189 has an official ICML implementation and OpenReview identifier; R190 is an accepted ICML 2026 paper whose abstract/author listings were available during prosecution.
- **Inference:** the claim that wrong-winner probability alone is derivative follows from the differential-error decomposition above and from the fact that R183 already supplies model-specific oracle and observed scores.
- **Unresolved:** no claim is made that R190 proves pairwise equivalence between its observed-data score ranking and every exact-event-time scoring rule; its role is competitive/theoretical occupation, not an exact theorem match.

## 10. Final classification

**OF-35 — PARKED / NO-GO FOR FIRST PROJECT**  
**C011 — UNASSIGNED**  
**OF-38 — WATCHLIST / THEORY-HEAVY RESIDUAL**
