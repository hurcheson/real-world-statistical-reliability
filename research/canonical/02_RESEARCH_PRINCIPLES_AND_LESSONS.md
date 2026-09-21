---
title: Research Principles and Lessons
version: 0.23.0
last_updated: 2026-09-21
status: active
---

# Research Principles and Lessons

## L001 — A gap is not necessarily a paper

An empty literature cell can be:

- trivial;
- unimportant;
- unidentifiable;
- data-infeasible;
- computationally unrealistic;
- empty because stronger researchers already tried and failed.

The target is a **consequential contribution**, not merely an unoccupied combination of keywords.

## L002 — Novelty does not mean “nobody has ever done anything close”

Research can be publishably novel through:

- method;
- theory;
- robustness;
- context;
- validation;
- measurement;
- contradiction;
- improved inference;
- better evaluation;
- useful simplification;
- external transportability.

The key question is:

> What can this paper claim that the closest existing paper cannot?

## L003 — Search to falsify novelty

A weak search asks:

> What supports my idea?

A strong novelty prosecution asks:

> What paper, preprint, dissertation, conference abstract, repository, or active group would make this idea redundant?

The search process should actively try to kill the candidate.

## L004 — Active work matters

Peer-reviewed literature is delayed.

Novelty surveillance must include, when relevant:

- arXiv/medRxiv/bioRxiv;
- dissertations and proposals;
- conference programs and abstracts;
- lab websites;
- grants;
- recent talks;
- GitHub repositories;
- active software development;
- current PhD projects.

The discovery of active PhD work materially changed the assessment of the informative-observation/BPV candidate.

## L005 — Exact-combination novelty is weak evidence by itself

The fact that nobody appears to have combined A + B + C + D does not establish a strong contribution.

Ask:

1. Does the combination solve a real problem?
2. Does it change identifiable knowledge?
3. Are the components already known to fit together?
4. Have leading authors already named the extension?
5. Is the technical burden justified?

## L006 — Identifiability precedes computation

A model can converge and still answer a question that is largely determined by unverifiable assumptions.

Before coding a sophisticated model, identify:

- the estimand;
- observed data;
- latent quantities;
- assumptions required for identification;
- sensitivity to those assumptions.

## L007 — Public data is an advantage, not a justification

Accessible data can make execution possible, but it does not make a weak question important or novel.

Question first; data fit second.

## L008 — Productive researchers build neighborhoods

High publication output usually comes from accumulating expertise in a problem family rather than rediscovering a new field for every paper.

A research neighborhood compounds:

- literature familiarity;
- methods;
- code;
- datasets;
- collaborators;
- vocabulary;
- open questions;
- reviewer/venue awareness.

## L009 — You cannot eliminate scooping risk

No search can reveal every unpublished project.

The rational target is:

> **defensible novelty under uncertainty.**

Once a candidate passes a reasonable threshold, execution speed becomes part of the strategy.

## L010 — Maintain a project portfolio

Long-term, a productive research program may contain projects at different stages:

- high-risk methodology;
- applied collaboration;
- validation study;
- simulation study;
- manuscript under review;
- backup candidate.

For the present phase, however, avoid overexpansion. Select one first execution project after the mapping stage.

## L011 — Stop searching when the project has earned execution

Endless novelty checking can itself become procrastination.

Once importance, differentiation, feasibility, and active-competition risk are acceptable:

**switch from discovery to monitoring and execute.**

## L012 — Do not overbuild the research system

A recurring personal failure mode identified in the conversation is designing systems before using them.

Therefore:

- no research OS;
- no agent swarm;
- no vector database;
- no elaborate dashboard;

until a repeated empirical need justifies it.

Markdown + evidence + one real project first.

## L013 — Killed ideas are assets

Do not delete failed candidates.

They preserve:

- what was searched;
- what was learned;
- nearest competitors;
- why the idea failed;
- conditions under which it might become viable later.

Failure records prevent expensive rediscovery.

## L014 — Separate research discovery from research execution

Research discovery asks:

- Is the problem important?
- Is there a defensible contribution?
- Can we execute it?

Research execution asks:

- What data?
- What estimand?
- What design?
- What code?
- What analysis?
- What manuscript?

Do not write substantial project code before discovery has passed its gate.

## L015 — Map interfaces between literatures, not only named topics

A promising research seam may sit between communities that use different assumptions and success criteria.

In the first reliability field map, four communities had to be connected:

- clinical prediction-model methodology;
- robust/distribution-shift ML;
- informative observation/missingness;
- post-deployment monitoring.

Searching only “missingness shift” or only “clinical external validation” would have produced a distorted novelty assessment.

## L016 — The data-collection process can be part of the predictive signal

Routine clinical data are generated by both patient physiology and healthcare processes.

Test ordering, visit frequency, charting intensity, interface availability and latency can all carry predictive information.

A model that exploits those signals may perform well internally yet fail to transport if the process changes.

Therefore, in real-world ML reliability research, model inputs should be classified not only by variable type but also by **how and why they were recorded**.

## L017 — Better metric reporting is not automatically a contribution

Once nearby work already evaluates:

- discrimination;
- calibration;
- recalibration;
- decision curves;
- subgroups;

a new paper cannot differentiate itself merely by adding those metrics to another external-validation dataset pair.

The contribution must instead come from a consequential scientific object, design, estimand, or actionable diagnosis.

## L018 — A close competitor should sharpen the candidate before it kills the neighborhood

Discovering direct active work does not necessarily mean abandoning the entire research area.

The correct response is:

1. identify exactly what the competitor establishes;
2. identify what it does not establish;
3. narrow the candidate to a consequential surviving claim;
4. kill the candidate if the surviving claim becomes trivial or infeasible.

This happened during C008 screening: direct 2026 MIMIC/eICU work eliminated a shallow “observation features hurt transfer” project but left a narrower question about **attribution and stress testing** worth screening.

## L019 — Preserve provenance when the data-generation process is the object of study

Harmonization can be scientifically useful, but when the research question concerns measurement or observation processes, source-specific provenance may be part of the signal.

Therefore multi-database work should preserve:

- original variable/source definitions;
- site/unit identifiers where permitted;
- interface/availability information;
- timing/frequency metadata;
- transformation/harmonization lineage.

A common data model should not erase the mechanism the study is trying to understand.

---


## L020 — Competitive geometry is part of feasibility, not a proxy for prestige

**Lesson:** Do not reject a field merely because famous groups work in it. Reject or park a first-project frontier when the combination of direct competition, prerequisite breadth, data/compute burden and expected marginal differentiation is unfavorable.

**Origin:** C008 remained scientifically interesting but required too many simultaneous competencies beside direct 2025–2026 competitors.

**Operational rule:** Compare *marginal effort required for a defensible contribution*, not the fame of neighboring researchers.

---

## L021 — Assumption interfaces are better candidate generators than empty topic labels

**Lesson:** A mature method often has a compact assumption that connects it to another literature. Those boundaries can produce sharper projects than adding another estimator or application.

**Origin:** Probability/nonprobability integration depends on shared auxiliary variables; survey-measurement work shows cross-source measurement equivalence can fail.

**Operational rule:** For every method family, list which objects are assumed known, common, error-free, transportable or ignorable. Search each assumption as a possible failure mode before generating method extensions.

---

## L022 — Identification should precede correction

**Lesson:** When selection and measurement error interact, do not jump to a bias-corrected estimator. First establish what is identified from the observed data and what requires validation information or sensitivity parameters.

**Origin:** C009 may involve latent true adjustment variables observed differently in two sources; without bridge/validation information, source measurement and selection can be confounded.

**Operational rule:** Classify no-validation, known-error and validation-sample regimes before writing correction algorithms.

---

## L023 — Public methodological datasets can be strategic assets

**Lesson:** A dataset designed to study survey methodology can be more valuable than a larger generic dataset because its provenance, modes, weighting and paired sample structures support inferential questions directly.

**Origin:** CDC/NCHS RANDS rounds 8–10 provide public probability and opt-in nonprobability samples with detailed documentation.

**Operational rule:** Prefer data whose collection mechanism is part of the scientific design, not merely data with more rows.



## L024 — A bridge sample is not automatically a validation sample

**Lesson:** Measuring two fallible versions of a construct on the same units does not by itself identify the latent construct or both measurement processes.

**Origin:** In C009's binary toy model, two fallible measurements in one population give fewer observed degrees of freedom than prevalence plus both sensitivities/specificities [R119].

**Operational rule:** Specify exactly what a bridge design identifies. Distinguish (a) a bridge that estimates a target benchmark on the other source's measurement scale from (b) a true validation design with gold-standard or otherwise identifying information.

---

## L025 — Search old survey-methodology and working-paper literatures before claiming a modern interface gap

**Lesson:** A problem that looks new because two modern literatures use different terminology may already have a close ancestor in older survey-statistics work.

**Origin:** Chambers' 2008 working paper [R113] directly studied calibration when the available auxiliary population value is erroneous or belongs to a closely related but non-identical variable, materially narrowing C009.

**Operational rule:** During methodological prosecution, citation-chain backwards through calibration, measurement-error and official-statistics literatures, including institutional working papers—not only recent journal/preprint searches.

---

## L026 — Decompose interacting errors before proposing a correction

**Lesson:** When selection and measurement incompatibility coexist, a useful contribution may be to separate failure mechanisms rather than immediately invent a combined estimator.

**Origin:** C009's toy model separated wrong-scale benchmark bias from residual selection bias due to noisy proxy adjustment. The two components require different information to resolve.

**Operational rule:** Derive mechanism-specific bias components and information requirements first; only build correction machinery if the decomposition yields a distinct, decision-relevant target.

## L027 — Use multiple independent channels to discover research opportunities

Gap discovery should not be dominated by literature search alone.

Use four complementary channels:

1. **Literature-generated opportunities** — prior art, interfaces, assumptions, limitations, contradictions, citation networks, methodological ancestors, and active work.
2. **Theory-generated opportunities** — estimands, identification failures, bias decompositions, sensitivity, boundary cases, and assumption relaxation.
3. **Data-generated opportunities** — reproducible anomalies, cross-dataset failures, benchmark audits, subgroup failures, temporal instability, and failed replications.
4. **Decision-generated opportunities** — agency pain points, practitioner problems, statistical-production decisions, stakeholder priorities, and uncertainty that affects a real choice.

A candidate is especially attractive when two or more channels independently point to the same problem.

## L028 — Distinguish an evidence gap from a research need

A sparse literature does not automatically imply that new research is worth doing.

Ask not only:

> What is missing from the literature?

but also:

> Why is the existing evidence inadequate, and what decision would improve if the uncertainty were reduced?

Existing evidence may be inadequate because it is:

- imprecise;
- biased;
- inconsistent;
- based on implausible assumptions;
- unrepresentative of the target setting;
- unable to answer the actual decision question.

This converts gap hunting from empty-cell detection into reliability diagnosis.

## L029 — Mine recurring limitations and assumptions, not isolated future-work sentences

A single paper's limitation is weak evidence of a field-level opportunity.

Across the closest literature, extract and cluster recurring statements about:

- assumptions;
- missing variables or unavailable data;
- unsupported populations or settings;
- failure cases;
- measurement limitations;
- validation limitations;
- future-work requests.

Repeated independent limitations are stronger candidate signals than one author's suggestion.

## L030 — Contradictions can be more valuable than empty literature cells

When credible studies reach different conclusions, do not treat the disagreement merely as noise.

Ask:

> Under what conditions does each result hold?

A contribution may consist of identifying the moderator, boundary condition, failure regime, or hidden assumption that reconciles apparently conflicting results.

This is often more consequential than studying a topic no one has examined.

## L031 — Empirical anomalies can generate questions, but they do not validate themselves

A bounded exploratory analysis of informative public data can reveal:

- methods that help some outcomes but harm others;
- unexplained panel/site differences;
- temporal instability;
- subgroup-specific failures;
- unexpected interactions between cleaning, weighting, measurement, and selection.

The correct workflow is:

> reproducible phenomenon → explanation question → theory/literature prosecution → confirmatory design

Do not convert exploratory anomalies directly into causal or general scientific claims.

## L032 — Replication and failure analysis are legitimate contribution generators

Do not restrict novelty search to new estimators or new combinations of methods.

A strong project may show that an influential result or method fails under a scientifically important condition that has not been adequately tested, such as:

- another population;
- another institution or vendor;
- another time period;
- a realistic measurement process;
- realistic missingness or selection;
- proper uncertainty propagation.

The contribution must identify why the failure matters and what can be learned from it, not merely report that performance decreased.

## L033 — Bibliometric structure is a discovery aid, not proof of novelty

When a field is difficult to map manually, use citation-network and bibliometric tools where useful:

- backward and forward citation chains;
- co-citation networks;
- bibliographic coupling;
- temporal topic clusters;
- citation bursts;
- bridges between weakly connected communities.

These tools can reveal emerging fronts and disconnected literatures, but sparse connectivity does not by itself establish a publishable gap.

## L034 — Practitioner and agency pain points are valid research signals

Methodological reports, statistical agencies, standards bodies, survey organizations, domain practitioners, workshops, calls for proposals, and direct expert conversations can expose important problems that the journal literature describes poorly.

Use these signals to establish relevance and decision need.

Do not treat practitioner demand as a substitute for novelty, identification, or feasibility analysis.

## L035 — Apply a decision-changing-information test

For every serious candidate, ask:

> Who currently has to make what decision without knowing this result?

Then ask whether the proposed study could realistically change:

- estimator choice;
- screening or quality-control thresholds;
- data-collection design;
- validation strategy;
- deployment decision;
- monitoring action;
- resource allocation;
- interpretation of an existing evidence base.

This is a lightweight value-of-information discipline. Formal value-of-information analysis is optional, not mandatory.

## L036 — Use structured evidence-gap maps selectively

For the final few ambiguous candidates, a mini evidence-and-gap map can be more informative than unstructured searching.

Predefine dimensions such as:

- population;
- data source;
- error mechanism;
- estimand;
- method;
- outcome;
- validation setting.

Then code the closest literature into the grid.

Use this selectively; do not build a large mapping infrastructure before a candidate warrants the effort.

## L037 — Expert elicitation is for prioritization, not novelty certification

Independent conversations with domain experts can reveal hidden assumptions, practical failure modes, inaccessible data constraints, and high-value questions.

Expert agreement can increase confidence that a problem matters, but it cannot establish that the problem is novel.

Novelty still requires literature and active-work prosecution.

## L038 — Candidate confidence should rise when independent discovery channels converge

The strongest early signal is not one impressive search result.

Confidence should increase when, for example:

- recurring literature limitations identify a problem;
- first-principles analysis explains the mechanism;
- public data show the phenomenon;
- practitioners face a real decision affected by it.

Conversely, a candidate supported by only one channel should receive more skeptical screening.

## L039 — Data cleaning can be an inferential selection intervention

When a cleaning rule removes observations from the analytic sample, do not assume it only reduces measurement error.

If exclusion depends on variables related to the estimand, outcome, participation mechanism, subgroup membership or unmeasured determinants of those quantities, the cleaning rule creates an additional selection event. Reweighting the retained sample repairs that event only under explicit exchangeability/balance conditions.

**Origin:** C010 response-quality filtering prosecution.

**Operational rule:** For every exclusion/filtering rule, write the retained-sample indicator into the data-generating process and ask what must be true for the target estimand to remain identified after conditioning on it.

## L040 — Classification accuracy and inferential utility are different objectives

A respondent-quality screen should not be tuned only to sensitivity, specificity or aggregate classification accuracy if the downstream goal is a population estimand. False-positive exclusion, false-negative retention, changing overlap, weight inflation and outcome-dependent errors can have asymmetric inferential costs.

**Origin:** C010 threshold analysis plus Pew/Gallup screening evidence [R129–R131].

**Operational rule:** When a classifier changes the analysis sample, evaluate thresholds against the downstream estimand's bias/MSE/robustness, not only respondent-level classification metrics.

## L041 — “No gold standard” is an identification condition, not a novelty claim

If a latent quality/validity state is not observed, false-positive and false-negative rates are not automatically known. Multiple imperfect screens may still require strong latent-class assumptions, and bounded error rates lead into established partial-identification territory.

**Origin:** C010 prosecution and comparison with no-gold-standard test-accuracy methods [R141] and bounded misclassification [R121].

**Operational rule:** State what validates a screen. If no credible validation source exists, either derive a genuinely new structure-specific identification result or treat classifier accuracy as a sensitivity/partial-identification problem rather than assuming it.

## L042 — “No candidate” is a valid output of bounded triage

A research pipeline should not force promotion merely because a bounded set of ideas has been exhausted. If every broad opportunity is already occupied or lacks a defensible identification/data path, assigning the next candidate ID creates false momentum and weakens the novelty gate.

**Origin:** OF-19–OF-23 collapse-first triage. All five broad formulations failed promotion; OF-22 retained only a sharpen-before-candidate residue [R142, R145].

**Operational rule:** Candidate identifiers are earned, not sequential obligations. When a bounded slate collapses, return to opportunity generation with the failure records as constraints.

## L043 — Temporal drift is not identified by change alone

In repeated surveys, a change in the observed NPS distribution or in an estimated trend does not uniquely identify drift in the participation mechanism. Population composition, outcomes, measurement, vendor/recruitment processes and selection can all change over time.

**Origin:** OF-22 triage and comparison of recurring-hybrid work [R142] with refreshment-sample selection diagnostics [R145].

**Operational rule:** A drift candidate must state what is anchored across waves and what reference information makes selection drift distinguishable from genuine population or measurement change.

## L044 — A finite benchmark set is a validation design, not a universal quality certificate

Low bias on observed benchmark variables does not, by itself, establish low bias for every unbenchmarked target outcome.

For discrepancy `B(f)=E_Q[f]-E_P[f]`, if a target can be written as `f=a+beta^T G+r` for observed benchmark vector `G`, then `B(f)=beta^T B(G)+B(r)`. Benchmark success controls the target only to the extent that the residual discrepancy is also controlled by an explicit target class, structural assumption, validation design or sensitivity bound.

**Origin:** fresh D013 four-channel generation and OF-30, motivated by Pew's explicit warning that benchmark bias need not transfer to political-attitude targets [R150] and NCHS's evolving benchmark-selection practice [R148].

**Operational rule:** When using benchmarks to call a source/method “high quality,” state what class of unbenchmarked targets the claim is intended to cover. Prefer held-out/leave-domain-out validation and keep benchmark variables used for tuning distinct from those used for final certification where feasible.

## L045 — A survey-level quality signal is not a statistic-level guarantee

Survey methodology already contains explicit warnings and theory showing that nonresponse/selection bias is attached to a particular statistic or survey variable, even when organizations want a single survey-level quality indicator. R-indicator validation work shows that more imbalance/bias in auxiliary information does not automatically imply more bias in other survey variables [R161–R164].

For finite external benchmarks, the same principle applies: held-out target reliability is not identified unless an explicit target class, outcome-superpopulation, covariance structure or outcome-specific selection model links the target to the observed benchmarks.

**Origin:** bounded OF-30 screening.

**Operational rule:** Treat global quality scores as decision summaries, not universal certificates. When validating them, use nested grouped/leave-domain-out outcomes, exclude mechanically calibrated targets, and state the outcome universe over which any generalization claim is intended to hold.

## L046 — Search for the classical statistical object before promoting a stronger guarantee

A recent paper can expose a genuine weakness while the natural repair already exists under an older name. In the cross-field reconnaissance, concern about the distribution—not only the mean—of random-effects prediction-interval coverage suggested high-confidence content coverage. That object is already a tolerance interval in meta-analysis [R174–R175].

**Operational rule:** Before promoting a new guarantee, translate its defining property into classical statistical nouns—tolerance interval, calibration, partial identification, selective inference, measurement error, decision regret, and related concepts—and search those ancestors directly.

## L047 — Review-first reconnaissance is a distinct discovery mode

Mechanism-first discovery asks whether a hypothesized new method has been done. Review-first discovery instead starts from an active statistical field, maps what reviews and current methods say is unresolved, then attacks the apparent opening with classical ancestors and active work.

**Origin:** cross-field reconnaissance in `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

**Operational rule:** When repeated candidate-first searches collapse, do not merely generate more combinations. Sample several current statistical reviews, extract unresolved assumptions/failures/decisions, then formulate leads only after direct-method and ancestor searches.

## L048 — Under incomplete outcomes, model evaluation is itself an inference problem

Prediction metrics such as Brier score or AUC may be well defined for the latent fully observed outcome while their estimators from censored/interval-censored observations depend on assumptions about censoring, assessment and nuisance models [R179–R183]. A failure can therefore arise from the **evaluation estimator or observation mechanism**, not from the prediction model or metric definition itself.

**Operational rule:** Separate `(i)` the target score/estimand, `(ii)` the observed-data estimator, and `(iii)` the observation/assessment mechanism before calling an evaluation metric unreliable.

## L049 — Ranking reliability is a decision target distinct from average metric accuracy

An evaluation procedure can estimate each model's score with modest average bias yet still choose the wrong model if differential errors reverse their ordering. For model selection, pairwise ranking-reversal probability, wrong-winner probability and selection regret can be more decision-relevant than the marginal bias of a score estimator.

Right-censoring work already demonstrates that some scoring constructions can reverse the oracle ranking [R179]. OF-35 asks whether interval censoring plus recurrent assessment creates a distinct version of this problem.

**Operational rule:** When evaluation is used to select a model/method, analyze the probability and consequence of selecting the wrong winner—not only per-model metric bias or coverage.

## L050 — A new decision summary is not automatically a new statistical contribution

Wrong-winner probability and selection regret can be scientifically useful, but if existing simulations already produce oracle and observed-data scores for multiple competing models, these quantities may be direct transformations of existing output. For two models, ranking reversal is determined by whether differential evaluation error crosses the oracle performance gap.

**Operational rule:** When proposing a new decision metric, write it algebraically in terms of quantities the nearest paper already estimates. If it is mechanically recoverable, novelty must come from a new distributional result, identification/bound, guarantee, intervention or decision rule—not the summary statistic alone.

## L051 — Search the problem sentence across adjacent mechanisms

OF-35 initially looked more distinct when searches were centered on “interval censoring.” A broader search for the actual problem sentence—**oracle versus observed survival-model evaluation and preservation of model ranking**—surfaced a 2026 ICML paper directly studying that question under right censoring [R189].

**Operational rule:** Before promoting a mechanism-specific variant, search the same estimand, decision and failure mode across adjacent observation mechanisms and neighboring venues. A change in censoring/missingness type is not a contribution unless it creates demonstrably new statistical structure.

## L052 — Stop computation when the novelty gate has already failed

A toy simulation is valuable when it tests whether a proposed phenomenon exists or is nontrivial. It is not valuable as a rescue device after current literature already demonstrates the phenomenon and supplies the same oracle-versus-observed design.

**Operational rule:** If nearest-neighbor prosecution already collapses the contribution claim, do not spend compute reproducing plausibility. Record the negative result and redirect the search.

## L053 — Distinguish score validity from pairwise oracle-ranking equivalence

A strictly proper observed-data score under censoring assumptions establishes an important validity property, but it does not automatically imply that every pair of misspecified prediction models will be ordered exactly as under a different fully observed oracle score. These are related but distinct claims.

**Operational rule:** In evaluation research, distinguish (i) propriety/consistency for the truth, (ii) bias of a score estimator, (iii) pairwise ranking preservation among candidate models, and (iv) top-model selection regret. Do not use one as evidence for another without a theorem or explicit experiment.

## L054 — Re-audit model checking when data collection becomes outcome-adaptive

Correcting point estimation under an adaptive design does not establish that ordinary diagnostics, goodness-of-fit tests or uncertainty procedures retain their nominal reference laws. When the design depends on previous outcomes, the realized design object may cease to be ancillary.

**Operational rule:** Whenever current work repairs estimation under adaptive sampling/scheduling, separately audit the downstream diagnostic law and condition on only genuinely ancillary design components.

## L055 — A replay bootstrap is not a contribution when replay is already established

If prior work already simulates the full adaptive data-collection algorithm inside a parametric bootstrap, proposing the same replay mechanism for a neighboring statistic is an implementation transfer, not by itself a research contribution.

**Operational rule:** Require a new failure theorem, calibration result, validity argument, power result or diagnostic insight. “Put the scheduler inside the bootstrap” is insufficient when that principle is prior art.

## L056 — Exact null calibration is a high-value early gate for diagnostic-reliability ideas

Diagnostic-reliability opportunities often become testable before a full application study. Under a correctly specified generative model, the first question is whether the nominal rejection probability is actually nominal under the real data-collection mechanism.

**Operational rule:** Define a null-calibration target such as `P(p <= alpha) - alpha` early. If it is negligible under realistic mechanisms, kill the lead before developing elaborate corrections; if it is material, then investigate the structural reason and only afterward power/application behavior.

## L057 — Sequential predictability is not the same as final-design ancillarity

An adaptive design can choose the next covariate/pair using past outcomes while preserving a martingale score under the null. Yet the final realized design can still be non-ancillary, so conditioning on that final design can change the law of the previous outcomes.

**Operational rule:** Separate sequential conditional validity from inference conditional on the completed adaptive design. Do not infer one from the other.

## L058 — Use a frozen-design twin to isolate adaptive endogeneity from topology

Adaptive designs often change graph sparsity, balance and leverage at the same time they create outcome–design dependence. Comparing an adaptive dataset with fresh outcomes regenerated on the exact same realized design isolates the endogeneity component.

**Operational rule:** For adaptive-design reliability questions, include an exact frozen-design twin before attributing any failure to adaptivity.

## L059 — Sparse-GOF failure is a confound, not evidence of adaptive failure

Pearson/deviance reference laws can be poor when there are few observations per covariate pattern or pair cell, even under nonadaptive designs. Adaptive schedules can exacerbate or reshape this sparsity, but the two mechanisms must be prosecuted separately.

**Operational rule:** Any adaptive GOF claim must benchmark against a nonadaptive/frozen design with the same effective sparsity and leverage structure.

## L060 — Information-efficient designs can be model-checking inefficient

A scheduler optimized to compare near-equal items can improve parameter/ranking information while reducing exposure to regions where certain model misspecifications are most visible. Diagnostic power is therefore a design property, not merely a property of the test statistic.

**Operational rule:** After calibrating Type-I error under adaptive sampling, test power across structurally different departures. A design that is efficient for estimation may be weak for model discrimination.

## L061 — Exact counterexamples can prove a failure without proving a contribution

A finite-state enumeration can decisively establish that an inferential reference is wrong, yet the resulting theorem may still be too mechanically implied by known non-ancillarity or generic resampling theory to support a new project. Phenomenon existence and contribution novelty are separate gates.

**Operational rule:** After an exact counterexample succeeds, write the general proposition and identify which step is genuinely new. If the proof is only “condition on the scheduler-compatible path set” plus “replay the same null experiment,” treat it as a program lesson unless a statistic-specific fitted-parameter result, computable correction, power theorem or decision rule adds non-generic content.


## L062 — A live standards transition is not itself a new statistical method

When an agency changes a classification or reporting standard, official bridge tools may be preliminary and downstream statistics may be visibly discontinuous. That creates an important reliability problem, but classical harmonization, misclassification and quantitative-bias methods can already occupy the generic correction/uncertainty layer.

**Operational rule:** For standards-transition opportunities, abstract first to the transition/misclassification matrix. Promote only a residual object that changes a downstream decision — for example a sharp robustness region, sign/ranking/trend tipping condition, or validation result tied to documented heterogeneity — and kill any proposal that is merely “apply uncertainty propagation to the new standard.”


## L063 — Translate category bridges into generic matrix-identification form before inventing a robustness theorem

A standards crosswalk or bridge can look application-specific because the categories have substantive meaning, but once the bridge is represented as a stochastic transition/misclassification matrix, generic partial-identification results may already provide sharp regions for arbitrary downstream functionals under restrictions on that matrix. A sign/ranking “tipping point” is then often only the event that the identified region crosses zero or an ordering boundary.

**Operational rule:** Before deriving a bridge-specific robustness certificate, write the problem as `q = Bp` (or the corresponding conditional/outcome version), define the admissible matrix set, and search generic misclassification/partial-identification and matrix-method literatures. If the proposed theorem is just optimization of an already-covered functional over that set, stop unless new structural restrictions, inference, design, or decision theory create non-generic content.

## L064 — A precision screen is a selection intervention, and downstream caps can make its effects nonlocal

A hard uncertainty threshold does more than improve the precision profile of retained estimates. When pass/fail depends on relative uncertainty, the screen selectively changes which units enter a downstream decision. If a later ranking or population/resource cap reallocates among the remaining units, screening one unit can change the decision received by another unit whose own estimate, uncertainty and substantive eligibility never changed.

D033 provides a concrete example: HUD's tighter QCT MoER screen produces both population-dependent eligibility loss and hundreds of strict nonlocal designation gains through the 20% cap.

**Operational rule:** evaluate precision screens with a same-data policy replay before treating them as benign quality control. Decompose (i) direct screen passage, (ii) substantive eligibility, (iii) ranking changes, and (iv) nonlocal cap/allocation displacement; condition coverage effects on substantive-threshold proximity; and keep observable precision/coverage claims separate from latent accuracy claims.

## L065 — Separate the discovery year from the confirmatory replication set

Once an empirical anomaly or effect size has helped a candidate survive, that same dataset is no longer an untouched confirmation set. Reusing it as the primary confirmatory benchmark hides researcher degrees of freedom created during discovery.

D033 used the 2026 QCT workbook to discover and quantify C011. D034 therefore freezes 2026 as a development/anchor year and reserves 2016–2025 for prospective multi-year replication under a pre-specified protocol.

**Operational rule:** after candidate promotion from an empirical development dataset, freeze estimands, decomposition rules, robustness analyses and stop criteria before inspecting the replication set. Preserve the development result as a regression-test fixture, not as independent confirmation.

## L066 — Exact historical reconstruction is itself a feasibility gate, not a nuisance to optimize away

A prospective policy-replay study can fail its replication design even when the underlying empirical mechanism remains visible. Historical agency outputs may depend on undocumented geography vintages, stale or incomplete workbooks, hidden preprocessing, or threshold-dependent intermediates that cannot be regenerated from the public record. If exact reconstruction was pre-specified as the admission rule, these are scientific feasibility failures of the planned design—not invitations to add a mismatch tolerance or tune undocumented conventions until the flags match.

C011 illustrates the distinction. Four confirmatory years reconstruct exactly and show consistent precision-screen coverage, population-burden and nonlocal allocation effects, while four other years remain non-exact for heterogeneous provenance reasons. Once the frozen 7/10 exact-year criterion became mathematically unattainable, the correct action was to pause decade generalization even though the exact-year effects remained consequential.

**Operational rule:** pre-specify reconstruction admissibility before historical outcomes are inspected. When the gate fails, separate **mechanism evidence** from **generalization-design feasibility**. Preserve exact-year results and diagnostic near-reconstructions, but do not rescue the original claim with post-hoc tolerances, forbidden oracles or undocumented implementation guesses. Reopen only on genuinely new authoritative operational evidence or through an explicit scope reassessment.


## L067 — Reconstruction-based inclusion can create generalizability selection even without outcome peeking

A prospectively frozen exact-reconstruction gate protects against ordinary outcome-driven cherry-picking when non-admitted units never have their counterfactual outcomes inspected. It does **not** make the admitted set representative. Reconstructability may depend on data preservation, geography changes, operational complexity, undocumented preprocessing or other features that can also affect the scientific mechanism.

C011 demonstrates the distinction. The four exact confirmatory years were admitted by a zero-mismatch rule fixed before their counterfactuals were inspected, while the non-exact years' `c=1.00` gates remained closed. This materially strengthens the integrity of the exact-year evidence. Yet those four years cannot be treated as a random sample of 2016–2025, and their medians/ranges cannot be promoted to decade-level estimates.

**Operational rule:** when a provenance/reconstruction gate fails, a transparent post-stop scope reduction may preserve a scientifically useful project, but only if the narrowed evidence set is labeled as such. Show the full admissibility table, avoid missing-at-random assumptions or post-hoc weighting for unavailable outcomes, preserve unopened outcomes, and distinguish recurrence within reconstructable cases from frequency or representativeness in the original target set.

## L068 — Historical execution success and manuscript reproducibility are different gates

A result can pass a prospective execution gate at analysis time yet later become inadmissible for publication if the computational provenance needed to regenerate it was not durably retained. Historical result status must therefore be distinguished from current manuscript admissibility.

C011 illustrates the distinction. Historical execution recorded Tier-A results for 2016, 2020, 2021 and 2022, but the final manuscript-grade reproducibility adjudication could fully regenerate only 2016. The other three results remain diagnostics of what the historical execution reported; they are not currently manuscript-admissible evidence. This does not scientifically falsify the precision-screen mechanism demonstrated by the 2016 replay. It closes the four-year recurrence claim under the evidence now preserved.

**Operational rule:** for computational policy/statistical research, preserve enough durable state when a result is generated to recreate it without conversational memory:

- immutable input hashes;
- source provenance;
- environment lock;
- exact code commit;
- machine-readable rule configuration;
- processed intermediate tables;
- deterministic output digests;
- regression tests;
- figure/table source data.

A remembered result is a diagnostic, not reproducible evidence.

## L069 — A useful task utility is not automatically a new statistical object

C012 showed that a nonlinear decision-certification score can have valid and operationally interesting behavior while remaining a plug-in objective inside an established release-optimization framework. Promotion requires more than objective mismatch: a new guarantee, identification result, mechanism, scalable algorithm, or empirically consequential inferential object must survive.

## L070 — Release year is not observation time

For modeled public-data products, temporal indexing must be reconstructed at the `release × measure × source-year` level before any trend, lag, persistence or pre/post interpretation. A sequence of files can contain fewer distinct temporal observations than its release count suggests.

## L071 — Exact carry-forward detection is both a falsification test and an effective-sample-size audit

When geography-level values, intervals and ranks are identical across nominally adjacent releases, the later file supplies no new outcome wave for that measure. Removing deterministic copies is not a robustness flourish; it is required to state the temporal sample size honestly.

## L072 — A bounded non-reproduction is stronger than speculative error language

When public descriptions omit release IDs, code, weighting or spatial-neighbor rules, test the natural archive mappings and report what they do and do not reproduce. If none matches, classify the result as bounded non-reproduction or non-adjudicable. Do not call a named analysis erroneous without exact reconstruction and a fair alternative.

## L073 — An agency warning does not eliminate the value of an empirical downstream audit

CDC already warns that PLACES should not be used to track local change. C013 survives because it operationalizes that warning: it measures effective source-wave counts, identifies deterministic carry-forwards and discontinuities, and tests whether published decision statements change. The contribution must remain this empirical audit rather than rebranding the warning as a discovery.

## Change log

### 0.23.0 — 2026-09-21

- Added L070–L073 from C013: source-time reconstruction, exact-copy auditing, bounded non-reproduction and the distinction between agency warning and downstream audit.

### 0.22.0 — 2026-09-21

- Added L069 from the C012 kill: a useful task utility is not automatically a new statistical object.

### 0.21.0 — 2026-09-17
- Added L068: historical execution success and current manuscript reproducibility are distinct gates.
- Recorded the minimum durable computational state required to preserve manuscript admissibility.

### 0.20.0 — 2026-09-09
- Added L067 from D036: reconstruction-based inclusion can induce generalizability selection even without counterfactual outcome peeking; scope reduction must remain transparent and nonrepresentative.

### 0.19.0 — 2026-09-09
- Added L066 from D035: exact historical reconstruction is a pre-specified feasibility gate; distinguish mechanism evidence from generalization-design feasibility and do not optimize away provenance failures.

### 0.18.0 — 2026-09-08
- Added L065 from D034: once a development dataset helps select a candidate, reserve untouched data/years for confirmatory replication and freeze the protocol before inspecting them.

### 0.17.0 — 2026-09-08
- Added L064 from D033: precision screening is a selection intervention and downstream caps can create nonlocal effects.
- Repaired the duplicated lesson identifier by renumbering the OF-44 matrix-identification lesson from L062 to L063; lesson substance is unchanged.

### 0.16.0 — 2026-09-08

- Added L063 from OF-44: translate standards bridges to generic matrix-identification form before claiming a new robustness/tipping theorem.

### 0.15.0 — 2026-09-08

- Added L062 from D027: a live classification-standards transition is an important reliability setting, but generic bridging/misclassification uncertainty is prior art; require a distinct downstream decision-robustness object.

### 0.14.0 — 2026-09-08

- Added L061 from the OF-39 exact gate: an exact failure theorem does not by itself establish a distinct research contribution when it is mechanically inherited from known non-ancillarity and replay logic.

### 0.13.0 — 2026-09-08

- Added L057–L060 from the OF-39 prosecution: sequential predictability versus final-design ancillarity, frozen-design controls, sparse-GOF confounding, and estimation-versus-diagnostic design efficiency.

### 0.12.0 — 2026-09-08

- Added L054 on separate diagnostic audits under adaptive data collection.
- Added L055: an already-established replay bootstrap is not a contribution by itself.
- Added L056: use exact null calibration as an early diagnostic-reliability gate.

### 0.11.0 — 2026-09-07

- Added L050: a new decision summary is not automatically a new statistical contribution.
- Added L051: search the problem sentence across adjacent mechanisms.
- Added L052: stop computation when the novelty gate has already failed.
- Added L053: distinguish propriety from pairwise oracle-ranking equivalence.

### 0.10.0 — 2026-09-07

- Added L046 on classical-object ancestor searches before promoting stronger guarantees.
- Added L047 formalizing review-first cross-field reconnaissance as a discovery mode.
- Added L048–L049 separating incomplete-outcome evaluation inference from model quality and elevating ranking reliability as a decision target.

### 0.9.0 — 2026-09-07

- Added L045: a survey-level quality signal is not a statistic-level guarantee.

### 0.8.0 — 2026-09-07

- Added L044: a finite benchmark set is a validation design, not a universal quality certificate.

### 0.7.0 — 2026-09-07

- Added L042: no candidate is a valid output of bounded triage.
- Added L043: temporal change alone does not identify participation-mechanism drift.

### 0.6.0 — 2026-09-07

- Added L039: cleaning can be an inferential selection intervention.
- Added L040: classification accuracy and inferential utility are distinct objectives.
- Added L041: lack of a gold standard is an identification condition, not a novelty claim.

### 0.5.0 — 2026-09-07

- Added the four-channel research-opportunity discovery framework.
- Added evidence-gap versus research-need distinction.
- Added recurring limitation/assumption mining and contradiction mining.
- Added empirical anomaly, replication/failure, bibliometric, practitioner/agency, and expert-elicitation strategies.
- Added decision-changing-information and selective evidence-gap-map principles.
- Added convergence across independent discovery channels as a candidate-confidence criterion.
- Normalized previously duplicated lesson IDs so every principle now has a unique canonical number; lesson substance was unchanged.

### 0.4.0 — 2026-09-07

- Added lessons on bridge-versus-validation designs, older methodological ancestors, and decomposition before correction.

### 0.3.0 — 2026-09-07

- Added lessons on competitive geometry, assumption interfaces, identification-before-correction, and methodological datasets.

### 0.2.0 — 2026-09-07

- Added lessons from the first deep field-mapping pass: interface mapping, observation-process signal, contribution versus metric expansion, competitor-driven sharpening, and provenance preservation.
