---
title: Research Group Radar
version: 0.7.0
last_updated: 2026-09-08
status: active
---

# Research Group Radar

This radar records groups and active-work signals relevant to **real-world ML reliability**, with the first deep pass emphasizing external reliability under measurement / observation-process shift.

It is competitive intelligence, not a claim that every listed group is pursuing the exact same project. Re-check official pages and recent preprints before a high-stakes novelty decision.

## Why group mapping matters

Research groups are not only competitors. They can be:

- sources of methods;
- software maintainers;
- dataset creators;
- sources of future-work statements;
- seminar/preprint signals;
- potential collaborators;
- PhD/postdoctoral destinations.

## Competition scale

- **Very High** — directly studies a central object or candidate-neighbor problem.
- **High** — strong methodological overlap and capacity to enter the space quickly.
- **Medium** — adjacent methods or application overlap.
- **Low** — useful background with limited direct competition.

---

# 1. University of Manchester — clinical prediction, missing data, adaptive observation

**Institution:** University of Manchester  
**Key researchers observed in this mapping pass:** Matthew Sperrin, Niels Peek, Glen Martin; Antonia Tsvetanova (2024 PhD); Vincent Jeanselme and collaborators on clinical presence shift.  
**Primary themes:** clinical prediction models, transportability/generalizability, missing predictors, adaptive observation, prediction under intervention, dynamic updating, EHR data.  
**Why relevant:** this is the most direct classical-statistical/methodological neighbor to C008.

### Evidence

- Sperrin’s current official profile explicitly lists improving generalisability/transportability, missing data when making predictions, adaptive observation (“what should be measured, and when”), and keeping models up-to-date across space/time [R055].
- Tsvetanova’s 2024 PhD addresses compatible missing-data handling across validation and deployment [R020].
- Jeanselme et al. 2025 formalize **clinical presence shift** and jointly model inter-observation time, missingness and survival prediction [R026].

### Questions they appear to be pursuing

- How should clinical prediction interact with causal structure?
- How should missing predictors be handled at deployment?
- What should be measured and when?
- How should models remain current across settings and time?
- How can clinical presence be explicitly modeled for transportability?

### Potential adjacent territory to monitor

- follow-up work to R026;
- external validation of clinical-presence-aware models across actual institutions;
- new PhD work on deployment-compatible missing data;
- explicit measurement-policy stress testing.

**Competition level:** **Very High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R020, R026, R055

---

# 2. Johns Hopkins — Suchi Saria / context-shift robustness

**Institution:** Johns Hopkins University / CERSI  
**Key researcher:** Suchi Saria; associated work by Adarsh Subbaswamy and collaborators.  
**Primary themes:** robustness under changing context of use, causality for shift stability, regulatory evaluation of clinical ML.  
**Why relevant:** this group has an explicitly named active project on assessing robustness of clinical ML models to changes in context of use.

### Evidence

- Johns Hopkins CERSI lists current research: **“Assessing the robustness of clinical machine learning models to changes in context of use,”** led by Suchi Saria [R053].
- Subbaswamy/Adams/Saria provide a framework for stress testing user-defined conditional shifts, including changes in clinical practice [R005].
- Earlier work frames dataset shift and causality as a health-AI deployment problem [R004].

### Potential adjacent territory to monitor

- new regulatory stress-test frameworks;
- context-of-use shift definitions;
- robustness test suites that may subsume C008’s proposed controlled stress tests.

**Competition level:** **Very High / High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R004, R005, R053

---

# 3. Charité CLAIM — missingness shift and ICU external validation

**Institution:** Charité – Universitätsmedizin Berlin  
**Group:** Charité Lab for Artificial Intelligence in Medicine (CLAIM)  
**Key adjacent researcher:** Patrick Rockenschaub and collaborators.  
**Primary themes relevant here:** clinical AI, external validation, missingness robustness, generalizability.  
**Why relevant:** direct theoretical and empirical work sits on both sides of the C008 seam.

### Evidence

- Rockenschaub et al. 2024 explicitly study **robust prediction under missingness shifts** [R024].
- The 2025 systematic review maps external validation of ICU ML and highlights how uncommon/limited it remains [R029].
- CLAIM is an active clinical-AI lab [R058].

### Potential adjacent territory to monitor

- peer-reviewed/follow-up version of R024;
- general missingness-shift benchmarks;
- ICU generalizability analyses that extend beyond AUROC;
- observation-process stress testing.

**Competition level:** **Very High / High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R024, R029, R058

---

# 4. UMC Utrecht / Julius Center — prediction-model methodology

**Institution:** University Medical Center Utrecht, Julius Center for Health Sciences and Primary Care  
**Key researchers:** Maarten van Smeden; broader prediction-model methodology community includes Karel Moons, Thomas Debray and collaborators.  
**Primary themes:** prediction-model development, validation, implementation, statistical/data-science methodology, missing data.  
**Why relevant:** likely source of rigorous nearest-neighbor work and evaluation standards.

### Evidence

- van Smeden’s official profile describes a focus on development, validation and implementation of prediction models [R056].
- Utrecht-linked literature contributes heavily to calibration, validation and missing-predictor methodology [R011, R016–R018].
- Current 2026 missing-data validation guidance shows the area remains active [R015].

### Potential adjacent territory to monitor

- external-validation guidance on missing predictors;
- model evaluation under measurement heterogeneity;
- missing-data pipelines for deployment.

**Competition level:** **High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R011, R015–R018, R056

---

# 5. University of Birmingham — prognosis and prediction-model methods

**Institution:** University of Birmingham  
**Key researcher:** Richard Riley and collaborators.  
**Primary themes:** prognosis, prediction models, external validation, sample-size methodology, evidence synthesis, clinical usefulness.  
**Why relevant:** evaluation rigor and external-validation methodology are central to C008.

### Evidence

- Riley’s official profile states he leads methodological/applied work on prognosis and prediction models [R057].
- Current BMJ guidance emphasizes multidimensional external validation and explicitly treats missing-data handling as an active research issue [R012].

### Potential adjacent territory to monitor

- external-validation design/sample-size work;
- subgroup evaluation;
- decision-curve/net-benefit methodology;
- missing predictors in validation.

**Competition level:** **High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R012, R057

---

# 6. MIT Healthy ML — robust and deployment-aware health ML

**Institution:** MIT  
**Group:** Healthy ML  
**Principal investigator:** Marzyeh Ghassemi  
**Primary themes:** robust, fair and privacy-aware ML for health; deployment readiness; subgroup robustness.  
**Why relevant:** broad high-capacity health-ML group operating on reliability under real-world variation.

### Evidence

- Healthy ML’s official page states that the group develops health ML that is robust, private and fair [R052].
- The group’s 2026 activity includes work arguing that common benchmarks do not measure deployment readiness [R052].
- “Change is Hard” benchmarks 20 algorithms across 12 datasets for subpopulation shift [R037].

### Potential adjacent territory to monitor

- benchmark redesign around deployment readiness;
- shortcuts/workflow features;
- subgroup shift under real-world deployment.

**Competition level:** **High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R037, R052

---

# 7. University of Michigan MLD3 — robust applied ML in healthcare

**Institution:** University of Michigan  
**Group:** Machine Learning for Data-Driven Decisions (MLD3)  
**Principal investigator:** Jenna Wiens  
**Primary themes:** machine learning + healthcare, time series, causal inference, real-world deployment, actionable clinical prediction.  
**Why relevant:** the group has a strong history of studying shortcuts, changing clinical processes and deployment-oriented health ML.

### Evidence

- Current official MLD3 page describes a portfolio at the AI/ML-healthcare interface with real-world health datasets [R054].

### Potential adjacent territory to monitor

- robustness to changes in clinical testing/workflow;
- missing-data shortcuts;
- deployed-model evaluations.

**Competition level:** **High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R054

---

# 8. LSHTM / UCL dynamic-updating cluster

**Institutions:** London School of Hygiene & Tropical Medicine; University College London; collaborators at Oxford/Nottingham  
**Key researchers:** Kamaryn Tanner, Ruth Keogh, Karla Diaz-Ordaz and collaborators.  
**Primary themes:** dynamic prediction-model updating, proactive/reactive updating pipelines, changing environments.  
**Why relevant:** directly constrains C007/OF-12 and provides mature lifecycle-methodology context.

### Evidence

- Dynamic survival-model updating in changing environments [R039].
- Explicit proactive versus reactive updating pipeline [R040].
- Broader updating literature mapped by recent review [R041].

### Potential adjacent territory to monitor

- triggers based on specific shift mechanisms;
- update choice after calibration/measurement failures;
- prospective validation of update policies.

**Competition level:** **High for updating; Medium for C008**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R039–R041

---

# 9. CMU StatML / Aaditya Ramdas — conformal, calibration and sequential inference

**Institution:** Carnegie Mellon University  
**Group:** StatML / Aaditya Ramdas group  
**Primary themes:** conformal prediction, post-hoc calibration, sequential/anytime-valid inference, distribution-free predictive inference.  
**Why relevant:** indicates high theoretical density and active talent around uncertainty/calibration under shift.

### Evidence

- Ramdas’s current official group/profile lists conformal prediction and calibration among central interests [R059].
- Foundational conformal under covariate shift [R034].
- Recent doubly robust prediction-set calibration under covariate shift [R035].

### Potential adjacent territory to monitor

- covariate-shift conformal advances;
- online monitoring and sequential reliability;
- calibration guarantees under distribution change.

**Competition level:** **Very High for OF-03; Medium for C008**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R034–R035, R059

---

# 10. Stanford Hazy Research — model evaluation under shift and maintenance

**Institution:** Stanford University  
**Group:** Hazy Research  
**Principal investigator:** Christopher Ré  
**Primary themes:** building, validating and maintaining ML systems; weak supervision; model evaluation under distribution shift.  
**Why relevant:** Mandoline provides a nearby target-performance-estimation paradigm.

### Evidence

- Mandoline estimates target performance under distribution shift using target covariates/shift slices [R032].
- Hazy’s official page emphasizes systems for building, validating and maintaining ML models [R060].

### Potential adjacent territory to monitor

- unlabeled target performance estimation;
- slice-based shift attribution;
- data-centric model maintenance.

**Competition level:** **Medium–High**  
**Last checked:** 2026-09-07  
**Evidence IDs:** R032, R060

---

# Cross-group synthesis

## Most crowded zones

1. Generic distribution-shift robustness.
2. Conformal/UQ under covariate shift.
3. Generic missingness-shift prediction algorithms.
4. Dynamic updating / post-deployment drift monitoring.
5. MIMIC/eICU external validation based primarily on standard performance metrics.

## Under-connected seam worth screening

The most promising interface is not owned by a single community:

> **clinical external-validation rigor + explicit observation-process shift + controlled robustness/stress testing + calibration/decision utility.**

The presence of multiple high-capacity neighboring groups means novelty must come from a specific evaluation object/design, not from terminology.

## Groups requiring the closest surveillance during C008 prosecution

Priority order:

1. Manchester prediction/missing-data/clinical-presence cluster.
2. Johns Hopkins Saria/Subbaswamy context-shift robustness.
3. Charité CLAIM/Rockenschaub missingness-shift and ICU validation.
4. Utrecht/Birmingham clinical prediction methodology.
5. MIT Healthy ML / Michigan MLD3 for broader deployment/shortcut work.

---


# Field radar 2 — survey data integration / nonprobability inference

These records supplement the original ML/clinical-reliability radar. They are competitive-intelligence signals, not claims about unpublished work.

| ID | Group / cluster | Current evidence | Relevance to active map | Competition implication |
|---|---|---|---|---|
| G11 | University of Waterloo — Changbao Wu / Pengfei Li and collaborators | DR NPS inference, mass imputation, pseudo empirical likelihood, undercoverage, 2026 nonignorable inference; Wu's 2026 JSM invited work [R080–R081, R103–R104] | Core probability-reference/NPS theory; highest relevance | **High surveillance** for propensity/nonignorability/EL; C009 should differentiate through measurement mechanism rather than generic weighting |
| G12 | Iowa State — Jae Kwang Kim | Mass imputation, regression data integration, calibration; Aug 2026 Bregman-projection seminar [R069, R086, R105] | Calibration/information-projection theory and integration | **High surveillance** if C009 becomes a calibration estimator rather than failure/sensitivity analysis |
| G13 | NC State — Shu Yang and collaborators | Test-and-pool/safe borrowing and broad data integration [R073] | Decision whether NPS should be borrowed at all | Moderate-high; overlap with C009 if measurement mismatch is framed only as comparability testing |
| G14 | University of Michigan ISR — Michael Elliott / Yajuan Si | 2024 workshop on P/NPS integration, representativeness, software [R106] | Foundational/operational integration and MRP/generalizability | Moderate; useful methodology ecosystem rather than direct C009 claim yet |
| G15 | U.S. Bureau of Labor Statistics OSMR — Savitsky/Gershunskaya/Beresovsky et al. | Unknown-overlap, thresholding and quasi-randomization papers [R077–R079, R102] | Official-statistics implementation and robustness to overlap | Moderate-high around pseudo-weighting/overlap; monitor new OSMR papers |
| G16 | U.S. Census Bureau statistical research | Explicit current probability/nonprobability integration subproject FY2025–FY2027 [R100–R101] | Confirms institutional demand and active government research | Moderate; unpublished internal work is a novelty uncertainty |
| G17 | University of Maryland — Partha Lahiri / Aditi Sen | 2026 measurement-error + representativeness paper [R085] | Closest high-level measurement×selection competitor | **Very high surveillance** for C009; full mathematical read required |
| G18 | University of Toronto / Institute for Work & Health — Victoria Landsman / Christoffer Dharma collaborations | 2025 selection+misclassification; 2026 multiple-reference surveys [R083, R088] | Very close applied-biostatistics integration with measurement/harmonization issues | **Very high surveillance**; direct boundary marker for C009 |
| G19 | NCHS/CDC RANDS methodology program | Public paired P/NP rounds and stated focus on measurement error/calibration [R092–R099] | Primary empirical substrate and possible methodological audience | Low “scooping” interpretation; high value as official data/methods program |
| G20 | Oregon State survey-statistics cluster — Xue/Lesser/Zhu collaborators | Copula-based pseudo-weighting with common ancillary variables [R090] | Sophisticated modeling of auxiliary distributions and inclusion mechanism | Moderate; C009 must show why different source measurement maps require more than richer X distribution modeling |

## Radar interpretation for C009

The closest groups are not all attacking the same problem. The principal risk clusters are:

1. **Maryland** — measurement error + representativeness;
2. **Toronto/IWH** — selection + misclassification / multiple references;
3. **Waterloo/Iowa State** — general NPS weighting/calibration theory.

C009 should be killed if full-paper review shows any of these groups already permit source-specific measurement error in the participation-adjustment covariates with the same identification target.

# Field radar 3 — C010 response-quality filtering / survey fraud interface

| ID | Group / cluster | Current evidence | Relevance to C010 | Competition implication |
|---|---|---|---|---|
| G21 | Pew Research Center Methods | 2020 bogus-respondent benchmark/data; 2024 good-faith NPS paper; Aug 2026 comparison of three screening approaches [R125, R129–R130, R133–R134] | Closest empirical/practitioner program showing screen tradeoffs and outcome reversals | **Very high surveillance**; broad applied C010 claims are unsafe |
| G22 | Social Research Centre (Australia) — Slamowicz/Pennay/Neiger/Phillips/Ward collaborators | Direct 2026 JSSAM paper excluding satisficers before recalculating weights in four NPPs [R127] | Closest direct empirical nearest neighbor | **Very high surveillance**; generic filter-before-weighting contribution is occupied |
| G23 | Stanford — Maya Mathur / selection-bias methodology | 2025 formal analysis of attention-check exclusion and covariate adjustment [R128] | Closest formal ancestor for filter-induced selection | **High surveillance** for theory claims |
| G24 | University of Maryland — Sen/Lahiri | 2026 method jointly addressing measurement error and representativeness in NPS [R126] | Strong measurement×selection competitor already tracked as G17 | **Very high surveillance** for generic joint-error methods |
| G25 | Gallup Methodology | 2024 opt-in-panel careless-response threshold experiments [R131] | Operational evidence on exclusion aggressiveness versus benchmark gains | Moderate-high; constrains threshold novelty |
| G26 | AAPOR / online-sample quality community | 2023 online-sample quality report and Aug 2026 fraud-detection programming [R139–R140] | Confirms active methodological/practitioner demand | Moderate-high active-work signal |

## Radar interpretation for C010

The closest competitive geometry is unfavorable for a broad first project. The Social Research Centre already owns the direct empirical filter-before-reweighting question; Pew and Gallup are actively evaluating real screening rules; Mathur occupies the formal exclusion-selection mechanism; and Maryland occupies generic NPS measurement-error × representativeness methodology.

A future C010 revival must therefore be visibly narrower: a new post-filter calibration identification/partial-identification result or estimand-targeted threshold decision under validated/explicit classifier uncertainty.

# Field radar 4 — repeated-survey selection drift / refreshment interface

| ID | Group / cluster | Current evidence | Relevance | Competition implication |
|---|---|---|---|---|
| G27 | SSRS / recurring hybrid survey methods — Jackson, Hasanbasri, McPhee, Peugh | 2022 recurring hybrid tracking-poll study directly tests whether NPS selection mechanisms change over waves and evaluates propensity+raking correction [R142] | Closest direct empirical prior art for broad OF-22 | **Very high for broad temporal-drift claim**; a future candidate must differ through anchor design, identification or decision theory |
| G28 | USC/UAS / refreshment-sample selection diagnostics — Kapteyn collaborators | 2026 working paper tests selection-on-observables using refreshment samples [R145], adjacent to a mature refreshment-sample literature | Strong methodological ancestor for learning about changing selection/attrition with later representative draws | **Moderate-high for intermittent-anchor formulations**; avoid repackaging refreshment diagnostics as NPS drift monitoring |

## Radar interpretation for OF-22 residue

R142 removes novelty from the claim that recurring NPS selection can drift and stale adjustment can fail. The only retained residue is an intermittent-anchor design in which probability/reference data are unavailable at every NPS wave. That residue remains **pre-candidate** until its temporal identification assumptions and data path are explicit.

# Field radar 5 — cross-field reconnaissance / OF-35

| ID | Group / cluster | Current evidence | Relevance | Competition implication |
|---|---|---|---|---|
| G29 | Duke Statistical Science — Jerome Reiter / synthetic-data collaborators | 2026 *Annual Review* on synthetic data; complex-survey synthesis work [R170, R173] | Central statistical synthetic-data inference/privacy program | **High competition** for OF-36; do not enter with generic inferential-utility claims |
| G30 | Ghent SYNDARA / Vansteelandt-linked synthetic-data work | 2026 reanalysis of 115 phase-3 oncology trials documents large inferential distortions for deep generators [R171] | Direct empirical inferential-validity program | **High active-work threat** for synthetic-data validity projects |
| G31 | ETH Zürich scoring-rules cluster — Waghmare / Ziegel and collaborators | 2026 scoring-rule review plus closely related calibration/evaluation work [R178] | Core probabilistic-evaluation theory | High ancestor surveillance if OF-35 drifts toward generic score construction |
| G32 | Nankai / Waterloo — Wu / Cook | Interval-censored prediction-accuracy estimators with explicit assessment/loss-to-follow-up process [R182] | Closest foundational prior art to OF-35 | **Very high surveillance**; full simulation/supplement review required before promotion |
| G33 | Erasmus MC / Utrecht / Fred Hutchinson — Yang / Rizopoulos / Erler / Newcomb | 2026 model-based versus IPCW AUC/Brier/EPCE under interval censoring and competing risks [R183] | Closest current applied-method comparison | **Very high surveillance** for misspecification/ranking claims |
| G34 | Taiwan interval-censoring evaluation — Tseng / Wang | EcoSta 2026 semiparametric interval-censored Brier framework with Murphy decomposition, sparse schedules and measurement error [R185] | Active unpublished/early-stage expansion of OF-35's nearest neighborhood | **Immediate active-work threat**; avoid metric-construction novelty |

## Radar interpretation for OF-35

OF-35 sits in a technically active but narrower neighborhood than synthetic-data inference. The main risk is not that interval-censored evaluation is empty—it is not—but that the proposed ranking-reliability question may already be implicit in simulations or active manuscripts from G32–G34.

Promotion therefore depends on a direct comparison of their evaluation targets with the proposed oracle-ranking/wrong-winner estimand and on explicit differentiation from right-censoring ranking-reversal/dependent-censoring work [R179–R180].

# Field radar 6 — adaptive paired comparisons and D024 neighboring leads

| ID | Group / cluster | Current evidence | Relevance | Competition implication |
|---|---|---|---|---|
| G35 | University of Warwick — Ian Hamilton / Nick Tawn | 2026 adaptive comparative-judgment Bradley–Terry estimation, non-ancillarity and scheduler-replay bootstrap [R195] | Closest adaptive-design group for OF-39 | **Very high surveillance.** Any OF-39 contribution must be more than their estimation-bias result or replay-bootstrap principle. |
| G36 | Carnegie Mellon — Weichen Wu / Nynke Niezink / Brian Junker | Bradley–Terry diagnostic framework for overdispersion, objects and subjects [R196] | Direct diagnostic-method source for OF-39 | **Very high surveillance.** Prosecution must verify assumptions/reference-law derivations and check follow-on work before claiming a gap. |
| G37 | Edinburgh / Loughborough / Southampton comparative-judgment cluster — Kinnear / Jones / Davies | 2025 meta-analysis of 101 CJ datasets and open empirical materials [R210] | Practice/data substrate for OF-39 | Medium competition; high empirical value. Verify adaptivity and scheduling metadata dataset by dataset. |
| G38 | Correlated/geospatial CV methods — Rabinowicz/Rosset and Hutchinson collaborators | General correlated-data CV and geospatial target-aware validation [R200–R201] | Principal ancestor cluster for OF-40 | High conceptual competition; OF-40 needs a source-availability deployment target, not generic spatial leakage. |
| G39 | UCLA econometrics — Filip Obradović and adjacent partial-identification work | Imperfect-reference-test sharp bounds [R204], alongside broader misclassification PI ancestors [R203] | Principal theory threat for OF-41 | High methodological barrier; a probabilistic-score result must add nontrivial sharp identification/inference. |

## Change log

### 0.7.0 — 2026-09-08

- Added field radar 6 for OF-39 and the principal D024 neighboring-method groups.
- Marked Warwick and CMU Bradley–Terry/adaptive-scheduling work as very-high-surveillance for the next prosecution.

### 0.6.0 — 2026-09-07

- Added G29–G34 for synthetic-data, scoring-rule and interval-censored prediction-evaluation surveillance.
- Identified Wu/Cook, Yang/Rizopoulos collaborators and Tseng/Wang as the closest OF-35 prior-art/active-work clusters.

### 0.5.0 — 2026-09-07

- Added G27–G28 for recurring-hybrid selection drift and refreshment-sample diagnostics.
- Recorded R142 as direct collapse evidence for broad OF-22 and refreshment methods as ancestors for the intermittent-anchor residue.

### 0.4.0 — 2026-09-07

- Added G21–G26 for the C010 response-quality filtering/fraud interface.
- Identified Pew Methods, Social Research Centre, Mathur/Stanford, Maryland, Gallup and AAPOR as the closest active clusters.
- Recorded unfavorable broad competitive geometry for C010.

### 0.3.0 — 2026-09-07

- Added G11–G20 for survey data integration/NPS inference.
- Marked Maryland and Toronto/IWH as closest C009 measurement×selection surveillance clusters.


### 0.2.0 — 2026-09-07

- Replaced seed community list with ten evidence-linked group records.
- Added current official-page evidence and active-work signals.
- Identified highest-adjacency groups for C008.
- Recorded crowded zones and the under-connected interface to screen.
