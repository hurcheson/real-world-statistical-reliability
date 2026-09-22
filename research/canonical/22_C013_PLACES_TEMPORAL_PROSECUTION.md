---
title: O002-A1 Full Prosecution — PLACES as Longitudinal Data
version: 1.0.0
last_updated: 2026-09-21
status: survives-register-next-candidate
decision: REGISTER NEXT AVAILABLE CANDIDATE AND ADVANCE TO CONTROLLED EXECUTION DESIGN
---

# O002-A1 Full Prosecution — PLACES as Longitudinal Data

## 1. Binding decision

> **REGISTER NEXT AVAILABLE CANDIDATE AND ADVANCE TO CONTROLLED EXECUTION DESIGN**

O002-A1 survives full prosecution. Under the current registry state, the next available identifier is **C013**.

The registered object is narrow:

> **A release-provenance and temporal-interpretability audit of repeated PLACES/500 Cities estimates, with exact carry-forward detection and conclusion-level sensitivity analysis.**

The object is not a new small-area estimator, a claim that PLACES is defective, a general estimated-dependent-variable theory paper, or a blanket declaration that every repeated-release analysis is invalid. It is a reproducible audit of whether nominally repeated PLACES observations contain distinct temporal information, whether measure definitions and geography/population rules remain comparable, and which published conclusions survive provenance-aware restrictions.

This prosecution assigns the next candidate number but does not authorize manuscript drafting, author contact, or claims that release-to-release differences estimate true local health change.

## 2. Why the candidate survives

The full gate is cleared for five reasons.

1. **A complete, rule-defined eligible corpus exists.** Nine works were verified as using at least two PLACES/500 Cities releases or explicitly treating cross-release PLACES differences as temporal information. They span peer-reviewed articles, a conference abstract, a preprint, and a dissertation.
2. **The failure mechanism is exact, not speculative.** For rotating BRFSS measures, nominally adjacent releases can be deterministic copies. In the regional mammography audit, all four carried-forward release pairs were 100% identical tract by tract. In the national colorectal-screening audit, the 2020→2021 county pair was 100% identical and the 2024→2025 pair was 99.97% identical after common-county restriction.
3. **The audit discriminates rather than merely criticizes.** Washington, DC obesity, diabetes, cancer, and poor-mental-health series contained six distinct annual source years; Milwaukee poor-mental- and poor-physical-health series contained five. Those series do not exhibit the deterministic carry-forward mechanism, even though CDC's broader local-trend restriction still applies. High cholesterol in the same DC analysis contained only four distinct source years and two exact copied pairs.
4. **Published temporal conclusions change under provenance-aware interpretation.** Rahman et al.'s nine nominal annual mammography releases collapse to five biennial source waves. A colorectal-screening pre/post analysis uses a rotating measure whose paired years contain no new outcome information and whose target age definition changes across plausible archive mappings. These are decision-relevant changes, not wording-only corrections.
5. **No direct collision was located.** CDC and prior methods papers state important use limitations, but the search found no existing study that joins a temporal-use corpus, release/measure crosswalk, exact-copy diagnostics, and conclusion-level reanalysis of downstream PLACES studies.

## 3. Scope, estimand, and fairness boundary

### 3.1 Audit estimand

For a published repeated-release analysis, the audit asks:

> After replacing nominal release time with documented BRFSS source time, removing deterministic carry-forwards, harmonizing measure definitions and geography/population rules, and respecting reported uncertainty, does the study retain the temporal contrast, ordering, hotspot/set classification, or decision statement it claims?

The audit does **not** estimate the true local health trajectory. A difference between two distinct PLACES source waves still combines possible health change with survey composition, fitted-model, covariate, poststratification, geographic, and definition changes.

### 3.2 Governing use boundary

CDC states that the current modeling procedure does not support tracking local changes over time. At subcounty levels, PLACES uses fixed 2010/2020 Census poststratification populations and therefore does not incorporate year-to-year local population change. At county level, annual population estimates are used, but time is not a model variable. CDC also advises considering confidence intervals and warns against using the estimates to evaluate local programs or policies. See the [PLACES FAQ](https://www.cdc.gov/places/faqs/index.html).

That agency statement is the governing interpretive boundary. The candidate's added value is to quantify how downstream temporal analyses behave when that boundary is operationalized.

### 3.3 Fairness rules

- Cross-sectional comparisons are outside the target unless the paper explicitly interprets differences across releases as change.
- A paper is not classified as “wrong” merely because it uses repeated PLACES data.
- Exact-copy findings are attributed to release construction, not to author misconduct.
- Model-level conclusions are not declared reproduced when only the public outcome panel can be reconstructed.
- Surviving results are reported alongside fragile results.
- When release identifiers, code, weights, or spatial-neighbor definitions are unavailable, the result is a bounded reproduction or non-reproduction, not an accusation.

## 4. Search and deduplication ledger

### 4.1 Search protocol

Search date: **2026-09-21**. Coverage was from the first 500 Cities release through the search date.

Eligibility required either:

1. use of at least two distinct PLACES/500 Cities releases for an outcome, covariate, index, or classification; or
2. an explicit interpretation of cross-release PLACES differences as change, trend, longitudinal association, pre/post effect, persistence, temporal hotspot, or projection.

The search used:

- OpenAlex title/abstract discovery;
- PubMed and PubMed Central;
- Crossref DOI metadata;
- publisher full text and supplements where accessible;
- dissertation/repository, preprint, and conference-abstract discovery;
- CDC PLACES/500 Cities release documentation and Socrata catalog metadata;
- backward and forward citation checks from eligible studies and the closest methodological ancestors.

Four focused OpenAlex queries (`"CDC PLACES" longitudinal`, temporal, trend; and `"500 Cities" longitudinal health`) returned 400 top-ranked records and **289 unique DOI/OpenAlex records after deduplication**. A prior broader two-query cursor scan had screened **1,668 unique works**. Candidates were then deduplicated by DOI, normalized title, and repository/published-version linkage. Search-engine results were used for discovery only; eligibility was verified against an abstract, full text, repository record, or primary metadata.

Representative exact concepts:

- `CDC PLACES` AND longitudinal / temporal / annual / trend / change;
- `500 Cities` AND neighborhood health change / longitudinal;
- `PLACES` AND source year / carried forward / release provenance / validity;
- exact eligible titles, DOI chaining, author/repository records, and citing works.

### 4.2 Inclusion ledger

| ID | Work | Status | Why eligible | Evidence level |
|---|---|---|---|---|
| E1 | Candipan, Riley & Easley, *While Some Things Change, Do Others Stay the Same?* DOI `10.1080/10511482.2022.2076715` | Peer-reviewed article, 2023 | Models tract health change between two 500 Cities periods in relation to gentrification | Full-text/indexed-method verification |
| E2 | Hunyadi et al., *Spatial and Temporal Patterns of Chronic Disease Burden in the U.S., 2018–2021*. DOI `10.1016/j.amepre.2024.08.022` | Peer-reviewed article, 2025 | Constructs annual county CDBIs from 20 PLACES measures and interprets temporal burden patterns | Publisher abstract/methods; supplement blocked |
| E3 | Mohebbi et al., *A Computational Approach to Analyzing Spatiotemporal Trends in Gun Violence and Mental Health Disparities*. DOI `10.1007/s11524-025-00976-x` | Peer-reviewed open-access article, 2025 | Uses PLACES physical/mental-health outcomes labeled 2014–2018 in a longitudinal/spatiotemporal analysis | Full text |
| E4 | Nguyen et al., *Changes in the Neighborhood Built Environment and Chronic Health Conditions in Washington, DC, in 2014–2019*. DOI `10.2196/74195` | Peer-reviewed open-access article, 2025 | Treats annual tract PLACES outcomes as a longitudinal panel in mixed models with changing built-environment predictors | Full text |
| E5 | Al Qady et al., *S574 Examining Colorectal Cancer Screening Patterns Across US Counties Using Geospatial Analysis Pre- and Post-COVID-19*. DOI `10.14309/01.ajg.0001129756.58233.3d` | Conference abstract, 2025 | Claims county screening change from 2018–2019 to 2022–2023, spatial clusters, and resource-allocation relevance | Complete indexed abstract |
| E6 | Rahman et al., *Historical Redlining and Spatiotemporal Patterns in Breast Cancer Screening*. DOI `10.1001/jamanetworkopen.2026.30685` | Peer-reviewed article, 2026 | Models nominal annual tract mammography estimates for 2016–2024, reports peaks/stability/decline, and projects 2025–2026 | Full text and supplement description |
| E7 | Akomaning et al., *Temporal Trends in Stroke Prevalence Across North Dakota Before, During, and After the COVID-19 Pandemic*. DOI `10.1016/j.neuros.2026.100034` | Conference/supplement article, 2026 | Explicit multi-period county PLACES stroke trends | Abstract/metadata |
| E8 | Rapaka & Kaushik, *Reshaping Oral Health Inequities—Pandemic Impact on Geo-Spatial Structures of Geriatric Tooth Loss*. DOI `10.20944/preprints202602.0362.v1` | Preprint, 2026 | Compares ZCTA tooth-loss estimates for 2018, 2020, and 2022 as pandemic-period change | Preprint metadata/abstract |
| E9 | *The temporal relations among neighborhood-level binge drinking, depression, and gun violence*. DOI `10.7282/t3-xd0f-8817` | Dissertation, 2026 | Retrospective longitudinal use of 500 Cities/PLACES outcomes | Repository record |

### 4.3 Exclusion ledger

| Exclusion class | Examples | Decision rule |
|---|---|---|
| Single-release PLACES health outcome | Andrews et al., DOI `10.1016/j.amepre.2025.108087`; stroke/lending abstract DOI `10.1161/str.56.suppl_1.tp319` | Historical or longitudinal exposure does not make the PLACES outcome temporal |
| PLACES only as a baseline/cross-sectional covariate | Park-visitation, air-pollution, redlining, and social-determinant studies returned by broad searches | Exclude unless ≥2 releases or cross-release change is interpreted |
| Temporal outcome comes from another source | Lung-cancer clusters, mortality trends, gun-incident time series where PLACES is a single contextual layer | Exclude from the temporal-PLACES corpus |
| Methods/agency descriptions | Greenlund et al. 2022; CDC methodology/FAQ | Retain as governing or ancestor evidence, not downstream temporal applications |
| General estimated-dependent-variable theory | Lewis & Linzer 2005 and later EIV/EDV work | Ancestor, not direct collision or eligible application |
| Duplicate/preprint-published pair | Repository manuscripts and final journal versions | Keep the most complete version; retain earlier version only for active-work chronology |
| Ambiguous title/abstract with no verifiable multi-release use | Search hits whose abstracts say “longitudinal” but identify only one PLACES release | Exclude conservatively |

## 5. Dual coding of the complete eligible corpus

### 5.1 Procedure and agreement

The nine eligible works were coded twice using separate passes:

- **Pass A — source/provenance coding:** geography, release labels, BRFSS source years, measure rotation, definition/geography changes, and available uncertainty.
- **Pass B — claim/decision coding:** temporal estimand, analysis form, interpretation strength, decision audience, provenance disclosure, and the conclusion most exposed to a provenance-aware restriction.

This was dual-pass coding by one investigator, not independent dual-human coding; it reduces extraction drift but does not estimate inter-rater reliability. The two passes agreed on eligibility for **9/9 works**, on the primary temporal-use class for **8/9**, and on the primary fragility class for **8/9**. The one use-class disagreement was Mohebbi et al.: the title/abstract suggests a longitudinal health series, whereas the methods show that the formal time-series procedures are applied to gun incidents and PLACES health estimates are mapped/associated over 2014–2018. It remains eligible under the explicit cross-release interpretation rule but is coded “contextual temporal layer,” not “health-trend model.”

### 5.2 Final coding table

| ID | Geography | Temporal role of PLACES | Analysis form | Provenance disclosure | Decision-facing language | Primary audit risk |
|---|---|---|---|---|---|---|
| E1 | Tract, multi-city | Two-wave outcome change | Change score/regression | Limited | Neighborhood-health implications | Release/source alignment; boundary comparability |
| E2 | County, national | Annual composite outcome | PCA index, quintiles, Gi* hotspots, regression | Not visible in accessible methods | Burden prioritization/resource allocation | Mixed source years within each annual composite; ranking prohibition |
| E3 | Tract, Milwaukee | Contextual temporal health layer | Bivariate maps/local association; gun-violence time series | Source period stated, release IDs absent | Place-sensitive intervention | Health waves distinct, but local-trend and association interpretation remain limited |
| E4 | Tract, Washington, DC | Annual outcomes in longitudinal mixed models | Random tract/year effects and changing predictors | Modeled-estimate limitation only | Urban-development/health implications | One rotating outcome has copied waves; no joint covariance; changing coverage |
| E5 | County, national | Pre/post outcome change and cluster change | ΔRate, Local Moran's I, SVI stratification | Release IDs/definitions absent from abstract | Actionable screening-gap/resource allocation | Each two-year period is one copied source wave; definition change; result not reproducible under plausible mappings |
| E6 | Tract, KS/MO redlined areas | Nominal annual outcome trajectory and forecast | Bayesian spatiotemporal AR(1)/ICAR | General modeled-estimate limitation only | Outreach and resource allocation | Four deterministic pseudo-waves; annual effective n overstated |
| E7 | County, North Dakota | Before/during/after trend | Conference analysis | Unknown | Pandemic-period interpretation | Time absent from PLACES county model; release mapping required |
| E8 | ZCTA, national | Three-period pandemic comparison | Spatial comparison/hotspots | Preprint-level | Oral-health inequity targeting | Rotating tooth-loss measure; source-year and definition/geography harmonization |
| E9 | Neighborhood/tract | Lagged temporal relations | Dissertation longitudinal models | Repository text not fully exposed | Gun-violence/mental-health interpretation | Outcome timing, carry-forward, and estimated-outcome dependence |

## 6. Final measure-by-release provenance crosswalk

The crosswalk below is based on CDC's release history and was verified against live Socrata records by grouping `measureid × year` in each tract release.

| Release | Product/scope | Main BRFSS source | Older/carried source and measures | Temporal comparability notes |
|---:|---|---|---|---|
| 2016 | 500 Cities, city/tract | 2014 for 23 measures | 2013: BPHIGH, BPMED, CHOLSCREEN, HIGHCHOL | 2010 geography/population base |
| 2017 | 500 Cities, city/tract | 2015 for 20 measures | 2014 carry-forward: TEETHLOST, DENTAL, MAMMOUSE, PAPTEST, COLON_SCREEN, COREM/COREW, SLEEP | Seven rotating constructs; core older-adult service appears as sex-specific measures in the file |
| 2018 | 500 Cities, city/tract | 2016 for 23 measures | 2015 carry-forward: BPHIGH, BPMED, CHOLSCREEN, HIGHCHOL | Same 500 Cities geography |
| 2019 | 500 Cities, city/tract | 2017 for 20 measures | 2016 carry-forward: TEETHLOST, DENTAL, MAMMOUSE, PAPTEST, COLON_SCREEN, COREM/COREW, SLEEP | Same values can appear under a new release label |
| 2020 | First PLACES national county/place/tract/ZCTA release | 2018 for 23 measures | 2017: BPHIGH, BPMED, CHOLSCREEN, HIGHCHOL | Coverage expands nationally; PAPTEST becomes CERVICAL; cross-product geography changes |
| 2021 | National PLACES | 2019 for 22 measures plus DEPRESSION and GHLTH | 2018 carry-forward: TEETHLOST, DENTAL, MAMMOUSE, CERVICAL, COLON_SCREEN, COREM/COREW, SLEEP | Twenty-nine measures total |
| 2022 | National PLACES | 2020 for 25 measures | 2019: BPHIGH, BPMED, CHOLSCREEN, HIGHCHOL | Pre-2023 CI procedure |
| 2023 | National PLACES | 2021 for 29 measures | 2020 carry-forward: TEETHLOST, DENTAL, MAMMOUSE, CERVICAL, COLON_SCREEN, COREM/COREW, SLEEP | Seven disability measures added; CI simulation assumption changes |
| 2024 | National PLACES | 2022 for 36 measures | 2021: BPHIGH, BPMED, CHOLSCREEN, HIGHCHOL | Seven health-related social-needs measures added; CERVICAL unavailable; KIDNEY and older-adult core service discontinued; adult-population ≥50 reporting rule replaces total-population ≥50 rule |
| 2025 | National PLACES | 2023 for 35 measures | 2022: TEETHLOST, DENTAL, MAMMOUSE, COLON_SCREEN, SLEEP | Forty measures; social isolation renamed loneliness; CERVICAL remains absent |

### Cross-cutting discontinuities

- **Release year is not source year.** A nominal annual sequence can alternate new and carried estimates.
- **Measure definitions change.** The colorectal-screening definition, for example, changes from adults aged 50–75 in the 2020/2021 files to adults aged 45–75 in the 2024/2025 files.
- **Coverage changes.** The 2020 transition expands from 500 selected cities to national tract coverage.
- **Population eligibility changes.** Before 2024, reporting required total population ≥50; from 2024, adult population ≥50 is the stated rule.
- **Poststratification is not annual at subcounty scale.** Place, tract, and ZCTA estimates use fixed decennial population distributions.
- **Interval construction changes in 2023.** Before 2023, random-effect simulation error varied within population categories; beginning in 2023, it varies only within counties, producing potentially wider intervals.
- **Published files do not provide cross-release joint covariance.** Apparent precision of differences, slopes, or autoregressive effects cannot be obtained by treating marginal release CIs as independent repeated-observation errors.

## 7. Three contrasting reproductions

All reproductions used the official CDC Socrata API, explicit dataset IDs, crude or age-adjusted prevalence as specified, exact geographic-ID or state/county-name linkage, and common-unit restriction. They reproduce the temporal support of the published analysis. They do not claim to reproduce unavailable proprietary code, complete Bayesian/spatial models, or unreported data-processing choices.

### 7.1 Reproduction R1 — Rahman et al. mammography, 2016–2024

**Published use.** Rahman et al. describe a longitudinal ecological study of annual tract mammography prevalence, model time with AR(1) structure, report a 2018–2019 peak, stability through 2023, decline in 2024, and 2025–2026 projections. Results were shared for outreach and resource-allocation planning.

**Archive reconstruction.** The audit queried `MAMMOUSE`, `CrdPrv`, Kansas and Missouri tracts from releases 2016–2024 (`9z78-nsfp`, `vurf-k5wr`, `rja3-32tc`, `6vp6-wxuq`, `4ai3-zynv`, `373s-ayzu`, `nw2y-v4gm`, `em5e-5hvn`, `ai6z-tcin`). Adjacent comparisons used common tract IDs.

| Nominal pair | Source years | Common tracts | Exact equality | Median absolute change | Spearman ρ | Nonoverlapping marginal CIs |
|---|---|---:|---:|---:|---:|---:|
| 2016→2017 | 2014→2014 | 722 | **100.00%** | 0.0 pp | 1.00000 | 0.00% |
| 2017→2018 | 2014→2016 | 722 | 0.97% | 5.0 pp | 0.53107 | 37.53% |
| 2018→2019 | 2016→2016 | 722 | **100.00%** | 0.0 pp | 1.00000 | 0.00% |
| 2019→2020 | 2016→2018 | 722 | 3.05% | 1.8 pp | 0.79904 | 4.57% |
| 2020→2021 | 2018→2018 | 2,147 | **100.00%** | 0.0 pp | 1.00000 | 0.00% |
| 2021→2022 | 2018→2020 | 2,147 | 0.93% | 1.4 pp | 0.78161 | 1.12% |
| 2022→2023 | 2020→2020 | 2,147 | **100.00%** | 0.0 pp | 1.00000 | 0.00% |
| 2023→2024 | 2020→2022 | 1,797 | 1.06% | 2.1 pp | 0.67656 | 0.83% |

**Sensitivity result.** Nine nominal annual releases reduce to five source years: 2014, 2016, 2018, 2020, and 2022. Excluding carry-forwards removes four AR(1) time points. The 2018–2019 “peak” is one 2016 BRFSS estimate printed twice; portions of the stated stability through 2023 are deterministic. Rank and threshold sets are perfectly stable in copied pairs by construction, whereas rank correlations fall to 0.53–0.80 when source years change.

**Conclusion classification.** Cross-sectional statements about many tracts being below the 80.3% target may remain useful. The archive does not support a nine-wave annual local trajectory, annual persistence, or annual forecasting interpretation. A defensible description is five biennial modeled snapshots with additional coverage/model discontinuities.

### 7.2 Reproduction R2 — Nguyen et al. Washington, DC, 2014–2019

**Published use.** Nguyen et al. use 434,115 Google Street View images and tract-level health outcomes described as annual 2014–2019 PLACES data. Mixed-effects models associate changing built-environment features with obesity, diabetes, high cholesterol, cancer, and poor mental health.

**Archive reconstruction.** The audit mapped source years 2014–2019 to releases 2016–2021 and restricted all five outcomes to the 178 tracts present in every release.

| Measure | Nominal releases | Distinct source years | Exact copied adjacent pairs | Common-tract endpoint change | Release-time slope | Source-time slope |
|---|---:|---:|---|---:|---:|---:|
| Obesity | 6 | 6 | None | +2.684 pp | +0.3999 pp/y | +0.3999 pp/y |
| Diabetes | 6 | 6 | None | +0.238 pp | −0.0088 pp/y | −0.0088 pp/y |
| High cholesterol | 6 | **4** | 2017→2018 and 2019→2020, both **100% exact** | −6.517 pp | −1.2719 pp/y | −1.1267 pp/y |
| Cancer | 6 | 6 | None | +0.339 pp | +0.0907 pp/y | +0.0907 pp/y |
| Poor mental health | 6 | 6 | None | +2.056 pp | +0.4900 pp/y | +0.4900 pp/y |

For high cholesterol, the six nominal releases correspond to source years 2013, 2015, 2015, 2017, 2017, and 2019. The two carried pairs have 0.0-point change and 0% nonoverlapping intervals. For the four annually sourced measures, adjacent exact equality is low rather than deterministic, and source-time and release-time slopes coincide.

**Sensitivity result.** Stable-measure restriction does not eliminate the entire analysis: obesity, diabetes, cancer, and poor mental health retain six distinct source waves. It does, however, reduce high-cholesterol time information by one third and changes its fitted slope. Interval-aware checks also show that most adjacent tract differences for the annually sourced measures have overlapping marginal CIs; marginal overlap is not a formal difference test because cross-release covariance is unavailable.

**Conclusion classification.** This is a partial fragility, not a wholesale failure. The analysis supplies the candidate's needed negative control: provenance rules distinguish a rotating copied outcome from outcomes with distinct source years. Causal or true-local-change language remains unsupported, but the deterministic carry-forward critique applies specifically to high cholesterol.

### 7.3 Reproduction R3 — Al Qady et al. county colorectal screening, pre/post COVID-19

**Published use.** The abstract reports age-adjusted county colorectal-screening prevalence for “2018–2019” versus “2022–2023,” a median change of +1.6 percentage points across 3,108 counties, Local Moran clusters, SVI gradients, and actionable recovery/resource-allocation implications.

**Archive facts.** `COLON_SCREEN` is an even-year rotating measure. County releases 2020 and 2021 both contain the 2018 source estimates; releases 2022 and 2023 both contain the 2020 source estimates; releases 2024 and 2025 both contain the 2022 source estimates. In 2024/2025, the definition changes from ages 50–75 to 45–75.

On 3,126 common counties:

| Pair | Source years | Exact equality | Median change | Nonoverlapping marginal CIs |
|---|---|---:|---:|---:|
| 2020→2021 | 2018→2018 | **100.00%** | 0.0 pp | 0.00% |
| 2024→2025 | 2022→2022 | **99.97%** | 0.0 pp | 0.00% |
| 2020→2024 | 2018→2022 | 0.51% | −4.4 pp | 11.96% |

The one nonidentical county in the 2024→2025 age-adjusted pair changes by only 0.2 points, consistent with a file-level revision rather than a new source wave. Averaging the two releases within each period is therefore numerically equivalent, to within 0.2 points maximum, to using one observation per source wave.

**Bounded non-reproduction.** The reported +1.6-point median could not be obtained from either plausible archive interpretation:

- treating the periods as release pairs 2020/2021 versus 2022/2023 compares source 2018 with source 2020 and yields a common-county age-adjusted median change of **+6.2 points**;
- treating the periods as source 2018 versus source 2022 using 2020/2021 versus 2024/2025 yields **−4.4 points**, but crosses the 50–75 to 45–75 definition change;
- the analogous crude 2018→2022 common-county median is **0.0 points**.

Because the conference abstract does not provide release IDs, code, spatial weights, or a complete harmonization rule, this is not a declaration that the published analysis is erroneous. It is an exact demonstration that the reported temporal contrast is not reproducible from the public description and archive under the two natural mappings.

**Conclusion classification.** The hotspot counts and SVI distribution cannot be fairly adjudicated without the authors' spatial specification. The paper nevertheless illustrates the candidate's central reporting problem: two-year labels can duplicate one source wave, and an apparently simple pre/post comparison can cross a measure-definition discontinuity.

## 8. Prespecified sensitivity and falsification suite

The controlled execution should freeze these tests before expanding to the full corpus.

| Check | Operational rule | Failure signal | Demonstrated here |
|---|---|---|---|
| Stable-measure restriction | Retain measures with unchanged wording, eligibility, and source cadence over the claimed interval | Result vanishes or reverses when rotating/redefined measures are removed | Nguyen high cholesterol loses 2/6 waves; other four outcomes survive |
| Release-vintage alignment | Replace publication/release labels with `measureid × BRFSS source year` | Nominal time count exceeds distinct source-wave count | Rahman 9→5; high cholesterol 6→4 |
| Exclude carry-forwards | Keep one copy per identical `measureid × geography × source year × value` block | Temporal coefficients, peaks, or persistence rely on duplicate rows | Rahman loses four annual observations; CRC two-year periods each collapse to one |
| Common geography/population | Restrict to units present in all compared releases and report coverage transitions separately | Apparent change tracks entry/exit or 500 Cities→PLACES expansion | Applied to 722/2,147/1,797 KS/MO tracts, 178 DC tracts, 3,126 counties |
| Definition harmonization | Require identical target population/question wording; otherwise split the series | Pre/post contrast crosses eligibility or question change | CRC 50–75→45–75 discontinuity |
| Interval-aware comparison | Report marginal-CI overlap and avoid independence-based difference claims without covariance | Many apparent unit-level changes are not separable from published uncertainty | Demonstrated in all three reproductions |
| Rank/set stability | Compute Spearman/Kendall rank stability and Jaccard/churn for policy sets under each restriction | Priority areas change materially or appear stable only because values were copied | Rahman copied pairs have ρ=1; distinct waves fall to 0.53–0.80 |
| Effective temporal n | Count distinct source waves, not file/release rows | Time-series degrees of freedom are overstated | Rahman effective wave count is at most five |
| Negative-control outcome | Include a same-study outcome with genuinely distinct source years | Audit condemns all repeated releases indiscriminately | Nguyen's four annually sourced outcomes pass the exact-copy test |
| Method-boundary check | Separate data-panel reproduction from model reproduction | Strong claims rest on unreported model details | R3 retained as bounded non-reproduction |

## 9. Direct competitor, active-work, and audience map

### 9.1 Nearest prior and direct-collision judgment

| Work/source | What it already establishes | What remains for C013 | Collision |
|---|---|---|---|
| [CDC PLACES FAQ](https://www.cdc.gov/places/faqs/index.html) | Local trend tracking is unsupported; fixed subcounty populations; county time absent; rotating measures and CI change documented | Quantify downstream use, exact copy structure, effective wave count, and conclusion changes | Governing source, not a direct audit |
| Kong & Zhang 2020, DOI `10.2105/AJPH.2020.305611` | General cautions for secondary use of small-area estimates | Release-level PLACES provenance and empirical downstream sensitivity | Methodological ancestor |
| Greenlund et al. 2022, DOI `10.5888/pcd19.210459` | PLACES methods and intended use | Corpus and temporal reliability audit | Agency/method ancestor |
| Lewis & Linzer 2005, DOI `10.1093/pan/mpi026` | General estimated-dependent-variable theory | PLACES-specific deterministic carry-forward and provenance rules | Theory ancestor; blocks broad novelty claims |
| Urban Institute 500 Cities report | Early warning that SAE is unsuitable for measuring change/evaluation | Modern multi-release empirical audit | Prior warning, not collision |
| Gupta et al. 2026, arXiv `2607.28655` | Active surrogate-model work for timelier small-area estimates | Reliability of interpreting existing releases longitudinally | Adjacent active work |

No work found combines all four of: a deduplicated temporal-use corpus, finalized measure/release crosswalk, exact carry-forward detection, and conclusion-level sensitivity across contrasting applications. Novelty is therefore credible but dated, not absolute.

### 9.2 Active-work pressure

The 2025–2026 cluster—Nguyen, Al Qady, Rahman, Akomaning, Rapaka, and the Rutgers dissertation—shows accelerating temporal use. This raises both value and collision risk. Execution should begin with a frozen protocol and monthly automated collision checks, but the present search does not justify delay.

### 9.3 Audience and decision map

| Audience | Decision improved | Deliverable needed |
|---|---|---|
| Applied researchers | Whether a PLACES repeated-release design has a valid temporal contrast | Machine-readable provenance crosswalk and admissibility checklist |
| Reviewers/editors | Whether “annual,” “trend,” “pre/post,” or “longitudinal” is supported | Effective-wave table, carry-forward report, definition/geography audit |
| Local public-health teams | Whether priority areas are persistent, newly emerging, or merely copied | Rank/set stability and interval-aware classification |
| CDC/data stewards | Where release metadata are insufficient for downstream interpretation | Suggested release-level source-year and comparability fields |
| Methods researchers | Which uncertainty/covariance gaps prevent valid inference | Formal estimand map and simulation targets, without claiming true trends |

## 10. Claim–evidence–limitation matrix

| Proposed claim | Evidence now | Limitation / wording boundary |
|---|---|---|
| Nominal annual PLACES releases need not be distinct temporal observations | Exact 100% equality in four mammography pairs; 100%/99.97% in CRC pairs | Demonstrated for rotating measures, not all measures |
| Release labels can overstate temporal effective sample size | Rahman 9 releases → 5 source waves; Nguyen HIGHCHOL 6→4 | Does not quantify all model-specific effective degrees of freedom |
| Provenance correction can materially alter published temporal interpretation | Peak/stability statements become repeated source waves; CRC result not reproducible under natural mappings | Does not invalidate cross-sectional findings or unexposed model code |
| The mechanism generalizes beyond mammography | High cholesterol and colorectal screening show deterministic carry-forward | Exact magnitude varies by measure, geography, and release |
| A provenance-aware audit can distinguish robust from fragile uses | Four Nguyen outcomes and two Mohebbi outcomes have distinct source years; rotating outcomes do not | Distinct source years still do not establish true local change |
| Marginal release CIs are insufficient for repeated-release inference | CDC publishes marginal CIs but no cross-release joint covariance | A future paper must avoid pretending CI overlap is a formal paired test |
| A direct corpus/crosswalk/reanalysis audit is not already published | Multi-channel search through 2026-09-21 found no collision | Search completeness is never provable; active work can emerge |
| The object can support a first paper | Public archive, codeable rules, ≥9 eligible works, three feasible reproductions | Full spatial/model replication depends on code/data disclosures and must be scoped tightly |

## 11. Kill-gate adjudication

| Kill gate | Finding | Decision |
|---|---|---|
| Direct audit already supplies the same corpus, crosswalk, and sensitivity analysis | None located | Survives |
| Temporal estimands cannot be coded reliably | 9/9 eligibility agreement; 8/9 use/fragility agreement across two coding passes | Survives with dual-human coding required in execution |
| Exact provenance cannot be reconstructed | Reconstructed for all releases 2016–2025 and all three reproductions | Survives |
| No substantive conclusion/decision classification changes | Annual wave count, peak/stability interpretation, slope, and pre/post reproducibility change | Survives |
| All selected studies disclose and handle the issue | None of the three reproduced studies fully reports carry-forward/source-vintage structure; Nguyen gives a general modeled-estimate limitation | Survives |
| Contribution is one anomalous mammography case | Same mechanism found in high cholesterol and colorectal screening; non-rotating outcomes provide negative controls | Survives |
| First paper is infeasible without private data or author contact | Core corpus, crosswalk, and archive diagnostics are public | Survives; model-level claims must remain bounded |

## 12. First-paper feasibility

### 12.1 Feasible paper

A first paper is feasible as a compact empirical methods/audit article with four linked outputs:

1. a PRISMA-style temporal-use corpus through a frozen search date;
2. a machine-readable `release × measure × source year × definition × geography/population × CI-method` crosswalk;
3. exact carry-forward, effective-wave, rank/set, and interval-aware diagnostics for the complete archive; and
4. three prespecified case studies chosen to span annual modeling, longitudinal association, and pre/post spatial classification.

The strongest paper is about **temporal admissibility and conclusion sensitivity**, not author-by-author criticism. Rahman supplies the clean deterministic annual pseudo-wave case; Nguyen supplies within-study positive and negative controls; the colorectal abstract supplies a high-stakes pre/post reproducibility case but should remain secondary unless fuller methods become public.

### 12.2 Scope controls

- Primary estimand: change in claim/classification after provenance-aware restriction, not truth error.
- Primary corpus: peer-reviewed articles; dissertations, preprints, and conference abstracts form an active-work appendix.
- Maximum case studies: three.
- No latent “true local prevalence” benchmark.
- No independent-error combination of release CIs.
- No named-paper error language without exact model/data reproduction.
- No ranking critique broader than CDC's stated prohibition and observed set instability.

### 12.3 Resource estimate

- Corpus completion and independent dual coding: 1–2 researcher-weeks.
- Crosswalk and automated archive tests: 1 researcher-week; current scripts establish feasibility.
- Three controlled reproductions and robustness checks: 2–4 researcher-weeks, depending on spatial/model code availability.
- Draft-ready evidence package after protocol freeze: approximately 4–7 researcher-weeks total.

The work is computationally light enough for ordinary hardware. The binding costs are provenance verification, full-text access, and careful interpretive adjudication rather than compute.

## 13. Controlled execution design to freeze next

Before inspecting additional case-study outcomes, freeze:

1. **Corpus cutoff and update rule:** search through 2026-09-21, with a documented one-time update immediately before submission.
2. **Independent dual coding:** two human coders, adjudicated disagreements, and a public codebook.
3. **Crosswalk schema:** release, Socrata ID, geography, measure ID, wording, eligibility population, BRFSS source year, carried-forward flag, geography vintage, population base, CI method, and comparability flag.
4. **Primary outcome:** whether the paper's principal temporal claim remains supported, narrows, changes classification, or becomes non-adjudicable.
5. **Case-study hierarchy:** Rahman primary; Nguyen contrasting control; third case selected between Hunyadi and Al Qady based on methods/code access before outcome inspection.
6. **Sensitivity order:** common geography → definition harmonization → source-year alignment → carry-forward removal → interval-aware result → rank/set stability.
7. **Stopping rules:** stop a case study if release mapping is ambiguous after public-source review; classify it as non-adjudicable rather than infer hidden choices.
8. **Reproducibility package:** raw-query manifests, cached hashes, scripts, environment lock, and machine-readable results.

## 14. Side findings preserved but not claimed as the paper

1. Nguyen et al. describe tract-level annual ACS estimates despite also noting that ACS 1-year estimates apply only above a large population threshold. Because tract socioeconomic data are normally drawn from 5-year ACS products, this may be a reporting inconsistency. It is outside C013's PLACES claim and should not be pursued without exact source-file verification.
2. The current CDC FAQ prohibits overall health ranking from PLACES modeled estimates. Hunyadi et al.'s composite burden quintiles may therefore raise a separate ranking-governance question. This is adjacent to, but not necessary for, the temporal paper.
3. The one 0.2-point county discrepancy between 2024 and 2025 colorectal files shows that “carried forward” can include a rare file revision. Execution should define exact-copy blocks empirically rather than assume literal identity from documentation alone.
4. Release-level point changes can be large even when very few unit-level marginal CIs are nonoverlapping. This is not a formal paired uncertainty result; it highlights the need for joint covariance or external resampling access.
5. The 2020 500 Cities→PLACES expansion can induce coverage artifacts even when a measure has a new source year. Common-geography restriction is therefore logically separate from carry-forward removal.

## 15. Reproducibility record

Scripts created for this prosecution:

- `o002_mammography_pair_audit.py`
- `o002_dc_temporal_audit.py`
- `o002_milwaukee_temporal_audit.py`
- `o002_crc_county_audit.py`
- `o002_openalex_scan.py`

Primary CDC dataset IDs used in the three reproductions:

- tract 2016–2025: `9z78-nsfp`, `vurf-k5wr`, `rja3-32tc`, `6vp6-wxuq`, `4ai3-zynv`, `373s-ayzu`, `nw2y-v4gm`, `em5e-5hvn`, `ai6z-tcin`, `cwsq-ngmh`;
- county 2020–2025 as needed: `dv4u-3x3q`, `pqpp-u99h`, `duw2-7jbt`, `h3ej-a9ec`, `fu4u-a9bh`, `swc5-untb`.

All numerical results in Sections 6–8 were recomputed against the live CDC API on 2026-09-21. The report preserves exact dataset identifiers because CDC catalog pages can be updated while Socrata IDs remain the reproducible query anchor.

## 16. Sources

1. CDC. [PLACES Frequently Asked Questions](https://www.cdc.gov/places/faqs/index.html).
2. CDC. [PLACES Methodology](https://www.cdc.gov/places/methodology/index.html).
3. CDC. [PLACES and 500 Cities Data Dictionary](https://data.cdc.gov/500-Cities-Places/PLACES-and-500-Cities-Data-Dictionary/m35w-spkz).
4. Kong AY, Zhang X. *The Use of Small Area Estimates in Place-Based Health Research*. DOI `10.2105/AJPH.2020.305611`.
5. Greenlund KJ et al. *PLACES: Local Data for Better Health*. DOI `10.5888/pcd19.210459`.
6. Candipan J, Riley AR, Easley JA. DOI `10.1080/10511482.2022.2076715`.
7. Hunyadi JV et al. DOI `10.1016/j.amepre.2024.08.022`.
8. Mohebbi F et al. [Full text](https://link.springer.com/article/10.1007/s11524-025-00976-x).
9. Nguyen QC et al. DOI `10.2196/74195`.
10. Al Qady A et al. DOI `10.14309/01.ajg.0001129756.58233.3d`.
11. Rahman MA et al. DOI `10.1001/jamanetworkopen.2026.30685`.
12. Akomaning E et al. DOI `10.1016/j.neuros.2026.100034`.
13. Rapaka R, Kaushik R. DOI `10.20944/preprints202602.0362.v1`.
14. Rutgers dissertation record. DOI `10.7282/t3-xd0f-8817`.
15. Gupta A et al. arXiv `2607.28655`.

## 17. Final disposition

The object clears novelty, mechanism, empirical consequence, feasibility, and audience gates. Its strongest contribution is not that CDC already warns against local trend use; it is that the release archive permits an exact, measure-specific accounting of temporal information and shows that published annual, pre/post, and association analyses can move into different admissibility classes after that accounting.

> **REGISTER NEXT AVAILABLE CANDIDATE AND ADVANCE TO CONTROLLED EXECUTION DESIGN**

