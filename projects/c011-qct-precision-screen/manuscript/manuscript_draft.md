# Precision Screening and Geographic Coverage in HUD Qualified Census Tract Designation

## A deterministic 2016 policy-sensitivity analysis

**Evidence-locked manuscript draft — September 2026**

**Computational archive:** [hurcheson/real-world-statistical-reliability](https://github.com/hurcheson/real-world-statistical-reliability)

**Admissible evidence:** 2016 only; 74,272 HUD QCT records; zero official-replay mismatches

**Project disposition:** Manuscript-grade technical record. Under decision D037, C011 remains parked as a first-paper project because no multi-year recurrence claim is reproducible from retained provenance.

## Abstract

The U.S. Department of Housing and Urban Development (HUD) strengthened the data-quality screen used for 2016 Qualified Census Tract (QCT) designations under Internal Revenue Code Section 42. This study reconstructs HUD's 2016 national designation calculation and evaluates a same-data sensitivity contrast between a strict relative-margin-of-error screen of `MoE < 0.50 × estimate` and a looser `MoE < 1.00 × estimate` screen. The official `c=0.50` replay matches all 13,619 published designations across 74,272 HUD records, with zero record-level mismatches. Tightening the screen reduces union eligibility from 17,042 to 16,368 records and designation from 14,057 to 13,619 records. The net designation change is −438, while 864 records change status: 651 losses and 213 gains. A five-part decomposition assigns this churn to direct eligibility loss (473), own-screen ranking or cap loss (159), strict non-local loss (19), own-screen ranking or cap gain (71), and strict non-local gain (142). Thus 161 status changes occur even though the record's own six release-by-criterion precision indicators do not change. Among records eligible under the looser screen, raw eligibility-loss rates decline from 10.62% in the lowest population quintile to 1.03% in the highest. A prespecified standardization over eligibility type and substantive-threshold-distance quintile yields a burden risk difference of 0.122396. These results identify sensitivity of 2016 administrative eligibility and designation to the precision threshold. They do not identify latent classification accuracy, housing production, subsidy receipt, demographic effects, or recurrence in other years.

**Keywords:** Qualified Census Tracts; American Community Survey; margin of error; deterministic reconstruction; administrative allocation; policy sensitivity.

## 1. Introduction

Small-area policy formulas often combine survey estimates with deterministic eligibility and allocation rules. A precision screen can remove estimates judged too imprecise, but its administrative consequences depend on the rest of the formula. In QCT designation, release-level screening feeds a two-of-three eligibility rule, a ranking calculation, and a statutory population cap. Changing the screen can therefore alter both the status of records that fail it and the allocation of records whose own precision indicators are unchanged.

HUD's [2016 Federal Register notice](https://www.govinfo.gov/content/pkg/FR-2015-11-24/pdf/2015-29953.pdf) described a strengthened data-quality standard and noted that a 50% margin-of-error ratio corresponds approximately to a 30% coefficient of variation. The earlier operational rule rejected a positive estimate when its 90% confidence interval included zero, which is equivalent to the strict condition `MoE < estimate`. The 2016 contrast can therefore be represented by holding the 2016 workbook and all non-screen rules fixed while changing only the relative-MoE threshold from `c=1.00` to `c=0.50`.

The analysis asks three descriptive questions:

1. How many 2016 eligibility and final-designation statuses are sensitive to the screen threshold?
2. How does final-status churn divide between own-screen changes and cap-mediated changes?
3. How does eligibility loss vary across the population distribution after standardizing over eligibility type and threshold distance?

The contribution is a verified policy-sensitivity calculation, not a causal estimate. QCT status establishes geographic eligibility for an enhanced basis treatment; it is not a cash payment, a tax-credit allocation, or a guarantee that housing will be developed.

## 2. Institutional setting

Section 42 directs HUD to designate QCTs. The 2016 notice explains that eligible basis for a building in a designated QCT can be increased to as much as 130% of the otherwise applicable amount. State housing credit agencies still allocate credits under their qualified allocation plans, and QCT designation alone does not determine project selection or construction.

For 2016, HUD used three overlapping ACS five-year releases. A record can qualify through an income criterion, a poverty criterion, or both. Each release-level input must first pass the precision screen. Income uses a positive median-family-income estimate with `MoE < c × estimate`. Poverty requires positive numerator and denominator estimates and requires both margins of error to pass the same strict inequality. A criterion is eligible when its substantive threshold is satisfied in at least two of the three releases.

Eligible records are ranked within allocation areas. HUD's population cap limits designated QCT population to 20% of the relevant area population. The implementation uses a skip-and-continue allocation: an eligible record that would exceed the remaining cap is skipped while later records may still fit. The public [HUD QCT algorithm page](https://www.huduser.gov/portal/qct/QCT_Algorithm.html) documents the operational structure.

## 3. Data and reproducibility

The source is HUD's 2016 QCT workbook, `qct_data_2016.xlsx`:

- file size: 27,467,633 bytes;
- SHA-256: `75ae56ca258aabde75081739c401aa619886f0463a525d7cf786effbe9ba991f`;
- HUD records: 74,272;
- official designated records: 13,619.

The raw workbook is excluded from Git because of its size, but its identity is registered in the repository. The code preserves the workbook's record structure and constructs a stable 12-digit record key. The official `c=0.50` replay reproduces all 13,619 official designations with zero mismatches.

Three defensible income-arithmetic implementations—full-precision ratio, ratio rounded to seven decimals, and stored positive factor followed by raw fallback—produce identical eligibility and designation sets. Two fresh pipeline executions produce byte-identical output files. The automated suite checks half-up poverty-rate rounding, screen monotonicity, skip-and-continue allocation, the five-part partition, strict non-local invariants, and the full 2016 regression fixture.

## 4. Policy-sensitivity design

Let `E(c)` be the set eligible under screen threshold `c` and `Q(c)` the final designated set. The analysis compares `c=1.00` with `c=0.50` while holding the workbook, substantive thresholds, geography, ranking, rounding, and cap algorithm fixed.

The principal summaries are:

\[
ELR = \frac{|E(1.00) \setminus E(0.50)|}{|E(1.00)|},
\]

\[
CHR = \frac{|Q(1.00) \triangle Q(0.50)|}{|Q(1.00)|},
\]

and

\[
NDR = \frac{|Q(0.50)|-|Q(1.00)|}{|Q(1.00)|}.
\]

For each record, the own-screen vector contains six indicators: income and poverty precision-pass status for each of three releases. Status churn is partitioned as follows:

- `L1`: designated at `c=1.00`, not designated at `c=0.50`, and no longer eligible;
- `L2`: designation loss while remaining eligible and the own-screen vector changes;
- `L3`: designation loss while remaining eligible and the own-screen vector does not change;
- `G1`: designation gain and the own-screen vector changes;
- `G2`: designation gain and the own-screen vector does not change.

`L3 + G2` is the strict non-local count. “Non-local” refers to the unchanged own-screen vector; all survey inputs are fixed by design in both replays.

The population analysis is restricted to `E(1.00)`. Population quintiles are formed over those 17,042 records. The loss indicator equals one for `E(1.00) \ E(0.50)`. The standardized burden risk difference compares the lowest and highest population quintiles after standardizing over eligibility type (`income`, `poverty`, or `both`) and quintile of substantive-threshold distance:

\[
BRD = \sum_s w_s\{P(L=1\mid Q_1,s)-P(L=1\mid Q_5,s)\}.
\]

Here `w_s` is the share of looser-screen eligible records in stratum `s`. BRD is descriptive standardization, not a causal effect of population.

## 5. Results

### 5.1 Aggregate sensitivity

| Metric | `c=1.00` | `c=0.50` | Change |
|---|---:|---:|---:|
| Eligible records | 17,042 | 16,368 | −674 |
| Designated records | 14,057 | 13,619 | −438 |
| Binding allocation areas | 175 | 162 | −13 |

The eligibility-loss rate is 3.9549%. Final-status churn is 864 records, or 6.1464% of the `c=1.00` designated set. The 651 losses and 213 gains yield a net designation-rate change of −3.1159%.

### 5.2 Churn decomposition

| Component | Definition | Records | Share of churn |
|---|---|---:|---:|
| `L1` | Eligibility loss | 473 | 54.75% |
| `L2` | Remains eligible; own-screen vector changes | 159 | 18.40% |
| `L3` | Remains eligible; own-screen vector unchanged | 19 | 2.20% |
| `G1` | Gain; own-screen vector changes | 71 | 8.22% |
| `G2` | Gain; own-screen vector unchanged | 142 | 16.44% |
| Total | Exact partition | 864 | 100.00% |

The strict non-local count is 161 (`L3 + G2`), spanning 75 allocation areas and 31 state codes. This is 18.63% of all churn. Thirteen areas move from binding under `c=1.00` to nonbinding under `c=0.50`; none move in the opposite direction.

![Five-part churn decomposition](../outputs/figures/figure_2_churn_decomposition.svg)

### 5.3 Population gradient

| Population quintile | Eligible at `c=1.00` | Eligibility losses | Loss rate |
|---|---:|---:|---:|
| Q1, lowest | 3,409 | 362 | 10.619% |
| Q2 | 3,409 | 133 | 3.901% |
| Q3 | 3,411 | 95 | 2.785% |
| Q4 | 3,405 | 49 | 1.439% |
| Q5, highest | 3,408 | 35 | 1.027% |

![Eligibility loss by population quintile](../outputs/figures/figure_1_population_loss_gradient.svg)

The standardized burden risk difference is 0.122396, or 12.24 percentage points. This quantity should be interpreted as a standardized descriptive contrast under the fixed 2016 policy replay. It does not establish that population itself causes loss or that the same contrast holds in other designation years.

### 5.4 Precision observations retained

Across the three releases, the income screen passes 218,574 release-level observations at `c=1.00` and 215,578 at `c=0.50`, a difference of 2,996. The poverty screen, which requires both the positive numerator and denominator to pass, retains 208,988 observations at `c=1.00` and 118,854 at `c=0.50`, a difference of 90,134.

## 6. Interpretation and limitations

The replay establishes three bounded facts about the 2016 algorithm. First, the tighter screen changes more final statuses than the net count reveals. Second, cap and ranking operations propagate the threshold change to records whose own precision indicators are unchanged. Third, eligibility loss is more common in the lower population quintiles, and the contrast remains positive under the prespecified standardization.

The study does not estimate how many designations are statistically correct. The three ACS five-year releases overlap substantially, so they cannot be treated as independent replications; Census guidance warns against ordinary comparisons of overlapping period estimates. Published margins of error provide marginal uncertainty, not the cross-release covariance needed to infer a fixed latent tract state. The analysis therefore uses “precision purchased” only to describe which observations pass the administrative screen, not an observed accuracy gain.

The study also does not estimate housing construction, developer response, tax-credit allocation, fiscal incidence, or household outcomes. It does not classify the threshold as fair or unfair. The population contrast can reflect multiple features of survey design and tract composition and is not a demographic causal estimate.

Finally, the evidence is one designation year. Historical work on 2020–2022 and the 2026 development anchor remains part of the project record, but retained provenance does not support independent manuscript-grade regeneration. Under D037, the 2016 result cannot be used to claim recurrence or representativeness across 2016–2025, and C011 remains parked as a first-paper project absent materially new authoritative operational provenance.

## 7. Conclusion

A zero-mismatch reconstruction shows that the 2016 QCT designation map is materially sensitive to the relative-MoE threshold. Tightening the threshold changes 864 final statuses, including 161 strict non-local changes produced through ranking and cap interactions. Eligibility loss is concentrated in lower population quintiles in the observed data and in the prespecified standardized contrast. These findings support a reproducible description of the 2016 administrative mechanism. They do not support claims about latent accuracy, causal program outcomes, or multi-year recurrence.

## References

- U.S. Department of Housing and Urban Development. 2015. [Statutorily Mandated Designation of Difficult Development Areas and Qualified Census Tracts for 2016](https://www.govinfo.gov/content/pkg/FR-2015-11-24/pdf/2015-29953.pdf). *Federal Register* 80:73201–73207.
- U.S. Department of Housing and Urban Development. [QCT Designation Algorithm](https://www.huduser.gov/portal/qct/QCT_Algorithm.html).
- U.S. Census Bureau. 2010. [American Community Survey Design and Methodology, Chapter 12](https://www.census.gov/content/dam/Census/library/publications/2010/acs/acs_design_methodology_ch12.pdf).
- U.S. Census Bureau. 2022. [Period Estimates in the American Community Survey](https://www.census.gov/newsroom/blogs/random-samplings/2022/03/period-estimates-american-community-survey.html).
- Soltas, Evan. 2024. [Tax Incentives and the Supply of Low-Income Housing](https://evansoltas.com/papers/SoltasJMP.pdf). Working paper. Closest identified empirical neighbor; it reconstructs QCT assignment and uses ACS sampling variation for a housing-supply estimand rather than evaluating the precision screen as the policy object.

## Reproducibility statement

Run from `projects/c011-qct-precision-screen` after placing the registered workbook at `data/raw/qct_data_2016.xlsx`:

```bash
python -m pytest -v
PYTHONPATH=src python scripts/03_run_2016.py --output outputs/determinism/run1/2016
PYTHONPATH=src python scripts/03_run_2016.py --output outputs/determinism/run2/2016
python scripts/04_build_final_outputs.py
python scripts/05_build_manuscript_figures.py
python scripts/06_verify_manuscript.py
```
