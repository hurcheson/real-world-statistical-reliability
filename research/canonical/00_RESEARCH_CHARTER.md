---
title: Research Charter
version: 0.2.0
last_updated: 2026-09-07
status: active
---

# Research Charter

## Program

**Real-World Statistical Reliability**

*Project provenance:* originated as **Real-World ML Reliability**; historical records retain that name. Infrastructure renaming is deferred until execution (D015).

## Core research interest

Reliable statistical inference and decision support under imperfect real-world data, including:

- selection bias and nonrepresentative samples;
- integration of probability, nonprobability, administrative and other data sources;
- measurement error and cross-source measurement incompatibility;
- missingness, undercoverage and informative observation;
- calibration, weighting and finite-population inference;
- sensitivity analysis under unverifiable assumptions;
- external validity, transportability and distribution shift;
- uncertainty, subgroup heterogeneity and model updating.

Machine learning and biomedical data remain legitimate application branches, not permanent requirements. The active first-project neighborhood is governed by the Decision Ledger rather than hard-coded into this charter.

## Program objective

Develop rigorous, useful, reproducible work in **Applied Statistics and Data Science** in which the central contribution concerns the reliability of inference, estimation, prediction or decisions under real-world data imperfections. Machine learning is used when the scientific question requires it, not as a mandatory identity.

## What counts as a viable research contribution

A project does **not** need to be completely untouched by prior literature.

A candidate is acceptable when it provides a **defensible, consequential contribution** that the closest existing work cannot already claim.

Possible contribution types include:

- new statistical method or estimator;
- improved identification or inference;
- new robustness or failure analysis;
- external validation or transportability analysis;
- meaningful contradiction or boundary condition;
- improved measurement/evaluation framework;
- realistic benchmark that changes methodological conclusions;
- new population or context when that context matters scientifically;
- simplification of an impractical method;
- integration of established methods where the integration changes what can be learned.

## Candidate acceptance gate

Before execution, a candidate should satisfy all of the following as strongly as practical:

1. **Importance** — the problem matters scientifically, statistically, or operationally.
2. **Prior-art map** — the closest papers, methods, groups, and active work are identified.
3. **Differentiation** — the contribution can be stated in one or two sentences relative to the nearest competitor.
4. **Consequentiality** — the remaining contribution matters; it is not merely an empty literature cell.
5. **Identifiability** — the estimand or scientific question is coherent and, where relevant, identifiable under explicit assumptions.
6. **Data feasibility** — required data are public, institutionally accessible, or realistically obtainable.
7. **Computational feasibility** — the project can be executed with available compute and software.
8. **Scope feasibility** — it can be completed at the intended student/research level.
9. **Competition risk** — active neighboring work is understood and the execution window is acceptable.
10. **Audience** — there is a plausible methodological or applied community that would care about the result.

## Stop rule for searching

Once a candidate survives deep prosecution and has a clear contribution, literature work changes from **discovery mode** to **monitoring mode**.

We do not seek impossible certainty that nobody else is working on the topic. We seek **defensible novelty under uncertainty**, then execute.

## Kill rule

A candidate should be killed or parked when one or more of the following holds:

- the claimed novelty is already established;
- the closest active work leaves only a trivial extension;
- the remaining problem is poorly identified;
- the technical burden is disproportionate to the contribution;
- data access is unrealistic;
- the contribution is scientifically unimportant;
- the project is too exposed to active competition for its expected value.

Killed candidates are **never deleted**. Their dossiers remain part of the program memory.

## Anti-overengineering rule

Do not build a research platform, autonomous agent system, vector database, or elaborate software architecture before a real project needs it.

Start with evidence, Markdown records, and one executable research project.

Infrastructure should be earned by repeated need.

## Research integrity rules

- Distinguish evidence from inference.
- Never claim “no one has studied this” without a documented search.
- Search for work that could falsify novelty, not only work that supports it.
- Treat preprints, dissertations, conference programs, grants, lab pages, and active repositories as part of the competitive landscape.
- Do not convert absence of search results into proof of absence.
- Prefer primary sources.
- Record uncertainty explicitly.
- Re-verify literature claims before publication.


## Change log

### 0.2.0 — 2026-09-07

- Broadened the scientific umbrella after the field-selection pivot.
