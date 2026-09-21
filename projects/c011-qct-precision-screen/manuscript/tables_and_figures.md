# Tables and Figures Compendium: HUD QCT Precision Screening (2016 National Replay)

**Source Data:** Frozen Admitted Execution `outputs/final/` and `outputs/determinism/run1/2016/`  
**Dataset:** Official 2016 HUD Qualified Census Tract Master Dataset ($N = 85,390$ records)  
**Reconstruction Fidelity:** Zero mismatches against published designations ($100.000\%$)  

---

## Table 1: Baseline National Designation Summary & Counterfactual Totals (2016)

| Policy Regime / Metric | Baseline Administrative ($c = 0.50$) | Counterfactual Loose ($c = 1.00$) | Net Policy Difference ($\Delta$) | Relative Change (%) |
|---|---:|---:|---:|---:|
| **Total Census Tract Records Evaluated** | $85,390$ | $85,390$ | $0$ | $0.00\%$ |
| **Statutary Substantive Eligible Records ($E$)** | $16,368$ | $17,042$ | $-674$ | $-3.95\%$ |
| — Single-Criterion Eligible (Poverty Only) | $7,842$ | $8,189$ | $-347$ | $-4.24\%$ |
| — Single-Criterion Eligible (Income Only) | $2,876$ | $2,981$ | $-105$ | $-3.52\%$ |
| — Dual-Criterion Eligible (Poverty & Income) | $5,650$ | $5,872$ | $-222$ | $-3.78\%$ |
| **Final Designated Qualified Census Tracts ($Q$)** | **$13,619$** | **$14,057$** | **$-438$** | **$-3.12\%$** |
| — Official Published Determinations | $13,619$ | — | — | — |
| — Replication Mismatches | **$0$** | — | — | — |
| **Gross Designation Status Churn** | — | — | **$864$** | **$6.15\%$** |
| — Total Designation Losses ($L$) | — | — | $651$ | $4.63\%$ |
| — Total Designation Gains ($G$) | — | — | $213$ | $1.52\%$ |
| **Churn-to-Net Ratio ($\|L+G\| / \|\Delta Q\|$)** | — | — | **$1.97\times$** | — |

*Notes:* All records derived from official HUD 2016 administrative files (`qct_data_2016.xlsx`). $c$ denotes the maximum allowable ratio of the 90% margin of error to the point estimate ($RMoE \le c$). Designated tracts ($Q$) are constrained by the statutory 20% aggregate population ceiling within each metropolitan area (CBSA) and non-metropolitan county. Data source: `c011_final_master_results.csv`.

---

## Table 2: Complete Five-Part Status Churn Decomposition (2016)

| Category | Description & Allocation Mechanism | Tract Count | Share of Churn (%) | Share of Baseline $Q(1.00)$ (%) |
|---|---|---:|---:|---:|
| **$L_1$** | **Direct Precision Loss:** Disqualified by the $c=0.50$ screen; lost statutory eligibility ($E$). | $473$ | $54.75\%$ | $3.37\%$ |
| **$L_2$** | **Cap Crowd-Out Loss:** Retained eligibility ($E$), but crowded out by higher-ranked tracts under the 20% cap. | $159$ | $18.40\%$ | $1.13\%$ |
| **$L_3$** | **Compound Rank Loss:** Lost dual-criterion priority tier; excluded by cap in single-criterion tier. | $19$ | $2.20\%$ | $0.14\%$ |
| **Total Losses ($L = L_1 + L_2 + L_3$)** | **All Tracts Disqualified from Designation** | **$651$** | **$75.35\%$** | **$4.63\%$** |
| **$G_1$** | **Direct Priority Gain:** Shifted priority ranking tier, gaining designation under cap. | $71$ | $8.22\%$ | $0.51\%$ |
| **$G_2$** | **Cap Vacancy Gain (Externality):** Gained designation purely because $L_1$ tracts vacated cap capacity. | $142$ | $16.44\%$ | $1.01\%$ |
| **Total Gains ($G = G_1 + G_2$)** | **All Tracts Newly Designated under $c = 0.50$** | **$213$** | **$24.65\%$** | **$1.52\%$** |
| **Total Gross Churn** | **$\sum_{k=1}^3 L_k + \sum_{m=1}^2 G_m$** | **$864$** | **$100.00\%$** | **$6.15\%$** |
| **Strict Non-Local Spillovers** | **Tracts with $\Delta Q_i \neq 0$ and $\Delta \text{Screen}_i = 0$ ($L_3 + G_2$)** | **$161$** | **$18.63\%$** | **$1.15\%$** |

*Notes:* Partition sums exactly to 864 ($473 + 159 + 19 + 71 + 142 = 864$). Strict non-local spillovers ($N = 161$) represent tracts whose final federal designation changed solely as an indirect consequence of cap re-allocations driven by precision failures in other tracts within the same CBSA or county. Data source: `c011_final_decomposition.csv`.

---

## Table 3: Population Quintile Disparity and Bounded Relative Disadvantage ($BRD$)

| Population Quintile | Mean Tract Population | Population Range | Total Baseline Eligible ($E_{100}$) | Tracts Disqualified ($L_1$) | Unadjusted Loss Rate (%) | Standardized Loss Rate (%) |
|---|---:|---:|---:|---:|---:|---:|
| **Quintile 1 (Lowest)** | $1,842$ | $14 - 2,518$ | $3,287$ | $349$ | **$10.62\%$** | **$13.27\%$** |
| **Quintile 2** | $3,115$ | $2,519 - 3,694$ | $3,409$ | $133$ | $3.90\%$ | $4.88\%$ |
| **Quintile 3** | $4,281$ | $3,695 - 4,891$ | $3,411$ | $95$ | $2.79\%$ | $3.49\%$ |
| **Quintile 4** | $5,612$ | $4,892 - 6,530$ | $3,405$ | $49$ | $1.44\%$ | $1.80\%$ |
| **Quintile 5 (Highest)** | $8,429$ | $6,531 - 37,452$ | $3,530$ | $36$ | **$1.03\%$** | **$1.03\%$** |
| **Quintile 1 vs. Quintile 5 Ratio** | — | — | — | — | **$10.31\times$** | **$12.88\times$** |
| **Bounded Relative Disadvantage ($BRD$)** | — | — | — | — | — | **$+12.24\text{ pp}$** |

*Notes:* Quintiles are defined over the national distribution of census tracts with non-zero population. Standardized loss rate adjusts for distance to the statutory poverty ($25\%$) and median family income ($60\%$) thresholds using two-dimensional bin stratification across 25 economic distance bins. $BRD = 0.122396$ indicates that a low-population tract faces a 12.24 percentage-point higher risk of disqualification than an identical large-population tract at the exact same distance from the substantive cutoff. Data source: `c011_final_population_burden.csv` and `brd_strata.csv`.

---

## Table 4: Metropolitan Cap Dynamics and Non-Local Spatial Externalities

| Geographic / Allocation Metric | Value |
|---|---:|
| **Total Allocation Areas (CBSAs and Non-Metro Counties)** | $2,834$ |
| **Areas with Binding 20% Population Cap ($c = 1.00$)** | $175$ |
| **Areas with Binding 20% Population Cap ($c = 0.50$)** | $162$ |
| **Cap Transitions: Binding $\rightarrow$ Non-Binding** | **$13$** |
| **Cap Transitions: Non-Binding $\rightarrow$ Binding** | **$0$** |
| **Total Strict Non-Local Spillover Tracts ($L_3 + G_2$)** | **$161$** |
| — Allocation Areas Experiencing Non-Local Spillovers | $75$ |
| — U.S. States Represented | $31$ |
| — Non-Local Gainers ($G_2$: Designated Solely via Cap Vacancy) | $142$ |
| — Non-Local Losers ($L_3$: Displaced Solely via Cap Crowding) | $19$ |

*Notes:* Binding areas are those where total substantive eligible population exceeds the statutory 20% cap ceiling. When $c$ is tightened to $0.50$, disqualifications in 13 metropolitan areas reduced eligible population below the 20% cap, releasing all remaining eligible tracts into designation without ranking exclusions. Data source: `c011_final_cap_transitions.csv` and `c011_final_master_results.csv`.

---

## Table 5: Precision Purchased vs. Newly Excluded Observations by Release & Criterion

| Substantive Eligibility Criterion | Operative ACS Release | Total Observations Evaluated | Observations Passing at $c = 1.00$ | Observations Passing at $c = 0.50$ | Disqualified by Precision Screen ($c=0.50$) | Rejection Share (%) |
|---|---|---:|---:|---:|---:|---:|
| **Poverty Rate ($\ge 25\%$)** | ACS 2009–2013 | $85,390$ | $15,821$ | $15,249$ | $572$ | $3.62\%$ |
| Poverty Rate ($\ge 25\%$) | ACS 2008–2012 | $85,390$ | $15,412$ | $14,891$ | $521$ | $3.38\%$ |
| Poverty Rate ($\ge 25\%$) | ACS 2007–2011 | $85,390$ | $14,910$ | $14,418$ | $492$ | $3.30\%$ |
| **Median Family Income ($\le 60\%$)** | ACS 2009–2013 | $85,390$ | $10,114$ | $9,982$ | $132$ | $1.31\%$ |
| Median Family Income ($\le 60\%$) | ACS 2008–2012 | $85,390$ | $9,876$ | $9,754$ | $122$ | $1.24\%$ |
| Median Family Income ($\le 60\%$) | ACS 2007–2011 | $85,390$ | $9,620$ | $9,511$ | $109$ | $1.13\%$ |

*Notes:* Evaluates all individual tract-by-release observations. A single tract is evaluated across three distinct 5-year ACS releases per criterion. Disqualifying an individual release estimate prevents it from counting toward the statutory "two-of-three" rule. Poverty estimates exhibit higher relative margins of error and consequently suffer greater disqualification rates than median family income estimates. Data source: `c011_final_precision_purchased.csv`.

---

## Figure Concepts & Visual Architecture

### Figure 1: Algorithmic Pipeline and Non-Local Spillover Mechanism
```mermaid
flowchart TD
    subgraph DataInput ["1. Multi-Release ACS Survey Data"]
        ACS1["ACS 2009-2013 (Vintage 1)"]
        ACS2["ACS 2008-2012 (Vintage 2)"]
        ACS3["ACS 2007-2011 (Vintage 3)"]
    end

    subgraph Screen ["2. Administrative Precision Filter"]
        Check["Evaluate Relative MoE: MoE / Estimate <= c"]
        Pass1["c = 1.00: 17,042 Eligible Tracts"]
        Pass2["c = 0.50: 16,368 Eligible Tracts"]
    end

    subgraph TwoOfThree ["3. Statutory Two-of-Three Gate"]
        Qual["Tract Qualifies if >= 2 Releases Satisfy Poverty or Income Criteria"]
    end

    subgraph Allocation ["4. Capped Allocation Hierarchy"]
        Dual["Tier 1: Dual Eligible (Poverty & Income)"]
        Single["Tier 2: Single Eligible (Ranked by Distress)"]
        Cap{"Cumulative Area Pop <= 20%?"}
        Desig["Designated QCT"]
        Excl["Excluded by Cap"]
    end

    subgraph Externalities ["5. Emergent Churn & Externalities"]
        Direct["Direct Loss: L1 = 473"]
        Spillover["Strict Non-Local Spillovers: N = 161 (75 CBSAs, 31 States)"]
        Vacancy["Cap Vacancy Gain: G2 = 142"]
    end

    DataInput --> Check
    Check --> TwoOfThree
    TwoOfThree --> Allocation
    Allocation --> Cap
    Cap -- Yes --> Desig
    Cap -- No --> Excl
    Screen -. Tightening c to 0.50 .-> Externalities
```

### Figure 2: The Small-Population Disadvantage Gradient ($BRD$)
```text
Loss Rate (%)
  12% |    [Q1: 10.62%]
  10% |       *
   8% |
   6% |
   4% |             [Q2: 3.90%]
   2% |                *      [Q3: 2.79%]
   0% +--------------------------*------[Q4: 1.44%]--[Q5: 1.03%]
      0              2,000            4,000         6,000        8,000+
                               Tract Population
```
*Description:* Standardized probability of precision screen disqualification plotted across tract population quintiles, illustrating the steep $10.31\times$ unadjusted ($12.88\times$ standardized) risk gradient confronting low-population communities.
