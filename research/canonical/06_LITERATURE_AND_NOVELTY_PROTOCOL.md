---
title: Literature and Novelty Protocol
version: 0.2.0
last_updated: 2026-09-07
status: active
---

# Literature and Novelty Protocol

## Purpose

Prevent plausible-sounding but weak research gaps from advancing into expensive execution.

This protocol is intentionally adversarial and multi-channel.

The goal is not to prove that nobody has ever studied an exact keyword combination. The goal is to establish a **consequential, defensible contribution under uncertainty**.

## Core discovery model

Research opportunities should be generated and challenged through four complementary channels.

### 1. Literature-generated opportunities

Search for:

- direct prior art;
- interfaces between literatures;
- methodological ancestors;
- recurring assumptions and limitations;
- contradictions and heterogeneous findings;
- citation-network structure;
- active and unpublished work.

### 2. Theory-generated opportunities

Search for:

- unclear estimands;
- identification failures;
- bias decompositions;
- interacting error mechanisms;
- boundary cases;
- sensitivity problems;
- assumptions that can be weakened, diagnosed, or made operational.

### 3. Data-generated opportunities

Search for reproducible phenomena such as:

- cross-dataset or cross-site failures;
- temporal instability;
- subgroup failures;
- benchmark anomalies;
- failed replications;
- methods that help one target while harming another;
- interactions between cleaning, weighting, measurement, selection, and prediction.

Exploratory findings generate questions; they do not establish claims by themselves.

### 4. Decision-generated opportunities

Search for uncertainty affecting real choices made by:

- statistical agencies;
- survey organizations;
- clinical or operational practitioners;
- standards bodies;
- researchers choosing estimators, validation procedures, or screening rules;
- policy or production teams allocating data-collection and quality-control effort.

A candidate is stronger when two or more independent channels converge on the same problem.

## Phase 0 — Define the candidate precisely

Write:

- one-sentence problem;
- proposed contribution;
- target population/context;
- estimand or output;
- closest known method;
- why it might matter;
- the decision or scientific interpretation the result could change.

Avoid vague labels such as “AI reliability” without a testable object.

## Phase 1 — Establish importance and decision need

Search for:

- systematic/scoping reviews;
- consensus or reporting guidance;
- deployment or production failures;
- empirical evidence that the problem occurs;
- repeated limitations across applied studies;
- agency or practitioner documentation showing that the uncertainty affects a real decision.

Ask both:

> Is this an actual scientific/statistical problem or merely an available technical exercise?

and:

> If the uncertainty were reduced, who would make a different or better decision?

Classify why the existing evidence is inadequate. Possibilities include:

- insufficient or imprecise information;
- biased information;
- inconsistent findings;
- implausible or untested assumptions;
- poor transportability to the target context;
- evidence that does not answer the actual decision question.

## Phase 2 — Search direct prior art

Use multiple formulations of the exact candidate.

Search:

- PubMed/biomedical indexes where relevant;
- Google Scholar or equivalent scholarly search;
- OpenAlex/Semantic Scholar where useful;
- arXiv/medRxiv/bioRxiv;
- conference proceedings.

Do not stop at title matches. Search conceptual synonyms and defining components.

## Phase 3 — Search methodological ancestors

Decompose the idea into components.

Example:

A + B + C may look novel, while established method M already solves A + B and paper N already connects B + C.

Search each pair and the underlying statistical object.

Old theory can eliminate apparent modern novelty.

## Phase 4 — Search terminology across communities

Different fields may describe the same phenomenon differently.

Create synonym families and search them separately.

Examples:

- dataset shift / distribution shift / transportability / domain shift;
- model updating / recalibration / dynamic validation;
- informative observation / informative visiting / endogenous sampling;
- uncertainty / coverage / abstention / selective prediction;
- nonprobability sampling / opt-in panels / volunteer samples / convenience samples;
- response quality / satisficing / fraud / bots / data integrity.

Record terminology collisions in the taxonomy file when they materially affect search.

## Phase 5 — Mine recurring limitations and assumptions

For a bounded set of the closest papers, extract:

- assumptions;
- limitations;
- unavailable variables or data;
- unsupported populations or settings;
- measurement or validation weaknesses;
- stated failure cases;
- future-work requests.

Cluster repeated themes rather than treating each paper in isolation.

A recurring independent limitation is stronger candidate evidence than one author's future-work sentence.

## Phase 6 — Search contradictions and heterogeneity

Look for credible studies that appear to disagree.

For each contradiction, ask:

1. Are the estimands actually the same?
2. Are populations, time periods, measurement processes, or interventions different?
3. Do methods rely on different assumptions?
4. Is there an unmodeled moderator or boundary condition?
5. Could both results be correct in different regimes?

A strong contribution may explain **when** an existing result holds rather than introduce an entirely new method.

## Phase 7 — Search authors' future-work statements

For nearest-neighbor papers, inspect:

- Discussion;
- Limitations;
- Future work.

Classify whether our candidate is:

- unrecognized;
- explicitly proposed;
- partially addressed;
- already answered.

An explicitly proposed extension is not automatically fatal, but it lowers conceptual originality and raises competition risk.

## Phase 8 — Search active work

This is mandatory for serious novelty claims.

Check:

- preprints;
- dissertations/proposals;
- conference programs;
- lab/project pages;
- grants when visible;
- GitHub repositories;
- recent commits/releases;
- current PhD projects.

Record the date checked.

## Phase 9 — Use citation-network and bibliometric discovery when helpful

For crowded, fragmented, or terminology-diverse fields, consider:

- backward citation chaining;
- forward citation chaining;
- co-citation networks;
- bibliographic coupling;
- temporal topic clusters;
- citation bursts;
- bridge papers connecting weakly linked communities.

Use these tools to discover research fronts and missing interfaces.

Do **not** treat sparse network structure as proof of novelty.

## Phase 10 — Run bounded empirical anomaly and replication searches when suitable

When informative public data or reproducible benchmarks exist, inspect whether important methods or claims fail under conditions that matter.

Potential signals include:

- another population or institution;
- another vendor or data source;
- another time period;
- realistic missingness or selection;
- altered measurement or observation processes;
- proper uncertainty propagation;
- subgroup-specific behavior;
- data cleaning or quality filtering that changes bias and variance in unexpected ways.

Required discipline:

> reproducible phenomenon → explanation question → theory/literature prosecution → confirmatory design

Do not promote a candidate solely because an exploratory analysis produced an unusual result.

## Phase 11 — Search practitioner, agency, and stakeholder pain points

Where relevant, inspect:

- statistical-agency research agendas;
- methodological and technical reports;
- standards documents;
- survey-organization research briefs;
- workshop proceedings;
- calls for proposals;
- production guidance;
- expert conversations.

Use these sources to establish relevance and uncover operational constraints that academic papers may omit.

Expert or practitioner opinion does not establish novelty.

## Phase 12 — Build a mini evidence-and-gap map when ambiguity remains

For the final few candidates, predefine useful dimensions such as:

- population;
- data source;
- error mechanism;
- estimand;
- method;
- outcome;
- validation setting;
- decision context.

Code the closest literature into the grid.

Use this selectively. Do not build a large evidence-mapping infrastructure for every candidate.

## Phase 13 — Nearest-neighbor table

Build a table where rows are the closest works and columns are the candidate's defining components.

The goal is to see whether novelty is:

- a genuinely missing capability;
- a consequential intersection;
- a boundary/failure-condition contribution;
- or merely an empty combinatorial cell.

For each closest work, record what it establishes and what it does not establish.

## Phase 14 — First-principles challenge

Ask:

1. What is observed?
2. What is latent?
3. What is the estimand?
4. Under what assumptions is it identified?
5. Can those assumptions be checked?
6. Could the method “work” computationally while the scientific claim remains assumption-driven?
7. What result would falsify the motivating story?
8. Are multiple error processes interacting in a way the proposed analysis ignores?

## Phase 15 — Feasibility audit

Evaluate:

- data access;
- data provenance;
- sample size/event count;
- required variables;
- required paradata or quality indicators;
- compute;
- software;
- supervision needs;
- timeline;
- reproducibility.

If the data-generation process is scientifically relevant, verify that harmonization has not erased required provenance.

## Phase 16 — Competitive-risk audit

Evaluate:

- number of active groups;
- whether leading groups have named the exact extension;
- pace of recent publications;
- existence of active software;
- whether the project can be executed before likely neighboring work appears;
- the marginal effort required to differentiate from the nearest competitor.

Competition should sharpen a candidate before it kills an entire neighborhood.

## Phase 17 — Decision-changing-information test

For every serious candidate, answer explicitly:

> Who currently has to make what decision without knowing this result?

Then ask whether the proposed study could realistically change:

- estimator choice;
- screening or quality-control thresholds;
- data-collection design;
- validation strategy;
- deployment or monitoring action;
- resource allocation;
- interpretation of an existing evidence base.

Use this as a lightweight value-of-information test.

Formal value-of-information analysis is optional and should only be used when it materially improves prioritization.

## Phase 18 — Verdict

Use one of:

### SURVIVES

A consequential, defensible contribution remains and is feasible.

### NARROW

The broad idea is occupied, but a meaningful subproblem remains. Re-prosecute the narrowed version.

### PARK

Interesting but poor fit now because of scope, competition, data, identification, or supervision.

### KILL

Prior art, first-principles analysis, data limitations, or lack of decision value removes sufficient value.

## Evidence discipline

For each major claim, record:

- source;
- date;
- what it establishes;
- what it does **not** establish;
- confidence.

Distinguish:

**Evidence:** what a paper/repository/data source directly says or demonstrates.

**Inference:** our interpretation.

**Exploratory signal:** a reproducible observation that has not yet survived theory and confirmatory scrutiny.

**Stakeholder signal:** evidence that a problem affects practice or decisions, but not evidence of novelty.

## Candidate-generation discipline

Do not rely on one discovery mode.

For each promoted candidate, record which channels support it:

- literature;
- theory;
- data;
- decision/practice.

Candidates supported by only one channel require more skeptical screening.

## Search stopping criterion

Do not aim for proof that no unpublished competitor exists.

Stop when:

- nearest prior art is well understood;
- recurring assumptions/limitations have been checked;
- contradictory findings, if any, are understood well enough;
- active-work checks are complete enough;
- contribution is explicit;
- the decision or scientific consequence is explicit;
- feasibility and data provenance are acceptable;
- residual novelty uncertainty is acceptable.

Then begin execution and maintain a lighter literature radar.

## Change log

### 0.2.0 — 2026-09-07

- Reframed discovery around four channels: literature, theory, data, and decision/practice.
- Added recurring limitation/assumption mining.
- Added contradiction and heterogeneity mining.
- Added citation-network/bibliometric discovery.
- Added bounded empirical anomaly and replication/failure discovery.
- Added practitioner/agency/stakeholder problem mining.
- Added mini evidence-and-gap mapping.
- Added explicit decision-changing-information/value-of-information screening.
- Strengthened evidence labels and search stopping criteria.
