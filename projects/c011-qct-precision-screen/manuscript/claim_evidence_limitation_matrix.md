# Claim–evidence–limitation matrix

| ID | Admissible claim | Evidence | Required limitation |
|---|---|---|---|
| C1 | The 2016 `c=0.50` implementation reproduces HUD's published designation vector exactly. | 74,272 records; 13,619 official and reconstructed designations; 0 mismatches; `c011_final_reconstruction_validation.csv`. | Applies only to 2016 and the registered workbook. |
| C2 | Tightening the screen from `c=1.00` to `c=0.50`, with other rules fixed, reduces eligibility by 674 and designation by 438 records. | `E100=17,042`, `E050=16,368`, `Q100=14,057`, `Q050=13,619`; `c011_final_master_results.csv`. | Same-data policy sensitivity, not a causal estimate or evaluation of latent accuracy. |
| C3 | Net designation change understates final-status movement. | 651 losses, 213 gains, 864 churn; `CHR=0.061464`; master results. | Churn is relative to `Q(1.00)`, not all 74,272 records. |
| C4 | Churn partitions exactly into `473/159/19/71/142`. | `c011_final_decomposition.csv`; invariant test. | Use the operational definitions in the protocol. Do not relabel the components as causal mechanisms. |
| C5 | 161 changes are strict non-local under the own-screen-vector definition. | `L3+G2=19+142`; 75 allocation areas; 31 state codes. | “Non-local” means own precision-pass vector unchanged. It does not mean inputs changed elsewhere; inputs are fixed in both replays. |
| C6 | Eligibility-loss rates are higher in lower population quintiles in 2016. | Q1–Q5 losses `362/133/95/49/35`; rates `10.619/3.901/2.785/1.439/1.027%`. | Descriptive association. No unsupported demographic, rural, fairness, or causal interpretation. |
| C7 | The standardized burden risk difference is 0.122396. | `brd_strata.csv` and `annual_result.csv`; standardized over eligibility type and threshold-distance quintile. | Do not call BRD a regression coefficient, an adjusted causal effect, or proof of discrimination. |
| C8 | The tighter screen retains fewer release-level criterion observations. | Income: 218,574 to 215,578; poverty: 208,988 to 118,854. | “Precision purchased” refers to the administrative pass condition, not measured improvement in true classification. |
| C9 | QCT designation can make a building eligible for enhanced basis treatment. | HUD 2016 notice and IRC Section 42 summary. | Not a direct cash subsidy, tax-credit allocation, construction decision, or guaranteed 30% increase. |
| C10 | The package is reproducible on the registered input. | Workbook SHA-256, two byte-identical runs, 5 passing tests, `06_verify_manuscript.py`. | Raw workbook is excluded from Git; users must obtain the exact registered file. |

## Prohibited manuscript claims

- recurrence, prevalence, typical magnitude, or representativeness across 2016–2025;
- improved or reduced true classification error;
- effects on housing production, developer behavior, households, or fiscal incidence;
- demographic redistribution, rural disadvantage, bias, fairness, or discrimination without additional evidence;
- novelty stated as “first” without a completed, current systematic literature search;
- a recommendation to publish C011 as the first paper under the current D037 evidence state.
