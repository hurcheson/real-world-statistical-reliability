# C011 Claim–Evidence–Limitation Matrix: 2016 Bounded Evidence Set

**Project:** HUD Qualified Census Tract (QCT) Precision-Screen Policy Sensitivity Analysis  
**Evidence Standard:** 2016 Admitted Execution (Zero-mismatch official replay; deterministic counterfactual identity)  
**Date:** September 2026  
**Status:** Cryptographically & Computationally Frozen  

---

## Matrix Summary Table

| # | Core Empirical Claim | Direct Mathematical Estimand | Empirical Evidence (2016 National Replay) | Supporting Artifacts / File Source | Methodological & Policy Limitations |
|---|---|---|---|---|---|
| **C1** | **Exact Official Reconstruction** | $\sum_{i=1}^N \mathbf{1}\{Q_i^{\text{recon}}(0.50) \neq Q_i^{\text{official}}\} = 0$ | $13,619$ designated tracts reconstructed with **0 mismatches** out of $85,390$ records nationwide ($100.000\%$ accuracy). | `c011_final_reconstruction_validation.csv`<br>`reconstruction_mismatches.csv`<br>`test_2016_regression.py` | Validated for the 2016 statutory cycle. 2020/2021/2022/2026 retain unresolved administrative provenance anomalies and are formally excluded from this manuscript. |
| **C2** | **Concealed Designation Churn** | $\text{Churn} = \sum_{i} \|Q_i(1.00) - Q_i(0.50)\| = \sum_{k=1}^3 L_k + \sum_{m=1}^2 G_m$ | Net change: $-438$ ($-3.12\%$).<br>Gross churn: **$864$ tracts** ($1.97\times$ the net reduction).<br>Losses: $651$; Gains: $213$.<br>Decomposition: $473 / 159 / 19 / 71 / 142$. | `c011_final_decomposition.csv`<br>`c011_final_master_results.csv`<br>`annual_result.csv` | Churn captures status transitions under identical survey data. It measures administrative policy sensitivity, not underlying demographic migration or economic gentrification. |
| **C3** | **Small-Population Disproportionate Penalty** | $BRD = \mathbb{E}[L_i \mid \text{PopQuint}=1] - \mathbb{E}[L_i \mid \text{PopQuint}=5] \mid \text{Distance to Threshold}$ | Tracts in the lowest population quintile ($Q_1$) suffer a **$12.24$ percentage-point higher risk of disqualification** ($BRD = 0.1224$).<br>Raw loss rate: $Q_1 = 10.62\%$ vs. $Q_5 = 1.03\%$ ($10.3\times$ gradient). | `c011_final_population_burden.csv`<br>`brd_strata.csv`<br>`annual_result.csv` | Driven by the mathematical properties of ACS sampling variance ($\sigma \propto 1/\sqrt{n}$). Small tract populations structurally widen confidence intervals, conflating small sample size with measurement unreliability. |
| **C4** | **Strict Non-Local Spatial Externalities** | $S_{\text{nonlocal}} = \{i : Q_i(1.00) \neq Q_i(0.50) \land \Delta \text{Screen}_i = 0\}$ | **$161$ tracts** changed federal designation despite experiencing **zero change** in their own survey estimates or precision flags.<br>Spans $75$ allocation areas across $31$ states ($18.63\%$ of all churn). | `c011_final_decomposition.csv`<br>`analysis_records.csv` ($L_2 + G_2 = 19 + 142$) | Spillover occurs strictly through the statutory 20% aggregate area population cap ceiling. Unaffected tracts in non-binding areas experience zero spillovers. |
| **C5** | **Diminishing Precision Purchased** | $\Delta \text{MoE}_{\text{disqualified}} \text{ vs. } \Delta \text{Coverage}$ | Of $674$ tracts losing eligibility, $473$ ($70.18\%$) are eliminated by marginal precision failures rather than failing the substantive $25\%$ poverty or $60\%$ MFI thresholds. | `c011_final_precision_purchased.csv`<br>`c011_final_cap_transitions.csv` | Analysis evaluates administrative precision thresholds ($c=0.50$ vs $c=1.00$); does not evaluate Bayesian shrinkage, empirical Bayes, or tract-aggregation alternative estimators. |

---

## Detailed Claim Specifications

### Claim 1: Exact Official Replication
* **Mathematical Statement:** The algorithmic implementation $f(X_i, c=0.50)$ reproduces HUD's published vector $Q_i^{\text{official}}$ with identity across all $N=85,390$ records:
  $$\forall i \in \{1, \dots, N\}, \quad Q_i(c=0.50) = Q_i^{\text{official}}$$
* **Empirical Evidence:** In `outputs/determinism/run1/2016/reconstruction_mismatches.csv`, the file contains 0 data rows (header only). The test `test_2016_exact_and_counterfactual_identity` asserts `(official != tight.designated).sum() == 0` and passes unconditionally.
* **Sensitivity to Arithmetic Variants:** Three competing implementations of intermediate income ratio arithmetic (`ratio_full`, `ratio_round7`, and `stored_then_raw`) were tested. All three yield **exactly 13,619 designations**, **zero mismatches**, and identical set digests (`42d42efa5148...`). The counterfactual is thus uniquely identified.
* **Limitations:** Replication holds strictly for the 2016 workbook and statutory rules. It does not imply that HUD's legacy internal code was elegant or documented, but that its deterministic mapping is completely recovered.

### Claim 2: Concealed Allocation Churn
* **Mathematical Statement:** Net change $|\Delta Q| = |Q(0.50) - Q(1.00)|$ severely understates total designation turnover:
  $$\text{Net Change} = 13,619 - 14,057 = -438 \quad (-3.12\%)$$
  $$\text{Gross Churn} = |L| + |G| = 651 + 213 = 864 \quad (6.15\% \text{ of baseline})$$
* **Decomposition:**
  * $L_1 = 473$: Direct losses (tract lost eligibility due to precision screen disqualification).
  * $L_2 = 159$: Non-local losses (tract was eligible under both $c=1.00$ and $c=0.50$, but was crowded out by higher-ranked tracts re-entering under cap).
  * $L_3 = 19$: Direct & Non-local compound losses (tract lost eligibility on one criterion, fell in rank tier, and lost designation).
  * $G_1 = 71$: Direct gains (tract qualified under a secondary criterion that became viable under altered ranking).
  * $G_2 = 142$: Non-local gains (tract gained designation purely because cap space was vacated by $L_1$ tracts).
* **Limitations:** The study evaluates designation eligibility, not actual private developer take-up of 9% or 4% LIHTC credits in these tracts.

### Claim 3: Small-Population Penalty ($BRD$)
* **Mathematical Statement:** The Bounded Relative Disadvantage ($BRD$) measures the difference in designation loss probability between the smallest and largest tract population quintiles, standardized by economic proximity to the statutory poverty ($25\%$) and income ($60\%$) thresholds:
  $$BRD = 0.122396 \quad (12.24 \text{ percentage points})$$
* **Empirical Gradient:**
  * Quintile 1 (Mean Pop $\approx 1,850$): Loss rate = $10.62\%$
  * Quintile 2: Loss rate = $3.90\%$
  * Quintile 3: Loss rate = $2.79\%$
  * Quintile 4: Loss rate = $1.44\%$
  * Quintile 5 (Mean Pop $\approx 6,400$): Loss rate = $1.03\%$
* **Mechanism:** Sampling variance in the ACS 5-year estimate scales as $\text{Var}(\hat{p}) \approx \frac{p(1-p)}{n}$. Tracts with small base populations have smaller completed sample sizes ($n$), which mechanically blows up the margin of error ($MoE = 1.645 \cdot \text{SE}$). A fixed administrative cutoff ($c = 0.50$) therefore functions as an implicit population filter.
* **Limitations:** Tract population variation reflects Census Bureau boundary design rules (typically targeting 4,000 residents, but ranging from 1,200 to 8,000+ due to geographic features and local boundaries).

### Claim 4: Strict Non-Local Spatial Externalities
* **Mathematical Statement:** An allocation externality occurs when tract $j$'s designation changes ($Q_j(1.00) \neq Q_j(0.50)$) while its own survey parameters are invariant ($\Delta \text{Screen}_j = 0$):
  $$S_{\text{nonlocal}} = L_3 + G_2 = 19 + 142 = 161 \text{ tracts}$$
* **Geography:** The 161 spillover tracts are distributed across 75 distinct CBSAs and non-metro county allocation areas in 31 states.
* **Mechanism:** In areas where the statutory 20% population cap is binding, designating or disqualifying tract $A$ releases or consumes cap capacity, immediately altering the designation status of tract $B$ miles away, despite tract $B$'s demographic reality being entirely unchanged.
* **Policy Implication:** Developers and housing authorities in cap-constrained metros face regulatory uncertainty generated by survey noise in adjacent or distant neighborhoods within the same CBSA.

---

## Provenance and Verification Hash Signatures

| File / Component | Path | Exact SHA-256 Checksum |
|---|---|---|
| Raw 2016 Workbook | `projects/c011-qct-precision-screen/data/raw/qct_data_2016.xlsx` | `75ae56ca258aabde75081739c401aa619886f0463a525d7cf786effbe9ba991f` |
| Frozen Protocol | `projects/c011-qct-precision-screen/protocol/C011_EXECUTION_PROTOCOL.md` | `f1e7e8e331e4016cbf6eb7243450364cfc97da2066ebf7215f42251ae7184ae1` |
| Master Results CSV | `projects/c011-qct-precision-screen/outputs/final/c011_final_master_results.csv` | Deterministic rerun verified; 100% semantic identity |
| Decomposition CSV | `projects/c011-qct-precision-screen/outputs/final/c011_final_decomposition.csv` | Deterministic rerun verified; 100% semantic identity |
| Population Burden CSV | `projects/c011-qct-precision-screen/outputs/final/c011_final_population_burden.csv` | Deterministic rerun verified; 100% semantic identity |
