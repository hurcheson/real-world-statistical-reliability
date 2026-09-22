---
title: C010 — Selection-Aware Response-Quality Filtering in Nonprobability Survey Inference
version: 0.1.0
last_updated: 2026-09-07
status: parked-no-go-first-project
---

# C010 — Selection-Aware Response-Quality Filtering in Nonprobability Survey Inference

## Purpose

This file records the screening/prosecution of the candidate generated from OF-24:

> **When an analyst removes respondents flagged as low-quality, careless, satisficing or bogus from a nonprobability survey and then reweights/recalibrates the retained cases, when does filtering reduce population-estimation error versus create additional selection bias?**

The prosecution uses the program's expanded **four-channel discovery protocol**: literature-generated, theory-generated, data-generated and decision-generated opportunity discovery. It applies the same collapse-first standard used for C009: search first for the strongest existing result that would make the proposed contribution unnecessary or derivative.

The candidate is deliberately narrower than generic survey fraud, bot detection, careless responding, or total-survey-error research. Its inferential object is the interaction between:

1. original nonprobability participation;
2. an imperfect response-quality screen;
3. exclusion/retention induced by that screen; and
4. population adjustment after filtering.

---

# 1. Final prosecution verdict

**C010 status: PARKED / NO-GO FOR FIRST PROJECT.**

The scientific problem is real and consequential, but the candidate does not currently clear the program's first-project distinctiveness and identification gates.

The broad claim fails directly: existing work already demonstrates that removing respondents flagged for satisficing **before recalculating weights** can reduce bias in nonprobability online panels [R127]. Contemporary Pew and Gallup evidence also shows that quality-screening rules can materially alter survey estimates and respondent composition, sometimes improving some quality metrics while worsening substantive benchmark error [R129–R131].

The narrowed statistical object survives conceptually:

> Treat response-quality filtering as a **second selection mechanism** layered on top of nonprobability participation, with an imperfect classifier whose false-positive and false-negative behavior may be outcome- and covariate-dependent.

However, the remaining pieces are strongly adjacent to established methods:

- exclusion after attention checks can induce selection bias, and formal conditions for valid exclusion plus covariate adjustment already exist [R128];
- joint measurement-error and representativeness problems in nonprobability surveys are now directly studied [R125–R126];
- careless-response detection/cleaning is a mature methodological literature [R135–R138]; and
- when no gold-standard respondent-quality label exists, sensitivity/specificity are themselves latent and require strong latent-class assumptions, validation information or partial-identification logic [R141; see also R121].

The residual contribution would therefore need to be more than a decomposition or a generic sensitivity analysis. It would need a genuinely new identification, partial-identification, or decision-theoretic result exploiting the **post-filter recalibration structure** in a way not reducible to existing selection-bias, measurement-error, calibration, or no-gold-standard classification machinery.

No such result was established in this prosecution.

---

# 2. Candidate definition

## 2.1 Broad candidate rejected

A broad C010 such as

> “Can removing bad respondents improve nonprobability survey estimates after weighting?”

is not viable as a novelty claim.

Slamowicz et al. [R127] compare one probability online panel with four nonprobability online panels, identify satisficing using multiple indicators, remove flagged cases and **recalculate calibration weights on the retained cases**. Their empirical result is directly in the proposed lane: exclusion plus weighting reduced average absolute bias across all four nonprobability panels more than weighting alone. The paper explicitly frames the contribution as combining selection-error adjustment with removal of satisficing-related measurement error.

The generic empirical proposition is therefore occupied.

## 2.2 Narrowed candidate prosecuted

The strongest surviving formulation is:

> **Selection-aware response-quality filtering in nonprobability survey inference:** characterize when excluding respondents according to an imperfect response-quality screen before population calibration reduces versus increases total population-estimation error, accounting explicitly for false-positive exclusion, false-negative retention, and the filter-induced change in the effective participation mechanism.

This version asks not merely whether filtering can help, but **when it helps, when it harms, what is identifiable, and what information is needed to choose a filtering threshold.**

---

# 3. Four-channel discovery result

## 3.1 Channel 1 — Literature-generated

### Signal

The literature strongly confirms that the interface matters, but it also substantially occupies the obvious contribution.

Key evidence:

- Kennedy, Mercer & Lau [R125] show that selection-adjustment theory for commercial nonprobability samples relies on an implicit response-accuracy assumption and argue that bogus responding must be addressed alongside representativeness.
- Sen & Lahiri [R126] directly develop methodology for measurement error and representativeness in nonprobability surveys.
- Slamowicz et al. [R127] explicitly combine satisficer exclusion with recalculated weighting and show bias reduction across four nonprobability panels.
- Mathur [R128] formalizes attention checks as measurement-error indicators and shows that exclusion can induce selection bias; the paper gives conditions and covariate-adjusted alternatives.
- Ward & Meade [R136], Stosic et al. [R137], and Freese & Jin [R138] demonstrate that careless responding and online nonprobability sample quality are mature literatures rather than an untouched interface.

### Literature-channel conclusion

**Importance: strong. Novelty of the broad proposal: failed.**

The literature leaves room only for a substantially narrower inferential result about an imperfect screen, post-filter selection, recalibration and threshold choice.

---

## 3.2 Channel 2 — Theory-generated

The theory channel produces a clean decomposition and clarifies the exact failure mechanism.

Let:

- `S=1` denote inclusion/participation in the nonprobability survey;
- `Q` denote latent response validity/quality, where the exact definition is application-specific;
- `C=1` denote passing an observed response-quality screen;
- `X` denote adjustment variables with target-population benchmarks;
- `Y` denote the latent/target response of inferential interest; and
- `Y_tilde` denote the observed response, which may differ from `Y` when response quality is poor.

Suppose the analyst:

1. begins with `S=1` nonprobability respondents;
2. excludes `C=0` cases;
3. calibrates the retained `S=1,C=1` sample to the target distribution of `X`; and
4. estimates the population mean of `Y` using the weighted observed response `Y_tilde`.

Under ideal calibration to the target `X` distribution, the post-filter estimand is approximately

\[
\mu_C = E_X\{E(\widetilde Y\mid X,S=1,C=1)\}.
\]

For the target mean

\[
\mu=E(Y),
\]

add and subtract `E(Y | X,S=1,C=1)` to obtain

\[
\mu_C-\mu
=
E_X\{E(\widetilde Y-Y\mid X,S=1,C=1)\}
+
E_X\{E(Y\mid X,S=1,C=1)-E(Y\mid X)\}.
\]

This separates two post-filter errors:

1. **retained-response contamination** — measurement error among cases that pass the screen, including false negatives; and
2. **residual retained-sample selection** — the difference between the target outcome distribution and the outcome distribution among `S=1,C=1` cases conditional on `X`.

The second term contains both the original nonprobability participation mechanism and the additional selection induced by the quality screen. A false-positive exclusion is inferentially harmless only under conditions strong enough to preserve the target outcome distribution after conditioning on `X`; otherwise removing a valid respondent can change representativeness.

### Immediate implication

Recalibration on `X` after filtering does **not** automatically repair filter-induced selection. It succeeds only when the retained sample is sufficiently exchangeable for the target conditional on the calibration information and when retained response error is negligible/mean-zero at the relevant level.

### Threshold form

If a screen uses threshold `t`, the relevant decision is not “maximize classification accuracy” in isolation. It is closer to

\[
\operatorname{MSE}(t)=\operatorname{Bias}(t)^2+\operatorname{Var}(t),
\]

where tightening `t` may:

- reduce retained-response contamination;
- increase false-positive exclusion and therefore selection bias;
- reduce effective sample size;
- increase weight variability after recalibration; and
- alter subgroup support/overlap.

Thus an inferentially optimal threshold need not equal a classification-optimal threshold.

### Theory-channel conclusion

**Mechanism: clear and useful. Novelty: not established.**

The decomposition is a useful canonical lemma, but it is assembled from familiar measurement-error and selection logic. By itself it is not enough to support a first paper.

---

## 3.3 Channel 3 — Data-generated

Empirical evidence strongly supports a real filtering/selection tradeoff.

### Pew 2026

Pew's 2026 opt-in study [R129–R130] used 11,114 U.S. adults and evaluated three screening approaches: trap questions, CloudResearch Sentry prescreening and voter-file matching. The retained samples differed sharply in size. Pew found that purging cases generally improved some data-quality metrics, yet voter-file matching could **increase error by removing mostly valid respondents**, while all three approaches modestly worsened the Harris-vote overestimate in the application studied.

This is almost exactly the empirical anomaly C010 would need to explain: a screen can look defensible as a data-quality intervention yet worsen a population estimate because the removed and retained cases are not inferentially neutral.

### Gallup 2024

Gallup [R131] compared several exclusion thresholds across six opt-in providers. Stringent rules removed roughly 44%–46% of the sample but produced only modest changes in benchmark accuracy. This shows a practical threshold problem: much more aggressive filtering need not yield commensurate inferential improvement.

### Francois 2026

Francois [R132] reports systematic variation in attention-check performance across respondent characteristics and evaluates how filtering changes quality-of-life conclusions. This reinforces the possibility that a quality screen changes sample composition in outcome-relevant ways.

### Earlier Pew public data

Pew's 2020 bogus-respondent study [R133–R134] includes more than 60,000 interviews across six online sources and has a downloadable dataset after Pew account access. It is a feasible empirical substrate for reproducing subgroup composition and screening effects, though it does not provide a perfect latent gold-standard quality label.

### Data-channel conclusion

**Phenomenon: strongly supported. Feasibility for illustration: good. Feasibility for identifying false-positive/false-negative operating characteristics: weak to moderate.**

Available public data can show that screening changes estimates and composition. They generally cannot reveal the true counterfactual response each excluded case would have given under full attention/good faith, so the central classifier-error parameters remain only partially anchored.

---

## 3.4 Channel 4 — Decision-generated

There is a concrete analyst/agency decision:

> Given one or more quality signals, which cases should be excluded before weighting, and how aggressive should the threshold be if the inferential target is a population estimand rather than classifier performance?

This is not an abstract methodological choice. AAPOR's online-sample guidance [R139], current fraud-detection activity [R140], Pew's current methods program [R129–R130] and Gallup's threshold experiments [R131] all demonstrate operational demand.

A decision-relevant method would need to tell an analyst one of the following:

- whether a proposed screen is safe enough to use;
- whether a stricter threshold improves or worsens target MSE;
- which covariates must enter post-filter adjustment;
- when the data are too weak to justify hard deletion;
- when sensitivity analysis should replace a single cleaned estimate; or
- when soft weighting/imputation/robust estimation should replace binary exclusion.

### Decision-channel conclusion

**Decision importance: high. Existing decision rule: incomplete.**

This is the strongest reason not to kill the scientific question. But the decision problem alone does not supply novelty; C010 still needs an identifiable or sharply sensitivity-analyzable object.

---

# 4. Convergence across channels

All four channels converge on the same substantive fact:

> **Response-quality cleaning in a nonprobability survey is an inferential intervention, not merely a preprocessing operation.**

The convergence increases confidence that the problem matters, consistent with L038. It does **not** increase confidence that the broad research claim is novel.

The channels also expose the same bottleneck from different directions:

- literature: direct nearest neighbors already exist;
- theory: filtering creates a second selection event;
- data: filters remove different demographic/outcome-relevant cases and can reverse the direction of accuracy gains;
- decision: analysts need a threshold rule but usually lack true quality labels.

The residual research problem is therefore the intersection of **selection-aware threshold choice** and **no-gold-standard screen uncertainty**.

---

# 5. What recalibration can and cannot repair

## Recalibration can repair

If filtering changes only the marginal distribution of observed adjustment variables `X`, and if within levels of `X` the retained respondents remain representative of the target outcome distribution and their observed responses are valid, recalibration to population `X` benchmarks can repair the induced imbalance.

## Recalibration cannot automatically repair

Recalibration does not solve the problem when:

- pass/fail status depends on latent factors related to `Y` after conditioning on `X`;
- the screen differentially excludes valid cases within `X` strata;
- invalid cases that remain have outcome-dependent response error;
- the screen itself uses variables downstream of or mechanically related to the outcome;
- the post-filter sample loses support/overlap for important target subgroups; or
- calibration variables are too coarse to represent the dimensions along which filtering changes the sample.

This is the precise inferential distinction C010 would need to operationalize.

---

# 6. False positives and false negatives are not symmetric

Let latent `Q=1` indicate a response that is sufficiently valid for the target analysis.

- **False negative of the screen:** `Q=0,C=1` — an invalid/problematic response remains. This contributes primarily to retained-response contamination, though its distribution may also interact with selection.
- **False positive of the screen:** `Q=1,C=0` — a valid response is removed. This contributes no direct response contamination after removal, but it can worsen representativeness and variance.

The inferential costs depend on more than sensitivity and specificity:

- how `Q` relates to `Y`;
- how classifier errors vary with `X`;
- how the original participation mechanism `S` relates to `Q` and `Y`;
- how much weight recalibration places on the remaining cases; and
- which estimand is being targeted.

Therefore two screens with the same overall sensitivity/specificity can have different population-estimation consequences.

This is potentially the most promising theoretical seam, but it was not enough in the current prosecution to establish a distinct new result.

---

# 7. Identification and the no-gold-standard problem

A central obstacle is that `Q` is rarely observed.

Pew explicitly notes that for most survey answers there is no direct way to know whether the respondent answered truthfully [R129]. A screen can therefore be evaluated against proxy quality metrics or external benchmarks without revealing the true respondent-level false-positive and false-negative rates.

With one imperfect screen and no validation labels, the distribution of latent `Q` and the screen's operating characteristics are not generally identified without additional assumptions.

Possible information regimes include:

1. **Gold-standard/adjudicated validation subset** — strongest route; can identify or estimate screen operating characteristics under validation-sampling assumptions.
2. **Multiple imperfect screens** — latent-class models may identify parameters under strong conditional-independence and population-structure assumptions, but robustness is a known concern [R141].
3. **External sensitivity/specificity bounds** — can support partial identification/sensitivity analysis, but generic bounded-misclassification machinery already exists [R121].
4. **Outcome/benchmark-only validation** — can compare aggregate inferential performance across thresholds but may not identify why a filter helps or harms.

The key prosecution result is negative but important:

> “No gold standard” cannot itself be sold as the novelty. It is a mature statistical problem. C010 would need to exploit special survey-calibration structure to obtain tighter identification, bounds, or decision rules than generic latent-class/misclassification methods provide.

---

# 8. Nearest-neighbor matrix

| Reference | Main object | What it already covers | Residual space left for C010 |
|---|---|---|---|
| R127 — Slamowicz et al. | Satisficer exclusion + weighting in P/NPP panels | Direct empirical filter-before-reweighting bias reduction | General rule for when filtering helps/hurts; imperfect-classifier sensitivity; theory |
| R128 — Mathur | Attention-check exclusion | Formal selection-bias conditions and covariate adjustment | Nonprobability population weighting/calibration and threshold decision |
| R126 — Sen & Lahiri | Measurement error + representativeness in NPS | Joint measurement/sampling-error correction | Specific post-filter classifier/selection mechanism |
| R125 — Kennedy et al. | Bogus response + NPS benchmarking | Demonstrates response error cannot be ignored alongside selection | Formal selection-aware filter decision |
| R129–R130 — Pew 2026 | Three quality screens in opt-in polling | Real false-positive-like removal and outcome reversals; recalculated weights | General inferential theory/identification |
| R131 — Gallup | Exclusion-threshold comparison | Real threshold/composition tradeoff | Formal target-MSE rule |
| R136–R138 | Careless response / NPS reviews | Mature detection/cleaning landscape | P/NPS calibration-specific inference only |
| R141 / R121 | No-gold-standard test accuracy / partial ID | Generic latent classifier uncertainty and bounded misclassification | Special structure exploiting survey calibration/benchmarks |

### Nearest-neighbor conclusion

No single reference fully subsumes the exact narrowed C010 statement. But the residual space is the **intersection of several mature literatures**, so the novelty burden is high. A paper that simply combines them procedurally would be vulnerable to the “composition of known methods” critique.

---

# 9. Data feasibility

## Strongest public substrate found

**Pew 2020 bogus-respondent dataset [R133–R134].**

Advantages:

- large sample (>60,000 interviews);
- multiple online source types;
- explicit quality flags/behaviors;
- externally benchmarkable survey estimates;
- public download after Pew account access.

Limitations:

- quality status remains operational rather than a universal latent gold standard;
- the data were not designed to identify a complete screen confusion matrix for every quality criterion;
- threshold experiments can be reproduced, but causal attribution to false-positive versus false-negative error is limited.

## High-value but not openly reusable substrate

Slamowicz et al. [R127] is directly aligned but states that underlying data cannot be shared publicly because of privacy/commercial considerations; replication requests may be made to the corresponding author.

## Current empirical evidence without confirmed public microdata

Pew 2026 [R129–R130] is exceptionally relevant and recent, but the report currently provides report materials rather than an obvious public respondent-level dataset suitable for full methodological development.

Gallup's study [R131] is methodologically informative but is not presented as a public analysis dataset.

### Feasibility verdict

**Moderate for empirical illustration; weak-to-moderate for the key latent-classifier identification problem.**

This is not a compute problem. It is an information problem.

---

# 10. Competition and active-work assessment

The candidate sits near several active clusters:

- **Pew Research Center Methods** — direct 2020, 2024 and August 2026 work on bogus responding and opt-in polling [R125, R129–R130, R133].
- **Social Research Centre (Australia)** — direct satisficer-exclusion + recalibration study [R127].
- **Maryland / Sen-Lahiri** — direct 2026 measurement-error + representativeness methodology [R126].
- **Stanford / Mathur** — formal selection-bias analysis of attention-check exclusion [R128].
- **Gallup Methodology** — applied threshold/filtering experiments [R131].
- **AAPOR / survey-research community** — active guidance and 2026 fraud-detection programming [R139–R140].

Competition is therefore **moderate-high to high** for the broad problem. The narrower post-filter-calibration decision rule is less directly occupied, but it touches mature theory on all sides.

---

# 11. Charter-gate assessment

| Gate | Assessment | Rationale |
|---|---|---|
| Importance | **PASS** | Opt-in survey quality and representativeness are real, current problems with substantive consequences. |
| Clear estimand/failure mode | **PASS** | Population mean/estimand after `S` participation, `C` filtering and recalibration can be stated precisely. |
| Literature distinctiveness | **FAIL / weak** | Direct empirical and methodological neighbors occupy most broad claims. |
| Identification | **WEAK** | Latent response quality and screen FP/FN rates are not generally identified without validation or strong assumptions. |
| Decision consequence | **PASS** | Analysts must choose whether/how aggressively to filter before weighting. |
| Public-data feasibility | **MODERATE** | Pew 2020 supports illustration; strongest direct datasets are not all publicly reusable. |
| Compute feasibility | **PASS** | Analytic derivation, moderate simulation and survey reweighting are workstation-scale. |
| Scope for first project | **PASS in size, FAIL in distinctiveness** | Technically bounded, but residual novelty is too thin/uncertain. |
| Competition | **MODERATE-HIGH / HIGH** | Multiple current academic and practitioner groups are active. |
| Audience | **PASS** | JSSAM, POQ, Survey Methodology, AAPOR and applied survey organizations are obvious audiences. |

**Overall:** no promotion.

---

# 12. What survives from C010

Even though C010 is parked, two program assets should be retained.

## 12.1 Reusable inferential lemma

After filtering and ideal calibration on `X`, error can be organized as

\[
\text{post-filter error}
=
\text{retained response contamination}
+
\text{residual selection among retained cases}.
\]

This prevents future work from treating data-quality deletion as inferentially neutral preprocessing.

## 12.2 Reusable threshold principle

A response-quality threshold should be judged against the **target estimand's MSE/robustness**, not only respondent-level classification accuracy. More aggressive deletion can simultaneously reduce contamination, increase selection bias, degrade overlap and inflate variance.

These are principles, not yet a standalone paper contribution.

---

# 13. Reopening conditions

Reopen C010 only if at least one of the following materially changes the evidence base:

1. **Validation data appear:** a public or accessible nonprobability survey contains credible adjudicated/gold-standard respondent-quality labels, multiple screen scores, population benchmarks and outcome variables.
2. **A new identification theorem emerges:** post-filter calibration structure yields point identification or materially tighter partial-identification bounds than generic latent-class/misclassification methods.
3. **A decision rule is genuinely new:** an estimand-targeted threshold rule can be derived that remains valid under explicit classifier uncertainty and is not reducible to generic bias-variance tuning.
4. **A defensible validation design is available:** e.g., randomized recontact, verified identity/behavior, intensive adjudication or a probability-based comparator that can anchor key false-positive/false-negative parameters.
5. **A high-stakes official-statistics decision appears:** an agency is actively deciding whether to hard-delete, downweight or retain flagged NPS cases and existing methods do not answer the inferential question.

Absent one of these conditions, C010 should remain parked.

---

# 14. Recommended next scientific action

Do **not** begin a C010 simulation/application program and do not automatically assign C011.

Return to the remaining live opportunity portfolio inside D013 and run a fresh collapse-first comparison of OF-19–OF-23. The next candidate should be promoted only if it survives:

1. direct-prior-art search;
2. identification/estimand check;
3. a concrete decision consequence;
4. public-data or validation feasibility; and
5. a nearest-neighbor comparison demonstrating a contribution that is not merely a composition of established methods.

C010's strongest reusable lesson should be carried forward:

> **A cleaning rule that changes who remains in the analytic sample is part of the selection mechanism and must be analyzed as such.**

---

# 15. C010 search/evidence log

## Literature-generated query families

- nonprobability online panels satisficing exclusion weighting bias
- bogus respondents opt-in polling screening weighting
- attention-check exclusion selection bias
- careless responding exclusion survey representativeness
- nonprobability survey measurement error representativeness

## Theory-generated query families

- post-selection inference after attention-check exclusion
- selection bias induced by filtering/conditioning
- calibration after sample restriction
- measurement error plus selection bias survey weighting

## Data-generated query families

- opt-in panel bogus respondent benchmark study dataset
- quality screen false positives demographic composition
- exclusion threshold benchmark error online survey

## Decision-generated query families

- survey fraud screening guidance AAPOR
- online panel data-quality threshold practice
- hard exclusion versus weighting/imputation careless respondents
- no gold standard respondent quality sensitivity specificity

## Search interpretation

The search was explicitly collapse-first. Positive evidence that the phenomenon exists was not treated as novelty evidence. Direct empirical occupation [R127], formal selection-bias theory [R128], current NPS measurement/representativeness methodology [R126], and mature no-gold-standard machinery [R141/R121] jointly drove the parking decision.

---

## Change log

### 0.1.0 — 2026-09-07

- Created C010 prosecution record from OF-24.
- Executed the four-channel discovery protocol.
- Derived and preserved the post-filter contamination + retained-selection decomposition.
- Recorded direct prior-art collapse of the broad candidate.
- Classified the narrowed candidate **PARKED / NO-GO FOR FIRST PROJECT**.
- Added explicit reopening conditions and next-candidate guidance.
