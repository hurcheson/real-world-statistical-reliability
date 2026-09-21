# Manuscript Outline: Precision Screening and Geographic Coverage in HUD Qualified Census Tract Designation

**Target Outlets:**  
* Primary: *Journal of Policy Analysis and Management* (JPAM) — Research Article  
* Secondary: *National Tax Journal* (NTJ) or *Journal of Housing Economics* (JHE)  
* Methodological Track: *Journal of the American Statistical Association* (JASA: Applications & Case Studies)  

**Working Title:** Precision Screening and Geographic Coverage in HUD Qualified Census Tract Designation: A Reproducible Policy Sensitivity Analysis  
**Evidence Scope:** 2016 Admitted National Execution ($N = 85,390$ tract records; 0 mismatches)  

---

## Section-by-Section Structural Blueprint

### 1. Introduction
* **1.1 The Growth of Survey-Based Resource Allocation**
  * Historical shift from decennial Census counts to continuous American Community Survey (ACS) 5-year rolling samples in federal distribution formulas.
  * The fundamental trade-off in small-area administrative targeting: point estimates vs. sampling variance.
* **1.2 Administrative Noise Filters in Federal Policy**
  * Why federal agencies introduce relative margin of error (RMoE) screening rules.
  * The 2016 HUD policy shift: tightening the precision filter from $c = 1.00$ to $c = 0.50$ for Qualified Census Tracts (QCTs) under Section 42 of the Internal Revenue Code (LIHTC).
* **1.3 Core Questions & Research Contributions**
  * Does precision screening remove noise, or does it systematically redistribute capital?
  * Three empirical discoveries from the 2016 national replay:
    1. *Gross Churn vs. Net Change:* Net change is $-438$ ($-3.12\%$), but gross churn is $864$ tracts ($1.97\times$ the net reduction).
    2. *Small-Population Penalty ($BRD$):* A $12.24$ percentage-point standardized risk premium against low-population tracts.
    3. *Strict Non-Local Spillovers:* $161$ tracts change status through the 20% statutory population cap without any change in their own survey data.
* **1.4 Structure of the Article**

### 2. Institutional & Statutory Setting: The LIHTC QCT Mechanism
* **2.1 Section 42 and the 30% Basis Boost**
  * The economic significance of QCT status: boosting tax credit allocations and private equity syndication values for low-income housing.
* **2.2 Statutory Designation Criteria**
  * The Poverty Criterion: Poverty rate $\ge 25\%$.
  * The Income Criterion: Median Family Income (MFI) $\le 60\%$ of Area Median Family Income (AMFI).
* **2.3 The "Two-of-Three" Multi-Release Rule**
  * ACS 5-year releases used: 2009–2013, 2008–2012, 2007–2011.
  * A tract must satisfy substantive criteria in $\ge 2$ of 3 releases. How the precision screen invalidates individual releases and breaks the qualifying chain.
* **2.4 The Statutory 20% Area Population Cap**
  * The statutory ceiling on aggregate designated tract population within Core Based Statistical Areas (CBSAs) and non-metro counties.
  * Dual-criterion priority ranking and intra-tier sorting algorithms.
  * The "greedy skip-and-continue" allocation heuristic used by HUD.

### 3. Theoretical Framework: Precision Screening in Capped Allocation Systems
* **3.1 Sampling Variance as a Function of Tract Population**
  * Analytical derivation: $\text{Var}(\hat{\theta}) \propto \frac{1}{n_i}$.
  * Proof of the structural inverse relationship between tract base population and margin-of-error ratio ($RMoE$).
* **3.2 The Mechanism of Policy-Induced Churn**
  * Mathematical definition of the 5-part decomposition ($L_1, L_2, L_3, G_1, G_2$):
    * Direct exclusion ($L_1$)
    * Secondary cap crowd-out ($L_2$)
    * Rank degradation exclusion ($L_3$)
    * Tie-breaker substitution gain ($G_1$)
    * Cap vacancy spillover gain ($G_2$)
* **3.3 Non-Local Allocation Externalities**
  * Definition of strict non-local spillovers: $\Delta Q_i \neq 0$ while $\Delta \text{Screen}_i = 0$.
  * How cap capacity released by disqualified tract $A$ cascades down the ranking ladder to designate tract $B$.

### 4. Data, Algorithmic Reconstruction, and Verification
* **4.1 Empirical Data Substrate**
  * Official 2016 HUD master workbook (`qct_data_2016.xlsx`, $27.47\text{ MB}$, SHA-256 registered).
  * Unit of analysis: $85,390$ tract and sub-area records nationwide.
* **4.2 Zero-Mismatch Reconstruction Standard**
  * Execution of the prospective Tier A acceptance standard.
  * 0 mismatches against published 2016 HUD determinations across all 85,390 records.
  * Invariance across income-arithmetic variants (`ratio_full`, `ratio_round7`, `stored_then_raw`).
* **4.3 Counterfactual Identification Strategy**
  * Pure same-data replay: all survey estimates, margins of error, thresholds, and population caps held constant.
  * Shift parameter: $c \in \{0.50, 1.00\}$.

### 5. Empirical Results: The 2016 National Replay
* **5.1 Aggregate Designation Impacts: Net Stability Masking Gross Churn**
  * Total eligible tracts: $17,042$ ($c=1.00$) vs. $16,368$ ($c=0.50$).
  * Total designated tracts: $14,057$ ($c=1.00$) vs. $13,619$ ($c=0.50$).
  * Net change: $-438$; Gross churn: $864$.
* **5.2 The 5-Part Churn Partition**
  * Presentation of Table 2: $L_1 = 473$, $L_2 = 159$, $L_3 = 19$, $G_1 = 71$, $G_2 = 142$.
  * Analysis of paradoxical gains ($G_2 = 142$) awarded to lower-distress tracts purely because higher-distress small tracts were disqualified.
* **5.3 The Small-Population Disadvantage ($BRD$)**
  * Empirical loss rates by population quintile: $Q_1 (10.62\%)$ to $Q_5 (1.03\%)$.
  * Standardized Bounded Relative Disadvantage: $BRD = 0.1224$ ($12.24$ percentage points).
  * Conditioning on distance-to-threshold to confirm that the penalty is an artifact of sample size, not economic distress.
* **5.4 Spatial Externalities and Cap Dynamics**
  * Analysis of the $161$ strict non-local spillover tracts across 75 metropolitan areas and 31 states.
  * Metropolitan cap transitions: $175$ binding areas under $c=1.00$ vs. $162$ under $c=0.50$ (13 areas transition from binding to non-binding).

### 6. Policy Discussion & Reform Alternatives
* **6.1 The Illusion of Administrative Neutrality**
  * Administrative precision filters are not value-neutral statistical hygiene; they redistribute federal subsidies across geography and tract sizes.
* **6.2 Evaluation of Alternative Statistical Approaches**
  * Bayesian hierarchical models / Empirical Bayes shrinkage to borrow strength across adjacent tracts without discarding high-poverty small areas.
  * Moving from hard cutoffs ($c=0.50$) to continuous variance weighting in ranking.
  * Decoupling the precision screen from the 20% area population cap to prevent non-local spillovers.
* **6.3 Implications for Other Federal Formula Grants**
  * Broader relevance for Title I school funding, New Markets Tax Credits (NMTC), and Community Development Block Grants (CDBG).

### 7. Conclusion
* Summary of findings.
* The imperative for reproducible computational policy audits prior to implementing administrative statistical rules.
* Data availability and replication archive statement.
