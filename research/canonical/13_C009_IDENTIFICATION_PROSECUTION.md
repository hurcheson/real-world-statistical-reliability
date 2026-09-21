---
title: C009 Identification, Sensitivity, and Nearest-Neighbor Prosecution
version: 0.2.0
last_updated: 2026-09-07
status: active
---

# C009 Identification, Sensitivity, and Nearest-Neighbor Prosecution

## Purpose

This record executes the promotion gate specified for C009 in `04_CANDIDATE_REGISTRY.md` and `12_SURVEY_DATA_INTEGRATION_FIELD_MAP.md`.

The question prosecuted here is not the broad claim that measurement error can bias weighting. That claim is established. The question is whether a narrower, finite-population probability/nonprobability (P/NPS) object remains:

**Stage-2 update (2026-09-07):** the bounded-mismatch / partial-identification sensitivity gate specified in Section 15 has now been executed. It produces a clean decision map but does **not** justify promotion to `SURVIVES`; the final C009 verdict is **PARKED / NO-GO FOR FIRST PROJECT**. Sections 17 onward contain the stage-2 prosecution and supersede the earlier forward-looking recommendation.

> **When the probability reference and the nonprobability source encode a nominally shared adjustment variable on different measurement scales, can we separate the bias created by calibrating to the wrong-scale benchmark from the residual selection bias caused by using a noisy proxy at all, and what information is needed to identify or sensitivity-analyze those components?**

This document is a research prosecution record, not a manuscript and not a proof of novelty.

---

# 1. Prosecution verdict

## Broad C009 claim

**FAILS AS STATED / MUST BE NARROWED.**

The broad proposition “cross-source measurement mismatch in calibration or propensity variables is an unaddressed problem” is not defensible.

Three prior-art lines are especially important:

1. Chambers studied survey calibration when the available population auxiliary total belongs to a closely related but non-identical variable, including a direct substitution strategy that induced substantial bias in simulation [R113].
2. Hong, Rudolph and Stuart studied differential measurement error in a propensity-score covariate across treatment groups and developed a Bayesian sensitivity/correction framework [R114].
3. Kim and Tam developed finite-population data-integration estimators that explicitly handle measurement error in big-data and probability-sample variables [R115].

McCaffrey, Lockwood and Setodji remain an additional direct ancestor for IPW with error-prone covariates [R089].

Therefore the contribution cannot be “measurement error matters,” “different groups/sources measure X differently,” or “calibration to an erroneous benchmark can be biased.”

## Narrowed C009 claim

**ADVANCE TO PROSECUTION — NARROWED, NOT TO EXECUTION.**

The surviving object is the interaction of:

- a probability reference source that identifies a benchmark on measurement scale A;
- a nonprobability sample whose selection/outcome relationship is governed by a latent adjustment variable;
- source-specific measurement scale B in the NPS;
- calibration/poststratification that incorrectly treats the A benchmark as the target benchmark for B;
- a decomposition separating *benchmark-scale mismatch* from *residual proxy-selection bias*;
- explicit information regimes showing what a bridge sample, known error rates, or a gold-standard validation sample actually identify.

Targeted searches in this prosecution did not surface a paper whose primary inferential object is this exact decomposition in P/NPS integration. This is evidence for continued prosecution, **not evidence of novelty**.

---

# 2. Minimal statistical model

## 2.1 Target

Let the finite population be `U={1,...,N}` and let

\[
\mu_N = \frac{1}{N}\sum_{i\in U}Y_i
\]

be the finite-population mean. For the identification algebra below, use the corresponding population/stochastic notation

\[
\mu = E(Y).
\]

The probability sample `A` is assumed to identify target-population distributions after its design weights are applied. The nonprobability sample `B` is indicated by `R=1`.

## 2.2 Latent adjustment variable and outcome

Begin with one binary latent adjustment variable

\[
X\in\{0,1\}.
\]

Define

\[
p=P(X=1), \qquad p_B=P(X=1\mid R=1),
\]

and outcome means

\[
m_x=E(Y\mid X=x), \qquad x\in\{0,1\}.
\]

Assume, for the toy model only,

\[
Y\perp R\mid X
\]

and positivity. Thus selection may depend on `X`, but conditional outcome means transport from the target population to `B`.

## 2.3 Source-specific measurement

The probability source observes `W_A`; the NPS observes `W_B`. They are not assumed to be the same measurement.

For source `s in {A,B}`, define

\[
a_s=P(W_s=1\mid X=1),\qquad
b_s=P(W_s=0\mid X=0),
\]

with Youden index

\[
J_s=a_s+b_s-1.
\]

For the toy model assume nondifferential measurement conditional on `X`:

\[
W_s\perp(Y,R)\mid X.
\]

The observed target benchmark in source A is

\[
q_A=P(W_A=1)=(1-b_A)+J_Ap.
\]

The observed NPS marginal is

\[
q_B=P(W_B=1\mid R=1)=(1-b_B)+J_Bp_B.
\]

A crucial unobserved quantity is the target-population marginal **on the B measurement scale**:

\[
q_B^P=P(W_B=1)=(1-b_B)+J_Bp.
\]

The ordinary cross-source calibration mistake is to use `q_A` where the relevant B-scale benchmark would be `q_B^P`.

---

# 3. Probability limit of naive binary calibration

Within `B`, define

\[
r_1=P(X=1\mid R=1,W_B=1)=\frac{a_Bp_B}{q_B},
\]

\[
r_0=P(X=1\mid R=1,W_B=0)=\frac{(1-a_B)p_B}{1-q_B}.
\]

Then

\[
E(Y\mid R=1,W_B=w)=m_0+(m_1-m_0)r_w.
\]

Consider binary poststratification/calibration that weights the NPS so that its observed `W_B` marginal equals the probability-source benchmark `q_A`.

Its large-sample target is

\[
\mu_{\text{naive}}
= q_A E(Y\mid R=1,W_B=1)
 +(1-q_A)E(Y\mid R=1,W_B=0),
\]

or

\[
\mu_{\text{naive}}
=m_0+(m_1-m_0)\{q_Ar_1+(1-q_A)r_0\}.
\]

The true target is

\[
\mu=m_0+(m_1-m_0)p.
\]

Therefore

\[
\operatorname{Bias}(\mu_{\text{naive}})
=(m_1-m_0)\{q_Ar_1+(1-q_A)r_0-p\}.
\]

This expression alone is not the contribution; the useful object is the decomposition below.

---

# 4. Two-component bias decomposition

Define the hypothetical estimator that calibrates `B` to the *correct B-scale target benchmark*:

\[
\mu_{B\text{-scale}}
=q_B^P E(Y\mid R=1,W_B=1)
+(1-q_B^P)E(Y\mid R=1,W_B=0).
\]

Then exactly,

\[
\mu_{\text{naive}}-\mu
=
\underbrace{(m_1-m_0)(q_A-q_B^P)(r_1-r_0)}_{\text{cross-source benchmark-scale mismatch}}
+
\underbrace{(m_1-m_0)(p_B-p)\{1-J_B(r_1-r_0)\}}_{\text{residual proxy-selection bias}}.
\]

The first term is zero when the two sources use the same measurement map. Indeed,

\[
q_A-q_B^P
=(b_B-b_A)+p(J_A-J_B).
\]

The second term is zero when there is no latent-X selection (`p_B=p`), and it also shrinks as the B-scale measurement becomes more informative about `X`.

## Interpretation

The decomposition distinguishes two inferential failures that ordinary “measurement error in weights” language conflates:

1. **Wrong benchmark scale:** even if `W_B` were an adequate adjustment variable, the analyst is forcing it to a target marginal belonging to a different measurement process.
2. **Insufficient proxy adjustment:** even if the analyst had the correct target marginal for `W_B`, balancing a noisy proxy need not reproduce balance on latent `X`, so selection bias can remain.

This separation is the principal mathematical reason to continue C009 in narrowed form.

---

# 5. A sharper operational representation

Let

\[
\Delta_W=E(Y\mid B,W_B=1)-E(Y\mid B,W_B=0)
=(m_1-m_0)(r_1-r_0).
\]

Let

\[
d_{obs}=q_A-q_B,
\]

be the observed probability-versus-NPS difference, and define the unknown cross-scale discrepancy

\[
\delta=q_A-q_B^P.
\]

Then the B-scale selection discrepancy is

\[
q_B^P-q_B=d_{obs}-\delta.
\]

Naive calibration changes the unweighted NPS mean by

\[
\mu_{\text{naive}}-\mu_B=d_{obs}\Delta_W,
\]

whereas calibration to the correct B-scale target would change it by

\[
\mu_{B\text{-scale}}-\mu_B=(d_{obs}-\delta)\Delta_W.
\]

Hence the excess adjustment caused purely by using the wrong-scale benchmark is

\[
\mu_{\text{naive}}-\mu_{B\text{-scale}}=\delta\Delta_W.
\]

This suggests an interpretable sensitivity parameter: the amount of cross-source benchmark mismatch, on the observed proportion scale, needed to materially change or reverse the inferred selection imbalance.

In particular, if `|delta| < |d_obs|`, the sign of the B-scale selection discrepancy is protected against all mismatches within that bound; if the plausible mismatch can exceed `|d_obs|`, even the *direction* of the apparent imbalance is not robust.

This sensitivity interpretation is a candidate contribution to test in prosecution stage 2; it is not yet validated as sufficiently novel or useful.

---

# 6. Boundary case: calibration can create bias from zero

If there is no selection on the latent variable,

\[
p_B=p,
\]

then the unweighted NPS mean is unbiased under the toy assumptions:

\[
E(Y\mid R=1)=\mu.
\]

But naive cross-source calibration has bias

\[
\mu_{\text{naive}}-\mu
=(m_1-m_0)(q_A-q_B^P)(r_1-r_0).
\]

Thus, whenever

- the outcome is associated with latent `X`,
- `W_B` contains information about `X`, and
- A and B encode the nominally shared variable differently,

calibration can **introduce bias into an otherwise unbiased sample**.

This phenomenon is not claimed as globally new: Chambers already showed that substitution of a non-identical auxiliary control can generate substantial calibration bias in conventional survey estimation [R113]. Its value here is as a boundary condition inside the P/NPS selection-adjustment problem.

---

# 7. Identification without validation information

## 7.1 Constructive nonidentification example

The minimal observed-data structure does not point-identify `mu` when both selection and the A-side measurement map are unknown.

Assume B measures `X` perfectly for simplicity and the observed B data satisfy

\[
P(W_B=1\mid R=1)=0.6,
\]

\[
E(Y\mid W_B=0,R=1)=0.2,\qquad
E(Y\mid W_B=1,R=1)=0.8.
\]

Assume A identifies

\[
P(W_A=1)=0.5.
\]

Two latent parameterizations generate the same observed distributions:

### Parameterization I

- `p=0.3`;
- selection probabilities proportional to `P(R=1|X=1)=0.7`, `P(R=1|X=0)=0.2`, yielding `p_B=0.6`;
- A sensitivity `a_A=1` and specificity `b_A=5/7`, yielding `q_A=0.5`;
- `m_0=0.2`, `m_1=0.8`.

Then

\[
\mu=0.38.
\]

### Parameterization II

- `p=0.5`;
- selection probabilities proportional to `0.6` and `0.4`, again yielding `p_B=0.6`;
- A measures X perfectly, also yielding `q_A=0.5`;
- the same `m_0=0.2`, `m_1=0.8`.

Then

\[
\mu=0.50.
\]

Observed A and B distributions are identical while the target mean differs. Therefore the minimal model is not identified without additional information/restrictions.

## 7.2 Scope of the nonidentification result

This is deliberately a **minimal-model counterexample**, not a theorem that “two noisy samples can never identify a latent covariate.” Two-sample errors-in-variables models can be identified under additional structural conditions [R116], and latent-class models can become identified with additional populations/tests and invariance restrictions [R119].

The point is narrower: the canonical P/NPS data structure does not obtain latent-X identification merely because two nominal versions of X are observed in two sources.

---

# 8. Known-error-rate regime

Suppose `(a_A,b_A,a_B,b_B)` are known and `J_A,J_B != 0`.

Then target and NPS latent prevalences are identified:

\[
p=\frac{q_A-(1-b_A)}{J_A},
\]

\[
p_B=\frac{q_B-(1-b_B)}{J_B}.
\]

Define observable B moments

\[
S_1=E\{YI(W_B=1)\mid R=1\},
\]

\[
S_0=E\{YI(W_B=0)\mid R=1\}.
\]

They satisfy

\[
\begin{pmatrix}S_1\\S_0\end{pmatrix}
=
\begin{pmatrix}
 a_Bp_B & (1-b_B)(1-p_B)\\
 (1-a_B)p_B & b_B(1-p_B)
\end{pmatrix}
\begin{pmatrix}m_1\\m_0\end{pmatrix}.
\]

The determinant is

\[
p_B(1-p_B)J_B.
\]

When it is nonzero,

\[
m_1=\frac{b_BS_1-(1-b_B)S_0}{p_BJ_B},
\]

\[
m_0=\frac{a_BS_0-(1-a_B)S_1}{(1-p_B)J_B},
\]

and therefore

\[
\mu=(1-p)m_0+pm_1
\]

is identified under the toy assumptions.

Notably, the latent selection probabilities themselves need not be identified for this target once latent-X conditional outcome transportability is assumed.

---

# 9. What a “bridge sample” actually identifies

The v0.3 field map treated a bridge sample too loosely. This prosecution corrects that.

## 9.1 Two fallible measurements without gold X

A bridge sample that merely measures both binary versions `(W_A,W_B)` on the same units is **not generally sufficient** to identify latent prevalence and both measurement models.

Under a simple conditional-independence latent-class formulation, a 2x2 observed table has 3 degrees of freedom, while prevalence plus two sensitivities and two specificities gives 5 unknown parameters. This is the classical nonidentification problem for two fallible tests in one population [R119].

Extra populations, additional indicators, external restrictions, or validation information can change this conclusion; they must be stated rather than assumed.

## 9.2 Representative bridge measured on the B scale

A different bridge design is immediately useful even without latent X:

- draw or use a probability-representative target sample;
- administer the **B measurement protocol** to it.

This directly estimates `q_B^P` and therefore fixes the *benchmark-scale mismatch* component.

It does **not** remove the residual proxy-selection term when ignorability holds only given latent `X` rather than given observed `W_B`.

## 9.3 Gold-standard validation

A validation sample observing latent/gold `X` plus both source-specific measurements can identify the source-specific error maps under suitable sampling assumptions, after which the known-error-rate logic above becomes available.

## 9.4 Sensitivity-only regime

When no validation data exist, external bounds or priors on measurement disagreement can be propagated through `delta=q_A-q_B^P` and, for latent-X correction, through plausible error-rate sets. The usefulness of the resulting identified/sensitivity region is an empirical question and is now the next prosecution target.

---

# 10. Nearest-neighbor derivation matrix

| Work | Setting | Where measurement error/mismatch enters | Selection/integration structure | What it already establishes | What remains distinct for narrowed C009 |
|---|---|---|---|---|---|
| Yang & Kim [R064] | Finite-population P/NPS integration | Common auxiliary `X` treated as available | Calibration, IPW, MI, DR families | Canonical integration architecture | Does not analyze source-specific measurement maps for the shared adjustment variable |
| McCaffrey et al. [R089] | IPW / propensity framework | Error-prone covariate | Corrected weighting using error model | Generic error-prone weighting can be repaired with measurement information | Prevents novelty claim based on “IPW covariate error”; does not provide the P-reference wrong-scale benchmark decomposition |
| Chambers [R113] | Conventional survey calibration | Population auxiliary value may be erroneous or a related non-identical variable | Probability-survey calibration/GREG | Wrong/substituted auxiliary controls can generate substantial bias; prediction of correct control can help | Directly kills generic “wrong benchmark harms calibration”; does not include NPS selection/proxy residual decomposition |
| Hong et al. [R114] | Causal propensity score | Covariate measured differently across treatment groups | Treatment assignment + outcome | Differential covariate error can bias propensity methods; Bayesian sensitivity/correction framework | Directly kills generic “group-specific measurement in propensity is new”; different target/data structure from P/NPS finite-pop mean |
| Kim & Tam [R115] | Finite-population big-data + probability sample integration | Measurement error in study variables/data sources; matching misclassification | Unknown big-data selection plus probability sample | Data integration can jointly address undercoverage/selection and measurement error in finite populations | Very close field ancestor; does not center the shared participation-adjustment covariate being encoded on different scales |
| Carroll, Chen & Hu [R116] | Two-sample EIV | Nonclassical error in latent covariate, no gold standard | Two samples under structural invariance | Some two-sample latent-error models are identifiable without gold X | Prevents overclaiming nonidentification; assumptions/data structure differ from canonical P/NPS reference + selected outcome sample |
| Dever & Valliant [R117] | Survey calibration | Control totals are estimated rather than fixed | Probability-survey calibration | Control-total uncertainty affects variance and should be propagated | Random control uncertainty is distinct from semantic/measurement-scale incompatibility |
| Opsomer & Erciulescu [R118] | Sample-based calibration | Control totals estimated from another survey | Two-survey calibration variance | Valid replication variance after random sample-based calibration | Again addresses randomness of comparable controls, not mismatched measurement maps |
| Einarsson et al. [R087] | P vs NP online panels | Empirical measurement nonequivalence | Cross-panel comparison, weighting | Measurement equivalence can fail and weighting does not guarantee it | Establishes phenomenon, not finite-population adjustment bias/identification |
| Dharma et al. [R088] | P/NPS selection + misclassification | Misclassified target status | ALP weighting + bias correction | Joint selection/misclassification correction in a close applied setting | Participation covariates are assumed measured without error in both sources; boundary marker for C009 |
| Sen & Lahiri [R085] | P/NP survey combination | Measurement error and representativeness | Composite estimation | Direct 2026 integration of sampling and measurement concerns | Broad “selection + measurement” claim is occupied; adjustment-X scale mismatch remains a narrower object |

## Nearest-neighbor conclusion

The candidate is **not** novel because it mentions measurement error, source differences, calibration error, or propensity error. Those pieces are established.

The only defensible remaining claim to investigate is the **P/NPS-specific separation of benchmark-scale mismatch from residual latent-selection/proxy bias, together with the information design needed to resolve each component**.

That claim is narrow enough to survive into deeper prosecution, but current evidence is insufficient for a `SURVIVES` verdict.

---

# 11. RANDS 10 provenance audit

The empirical substrate remains credible, but its role is narrower than “validation dataset.”

## 11.1 What is documented

RANDS 10 contains paired source types:

- AmeriSpeak probability sample: 5,017 completed interviews, using web and phone [R093, R095];
- Cint-Lucid nonprobability sample: 5,420 opt-in web respondents [R094, R096].

RANDS rounds 8–10 publicly provide both probability and nonprobability samples [R092].

The nonprobability balancing weight uses age, race/Hispanic ethnicity, education, marital status and metropolitan status to balance against the probability source [R096].

Critically, probability-sample technical documentation states that after the AmeriSpeak pretest, **demographic questions for the opt-in panelists were added before main fielding** [R095]. This establishes different variable provenance at least for some adjustment information: the opt-in source required demographic questions to be added, while the probability panel already possessed panel/sample demographic information used in sampling and weighting.

The two samples also differ in survey mode: AmeriSpeak includes web and phone, while the opt-in source is web-only [R093–R095].

## 11.2 What is not documented

These facts do **not** establish a known sensitivity/specificity or gold-standard latent value for any adjustment variable.

Shared final coding also does not by itself prove measurement equivalence or nonequivalence.

Therefore RANDS can support:

- a provenance-grounded demonstration of the problem;
- observed-scale discrepancy diagnostics;
- controlled/sensitivity analyses tied to documented source differences;
- replication across rounds.

It cannot, without additional validation information, establish the true source-specific measurement-error parameters.

---

# 12. Promotion-gate audit

The v0.3 promotion conditions are now assessed as follows.

| Promotion condition | Status | Evidence |
|---|---|---|
| Finite-population target fixed | **MET** | Mean/prevalence is the canonical target |
| One measurement model fixed | **MET** | Binary source-specific misclassification |
| Information regimes classified | **MET, corrected** | No-validation, known-error, representative B-scale bridge, gold validation, sensitivity-only |
| Naive estimator target/bias derived | **MET** | Exact poststratification/calibration limit and two-component decomposition |
| Nearest-neighbor equivalence test | **MET FOR SCREENING; prosecution continues** | R089/R113/R114/R115 materially narrow the claim; exact P/NPS interaction not surfaced in targeted search |
| RANDS provenance audit | **MET** | Paired P/NPS public data and documented provenance/mode differences; not a gold standard |
| Contribution statement relative to nearest work | **MET, provisional** | See Section 13 |

The candidate has therefore earned **PROSECUTION — NARROWED** status, not `SURVIVES`.

---

# 13. Provisional contribution statement

A contribution worth prosecuting would have to be approximately:

> **For probability/nonprobability integration, distinguish calibration error caused by using a reference benchmark measured on the wrong source scale from residual selection bias caused by conditioning on a noisy proxy; characterize identification of the two components under realistic validation/bridge information and develop an interpretable sensitivity analysis when commensurability is uncertain.**

The nearest literature already covers erroneous auxiliary controls [R113], differential propensity-covariate measurement error [R114], generic error-prone IPW [R089], and finite-population integration with other measurement errors [R115]. Therefore any future manuscript must demonstrate that this decomposition/information-regime framework changes what an analyst can diagnose or do in P/NPS integration.

---

# 14. Kill conditions after this prosecution

Kill C009 if the next stage establishes any of the following:

1. the decomposition is algebraically novel-looking but adds no decision-relevant result beyond Chambers [R113] plus Hong/McCaffrey [R114, R089];
2. useful sensitivity regions require implausibly tight external information;
3. multivariable/multicategory extensions become intractable or reduce to standard calibration theory without a useful diagnostic;
4. RANDS and other accessible data cannot anchor plausible mismatch ranges;
5. the best output is only a methodological caution rather than a statistical contribution.

---

# 15. Recommended next prosecution step

Do **not** begin a full simulation study or general estimator-development program.

The next gate should be a **sensitivity-utility and decision-value prosecution**:

1. parameterize cross-source benchmark mismatch by `delta=q_A-q_B^P` (and a multivariable analogue later);
2. derive the smallest plausible `|delta|` required to reverse the direction of apparent selection imbalance or erase the estimated calibration benefit;
3. derive partial-identification/sensitivity intervals for `mu` under bounded source-specific misclassification;
4. test whether those intervals remain informative under mismatch magnitudes supported by survey-methodology evidence and RANDS provenance;
5. compare the resulting diagnostic directly to Chambers-style wrong-control correction and Hong/McCaffrey-style measurement-error propensity correction;
6. only if the diagnostic is both distinct and useful, promote C009 to `SURVIVES` and design the full simulation/application protocol.

This next gate is deliberately designed to answer **“does the narrowed result change a decision?”** rather than merely “can more algebra be written?”

---

# 16. Reproducibility notes

### Search date

2026-09-07.

### Search families added in this prosecution

- `nonprobability calibration auxiliary variables measurement error noncommensurate mismatched benchmark survey`
- `nonprobability sample calibration measurement error auxiliary variables`
- `nonprobability measurement equivalence calibration weighting survey`
- `calibration nonprobability sample misclassification covariate`
- `measurement error auxiliary information calibration Chambers`
- `differential covariate measurement error propensity score`
- `two-sample nonclassical measurement error identification`
- `estimated control totals calibration survey`
- `two fallible tests no gold standard identifiability`

### Algebra checks

The two-component decomposition, its special cases, and the constructive nonidentification parameterizations were independently checked symbolically/numerically during this prosecution. These checks support the research record but are not substitutes for manuscript-level proofs.

### Literature-search limitation

No search can establish absence. The exact P/NPS decomposition must still be citation-chained through Chambers [R113], Hong et al. [R114], McCaffrey et al. [R089], Kim & Tam [R115], and papers citing them before any novelty statement is made in a manuscript.

---

# 17. Stage-2 prosecution: bounded mismatch and partial identification

Section 15 required the next gate to answer a decision question, not merely produce more algebra. This section executes that gate.

The stage-2 objectives were:

1. parameterize cross-source benchmark mismatch;
2. derive the smallest mismatch that changes the calibration decision;
3. propagate bounded source-specific misclassification into a target-mean sensitivity region;
4. test whether the region is informative under defensible information levels;
5. compare the result directly to the closest sensitivity/partial-identification ancestors;
6. decide whether C009 deserves promotion to `SURVIVES`.

The answer to item 6 is **no**. The reasoning is developed below.

---

# 18. A two-parameter sensitivity representation

Retain the binary model and notation from Sections 3–5. Let

\[
d=d_{obs}=q_A-q_B,
\]

\[
\delta=q_A-q_B^P,
\]

and

\[
\Delta_W=E(Y\mid R=1,W_B=1)-E(Y\mid R=1,W_B=0).
\]

The correct B-scale discrepancy is

\[
q_B^P-q_B=d-\delta.
\]

## 18.1 Proxy attenuation parameter

From Section 3,

\[
r_1-r_0
=\frac{J_B p_B(1-p_B)}{q_B(1-q_B)}.
\]

Define

\[
\kappa=J_B(r_1-r_0)
=\frac{J_B^2p_B(1-p_B)}{q_B(1-q_B)}.
\]

For the binary latent variable and binary B-side proxy,

\[
\boxed{\kappa=\operatorname{Corr}(X,W_B\mid R=1)^2}.
\]

Thus `kappa` has a direct reliability interpretation inside the selected NPS: it is the squared latent-proxy correlation. Under an informative orientation, `0<kappa<=1`.

An equivalent expression in terms of B-side sensitivity/specificity is

\[
\kappa
=\frac{(q_B+b_B-1)(a_B-q_B)}{q_B(1-q_B)}.
\]

## 18.2 Exact target-mean identity

Because

\[
\mu-\mu_B=(m_1-m_0)(p-p_B),
\]

while

\[
(d-\delta)\Delta_W
=J_B(p-p_B)(m_1-m_0)(r_1-r_0)
=\kappa(\mu-\mu_B),
\]

we obtain

\[
\boxed{
\mu=\mu_B+\frac{(d-\delta)\Delta_W}{\kappa}
}.
\]

This is the central stage-2 result.

It separates two uncertainties:

- `delta`: how wrong the probability-source benchmark is for the B measurement scale;
- `kappa`: how much of the latent-X selection correction is recoverable by balancing the noisy B-side proxy even if the correct B-scale target margin were known.

Correct B-scale calibration changes the NPS mean by

\[
\mu_{B\text{-scale}}-\mu_B=(d-\delta)\Delta_W
=\kappa(\mu-\mu_B).
\]

Therefore `kappa` is also exactly the fraction of the latent-X mean correction recovered by correct-scale proxy calibration under the toy assumptions.

Naive A-benchmark calibration remains

\[
\mu_{naive}=\mu_B+d\Delta_W.
\]

Its total bias is therefore

\[
\boxed{
\mu_{naive}-\mu
=\frac{\{\delta-d(1-\kappa)\}\Delta_W}{\kappa}
}.
\]

The expression exposes an important cancellation possibility: wrong-scale benchmark error can partially offset proxy under-correction, so a mismatched benchmark can occasionally make the final mean closer to truth by accident. That is not a reason to use the wrong benchmark; it is a reason that monotone “more harmonization always moves the estimate toward truth” intuition fails without identifying the latent correction.

---

# 19. Exact decision zones

Assume `d != 0`, `Delta_W != 0`, and `kappa>0`. Define the dimensionless mismatch ratio

\[
\rho=\frac{\delta}{d}.
\]

The ratio of the naive calibration adjustment to the true latent-X correction is

\[
\frac{\mu_{naive}-\mu_B}{\mu-\mu_B}
=\frac{\kappa}{1-\rho}.
\]

This produces exact boundaries.

| Region | Condition | Interpretation |
|---|---:|---|
| Under-correction but helpful | `rho < 1-kappa` | Naive adjustment points toward truth but is smaller than the needed correction |
| Exact by cancellation | `rho = 1-kappa` | Wrong-scale mismatch exactly offsets proxy attenuation |
| Over-correction but still helpful | `1-kappa < rho < 1-kappa/2` | Adjustment overshoots truth but remains closer than the unweighted NPS |
| Tie with no calibration | `rho = 1-kappa/2` | Naive calibrated and unweighted NPS means are equally far from truth |
| Same direction but harmful | `1-kappa/2 < rho < 1` | Calibration moves in the nominally correct direction but overshoots enough to be worse than no adjustment |
| Wrong direction | `rho >= 1` | The true B-scale imbalance is zero/reversed relative to the observed A-vs-B discrepancy |

Two particularly interpretable thresholds are therefore

\[
\boxed{\rho_{exact}=1-\kappa}
\]

and

\[
\boxed{\rho_{benefit}=1-\frac{\kappa}{2}}.
\]

The latter is the boundary for whether naive calibration improves absolute error relative to leaving the NPS unadjusted.

## 19.1 Mismatch-only decision zones

If the target is only the mean that would result from **correct B-scale calibration**, ignoring residual latent-X bias, then the comparison does not require `kappa`.

Naive calibration is closer to `mu_Bscale` than the unweighted NPS iff

\[
|\delta|<|d-\delta|,
\]

which for `d!=0` is equivalent to

\[
\boxed{\rho<1/2}.
\]

Under a symmetric mismatch bound `|delta|<=epsilon`, this yields a robust three-zone diagnostic:

1. **Calibration-dominance:** `epsilon < |d|/2`. Naive calibration is guaranteed to be closer to the correct B-scale calibrated target than no calibration.
2. **Sign-robust / benefit-ambiguous:** `|d|/2 <= epsilon < |d|`. The direction of B-scale imbalance is protected, but calibration is not guaranteed to improve the B-scale target.
3. **Direction-ambiguous:** `epsilon >= |d|`. Even the sign of the B-scale selection discrepancy can reverse.

These are decision-relevant results. Stage 2 therefore does **not** fail because the algebra lacks a tipping point.

---

# 20. Bounding the sensitivity parameters with minimum correct-report assumptions

Suppose a binary measurement has sensitivity and specificity both at least `c>1/2`.

For an observed positive proportion `q`, the latent prevalence `p` must satisfy

\[
\boxed{
\max\left\{0,\frac{q+c-1}{c}\right\}
\le p \le
\min\left\{1,\frac{q}{c}\right\}
}.
\]

This follows because, for fixed `p`, the feasible observed proportion under `a,b>=c` is

\[
cp\le q\le (1-c)+cp.
\]

## 20.1 Bound on cross-scale mismatch

Let source A and source B have maximum class-specific error probabilities `e_A=1-c_A` and `e_B=1-c_B`. Because both measurements act on the same target latent prevalence `p`,

\[
|q_A-p|\le e_A\text{ in the source-specific direction},
\]

and the exact common-prevalence geometry gives the conservative uniform bound

\[
\boxed{|\delta|=|q_A-q_B^P|\le \max(e_A,e_B)}.
\]

If both sources satisfy the same minimum sensitivity/specificity `c`, then

\[
\boxed{|\delta|\le 1-c}.
\]

This is tighter than a crude triangle bound because the two source errors share the same latent prevalence.

## 20.2 Lower bound on proxy reliability

For the B source,

\[
\kappa=\frac{(q_B+b_B-1)(a_B-q_B)}{q_B(1-q_B)}.
\]

If only `a_B,b_B>=c` is known, a strictly positive universal lower bound exists only when

\[
c>\max(q_B,1-q_B).
\]

In that case,

\[
\boxed{
\kappa\ge
\kappa_{min}(c;q_B)
=\frac{(q_B+c-1)(c-q_B)}{q_B(1-q_B)}
}.
\]

If `c<=max(q_B,1-q_B)`, the accuracy bound alone permits `kappa` arbitrarily close to zero because a nearly degenerate latent prevalence/error configuration can reproduce the observed `q_B`.

These formulas turn lower bounds on source-specific correct classification into an outer sensitivity rectangle for `(delta,kappa)`. The rectangle is conservative because `delta` and `kappa` are coupled through the same source-specific measurement parameters.

---

# 21. Toy stress test

To examine whether the sensitivity region can remain informative, use the observed-data configuration from the Section 7 nonidentification example:

\[
q_A=0.50,\qquad q_B=0.60,
\]

\[
E(Y\mid W_B=0,R=1)=0.20,\qquad
E(Y\mid W_B=1,R=1)=0.80.
\]

Hence

\[
\mu_B=0.56,\quad \Delta_W=0.60,\quad d=-0.10,
\]

and naive A-benchmark calibration gives

\[
\mu_{naive}=0.50.
\]

Assume for illustration that `Y` is bounded in `[0,1]` and that **both** source-specific sensitivities and specificities are at least `c`. For each `c`, optimize the target mean over all source-specific binary misclassification maps satisfying those bounds and the observed data, while retaining feasible latent outcome means in `[0,1]`.

The resulting **population-level sensitivity envelope** is:

| Minimum Se/Sp `c` | Feasible `mu` envelope | Width |
|---:|---:|---:|
| 0.99 | [0.492, 0.505] | 0.013 |
| 0.95 | [0.457, 0.527] | 0.070 |
| 0.90 | [0.400, 0.560] | 0.160 |
| 0.85 | [0.329, 0.600] | 0.271 |
| 0.80 | [0.300, 0.650] | 0.350 |
| 0.75 | [0.267, 0.714] | 0.448 |
| 0.70 | [0.229, 0.771] | 0.543 |

These are **not sampling confidence intervals** and are not claimed here as a theorem of sharpness. They are numerically optimized feasible envelopes under the toy population model and the stated lower-bound restrictions.

The diagnostic message is clear: the target can be tightly constrained when measurement is known to be extremely accurate, but uncertainty grows quickly as the minimum correct-classification information weakens.

For comparison, treating only the marginal bounds `|delta|<=1-c` and `kappa>=kappa_min` as independent gives a looser outer rectangle. In this same toy example:

| `c` | `kappa_min` | Conservative outer `mu` range |
|---:|---:|---:|
| 0.95 | 0.802 | [0.448, 0.530] |
| 0.90 | 0.625 | [0.368, 0.560] |
| 0.85 | 0.469 | [0.240, 0.624] |
| 0.80 | 0.333 | [0.020, 0.740] |

The gap between the coupled envelope and the rectangle shows why source-error parameters should be constrained jointly when sensitivity analysis is actually implemented.

## 21.1 Toy decision thresholds

Here `|d|=0.10`.

- A symmetric `|delta|<0.05` bound guarantees that naive calibration is closer to the **correct B-scale calibrated target** than leaving the NPS unweighted.
- `|delta|<0.10` protects the direction of B-scale imbalance.
- Once plausible mismatch reaches 0.10 on the proportion scale, even the imbalance direction can be reversed.

For truth-relative benefit, the threshold additionally depends on `kappa` through `rho=1-kappa/2`. A less reliable proxy makes the boundary depend more strongly on how much wrong-scale mismatch may accidentally compensate for proxy attenuation; without information on `kappa`, the truth-relative decision cannot be reduced to `delta` alone.

---

# 22. Can RANDS anchor `delta` or `kappa`?

RANDS remains useful for demonstrating that the two sources have different provenance and collection modes and that shared demographics are used to balance the NPS to the probability sample [R092–R096].

But the stage-2 question is stricter: can the data defend a numeric region for `delta` or `kappa`?

The answer is currently **no**.

RANDS does not provide, for the balancing variables:

- gold-standard latent `X`;
- source-specific sensitivity/specificity estimates;
- repeated independent source-specific measurements on the same units sufficient to estimate an error model;
- a representative target-population administration of the B-side measurement protocol that directly identifies `q_B^P`.

The documentation therefore anchors **provenance**, not the sensitivity-parameter magnitudes.

External survey-reliability work confirms that response reliability and classification accuracy can vary by construct, category, subgroup and data source. Such studies can motivate candidate bounds for a *specific* variable only after the measurement definitions and validation design are matched closely enough. They do not justify a universal `c=0.90` or `0.95` assumption for education, race/ethnicity, marital status, metropolitan status, or other RANDS balancing variables.

Consequently, a tight C009 sensitivity result on RANDS would currently be driven mainly by analyst-chosen assumptions rather than by validation information.

---

# 23. Stage-2 nearest-neighbor prosecution

The new algebra is useful, but the project gate asks what remains that the nearest papers cannot already claim.

| Work | Established result relevant to stage 2 | Consequence for C009 |
|---|---|---|
| Hartman & Huang [R120] | For a weighting covariate observed in the survey sample but absent from the target population, calibration sensitivity can vary the unknown target-population mean/moment over plausible values; includes robustness thresholds and benchmarking | Substantially absorbs the `delta`-only sensitivity operation because `q_B^P=q_A-delta` is simply an unknown target B-scale margin reparameterized around the available A-scale margin |
| Molinari [R121] | Sharp partial identification for discrete misclassification under restrictions on misclassification matrices, including lower bounds on correct-report probabilities | Generic bounded-misclassification -> identified-region machinery is not a C009 novelty |
| Imai & Yamamoto [R122] | Nonparametric identification and sensitivity analysis under differential measurement error | Generic differential-error sensitivity claims are occupied |
| Rudolph & Stuart [R123] | Recasts covariate measurement error as unobserved confounding and adapts sensitivity analyses for propensity methods | Further occupies sensitivity analysis for error-prone weighting covariates |
| Lockwood & McCaffrey [R124] | Conditions for matching/weighting with functions of error-prone covariates, including discrete misclassification and group-specific functions | Strong ancestor for the proxy-balancing side and group-specific measurement functions |
| Chambers [R113] | Calibration with erroneous/non-identical auxiliary information | Already occupies the wrong-control warning and correction motivation |
| Hong et al. [R114] / McCaffrey et al. [R089] | Differential measurement error and corrected propensity weighting | Occupy much of the error-prone selection-adjustment machinery |

## What remains distinct

After this comparison, the cleanest residual C009 object is:

> the **joint** P/NPS interaction between (i) using a target benchmark from the wrong measurement scale and (ii) attenuated recovery of latent selection correction when the NPS weighting variable is only a proxy, summarized in the binary model by the `(delta,kappa)` decision surface.

This interaction is more specific than the cited ancestors, and the exact identity in Section 18 is worth retaining.

However, the residual is now narrow. The `delta` margin sensitivity, the generic partial-identification machinery, and the generic measurement-error sensitivity/weighting components cannot independently support novelty.

---

# 24. Promotion-gate verdict

The stage-1 Section 14 kill conditions can now be assessed directly.

| Kill / promotion issue | Stage-2 result |
|---|---|
| Does the decomposition produce a decision-relevant result? | **YES.** Exact sign, benefit, over/under-correction and reversal thresholds exist. |
| Is the `delta`-only diagnostic distinct from existing sensitivity work? | **NO, not enough.** R120 substantially covers unknown target-margin sensitivity in calibration. |
| Is bounded-misclassification partial identification itself distinct? | **NO.** R121 is a strong generic ancestor. |
| Are useful regions guaranteed under weak information? | **NO.** The toy envelope widens rapidly as minimum correct classification weakens. |
| Can RANDS anchor plausible numeric bounds? | **NO with current documentation.** It anchors provenance but not source error rates or latent truth. |
| Does a full multivariable contribution already exist? | **NOT YET.** No nontrivial extension has been derived that clearly escapes standard calibration/misclassification machinery. |
| Is the residual interaction mathematically empty? | **NO.** The `(delta,kappa)` lemma is clean and potentially reusable. |
| Is it large and anchored enough for the first project? | **NO.** |

## Final verdict

\[
\boxed{\text{C009 = PARKED / NO-GO FOR FIRST PROJECT}}
\]

**Confidence: moderately high.**

This is a failure to clear the **project-selection gate**, not a claim that the mathematics is uninteresting or globally known in exactly this notation.

The stage-2 result improves the program in three ways:

1. it prevents us from spending a full simulation/application cycle on a contribution whose generic components have already been developed elsewhere;
2. it leaves behind a compact decision lemma that can be reused if a future candidate encounters cross-source auxiliary mismatch;
3. it sharpens the empirical requirement for any revival: obtain information that identifies or defensibly bounds the **target B-scale margin** and/or **latent-proxy reliability**, rather than merely documenting that the sources differ.

---

# 25. Reopening conditions and next program action

Do not delete C009. Reopen it only if at least one of the following becomes true:

1. **Representative B-scale bridge:** a probability/target sample is administered the NPS version of a key adjustment variable, directly informing `q_B^P` and therefore `delta`.
2. **Gold or strong validation:** the same units have latent/gold `X` or a validation design that identifies source-specific error maps, allowing `kappa` to be estimated or tightly bounded.
3. **Construct-specific defensible bounds:** a closely matched validation study provides sensitivity/specificity or repeatability information for the actual variable definitions used in the target P/NPS application.
4. **Nontrivial multivariable theorem:** the vector/multicategory extension yields structure beyond ordinary calibration moment perturbation plus established misclassification-matrix optimization.
5. **High-value application boundary:** a substantive survey decision depends on the joint `(delta,kappa)` region and the nearest sensitivity literature does not already provide an equivalent diagnostic.

Absent one of those conditions, the correct program action is:

> **Return to candidate generation/prosecution within D013 rather than promote C009 into execution.**

No large simulation suite, software package, or RANDS application should be built for C009 at this stage.

---

# 26. Stage-2 reproducibility notes

### Date

2026-09-07.

### Added nearest-neighbor search families

- `survey weights sensitivity partially observed confounder target population mean calibration`
- `partial identification misclassified data lower bound correct report probability`
- `differential measurement error sensitivity analysis`
- `covariate measurement error propensity score sensitivity unobserved confounding`
- `matching weighting error-prone covariates discrete misclassification`
- `survey demographic reliability reinterview race education marital status mode`

### Numerical check

The toy sensitivity envelopes in Section 21 were obtained by optimizing over source-specific binary sensitivity/specificity parameters subject to:

- the displayed observed A and B margins/outcome means;
- source-specific sensitivity and specificity lower bounds `a_s,b_s>=c`;
- informative measurement maps;
- latent prevalences in `[0,1]`;
- latent stratum outcome means in `[0,1]`.

The analytic identities and decision boundaries were independently checked algebraically and numerically. Manuscript use would still require formal proofs, sampling-uncertainty treatment, and a sharper characterization of the identified set.

### Literature limitation

The stage-2 verdict is a research-program decision, not a proof of global absence. The residual `(delta,kappa)` interaction should not be called novel in public without citation-chaining R120–R124 and the stage-1 ancestors. The reason for parking is that, under the evidence currently available, the expected incremental contribution is too narrow and weakly anchored relative to the first-project standard.

