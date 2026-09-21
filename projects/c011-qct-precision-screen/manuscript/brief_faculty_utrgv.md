# Research Brief for Faculty Feedback and Potential Collaboration

## C011: 2016 HUD QCT precision-screen sensitivity

**Repository:** [hurcheson/real-world-statistical-reliability](https://github.com/hurcheson/real-world-statistical-reliability)

**Evidence state:** 2016 only; 74,272 HUD records; zero official-replay mismatches

**Current disposition:** C011 is parked as a first-paper project under D037.

## Purpose

This brief requests methodological and institutional feedback on a reproducible analysis of HUD's 2016 Qualified Census Tract designation rule. It is not a co-authorship solicitation or a submission-ready claim.

The analysis holds HUD's 2016 workbook and allocation rules fixed and changes only the strict relative-margin-of-error screen from `MoE < 1.00 × estimate` to `MoE < 0.50 × estimate`.

## Verified results

| Quantity | Result |
|---|---:|
| HUD records | 74,272 |
| Official `c=0.50` designations | 13,619 |
| Reconstruction mismatches | 0 |
| Eligible, `c=1.00` / `c=0.50` | 17,042 / 16,368 |
| Designated, `c=1.00` / `c=0.50` | 14,057 / 13,619 |
| Losses / gains / total churn | 651 / 213 / 864 |
| Five-part partition | 473 / 159 / 19 / 71 / 142 |
| Strict non-local changes | 161 across 75 areas and 31 state codes |
| Standardized burden risk difference | 0.122396 |

The population-quintile loss rates are 10.619%, 3.901%, 2.785%, 1.439%, and 1.027% from the lowest to highest quintile.

## Interpretation boundary

QCT designation establishes geographic eligibility for enhanced basis treatment under Section 42. It is not a direct cash transfer, a project-level tax-credit allocation, or a guarantee of development. The replay measures administrative sensitivity; it does not identify true classification accuracy, program outcomes, demographic effects, fairness, or causal effects of population.

Only 2016 is manuscript-admissible from the retained provenance. Results from other years cannot support recurrence or representativeness claims. Faculty feedback would be most useful on:

1. whether the 2016 mechanism is worth preserving as a technical note or methods case;
2. whether the BRD standardization is the clearest descriptive summary;
3. whether authoritative operational provenance exists for additional years;
4. whether the Section 42 institutional description needs correction.

## Reproducibility

The exact workbook is 27,467,633 bytes with SHA-256 `75ae56ca258aabde75081739c401aa619886f0463a525d7cf786effbe9ba991f`. The repository includes the algorithm, output hashes, two-run determinism artifacts, five automated tests, two generated figures, and a manuscript verification script.
