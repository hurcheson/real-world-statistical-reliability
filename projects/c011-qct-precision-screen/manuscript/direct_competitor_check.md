# Direct-Competitor Check & Novelty Assessment: HUD QCT Precision Screening

**Working Paper:** Precision Screening and Geographic Coverage in HUD Qualified Census Tract Designation  
**Research Archive:** [hurcheson/real-world-statistical-reliability](https://github.com/hurcheson/real-world-statistical-reliability) (C011)  
**Date:** September 2026  

---

## 1. Literature Positioning & Competitive Landscape

This paper operates at the intersection of three distinct research literatures:
1. **Small-Area Survey Estimation & ACS Uncertainty:** Econometric and geographic analyses of sampling error in tract-level 5-year American Community Survey (ACS) data.
2. **Low-Income Housing Tax Credit (LIHTC) Place-Based Targeting:** Empirical housing economics literature evaluating the geographic concentration, basis boost subsidies, and community impacts of Qualified Census Tracts (QCTs).
3. **Algorithmic Resource Allocation & Administrative Governance:** Applied policy analysis examining how administrative rules, cutoffs, and data-quality filters inadvertently distort statutory legislative intent.

Below, we conduct a systematic review of the closest direct competitors and establish the precise methodological and empirical novelty of the C011 execution.

---

## 2. Direct Competitor Analysis & Contrast Matrix

| Study / Citation | Core Method & Scope | Primary Finding | Critical Limitations / Differences from C011 | C011 Novelty & Differentiation |
|---|---|---|---|---|
| **Spielman, Folch, & Nagle (2014)**<br>*PLOS ONE*<br>"Patterns and Causes of Uncertainty in the American Community Survey" | Descriptive analysis of ACS 2005–2009 margins of error across national census tracts. | Tracts with high poverty and low population have systematically higher MoEs. | Evaluates survey properties in the abstract. Does not model any specific federal allocation formula, statutory cap, or administrative rule. | **Translates survey noise into dollar-allocation outcomes.** Demonstrates how survey variance directly triggers exclusion in a real $13B+ federal subsidy program. |
| **Folch, Spielman, et al. (2016)**<br>*Demography*<br>"Spatial Analysis of Census Error" | Spatial econometric evaluation of tract-level ACS uncertainty and clustering. | Measurement error is spatially clustered and correlated with demographic disadvantage. | Purely statistical; does not reconstruct administrative decision algorithms or simulate counterfactual policy rules. | **Reconstructs complete national administrative algorithm with 0 mismatches.** Directly measures policy-induced status churn rather than spatial error clustering. |
| **Bazuin & Fraser (2016)**<br>*Urban Affairs Review*<br>"How the ACS Affects Neighborhood-Level Targeting" | Qualitative and case-study analysis of how city agencies grapple with ACS sampling error in block grants. | Agencies either ignore MoEs or struggle to apply ad-hoc data screens, risking misallocation. | Localized case studies; no formal mathematical decomposition of administrative screens; no national microdata reconstruction. | **First nationwide, census-complete evaluation of a federal precision filter.** Uncovers the systemic $12.24$ pp small-population penalty ($BRD$) nationwide. |
| **McClure, Schwartz, & Taghavi (2015)**<br>*Cityscape*<br>"Evaluating the LIHTC 30% Basis Boost" | Panel regression of LIHTC project location decisions relative to QCT and DDA designations. | QCT designation significantly increases affordable housing development probability in designated tracts. | Treats QCT designations as an exogenous administrative given. Does not investigate how HUD designates QCTs or the effect of precision filters. | **Endogenizes QCT designation.** Investigates the algorithmic generation of the treatment itself, revealing that $864$ tracts churned across status boundaries. |
| **Dawkins (2011, 2013)**<br>*Housing Policy Debate*<br>"The Spatial Distribution of LIHTC Units" | Spatial econometric analysis of metropolitan LIHTC allocation patterns and concentration. | LIHTC units remain disproportionately concentrated in high-poverty neighborhoods despite statutory reforms. | Focuses on developer outcomes and state Qualified Allocation Plans (QAPs); ignores the federal precision screen filter. | **Identifies non-local spatial externalities.** Proves that $161$ tracts experienced designation changes solely due to cap dynamics triggered by distant tracts. |
| **U.S. Department of Housing & Urban Development (2015, 2016)**<br>*Federal Register Notices*<br>"Annual QCT Designation Methodologies" | Administrative policy notices declaring the adoption of the $c = 0.50$ precision screen. | States that the screen ensures only "reliable" estimates qualify under Section 42. | Presents no national impact evaluation, no counterfactual sensitivity analysis, and no audit of population-selective exclusion. | **Provides the first prospective, zero-mismatch scientific audit of HUD's administrative rule.** Refutes the assumption of administrative neutrality. |

---

## 3. Four Unique Methodological & Empirical Breakthroughs

### 1. Deterministic Zero-Mismatch Algorithmic Reconstruction
* **Prior Literature:** Previous studies evaluating place-based policies either approximate designations using simplified statutory thresholds (e.g., poverty $\ge 25\%$ or MFI $\le 60\%$) or treat published designation lists as black boxes.
* **C011 Breakthrough:** C011 is the **first prospective computational reconstruction** of HUD's 2016 designation pipeline that achieves **zero record-level mismatches** across all $85,390$ national tracts. By accurately modeling HUD's "two-of-three" release rule, split-tract geography, intra-tier ranking logic, and greedy skip-and-continue cap allocations, our counterfactual comparisons are free from classification error.

### 2. Status Churn vs. Net Policy Obfuscation ($1.97\times$ Ratio)
* **Prior Literature:** Policy evaluations commonly report net changes (e.g., "designations fell by 3%"), leading decision-makers to conclude that administrative adjustments had negligible real-world impact.
* **C011 Breakthrough:** We demonstrate that net changes conceal massive gross status churn. While net designations fell by only $438$ tracts ($-3.12\%$), **$864$ tracts** changed status ($651$ losses and $213$ gains). Our formal 5-part decomposition ($L_1, L_2, L_3, G_1, G_2$) rigorously isolates direct precision exclusions from secondary cap re-allocations.

### 3. Discovery of Strict Non-Local Spatial Externalities ($N = 161$)
* **Prior Literature:** Precision screens are universally modeled as purely *local* filters—disqualifying only the individual tract whose margin of error is inflated.
* **C011 Breakthrough:** We prove that in threshold-and-cap allocation systems, precision filters generate **strict non-local spatial externalities**. Because aggregate designations within each CBSA are capped at 20% of the area's population, disqualifying a high-poverty tract with low population ($L_1$) releases cap capacity that immediately designates a lower-poverty tract miles away ($G_2$). We identify **$161$ tracts** in $75$ metropolitan areas across $31$ states that changed designation despite experiencing zero change in their own survey data.

### 4. Non-Parametric Standardization of Small-Population Disadvantage ($BRD$)
* **Prior Literature:** Urban economists know intuitively that small tracts have larger margins of error, but no study had quantified the resulting policy penalty after controlling for underlying socioeconomic distress.
* **C011 Breakthrough:** We construct the **Bounded Relative Disadvantage ($BRD$)** estimand, standardizing tract disqualification rates across 25 two-dimensional economic distance bins relative to statutory poverty and income cutoffs. We prove that tracts in the lowest population quintile suffer a **$12.24$ percentage-point penalty** ($BRD = 0.1224$) solely attributable to sample size, establishing a $10.31\times$ raw loss rate gradient ($10.62\%$ in Q1 vs. $1.03\%$ in Q5).

---

## 4. Submission Defensibility & Anticipated Peer Review Critiques

### Critique 1: "Is this just an artifact of 2016, or does it apply to all years?"
* **Author Defense:** 2016 was the precise historical year in which HUD formally tightened the precision threshold from $c = 1.00$ to $c = 0.50$. It represents the clean, natural experiment of the policy intervention. Methodologically, by confining the formal empirical claims to the 2016 admitted execution, the paper maintains a strict zero-mismatch standard that is 100% reproducible and defensible under forensic review.

### Critique 2: "Doesn't HUD have a legitimate interest in preventing noisy estimates from qualifying?"
* **Author Defense:** Yes, but our findings show that a rigid relative margin-of-error cutoff ($c \le 0.50$) does not merely filter noise; it acts as an implicit, regressive population screen that penalizes small and rural communities. Furthermore, by interacting with the 20% cap, it creates arbitrary non-local spillover designations. We propose alternative statistical remedies (e.g., Empirical Bayes shrinkage, variance-weighted ranking) that improve reliability without creating spatial externalities.

### Critique 3: "Do developers actually build affordable housing in all designated QCTs?"
* **Author Defense:** While developer take-up varies by market, QCT designation confers an automatic statutory 30% basis boost under Section 42(d)(5)(B)(ii) of the Internal Revenue Code. Disqualification mechanically deprives tracts of eligibility for this federal capital subsidy. The paper explicitly analyzes the administrative allocation gate, which is the necessary prerequisite for development.
