---
title: C012 Decision-Preserving Disclosure Prosecution
version: 1.0.0
last_updated: 2026-09-17
status: final-killed
decision: KILL / NO-GO FOR FIRST PAPER
---

# C012 decision-preserving disclosure prosecution

**Date:** 2026-09-17  
**Final disposition:** **KILL**

## Binding adjudication

“Decision-preserving disclosure control” is a legitimate task-specific utility objective, but the prosecution does not support it as a genuinely new statistical contribution. The complete idea can be implemented by taking an established optimal-release framework, defining the permitted release actions and disclosure constraints, and replacing its conventional information-loss objective with a decision-certification score. That is precisely the binding kill condition.

The experiments establish useful behavior—monotonicity, safe release synergy, non-submodularity, non-supermodularity, decision identification without cell identification, and divergence from cell-width utility. None of those findings supplies a new privacy definition, identification theory, release mechanism, scalable algorithm, or inferential result. They characterize one nonlinear task utility inside a well-established risk–utility/workload-aware design template.

## Question prosecuted

Does selecting disclosure-safe releases to preserve geographic ranking, top-*k*, and threshold conclusions define a new statistical problem, or is it an instance of existing optimal tabular release and task-aware privacy in which the analyst substitutes a downstream decision utility for a generic accuracy/information-loss utility?

The answer is the latter.

## Formal release-design problem

Let (x^\star\in\mathbb Z_+^p) be the agency-held confidential table. A baseline public release (R_0) induces the compatible fiber

\[
\mathcal F(\varnothing)=\{x\in\mathbb Z_+^p:\ell\le x\le u,\;A_0x=b_0,\;G_0x\le h_0\}.
\]

Let (\mathcal A=\{a_1,\ldots,a_m\}) be candidate release actions. In the experiment, an action publishes an exact subset sum (a_j(x^\star)); more generally an action may publish a margin, perturbed query, coarser category, or cell. For an action set (S\subseteq\mathcal A),

\[
\mathcal F(S)=\{x\in\mathcal F(\varnothing):a_j(x)=a_j(x^\star)\text{ for every }a_j\in S\}.
\]

Let (d_q(x)\in\{0,1\}), (q=1,\ldots,Q), denote prespecified downstream decisions. The prosecuted family contains:

- threshold decisions (1\{r_i(x)\ge\tau\});
- deterministic pairwise orderings (1\{r_i(x)>r_j(x)\}), with a fixed tie rule; and
- top-*k* membership (1\{\operatorname{rank}_i(x)\le k\}).

A decision is certified by release (S) when it is invariant over the compatible fiber:

\[
c_q(S)=1\left\{\min_{x\in\mathcal F(S)}d_q(x)=
\max_{x\in\mathcal F(S)}d_q(x)\right\}.
\]

For nonnegative importance weights (w_q), decision-certification utility is

\[
U_D(S)=\sum_{q=1}^{Q}w_qc_q(S).
\]

An agency-side optimization would be

\[
\max_{S\subseteq\mathcal A}U_D(S)
\quad\text{subject to}\quad
S\in\mathcal R_{\mathrm{safe}},\ C(S)\le B,
\]

where (\mathcal R_{\mathrm{safe}}) is an accepted disclosure-protection rule and (C(S)) is a release cost or budget.

This formulation makes the collision visible: the privacy/safety constraint, action space, and release optimizer are inherited; C012 supplies a particular utility function.

## Literature prosecution

### Classical optimal tabular release

Cell suppression and controlled tabular adjustment already formulate disclosure control as constrained optimization: protect sensitive cells or satisfy protection intervals while minimizing a loss/cost of suppressing or changing published cells. The foundational and closest works include:

- Cox, “Suppression Methodology and Statistical Disclosure Control” (1980), which develops systematic tabular suppression;
- Cox, “Network Models for Complementary Cell Suppression” (1995), which treats protection through network optimization;
- Fischetti and Salazar-González, “Models and Algorithms for Optimizing Cell Suppression in Tabular Data with Linear Constraints” (2000), [DOI](https://doi.org/10.1080/01621459.2000.10474282);
- Fischetti and Salazar-González, “Solving the Cell Suppression Problem on Tabular Data with Linear Constraints” (2001), [DOI](https://doi.org/10.1287/mnsc.47.7.1008.9805);
- Salazar-González, *Mathematical Models for Cell-Suppression* (2002), [full text](https://research.cbs.nl/casc/deliv/41-d1.pdf); and
- the Census overview of [optimization in suppression and controlled tabular adjustment](https://www.census.gov/library/working-papers/2004/adrm/rrs2004-04.html).

This literature already owns: feasible/congruent tables, attacker bounds, complementary protection, permitted release decisions, weighted information-loss objectives, and mathematical programming over tabular releases. Classical objectives are often additive for computational reasons, but the framework is not a scientific claim that utility must be additive. Replacing the loss with a nonlinear oracle changes computational difficulty, not the intellectual category of the problem.

### Risk–utility and purpose-specific data utility

Statistical disclosure control explicitly treats publication as a trade-off between disclosure risk and data utility. Official guidance defines utility in terms of whether anonymized data remain useful and valid for end-user analyses; see the [SDC Practice Guide](https://sdcpractice.readthedocs.io/en/latest/utility.html). The privacy-preserving data-publishing literature has long distinguished general-purpose distortion metrics from task-specific utility.

Fung et al.'s survey, “Privacy-Preserving Data Publishing: A Survey of Recent Developments,” [full text](https://www.cs.sfu.ca/~wangk/pub/FWCY10csur.pdf), is especially damaging to novelty. It states that when the downstream task is known, a publisher can customize the release to preserve patterns for that task; it also explains that minimizing generic distortion can be the wrong objective and discusses classification error as the relevant utility for a classification goal. Decision certification is another known-task utility of the same form.

Thus “optimize the release for the decisions users actually make” is not a new research principle.

### Workload-aware query release

Differentially private query-release research treats the analyst's target queries as a workload and designs the release mechanism to minimize error on that workload:

- Li, Hay, Rastogi, Miklau and McGregor, “Optimizing Linear Counting Queries under Differential Privacy,” [ACM](https://dl.acm.org/doi/10.1145/1807085.1807104), introduces the matrix-mechanism perspective of selecting a query strategy for a specified workload;
- Li, Hay, Miklau and Wang, “A Data- and Workload-Aware Algorithm for Range Queries under Differential Privacy,” [DOI](https://doi.org/10.14778/2732269.2732271), adapts measurements to both the data and query workload;
- Yuan et al., “Low Rank Mechanism: Optimizing Batch Queries under Differential Privacy,” [arXiv](https://arxiv.org/abs/1208.0094), optimizes correlated query workloads;
- Blasiok et al., “Towards Instance-Optimal Private Query Release,” [arXiv](https://arxiv.org/abs/1811.03763), studies mechanisms optimal for a given workload; and
- Ge et al., “APEx: Accuracy-Aware Differentially Private Data Exploration,” [arXiv](https://arxiv.org/abs/1712.10266), lets users specify query accuracy requirements and selects mechanisms accordingly.

C012's ranking, top-*k*, and threshold predicates are nonlinear downstream workloads rather than linear counts. That distinction affects computation, but workload-specific mechanism design is already established.

### Task-aware privacy and downstream decisions

The broader privacy literature goes beyond query error and explicitly optimizes ultimate task performance:

- Cheng, Tang and Chinchali, “Task-aware Privacy Preservation for Multi-dimensional Data” (ICML 2022), [PMLR full text](https://proceedings.mlr.press/v162/cheng22a.html), learns privacy-preserving representations optimized for a specified downstream task and derives a near-optimal linear solution;
- Majeed and Hwang, “Task-Specific Adaptive Differential Privacy Method for Structured Data” (2023), [DOI](https://doi.org/10.3390/s23041980), allocates perturbation according to task relevance; and
- Pujol et al., “Post-processing of Differentially Private Data: A Fairness Perspective” (2022), [full text](https://www.ijcai.org/proceedings/2022/0559.pdf), analyzes private releases used for consequential downstream allocation decisions and designs post-processing against downstream criteria.

These mechanisms, privacy definitions, and data models differ from cell suppression. But they decisively occupy the conceptual move of designing privacy protection around a known downstream objective. C012 would need new theory or an algorithm specific to exact decision certification; naming a new task does not clear that bar.

### Ranking/top-*k* does not rescue novelty

Possible/necessary outcomes under incomplete information and uncertain rankings are established in computational social choice and uncertain databases. The earlier C012 prosecution already found possible/necessary winner and partial-ranking work. Encoding those predicates as the utility of a release design combines established ingredients; it does not create a new statistical object.

## Structural results

The following results are correct and useful but do not overturn the collision finding.

### 1. Monotonicity: established

If (S\subseteq T), then (\mathcal F(T)\subseteq\mathcal F(S)). Once a binary decision is constant on (\mathcal F(S)), it remains constant on every nonempty subset (\mathcal F(T)). Therefore

\[
U_D(S)\le U_D(T).
\]

This holds for all nonnegative weights. The proof is immediate from fiber nesting. The exhaustive program checked 177,147 inclusion pairs across the three reported witness instances; none violated monotonicity.

### 2. Submodularity: refuted

Submodularity would require diminishing returns:

\[
U_D(A\cup\{e\})-U_D(A)\ge
U_D(B\cup\{e\})-U_D(B),\qquad A\subseteq B.
\]

The exhaustive search found a disclosure-safe counterexample for the synthetic confidential vector ((0,0,0,1)). Candidate releases are exact pair/triple sums, and every reported fiber retains at least two feasible values for each cell.

Let (A=\varnothing), (B=\{x_1+x_4\}), and (e=x_2+x_3+x_4). Adding (e) to (A) certifies four decisions; adding it after (B) certifies five additional decisions. Hence (4<5), violating submodularity.

### 3. Release synergy: established

In that same witness:

| Release actions | Feasible tables | Cell widths | Certified decisions |
|---|---:|---|---:|
| none | 256 | (3,3,3,3) | 0 |
| (x_1+x_4) | 32 | (1,3,3,1) | 2 |
| (x_2+x_3+x_4) | 12 | (3,1,1,1) | 4 |
| both | 3 | (1,1,1,1) | 7 |

The joint gain exceeds the sum implied by diminishing returns, while no cell is point identified. This is genuine complementarity between releases.

### 4. Supermodularity: refuted

The utility is not uniformly complementary either. A second safe witness has an added action with gain 3 at the empty set but gain 2 after another release. Redundant constraints therefore create diminishing returns. Decision-certification utility is generally neither submodular nor supermodular.

### 5. Decision identification without cell identification: established

Every safe witness retained a nonzero projection width for all four confidential cells, yet several threshold, ordering, or top-2 predicates were invariant. Decision certification is therefore not equivalent to reconstructing cells and need not imply point identification.

This is an important interpretive fact, but it follows directly from a many-to-one decision functional: a function may be constant on a set even when every coordinate varies.

## Exhaustive implementation and experiments

New code is preserved in [`C012_prototype/decision_release_design.py`](C012_prototype/decision_release_design.py). Machine-readable results are in [`C012_prototype/outputs/decision_release_results.json`](C012_prototype/outputs/decision_release_results.json).

For each witness instance, the program exhaustively enumerates:

- all (4^4=256) confidential four-cell tables with counts in ({0,1,2,3});
- ten candidate actions consisting of every pair sum and triple sum;
- all (2^{10}=1,024) release-action subsets;
- four threshold predicates, six deterministic pairwise-order predicates, and four top-2 predicates; and
- disclosure safety under the test rule that every cell retain at least two feasible values.

It computes fiber size, cell projection widths, number and identities of certified decisions, total cell-width reduction, and log fiber-size reduction. It searches rather than hand-selects the counterexamples.

### Decision utility versus conventional cell-width utility

For confidential vector ((0,1,3,1)) and a budget of two release actions:

| Objective | Selected safe actions | Certified decisions | Cell-width reduction | Feasible tables |
|---|---|---:|---:|---:|
| Decision certification | (x_1+x_4), (x_2+x_3+x_4) | 10 | 6 | 5 |
| Cell-width reduction, optimum 1 | (x_2+x_3), (x_1+x_2+x_4) | 8 | 8 | 3 |
| Cell-width reduction, optimum 2 | (x_3+x_4), (x_1+x_2+x_4) | 7 | 8 | 3 |

The optimal sets are disjoint. A release that narrows cells most is not necessarily the release that certifies the most decisions. This establishes consequential objective mismatch.

It does **not** establish a new framework. Risk–utility optimization is expected to choose different releases when its utility changes.

## Why the structural results do not save C012

The findings might have supported a methods paper if they yielded an exploitable special structure, a new approximation guarantee, a new privacy guarantee, or a statistically principled inferential theory. Instead:

1. monotonicity is a one-line consequence of nested feasible sets;
2. non-submodularity removes the standard greedy guarantee rather than supplying a new algorithm;
3. non-supermodularity shows that neither pure complementarity nor pure diminishing returns organizes the problem;
4. synergy is expected when multiple linear equations jointly cross a nonlinear decision boundary;
5. objective disagreement is expected when one changes the utility being optimized; and
6. the prototype solves release selection by exhaustive enumeration, with no scalable method.

The resulting optimization is a black-box, nonadditive utility maximization over established disclosure-safe release actions. Existing optimal-release frameworks can host it directly, and modern task-aware privacy already justifies choosing task performance rather than generic distortion.

## Statistical contribution assessment

### What is real

- Release-only decision certification is more honest than silently converting unidentified outcomes into point decisions.
- Cellwise information loss can be poorly aligned with ranking or threshold utility.
- Aggregate releases can certify decisions without reconstructing cells.
- Agencies could use such scores operationally when a narrow, declared workload is important.

### What is missing

- a new estimand or identification principle beyond constancy over a feasible set;
- a new disclosure-risk guarantee;
- a new release mechanism;
- a nontrivial characterization of when certification occurs;
- a scalable exact or approximate algorithm with guarantees;
- sampling uncertainty or inferential theory;
- a legitimate agency-reviewed empirical application; and
- evidence that the method solves a recognized gap rather than instantiating task-aware utility.

The lack of these elements is not merely unfinished engineering. It means the claimed contribution collapses under the controlling novelty test.

## Reproducibility and scope

The scripts operate only on synthetic data. They do not query CDC WONDER, reconstruct protected counts, or modify any canonical v0.26.0 record. Run:

```bash
python C012_prototype/c012_bounds.py
python C012_prototype/decision_release_design.py
```

The original prototype continues to verify sharp rate, pairwise, rank, top-*k*, and threshold calculations. The new script performs release-design enumeration and writes its JSON results deterministically.

## Final decision

**KILL**

C012 has now exhausted its permitted narrowing round. Decision-preserving disclosure control is best understood as a potentially useful application-specific utility within classical risk–utility release optimization and modern task/workload-aware privacy. The experiments show that the utility differs from conventional cellwise utility, but changing the utility is exactly what the existing framework permits. No independently publishable statistical theory or algorithm survived prosecution.

C012 should not receive an execution protocol and should not be reframed again. Any future work on suppressed tables must arise from a materially different contribution discovered independently, not from another refinement of this candidate.
