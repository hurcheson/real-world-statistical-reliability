---
title: OF-19–OF-23 Collapse-First Triage
version: 0.1.1
last_updated: 2026-09-07
status: active
---

# OF-19–OF-23 Collapse-First Triage

## Purpose

Execute the bounded next step ordered by D018: compare OF-19 through OF-23 adversarially, locate the strongest direct prior art that could collapse each broad opportunity, and assign **C011 only if a survivor earns promotion**.

This is a triage dossier, not five full candidate prosecutions. The stop rule is deliberately asymmetric: a direct paper/method that already owns the broad contribution is sufficient to prevent promotion; a possible residual niche is not sufficient to create a candidate until its estimand, identification, decision value and data path are explicit.

## Canonical starting state

The active neighborhood remains survey data integration / nonprobability inference under D013. The five open formulations entering this pass were:

- **OF-19:** sensitivity analysis under nonignorable NPS participation;
- **OF-20:** regression/association parameters under data integration;
- **OF-21:** safe/selective borrowing from NPS;
- **OF-22:** drift in nonprobability participation mechanisms across repeated survey waves;
- **OF-23:** overlap/undercoverage diagnostics tied to inferential decisions.

The acceptance gate is the Research Charter: importance, mapped prior art, one- or two-sentence differentiation, consequentiality, coherent identification, data/compute/scope feasibility, acceptable competition risk and a plausible audience.

## Triage result at a glance

| Opportunity | Broad-claim verdict | Strongest collapse evidence | Residual worth keeping? | C011? |
|---|---|---|---|---|
| OF-19 | **PARK / broad form occupied** | R080, R143, R144 | Only if coupled to a new failure mechanism/estimand not covered by current nonignorable/sensitivity work | **No** |
| OF-20 | **PARK / generic form occupied** | R086 | Mechanism-specific association reliability may still matter | **No** |
| OF-21 | **PARK / decision already directly studied** | R073, R074 | Only a materially different loss/robustness structure | **No** |
| OF-22 | **BROAD FORM COLLAPSED; WATCHLIST RESIDUE** | R142 | Early drift detection / intermittent probability anchors | **No — sharpen first** |
| OF-23 | **PARK / generic diagnostic-decision form occupied** | R071, R079 | Only with a different estimand or decision loss not reducible to existing threshold/undercoverage methods | **No** |

**Portfolio decision:** no candidate is promoted. **C011 remains unassigned.**

---

# OF-19 — Sensitivity analysis under nonignorable NPS participation

## Broad question

How should finite-population inference from a nonprobability survey change when participation remains outcome-dependent after conditioning on observed auxiliaries?

## Collapse evidence

The broad methodological niche is now plainly occupied.

- Liu, Yuan, Li and Wu develop pseudo-likelihood inference for **nonignorable nonprobability samples**, including regression prediction, IPW and augmented IPW estimators with variance estimation [R080].
- Pfeffermann, Preminger and Sikov's 2025 JSSAM paper treats informative probability sampling plus nonignorable nonresponse when selection/response depends on the outcome after conditioning on model covariates [R143]. It is an adjacent nonignorability ancestor, not direct NPS prior art.
- Current Michigan survey-methodology work extends **sensitivity analysis for nonignorable selection bias** to subgroup parameters in NPS [R144].
- Conti, Marella and Summa provide a 2026 uncertainty/non-identifiability treatment for unknown NPS sampling designs and show how extra-sample information contracts the plausible class [R146].

## Theory channel

A generic sensitivity parameter for outcome-dependent selection is not enough. The theory frontier already includes explicit nonignorable selection models, uncertainty classes and sensitivity formulations. A viable descendant would need a sharper structure—e.g. interaction with measurement incompatibility, undercoverage, domain-specific constraints or a decision loss not already handled by these frameworks.

## Data / decision channel

The practical need is real, but the broad decision “how sensitive is my NPS estimate to nonignorability?” is already served by existing methods and active work. No unique public-data design emerged that would turn the broad OF-19 statement into a distinct first-project contribution.

## Verdict

**PARKED in broad form. Do not promote to C011.**

Reopen only after defining a mechanism-specific failure that changes the sensitivity object or identifies new information unavailable to existing nonignorable-selection frameworks.

---

# OF-20 — Regression/association parameters under data integration

## Broad question

Do regression or association parameters behave differently from population means when probability and nonprobability sources are integrated?

## Collapse evidence

Wang, Kim and Kim already provide a direct method for **survey data integration for regression analysis using model calibration**, with theoretical properties and applications across sources with different missing patterns; the work explicitly connects to missing-covariate and measurement-error problems [R086]. Earlier benchmarking literature also shows that multivariate relationships can behave differently from marginal estimates, so “associations may be more robust than means” is an empirical observation rather than a candidate contribution by itself.

## Theory channel

A regression coefficient is not automatically a more defensible estimand under sample selection. Its transportability depends on the population model, the sampling mechanism, effect/association heterogeneity and which covariates are shared. Therefore a viable descendant needs a *specific failure mechanism* and a population regression estimand whose identification or bias differs consequentially from existing data-integration regression theory.

## Verdict

**PARKED in generic form. Do not promote to C011.**

Reopen only with a mechanism-specific proposition—e.g. a boundary condition where mean integration fails but a clearly defined association estimand remains identified, or vice versa—and a data design capable of validating that distinction.

---

# OF-21 — Safe/selective borrowing from NPS

## Broad question

When should a probability survey decline to borrow information from a large nonprobability sample because bias risk exceeds efficiency gain?

## Collapse evidence

This is directly occupied by the test-and-pool literature. Gao and Yang's pretest estimator uses the probability design to test P/NPS comparability and **decide whether to leverage the NPS or retain the probability sample alone**, with data-adaptive tuning targeting MSE and robust confidence intervals [R073]. Current doubly robust integration work further studies efficient combination of a DR NPS estimate with the probability-only estimate [R074].

## Theory / decision channel

The decision itself is therefore not novel. A new candidate would need a materially different uncertainty set or loss function—such as one induced by a specific measurement/coverage failure—and would need to prove that the resulting borrowing rule is not simply a re-expression of pretest, shrinkage or robust-combination machinery.

## Verdict

**PARKED in broad form. Do not promote to C011.**

---

# OF-22 — Drift in NPS participation mechanisms across repeated survey waves

## Broad question

Can a selection-adjustment model calibrated at one wave stop transporting because the nonprobability participation mechanism changes over time?

## Direct collapse evidence

Jackson, Hasanbasri, McPhee and Peugh (2022) ask essentially this question in a recurring hybrid probability/nonprobability tracking poll [R142]. Their study explicitly asks whether NPS selection mechanisms change over time and whether an additional propensity adjustment can recover trend accuracy. They show that:

- the characteristics predicting NPS membership changed between waves;
- raking that had been adequate earlier could become inadequate later;
- the resulting change distorted trend estimates; and
- a flexible propensity adjustment partially corrected the distortion, at a precision cost.

Therefore **“selection mechanisms drift across waves and stale adjustment can break trend inference” is not a novel broad claim.**

## Four-channel residue

### Literature-generated

R142 directly occupies retrospective detection/correction when a side-by-side probability sample is present at each wave. Longitudinal-survey refreshment-sample literature supplies strong ancestors for learning about changing response/attrition mechanisms, and 2026 active work tests selection-on-observables assumptions using refreshment samples [R145].

### Theory-generated

A narrower statistical question remains coherent:

> Suppose a cheap NPS is observed every wave but a high-quality probability/reference sample is available only intermittently. Can one detect or bound **selection-mechanism drift** early enough to decide when previously learned NPS adjustment weights/models should no longer be transported?

This is not the same design as R142, which observes side-by-side P and NPS data at every studied wave. But the residual requires explicit assumptions linking adjacent-wave participation mechanisms. Without such temporal structure, drift between unanchored waves is not identified merely from the NPS itself.

### Data-generated

The strongest direct recurring-hybrid example in R142 is a confidential media tracking poll; its article exposes figures/tables but not a reusable public microdata benchmark. Public Pew benchmarking datasets provide high-value P/opt-in comparisons, but the 2016 and 2021 studies are not a clean same-design recurring series and therefore do not yet supply the ideal validation substrate for an intermittent-anchor method.

### Decision-generated

A real decision exists: **when must a survey organization refresh a probability benchmark, rebuild adjustment, or refuse trend claims based on stale NPS weights?** That is consequential. However, a candidate needs a defensible observable trigger tied to estimand error—not merely a generic distribution-drift score.

## Why OF-22 is not promoted yet

The residue is more promising than the other four, but it fails several candidate gates today:

1. **Differentiation is not yet theorem-level.** “Early warning rather than retrospective repair” is a useful distinction, but not yet a statistical contribution.
2. **Identification depends on unformulated temporal assumptions.** With no reference sample at an unanchored wave, changes in outcome composition can reflect population change, measurement change, or selection drift.
3. **Public-data feasibility is not yet secured.** The closest recurring hybrid microdata are not clearly public.
4. **Ancestor competition is broad.** Refreshment-sample diagnostics, nonresponse/attrition modeling, sequential drift detection and recurring-hybrid weighting all touch pieces of the residual.
5. **Scope risk is high.** A fully general dynamic selection model would be too large for the intended first project unless the estimand and anchor design are sharply restricted.

## Promotion gate for a future C011

Promote only if a subsequent sharpening pass can state all of the following:

- a repeated-wave estimand (e.g. population mean trend or change);
- the exact anchor schedule (which waves contain a probability/reference sample);
- a minimal temporal model/restriction on participation drift;
- an observable diagnostic or partial-identification bound whose threshold changes a real decision;
- a theorem showing what can/cannot be learned between anchor waves;
- a public or realistically obtainable dataset that contains enough repeated P/NPS structure to falsify the method; and
- a nearest-neighbor statement explaining why R142 plus refreshment-sample methods do not already imply the result.

## Verdict

**WATCHLIST / SHARPEN BEFORE CANDIDATE. No C011 yet.**

---

# OF-23 — Overlap/undercoverage diagnostics tied to inferential decisions

## Broad question

Can overlap diagnostics tell analysts when to trim/threshold NPS units, restrict the target population or abandon NPS borrowing?

## Collapse evidence

The generic version is already directly occupied.

- Chen, Li and Wu distinguish stochastic from deterministic undercoverage, use convex-hull structure, propose bias-mitigation strategies and explicitly treat failures of positivity [R071].
- Savitsky, Williams, Beresovsky and Gershunskaya develop thresholding rules for low-overlap nonprobability units in combined P/NPS data; excluding units with poor joint support can reduce estimation error [R079]. The work is now peer-reviewed in *Statistics in Transition New Series* (2025), beyond the earlier BLS working-paper form.
- Lohr's diagnostics discussion explicitly addresses NPS model assumptions, fit-for-use evidence and the question of when NPS data should be used [R147].

## Verdict

**PARKED in broad form. Do not promote to C011.**

A future descendant would need a different inferential target or decision loss whose optimal action cannot be reduced to existing positivity/convex-hull/thresholding machinery.

---

# Cross-opportunity comparison

## Why no candidate is the correct output

The five ideas were intentionally retained as **opportunities**, not promises of five papers. Collapse-first triage did its job:

- OF-19 is crowded by direct nonignorable-selection and sensitivity methodology;
- OF-20 is too generic relative to existing regression-integration methods;
- OF-21's core decision is already the object of test-and-pool methods;
- OF-22's broad temporal-drift claim is directly demonstrated in a recurring hybrid survey;
- OF-23's generic overlap-to-threshold/restrict decision is directly developed in undercoverage and thresholding work.

Assigning C011 anyway would violate the program's kill rule and the principle that candidate IDs are earned by differentiation, not by sequence.

## Portfolio consequence

D013 remains scientifically viable: survey data integration / NPS inference is still a rich reliability neighborhood. What is exhausted is the **current bounded opportunity slate**, not the field.

The next pass should therefore return to **four-channel opportunity generation**, using the failure records from C009, C010 and this triage as boundary conditions. In particular, seek problems where:

1. two error mechanisms interact in a way not already reducible to standard weighting/sensitivity machinery;
2. a real agency/practitioner decision is not answered by current estimators;
3. the key failure parameter is identifiable or tightly bounded by an available design; and
4. public/reproducible data exist before candidate promotion.

Do not automatically revive OF-25/OF-26 or assign C011. Generate, collapse, and promote only a genuinely sharper survivor.

# Evidence status

Search date: **2026-09-07**.

This triage used the canonical reference set plus current web verification for R142–R147 and the peer-reviewed status of R079. Absence of a found paper is not treated as proof of novelty. OF-22's residual is explicitly labeled a watchlist question rather than a novelty claim.
