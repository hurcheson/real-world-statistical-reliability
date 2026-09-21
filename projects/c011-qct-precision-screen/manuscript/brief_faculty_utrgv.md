# Research Collaboration Brief: Algorithmic Precision Screening and Geographic Coverage in Federal Place-Based Housing Policy

**To:** Graduate Faculty & Prospective Co-Authors  
**From:** Research Team  
**Institution:** University of Texas Rio Grande Valley (UTRGV)  
**Date:** September 2026  
**Subject:** Co-Authorship & Working Paper: HUD Qualified Census Tract Precision Screening  
**Computational Repository:** [hurcheson/real-world-statistical-reliability](https://github.com/hurcheson/real-world-statistical-reliability) (Verified 2016 Replication Archive)  

---

## 1. Executive Summary & Core Discovery

Federal agencies increasingly distribute billions of dollars in place-based subsidies using algorithmic formulas built on American Community Survey (ACS) 5-year sample estimates. Because tract-level estimates suffer from sampling variance, the U.S. Department of Housing and Urban Development (HUD) in 2016 introduced an administrative **statistical precision screen** for Qualified Census Tract (QCT) designations under the **Low-Income Housing Tax Credit (LIHTC)**—the nation's primary affordable housing production program, deploying over $13 billion annually.

HUD lowered the permissible relative margin-of-error ratio from $c = 1.00$ to $c = 0.50$ ($RMoE \le 0.50$). While framed as a neutral statistical noise filter, our nationwide computational replay reveals that this administrative screen systematically redistributes housing capital away from smaller communities and generates severe spatial externalities:

1. **Reconstruction Fidelity:** We have reconstructed HUD's 2016 national designation algorithm across all **$85,390$ census tract records with zero mismatches** against published federal determinations ($100.000\%$ exact replication).
2. **Hidden Status Churn:** While net designations fell by only $438$ tracts ($-3.12\%$), gross designation churn affected **$864$ tracts** ($1.97\times$ the net reduction; $651$ losses, $213$ gains).
3. **Small-Population Penalty ($BRD$):** Because survey sampling variance scales inversely with population size ($\sigma \propto 1/\sqrt{n}$), tracts in the lowest population quintile face a **$12.24$ percentage-point higher risk of disqualification** ($BRD = 0.1224$) after standardizing for economic proximity to statutory thresholds ($10.62\%$ loss rate in Quintile 1 vs. $1.03\%$ in Quintile 5).
4. **Strict Non-Local Spillovers:** Through interaction with the statutory 20% area population cap, **$161$ tracts** in $75$ metropolitan areas across $31$ states changed designation status despite experiencing **zero change in their own survey data**.

---

## 2. Institutional & Regional Relevance for UTRGV

For the Rio Grande Valley (Cameron, Hidalgo, Starr, and Willacy counties), LIHTC subsidies and QCT 30% basis boosts are critical financing mechanisms for affordable housing development in colonias and small border municipalities. 

Our findings demonstrate that federal precision screens systematically penalize low-population and non-metropolitan census tracts—conflating small survey sample sizes with an absence of severe poverty. Partnering on this research allows UTRGV to lead a high-profile national policy dialogue on administrative data equity, small-area statistics, and federal formula design.

---

## 3. Ready Empirical & Computational Infrastructure

This is **not an exploratory proposal requiring months of data cleaning**. The entire empirical pipeline is already constructed, tested, and deterministically verified:

* **Complete Codebase & Invariant Suite:** Fully functional Python package (`qct_reliability`) implementing official HUD ranking logic, greedy skip-and-continue allocation, half-up rounding, and five-part status decomposition.
* **Deterministic Verification:** 5/5 automated test suites pass unconditionally (`pytest`). Independent executions yield bit-identical output tables across multiple intermediate arithmetic variants.
* **Public Data Integrity:** The raw 2016 master workbook (`qct_data_2016.xlsx`, $27.47\text{ MB}$) is cryptographically frozen via SHA-256 (`75ae56ca258aabde75081739c401aa619886f0463a525d7cf786effbe9ba991f`).
* **Prepared Manuscript Assets:** Full working paper draft, claim-evidence-limitation matrix, and complete empirical tables are available immediately for faculty review.

---

## 4. Co-Authorship Scope & Target Journal Strategy

We are seeking **one to two faculty co-authors** (Economics, Public Affairs, Statistics, or Urban Planning) to collaborate on the final polish, policy framing, and journal submission.

### Target Publication Venues
* **Primary Target:** *Journal of Policy Analysis and Management* (JPAM) — Premier policy analysis journal.
* **Specialized Targets:** *National Tax Journal* (NTJ) or *Journal of Housing Economics* (JHE).
* **Methodological Alternative:** *Journal of the American Statistical Association* (JASA: Applications & Case Studies).

### Collaborative Roles for Interested Faculty
1. **Institutional Framing:** Enhancing the policy narrative regarding Treasury/HUD rule-making, administrative procedure, and the political economy of the LIHTC basis boost.
2. **Econometric / Statistical Validation:** Reviewing our non-parametric standardization technique ($BRD$) and exploring potential extensions (e.g., Empirical Bayes shrinkage benchmarks).
3. **Grant Development:** Leveraging the working paper into an external funding proposal (e.g., National Science Foundation Methodology, Measurement, and Statistics (MMS); HUD Research Grants; or Russell Sage Foundation).

---

## 5. Summary Results Table for Review

```text
========================================================================================
HUD QCT 2016 POLICY SENSITIVITY REPLAY: CORE EMPIRICAL METRICS
========================================================================================
Total Nationwide Tract Records Evaluated:                  85,390
Reconstructed Official Designations (c = 0.50):           13,619
Reconstruction Mismatches against Published Record:            0  (100.00% exact)
----------------------------------------------------------------------------------------
Counterfactual Designations (c = 1.00):                   14,057
Net Designation Change (c = 1.00 -> c = 0.50):              -438  (-3.12%)
Gross Designation Churn (Losses + Gains):                    864  (6.15% turnover)
  - Direct Precision Screen Disqualifications (L1):          473
  - Secondary Cap Crowd-Out Losses (L2):                     159
  - Compound Priority Degradation Losses (L3):                19
  - Priority Tier Shift Gains (G1):                           71
  - Cap Vacancy Spillover Gains (G2):                        142
----------------------------------------------------------------------------------------
Strict Non-Local Spillovers (Tracts with Zero Data Change):  161  (75 CBSAs, 31 States)
Standardized Small-Population Disadvantage (BRD):         12.24%  (Q1: 10.62% vs Q5: 1.03%)
========================================================================================
```

### Next Steps
We invite interested faculty to review the working paper draft ([`manuscript_draft.md`](file:///d:/dev/research/real-world-statistical-reliability/projects/c011-qct-precision-screen/manuscript/manuscript_draft.md)) and empirical exhibits. Please contact the research team to arrange a brief introductory meeting or review repository access.
