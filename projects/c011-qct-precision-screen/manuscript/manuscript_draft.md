# Precision Screening and Geographic Coverage in HUD Qualified Census Tract Designation: A Reproducible Policy Sensitivity Analysis

**Working Paper — September 2026**  
**Computational Archive:** [hurcheson/real-world-statistical-reliability](https://github.com/hurcheson/real-world-statistical-reliability) (C011)  
**Execution Standard:** Zero-mismatch 2016 Admitted Execution  

---

## Abstract

Federal resource-allocation formulas increasingly distribute public capital based on small-area survey estimates characterized by substantial sampling error. To prevent designation errors driven by survey noise, administering agencies frequently institute statistical precision screens that disqualify estimates with large margins of error. In 2016, the U.S. Department of Housing and Urban Development (HUD) tightened the precision gate for Qualified Census Tract (QCT) designations under the Low-Income Housing Tax Credit (LIHTC)—the nation's primary private-capital subsidy for affordable housing—lowering the permissible margin-of-error ratio from $c = 1.00$ to $c = 0.50$. In this study, we conduct a deterministic, zero-mismatch computational reconstruction of the 2016 nationwide HUD QCT allocation algorithm across all 85,390 U.S. census tract records and execute a controlled, same-data counterfactual policy sensitivity analysis. Holding all observed survey data, statutory poverty/income cutoffs, and geography constant, tightening the screen from $c = 1.00$ to $c = 0.50$ reduced net designations by 438 tracts ($-3.12\%$), but induced gross status churn across 864 tracts ($1.97\times$ the net reduction). We demonstrate that this precision filter operates selectively: because survey sampling variance scales inversely with tract population, tracts in the lowest population quintile face a 12.24 percentage-point higher standardized risk of losing eligibility ($BRD = 0.1224$) after conditioning on proximity to statutory thresholds ($10.62\%$ raw loss rate in Quintile 1 vs. $1.02\%$ in Quintile 5). Furthermore, through interaction with the statutory 20% area population cap, the screen generates strict non-local allocation externalities: 161 tracts in 75 metropolitan areas across 31 states experienced designation status changes despite experiencing zero change in their own survey estimates, margins of error, or precision indicators. These findings demonstrate that in threshold-and-cap allocation formulas, administrative precision screens trade statistical reliability for systematic demographic coverage shifts and non-local spatial externalities.

**Keywords:** Qualified Census Tracts, American Community Survey, Margins of Error, Algorithmic Allocation, Low-Income Housing Tax Credit, Policy Sensitivity Analysis, Administrative Data Quality.

---

## 1. Introduction

Over the past two decades, federal statutory and administrative programs have transitioned from decennial census counts to rolling sample estimates produced by the American Community Survey (ACS). While the ACS provides continuous, updated indicators of poverty, income, and demographic structure, tract-level 5-year estimates are characterized by substantial sampling variability, particularly in sparsely populated or socioeconomically disadvantaged communities (Spielman et al., 2014; Folch et al., 2016).

Policymakers and administering agencies face an inherent methodological dilemma when deploying survey data to distribute targeted public resources. Using point estimates without regard to precision risks awarding capital to statistical artifacts—directing subsidies to tracts that appear eligible solely due to positive sampling shocks. Conversely, disqualifying estimates based on statistical noise risks denying statutory entitlements to communities whose true deprivation is obscured by small sample sizes (Bazuin & Fraser, 2016).

In 2016, the U.S. Department of Housing and Urban Development (HUD) addressed this dilemma within the Low-Income Housing Tax Credit (LIHTC) program. Authorized under Section 42 of the Internal Revenue Code (IRC), the LIHTC program provides a 30% "basis boost" in federal tax credit subsidies to developments located within **Qualified Census Tracts (QCTs)**. To ensure that QCT designations reflect durable economic distress rather than transient survey error, HUD established a formal statistical precision screen requiring that a tract's relative margin of error (the ratio of the 90% margin of error to the point estimate) not exceed a predetermined threshold $c$:
$$c = \frac{\text{Margin of Error}}{\text{Point Estimate}} \le 0.50$$
Prior to this administrative tightening, the effective operative threshold was $c = 1.00$.

While intended as a neutral data-quality safeguard, administrative precision screens do not operate in a vacuum. In QCT designation, the precision screen interacts with two statutory mechanisms:
1. **The Multi-Release Qualifying Rule ("Two-of-Three"):** A tract qualifies if it satisfies substantive poverty or income criteria in at least two of the three most recent ACS 5-year releases. Disqualifying a single release's estimate due to low precision can eliminate an otherwise eligible tract.
2. **The 20% Area Population Cap:** By statute, designated QCTs within any metropolitan area or non-metropolitan county cannot exceed 20% of the aggregate population. Eligible tracts are ranked by substantive economic distress; when the cap binds, marginal tracts are excluded.

This paper provides the first nationwide, deterministic policy sensitivity analysis of HUD's precision screen. Using official 2016 HUD administrative files and published ACS inputs, we reconstruct the complete national allocation with **zero record-level mismatches** against HUD’s published designations across all 85,390 U.S. tract records. We then conduct an exact same-data counterfactual evaluation, holding all underlying survey inputs constant while varying only the precision threshold $c \in \{0.50, 1.00\}$.

We document three primary empirical findings:
* **Concealed Allocation Churn:** While the net reduction in designated QCTs is modest ($-438$ tracts, or $-3.12\%$), the gross status churn is nearly double (**864 tracts** change designation status).
* **Population-Selective Exclusion:** The precision screen imposes a regressive burden on smaller communities. Tracts in the lowest population quintile experience a 12.24 percentage-point higher risk of losing statutory eligibility ($BRD = 0.1224$) after conditioning on proximity to substantive cutoffs ($10.62\%$ loss rate in Quintile 1 vs. $1.02\%$ in Quintile 5).
* **Strict Non-Local Spillovers:** Through interaction with the 20% area population cap, **161 tracts** across 75 metropolitan areas and 31 states experience final designation changes despite experiencing zero change in their own survey estimates, margins of error, or precision indicators.

---

## 2. Institutional & Statutory Setting

### 2.1 The LIHTC Program and Qualified Census Tracts
Section 42 of the Internal Revenue Code establishes the Low-Income Housing Tax Credit to stimulate private investment in affordable rental housing. To encourage development in severely distressed neighborhoods, Section 42(d)(5)(B)(ii) provides an enhanced subsidy—a 30% increase in the eligible basis—for projects located in Qualified Census Tracts.

By statute, a census tract is designated a QCT if:
1. **The Poverty Criterion:** At least 25% of the tract’s population resides below the federal poverty line; or
2. **The Income Criterion:** The tract's median family income (MFI) does not exceed 60% of the area median family income (AMFI) for the metropolitan area or non-metropolitan county.

### 2.2 The 20% Area Population Cap and Ranking Logic
To prevent over-concentration of subsidized housing and manage fiscal liability, Congress enacted a strict statutory ceiling: the aggregate population of designated QCTs in any metropolitan area (CBSA) or non-metropolitan county cannot exceed **20% of the aggregate population** of that area.

When the aggregate population of eligible tracts exceeds the 20% cap, HUD enforces a statutory ranking mechanism:
* Tracts eligible under both poverty and income criteria are prioritized over single-criterion tracts.
* Within priority tiers, tracts are ranked in descending order of poverty rate (for poverty-eligible tracts) or ascending order of MFI ratio (for income-eligible tracts).
* Tracts are designated cumulatively down the ranked list using a greedy skip-and-continue rule: if the next tract exceeds the remaining cap capacity, the algorithm evaluates subsequent eligible tracts until no remaining tract can fit within the cap.

### 2.3 Transition to the ACS and the "Two-of-Three" Logic
Prior to 2012, designations were based on decennial census "long form" sample data. Following the discontinuation of the long form, HUD transitioned to 5-year ACS estimates. Because 5-year estimates represent rolling multi-year averages with small tract-level sample sizes, HUD instituted a rule requiring that a tract satisfy substantive eligibility criteria in **at least two of the three most recent ACS 5-year releases**.

For the 2016 designations, the qualifying releases were:
* ACS 2009–2013 (Primary vintage)
* ACS 2008–2012 (Secondary vintage)
* ACS 2007–2011 (Tertiary vintage)

---

## 3. The Statistical Precision-Screen Mechanism

### 3.1 Relative Margin of Error (RMoE) Screen
To prevent tracts from qualifying based on noisy point estimates, HUD introduced a relative margin-of-error filter. For estimate $\hat{\theta}_{irt}$ (representing the poverty rate or median family income for tract $i$, release $r$, and criterion $t$) with published 90% margin of error $MoE_{irt}$, the precision ratio is defined as:
$$RMoE_{irt} = \frac{MoE_{irt}}{\hat{\theta}_{irt}}$$

Under the administrative rule enforced beginning in 2016, an estimate is disqualified if:
$$RMoE_{irt} > c, \quad \text{where } c = 0.50$$
Prior to this policy, the effective operational standard permitted estimates up to $c = 1.00$.

When an estimate fails the screen ($RMoE_{irt} > c$), that specific release-criterion observation is marked invalid and cannot contribute toward satisfying the "two-of-three" requirement. If a tract has only two qualifying releases and one is disqualified by the precision screen, the tract loses eligibility for that criterion entirely.

### 3.2 Non-Linear Allocation Interactions
The precision filter produces two distinct non-linear dynamics:
1. **The Sampling Error Gradient:** Survey sampling variance is inversely proportional to effective sample size:
   $$\text{Var}(\hat{\theta}) \propto \frac{1}{n_i}$$
   Because census tracts vary in population (typically between 1,200 and 8,000 residents), smaller tracts have systematically smaller ACS sample sizes, generating structurally larger margins of error. Consequently, a uniform precision threshold $c$ imposes a higher probability of disqualification on low-population tracts, independent of their true socioeconomic status.
2. **Cap Re-Allocation (Externalities):** In metropolitan areas where the 20% population cap binds, the disqualification of a highly ranked tract by the precision screen reduces the cumulative population allocated. This newly available cap capacity cascades down the rank order, pulling in lower-ranked eligible tracts that were previously excluded by the cap.

---

## 4. Data & Exact Algorithmic Reconstruction

### 4.1 Data Sources & Primary Unit of Analysis
The empirical substrate comprises:
1. The official HUD 2016 QCT master data file (`qct_data_2016.xlsx`, SHA-256: `75ae56ca258aabde75081739c401aa619886f0463a525d7cf786effbe9ba991f`) containing tract-level poverty, income, and margin-of-error estimates across the three operative ACS releases for all U.S. tracts.
2. Official HUD metropolitan area and non-metropolitan county allocation boundaries and population cap determinations.
3. Published official 2016 QCT designation determinations.

The primary unit of analysis is the **HUD QCT record** ($N = 85,390$). While there are 85,385 unique Census tract FIPS codes in the 2016 data, HUD splits rare tracts that cross metropolitan sub-area (HMFA) boundaries. Preserving these split records is essential for exact replication.

### 4.2 Reconstruction Validation (Tier A Standard)
Following prospective execution protocols, we reconstructed the year-specific 2016 HUD algorithm incorporating:
* Exact $c = 0.50$ precision checks on all poverty and income numerator/denominator components.
* Two-of-three release evaluation.
* Statutory dual-criterion priority sorting and intra-tier ranking.
* Area-specific cumulative population cap tracking and greedy skip-and-continue allocation.

**Validation Result:** Reconstructed final QCT designations matched official published designations across all records with **zero mismatches** (0 discrepancies across 85,390 records), satisfying the Tier A exact reproducibility standard.

---

## 5. Counterfactual Sensitivity Design

### 5.1 The Policy Contrast
Holding all observed survey inputs, thresholds, and ranking rules constant, we define the counterfactual designation mapping:
$$D_i(c) = \text{Algorithm}(X_i; c)$$
where $c \in \{0.50, 1.00\}$.

### 5.2 Core Estimands
1. **Union-Eligibility Loss Rate ($ELR$):**
   $$ELR = \frac{|E(1.00) \setminus E(0.50)|}{|E(1.00)|}$$
   where $E(c)$ denotes the set of tracts satisfying statutory eligibility under threshold $c$.
2. **Final Status Churn Rate ($CHR$):**
   $$CHR = \frac{|Q(0.50) \Delta Q(1.00)|}{|Q(1.00)|}$$
   where $Q(c)$ is the set of designated tracts, and $\Delta$ denotes the symmetric difference.
3. **Net Designation Rate Change ($NDR$):**
   $$NDR = \frac{|Q(0.50)| - |Q(1.00)|}{|Q(1.00)|}$$
4. **Standardized Burden Risk Difference ($BRD$):**
   To test whether the screen selectively excludes smaller communities, we evaluate the eligibility loss indicator $L_i = \mathbf{1}\{i \in E(1.00) \setminus E(0.50)\}$ across population quintiles. To control for confounding by socioeconomic distress, we standardize across strata defined by:
   - Eligibility type (poverty-only, income-only, or both); and
   - Quintiles of substantive threshold distance (margin of safety above the statutory cutoff).
   
   The standardized Burden Risk Difference between the lowest ($Q_1$) and highest ($Q_5$) population quintiles is:
   $$BRD = \sum_{s} w_s \left[ \Pr(L=1 \mid Q_1, s) - \Pr(L=1 \mid Q_5, s) \right]$$
   where $w_s$ represents the stratum population share.

---

## 6. Empirical Results

### 6.1 National Policy Sensitivity: Net Reductions vs. Gross Churn

Table 1 summarizes national eligibility and designation counts under the two precision thresholds.

#### Table 1: National Algorithmic Reconstruction and Policy Sensitivity (2016)
| Metric | Historical Loose Screen ($c=1.00$) | Official HUD Rule ($c=0.50$) | Difference | Relative Impact |
| :--- | :---: | :---: | :---: | :---: |
| **Reconstruction Mismatch Count** | — | **0** | — | Exact Replay |
| **Statutorily Eligible Tracts ($E(c)$)** | 17,042 | 16,368 | $-674$ | $-3.95\%$ |
| **Designated QCT Tracts ($Q(c)$)** | 14,057 | 13,619 | $-438$ | $-3.12\%$ |
| **Gross Status Churn ($|Q_1 \Delta Q_{.50}|$)** | — | — | **864** | **6.15%** |
| — Designation Losses ($L$) | — | — | 651 | 4.63% |
| — Designation Gains ($G$) | — | — | 213 | 1.52% |
| **Churn-to-Net-Change Ratio** | — | — | **$1.97\times$** | — |

Tightening the screen disqualified 674 tracts from statutory eligibility ($ELR = 3.95\%$) and produced a net reduction of 438 designated QCTs ($NDR = -3.12\%$). However, evaluating net changes severely understates policy instability: **864 tracts** experienced a flip in their federal designation status, representing a churn-to-net-change ratio of $1.97\times$.

---

### 6.2 The Anatomy of Status Churn

To understand how the precision filter propagates through the allocation algorithm, we decompose the 864 churned tracts into five mutually exclusive categories.

#### Table 2: 5-Part Mutually Exclusive Decomposition of Final Status Churn
| Component | Classification Definition | Tract Count | Share of Total Churn |
| :--- | :--- | :---: | :---: |
| **$L_1$** | Direct Eligibility Loss (Disqualified by $c=0.50$ screen) | **473** | 54.75% |
| **$L_2$** | Own-Screen Ranking Loss (Remains eligible; rank drops below cap) | **159** | 18.40% |
| **$L_3$** | **Strict Non-Local Loss** (Own data unchanged; displaced by cap shift) | **19** | 2.20% |
| **$G_1$** | Own-Screen Ranking Gain (Remains eligible; rank improves above cap) | **71** | 8.22% |
| **$G_2$** | **Strict Non-Local Gain** (Own data unchanged; pulled into cap by others' exit) | **142** | 16.44% |
| **Total** | **Exact Symmetric Difference ($L_1 + L_2 + L_3 + G_1 + G_2$)** | **864** | **100.00%** |
| *Spillover* | *Strict Non-Local Allocation Externalities ($L_3 + G_2$)* | *161* | *18.63%* |

While 54.75% of churn ($L_1 = 473$) reflects direct disqualification, the remaining 45.25% arises from ranking and cap interactions. Notably, **161 tracts** ($18.63\%$ of all churn) represent **strict non-local spillovers** ($L_3 + G_2$): their own survey point estimates, margins of error, and precision indicators were identical under both policies, yet their federal subsidy status changed purely due to reallocation under the 20% area population cap across 75 metropolitan areas and 31 states.

---

### 6.3 Population-Selective Exclusion

Table 3 evaluates whether the eligibility-loss burden falls disproportionately on low-population tracts.

#### Table 3: Eligibility Loss by Tract Population Quintile (2016)
| Population Quintile | Mean Tract Population | Baseline Eligible ($E_{100}$) | Disqualified ($L_1$) | Raw Loss Rate ($ELR_q$) |
| :--- | :---: | :---: | :---: | :---: |
| **Quintile 1 (Lowest)** | 1,842 | 3,287 | 349 | **10.62%** |
| **Quintile 2** | 3,115 | 3,409 | 133 | **3.90%** |
| **Quintile 3** | 4,281 | 3,411 | 95 | **2.79%** |
| **Quintile 4** | 5,612 | 3,405 | 49 | **1.44%** |
| **Quintile 5 (Highest)** | 8,429 | 3,530 | 36 | **1.02%** |
| **Gradient Ratio ($Q_1 / Q_5$)** | — | — | — | **$10.31\times$** |
| **Standardized Contrast ($BRD$)** | — | — | — | **$+12.24\text{ pp}$** |

In unadjusted terms, tracts in the lowest population quintile are more than ten times as likely to be disqualified as tracts in the highest quintile ($10.62\%$ vs. $1.02\%$). 

After standardizing across strata of substantive threshold proximity and eligibility type, the standardized Burden Risk Difference remains highly positive:
$$BRD = 0.122396 \approx +12.24\%$$
Even when comparing tracts with identical margins of economic distress above the statutory poverty or income cutoffs, smaller tracts face a **12.24 percentage-point higher risk** of exclusion solely due to ACS sample size constraints.

---

## 7. Discussion & Policy Implications

The empirical findings reveal critical structural tensions in federal algorithmic allocation:

1. **Noise Screens as De Facto Demographic Screens:**  
   Because survey variance is fundamentally tied to sample size, applying uniform precision thresholds creates an implicit bias against low-density and low-population jurisdictions. Rather than filtering out "bad data," the screen disproportionately excludes small communities whose true economic distress matches or exceeds that of larger urban tracts.
2. **Cap-Mediated Externalities:**  
   In competitive or capped allocation systems, data-quality decisions are never local. Excluding an unstable estimate in Tract A directly alters the funding probability for Tract B, even when Tract B’s data are perfectly precise. Policymakers who institute precision gates rarely account for these non-local reallocation dynamics.
3. **Implications for Administrative Data Governance:**  
   Administrative formulas require more nuanced reliability adjustments than hard threshold truncation. Potential alternative approaches include empirical Bayes shrinkage, small-area estimation models (e.g., Fay-Herriot estimators), or continuous variance penalties rather than sharp step-function exclusions.

---

## 8. Limitations & Claim Boundaries

To ensure scientific integrity, we explicitly note the methodological boundaries of this study:
* **No Latent Truth Identification:** We do not claim that $c = 0.50$ produces higher or lower true classification accuracy than $c = 1.00$. Estimating true misclassification would require identifying latent tract-level poverty distributions across overlapping multi-year ACS samples, which is not identifiable from public marginal estimates without unverifiable super-population assumptions.
* **Bounded Scope:** This study is an exact, identified policy sensitivity analysis of the 2016 nationwide establishment of the precision screen. It does not claim that identical numerical churn rates persisted across subsequent years.
* **Non-Normative Framing:** We evaluate the mechanical consequences of the policy screen; we do not make normative determinations regarding the optimal allocation of housing tax credits.

---

## 9. Reproducibility & Open Science Statement

All analyses in this study were conducted under a fail-closed, deterministic execution protocol. Raw data files are publicly available from the HUD User portal (`https://www.huduser.gov/portal/datasets/qct.html`). Reconstructed algorithms, parameter configurations, and analysis scripts are deposited in the immutable GitHub repository:  
`https://github.com/hurcheson/real-world-statistical-reliability`  
Commit Hash: `bdab3ff` (Replication Archive).

---

## References

* Bazuin, J. T., & Fraser, J. C. (2016). How the American Community Survey introduces systematic bias into public policy. *Poverty & Public Policy*, 8(2), 139–159.
* Folch, D. C., Arribas-Bel, D., Koschinsky, J., & Spielman, S. E. (2016). Spatial variation in the quality of American Community Survey data. *Demography*, 53(5), 1529–1554.
* Internal Revenue Code (IRC). Section 42: Low-Income Housing Credit. 26 U.S.C. § 42.
* McClure, K., Schwartz, A., & Taghavi, L. (2015). The Low-Income Housing Tax Credit: How well do the basis boosts work? *Cityscape*, 17(3), 187–208.
* Spielman, S. E., Folch, D., & Nagle, N. (2014). Patterns and causes of uncertainty in the American Community Survey. *Applied Geography*, 46, 147–157.
* U.S. Department of Housing and Urban Development (HUD). (2015). Qualified Census Tracts and Difficult Development Areas for 2016. *Federal Register*, 80(217), 69677–69688.
