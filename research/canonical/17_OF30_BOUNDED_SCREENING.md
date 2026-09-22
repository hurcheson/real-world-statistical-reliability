---
title: OF-30 Bounded Screening — Finite-Benchmark Certification / Benchmark-to-Target Transportability
version: 0.1.0
last_updated: 2026-09-07
status: completed
---

# OF-30 Bounded Screening

## 1. Purpose

D020 advanced **OF-30 — finite-benchmark certification / benchmark-to-target transportability** to PRIORITY SCREENING while deliberately leaving C011 unassigned.

The bounded gate asked only three questions:

1. Does direct nearest-neighbor literature already own the core benchmark-to-unseen-outcome quality-certification problem?
2. Do Pew/NCHS substrates support scientifically credible held-out or leave-domain-out validation?
3. Can the theory produce a nontrivial identification/bound/design result beyond a discrepancy decomposition, existing survey bias indicators/function-class balance bounds, and standard predictive validation?

**Final disposition:** **PARKED AFTER BOUNDED SCREENING — NO C011.**

The empirical problem is real and the data are usable, but the methodological contribution does not currently clear the project's novelty/theory gate.

# 2. Original OF-30 question

> When does low observed bias on a finite benchmark set legitimately certify low bias for unbenchmarked target outcomes, and how should benchmark sets be chosen to minimize false certification?

The motivating quality claim can be represented as a certificate based on benchmark quality `Q_B` and a target failure event based on held-out target quality `Q_T`:

`false-certification risk = Pr(Q_T > tau_T | Q_B <= tau_B)`.

This remains a useful diagnostic object. The screening result is that turning it into a new general statistical method requires assumptions that pull the problem into already-developed theory classes.

# 3. Gate 1 — direct nearest-neighbor prosecution

## 3.1 R-indicators are a close conceptual ancestor

Schouten, Cobben and Bethlehem introduced R-indicators as single survey-level indicators intended to reflect potential nonresponse bias rather than response rate alone [R161]. Their theory explicitly connects representativeness to worst-case/maximal bias for survey items.

Shlomo, Skinner and Schouten further developed estimation of the R-indicator and explicitly recognized the tension central to OF-30: nonresponse bias is defined for a **specific population parameter / survey variable**, while a survey organization may still desire a single survey-level quality indicator [R162].

Roberts, Vandenplas and Herzing then directly validated whether an R-indicator estimated from auxiliary data is informative about bias in **other survey variables**. They conclude that more apparent bias in auxiliaries does not automatically imply more bias in target variables, and adjustment on the former does not necessarily reduce bias in the latter [R163].

This does not exactly equal OF-30: R-indicators are propensity/auxiliary-based rather than finite external-outcome-benchmark scores. But it substantially weakens any broad novelty claim that “a survey-level quality signal may fail to transport to target variables.” That question is already explicit in survey methodology.

## 3.2 Outcome-specific selection-bias measures occupy the opposite response

Little, West, Boonstra and Hu emphasize that selection-bias risk depends on the relation between the selection mechanism and the survey outcome, and criticize survey-level indicators that are agnostic to the specific outcome [R164]. Their standardized measure of unadjusted bias is outcome-specific and uses a sensitivity parameter for nonignorable sample selection.

Therefore, a proposed OF-30 solution that simply says “make the quality certificate outcome-specific” also has mature ancestors.

## 3.3 Function-class bias bounds occupy the natural theorem route

Hartman, Hazlett and Sterbenz's **kpop** develops population weighting that minimizes worst-case approximation bias over a rich outcome-function class using kernel balance [R165]. More generally, calibration/balance theory already makes the key move that OF-30 would need for a theorem: restrict the target to a function class and convert observed imbalance into a bound on target bias.

The baseline OF-30 decomposition

`B(f)=beta^T B(G)+B(r)`

is therefore an identification warning, not a new theorem. If `r` is unrestricted, no finite benchmark certificate controls `B(f)`. If `r` is restricted by a norm/function class, the problem moves toward existing balance/IPM/RKHS/worst-case-bias theory.

## 3.4 Generic benchmark-subset prediction is now an active cross-field problem

Smola's 2026 **Submodular Benchmark Selection** formalizes selection of a small informative benchmark subset to predict remaining benchmark performance using covariance, entropy and mutual information, with held-out validation [R168]. The application is LLM evaluation rather than survey quality, so it is not a direct survey-method duplicate. It nevertheless crowds any generic “choose a small set of benchmarks that predicts the rest” contribution.

## Gate-1 verdict

**PARTIAL SURVIVAL, HEAVILY NARROWED.**

No exact survey paper was found that packages external outcome benchmarks into the precise OF-30 false-certification object. But the broad intellectual ingredients are already explicit:

- survey-level quality indicators versus statistic-level bias [R161–R164];
- worst-case target-bias bounds under function-class restrictions [R161, R165];
- empirical validation of whether a quality indicator predicts bias in other variables [R163];
- benchmark-subset selection/prediction under covariance structure [R168].

Any viable residual would have to be much sharper than “benchmarks may not generalize” or “select representative benchmarks.”

# 4. Gate 2 — held-out benchmark feasibility

## 4.1 Pew 2021 benchmarking study

Pew's six-source comparison evaluates three probability-based panels and three opt-in sources on **28 benchmark variables / 77 categories** spanning voting, health, work, family and living situations [R152]. Pew itself warns that relative sample accuracy could differ under a different benchmark set [R169].

This is sufficient for a preliminary benchmark-set-instability experiment. However, the 28 variables should **not** be treated as 28 independent draws from an outcome population. Variables share domains, benchmark sources, constructs and selection/measurement mechanisms. Random item holdout would therefore overstate effective validation sample size.

A scientifically stronger design is **leave-domain-out** or grouped holdout, with any variables mechanically enforced by weighting/calibration excluded from the certification target set.

## 4.2 NCHS Rapid Surveys System

The NCHS RSS provides an even richer official-statistics validation environment. The Round 7 quality profile evaluates **53 benchmark variables** against 2025 Quarter 1 NHIS and reports bias by health domain [R166]. It also states that 11 variables producing 28 control totals were used in NHIS calibration before benchmarking [R166].

This creates an important nesting constraint: variables used to construct/tune weights cannot simultaneously count as independent evidence that the resulting survey “certifies.” A valid design must separate:

1. calibration/tuning variables;
2. certificate variables used to choose/score a quality rule; and
3. final held-out benchmark domains used only for validation.

NCHS's domain organization makes grouped holdout plausible. Cross-round replication is also possible, but differences in question content, benchmark years, provider composition and weighting strategy mean rounds cannot be treated as simple exchangeable replications.

## Gate-2 verdict

**PASS, WITH DESIGN RESTRICTIONS.**

A credible empirical study can be built from existing public/obtainable substrates. The strongest unit of validation is an **outcome domain**, not an individual benchmark item. This reduces effective sample size but does not make the analysis impossible.

The data gate therefore does **not** kill OF-30.

# 5. Gate 3 — theory and decision differentiation

This is the decisive gate.

## 5.1 Impossibility without an outcome-link assumption

Let `G=(g_1,...,g_K)` denote benchmark outcomes whose population discrepancies are known and let `f` be an unbenchmarked target.

Without a restriction linking `f` to `G`, there is no nontrivial universal implication

`small B(G) => small B(f)`.

Even exact benchmark agreement can coexist with arbitrarily large target discrepancy on a target component orthogonal/unrelated to the benchmark class. This is a useful warning but is elementary.

## 5.2 Every natural repair enters an occupied theory class

A guarantee requires adding structure. The most natural structures map to existing methods:

### A. Target lies near the benchmark span / a smooth function class

Then the guarantee is a balance/function-class approximation-bias bound. This is the territory of calibration, worst-case bias and kernel balancing [R161, R165].

### B. Benchmark and target outcomes are exchangeable draws from an outcome superpopulation

Then certificate validity becomes a predictive-generalization / hierarchical-model / concentration problem. The novelty resides almost entirely in defining and defending the outcome superpopulation, not in new probability theory.

### C. Outcomes have an estimable covariance or latent-factor structure

Then selecting informative benchmarks and predicting unobserved performance becomes multivariate subset selection/imputation, now directly active in benchmark-selection research [R168].

### D. Selection propensity or nonignorability is modeled directly

Then the problem becomes outcome-specific nonresponse/selection-bias assessment, represented by R-indicator descendants, FMI-like measures and SMUB/sensitivity approaches [R163–R164].

## 5.3 The remaining empirical contribution is useful but not first-project strong

A nested leave-domain-out study could quantify how often provider or weighting-method rankings change under benchmark-set choice and estimate empirical false-certification rates. That would be useful evidence and could support a methods/practice note.

But at present it would mainly instantiate familiar validation ideas in a survey-benchmarking setting rather than establish a new identification theorem, estimator or decision theory. Under the Charter's first-project standard, that is insufficient for promotion.

## Gate-3 verdict

**FAIL.**

The broad OF-30 theory either remains an elementary impossibility statement or becomes a special case/application of existing outcome-specific bias, function-class balance, hierarchical prediction or benchmark-subset-selection theory.

# 6. Overall decision matrix

| Gate | Result | Consequence |
|---|---|---|
| Direct nearest-neighbor novelty | PARTIAL / HEAVILY CROWDED | Exact packaging not found, but core survey-level-vs-statistic-level issue and bias-risk theory are established. |
| Held-out empirical feasibility | PASS | Pew/NCHS support grouped/nested validation if calibration variables and domains are handled correctly. |
| Nontrivial theory/decision differentiation | **FAIL** | Natural theorem routes collapse into existing bias-bound/function-class or predictive-validation theory. |

# 7. Disposition

**OF-30 is PARKED AFTER BOUNDED SCREENING.**

**C011 remains unassigned.**

This is not a claim that the empirical question is unimportant. It is a first-project selection decision: the data and decision channel are strong, but the methodological novelty/theory channel is not strong enough to justify promotion.

OF-31 (adaptive benchmark reuse / quality-assessment overfitting) is also not promoted independently; its core correction is nested/held-out validation and is too close to generic post-selection validation.

# 8. What is preserved

The screening produces reusable program knowledge:

1. **Survey-level quality is not automatically statistic-level reliability.** This is established survey-methodology territory and should be treated as a prior-art constraint, not a gap claim.
2. **Benchmark validation must be nested.** Any outcome used to calibrate/tune/select a method cannot be counted as independent evidence that the method generalizes.
3. **Hold out domains, not merely items.** Correlated benchmark items create pseudo-replication if randomly split.
4. **A benchmark certificate requires an explicit outcome universe.** Without a defensible target class, outcome superpopulation or covariance structure, “certification” is not identified.
5. **Do not claim novelty from the elementary benchmark-residual decomposition.** It is useful exposition only.

# 9. Reopening conditions

OF-30 should be reopened only if at least one of the following appears:

- a genuinely survey-specific identification structure under which a finite external-outcome benchmark set yields a new, nontrivial guarantee for unbenchmarked estimands;
- a large multi-study benchmark matrix with enough independent outcome domains to support a new estimable outcome-transport law rather than an illustrative cross-validation exercise;
- a regulatory/official-statistics release decision whose loss function creates a new selective-inference/decision problem not reducible to standard validation;
- evidence that existing R-indicator/outcome-specific-bias/function-class approaches cannot express the observed benchmark-to-target failure mode.

# 10. Program consequence

The next scientific move returns to **fresh four-channel opportunity generation inside D013**, again without forcing C011.

Add the OF-30 failure mode to the hard constraints:

> Do not promote generic survey-level “quality certification,” representative-benchmark selection, or benchmark-to-unseen-outcome generalization unless the proposed structure yields a genuinely new outcome-specific identification/decision result beyond R-indicators, outcome-specific selection-bias measures, function-class balance bounds, and generic benchmark-subset prediction.

# 11. References added by this screening

See R161–R169 in `11_REFERENCE_LEDGER.md`.
