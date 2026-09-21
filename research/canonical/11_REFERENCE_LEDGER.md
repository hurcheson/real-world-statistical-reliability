---
title: Reference and Search Evidence Ledger
version: 0.22.0
last_updated: 2026-09-21
status: active
---

# Reference and Search Evidence Ledger

## Purpose

This ledger makes field mapping **traceable, falsifiable, and repeatable**. It records the sources that materially shaped the program's deep field-mapping passes, including evidence that weakens candidate ideas.

It is not a substitute for a manuscript-grade systematic review. Before a claim is used publicly, re-open the primary source and verify the final publication/version, methods, and exact result.

## Scope of mapping pass 1

**Program:** Real-World ML Reliability  
**Mapping focus:** external predictive reliability under **measurement / observation-process shift**, nested within dataset shift and clinical prediction-model transportability.  
**Initial domain:** clinical/EHR prediction, especially ICU data.  
**Search date:** 2026-09-07.  
**Status cutoff:** sources discoverable by the search date; 2025–2026 preprints are explicitly marked as provisional.

## Evidence-type codes

- **PP** — peer-reviewed primary research.
- **SR** — systematic/scoping review or methodological review.
- **GD** — guidance/reporting/risk-of-bias methodology.
- **PR** — preprint; findings and priority are provisional.
- **TH** — thesis/dissertation.
- **BK** — book/monograph.
- **DS** — dataset/data documentation.
- **SW** — software/repository.
- **GR** — official research-group/institutional page.

## Search procedure

This was a structured field-mapping search, **not a PRISMA systematic review**. The objective was to map intellectual communities, nearest prior art, active competition, datasets, software, and candidate seams quickly enough to decide what deserves formal prosecution.

Primary search surfaces included journal/publisher pages, PubMed/PMC, PMLR/NeurIPS/JMLR, arXiv/medRxiv, PhysioNet, university/lab pages, and GitHub repositories linked to papers/datasets. Preference was given to primary sources and official pages.

### Representative query families

The following query families were used or decomposed into close variants:

1. `clinical prediction dataset shift calibration external validation systematic review`
2. `distribution shift clinical prediction model transportability calibration`
3. `dataset shift machine learning health prediction review 2025`
4. `missing predictor external validation clinical prediction model`
5. `missingness shift prediction deployment`
6. `robust prediction under missingness shifts`
7. `informative observation EHR prediction measurement frequency`
8. `clinical presence shift prediction`
9. `observation process features domain shift MIMIC eICU`
10. `measurement heterogeneity external validation prediction model`
11. `calibration deterioration temporal dataset shift clinical prediction`
12. `conformal prediction covariate shift healthcare`
13. `subpopulation shift fairness transfer clinical machine learning`
14. `dynamic model updating clinical prediction drift`
15. `post deployment clinical AI missingness latency calibration drift`
16. `MIMIC-IV eICU external validation generalizability`
17. `eICU data interface missing data hospital units documentation`
18. `BlendedICU GitHub harmonized ICU dataset`
19. `clinical machine learning robustness context of use research group`
20. `clinical prediction model missing data PhD thesis deployment`

### Search limitations

- No Scopus/Web of Science export or formal dual-review screening was performed.
- Search-engine ranking and preprint availability can change.
- Some active-work signals may be invisible because they are unpublished.
- Group pages are competitive-intelligence signals, not proof of an unpublished project.
- Preprints should not be treated as established results until peer reviewed.
- A candidate that survives screening must receive a narrower, reproducible prosecution search with explicit inclusion/exclusion rules.

---

# A. Dataset shift, robustness, and transportability foundations

| ID | Citation / source | Type | What it establishes for this map | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R001 | Quiñonero-Candela J, Sugiyama M, Schwaighofer A, Lawrence ND, eds. *Dataset Shift in Machine Learning*. MIT Press. | BK | Canonical framing that train/test data-generating distributions can differ; connects multiple shift mechanisms. | Does not resolve clinical observation-process shift specifically. | https://mitpress.mit.edu/9780262170055/dataset-shift-in-machine-learning/ |
| R002 | Sugiyama M, Krauledat M, Müller K-R. Covariate Shift Adaptation by Importance Weighted Cross Validation. *JMLR*. 2007;8:985-1005. | PP | Classical importance-weighting response to covariate shift. | Requires assumptions that are often too narrow for workflow/measurement change. | https://www.jmlr.org/papers/v8/sugiyama07a.html |
| R003 | Moreno-Torres JG, Raeder T, Alaiz-Rodríguez R, Chawla NV, Herrera F. A unifying view on dataset shift in classification. *Pattern Recognition*. 2012;45(1):521-530. | PP | Useful taxonomy across covariate/prior/concept forms of shift. | Taxonomy alone does not identify the mechanism in EHR data. | https://doi.org/10.1016/j.patcog.2011.06.019 |
| R004 | Subbaswamy A, Saria S. From development to deployment: dataset shift, causality, and shift-stable models in health AI. *Biostatistics*. 2020;21(2):345-352. | PP | Makes context change and causal structure central to health-AI transportability. | Does not provide a complete external-validation protocol for observation-process shift. | https://doi.org/10.1093/biostatistics/kxz041 |
| R005 | Subbaswamy A, Adams R, Saria S. Evaluating Model Robustness and Stability to Dataset Shift. *AISTATS/PMLR*. 2021;130:2611-2619. | PP | Shows one can stress test user-specified conditional shifts, including clinical-practice changes, without collecting every target dataset. | Does not make EHR measurement-process decomposition trivial; shift set must be scientifically specified. | https://proceedings.mlr.press/v130/subbaswamy21a.html |
| R006 | Finlayson SG, Subbaswamy A, Singh K, et al. The Clinician and Dataset Shift in Artificial Intelligence. *NEJM*. 2021;385:283-286. | PP | Clinical framing of dataset shift as a deployment hazard. | Commentary does not quantify our proposed reliability object. | https://doi.org/10.1056/NEJMc2104626 |
| R007 | Nestor B, McDermott MBA, Boag W, et al. Feature Robustness in Non-stationary Health Records: Caveats to Deployable Model Performance in Common Clinical Machine Learning Tasks. *MLHC/PMLR*. 2019;106:381-405. | PP | Demonstrates temporal/EHR-system nonstationarity and that representation choices can affect robustness. | Does not isolate observation-process shift from all other temporal changes. | https://proceedings.mlr.press/v106/nestor19a.html |

# B. Reviews, standards, and clinical prediction methodology

| ID | Citation / source | Type | What it establishes for this map | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R008 | Silva et al. Strategies for detecting and mitigating dataset shift in machine learning for health predictions: A systematic review. *Journal of Biomedical Informatics*. 2025;170:104902. | SR | Recent map of health-prediction shift methods; reports heterogeneity and continuing need for standardized evaluation/external validation. | A review-level gap statement is not proof that C008 is novel. | https://doi.org/10.1016/j.jbi.2025.104902 |
| R009 | Guo et al. Systematic review of temporal dataset shift in clinical medicine. *Applied Clinical Informatics*. 2021;12(4):808-815. | SR | Temporal degradation often manifests in calibration and motivates updating/recalibration. | Temporal drift is broader than measurement-process shift. | https://doi.org/10.1055/s-0041-1735184 |
| R010 | Binuya et al. Methodological guidance for the evaluation and updating of clinical prediction models: a systematic review. *BMC Medical Research Methodology*. 2022;22:316. | SR | Clinical model evaluation should consider calibration, discrimination and clinical usefulness, and updating has a mature methodological literature. | Does not solve how to attribute external failure to the observation process. | https://doi.org/10.1186/s12874-022-01801-8 |
| R011 | Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW. Calibration: the Achilles heel of predictive analytics. *BMC Medicine*. 2019;17:230. | PP | Calibration is a distinct reliability property and can fail despite acceptable discrimination. | Not specific to dataset or observation-process shift. | https://doi.org/10.1186/s12916-019-1466-7 |
| R012 | Riley RD, et al. Evaluation of clinical prediction models (part of BMJ prediction-model guidance series). *BMJ*. 2024. | GD | External validation should evaluate calibration, discrimination, subgroups, and clinical utility; missing predictors in external validation remain an active methodological issue. | Guidance does not itself define a solved framework for source/target measurement-process shift. | https://doi.org/10.1136/bmj-2023-074820 |
| R013 | Collins GS, et al. TRIPOD+AI statement. *BMJ*. 2024. | GD | Current reporting expectations for prediction models using regression/ML. | Reporting guidance is not a robustness method. | https://doi.org/10.1136/bmj-2023-078378 |
| R014 | Moons KGM, et al. PROBAST+AI. *BMJ*. 2025. | GD | Current risk-of-bias/applicability framework for prediction-model studies. | Does not independently establish C008 novelty. | https://doi.org/10.1136/bmj-2024-082505 |
| R015 | Practical guidance for internal validation of prediction models in the presence of missing data. *Journal of Clinical Epidemiology*. 2026;192:112159. | GD | Shows missing-data validation methodology remains actively developed; provides an internal-validation workflow. | It is principally about **internal** validation and does not close the external observation-process-shift seam. | https://doi.org/10.1016/j.jclinepi.2026.112159 |

# C. Measurement heterogeneity and missing predictors in validation/deployment

| ID | Citation / source | Type | What it establishes for this map | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R016 | Luijken K, Wynants L, van Smeden M, Van Calster B, Steyerberg EW. Impact of predictor measurement heterogeneity across settings on the performance of prediction models: a measurement error perspective. *Statistics in Medicine*. 2019;38(18):3444-3459. | PP | Predictor measurement procedures can differ across settings and induce external miscalibration/performance loss. | Measurement error/heterogeneity is not identical to missingness or measurement frequency. | https://doi.org/10.1002/sim.8183 |
| R017 | Luijken K, et al. Changing predictor measurement procedures affected the performance of prediction models in clinical examples. *Journal of Clinical Epidemiology*. 2020;119:7-18. | PP | Empirical evidence that changing measurement procedures can materially change calibration intercept/slope. | Does not study EHR observation intensity as a predictive shortcut. | https://doi.org/10.1016/j.jclinepi.2019.11.001 |
| R018 | Hoogland J, et al. Handling missing predictor values when validating and applying a prediction model to new patients. *Statistics in Medicine*. 2020;39:3591-3607. | PP | Missing-data handling in validation must be compatible with model application/deployment. | Does not address all forms of between-site observation-process shift. | https://doi.org/10.1002/sim.8682 |
| R019 | Sperrin M, Martin GP, et al. Missing data should be handled differently for prediction than for description or causal explanation. *Journal of Clinical Epidemiology*. 2020;125:183-187. | PP | Prediction has deployment-specific missing-data requirements; standard inferential missing-data recipes need not be appropriate. | Does not provide a full shift benchmark. | https://doi.org/10.1016/j.jclinepi.2020.03.028 |
| R020 | Tsvetanova A. *Handling missing data when validating and deploying clinical prediction models in health settings: an investigation of compatible methods*. PhD thesis, University of Manchester. Awarded 2024. | TH | Direct active-methods lineage: validation should mimic deployment missing-data handling; incompatible pipelines can bias estimated performance. | Does not by itself settle observation-process shift in multi-site ML models. | https://research.manchester.ac.uk/en/studentTheses/handling-missing-data-when-validating-and-deploying-clinical-pred/ |

# D. Informative presence, informative observation, and missingness shift

| ID | Citation / source | Type | What it establishes for this map | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R021 | Agniel D, Kohane IS, Weber GM. Biases in electronic health record data due to processes within the healthcare system: retrospective observational study. *BMJ*. 2018;361:k1479. | PP | Presence/timing of tests can encode healthcare process and be predictive independently of values. | Predictiveness of workflow signals does not imply they are transportable. | https://doi.org/10.1136/bmj.k1479 |
| R022 | Groenwold RHH. Informative missingness in electronic health record systems: the curse of knowing. *Diagnostic and Prognostic Research*. 2020;4:8. | PP | Informative missingness can improve prediction in one environment while depending on a transportable missingness mechanism. | Does not quantify multi-site calibration/utility loss. | https://doi.org/10.1186/s41512-020-00077-0 |
| R023 | Sisk R, et al. Informative presence and observation in routine health data: a review of approaches to account for the patient-clinician interaction. *JAMIA*. 2021;28(1):155-166. | SR | Maps informative presence/observation terminology and methods around healthcare contact/measurement. | Focus is broader than predictive transportability. | https://doi.org/10.1093/jamia/ocaa242 |
| R024 | Rockenschaub P, Xian Z, Zamanian A, et al. Robust prediction under missingness shifts. arXiv:2406.16484. | PR | Provides theory/experiments showing ignorable versus non-ignorable missingness shifts have different implications for the Bayes predictor and robustness. | Does not close the clinical external-validation/calibration/utility problem; preprint status. | https://arxiv.org/abs/2406.16484 |
| R025 | Lee J, Kang M, Kim D. MIRRAMS: Learning Robust Tabular Models under Unseen Missingness Shifts. arXiv:2507.08280. | PR | Shows generic algorithmic robustness to unseen missingness shifts is an active, crowded methods frontier. | Benchmark tabular robustness is not equivalent to clinical transportability. | https://arxiv.org/abs/2507.08280 |
| R026 | Jeanselme V, Martin G, Sperrin M, Peek N, Tom B, Barrett J. Prediction of Survival Outcomes under Clinical Presence Shift: A Joint Neural Network Architecture. arXiv:2508.05472. | PR | Formalizes **clinical presence shift** and jointly models observation timing, missingness, and outcome for transportability. | Single-method/preprint evidence does not settle all evaluation questions. | https://arxiv.org/abs/2508.05472 |
| R027 | Yamamoto R, Wu F, Sprehe LK, Abeer A, Celi LA, Tohyama T. Observation-process features are associated with larger domain shift in sepsis mortality prediction: a cross-database evaluation using MIMIC-IV and eICU-CRD. medRxiv. 2026. | PR | **Closest direct competitor**: measurement counts improve internal discrimination but are associated with worse cross-database calibration/transportability; calibration slope deteriorates strongly with richer specifications. | One sepsis task/two databases does not automatically constitute a general external-validation stress-testing framework; preprint status. | https://doi.org/10.64898/2026.04.05.26350209 |
| R028 | Yang C-H, Salvatore M, Lu H, et al. Who seeks care, and what gets measured? Understanding the distinct mechanisms behind visit and observation processes in multi-center electronic health records. medRxiv. 2026. | PR | Separates visit and conditional measurement processes across three large EHR-linked cohorts; shows their drivers differ across cohorts and biomarkers. | Primarily characterizes the recording process rather than predictive-model reliability; preprint status. | https://doi.org/10.64898/2026.08.12.26360236 |

# E. External ICU validation and post-deployment evidence

| ID | Citation / source | Type | What it establishes for this map | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R029 | Rockenschaub P, et al. External validation of machine learning models in intensive care: a systematic review. *BMC Medical Informatics and Decision Making*. 2025;25:5. | SR | External validation is uncommon in ICU ML; MIMIC/eICU dominate, and evaluations often over-rely on AUROC. | Does not prove that another MIMIC→eICU validation paper is useful; rather, it warns against a shallow one. | https://doi.org/10.1186/s12911-024-02830-7 |
| R030 | Kopanitsa G. Validation is not enough: Longitudinal evidence of post-deployment fragility in clinical AI systems. *PLOS Digital Health*. 2026;5(7):e0001534. | PP | In four deployed systems, calibration drift and workflow telemetry such as missingness/latency were important post-deployment signals; label-independent monitoring can detect fragility early. | Makes a generic “monitor missingness after deployment” project less novel; does not replace pre-deployment attribution/stress testing. | https://doi.org/10.1371/journal.pdig.0001534 |
| R031 | Patel K, Beedala P. Calibration Drift Under Cross-Institutional Deployment: An External Validation Framework for ICU Mortality Prediction Across MIMIC-IV and eICU. medRxiv. 2026. | PR | Signals active competition around cross-institutional calibration drift using MIMIC/eICU; includes calibration, recalibration, decision curves and subgroup analyses. | Does not specifically isolate observation-process shift; preprint status. | https://doi.org/10.64898/2026.05.03.26352335 |

# F. Target-performance estimation, uncertainty, subgroup shift, and updating

| ID | Citation / source | Type | What it establishes for this map | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R032 | Chen M, Goel K, Sohoni N, Poms F, Fatahalian K, Ré C. Mandoline: Model Evaluation under Distribution Shift. *ICML/PMLR*. 2021;139:1617-1629. | PP | Target performance can be estimated from unlabeled target data using user-specified shift slices. | Does not uniquely solve observation-process shift or delayed/selective labels. | https://proceedings.mlr.press/v139/chen21a.html |
| R033 | Ulichney & Coston. Beyond Training Distribution: Estimating Target Risk under Joint Covariate Shift and Selective Labels. arXiv:2606.14506. 2026. | PR | Current frontier on target-risk estimation when both distribution and label-observation mechanisms differ. | Higher theory/identification burden; not a simple first project. | https://arxiv.org/abs/2606.14506 |
| R034 | Tibshirani RJ, Barber RF, Candès EJ, Ramdas A. Conformal Prediction Under Covariate Shift. *NeurIPS*. 2019. | PP | Foundational weighted conformal approach under covariate shift. | Coverage under general workflow/measurement-process shift is not automatically guaranteed. | https://papers.nips.cc/paper/2019/hash/8fb21ee7a2207526da55a679f0332de2-Abstract.html |
| R035 | Yang Y, Kuchibhotla AK, Tchetgen Tchetgen EJ. Doubly robust calibration of prediction sets under covariate shift. *JRSSB*. 2024. | PP | Conformal/prediction-set calibration under shift is theoretically active and mature. | Does not eliminate healthcare-specific UQ questions, but makes generic OF-03 less attractive. | https://doi.org/10.1093/jrsssb/qkae009 |
| R036 | Tuwani R, Beam AL. Safe and reliable transport of clinical prediction models using conformal prediction under covariate shift. medRxiv. 2023/2024. | PR | Direct health-domain application of conformal transport under covariate shift. | Restricted shift assumptions; not observation-process-specific. | https://doi.org/10.1101/2023.12.13.23299899 |
| R037 | Yang Y, et al. Change is Hard: A Closer Look at Subpopulation Shift. *ICML*. 2023. | PP | Large benchmark of algorithms under subpopulation shifts, including health datasets; indicates crowding. | Subpopulation shift is not identical to workflow measurement shift. | https://proceedings.mlr.press/v202/yang23s.html |
| R038 | Schrouff J, et al. Diagnosing failures of fairness transfer across distribution shift in real-world medical settings. *NeurIPS*. 2022. | PP | Fairness itself may fail to transport; causal shift structure matters. | Does not settle subgroup × observation-process shift. | https://proceedings.neurips.cc/paper_files/paper/2022/hash/7a969c30dc7e74d4e891c8ffb217cf79-Abstract-Conference.html |
| R039 | Tanner KT, Keogh RH, Coupland CAC, Hippisley-Cox J, Diaz-Ordaz K. Dynamic updating of clinical survival prediction models in a changing environment. *Diagnostic and Prognostic Research*. 2023;7:24. | PP | Dynamic updating is already an established methodological area. | Does not identify the correct update action for a diagnosed measurement-process failure. | https://doi.org/10.1186/s41512-023-00163-z |
| R040 | Tanner KT, Diaz-Ordaz K, Keogh RH. Implementation of a dynamic model updating pipeline provides a systematic process for maintaining performance of prediction models. *Journal of Clinical Epidemiology*. 2024;175:111531. | PP | Defines proactive/reactive updating pipeline ideas and operationalizes repeated updating. | Makes generic C007 less novel; does not couple update choice to observation-process decomposition. | https://doi.org/10.1016/j.jclinepi.2024.111531 |
| R041 | Meijerink et al. Scoping review of updating AI-based clinical prediction models. *Journal of Clinical Epidemiology*. 2025;178:111636. | SR | Updating literature is active and concentrated in some model/application classes. | Does not make every updating question solved. | https://doi.org/10.1016/j.jclinepi.2024.111636 |

# G. Datasets and reproducible substrates

| ID | Dataset / source | Type | Why it matters | Important caveat | Stable locator |
|---|---|---:|---|---|---|
| R042 | MIMIC-IV v3.1, PhysioNet. | DS | Rich single-center longitudinal ICU/ED/hospital data; mature code ecosystem; useful source environment. | Single health-system provenance limits natural site heterogeneity. | https://physionet.org/content/mimiciv/3.1/ |
| R043 | eICU Collaborative Research Database v2.0, PhysioNet. | DS | >200k ICU admissions across many US units/hospitals; especially useful for site/unit variation. Documentation notes that availability of data types depends on local interfaces, creating structural variation in captured data. | Full access requires credentialing/DUA; hospital-level process heterogeneity can confound physiology and workflow. | https://physionet.org/content/eicu-crd/2.0/ |
| R044 | eICU-CRD Demo. | DS | Small open subset suitable for schema/SQL prototyping before credentialed full-data work. | Too small for substantive reliability conclusions. | https://physionet.org/content/eicu-crd-demo/ |
| R045 | HiRID v1.1.1, PhysioNet. | DS | High-resolution ICU data from Bern; potential third environment. | Different schema/care setting requires careful variable alignment and provenance preservation. | https://physionet.org/content/hirid/1.1.1/ |
| R046 | AmsterdamUMCdb v1.5.0. | DS | European ICU/HDU data; OMOP representation; possible additional external environment. | Different era/system/case mix can induce multiple simultaneous shifts. | https://amsterdammedicaldatascience.nl/amsterdamumcdb/ |
| R047 | Faltys M, et al. Introducing the BlendedICU dataset. *Journal of Biomedical Informatics*. 2023;146:104502. | PP/DS | Harmonizes AmsterdamUMCdb, eICU, HiRID and MIMIC-IV; built for generalizability studies. | **Inference:** aggressive harmonization may erase some provenance/measurement-process differences that are themselves the object of study; retain source metadata/raw definitions. | https://doi.org/10.1016/j.jbi.2023.104502 |

# H. Software and reproducibility resources

| ID | Resource | Type | Use | Stable locator |
|---|---|---:|---|---|
| R048 | BlendedICU repository. | SW | OMOP standardization/harmonization pipeline for four ICU databases. | https://github.com/USM-CHU-FGuyon/BlendedICU |
| R049 | eICU Code repository. | SW | Community SQL/concepts and reproducible extraction patterns for eICU. | https://github.com/mit-lcp/eicu-code |
| R050 | CDSS-post-deployment-validation repository. | SW | Code/aggregate data supporting Kopanitsa 2026 monitoring analyses. | https://github.com/ITMO-NCCR/CDSS-post-deployment-validation |
| R051 | Mandoline repository/paper code ecosystem. | SW | Reference implementation for target-performance estimation under distribution shift. | https://github.com/stanford-futuredata/mandoline |

# I. Research-group and active-work radar evidence

| ID | Group / institutional source | Type | Relevance | Stable locator |
|---|---|---:|---|---|
| R052 | Healthy ML, MIT — Marzyeh Ghassemi. | GR | Robust/fair/deployment-oriented health ML; active 2026 work questions benchmark deployment readiness. | https://www.healthyml.org/ |
| R053 | Johns Hopkins CERSI — Suchi Saria project: “Assessing the robustness of clinical machine learning models to changes in context of use.” | GR | Directly adjacent robustness/stress-testing program with regulatory framing. | https://publichealth.jhu.edu/center-of-excellence-in-regulatory-science-and-innovation/research |
| R054 | MLD3, University of Michigan — Jenna Wiens. | GR | Applied ML/health group with real-world deployment, incomplete-data and robustness lineage. | https://wiens-group.engin.umich.edu/ |
| R055 | University of Manchester — Matthew Sperrin research profile. | GR | **Very high adjacency:** prediction generalisability/transportability, missing data, adaptive observation, dynamic updating; routine EHR focus. | https://research.manchester.ac.uk/en/persons/matthew.sperrin |
| R056 | UMC Utrecht/Julius Center — Maarten van Smeden profile. | GR | Prediction-model development, validation, implementation and methodology; close clinical-statistics community. | https://researchinformation.umcutrecht.nl/en/persons/maarten-van-smeden/ |
| R057 | University of Birmingham — Richard Riley. | GR | Major prognosis/prediction-model methodology group; external validation, sample size, clinical usefulness. | https://www.birmingham.ac.uk/staff/profiles/applied-health/riley-richard |
| R058 | Charité Lab for Artificial Intelligence in Medicine (CLAIM). | GR | Current clinical-AI methods/deployment group; Patrick Rockenschaub’s work is directly adjacent to missingness shift and ICU external validation. | https://claim.charite.de/en/ |
| R059 | CMU — Aaditya Ramdas / StatML. | GR | Conformal prediction, calibration, sequential and distribution-free inference; indicates high theoretical density around OF-03. | https://www.stat.cmu.edu/~aramdas/group.html |
| R060 | Stanford Hazy Research — Christopher Ré. | GR | Model validation/maintenance under weak supervision and distribution shift; Mandoline lineage. | https://hazyresearch.stanford.edu/ |

---

# Evidence synthesis encoded by this ledger

## Claims supported strongly enough for field mapping

1. **External reliability is multi-dimensional.** Calibration, discrimination and decision utility must be separated; acceptable AUROC does not imply trustworthy risk probabilities. [R010–R012]
2. **The measurement process is part of the predictive data-generating process.** Test ordering, observation frequency and EHR presence can contain predictive information created by care processes. [R021–R023]
3. **Those processes can change across environments.** Measurement procedures, missingness mechanisms, clinical presence and infrastructure differ across sites/time. [R016–R020, R024–R028, R043]
4. **This can create a transportability trade-off.** Current direct evidence shows observation-process features can improve internal discrimination while worsening external calibration. [R027]
5. **Generic versions of several candidate families are crowded.** Missingness-shift algorithms [R024–R026], conformal/UQ under shift [R034–R036], generic updating [R039–R041], and generic post-deployment monitoring [R030] all have active mature/fast-moving literatures.
6. **A remaining candidate seam is evaluation/attribution, not simply another predictor.** The potentially useful interface is a pre-deployment external-validation/stress-testing framework that distinguishes patient/case-mix shift from measurement/observation-process shift and evaluates calibration plus clinical utility. This is a **research inference from the map**, not an established gap.

## Evidence that could kill the current lead

- R027 is already very close: if its scope or follow-on work generalizes across tasks, sites and clinical utility in the way contemplated for C008, differentiation may be too small.
- R005 already provides a general conditional-shift stress-testing framework; C008 cannot merely rename user-defined “clinical practice shift.”
- R016–R020 show clinical-statistical methodology already treats measurement heterogeneity and deployment-compatible missing-data handling seriously.
- R026 explicitly formalizes “clinical presence shift,” so terminology or conceptual framing alone is not novel.
- R030 makes a generic operational-monitoring contribution much less attractive.

## Reproducibility rule for the next pass

If C008 enters formal prosecution, create a **nearest-neighbor matrix** with at minimum R005, R016–R020, R024, R026–R030. For every source record:

- exact population/task;
- source/target environments;
- shift mechanism;
- whether shift is observed, simulated, or intervened;
- estimand/evaluation target;
- primary reliability metrics;
- model classes;
- labels required in target;
- clinical utility assessed?;
- subgroup assessment?;
- code/data availability;
- explicit limitations/future work;
- exact claim C008 would make that the source cannot.

Do not promote C008 beyond **SCREENING** until that matrix is complete.


---

# Mapping pass 2 — survey data integration / nonprobability inference

## Scope

**Mapping focus:** finite-population inference combining probability and nonprobability samples, with attention to selection assumptions, robustness, measurement compatibility, public data and small-team feasibility.  
**Search date:** 2026-09-07.  
**Current lead generated:** C009 — cross-source measurement mismatch in nonprobability-sample adjustment.  
**Status cutoff:** sources discoverable by 2026-09-07; current 2025–2026 papers/preprints and agency programs were treated as active competition.

## Search procedure — pass 2

Searches deliberately covered both the field's own terminology and neighboring measurement-error terminology. Primary/official pages were preferred over secondary summaries.

Representative query families included:

1. `nonprobability sample probability reference survey data integration review`
2. `survey data integration calibration propensity mass imputation doubly robust`
3. `nonprobability samples official statistics state of the art 2025`
4. `nonignorable nonprobability survey sample sensitivity`
5. `multiple reference surveys nonprobability selection bias`
6. `probability nonprobability distribution quantile estimation 2026`
7. `measurement error representativeness nonprobability survey`
8. `measurement equivalence probability nonprobability online panels`
9. `nonprobability probability integration measurement error auxiliary covariates`
10. `error-prone covariates inverse probability weighting`
11. `selection misclassification bias nonprobability probability reference`
12. `shared covariates measured without error nonprobability sample`
13. `identically measured auxiliary variables nonprobability sample sensitivity`
14. `survey harmonization nonprobability probability auxiliary variables`
15. `RANDS probability nonprobability public use round 10`
16. `RANDS nonprobability balancing weights technical documentation`
17. `Census integration probability nonprobability samples current project`
18. `BLS quasi-randomization nonprobability samples`
19. `research group nonprobability survey data integration Waterloo Iowa Michigan`
20. `small area estimation nonprobability samples review 2026`

### Important search limitation for C009

The v0.3 search did **not** surface a direct modern paper whose primary estimand is finite-population probability/nonprobability integration when the *shared participation-adjustment covariates themselves* follow source-specific measurement-error mechanisms. The v0.4 prosecution expanded through older calibration, differential-propensity measurement error, two-sample EIV and finite-population data-integration ancestors [R113–R119]. That search **did find prior art strong enough to invalidate the broad C009 novelty framing**: erroneous/non-identical calibration controls [R113], differential propensity-covariate measurement error [R114], and finite-population integration with measurement error [R115] are established.

The remaining candidate is narrower: a P/NPS-specific decomposition of wrong-scale benchmark bias versus residual proxy-selection bias, plus identification/sensitivity by information regime. Targeted searches did not surface that exact object. This is **not evidence of absence**; it justifies continued PROSECUTION, not a novelty claim.

# J. Field foundations and major reviews — survey/nonprobability integration

| ID | Citation / source | Type | What it establishes for this map | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R061 | Rao JNK, Lohr SL. Trends and directions in sample survey theory and methods. *Survey Methodology*. 2025;51(1):81–113. | SR | Current field-level review; identifies data integration, NPS, new/admin sources and SAE as active survey-research frontiers. | Does not identify a specific small-team project. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2025001/article/00014-eng.htm |
| R062 | Pfeffermann D, Sverchkov M. Use of nonprobability samples for official statistics, state of the art. *Survey Methodology*. 2025;51(1):169–196. | SR | Current official-statistics review: NPS are cheaper/timelier but selection bias/nonrepresentativeness is central; distinguishes integration and NPS-only inference. | Does not make selection assumptions identifiable. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2025001/article/00008-eng.htm |
| R063 | Wu C. Statistical inference with non-probability survey samples. *Survey Methodology*. 2022;48(2):283–311. | SR/GD | Rigorous review of inferential frameworks, assumptions, IPW/calibration/DR and sensitivity; emphasizes rich probability-sample auxiliaries. | Does not solve source-specific measurement mismatch in auxiliaries. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2022002/article/00002-eng.htm |
| R064 | Yang S, Kim JK. Statistical data integration in survey sampling: a review. *Japanese Journal of Statistics and Data Science*. 2020;3:625–650. | SR | Canonical integration setup and method families: calibration, IPW, mass imputation, DR; explicitly formulates common X across sources. | Treats the shared-covariate representation largely as given. | https://doi.org/10.1007/s42081-020-00093-w |
| R065 | Salvatore C. Inference with non-probability samples and survey data integration: a science mapping study. *METRON*. 2023;81:83–107. | SR | Maps 1,023 documents; identifies selection bias, measurement differences across source/mode, and data quality as distinct challenges. | Bibliometric/conceptual mapping does not provide a correction for cross-source measurement mismatch. | https://doi.org/10.1007/s40300-023-00243-6 |
| R066 | Cornesse C, Blom AG, Dutwin D, et al. A Review of Conceptual Approaches and Empirical Evidence on Probability and Nonprobability Sample Survey Research. *JSSAM*. 2020;8(1):4–36. | SR | Establishes theoretical/model dependence of NPS inference and extensive empirical quality evidence. | Does not isolate adjustment-covariate measurement error. | https://doi.org/10.1093/jssam/smz041 |
| R067 | Elliott MR, Valliant R. Inference for Nonprobability Samples. *Statistical Science*. 2017;32(2):249–264. | SR | Foundational modern pseudo-design/weighting framing for NPS inference. | Does not settle newer multi-source measurement-error problems. | https://doi.org/10.1214/16-STS598 |

# K. Core and active methods

| ID | Citation / source | Type | What it establishes | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R068 | Chen Y, Li P, Wu C. Doubly Robust Inference With Nonprobability Survey Samples. *JASA*. 2020;115(532):2011–2021. | PP | Major finite-population framework using probability-sample auxiliaries; propensity and doubly robust estimators. | DR does not automatically protect against incompatible measurement of shared X. | https://doi.org/10.1080/01621459.2019.1677241 |
| R069 | Kim JK, Park S, Chen Y, Wu C. Combining Non-Probability and Probability Survey Samples Through Mass Imputation. *JRSS A*. 2021;184(3):941–963. | PP | Establishes mass-imputation integration under transportability; highlights importance of common auxiliaries and mode interpretation. | Does not model different measurement mechanisms for the same adjustment X across sources. | https://doi.org/10.1111/rssa.12696 |
| R070 | Chen Y, Li P, Rao JNK, Wu C. Pseudo empirical likelihood inference for nonprobability survey samples. *Canadian Journal of Statistics*. 2022;50(4):1166–1185. | PP | Empirical-likelihood inference/interval machinery for NPS. | Does not resolve source-specific covariate measurement mismatch. | https://doi.org/10.1002/cjs.11708 |
| R071 | Chen Y, Li P, Wu C. Dealing with undercoverage for non-probability survey samples. *Survey Methodology*. 2023;49:497–515. | PP | Distinguishes stochastic/deterministic undercoverage and positivity failures; provides bias-mitigation strategies. | Undercoverage is not the same as measurement mismatch. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2023002/article/00005-eng.htm |
| R072 | Chen S, Haziza D. General purpose multiply robust data integration procedures for handling nonprobability samples. *Scandinavian Journal of Statistics*. 2023;50(2):697–724. | PP | Multiple propensity/outcome models; general parameters; robustness to model misspecification. | Robustness is within the modeled variables, not necessarily to cross-source measurement incompatibility. | https://doi.org/10.1111/sjos.12605 |
| R073 | Gao C, Yang S. Pretest estimation in combining probability and non-probability samples. *Electronic Journal of Statistics*. 2023;17:1492–1546. | PP | Test-and-pool/safe borrowing: use NPS when compatible, retain probability sample otherwise. | Comparability pretest does not specifically identify measurement mismatch in adjustment X. | https://doi.org/10.1214/23-EJS2137 |
| R074 | Seaman SR, Nyberg T, Presanis AM. Doubly robust integration of nonprobability and probability survey data. arXiv:2508.05859. 2025. | PR | Current work on efficient combination of DR NPS estimates with probability-only estimates. | Preprint; not a measurement-mismatch framework. | https://arxiv.org/abs/2508.05859 |
| R075 | Seaman SR. Debiased machine learning for integrating probability and nonprobability survey data. arXiv:2508.08948. 2025. | PR | Active semiparametric/ML frontier; shows estimator-development space is crowded. | Preprint; does not establish C009. | https://arxiv.org/abs/2508.08948 |
| R076 | Kott PS, Ridenhour J. Calibration weighting with a blended (probability and nonprobability) sample: Mean and variance estimation when errors can come from both samples. RTI Press Methods Report. 2024. | PP/GD | Statistically defensible blended calibration and variance estimation; participation modeled by variables known for both samples. | “Errors” in title/report do not by themselves solve differential measurement error of shared adjustment X. | https://doi.org/10.3768/rtipress.2024.mr.0053.2405 |
| R077 | Beresovsky V, Gershunskaya J, Savitsky TD. Review of Quasi-Randomization Approaches for Estimation from Non-probability Samples. BLS OSMR. 2024. | SR/GD | Current agency review/comparison of participation-probability methods. | Does not make quasi-randomization robust to arbitrary measurement mismatch. | https://www.bls.gov/osmr/research-papers/2024/st240030.htm |
| R078 | Savitsky TD, Williams MR, Gershunskaya J, Beresovsky V, Johnson NG. Methods for Combining Probability and Nonprobability Samples Under Unknown Overlaps. *Statistics in Transition new series*. 2023;24(5):1–34. | PP | Exact/Bayesian likelihood formulation when P and NPS overlap status is unknown. | Sample overlap is a different problem from measurement mismatch. | https://doi.org/10.59170/stattrans-2023-061 |
| R079 | Savitsky TD, Williams MR, Beresovsky V, Gershunskaya J. Thresholding nonprobability units in combined data for efficient domain estimation. *Statistics in Transition New Series*. 2025;26(2); BLS OSMR working-paper version 2024. | PP/GD | Shows low-overlap NPS units can increase error and develops thresholding/exclusion to reduce estimation error. | Directly constrains generic overlap-to-threshold decision novelty; does not solve measurement equivalence. | https://doi.org/10.59139/stattrans-2025-013 |
| R080 | Liu Y, Yuan M, Li P, Wu C. Statistical inference with nonignorable non-probability survey samples. *Electronic Journal of Statistics*. 2026;20(1):2009–2048. | PP | Direct 2026 methodology beyond ignorable participation. | Does not make generic nonignorability an open niche; different from C009's measurement mechanism. | https://doi.org/10.1214/26-EJS2531 |
| R081 | Wu C. Estimation Strategies with Nonignorable Non-Probability Survey Samples. Joint Statistical Meetings 2026 invited session. | GR/PR | Active-work signal: nonignorable participation remains live in Waterloo program. | Conference abstract is not evidence that all sensitivity problems are solved. | https://ww3.aievolution.com/JSMAnnual2026/Events/viewEv?ev=5591 |
| R082 | Hammon A, Zinn S. Validating an Index of Selection Bias for Proportions in Non-Probability Samples. *International Statistical Review*. 2025;93:499–516. | PP | Validates sensitivity index for nonignorable selection; explicitly notes need for suitable, identically measured shared variables. | Does not treat the measurement mismatch itself as the inferential target. | https://doi.org/10.1111/insr.12590 |

# L. Direct 2025–2026 neighbors and idea-killing evidence

| ID | Citation / source | Type | What it establishes | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R083 | Landsman V, Wang L, Carrillo-Garcia I, et al. Correction for Participation Bias in Nonprobability Samples Using Multiple Reference Surveys. *Statistics in Medicine*. 2026;45:e70403. | PP | General framework for multiple reference surveys; requires/hardens harmonization of auxiliaries; direct active line. | Does not model residual source-specific measurement error after harmonization. | https://doi.org/10.1002/sim.70403 |
| R084 | Flood JRA, Mostafa SA. Survey data integration for distribution function and quantile estimation. *Japanese Journal of Statistics and Data Science*. 2026. | PP | Direct CDF/quantile integration method; kills generic “extend means to quantiles” idea. | Does not address C009. | https://doi.org/10.1007/s42081-026-00338-0 |
| R085 | Sen A, Lahiri P. Improving measurement error and representativeness in nonprobability surveys. *Survey Methodology*. 2026;52(1):1–26. | PP | Directly combines measurement-error and representativeness concerns using multiple P/NP surveys. | Focuses on response measurement/composite estimation; does not obviously treat differential error in the shared participation-adjustment covariates. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2026001/article/00013-eng.htm |
| R086 | Wang Z, Kim HJ, Kim JK. Survey data integration for regression analysis using model calibration. *Survey Methodology*. 2023;49(1). | PP | Regression/association targets and model calibration are active. | Does not make regression-target novelty unavailable if a different failure mechanism is central. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2023001/article/00002-eng.htm |
| R087 | Einarsson H, Sakshaug JW, Cernat A, Cornesse C, Blom AG. Measurement equivalence in probability and nonprobability online panels. *International Journal of Market Research*. 2022;64(4):484–505. | PP | Empirical evidence that P and NP panels can differ in measurement properties; demographic weighting does not guarantee equivalence. | Does not derive finite-population selection-adjustment bias from error in shared X. | https://doi.org/10.1177/14707853221085206 |
| R088 | Dharma C, Smith P, Salway T, et al. A two-step approach to simultaneously correct for selection and misclassification bias in nonprobability samples from hard-to-reach populations. *American Journal of Epidemiology*. 2025;194(11):3267–3272. | PP | Very close selection×measurement neighbor; ALP implementation explicitly assumes participation covariates are measured without error in both sources. | Misclassification target is hard-to-reach group status; does not solve general source-specific error in participation-adjustment X. | https://doi.org/10.1093/aje/kwaf132 |
| R089 | McCaffrey DF, Lockwood JR, Setodji CM. Inverse probability weighting with error-prone covariates. *Biometrika*. 2013;100(3):671–680. | PP | Critical methodological ancestor: IPW consistency can be repaired under covariate measurement error. | Not specifically two-source probability/NPS finite-population integration with different measurement maps in each source. | https://doi.org/10.1093/biomet/ast022 |
| R090 | Zhu T, Gamble LJ, Klapman M, Xue L, Lesser VM. Using Auxiliary Information in Probability Survey Data to Improve Pseudo-Weighting in Nonprobability Samples: A Copula Model Approach. *JSSAM*. 2024;12(5):1338–1364. | PP | Active pseudo-weighting with common ancillary variables; distribution modeling of X is sophisticated. | Still assumes a common set of ancillary variables observed across samples; not differential measurement of X. | https://doi.org/10.1093/jssam/smad032 |
| R091 | Kim JK. Calibration Weighting for Analyzing Non-Probability Samples. *Journal of Official Statistics*. 2025. | PP | Shows calibration weighting remains an active theoretical core. | Assumes auxiliary information is valid/available; does not address C009 directly. | https://doi.org/10.1177/0282423X251318104 |

# M. Public data and agency programs

| ID | Source | Type | What it establishes | Caveat | Stable locator |
|---|---|---:|---|---|---|
| R092 | NCHS/CDC — RANDS Questionnaires, Data, and Documentation. | DS/GD | Public-use RANDS rounds 1–10; rounds 8–10 use both probability and nonprobability samples. | Public data do not provide a gold standard for every measurement construct. | https://www.cdc.gov/nchs/rands/data-documentation/index.html |
| R093 | NCHS/CDC — RANDS 10 Probability Sample Description. | DS | 5,017 completes; AmeriSpeak; web and phone; common questionnaire content. | Probability sample still has survey nonresponse/mode issues. | https://www.cdc.gov/nchs/rands/data-documentation/r10probasample.html |
| R094 | NCHS/CDC — RANDS 10 Nonprobability Sample Description. | DS | 5,420 opt-in Cint-Lucid web respondents; public CSV/text/codebook/questionnaire. | Opt-in sample is not nationally representative by design. | https://www.cdc.gov/nchs/rands/data-documentation/r10nonprobasample.html |
| R095 | NCHS. RANDS 10 Probability Sample Technical Documentation. | DS/GD | Sampling strata, AmeriSpeak design, web+phone modes, weighting; establishes detailed provenance. | Does not itself quantify cross-source measurement error. | https://www.cdc.gov/nchs/media/pdfs/2025/12/RANDS10-technical-documentation.pdf |
| R096 | NCHS. RANDS 10 Non-Probability Sample Technical Documentation. | DS/GD | Balancing weight matches age, race/Hispanic ethnicity, education, marital and metro status to P sample using inverse propensity scores. | Documentation warns combined pseudo-sample is not for nationally/subnationally representative estimates. | https://www.cdc.gov/nchs/media/pdfs/2025/12/RANDS10-np-technical-documentation.pdf |
| R097 | NCHS/CDC — RANDS 9 Probability Sample Description. | DS | 7,055 probability-sample completes; repeated paired-source substrate. | Round-specific questionnaire/design. | https://www.cdc.gov/nchs/rands/data-documentation/r9probasample.html |
| R098 | NCHS/CDC — RANDS 9 Nonprobability Sample Description. | DS | 8,973 Cint-Lucid nonprobability respondents; public files. | Oversampling/round-specific content must be respected. | https://www.cdc.gov/nchs/rands/data-documentation/r9nonprobasample.html |
| R099 | NCHS Research Data Center — RANDS restricted-data overview. | DS/GR | RANDS explicitly examines measurement error, calibration and comparisons of probability/opt-in platforms/modes. | Restricted variables require RDC approval; public-use files remain available separately. | https://www.cdc.gov/rdc/restricted-nchs-variables/rands.html |
| R100 | U.S. Census Bureau — Sampling Estimation & Survey Inference. | GR | “Integration of data from probability and nonprobability samples” is a current subproject; short/long-term FY2025–FY2027 activities include empirical/simulation studies. | Institutional agenda does not disclose all unpublished work. | https://www.census.gov/topics/research/stat-research/expertise/survey-sampling.html |
| R101 | U.S. Census Bureau — Center for Statistical Research & Methodology FY2025 Annual Report, Nonprobability Samples. | GR/GD | Confirms active internal program and training on calibration, propensity, MI, DR/MR methods. | Annual report is program evidence, not peer-reviewed methodological proof. | https://www.census.gov/content/dam/Census/library/publications/2025/adrm/2025-CSRM-Annual-Report.pdf |
| R102 | U.S. Bureau of Labor Statistics OSMR — Research Papers index. | GR | Shows active agency sequence on unknown overlap, thresholding and quasi-randomization. | Index does not capture unpublished work. | https://www.bls.gov/osmr/research-papers/home.htm |

# N. Research groups / active-work signals

| ID | Group / source | Type | Relevance | Stable locator |
|---|---|---:|---|---|
| R103 | University of Waterloo — Changbao Wu publications / NPS program. | GR | Dense lineage: DR, mass imputation, pseudo EL, undercoverage, 2026 nonignorable inference. | https://sas.uwaterloo.ca/~cbwu/Publications.html |
| R104 | University of Waterloo — 2026 SSC Gold Medal profile for Changbao Wu. | GR | Confirms major active expertise in calibration, empirical likelihood and NPS; high-competition group to monitor. | https://uwaterloo.ca/statistics-and-actuarial-science/news/changbao-wu-2026-statistical-society-canada-gold-medalist |
| R105 | Iowa State Statistics — Jae-kwang Kim 2026 seminar, “Bregman projection for calibration estimation and data integration.” | GR | Current 2026 signal that calibration/data-integration theory remains active. | https://www.stat.iastate.edu/event/2026/bregman-projection-calibration-estimation-and-data-integration-jae-kwang-kim |
| R106 | University of Michigan ISR — Elliott & Si, Data Integration in Surveys & Clinical Trials workshop (2024). | GR | Active applied/methodological cluster; explicitly covers P→NPS representativeness and software. | https://pdhp.isr.umich.edu/workshops/data-integration-in-surveys/ |
| R107 | Kawano S, Vedensky D, Dong Q, et al. Nonprobability Samples for Small Area Estimation: A Review and Comparative Simulation Study. arXiv:2608.13673. 2026. | PR | Very current map/comparison; demonstrates SAE+NPS is rapidly active and not an easy low-competition niche. | https://arxiv.org/abs/2608.13673 |

# O. Software / reproducibility

| ID | Resource | Type | Use | Stable locator |
|---|---|---:|---|---|
| R108 | `survey` R package. | SW | Complex-survey design, calibration, weighting and inference; standard reproducibility substrate. | https://cran.r-project.org/package=survey |
| R109 | `nonprobsvy` R package. | SW | Nonprobability survey inference tools. | https://cran.r-project.org/package=nonprobsvy |
| R110 | `nonprobsampling` R package. | SW | Nonprobability sampling/adjustment tooling. | https://cran.r-project.org/package=nonprobsampling |
| R111 | `svrep` R package. | SW | Replicate-weight and survey simulation/variance infrastructure. | https://cran.r-project.org/package=svrep |
| R112 | Changbao Wu — R code for participation-probability estimation and pseudo empirical likelihood. | SW | Reproducibility resource for CLW-type methods and related survey inference. | https://sas.uwaterloo.ca/~cbwu/R.html |


# P. C009 prosecution — measurement-error/calibration ancestors

| ID | Citation / source | Type | What it establishes | What it does **not** establish | Stable locator |
|---|---|---:|---|---|---|
| R113 | Chambers R. *Measurement Error in Auxiliary Information*. Centre for Statistical & Survey Methodology, University of Wollongong, Working Paper 08-08. 2008. | WP/PP | Directly studies survey calibration when population auxiliary information is erroneous or comes from closely related but non-identical variables; substitution of the wrong control can create substantial bias. | Does not analyze a P/NPS selection problem or decompose wrong-scale benchmark bias from residual proxy-selection bias. | https://documents.uow.edu.au/content/groups/public/%40web/%40inf/%40math/documents/doc/uow043739.pdf |
| R114 | Hong H, Rudolph KE, Stuart EA. Bayesian Approach for Addressing Differential Covariate Measurement Error in Propensity Score Methods. *Psychometrika*. 2017;82(4):1078–1096. | PP | Direct ancestor for propensity methods when a confounder/covariate is measured differently across groups; develops Bayesian sensitivity/correction machinery. | Causal treatment-effect setting rather than finite-population P/NPS reference-calibration; does not isolate a wrong-reference-scale benchmark component. | https://doi.org/10.1007/s11336-016-9533-x |
| R115 | Kim JK, Tam SM. Data Integration by Combining Big Data and Survey Sample Data for Finite Population Inference. *International Statistical Review*. 2021;89(2):382–401. | PP | Very close finite-population ancestor: combines probability and nonprobability/big-data sources while handling undercoverage/selection, measurement error and matching misclassification. | Measurement error is not centered on a nominally shared participation-adjustment covariate encoded through source-specific maps with a P-reference wrong-scale calibration target. | https://doi.org/10.1111/insr.12434 |
| R116 | Carroll RJ, Chen X, Hu Y. Identification and Estimation of Nonlinear Models Using Two Samples with Nonclassical Measurement Errors. *Journal of Nonparametric Statistics*. 2010;22(4):379–399. | PP | Shows that two-sample errors-in-variables models can be identified without gold-standard X under additional structural conditions; prevents overclaiming generic nonidentification. | Observed-data structure and invariance assumptions differ from a probability reference with only auxiliary data plus a selected NPS with Y. | https://doi.org/10.1080/10485250902874688 |
| R117 | Dever JA, Valliant R. General Regression Estimation Adjusted for Undercoverage and Estimated Control Totals. *Journal of Survey Statistics and Methodology*. 2016;4(3):289–318. | PP | Establishes that calibration controls estimated from another survey carry additional uncertainty that can matter for inference. | Random/estimated control totals are not the same as controls measured on a noncommensurate semantic/measurement scale. | https://doi.org/10.1093/jssam/smw001 |
| R118 | Opsomer JD, Erciulescu AL. Replication variance estimation after sample-based calibration. *Survey Methodology*. 2021;47(2):265–277. | PP | Provides valid replication variance methods when one survey supplies random control totals for calibration of another; directly relevant two-survey calibration ancestor. | Assumes the controls are conceptually comparable; does not model source-specific measurement maps. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2021002/article/00006-eng.htm |
| R119 | Collins J, Huynh M. Estimation of diagnostic test accuracy without full verification: a review of latent class methods. *Statistics in Medicine*. 2014;33(24):4141–4169. | SR | Summarizes the classical identification count: with two fallible binary tests in one population and no gold standard, prevalence plus four accuracy parameters are not identified from a 2x2 table without extra restrictions/information. | Diagnostic-test setting; used only as an identification analogue for a bridge sample with two fallible measurements. | https://pmc.ncbi.nlm.nih.gov/articles/PMC4199084/ |

# Q. C009 stage-2 sensitivity / partial-identification ancestors

| ID | Citation / source | Type | What it establishes | Consequence for C009 | Stable locator |
|---|---|---:|---|---|---|
| R120 | Hartman E, Huang M. Sensitivity Analysis for Survey Weights. *Political Analysis*. 2024;32(1):1–16. Published online 2023. | PP | Develops sensitivity analyses for survey weights. For a covariate measured in the survey sample but not the target population, calibration/raking sensitivity reduces to varying the unknown target-population mean/moment over plausible values and re-estimating weights; also develops robustness thresholds/benchmarking. | C009's `delta`-only analysis, with `q_B^P=q_A-delta`, is substantially a binary reparameterization of an unknown target-margin sensitivity problem. The joint wrong-scale + latent-proxy attenuation interaction remains more specific. | https://doi.org/10.1017/pan.2023.12 |
| R121 | Molinari F. Partial identification of probability distributions with misclassified data. *Journal of Econometrics*. 2008;144(1):81–117. | PP | Direct misclassification approach; derives sharp identification regions for real functionals under restrictions on misclassification matrices, including known lower bounds on correct-report probabilities. | Generic “bound sensitivity/specificity and partially identify the target” cannot be claimed as new. C009 would need structure specific to P/NPS calibration beyond this machinery. | https://doi.org/10.1016/j.jeconom.2007.12.003 |
| R122 | Imai K, Yamamoto T. Causal Inference with Differential Measurement Error: Nonparametric Identification and Sensitivity Analysis. *American Journal of Political Science*. 2010;54(2):543–560. | PP | Nonparametric identification analysis and sensitivity analysis for differential misclassification/measurement error. | Further crowds generic differential-measurement sensitivity claims; different estimand but strong methodological ancestor. | https://doi.org/10.1111/j.1540-5907.2010.00446.x |
| R123 | Rudolph KE, Stuart EA. Using Sensitivity Analyses for Unobserved Confounding to Address Covariate Measurement Error in Propensity Score Methods. *American Journal of Epidemiology*. 2018;187(3):604–613. | PP | Shows covariate measurement error can be recast as unobserved confounding and adapts several existing sensitivity analyses to classical and differential measurement error in propensity-score methods. | Weakens any claim that sensitivity analysis for error-prone weighting covariates is itself novel. | https://doi.org/10.1093/aje/kwx248 |
| R124 | Lockwood JR, McCaffrey DF. Matching and Weighting With Functions of Error-Prone Covariates for Causal Inference. *Journal of the American Statistical Association*. 2016;111(516):1831–1839. | PP | Gives necessary and sufficient conditions for matching/weighting on functions of error-prone covariates, including discrete misclassification, and shows group-specific functions may sometimes recover appropriate balance. | Strong ancestor for the proxy-attenuation/weighting side; leaves the P-reference wrong-scale target-margin interaction as the narrower possible distinction. | https://doi.org/10.1080/01621459.2015.1122601 |

# Pass-3 evidence synthesis — C009 identification prosecution (historical stage-1 snapshot)

1. **The broad C009 novelty framing fails.** Chambers [R113] already studies calibration to erroneous/non-identical auxiliary information; Hong et al. [R114] already study differential propensity-covariate measurement error; Kim & Tam [R115] already combine finite-population integration and measurement error.
2. **The remaining object is narrower and interaction-specific.** The prosecution derived a decomposition separating wrong-scale reference-benchmark bias from residual selection bias due to conditioning on a noisy proxy; no exact P/NPS treatment of that decomposition surfaced in the targeted search.
3. **No-validation identification is not automatic.** A canonical P-reference/NPS observed-data structure can generate the same observed distributions under distinct latent target means. But generic statements that “two noisy samples are unidentified” are false without qualification because richer two-sample EIV models can be identified [R116].
4. **A bridge sample must be specified precisely.** Measuring two fallible versions on the same units does not by itself identify a latent binary construct in one population [R119]. A representative bridge administered on the NPS measurement scale can, however, identify the correct B-scale benchmark and remove the wrong-scale calibration component without identifying latent X.
5. **Estimated-control uncertainty is a different ancestor.** Dever & Valliant and Opsomer & Erciulescu [R117–R118] address randomness in otherwise commensurate controls, not source-semantic incompatibility.
6. **RANDS remains a credible illustration, not a gold-standard validation source.** RANDS 10 provides paired P/NPS sources [R092–R096]; its probability documentation records that demographic questions were added for opt-in panelists after pretest, supporting a real provenance difference for adjustment information. It does not reveal latent true values or source-specific error rates.
7. **Stage-1 status at that time:** C009 was **PROSECUTION — NARROWED**. That gate was subsequently resolved in Pass 4 below.

# Pass-4 evidence synthesis — C009 sensitivity-utility prosecution

1. **A decision-relevant algebraic object exists.** Stage 2 compresses the binary toy model into `mu = mu_B + ((d_obs-delta) Delta_W)/kappa`, with `kappa=Corr(X,W_B|R=1)^2`. This yields exact tipping boundaries for whether naive calibration helps, hurts, over-corrects, under-corrects, or reverses direction.
2. **The mismatch-only sensitivity component is not an independent novelty.** Hartman & Huang [R120] already treat an unknown target-population margin of a survey-observed weighting covariate as a calibration sensitivity parameter. C009's `delta` simply re-expresses that unknown B-scale target margin relative to an observed A-scale margin.
3. **The generic partial-identification step is occupied.** Molinari [R121] explicitly handles lower bounds on correct-report probabilities and sharp identification regions under discrete misclassification. C009 can use this logic but cannot claim it.
4. **The measurement-error sensitivity/weighting neighborhood is crowded.** Imai & Yamamoto [R122], Rudolph & Stuart [R123], Hong et al. [R114], McCaffrey et al. [R089], and Lockwood & McCaffrey [R124] collectively cover differential measurement error, sensitivity analysis, and weighting with error-prone covariates.
5. **RANDS cannot currently anchor the two sensitivity parameters.** RANDS establishes real P/NPS provenance and mode differences and exposes the variables used for balancing, but it does not provide gold-standard latent values or source-specific measurement-error parameters for those adjustment variables [R092–R096].
6. **External reliability evidence does not solve that problem generically.** Reliability/misclassification can vary sharply by construct, coding, subgroup and data source, so one universal correctness bound would be difficult to defend for the RANDS balancing variables.
7. **Final C009 status:** **PARKED / NO-GO FOR FIRST PROJECT.** Preserve the joint `delta`-`kappa` lemma and reopen only with validation/bridge information, defensible construct-specific bounds, or a nontrivial multivariable extension.

# Pass-2 evidence synthesis

## Strongly supported field-level conclusions

1. **Survey data integration/NPS inference is important and institutionally active.** Declining response, cost and new data sources motivate current academic and official-statistics work. [R061–R063, R100–R102]
2. **The field has a coherent inferential core.** Quasi-randomization, calibration, outcome modeling, mass imputation and DR/MR estimation all revolve around explicit finite-population assumptions. [R063–R072]
3. **Ignorability, overlap and shared auxiliary information are central vulnerabilities.** Recent methods actively address nonignorability and undercoverage, so generic versions are crowded. [R071, R080–R082]
4. **Measurement comparability is a real problem, not an invented gap.** Field mapping and panel-comparison work identify mode/source measurement differences; practical sensitivity methods need comparable shared variables. [R065, R087, R082]
5. **C009's seam is narrower than “measurement error + selection.”** Direct 2025–2026 papers already combine measurement and selection in other ways. [R085, R088]
6. **The exact adjustment-X mismatch question remains unverified, not proven novel.** R088 explicitly assumes participation covariates are error-free; R089 is the strongest general methodological ancestor and could collapse C009 if the two-source extension is trivial.
7. **Public paired-source data are unusually feasible.** RANDS 9–10 provide probability/NPS samples, documentation and balancing procedures without proprietary panels. [R092–R099]

## Evidence that could kill C009

- R089 may already imply the necessary correction once the integration estimator is written as an IPW/missingness problem.
- R085 may contain broader measurement-error machinery than is visible from abstract-level screening and must be read mathematically during prosecution.
- Survey calibration under measurement error has an older literature not yet exhaustively citation-chained in this pass.
- “Harmonize the variables” may be sufficient operationally for some cases; C009 needs a statistical question that remains after best-practice harmonization.
- Without validation information, selection and source-specific measurement may be too weakly identified for useful inference.

## Reproducibility rule for C009 prosecution — fulfilled in v0.4 stage 1

The stage-1 prosecution created the required nearest-neighbor derivation matrix in `13_C009_IDENTIFICATION_PROSECUTION.md` and expanded it with R113–R119. The matrix records:

- target parameter;
- sample structure;
- which variables are observed in each source;
- measurement-error model;
- selection/ignorability assumption;
- overlap assumption;
- validation data required;
- estimator/identification result;
- variance/uncertainty result;
- whether source-specific X measurement is allowed;
- exact theorem/claim C009 would add.

# R. C010 response-quality filtering / survey-quality prosecution

| ID | Citation / source | Type | What it establishes | Consequence for C010 | Stable locator |
|---|---|---:|---|---|---|
| R125 | Kennedy C, Mercer A, Lau A. Exploring the assumption that commercial online nonprobability survey respondents are answering in good faith. *Survey Methodology*. 2024. | PP | Shows that NPS selection-adjustment logic can fail when response measurement is systematically wrong; documents bogus responding as a serious NPS problem. | Confirms importance but occupies the broad “selection adjustment must account for bogus measurement” motivation. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2024001/article/00013-eng.htm |
| R126 | Sen A, Lahiri P. Improving measurement error and representativeness in nonprobability surveys. *Survey Methodology*. 2026;52(1):1–26. | PP | Directly addresses measurement error together with representativeness/selection in nonprobability survey inference. | Generic measurement-error × NPS-selection methodology cannot be claimed as C010 novelty. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2026001/article/00013-eng.htm |
| R127 | Slamowicz S, Pennay D, Neiger D, Phillips B, Ward AC, Xu M. Reducing the Bias from Probability and Nonprobability Online Panels by Excluding Satisficers. *Journal of Survey Statistics and Methodology*. 13(5):469–493; published 2026-01-28 (issue dated Nov 2025). | PP | Excludes satisficers before recalculating weights; across four NPPs, exclusion plus weighting reduces average absolute bias more than weighting alone. Underlying data are not publicly shareable. | Directly kills the broad C010 empirical claim; residual contribution must explain when filtering helps/hurts under imperfect screens. | https://doi.org/10.1093/jssam/smaf019 |
| R128 | Mathur MB. On the Statistical Analysis of Studies With Attention Checks. *Advances in Methods and Practices in Psychological Science*. 2025;8(2). | PP | Formalizes attention checks as measurement-error indicators and gives conditions under which exclusion is unbiased; shows exclusion can induce selection bias and discusses covariate adjustment/sensitivity. | Strong formal ancestor for “quality filtering is selection”; C010 must add NPS calibration-specific structure. | https://doi.org/10.1177/25152459251338041 |
| R129 | Mercer A. No Easy Fix for Bogus Respondents in Online Opt-In Polls. Pew Research Center. 2026-08-27. | TR | Compares trap questions, automated prescreening and voter-file matching in an opt-in poll; shows screening can improve some quality metrics yet remove valid cases and worsen some substantive estimates. | Strong data- and decision-channel evidence for asymmetric filtering costs; not a general inferential theory. | https://www.pewresearch.org/methods/2026/08/27/no-easy-fix-for-bogus-respondents-in-online-opt-in-polls/ |
| R130 | Mercer A. Methodology for No Easy Fix for Bogus Respondents in Online Opt-In Polls. Pew Research Center. 2026-08-27. | TR | Documents N=11,114 and retained counts under three screens; separate post-screen analyses allow direct composition comparison. | Provides current operational detail and illustrates how dramatically screen choice changes the retained analytic sample. | https://www.pewresearch.org/2026/08/27/bogus-respondents-methodology/ |
| R131 | Raynes S, Marlar J. Data Quality Issues With Opt-In Panels: Part 2. Gallup Methodology Blog. 2024-12-18. | TR | Compares lenient/moderate/strict/custom removal thresholds; strict/custom rules remove ~44%–46% of the sample with only modest benchmark changes. | Strong decision-channel evidence that more aggressive filtering need not produce proportional inferential gain. | https://news.gallup.com/opinion/methodology/654494/data-quality-issues-opt-panels-part-two.aspx |
| R132 | Francois JR. Attention-check performance and its implications for quality-of-life research. *Quality & Quantity*. 2026. | PP | Examines systematic variation in attention-check performance and how filtering affects substantive quality-of-life findings. | Supports the composition/estimand-dependence mechanism behind filter-induced selection. | https://doi.org/10.1007/s11135-026-03061-w |
| R133 | Kennedy C, Hatley N, Lau A, Mercer A, Keeter S, Ferno J, Asare-Marfo D. Assessing the Risks to Online Polls From Bogus Respondents. Pew Research Center. 2020-02-18. | TR | >60,000 interviews across six online sources; bogus cases in opt-in sources create systematic, not merely random, error and common checks miss many cases. | Strong empirical substrate and motivation for C010. | https://www.pewresearch.org/methods/2020/02/18/assessing-the-risks-to-online-polls-from-bogus-respondents/ |
| R134 | Pew Research Center. Assessing Risk to Online Polls Dataset. 2020. | DS | Public-use microdata corresponding to R133, downloadable after Pew account access. | Best public empirical substrate found for C010 illustration, though not a universal gold-standard respondent-quality label. | https://www.pewresearch.org/dataset/assessing-risk-to-online-polls-dataset/ |
| R135 | Cornesse C, Blom AG. Response Quality in Nonprobability and Probability-based Online Panels. *Sociological Methods & Research*. 2023;52(2):879–908. | PP | Compares response-quality behavior across probability and nonprobability online panels. | Establishes mature empirical response-quality comparison literature. | https://doi.org/10.1177/0049124120914940 |
| R136 | Ward MK, Meade AW. Dealing with Careless Responding in Survey Data: Prevention, Identification, and Recommended Best Practices. *Annual Review of Psychology*. 2023;74:577–596. | SR | Comprehensive review of careless-response prevention, identification, reporting and cleaning. | Generic careless-response detection/cleaning is mature; C010 must be inferentially narrower. | https://doi.org/10.1146/annurev-psych-040422-045007 |
| R137 | Stosic MD, Murphy BA, Duong F, Fultz AA, Harvey SE, Bernieri F. Careless Responding: Why Many Findings Are Spurious or Spuriously Inflated. *Advances in Methods and Practices in Psychological Science*. 2024. | PP | Shows careless responding can systematically distort results and emphasizes consequences of screening decisions. | Further crowds generic “remove careless cases to improve inference” claims. | https://doi.org/10.1177/25152459241231581 |
| R138 | Freese J, Jin O. Online Nonprobability Samples. *Annual Review of Sociology*. 2025;51:109–128. | SR | Reviews modern online NPS issues, including problematic respondents and inferential limitations. | Signals a mature broad field; C010 requires a precise statistical object. | https://doi.org/10.1146/annurev-soc-090524-043117 |
| R139 | AAPOR. Data Quality Metrics for Online Samples: Considerations for Study Design & Analysis. 2023-02-22. | TR | Reviews online-panel quality and representativeness considerations and practical quality metrics. | Decision-channel evidence for institutional need; not a novelty source. | https://aapor.org/reports/data-quality-metrics-for-online-samples-considerations-for-study-design-analysis/ |
| R140 | AAPOR. A Guide To Detecting Fraud In Online Survey Data. Webinar/event, 2026-08-26. | AW | Current practitioner programming on fraud detection and the FAST approach. | Active-work signal showing the topic is rapidly moving and practitioner-facing. | https://portal.aapor.org/integratedEvents/home/A-GUIDE-TO-DETECTING-FRAUD-IN-ONLINE-SURVEY-DATA |
| R141 | Schofield MR, Maze MJ, Crump JA, Rubach MP, Galloway R, Sharples KJ. On the robustness of latent class models for diagnostic testing with no gold standard. *Statistics in Medicine*. 2021;40(22):4751–4763. | PP | Shows sensitivity/specificity estimation without a gold standard relies on latent-class assumptions whose violations can materially bias results. | “Unknown FP/FN rates” is not an empty methodological space; C010 needs structure-specific identification or sensitivity beyond generic no-gold-standard methods. | https://doi.org/10.1002/sim.8999 |

# Pass-5 evidence synthesis — C010 four-channel prosecution

1. **Four-channel convergence establishes importance, not novelty.** Literature, theory, data and practitioner decisions all indicate that response-quality filtering can interact with selection and weighting [R125–R140].
2. **The broad contribution is occupied.** R127 directly evaluates exclusion before recalculating weights in probability/nonprobability online panels and reports lower NPP bias.
3. **Filtering as selection has formal prior art.** R128 already derives selection-bias conditions for attention-check exclusion and covariate-adjusted analysis.
4. **Generic NPS measurement-error × representativeness methods are current.** R126 directly occupies that high-level interface.
5. **A clean residual decomposition exists.** Under ideal calibration to target `X`, post-filter error separates into retained response contamination and residual selection among `S=1,C=1` cases. This is useful diagnostic structure but not yet a differentiating theorem.
6. **Real data show the tradeoff can change sign.** R129–R131 demonstrate that screens can remove valid cases, alter subgroup composition, and produce only modest or even adverse changes in substantive benchmark error.
7. **The main feasibility bottleneck is validation, not compute.** R134 supports empirical illustration, while the direct R127 data are not publicly shareable and real studies rarely observe universal gold-standard respondent quality.
8. **No-gold-standard screen accuracy is mature territory.** R141 and R121 mean that a future C010 cannot claim generic latent-class or bounded-misclassification sensitivity as its novelty.
9. **Final C010 status:** **PARKED / NO-GO FOR FIRST PROJECT.** Reopen only with credible validation information or a new post-filter calibration identification/decision result.

# S. OF-19–OF-23 collapse-first triage

| ID | Citation / source | Type | What it establishes | Triage consequence | Stable locator |
|---|---|---:|---|---|---|
| R142 | Jackson MT, Hasanbasri A, McPhee C, Peugh J. The Utility of a Random Forest Propensity Adjustment in Recurring Hybrid Probability-Nonprobability Samples: Evidence from a Tracking Poll. *Survey Practice*. 2022;15(1). | PP/TR | Directly asks whether NPS selection mechanisms change across recurring waves; shows changing predictors of NPS membership, stale-raking trend distortion and partial repair by propensity+raking. | Collapses broad OF-22. Residual must differ through intermittent anchors, identification or a new decision rule. | https://doi.org/10.29115/SP-2022-0004 |
| R143 | Pfeffermann D, Preminger A, Sikov A. Statistical Inference Under Nonignorable Sampling and Nonresponse—An Empirical Likelihood Approach. *Journal of Survey Statistics and Methodology*. 2025;13(5):519–551. | PP | Develops empirical-likelihood inference for informative probability sampling plus nonignorable nonresponse when selection/response depends on the outcome after conditioning on covariates. | Strong adjacent ancestor for OF-19's nonignorability logic, but not a direct nonprobability-sample method; do not count it as direct NPS prior art. | https://doi.org/10.1093/jssam/smaf015 |
| R144 | Andridge R. Sensitivity Analyses for Nonignorable Selection Bias When Estimating Subgroup Parameters in Nonprobability Samples: A Weighting Approach. Michigan Program in Survey and Data Science seminar, 2026-01-28. | AW/GR | Current work extending proxy-pattern-mixture sensitivity analysis for NPS to subgroup parameters. | Active-work signal that generic nonignorable NPS sensitivity remains competitive. | https://psm.mivideo.it.umich.edu/media/t/1_d39skp41 |
| R145 | Franguridi G, Kapteyn A. Testing selection on observables in parametric models with refreshment samples. Working paper / arXiv:2608.23508. 2026. | PR | Uses refreshment samples to test the selection-on-observables assumption by comparing distributions implied by alternative weighting schemes. | Strong ancestor for any intermittent-anchor OF-22 descendant; not itself a recurring NPS integration method. | https://arxiv.org/abs/2608.23508 |
| R146 | Conti PL, Marella D, Summa D. The effect of non-identifiability of sampling design in the inference from non-probability samples. *Statistical Methods & Applications*. 2026. | PP | Formalizes uncertainty arising from non-identifiable NPS sampling designs and contraction of plausible classes under extra-sample information. | Further crowds generic OF-19 sensitivity/uncertainty claims and reinforces identification-first screening. | https://doi.org/10.1007/s10260-026-00864-x |
| R147 | Lohr SL. Comments on “Statistical inference with non-probability survey samples”. *Survey Methodology*. 2022;48(2). | PP/CM | States that NPS inference requires strong assumptions, describes diagnostics for assessing those assumptions, and explicitly discusses when NPS data should be used. | Further constrains generic OF-23 formulations that claim novelty merely by linking overlap/model diagnostics to a use/do-not-use decision. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2022002/article/00005-eng.htm |

# Pass-6 evidence synthesis — OF-19–OF-23 collapse-first triage

1. **OF-19 broad sensitivity/nonignorability is crowded.** R080 and R144 directly occupy nonignorable NPS inference/sensitivity; R146 adds a current non-identifiability/uncertainty formulation, while R143 is a strong adjacent nonignorable sampling/nonresponse ancestor.
2. **OF-20 generic regression integration is occupied.** R086 directly treats regression analysis under data integration; any future version needs a mechanism-specific identification/failure result.
3. **OF-21's core decision is occupied.** R073 explicitly decides whether to borrow NPS data or retain probability-only inference; R074 adds current efficient combination.
4. **OF-22 broad temporal drift is directly occupied.** R142 asks the same recurring-wave mechanism question and documents stale-adjustment trend failure.
5. **OF-22 retains only a pre-candidate residue.** Intermittent probability/reference anchors create a distinct design, but R145 and the broader refreshment-sample literature are strong ancestors and no public validation path/theorem is yet established.
6. **OF-23 generic overlap-to-action is occupied.** R071 covers deterministic undercoverage/positivity; updated R079 provides peer-reviewed thresholding/exclusion tied to estimation error; R147 explicitly connects NPS diagnostics to the decision whether NPS data are fit for use.
7. **No C011 is assigned.** The correct output of this bounded pass is a collapsed slate plus one sharpen-before-candidate watchlist residue, not forced promotion.

# T. D013 fresh four-channel opportunity generation

| ID | Citation / source | Type | What it establishes | Opportunity consequence | Stable locator |
|---|---|---:|---|---|---|
| R148 | Irimata KE, Dahlhamer JM, Bramlett MD, Cai B, He Y, Parsons VL, Wei R. Methodological Research Informing Weighting, Combination, and Quality Assessment for the National Center for Health Statistics Rapid Surveys System Rounds 1–4. *Vital and Health Statistics*. Series 2, No. 215. 2026. | GR/TR | NCHS RSS uses NHIS benchmark variables for quality assessment; Rounds 1–3 rotated benchmark domains and Round 4 selected benchmarks related to main survey content. Bias varied by variable/domain. | Direct decision-channel evidence that benchmark selection is operational and content relevance matters; motivates OF-30 without proving novelty. | https://doi.org/10.15620/cdc/252442 |
| R149 | Irimata KE et al. Appendix II: Selection of Rapid Surveys System Round 4 Calibration Variables. In R148. 2026. | TR | Evaluated 99,969 candidate 12-variable calibration sets against 35 benchmark variables using standardized bias; also used leave-one-out assessment. | Strong nearest neighbor for any benchmark-guided tuning claim and motivates OF-31 benchmark-reuse/selection-optimism screening. | https://www.ncbi.nlm.nih.gov/books/NBK624159/ |
| R150 | Kennedy C, Mercer A, Keeter S, Hatley N, McGeeney K, Gimenez A. Evaluating Online Nonprobability Surveys. Pew Research Center. 2016. | TR | Nine NPS samples were evaluated on 20 government benchmarks; explicitly warns that benchmark error need not transfer to political-attitude targets that may have different bias structure. | Core empirical motivation for benchmark-to-target transportability; shows why a scalar benchmark score may not certify unbenchmarked outcomes. | https://www.pewresearch.org/methods/2016/05/02/evaluating-online-nonprobability-surveys/ |
| R151 | Pew Research Center. Online Nonprobability Landscape Study dataset. Survey fielded 2015; released with 2016 report. | DS | Dataset underlying R150; downloadable with a Pew Research Center account. | Realistically obtainable multi-vendor substrate for held-out benchmark experiments. | https://www.pewresearch.org/dataset/online-nonprobability-landscape-study/ |
| R152 | Mercer A, Lau A. Comparing Two Types of Online Survey Samples. Pew Research Center. 2023. | TR | Common questionnaire across three probability-based panels and three opt-in sources (29,937 adults); evaluates 28 government benchmark variables. | Strong multi-source empirical substrate for OF-30 certificate/held-out-target experiments. | https://www.pewresearch.org/methods/2023/09/07/comparing-two-types-of-online-survey-samples/ |
| R153 | Pew Research Center. 2021 Benchmarking Study dataset. Fielded 2021; released with R152 in 2023. | DS | Dataset associated with the six-sample benchmarking study. | Candidate data substrate for provider ranking stability and leave-domain-out benchmark validation. | https://www.pewresearch.org/dataset/2021-benchmarking-study/ |
| R154 | Kocar S. Accuracy and practical considerations in an RDD text-to-web survey. *International Journal of Market Research*. 2024;66(4):473–495. | PP | Uses 26 benchmark items and notes that, despite common benchmarking practice and described basic principles, no commonly used methodological framework advises researchers how to perform benchmarking. | Supports the methodological-structure question but is not evidence that OF-30's exact certificate problem is novel. | https://doi.org/10.1177/14707853231219956 |
| R155 | Ivanovska A, Bosnjak M, Vehovar V. Data Quality in Estimates from Probability-Based Online Panels: Systematic Review and Meta-Analysis. *Acta Informatica Pragensia*. 2026;15(1):173–197. | SR/PP | Synthesizes 1,897 relative-bias effects from 44 studies; reports substantial item-level heterogeneity and residual heterogeneity after modeled moderators. | Reinforces that data quality can be item/target dependent rather than one scalar panel property. | https://doi.org/10.18267/j.aip.279 |
| R156 | U.S. Census Bureau. Household Trends and Outlook Pulse Survey — Source and Accuracy Statements. Revised 2026-09-01. | GR/TR | States that March and May 2026 HTOPS weights incorrectly used residential controls including Group Quarters although HTOPS excludes GQ, creating target/control-universe misalignment; corrected files were pending. | Concrete production signal for OF-32, but broad novelty threatened by erroneous-control calibration literature. | https://www.census.gov/programs-surveys/household-pulse-survey/technical-documentation/source-accuracy.html |
| R157 | Parker AM et al. Assessing Public Reach of the 2023 National Test of the Wireless Emergency Alerts (WEA) System: Results of a National Survey. RAND Corporation. 2024. RR-A2451-1. | GR/TR | Six-panel study explicitly deduplicated across online panels; prior-completion reports averaged 1.7% across probability panels and 5.6% for a nonprobability panel aggregator; 2,855 affirmative repeats were excluded. | Real data signal for cross-vendor respondent overlap, but not enough to establish a new methodological gap. | https://www.rand.org/pubs/research_reports/RRA2451-1.html |
| R158 | Craig BM, Hays RD, Pickard AS, Cella D, Revicki DA, Reeve BB. Comparison of US Panel Vendors for Online Surveys. *Journal of Medical Internet Research*. 2013;15(11):e260. | PP | Seven-vendor comparison reports substantial between-vendor respondent overlap; except for one vendor, the authors summarize samples as overlapping by roughly 20% (about one in five respondents participating through two or more vendors). | Direct older evidence that vendor overlap is not a fresh phenomenon; crowds OF-33. | https://doi.org/10.2196/jmir.2903 |
| R159 | Murray-Watters A, Zins S, Sakshaug JW, Cornesse C. Averaging Non-Probability Online Surveys to Avoid Maximal Estimation Error. *Journal of Official Statistics*. 2025;41(2). | PP | Studies eight NPS vendors plus a probability sample and develops multi-vendor averaging/subset logic motivated by consistency and common/redundant error across vendors. | Directly crowds broad “multiple vendors as diversification” claims; OF-33 parked unless identity overlap yields a distinct estimand/covariance result. | https://doi.org/10.1177/0282423X241312775 |
| R160 | Coffey SM, Damineni J, Eltinge J, Mathur A, Varela K, Zotti A. Some Open Questions on Multiple-Source Extensions of Adaptive-Survey Design Concepts and Methods. *Journal of Official Statistics*. 2024;40(1):16–37. | PP | Frames multi-source survey adaptation in terms of goals, design features, auxiliary data, decision rules, systems, and quality/cost/risk profiles. | Broad source-redundancy/quality-change decision ideas are already an active research area; OF-34 parked. | https://doi.org/10.1177/0282423X241235270 |

# Pass-7 evidence synthesis — fresh D013 opportunity generation

1. **One lead showed four-channel convergence:** OF-30 asks whether quality demonstrated on a finite benchmark set transports to unbenchmarked target outcomes.
2. **The decision is real and current.** NCHS uses benchmark variables operationally and changed Round-4 benchmark selection toward main survey content [R148]; Pew explicitly warns that benchmark bias need not transfer to common political-attitude targets [R150].
3. **A tractable validation design exists.** Pew's 2015/2016 and 2021 benchmarking datasets provide multiple benchmarked outcomes across multiple online sample sources [R151–R153], enabling certificate/held-out pseudo-target splits rather than unverifiable claims about unknown truth.
4. **The baseline theory is an identification warning, not yet novelty.** Finite benchmark balance only controls targets linked to the benchmark span/class; unrestricted residual discrepancy defeats universal certification.
5. **Benchmark-guided method tuning is already sophisticated.** NCHS searched 99,969 calibration-variable combinations against 35 benchmark outcomes [R149], so OF-30 cannot be merely another benchmark-based calibration-variable selector.
6. **Item-level heterogeneity strengthens the problem statement.** R155 shows substantial heterogeneity in benchmark bias across items even within probability-based online-panel studies.
7. **OF-31 remains a mechanism, not a candidate.** Reusing the same outcomes to tune and certify a method raises selection-optimism concerns but may collapse into generic post-selection validation.
8. **OF-32 is real but highly threatened.** The 2026 HTOPS control-universe error is a concrete agency failure [R156], but erroneous-control calibration and C009-adjacent theory make broad novelty unlikely.
9. **OF-33 and OF-34 collapse in broad form.** Direct respondent-overlap evidence [R157–R158], current multi-vendor averaging [R159], and multi-source adaptive-design work [R160] already occupy much of the practical decision surface.
10. **No C011 is assigned.** OF-30 advances only to **PRIORITY SCREENING** pending direct nearest-neighbor search, held-out-benchmark feasibility audit and a nontrivial certificate/decision result.

# U. OF-30 bounded screening

| ID | Citation / source | Type | What it establishes | Opportunity consequence | Stable locator |
|---|---|---:|---|---|---|
| R161 | Schouten B, Cobben F, Bethlehem J. Indicators for the representativeness of survey response. *Survey Methodology*. 2009;35(1):101–113. | PP | Introduces R-indicators as whole-survey representativeness/nonresponse-quality indicators and derives their relation to potential/maximal bias for survey items. | Direct ancestor for survey-level quality certification and worst-case bias; broad OF-30 framing cannot claim this conceptual territory. | https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X200900110887 |
| R162 | Shlomo N, Skinner C, Schouten B. Estimation of an indicator of the representativeness of survey response. *Journal of Statistical Planning and Inference*. 2012;142(1):201–211. | PP | Develops R-indicator estimation and explicitly notes that nonresponse bias is defined for a specific population parameter even when a single survey-level indicator is desired. | Strong nearest neighbor to the survey-level-versus-statistic-level tension underlying OF-30. | https://doi.org/10.1016/j.jspi.2011.07.008 |
| R163 | Roberts C, Vandenplas C, Herzing JME. A Validation of R-Indicators as a Measure of the Risk of Bias using Data from a Nonresponse Follow-Up Survey. *Journal of Official Statistics*. 2020;36(3):675–701. | PP | Directly tests how an R-indicator/auxiliary information relates to bias in other survey variables; cautions that greater auxiliary bias does not automatically imply greater target-variable bias and adjustment may not transfer. | Very close conceptual ancestor for validating whether a quality signal transports to unseen survey outcomes. | https://doi.org/10.2478/jos-2020-0034 |
| R164 | Little RJA, West BT, Boonstra PS, Hu J. Measures of the Degree of Departure from Ignorable Sample Selection. *Journal of Survey Statistics and Methodology*. 2020;8(5):932–964. | PP | Argues that selection-bias measures must reflect the relation between sample selection and the specific survey outcome; proposes outcome-specific SMUB/sensitivity analysis. | Crowds any OF-30 repair that simply replaces a global quality certificate with an outcome-specific bias-risk measure. | https://doi.org/10.1093/jssam/smz023 |
| R165 | Hartman E, Hazlett C, Sterbenz C. kpop: a kernel balancing approach for reducing specification assumptions in survey weighting. *JRSS A*. 2025;188(3):875–895 (advance access 2024). | PP | Uses kernel balance and a worst-case approximation-bias criterion over a rich outcome-function class. | Crowds the natural theorem route in which finite balance/benchmark information certifies targets by restricting the target function class. | https://doi.org/10.1093/jrsssa/qnae082 |
| R166 | National Center for Health Statistics. Rapid Surveys System Round 7 Quality Profile. Revised 2026-01-15. | GR/TR | RSS-7 compares 53 benchmark variables to 2025 Q1 NHIS, reports domain-level benchmark bias, and uses 11 variables / 28 control totals in NHIS calibration. | Confirms strong held-out-data feasibility but imposes nested-validation requirements because calibration controls cannot serve as independent certification targets. | https://www.cdc.gov/nchs/data/rss/round7/RSS7-Quality-Profile.pdf |
| R167 | Rohr B, Silber H, Felderer B. Comparing the Accuracy of Univariate, Bivariate, and Multivariate Estimates across Probability and Nonprobability Surveys with Population Benchmarks. *Sociological Methodology*. 2025;55(1):121–154. | PP | Across eight German probability/NPS surveys, relative accuracy depends substantially on which variables/statistics are evaluated. | Supports target/item dependence as an empirical fact but also shows this broad phenomenon is already actively studied. | https://doi.org/10.1177/00811750241280963 |
| R168 | Smola A. Submodular Benchmark Selection. arXiv:2605.02209. 2026. | PR | Formalizes selecting a small informative benchmark subset to predict/impute remaining benchmark performance under a multivariate Gaussian model using entropy/mutual information and held-out validation. | Cross-field active-work threat to generic “select representative benchmarks that predict unseen benchmarks” novelty. | https://arxiv.org/abs/2605.02209 |
| R169 | Mercer A, Lau A. Assessing the accuracy of estimates for U.S. adults. Pew Research Center. 2023. | TR | Evaluates six online samples using 28 benchmarks / 77 categories and explicitly states relative accuracy might differ under a different benchmark set or weighting scheme. | Direct motivation and data-feasibility evidence for benchmark-set instability, but not a new theory result. | https://www.pewresearch.org/methods/2023/09/07/assessing-the-accuracy-of-estimates-for-u-s-adults/ |

# Pass-8 evidence synthesis — OF-30 bounded screening

1. **The motivating decision is real but the broad conceptual gap is not.** R-indicator work already asks how a whole-survey quality indicator relates to statistic-specific bias [R161–R163].
2. **Outcome specificity is a mature response.** R164 explicitly builds selection-bias assessment around the outcome/selection relationship.
3. **The natural theorem route is crowded.** Once targets are restricted to a function class, worst-case bias/balance methods such as kpop already provide the relevant structure [R165].
4. **The empirical data gate passes.** Pew and NCHS offer many benchmark outcomes, but validation must be nested and grouped by domain to avoid mechanical calibration and item-level pseudo-replication [R166, R169].
5. **Cross-field benchmark selection is active.** R168 demonstrates that informative benchmark-subset selection and prediction of unobserved benchmark scores is itself an explicit current methodological problem.
6. **OF-30 therefore fails the first-project theory/novelty gate.** Its remaining contribution is best treated as a validation protocol/empirical note unless a new survey-specific identification structure appears.
7. **C011 remains unassigned.**

# V. Cross-field review-first reconnaissance

| ID | Citation / source | Type | What it establishes | Opportunity consequence | Stable locator |
|---|---|---:|---|---|---|
| R170 | Liu Y, Reiter JP. Synthetic Data: A Tool for Privacy Protection and Model Empowerment. *Annual Review of Statistics and Its Application*. Review in Advance. 2026. | RR | Current statistical review of synthetic data spanning privacy, usefulness and model reliability; explicitly identifies open challenges. | Confirms OF-36 is important but broad and active. | https://doi.org/10.1146/annurev-statistics-042925-122848 |
| R171 | Decruyenaere A, Polet C, Decruyenaere J, et al. Challenges of analyzing synthetic tabular data generated from 115 phase 3 oncology trials. *Scientific Reports*. 2026. | PP | Reanalyzes 128 comparisons from 115 oncology trials across 16 generators; naive deep-generative analyses can yield severe false-positive distortion and simple SE correction is insufficient in many deep-generator settings. | Strong failure evidence but also a high-competition active group for synthetic inference. | https://doi.org/10.1038/s41598-026-62212-z |
| R172 | Tan L, Zrnic T. Valid Inference with Synthetic Data via Task Exchangeability. arXiv:2606.13629. 2026. | PR | Introduces task exchangeability and validity guarantees for scientific inference using synthetic data calibrated with historical real/synthetic tasks. | Active-work threat to generic valid-synthetic-inference novelty. | https://arxiv.org/abs/2606.13629 |
| R173 | Mathur S, Si Y, Reiter JP. Fully Synthetic Data for Complex Surveys. *Survey Methodology*. 2024;50(2):347–373. | PP | Develops fully synthetic data generation for complex surveys with multiple-imputation combining rules and repeated-sampling evaluation. | Collapses a broad complex-survey-synthetic-inference opening. | https://www150.statcan.gc.ca/n1/pub/12-001-x/2024002/article/00008-eng.htm |
| R174 | Mátrai P, Kói T, Sipos Z, Farkas N. Assessing the properties of the prediction interval in random-effects meta-analysis. *Research Synthesis Methods*. 2026;17(3):517–537. | PP | Comprehensive simulation of frequentist random-effects PIs; shows mean nominal coverage can conceal an unfavorable distribution of coverage probabilities. | Motivates stronger-than-mean criteria but is not itself a gap claim. | https://doi.org/10.1017/rsm.2025.10055 |
| R175 | Brannick MT, French KA, Rothstein HR, Kiselica AM, Apostoloski N. Capturing the underlying distribution in meta-analysis: Credibility and tolerance intervals. *Research Synthesis Methods*. 2021;12(3):264–290. | PP | Adapts and evaluates content tolerance intervals for random-effects meta-analysis. | Classical-ancestor collapse for the broad high-confidence-content-coverage idea suggested by R174. | https://doi.org/10.1002/jrsm.1479 |
| R176 | Girardi P, Vesely A, Lakens D, et al. Post-selection Inference in Multiverse Analysis (PIMA): An Inferential Framework Based on the Sign Flipping Score Test. *Psychometrika*. 2024;89(2):542–568. | PP | Provides formal multiverse inference for broad GLM specifications with family-wise error control. | Generic “add inference to multiverse” contribution is occupied. | https://doi.org/10.1007/s11336-024-09973-6 |
| R177 | Nepomuceno A, Ghosal A, Sandoval Lentisco A, Ioannidis JPA. Uptake and Implementation of Multiverse-style Analyses Across 613 Studies. bioRxiv. 2026. | PR | Audits 613 implementations; formal inference, preregistration and explicit specification-defensibility checks are uncommon. | Leaves implementation/defensibility questions but not a broad formal-inference gap. | https://doi.org/10.64898/2026.07.15.738584 |
| R178 | Waghmare K, Ziegel JF. Proper Scoring Rules for Estimation and Forecast Evaluation. *Annual Review of Statistics and Its Application*. 2026;13:271–296. | RR | Current review of proper scoring rules for estimation and forecast evaluation. | Establishes a mature/active ancestor literature for evaluation-method proposals. | https://doi.org/10.1146/annurev-statistics-042424-050626 |
| R179 | Jonkers J, Van Wallendael G, Duchateau L, Van Hoecke S. Proper Scoring Rules for Right-Censored Survival Data. arXiv:2606.06393. 2026. | PR | Constructs proper observed-data scores for right censoring and reports ranking reversals for some plug-in weighted scores. | Direct ancestor for OF-35's ranking-reliability lens; interval-censoring-specific differentiation is mandatory. | https://arxiv.org/abs/2606.06393 |
| R180 | Lillelund CM, Qi S-a, Greiner R. Overcoming Dependent Censoring in the Evaluation of Survival Models. *Proceedings of UAI 2026*, PMLR 337:3841–3866. | PP | Shows standard IPCW Brier evaluation can fail under dependent censoring; proposes a dependent Brier score and a semi-synthetic known-event-time framework. | Strong nearest ancestor for observation-mechanism-induced evaluation failure and oracle comparison. | https://proceedings.mlr.press/v337/lillelund26a.html |
| R181 | Gómez Melis G, Oller R, Langohr K. Regression Models with Interval-Censored Variables. *Annual Review of Statistics and Its Application*. 2026;13:321–346. | RR | Current review of interval-censored regression, software, challenges and future directions. | Establishes interval censoring as an active, technically coherent statistics neighborhood. | https://doi.org/10.1146/annurev-statistics-042424-103337 |
| R182 | Wu Y, Cook RJ. Assessing the accuracy of predictive models with interval-censored data. *Biostatistics*. 2022;23(1):18–33. | PP | Develops imputation, IPW and AIPW estimators for prediction error/AUC using models for event, recurrent assessment and loss to follow-up. | Closest foundational direct prior art for OF-35; its simulation targets must be fully compared before promotion. | https://doi.org/10.1093/biostatistics/kxaa011 |
| R183 | Yang Z, Rizopoulos D, Newcomb LF, Erler NS. Time-Dependent Predictive Accuracy Metrics in the Context of Interval Censoring and Competing Risks. *Biometrical Journal*. 2026;68(1):e70108. | PP | Compares model-based and IPCW approaches for AUC, Brier score and EPCE under interval censoring/competing risks and studies misspecification/censoring patterns. | Very close 2026 nearest neighbor; OF-35 cannot merely compare existing metrics under misspecification. | https://doi.org/10.1002/bimj.70108 |
| R184 | Kim Y-J. Dynamic prediction of interval-censored failure time data with longitudinal marker. *Statistical Methods in Medical Research*. 2026;35(3). | PP | Develops dynamic predictive-accuracy measures with interval-censored failure times and longitudinal markers. | Confirms rapid expansion of interval-censored prediction evaluation beyond static settings. | https://doi.org/10.1177/09622802251412849 |
| R185 | Tseng Y-K, Wang T-L. Semiparametric brier score framework for evaluating prediction accuracy under interval censoring. EcoSta 2026, submission E1274. | CA | Proposes fixed/time-dependent interval-censored Brier estimators, Murphy decomposition, and extensions for sparse schedules, measurement error and incomplete covariate histories. | Immediate active-work threat; rules out simple Brier-score construction as OF-35 novelty. | https://www.cmstatistics.org/RegistrationsV2/EcoSta2026/viewSubmission.php?in=1274&token=08p4p6n3n1418opo0r533119q5319so7 |
| R186 | Anderson-Bergman C. icenReg: Regression Models for Interval Censored Data in R. *Journal of Statistical Software*. 2017;81(12). | SW/PP | Provides interval-censored regression, imputation, prediction, diagnostics, simulation and example datasets. | Feasibility substrate for bounded OF-35 simulation/prototyping. | https://doi.org/10.18637/jss.v081.i12 |
| R187 | Hudecová Š. Structure Assessment in Count Time Series. *Annual Review of Statistics and Its Application*. 2026;13:399–419. | RR | Reviews count-time-series models, goodness-of-fit tests and diagnostics. | Confirms a coherent alternative statistics field but no sharp first-project seam emerged in the bounded pass. | https://doi.org/10.1146/annurev-statistics-042424-114518 |
| R188 | Davis RA, Fernandes L. Sample splitting and assessing goodness-of-fit of time series. *Biometrika*. 2025;112(2):asaf017. | PP | Develops sample-splitting GOF tests for fitted time-series residual dependence. | Current methodological activity further reduces the appeal of a broad count/time-series diagnostic gap. | https://doi.org/10.1093/biomet/asaf017 |

# Pass-9 evidence synthesis — cross-field review-first reconnaissance

1. **The discovery-mode change works as a filter.** Starting from reviews and active methods exposed both viable conversations and false gaps before candidate creation.
2. **Synthetic-data inference is scientifically strong but high-velocity.** R170–R173 show simultaneous review, empirical-failure and validity-method activity; keep it on watchlist rather than first prosecution.
3. **The meta-analysis stronger-coverage idea collapses to a classical ancestor.** R174 motivates the concern, while R175 shows the natural content-coverage repair is established tolerance-interval methodology.
4. **Multiverse inference is not formally empty.** R176 occupies the broad method claim; R177 leaves a practice/defensibility gap rather than a clean first-method gap.
5. **Prediction evaluation under incomplete event observation is itself an inference problem.** R179–R185 show that score validity depends on censoring/assessment assumptions and that multiple interval-censored estimators are already active.
6. **OF-35 is therefore framed around ranking/decision reliability, not metric invention.** The unresolved question is whether observed-data evaluation procedures preserve the oracle ordering of competing models across interval-censoring/assessment regimes.
7. **Novelty is not established.** R182–R185 are close enough that full-text simulations and supplementary material must be prosecuted before C011 can be assigned.
8. **C011 remains unassigned.**

# Y. OF-35 bounded prosecution — direct ranking and informative-assessment threats

| ID | Citation / source | Type | What it establishes | Consequence for OF-35 | Stable locator |
|---|---|---:|---|---|---|
| R189 | Bahrini G, Razakarivony S, Dupuy J-F, Gares V, Barbet-Massin M. *When Can We Trust Survival Model Evaluation?* ICML 2026. | PP/CC | Controlled semi-synthetic survival-evaluation study with known true event times; compares standard censored-data evaluation with oracle `true_time` evaluation and explicitly studies metric distortion and preservation of model rankings across censoring rates/mechanisms. | Decisive conceptual direct neighbor: the broad oracle-ranking-reliability problem is already an active 2026 contribution under right censoring. Interval censoring needs genuinely new structure, not a censoring-type substitution. | https://openreview.net/forum?id=Y9gsOEdaNE |
| R190 | Yanagisawa H, Akiyama S. *A Strictly Proper Scoring Rule and a Calibration Metric for Interval-Censored Data Analysis.* ICML 2026. | PP/CA | Studies independent monitoring versus non-informative censoring; distinguishes Case-1 from Case-K; proposes a strictly proper interval-censored score under a constant-sum assumption and a calibration metric under non-informative censoring. | Occupies the theoretical scoring/monitoring-assumption frontier; OF-35 cannot claim interval-censored score validity or monitoring assumptions as unexplored. | https://icml.cc/Downloads/2026 |
| R191 | Cheng Y, Wang S, Wang C. Semiparametric model averaging prediction for case K informatively interval-censored data. *Applied Mathematical Modelling*. 2025;138(A):115758. | PP | Constructs candidate joint models for informative Case-K interval censoring; proposes semiparametric model averaging with asymptotically optimal weights and compares against model-selection/model-averaging alternatives. | Crowds the narrowed “model choice under informative interval censoring” escape route. | https://doi.org/10.1016/j.apm.2024.115758 |
| R192 | Du M, Zhao X. A conditional approach for regression analysis of case K interval-censored failure time data with informative censoring. *Computational Statistics & Data Analysis*. 2024;198:107991. | PP | Develops simultaneous variable selection/estimation under informative Case-K interval censoring and a framework that can assess the degree of informativeness. | Shows informative-assessment identification/model-selection structure is an active methods area rather than an empty residual seam. | https://doi.org/10.1016/j.csda.2024.107991 |
| R193 | Avati A, Duan T, Zhou S, Jung K, Shah NH, Ng AY. Countdown Regression: Sharp and Calibrated Survival Predictions. *Proceedings of Machine Learning Research*. 2020;115. | PP | Introduces Survival-CRPS variants for right- and interval-censored outcomes and frames censored survival evaluation through proper scoring rules. | Older ML ancestor showing interval-censored proper-score construction predates the current OF-35 framing; reinforces need for sharper claims. | https://proceedings.mlr.press/v115/avati20a.html |
| R194 | Sinha D, Chen M-H, Ghosh SK. Bayesian Analysis and Model Selection for Interval-Censored Survival Data. *Biometrics*. 1999;55(2):585–590. | PP | Develops Bayesian interval-censored survival models together with predictive-loss/CPO model-selection tools. | Classical ancestor: model comparison with interval-censored survival data is longstanding; OF-35 must concern evaluation-process reliability, not model selection in general. | https://doi.org/10.1111/j.0006-341X.1999.00585.x |

# Pass-10 evidence synthesis — OF-35 prosecution

1. **OF-35's broad novelty claim fails.** R189 directly studies oracle-versus-censored survival-model ranking preservation; R183 already supplies multiple interval-censored models plus exact-event oracle metrics and observed-data estimators.
2. **Wrong-winner probability is decision-relevant but derivative without additional theory.** It is a tail event of differential score-estimation error once oracle and observed scores for multiple models already exist.
3. **Interval censoring does contain distinct monitoring structure, but that frontier is active.** R190 studies Case-K monitoring assumptions and proper scoring; R191–R192 address informative Case-K model choice/inference.
4. **No toy simulation is needed to decide novelty.** The phenomenon and oracle design are already demonstrated in current work.
5. **OF-35 is parked; OF-38 is retained only as a theory-heavy sensitivity/partial-ranking watchlist.**
6. **C011 remains unassigned.**

# Z. D024 cross-field opportunity generation II — adaptive diagnostics and screened alternatives

| ID | Citation / source | Type | What it establishes | Consequence for D024 | Stable locator |
|---|---|---:|---|---|---|
| R195 | Hamilton I, Tawn N. Parameter Estimation in Comparative Judgment Under Random and Adaptive Scheduling Schemes. *Journal of Educational Measurement*. 2026;63(1):e70022. | PP | Shows adaptive comparison scheduling can substantially alter Bradley–Terry parameter-estimation behavior; identifies the realized adaptive schedule as non-ancillary and develops a schedule-replay parametric bootstrap for bias correction. | Direct OF-39 neighbor. The contribution cannot be “adaptive schedules bias BT estimates” or simply “use a replay bootstrap.” Diagnostic calibration must add a distinct validity result. | https://doi.org/10.1111/jedm.70022 |
| R196 | Wu W, Niezink N, Junker B. A Diagnostic Framework for the Bradley–Terry Model. *Journal of the Royal Statistical Society: Series A*. 2022;185(S2):S461–S484. | PP/SW | Develops overdispersion, object-level and subject-level diagnostics for Bradley–Terry models and provides reproducible implementation. | Supplies the exact diagnostic objects whose null calibration under outcome-adaptive comparison scheduling must be audited in OF-39. | https://doi.org/10.1111/rssa.12959 |
| R197 | Yi Y, Wang X. Goodness-of-fit test for response adaptive clinical trials. *Statistics & Probability Letters*. 2007;77(10):1014–1020. | PP | Extends goodness-of-fit/asymptotic likelihood methods to dependent data generated by response-adaptive clinical-trial designs. | Classical adjacent-mechanism ancestor. The generic claim that adaptive allocation complicates GOF inference is already old; OF-39 must exploit paired-comparison graph structure or a non-transferable diagnostic law. | https://ideas.repec.org/a/eee/stapro/v77y2007i10p1014-1020.html |
| R198 | Gao C, Shen Y, Zhang AY. Uncertainty quantification in the Bradley–Terry–Luce model. *Information and Inference*. 2023;12(2):1073–1140. | PP | Develops modern uncertainty-quantification theory for BTL models on sparse random comparison graphs. | Constrains broad BTL-UQ novelty claims and supplies a random-graph benchmark against which adaptive-graph arguments should be distinguished. | https://doi.org/10.1093/imaiai/iaac032 |
| R199 | Oduori G, Cocco C, Sajadi P, Pilla F. Data fusion for low-cost sensors: A systematic literature review. *Information Fusion*. 2026;131:104124. | SR | Reviews 82 low-cost-sensor fusion studies and highlights unresolved validation/generalizability practice, including risks from random validation when spatial/temporal dependence remains. | Motivates OF-40 but does not establish a new statistical gap because general correlated/geospatial CV theory already exists. | https://doi.org/10.1016/j.inffus.2026.104124 |
| R200 | Rabinowicz A, Rosset S. Cross-Validation for Correlated Data. *Journal of the American Statistical Association*. 2022;117(538):718–731. | PP | Derives when ordinary CV is suitable for correlated observations and proposes a bias-corrected CV estimator. | Strong ancestor for OF-40; “correlated spatial leakage makes CV optimistic” is not a new principle. | https://doi.org/10.1080/01621459.2020.1801451 |
| R201 | Wang J, Hopkins L, Hallman T, Robinson WD, Hutchinson R. Cross-validation for geospatial data: Estimating generalization performance in geostatistical problems. *Transactions on Machine Learning Research*. 2023. | PP/SW | Formalizes target-aware CV for geospatial prediction and studies when common CV procedures misestimate deployment performance. | Further narrows OF-40 to a source-availability/deployment estimand that must be genuinely distinct from existing geospatial CV targets. | https://github.com/Hutchinson-Lab/Cross-validation-for-Geospatial-Data |
| R202 | Zou R, Williamson BD, Shortreed SM, Coley RY. Validation of a Risk-Prediction Model in the Presence of Outcome Misclassification. *Statistics in Medicine*. 2026;45(8-9):e70377. | PP | Corrects common prediction-validation measures, including TPR, FPR, PPV, NPV and AUC, when observed binary outcomes are misclassified and a chart-review gold standard is available. | Collapses a broad “prediction validation under outcome misclassification” opening; OF-41 must address genuinely no-gold-standard probabilistic-performance identification. | https://doi.org/10.1002/sim.70377 |
| R203 | Molinari F. Partial identification of probability distributions with misclassified data. *Journal of Econometrics*. 2008;144(1):81–117. | PP | Provides sharp identification regions for broad distributional functionals under restrictions on misclassification. | Major classical ancestor for OF-41. Merely applying generic partial identification to another prediction metric is unlikely to clear the contribution gate. | https://doi.org/10.1016/j.jeconom.2007.12.003 |
| R204 | Obradović F. Measuring diagnostic test performance using imperfect reference tests: A partial identification approach. *Journal of Econometrics*. 2024;244(1):105842. | PP | Derives sharp bounds and inference for true sensitivity/specificity and related quantities when the reference test is itself imperfect. | Current partial-identification neighbor for validation without a perfect gold standard; raises the bar for OF-41. | https://doi.org/10.1016/j.jeconom.2024.105842 |
| R205 | Polo FM, Maity S, Yurochkin M, Banerjee M, Sun Y. Weak Supervision Performance Evaluation via Partial Identification. *NeurIPS*. 2024. | PP | Frames model-performance evaluation without ground-truth labels as a partial-identification problem and derives bounds for common classification metrics. | Direct abstract neighbor for OF-41; “evaluate without true labels using bounds” is already occupied. | https://proceedings.neurips.cc/paper_files/paper/2024 |
| R206 | Wei K, Wang L, Xia Y. Testing serial dependence or cross dependence for time series with underreporting. *Biometrika*. 2024;111(4):1293–1312. | PP | Shows ordinary dependence tests can have uncontrolled Type-I error under time-varying underreporting and develops underreporting-robust bootstrap tests. | Directly collapses the broad OF-42 problem sentence “reporting error makes diagnostics lie”; only a narrower full parametric GOF problem remains. | https://doi.org/10.1093/biomet/asae027 |
| R207 | Tang Y, Chen J, Li D, Wang HJ. Recent Advances in Conditional Extreme Quantile Analysis. *Annual Review of Statistics and Its Application*. 2026;13:297–319. | RR | Reviews contemporary conditional extreme-quantile methodology, including semiparametric/nonparametric and ML directions. | Establishes an active, technically demanding frontier for OF-43. | https://doi.org/10.1146/annurev-statistics-042324-014139 |
| R208 | Wei Y, Carroll RJ. Quantile Regression With Measurement Error. *Journal of the American Statistical Association*. 2009;104(487):1129–1143. | PP | Develops quantile-regression methodology correcting covariate measurement error. | Classical ancestor for OF-43; ordinary quantile × measurement-error methodology is not open. | https://doi.org/10.1198/jasa.2009.tm08420 |
| R209 | Chesher A. Understanding the effect of measurement error on quantile regressions. *Journal of Econometrics*. 2017;200(2):223–237. | PP | Characterizes how measurement error changes quantile-regression relationships. | Reinforces the mature measurement-error ancestor literature constraining OF-43. | https://doi.org/10.1016/j.jeconom.2017.06.007 |
| R210 | Kinnear G, Jones I, Davies B. Comparative judgement as a research tool: A meta-analysis of application and reliability. *Behavior Research Methods*. 2025;57:222. | SR/DS | Analyzes 101 comparative-judgment datasets collected from prior studies and releases underlying comparison materials/code; documents broad variation in study design. | Provides a feasible empirical substrate and practice context for OF-39, although each dataset's scheduling regime must be verified before use. | https://doi.org/10.3758/s13428-025-02744-w |
| R211 | Comparative Judgement Research Consortium. CJ RAVE Dataset. 2026. | DS | Public contemporary comparative-judgment data with item-level pairwise comparisons and Bradley–Terry-style analysis context. | Possible empirical substrate for OF-39 only after confirming whether/how comparisons were scheduled adaptively. | https://cjrc.co.uk/cj_rave.html |
| R212 | Shanmugam D, Sadhuka S, Raghavan M, Guttag J, Berger B, Pierson E. Evaluating multiple models using labeled and unlabeled data. *NeurIPS*. 2025. | PP | Develops semi-supervised multi-model evaluation that can estimate broad performance functionals, including calibration-related metrics, under its assumptions. | Further crowds generic no-gold-standard evaluation claims in OF-41. | https://proceedings.neurips.cc/ |

| R213 | Glickman ME, Jensen ST. Adaptive paired comparison design. *Journal of Statistical Planning and Inference*. 2005;127(1–2):279–293. | PP | Develops adaptive paired-comparison scheduling using Bayesian optimal design, including Swiss-style tournament comparisons. | Establishes that outcome-informed paired-comparison design itself is classical; OF-39 novelty must be diagnostic calibration, not adaptive pairing. | https://doi.org/10.1016/j.jspi.2003.09.022 |
| R214 | Farrington CP. On Assessing Goodness of Fit of Generalized Linear Models to Sparse Data. *Journal of the Royal Statistical Society: Series B*. 1996;58(2):349–360. | PP | Derives moment corrections/modifications for Pearson GOF under sparse GLM covariate patterns. | Major confound for OF-39 simulation claims: sparse pair cells can miscalibrate Pearson references even without adaptive endogeneity. | https://doi.org/10.1111/j.2517-6161.1996.tb02086.x |
| R215 | Lin L, Khamaru K, Wainwright MJ. Semiparametric Inference Based on Adaptively Collected Data. *Annals of Statistics*. 2025;53(3):989–1014. | PP | Shows that adaptive collection can alter standard estimator asymptotics and develops weighted estimating equations with exploration conditions for asymptotic normality. | Constrains broad OF-39 claims and reinforces the need to state exactly which adaptive law/reference is being calibrated. | https://doi.org/10.1214/24-AOS2485 |
| R216 | Deshpande Y, Mackey L, Syrgkanis V, Taddy M. Accurate Inference for Adaptive Linear Models. *ICML*. 2018;PMLR 80:1194–1203. | PP | Demonstrates persistent inferential distortions under adaptively collected regression data and develops martingale-based correction. | Abstract ancestor for adaptive-inference failure/correction; OF-39 must exploit paired-comparison diagnostic structure rather than claim the generic phenomenon. | https://proceedings.mlr.press/v80/deshpande18a.html |

# Pass-12 evidence synthesis — OF-39 adaptive diagnostic prosecution

1. **Broad asymptotic invalidity does not survive.** Under the Bradley–Terry null with predictable scheduling, score/residual increments are martingale differences; R197 and R215 make standard asymptotic recovery plausible under exploration/repetition.
2. **A finite-sample conditional-calibration seam survives.** R195 establishes that the completed adaptive schedule is non-ancillary. A frozen-final-graph bootstrap therefore need not reproduce the conditional experiment generated by the scheduler.
3. **Sparse GOF is a separate major threat.** R214 shows that Pearson reference behavior can fail under sparse covariate patterns without any adaptive endogeneity. Freeze-versus-replay controls are required.
4. **Bounded simulation supports the seam, not a paper claim.** Adaptive-versus-frozen designs with identical graph topology produced materially different tails, and scheduler replay was closer to nominal than freezing the final schedule.
5. **Replay is not itself novel.** R195 already embeds the adaptive scheduler in a parametric bootstrap for estimation. OF-39 requires a new validity theorem/conditional-law result and useful diagnostic power.
6. **C011 remains unassigned.** The next gate is exact small-state enumeration of `Law(outcomes, graph)` and a proof-level comparison of fixed-graph versus joint/replay diagnostic calibration.

# Pass-11 evidence synthesis — D024 cross-field opportunity generation II

1. **OF-39 is the only lead that earns a bounded prosecution.** Hamilton & Tawn [R195] establish outcome-adaptive scheduling as non-ancillary for Bradley–Terry estimation, while Wu et al. [R196] supply a diagnostic framework whose calibration under that scheduling regime was not found in the bounded search.
2. **The generic principle is not new.** Yi & Wang [R197] already treat goodness-of-fit under response-adaptive allocation. OF-39 survives only as a paired-comparison specialization whose adaptive graph may alter the diagnostic reference law in a nontrivial way.
3. **OF-40 is watchlist only.** Current sensor-fusion reviews identify weak validation practice [R199], but correlated/geospatial CV theory [R200–R201] already occupies the broad leakage/generalization problem.
4. **OF-41 is theory-heavy and ancestor-threatened.** Outcome-misclassification validation [R202], general misclassification partial identification [R203], imperfect-reference bounds [R204] and weak-supervision evaluation [R205, R212] leave only a narrow probabilistic-score/calibration identification question.
5. **OF-42 is parked in broad form.** Underreporting-induced diagnostic distortion and robust dependence testing are already direct contributions [R206].
6. **OF-43 is theory-heavy.** Conditional extremes are active [R207] and quantile measurement-error correction is mature [R208–R209].
7. **C011 remains unassigned.** OF-39 is a pre-candidate prosecution lead, not an approved candidate or execution project.

# AA. OF-39 exact-enumeration theorem gate — direct 2026 diagnostic pressure

| ID | Reference | Type | Key contribution | Relevance / novelty implication | Link |
|---|---|---|---|---|---|
| R217 | Singh R, Davidov O. Testing for lack of fit in paired comparison data. arXiv:2604.00426. 2026. | PP/preprint | Develops lack-of-fit tests for paired-comparison graphs across fixed-item, unbalanced and sparse/high-dimensional regimes, including null/alternative theory and detectability results; discusses extension toward binary paired comparisons. | Does not address outcome-adaptive scheduling directly, but increases competition around OF-39's secondary diagnostic-power/detectability axis and reinforces that graph-specific lack-of-fit theory is active in 2026. | https://arxiv.org/abs/2604.00426 |

| R218 | Patten HW, Bhaby Z. Disasters, Statistics, and the Humanitarian Sector. Annual Review of Statistics and Its Application. 2026;13:51–73. | SR/review | Current review of humanitarian statistics emphasizing data gaps/biases, dynamic population data, aid allocation and decision use. | Review-first trigger for population/frame reliability ideas; supports importance but not novelty. | https://www.annualreviews.org/content/journals/10.1146/annurev-statistics-042424-061122 |
| R219 | Thomson DR, Rhoda DA, Tatem AJ, Castro MC. Gridded population survey sampling: a systematic scoping review of the field and strategic research agenda. Int J Health Geogr. 2020;19:34. | SR | Reviews 43 gridded-population surveys in 29 LMICs and explicitly identifies cell-level population accuracy/uncertainty and use of uncertainty in sample design as research needs. | Generates the modeled-population-frame seam, but does not establish that the underlying survey-sampling object is new. | https://doi.org/10.1186/s12942-020-00230-4 |
| R220 | Powers RK, Eltinge JL. Effects of Imperfect Unit Size Information on Complex Sample Designs and Estimators. U.S. Bureau of Labor Statistics, 2014. | GR/method | Studies PPS and other complex designs when size measures are imperfect approximations to ideal measures. | Classical/adjacent ancestor that collapses a broad claim that uncertain modeled population counts create a new PPS problem. | https://www.bls.gov/osmr/research-papers/2014/st140070.htm |
| R221 | Powers RK, Eltinge JL. Properties of Some Sample Designs Based on Imperfect Frame Information. U.S. Bureau of Labor Statistics, 2013. | GR/method | Studies sample-design properties when frame auxiliary information/size measures contain error or are missing. | Reinforces that imperfect frame/MOS reliability is an established survey-sampling object. | https://www.bls.gov/osmr/research-papers/2013/st130180.htm |
| R222 | U.S. OMB / U.S. Census Bureau. The 2024 Statistical Policy Directive No. 15. Current official page, revised Apr 7 2026. | GD/official | Defines the revised federal race/ethnicity standard, including combined collection and seven minimum categories with MENA. | Establishes the live standards transition and comparability context for OF-44. | https://spd15revision.gov/content/spd15revision/en/2024-spd15.html |
| R223 | Federal Interagency Technical Working Group on Race and Ethnicity Standards. Bridging Data Tools. Current official page, revised Apr 7 2026. | GD/SW | Publishes 1997↔2024 bridge factors, programs and examples; explicitly calls the current program initial/basic and anticipates more robust methods as data accrue. | Direct evidence that bridge reliability is a live implementation/research issue; also supplies public feasibility inputs. | https://spd15revision.gov/content/spd15revision/en/data-tools.html |
| R224 | Census Scientific Advisory Committee / U.S. Census Bureau. Recommendations and Comments from the Fall 2024 Meeting and Census Bureau Responses. Dec 9 2024. | GD/official | Flags national-vs-subnational bridge limitations, possible age/nativity/time heterogeneity, lack of an ideal simultaneous dual-format survey, linked-data limitations, and small-factor/small-area issues; Census is exploring alternative methods. | Strongest official problem statement for OF-44, but also a competition warning because Census Phase-2/alternative work is active. | https://www2.census.gov/about/partners/cac/sac/meetings/2024-09/csac-fall-2024-recommendations.pdf |
| R225 | Arias E, Liebler CA, Garcia MA, Sáenz R. Data impacts of changes in U.S. Census Bureau procedures for race and ethnicity data. SSM Popul Health. 2025;29:101742. | PP | Finds major discontinuities affecting demographic, socioeconomic and mortality statistics after Census race/ethnicity procedural changes. | Establishes downstream consequentiality and motivates trend/rate reliability rather than bridge construction alone. | https://doi.org/10.1016/j.ssmph.2024.101742 |
| R226 | Parker JD, Schenker N, Ingram DD, Weed JA, Heck KE, Madans JH. Bridging between two standards for collecting information on race and ethnicity: an application to Census 2000 and vital rates. Public Health Rep. 2004;119(2):192–205. | PP | Regression-based prior federal race bridging; allocation probabilities vary with demographic/geographic covariates and resulting death rates are compared across bridge methods. | Classical direct ancestor blocking generic bridge/modeled-heterogeneity novelty for OF-44. | https://pmc.ncbi.nlm.nih.gov/articles/PMC1497618/ |
| R227 | Chu H, Wang Z, Cole SR, Greenland S. Sensitivity analysis of misclassification: a graphical and a Bayesian approach. Ann Epidemiol. 2006;16(11):834–841. | PP/method | Incorporates uncertainty in misclassification parameters into probabilistic/Bayesian inference. | Blocks generic “propagate bridge-factor uncertainty” novelty; OF-44 must add a distinct downstream robustness/decision object. | https://pubmed.ncbi.nlm.nih.gov/16843678/ |
| R228 | Molinari F. Partial identification of probability distributions with misclassified data. Journal of Econometrics. 2008;144(1):81–117. | PP/method | Represents discrete misclassification as a linear system with a misclassification-probability matrix; permits general restrictions on that matrix and derives sharp identification regions for real functionals, with extensions to outcomes and conditioning covariates. | Direct theorem-level ancestor for OF-44: constrained heterogeneous bridge matrices plus sharp downstream functional regions are generically covered unless additional structure changes the problem. | https://doi.org/10.1016/j.jeconom.2007.12.003 |
| R229 | Rosenbaum WL, Sterling TD, Weinkam JJ. Correcting standardized rate ratios for imprecise classification of a polychotomous exposure variable with limited data. Am J Epidemiol. 1995;142(4):442–445. | PP/method | Shows standardized rate ratios can be corrected from published summary risk ratios plus a polychotomous misclassification matrix. | Blocks the claim that downstream rate-ratio correction under a categorical bridge matrix is itself new. | https://pubmed.ncbi.nlm.nih.gov/7625410/ |
| R230 | Harth K, et al. 2016 American Community Survey Content Test Evaluation Report: Race and Hispanic Origin. U.S. Census Bureau. 2017. | GD/official | Public report compares race/ethnicity distributions under separate versus combined question formats and documents aggregate format effects. | Provides a reproducible aggregate sensitivity signal for OF-44, but not a same-person stratum-specific transition matrix adequate to identify geography/nativity/time bridge heterogeneity. | https://www.census.gov/content/dam/Census/library/working-papers/2017/acs/2017_Harth_01.pdf |
| R231 | Coley RY, Walker RL, Cruz M, Simon GE, Shortreed SM. Clinical risk prediction models and informative cluster size: Assessing the performance of a suicide risk prediction algorithm. *Biometrical Journal*. 2021;63(7):1375–1388. | PP/method | Compares visit- versus person-level train/test splitting and cross-validation for clustered clinical prediction against a prospective validation set when cluster size is informative. | Directly occupies the proposed informative-cluster-size × prediction-validation problem sentence. | https://doi.org/10.1002/bimj.202000199 |
| R232 | Pavlou M, Ambler G, Omar RZ. Risk prediction in multicentre studies when there is confounding by cluster or informative cluster size. *BMC Medical Research Methodology*. 2021;21:135. | PP/method | Studies prediction performance, calibration/discrimination and modeling choices under confounding by cluster and informative cluster size. | Confirms the reliability object is already prediction-specific, not merely a generic clustered-data ancestor. | https://doi.org/10.1186/s12874-021-01321-x |
| R233 | Kanukula R, Page MJ, Turner SL, McKenzie JE. Identification of application and interpretation errors that can occur in pairwise meta-analyses in systematic reviews of interventions: a systematic review. *Journal of Clinical Epidemiology*. 2024;170:111331. | SR | Identifies 139 meta-analysis errors, including data extraction/manipulation, statistical analysis and interpretation errors. | Direct review-first evidence that the extraction-to-analysis failure space is already explicitly mapped. | https://doi.org/10.1016/j.jclinepi.2024.111331 |
| R234 | Xu C, Yu T, Furuya-Kanamori L, et al. Validity of data extraction in evidence synthesis practice of adverse events: reproducibility study. *BMJ*. 2022;377:e069155. | PP/meta-research | Re-extracts adverse-event data and quantifies how extraction errors alter meta-analytic results and conclusions. | Blocks a generic claim that downstream consequence of extraction error is an unstudied object. | https://doi.org/10.1136/bmj-2021-069155 |
| R235 | Atal I, Porcher R, Boutron I, Ravaud P. The statistical significance of meta-analyses is frequently fragile: definition of a fragility index for meta-analyses. *Journal of Clinical Epidemiology*. 2019;111:32–40. | PP/method | Defines a meta-analysis fragility index based on the minimum event-status changes needed to reverse pooled statistical significance. | Strong ancestor for extraction-error tipping/robustness proposals based only on small data perturbations. | https://doi.org/10.1016/j.jclinepi.2019.03.012 |
| R236 | Peterson EN, Nethery RC, Chen JT, Tabb LP, Coull BA, Piel FB, Waller LA. A Bayesian spatial measurement error approach to incorporate heterogeneous population-at-risk uncertainty in estimating small-area opioid mortality rates. *Spatial and Spatio-temporal Epidemiology*. 2025;53:100719. | PP/method | Models heterogeneous uncertainty in population-at-risk denominators using spatial classical/Berkson measurement-error approaches. | Directly occupies the broad denominator-uncertainty × small-area-rate reliability seam. | https://doi.org/10.1016/j.sste.2025.100719 |
| R237 | Nethery RC, Rushovich T, Peterson E, et al. Comparing denominator sources for real-time disease incidence modeling: American Community Survey and WorldPop. *SSM - Population Health*. 2021;14:100786. | PP | Compares denominator sources via simulation and real data and quantifies bias in small-area disparity estimates. | Shows downstream disparity consequences of denominator choice are already empirically explicit. | https://doi.org/10.1016/j.ssmph.2021.100786 |
| R238 | Awounvo S, Kieser M, Feißt M. Combining multiple imputation with internal model validation in clinical prediction modeling: a systematic methodological review. *Journal of Clinical Epidemiology*. 2025;186:111916. | SR/method | Reviews how multiple imputation is ordered relative to internal validation and the complexity/accuracy trade-offs of MI-prior-IMV versus MI-during-IMV. | Directly names the proposed imputation × validation-order reliability problem. | https://doi.org/10.1016/j.jclinepi.2025.111916 |
| R239 | Wahl S, Boulesteix AL, Zierer A, Thorand B, van de Wiel MA. Assessment of predictive performance in incomplete data by combining internal validation and multiple imputation. *BMC Medical Research Methodology*. 2016;16:144. | PP/method | Simulation study comparing strategies for combining validation and multiple imputation; documents optimistic bias for some orderings. | Classical/direct method ancestor blocking a generic “imputation leakage” opportunity. | https://doi.org/10.1186/s12874-016-0239-7 |
| R240 | Celis LE, Huang L, Keswani V, Vishnoi NK. Fair Classification with Noisy Protected Attributes: A Framework with Provable Guarantees. *ICML / PMLR*. 2021;139:1349–1361. | PP/method | Develops fair classification with accuracy/fairness guarantees when protected attributes are noisy, for broad fairness constraints and multiple groups. | Direct occupation of noisy protected-attribute fairness reliability. | https://proceedings.mlr.press/v139/celis21a.html |
| R241 | Wu M, Lin L, Zhang W, Wang X, Yang Z, Hu S. Preserving AUC Fairness in Learning with Noisy Protected Groups. *ICML / PMLR*. 2025;267:67427–67448. | PP/method | Develops distributionally robust AUC fairness with theoretical guarantees under noisy protected groups. | Demonstrates current competition on a narrower metric-specific version of the same object. | https://proceedings.mlr.press/v267/wu25q.html |
| R242 | Shankar R, Lim A, Qian X. Performance of large language models in data extraction for evidence synthesis: A systematic review. *Journal of Biomedical Informatics*. 2026;181:105086. | SR | Reviews accuracy, reliability and efficiency of LLM-based extraction for evidence synthesis. | Current review-first evidence that AI extraction reliability is already a mature active research conversation. | https://doi.org/10.1016/j.jbi.2026.105086 |
| R243 | Gartlehner G, Kugley S, Crotty K, et al. Artificial Intelligence-Assisted Data Extraction With a Large Language Model: A Study Within Reviews. *Annals of Internal Medicine*. 2025;178(12):1763–1771. | PP/meta-research | Evaluates AI-assisted versus human extraction across reviews and quantifies extraction errors. | Direct empirical occupation of the error-characterization component of an AI-evidence-synthesis reliability proposal. | https://doi.org/10.7326/ANNALS-25-00739 |
| R244 | Boudourides M. End-to-End Error Propagation in AI-Assisted Evidence Synthesis: An Empirical Evaluation Across 20 Case Studies. SSRN preprint. Posted 2026-08-26. | PP/preprint | Explicitly evaluates propagation from AI-assisted evidence-synthesis errors into pooled effect sizes and heterogeneity across 20 cases. | Exact active-work threat to an end-to-end error-propagation opportunity; unfavorable first-project competition geometry. | https://doi.org/10.2139/ssrn.7346302 |
| R245 | Marzi C, Giannelli M, Barucci A, et al. Efficacy of MRI data harmonization in the age of machine learning: a multicenter study across 36 datasets. *Scientific Data*. 2024;11:115. | PP/method | Demonstrates leakage when harmonization is fitted to the full dataset before ML splitting and implements a pipeline-safe harmonizer transformer. | Directly occupies the harmonization × validation-leakage problem sentence. | https://doi.org/10.1038/s41597-023-02421-7 |
| R246 | Nieto N, et al. Impact of leakage on data harmonization in machine learning pipelines in class imbalance across sites. *Neurocomputing*. 2026;680:133146. | PP/method | Studies target/test-label leakage under cross-site class imbalance and proposes leakage-free harmonization. | Confirms the harmonization leakage seam remains active and highly occupied in 2026. | https://doi.org/10.1016/j.neucom.2026.133146 |

# Pass-13 evidence synthesis — OF-39 exact theorem gate

1. Exact four-object enumeration proves that an outcome-generated final comparison graph can truncate the Bradley–Terry null path space; frozen-final-graph resampling can therefore be wrong even with known parameters and exact finite-sample references.
2. Hamilton & Tawn [R195] already supply the central causal fact for this theorem: later adaptive comparisons are non-ancillary, and their parametric bootstrap replays the scheduler while preserving only ancillary scheduling components.
3. The exact truncation formula is therefore a direct finite-state consequence of R195 rather than an independently difficult Bradley–Terry diagnostic theorem.
4. Exact replay validity with known parameters is a generic identical-null-experiment result. Substituting Wu et al.'s diagnostics [R196] into that replay principle does not clear L055.
5. Yi & Wang [R197] continues to block the broad claim that adaptive-design GOF itself is new.
6. R217 adds current pressure on the alternative power/detectability branch, though it does not directly cover adaptive schedules.
7. **Disposition:** park OF-39; C011 remains unassigned.


# Pass-14 evidence synthesis — D027 review-first generation III

1. A current humanitarian-statistics review [R218] and gridded-population survey review [R219] expose a practical modeled-frame uncertainty problem, but imperfect frame/measure-of-size sampling is already a classical methodological object [R220–R221]. The broad lead is collapsed before registration.
2. The live 1997↔2024 SPD-15 transition is unusually well documented as a reliability problem: official tools are explicitly initial/basic [R223], and Census advisory material specifies geography/age/time heterogeneity, validation limitations and small-factor problems [R224].
3. Consequentiality is real: recent work shows race/ethnicity procedural discontinuities can alter mortality and other statistics [R225].
4. Generic bridge construction is not new [R226], and generic uncertainty propagation through misclassification parameters is not new [R227].
5. The only surviving object is therefore **downstream decision robustness under bridge heterogeneity** — sign/ranking/trend invariance, tipping conditions or sharp sensitivity regions — with a strict public-data and nearest-neighbor gate.
6. **Disposition:** register OF-44 as PRIORITY BOUNDED SCREENING only; keep C011 unassigned.


# Pass-15 evidence synthesis — OF-44 bounded screening

1. Molinari [R228] is the decisive theorem-level nearest neighbor: generic restricted misclassification matrices already yield sharp identification regions for arbitrary real functionals, including conditional/outcome extensions.
2. Rosenbaum et al. [R229] provides direct downstream rate-ratio matrix-method ancestry for polychotomous classification error.
3. Public Phase-1 bridge factors/code remain reproducible [R223], but official Census material still treats subnational/nativity/time heterogeneity as unresolved and relies on linked 2015 NCT↔2020 Census evidence unavailable as an ideal public simultaneous dual-format substrate [R224].
4. Public content-test reporting [R230] can inform aggregate stress tests but does not identify the required heterogeneous transition matrices.
5. **Disposition:** P1 FAIL; P2 PARTIAL/INSUFFICIENT; stop P3/P4; park OF-44 and keep C011 unassigned.


# Pass-16 evidence synthesis — D029 review-first generation IV

1. Informative cluster size is already tied directly to clinical prediction splitting, cross-validation and prospective performance [R231–R232]; no generic validation-estimand opportunity survives.
2. Meta-analysis extraction/application errors already have a systematic error taxonomy, empirical downstream correction evidence and fragility machinery [R233–R235].
3. Population-denominator uncertainty is directly represented by modern spatial measurement-error models and denominator-source bias studies [R236–R237].
4. Multiple-imputation/internal-validation ordering is already an explicit methodological question with both a current systematic review and older simulation evidence [R238–R239].
5. Noisy protected attributes are an established fairness-theory object, including current AUC-specific robust methods [R240–R241].
6. LLM evidence-synthesis extraction reliability is highly active, and an August 2026 preprint already states the exact end-to-end error-propagation problem [R242–R244].
7. Harmonization-before-splitting leakage is already directly demonstrated and has leakage-safe pipeline methods, with further 2026 work under cross-site imbalance [R245–R246].
8. **Disposition:** valid null generation pass. Create no new OF number; keep C011 unassigned. Diversify the next review-first pass away from repeatedly sampled biomedical prediction/evidence-synthesis/harmonization neighborhoods.

# W. D030 diversified review-first reconnaissance

| ID | Citation / source | Type | What it establishes | D030 consequence | Stable locator |
|---|---|---:|---|---|---|
| R247 | UNECE HLG-MOS RAMSES Project. *HLG-MOS Handbook on Multi-Source Statistics*. 2026. | TR/guidance | States that quality management for multi-source statistics must shift from assessing individual datasets to ensuring quality across entire integrated systems. | Strong direct occupation of generic system-level quality propagation in official statistics. | https://unece.org/statistics/documents/2026/03/reports/hlg-mos-handbook-multi-source-statistics |
| R248 | National Academies of Sciences, Engineering, and Medicine. *Federal Statistics, Multiple Data Sources, and Privacy Protection: Next Steps*, Ch. 6 “Quality Frameworks for Statistics Using Multiple Data Sources.” 2017. | TR/consensus | Develops quality frameworks for federal statistics built from multiple administrative/private-sector sources, including linkage error and fitness-for-use concerns. | Classical/institutional ancestor for multi-source quality propagation. | https://doi.org/10.17226/24893 |
| R249 | Office for National Statistics. *ONS Working Paper Series No. 19 — An error framework for longitudinal administrative sources; its use for understanding the statistical properties of data for international migration.* | TR/method | Defines single- and multiple-source error frameworks across target/source/linked/aligned/processed data and uses them to inform integrated statistical-system design. | Further collapses a generic multi-source error-propagation opportunity. | https://www.ons.gov.uk/methodology/methodologicalpublications/generalmethodology/onsworkingpaperseries/onsworkingpaperseriesno19anerrorframeworkforlongitudinaladministrativesourcesitsuseforunderstandingthestatisticalpropertiesofdataforinternationalmigration |
| R250 | Mei H, Xu X, Yang H, Wang F, Li Y. A practical review of response-adaptive randomization: Under-explored challenges and potential directions. *Statistical Methods in Medical Research*. 2026. | SR | Reviews RAR implementation and explicitly names repeated outcomes, missing data and related practical inferential challenges. | Shows the adaptive-design imperfection seam is already an explicit active research program. | https://doi.org/10.1177/09622802261427330 |
| R251 | Tao Y, Zhang L-X. Statistical Inference for Covariate-Adaptive Randomization Procedures With Missing Covariates. *Statistics in Medicine*. 2026;45:e70697. | PP/method | Establishes testing theory for covariate-adaptive randomization with imputed missing covariates and correction of conservative tests. | Direct 2026 occupation of an adaptive-randomization × missing-covariate seam. | https://doi.org/10.1002/sim.70697 |
| R252 | Robertson DS, Lee KM, López-Kolkovska BC, Villar SS. Response-adaptive randomization in clinical trials: from myths to practical considerations. 2023. | SR/method | Explicitly discusses measurement/classification error and missing data under RAR and cites existing misclassification-specific allocation work. | Demonstrates that feedback from imperfect outcomes into adaptive allocation is already named and partly developed. | https://pmc.ncbi.nlm.nih.gov/articles/PMC7614644/ |
| R253 | Wang Y. Hidden Decisions in Statistical Software: How Default Settings and Implementation Choices Undermine Reproducibility. *The American Statistician*. Accepted 2026-08-27; accepted manuscript posted 2026-09-03. | PP/AW | Catalogs 37 hidden cross-package implementation/default decisions and demonstrates significance reversals on boundary datasets. | Exact active-work occupation of software-implementation decision reliability. | https://doi.org/10.1080/00031305.2026.2729003 |
| R254 | McCullough BD. Assessing the Reliability of Statistical Software: Part I. *The American Statistician*. 1998;52(4):358–366. | PP/classical | Proposes intermediate-level benchmark tests for estimation, random-number generation and statistical distributions. | Classical ancestor blocks novelty claims based on generic statistical-software reliability testing. | https://doi.org/10.1080/00031305.1998.10480597 |
| R255 | Altman M, Gill J, McDonald MP. accuracy: Tools for Accurate and Reliable Statistical Computing. *Journal of Statistical Software*. 2007;21(1). | PP/software | Provides tools/frameworks for computational stability, numerical/measurement error and model-result comparison. | Further classical occupation of model-result numerical-stability diagnostics. | https://doi.org/10.18637/jss.v021.i01 |
| R256 | Wadoux AMJ-C, Heuvelink GBM. Uncertainty of spatial averages and totals of natural resource maps. *Methods in Ecology and Evolution*. 2023. | PP/method | Shows spatial autocorrelation of map errors is essential for aggregate uncertainty and proposes scalable Monte Carlo integration for spatial averages/totals. | Directly occupies the methodological repair for correlated-error uncertainty of spatial aggregates. | https://doi.org/10.1111/2041-210X.14106 |
| R257 | Wadoux AMJ-C, Heuvelink GBM. Scientists yet to consider spatial correlation in assessing uncertainty of spatial averages and totals. *International Journal of Applied Earth Observation and Geoinformation*. 2025;139:104472. | PP/commentary | Documents persistent incorrect aggregate-uncertainty practice while explicitly stating that methods exist to account for spatial dependence. | Reclassifies the apparent gap mainly as uptake/implementation rather than method invention. | https://doi.org/10.1016/j.jag.2025.104472 |
| R258 | Tomova GD, Silverwood RJ, Wright L. Mode effects on survey item measurement: a systematic review of the experimental evidence. *Survey Futures Working Paper Series* 12. 2026-01-15. | SR | Finds fragmented mode-effect evidence and notes that suitable adjustment methods are underused because they often need external evidence on mode-effect magnitude. | Initially exposes a plausible partial-information reliability seam. | https://www.iser.essex.ac.uk/research/publications/working-papers/survey-futures/12 |
| R259 | Wright L, et al. How can the use of different modes of survey data collection introduce bias? An introduction to mode effects using directed acyclic graphs (DAGs). *American Journal of Epidemiology*. 2026;195(5):1406–1415. | PP/method | Separates mode effects from mode selection, shows naïve conditioning can induce collider bias, and advocates quantitative bias analysis. | Strong direct active-work pressure on the mixed-mode partial-information seam. | https://doi.org/10.1093/aje/kwag017 |
| R260 | Wright L, Tomova GD, Brown M, Tsigaridis K, Henderson M, Silverwood RJ. Experimental evidence on the effect of mixed-mode survey designs on item measurement and variable correlations. *Survey Futures Working Paper Series* 27. 2026-08-01. | PP/AW | Randomized mixed-mode evidence on item measurements and variable correlations. | Confirms the same group is actively extending the exact review-generated seam in 2026. | https://www.iser.essex.ac.uk/research/publications/working-papers/survey-futures/27 |

# Pass-17 evidence synthesis — D030 diversified review-first reconnaissance

1. **Official statistics:** integrated multi-source quality is already an explicit system-level object in current UNECE guidance and older NASEM/ONS error frameworks [R247–R249].
2. **Experimental design:** missingness/mismeasurement under adaptive randomization is directly named, partly developed, and active in 2026 [R250–R252].
3. **Statistical computing:** cross-software implementation/default decisions causing inferential reversals are directly demonstrated in September 2026, with mature software-reliability ancestors [R253–R255].
4. **Environmental/spatial:** spatial-correlation-aware uncertainty of map averages/totals already has a dedicated scalable method; the current residual is largely failure of uptake [R256–R257].
5. **Social-science measurement:** the mixed-mode external-evidence gap from a January 2026 review is already being prosecuted by the same active group through DAG/QBA and randomized association studies [R258–R260].
6. **Disposition:** second valid null generation pass. No OF-45; C011 remains unassigned.
7. **Search-strategy consequence:** do not answer the null by sampling more review fields. Per L027/L038, switch to independent theory/data/decision discovery channels and require convergence before opportunity registration.

# X. D031 independent-channel triangulation and OF-45 bounded prosecution lead

| ID | Citation / source | Type | What it establishes | D031 consequence | Stable locator |
|---|---|---|---|---|---|
| R261 | U.S. EPA. *Multiyear Tile Plot — Exceptional Events Analysis*. Updated 2026-03-25. | AG | Recent AirNow observations are not fully verified/validated and are replaced by AQS data when available. | Establishes a real provisional→quality-assured data-state workflow, but not novelty. | https://www.epa.gov/air-quality-analysis/multiyear-tile-plot-exceptional-events-analysis |
| R262 | Croushore D, Stark T. A Real-Time Data Set for Macroeconomists: Does the Data Vintage Matter? *Review of Economics and Statistics*. 2003;85(3):605–617. | PP/classical | Shows revisions/data vintages can change econometric results, policy analysis and forecasts. | Collapses the generic “evaluate on final data although decisions used provisional data” object against mature vintage-data ancestry. | https://doi.org/10.1162/003465303322369759 |
| R263 | *Navigating duplication in pharmacovigilance databases: a scoping review*. 2024. | SR | Synthesizes duplicate-report prevalence, consequences and deduplication methods across pharmacovigilance databases. | Direct occupation of the generic FAERS duplicate-reliability problem. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11086478/ |
| R264 | Kreimeyer K, Spiker J, Dang O, De S, Ball R, Botsis T. Deduplicating the FDA adverse event reporting system with a novel application of network-based grouping. *Journal of Biomedical Informatics*. 2025;165:104824. | PP/AW | Full-database FAERS deduplication pipeline, evaluated on expert-adjudicated sets and operating at FDA. | Kills FAERS deduplication as a first-project lead under current active-work competition. | https://doi.org/10.1016/j.jbi.2025.104824 |
| R265 | Centers for Medicare & Medicaid Services. *Overall Hospital Quality Star Rating — Comprehensive Methodology v5.0 / April 2026*. | AG | Ratings use available measure groups, redistribute weights, apply minimum thresholds and peer groups based on 3/4/5 groups. | Makes missing-measure/peer-group reliability an explicit current methodology object. | https://data.cms.gov/provider-data/topics/hospitals/overall-hospital-quality-star-rating/ |
| R266 | American Hospital Association / KNG Health. *Understanding CMS' Changes to Hospital Overall Star Ratings*. 2022. | PR/evaluation | Reports remaining volatility for hospitals with fewer measures, especially smaller/rural/critical-access hospitals. | Direct empirical occupation of the apparent missing-measure stability/equity seam. | https://www.aha.org/2022-07-12-understanding-cms-changes-hospital-overall-star-ratings |
| R267 | U.S. HUD. *Statutorily Mandated Designation of Difficult Development Areas and Qualified Census Tracts for 2026*. 90 FR 46904. | AG/policy | Current QCT rule uses three ACS releases, ~50% MoER reliability screens, two-of-three eligibility and statutory population-cap machinery. | Supplies the live decision mechanism for OF-45. | https://www.federalregister.gov/documents/2025/09/30/2025-19007/statutorily-mandated-designation-of-difficult-development-areas-and-qualified-census-tracts-for-2026 |
| R268 | U.S. Department of the Treasury. *Strategies for Determining Eligibility of Homeowners Based on Income — Margin of error strategy*. | AG/policy | States sampling error is inversely related to sample size and that using ACS margin of error across tracts can systematically disadvantage lower-population areas; permits disregarding it in the interest of equity. | Decision-channel convergence: reliability screening can itself create geographic coverage burden. | https://home.treasury.gov/policy-issues/coronavirus/assistance-for-state-local-and-tribal-governments/homeowner-assistance-fund/program-service-design/strategies-for-determining-eligibility-of-homeowners-based-on-income |
| R269 | U.S. Census Bureau / HUD. *The American Community Survey: Challenges and Opportunities for HUD*. | AG/analysis | QCT misclassification risk rises near thresholds and for smaller tracts; false inclusion/exclusion trade off; 20% cap complicates error handling. | Direct ancestor sharply limits OF-45 novelty. | https://www.census.gov/content/dam/Census/library/working-papers/2002/acs/2002_Kuchak_01.pdf |
| R270 | Brown W, Scardamalia R. *Using the American Community Survey (ACS) Multi-Year Estimates in State Programs: Empire Zones in Rockland County, NY*. 2007. | AG/working paper | Evaluates legislative threshold-based eligibility using ACS multi-year estimates and documents designation instability concerns across releases. | Classical/direct ancestor for generic noisy-threshold eligibility instability. | https://www.census.gov/library/working-papers/2007/acs/2007_Brown_01.html |
| R271 | U.S. HUD. *Statutorily Mandated Designation of Difficult Development Areas and Qualified Census Tracts for 2016*. 80 FR 73201. | AG/policy | Documents regime change: prior designations accepted MoER <100%; 2016 tightened the reliability standard to about 50%, with two-of-three reliability requirements. | Creates a concrete historical policy counterfactual unique to the modern OF-45 framing. | https://www.govinfo.gov/content/pkg/FR-2015-11-24/pdf/2015-29953.pdf |
| R272 | U.S. HUD USER. *Qualified Census Tract Table Generator / QCT Designation Algorithm*. | AG/data/code-spec | Public all-tract extracts contain Census/ACS inputs and margins of error; the algorithm specifies exact reliability, eligibility, ranking and cap operations. | Establishes reproducible public-data feasibility for the next OF-45 gate. | https://www.huduser.gov/portal/qct/index.html ; https://www.huduser.gov/portal/qct/QCT_Algorithm.html |
| R273 | Soltas E. *Tax Incentives and the Supply of Low-Income Housing*. Working paper, 2024. | WP/AW | Precisely reconstructs QCT assignment, notes high-sampling-error disqualifications and 20% cap, and simulates ACS sampling variation; uses it as identifying variation for LIHTC effects. | Closest current empirical neighbor. Narrows OF-45 to evaluating the precision screen's own reliability/coverage consequences. | https://economics.sas.upenn.edu/system/files/2024-08/Empirical%20Micro%2010312024.pdf |
| R274 | Jones E, Sagawa S, Koh PW, Kumar A, Liang P. Selective Classification Can Magnify Disparities Across Groups. ICLR 2021. | PP/theory | Shows that abstention based on confidence can improve average accuracy while magnifying subgroup disparities. | Abstract ancestor for reliability-screen/selective-coverage tradeoffs; blocks generic theorem novelty. | https://openreview.net/forum?id=HPyhX33H1a9 |

# Pass-18 evidence synthesis — D031 independent-channel triangulation

1. **Provisional→final data states:** EPA supplies a concrete operational workflow, but vintage/revision reliability has mature statistical ancestry [R261–R262]. Collapse before registration.
2. **FAERS duplication:** a 2024 synthesis plus a 2025 FDA-operational full-database pipeline make this directly occupied and highly active [R263–R264]. Collapse before registration.
3. **CMS hospital-star missing measures:** the current methodology explicitly conditions on available groups and existing evaluation already identifies volatility for fewer-measure/smaller hospitals [R265–R266]. Collapse before registration.
4. **HUD QCT precision screening:** three channels converge. HUD applies an explicit MoER-based reject rule and publishes exact inputs/algorithm [R267, R272]; Treasury states the sample-error equity concern directly [R268]; theory predicts population-linked selective coverage plus cap-mediated nonlocal effects.
5. **Ancestor constraint:** old HUD/Census work already establishes small-tract misclassification and error tradeoffs [R269], ACS threshold-program instability is established [R270], and generic selective-classification disparity theory exists [R274]. These are not OF-45 novelty claims.
6. **Modern distinction:** HUD materially tightened the QCT MoER screen in 2016 [R271]. The surviving question is the empirical/theoretical consequence of that current screen, not whether ACS estimates are noisy.
7. **Closest active neighbor:** Soltas reconstructs the rule and simulates sampling-driven QCT variation [R273] but studies housing-subsidy incidence/supply, not the precision screen's reliability-versus-coverage tradeoff.
8. **Disposition:** register **OF-45 — PRIORITY BOUNDED PROSECUTION / NOT C011**. The next gate must distinguish policy-counterfactual designation effects, which are publicly reconstructible, from actual latent classification-error reduction, which is not directly observed.

# XI. D032 OF-45 rule/identification prosecution

| ID | Citation / source | Type | What it establishes | D032 consequence | Stable locator |
|---|---|---|---|---|---|
| R275 | U.S. HUD. *Statutorily Mandated Designation of Difficult Development Areas and Qualified Census Tracts for 2015*. 79 FR 59855. | AG/policy | Introduced the three-release QCT procedure using 2006–2010, 2007–2011 and 2008–2012 ACS data; release-level income/poverty inputs were rejected when their 90% confidence interval included zero. | Makes the pre-2016 screen operationally explicit; for positive estimates this corresponds to relative MoE `<100%`. | https://www.govinfo.gov/content/pkg/FR-2014-10-03/pdf/2014-23684.pdf |
| R276 | U.S. Census Bureau. *Period Estimates in the American Community Survey*. 2022; current guidance accessed 2026. | AG/methodology | Census strongly recommends against comparing overlapping ACS 5-year estimates because much of the underlying data are shared. | Blocks independent-release/binomial treatment of HUD's three overlapping ACS releases. | https://www.census.gov/newsroom/blogs/random-samplings/2022/03/period-estimates-american-community-survey.html |
| R277 | U.S. Census Bureau. *American Community Survey Design and Methodology*, Ch. 12 / sampling error. | AG/methodology | ACS 90% margin of error satisfies `MOE = 1.645 * SE`, so `SE = MOE / 1.645`. | Converts HUD's MoER thresholds to CV scales and defines marginal error inputs while underscoring that MoEs alone do not supply cross-release covariance. | https://www.census.gov/content/dam/Census/library/publications/2010/acs/acs_design_methodology_ch12.pdf |
| R278 | Soltas E. *Tax Incentives and the Supply of Low-Income Housing*. Linked current PDF dated May 11, 2024; rechecked 2026-09-09. | WP/AW | Current paper still reconstructs QCT assignment, includes high-ACS-sampling-error disqualifications and the 20% cap, and simulates sampling variation using marginal normal errors with standard deviations implied by MoEs. | Closest neighbor remains adjacent: reconstruction/noise simulation are not novel, but the precision screen's own policy consequences are not its estimand. | https://evansoltas.com/papers/SoltasJMP.pdf |
| R279 | Florida Housing Finance Corporation ArcGIS. *QCTs As of 2026* feature layer. | AG/state data mirror | Florida-only layer exposes HUD-derived tract fields including three releases of B17001/B19013 estimates and MoEs, population, area population, income limits and QCT status. | Confirms practical input schema but is not national HUD evidence and cannot resolve the nationwide magnitude gate. | https://services8.arcgis.com/GfH4uM8d7iVMXBlB/arcgis/rest/services/QCTs_As_of_2026/FeatureServer/0 |

# Pass-19 evidence synthesis — D032 OF-45 bounded rule/identification gate

1. The historical reliability intervention is operationally sharp: 2015 excluded release-level values whose 90% interval included zero [R275], while 2016 tightened the reliability standard to approximately 50% relative MoE [R271].
2. The modern deterministic policy map is fully specified by HUD [R272]. Therefore a same-data `c=0.50` versus `c=1.00` replay identifies screen-induced policy changes once all-tract inputs are available.
3. The latent accuracy estimand is not directly identified. Consecutive ACS 5-year products share most component years, and Census warns against treating overlapping period estimates as ordinary independent comparisons [R276]. Published MoEs provide marginal SEs [R277], not the required cross-release covariance or a fixed latent tract state.
4. Soltas's current 2026 version remains a strong anti-novelty neighbor for QCT reconstruction and ACS-noise simulation [R278], but it does not directly estimate the screen's reliability-versus-coverage/designation tradeoff.
5. A Florida mirror confirms the expected tract-level schema [R279] but is not an adequate substitute for the national empirical replay.
6. **Disposition:** OF-45 survives the rule/identification/nearest-neighbor components but **does not clear the empirical magnitude gate**. C011 remains unassigned.

# XII. D033 C011 national empirical gate

| ID | Citation / source | Type | What it establishes | D033 consequence | Stable locator |
|---|---|---:|---|---|---|
| R280 | U.S. HUD USER. *qct_data_2026.xlsx — 2026 QCT data for all census tracts in the United States and Puerto Rico*. Project-local copy acquired 2026-09-08. SHA-256 `aa1a076b63ca839402558fd1b57f017d1b934857851ebf5726876455dffc8e29`. | AG/data | National all-tract inputs for 2026: 2020 Census population/households, three ACS 5-year income/poverty estimate+MoE sets, adjusted income limits, derived ratios/rates and final QCT flag. | Resolves the D032 binary-ingestion bottleneck; supports exact zero-mismatch reconstruction and the national `c=0.50` vs `c=1.00` policy replay. | Project source `qct_data_2026.xlsx`; public origin via R272 / https://www.huduser.gov/portal/datasets/qct.html |


| R281 | U.S. HUD USER / Federal Register. *Statutorily Mandated Designation of Difficult Development Areas and Qualified Census Tracts* (current algorithmic notice rechecked 2026-09-09). | AG/policy | Current HUD QCT materials continue to apply an approximately 50% relative-MoE reliability screen, multi-release eligibility logic and a statutory 20% population-cap allocation procedure. | Confirms that C011 remains tied to a live official-statistics policy mechanism; does not itself evaluate selective coverage/nonlocal consequences. | https://www.huduser.gov/portal/datasets/qct.html |
| R282 | Soltas E. *Tax Incentives and the Supply of Low-Income Housing*. Author-linked PDF rechecked 2026-09-09; PDF title page dated May 11, 2024. | WP/AW | The paper remains a close LIHTC/QCT neighbor using cutoff/scoring variation and QCT-related sampling-error features, but the precision screen's population-selective coverage and cap-propagation consequences are not its central policy estimand. | Bounded D036 monitoring finds adjacent competition, not direct occupation. Corrects the prior ledger's “May 2026” version label while leaving the substantive nearest-neighbor conclusion unchanged. | https://evansoltas.com/papers/SoltasJMP.pdf |

# Pass-21 evidence synthesis — D036 narrowed-scope monitoring

1. Current HUD materials still document the live reliability-screen and statutory population-cap machinery underlying C011 [R281].
2. The author-linked Soltas PDF currently resolves to a document dated May 11, 2024, not May 2026 [R282]. This bibliographic correction does not change its role as the closest adjacent LIHTC/QCT competitor.
3. The bounded monitoring pass did not identify a direct study making the post-2016 precision screen's selective coverage, population burden and strict nonlocal cap propagation the central estimand.
4. D036 therefore treats novelty as **sufficient for a narrowed exact-year paper but monitoring-sensitive**, not as a claim that QCT reconstruction, ACS noise or threshold assignment are untouched topics.
5. Discovery-mode literature searching remains closed; reopen only if monitoring surfaces direct occupation or manuscript positioning reveals a fatal overlap.

# Pass-20 evidence synthesis — D033 national OF-45 replay

1. The 2026 HUD algorithm can be reproduced exactly from R280: **0 final-QCT mismatches across 85,390 records**.
2. Holding the 2026 data and algorithm fixed, changing only the relative-MoE screen from `<100%` to `<50%` removes 2,043 of 19,253 looser-screen eligible records (10.61%) and changes 2,825 final statuses (2,063 losses, 762 gains).
3. The population-linked burden is not explained away by substantive-threshold proximity. Within every quintile of two-of-three threshold distance, the smallest population quintile has materially higher eligibility-loss rates than the largest; a state/metro/threshold-adjusted diagnostic regression gives OR 0.447 per population doubling.
4. The cap is an active propagation mechanism: 40 of 144 looser-screen binding areas cease to bind, and 332 gaining records across 87 areas / 32 states change final status despite no change in any of their own precision-screen indicators.
5. The identified claim is a **precision/coverage/designation** tradeoff. R276–R277 still block a direct claim about latent true-classification accuracy from the three overlapping ACS releases.
6. R278 remains the closest active empirical neighbor but does not evaluate the post-2016 precision screen as the policy object.
7. **Disposition:** the OF-45 empirical promotion gate passes. Promote to **C011 — SURVIVES / PRE-EXECUTION** and stop primary-project discovery mode.

# C013 PLACES temporal-provenance evidence

**Search cutoff:** 2026-09-21. The complete protocol, inclusion/exclusion ledger and three reproductions are preserved in `22_C013_PLACES_TEMPORAL_PROSECUTION.md`.

| ID | Source | Type | Contribution to C013 | Limitation / use boundary | Stable locator |
|---|---|---|---|---|---|
| R283 | CDC. *PLACES Frequently Asked Questions*. | AG/GD | Documents release history, rotating measures, local-trend prohibition, ranking warning, policy-evaluation warning and the 2023 confidence-interval procedure change. | Agency warnings do not quantify downstream use or conclusion sensitivity. | https://www.cdc.gov/places/faqs/index.html |
| R284 | CDC. *PLACES Methodology*. | AG/GD | Defines the multilevel regression and poststratification framework and geographic products. | Method documentation does not supply cross-release joint covariance. | https://www.cdc.gov/places/methodology/index.html |
| R285 | CDC. *PLACES and 500 Cities Data Dictionary*. | AG/DS | Supports release-, geography- and measure-level schema reconstruction. | Catalog metadata can change; execution must preserve Socrata IDs and query manifests. | https://data.cdc.gov/500-Cities-Places/PLACES-and-500-Cities-Data-Dictionary/m35w-spkz |
| R286 | Kong AY, Zhang X. *The Use of Small Area Estimates in Place-Based Health Research*. 2020. | PP/method | Establishes general cautions for secondary use of small-area estimates. | Does not perform a PLACES release-provenance corpus or downstream reanalysis. | https://doi.org/10.2105/AJPH.2020.305611 |
| R287 | Greenlund KJ et al. *PLACES: Local Data for Better Health*. 2022. | PP/method | Primary PLACES methods/intended-use ancestor. | Not a temporal reliability audit of published repeated-release applications. | https://doi.org/10.5888/pcd19.210459 |
| R288 | Candipan J, Riley AR, Easley JA. *While Some Things Change, Do Others Stay the Same?* 2023. | PP | Eligible two-wave 500 Cities tract-health change application. | Requires exact release/source alignment and boundary comparability before temporal adjudication. | https://doi.org/10.1080/10511482.2022.2076715 |
| R289 | Hunyadi JV et al. *Spatial and Temporal Patterns of Chronic Disease Burden in the U.S., 2018–2021*. 2025. | PP | Eligible annual county composite/hotspot application with decision-facing burden prioritization. | Accessible methods did not resolve all supplement/code choices; composite mixes measure cadences. | https://doi.org/10.1016/j.amepre.2024.08.022 |
| R290 | Mohebbi F et al. *A Computational Approach to Analyzing Spatiotemporal Trends in Gun Violence and Mental Health Disparities*. 2025. | PP | Eligible contextual temporal use; supplies health outcomes with distinct source years as a contrast to rotating measures. | Formal time-series procedures chiefly target gun incidents; health layer must not be overclassified. | https://doi.org/10.1007/s11524-025-00976-x |
| R291 | Nguyen QC et al. *Changes in the Neighborhood Built Environment and Chronic Health Conditions in Washington, DC, in 2014–2019*. 2025. | PP | C013 contrasting reproduction: four outcomes have six distinct source years while high cholesterol has four and two exact copied pairs. | Public outcome-panel reproduction does not reproduce the complete image-processing/mixed-model pipeline. | https://doi.org/10.2196/74195 |
| R292 | Al Qady A et al. *S574 Examining Colorectal Cancer Screening Patterns Across US Counties Using Geospatial Analysis Pre- and Post-COVID-19*. 2025. | CA | C013 bounded pre/post reproduction; exposes copied release pairs and a target-age definition change. | Abstract omits release IDs, code, weights and complete harmonization, so the result is bounded non-reproduction rather than an error finding. | https://doi.org/10.14309/01.ajg.0001129756.58233.3d |
| R293 | Rahman MA et al. *Historical Redlining and Spatiotemporal Patterns in Breast Cancer Screening*. 2026. | PP | Primary deterministic pseudo-wave case: nine nominal annual releases collapse to five mammography source waves. | Archive reproduction does not claim to reproduce unavailable complete Bayesian code or infer true local trajectories. | https://doi.org/10.1001/jamanetworkopen.2026.30685 |
| R294 | Akomaning E et al. *Temporal Trends in Stroke Prevalence Across North Dakota Before, During, and After the COVID-19 Pandemic*. 2026. | CA | Eligible active-work signal for multi-period county PLACES interpretation. | Abstract-level evidence; exact release mapping is required before adjudication. | https://doi.org/10.1016/j.neuros.2026.100034 |
| R295 | Rapaka R, Kaushik R. *Reshaping Oral Health Inequities—Pandemic Impact on Geo-Spatial Structures of Geriatric Tooth Loss*. 2026. | PR | Eligible active-work signal using rotating tooth-loss estimates across pandemic periods. | Preprint status and definition/geography harmonization require recheck before public claims. | https://doi.org/10.20944/preprints202602.0362.v1 |
| R296 | *The temporal relations among neighborhood-level binge drinking, depression, and gun violence*. Rutgers dissertation. 2026. | TH | Eligible retrospective longitudinal use of 500 Cities/PLACES outcomes. | Repository record does not expose every modeling/provenance choice. | https://doi.org/10.7282/t3-xd0f-8817 |
| R297 | Gupta A et al. arXiv:2607.28655. 2026. | PR/AW | Active adjacent work on surrogate models for timelier small-area estimates. | Addresses timeliness/modeling rather than the admissibility of longitudinal interpretation of existing releases. | https://arxiv.org/abs/2607.28655 |

## C013 search synthesis

Four focused OpenAlex queries returned 400 top-ranked records and 289 unique DOI/OpenAlex records after deduplication; a prior broader cursor scan screened 1,668 unique works. Full eligibility required at least two distinct PLACES/500 Cities releases or explicit interpretation of cross-release differences as temporal information. Nine works survived. No located source combined all four defining elements: a deduplicated temporal-use corpus, finalized measure/release/source-year crosswalk, exact carry-forward detection and conclusion-level sensitivity reanalysis.

## Change log

### 0.22.0 — 2026-09-21

- Added R283–R297 and the C013 search synthesis.

### 0.21.0 — 2026-09-17

- Preserved C012's authoritative prosecution as `21_C012_DECISION_PRESERVING_DISCLOSURE_PROSECUTION.md`; D038 relies on that record rather than duplicating its full literature table here.

### 0.20.0 — 2026-09-09
- Added R281–R282 and Pass-21 for the D036 bounded monitoring recheck.
- Corrected R278/Soltas version dating: the currently linked author PDF is dated May 11, 2024, not May 2026; substantive nearest-neighbor disposition is unchanged.
- Recorded no direct occupation of the narrowed precision-screen/selective-coverage/cap-propagation estimand in the bounded pass.

### 0.19.0 — 2026-09-08
- Added R280, the checksum-pinned project-local 2026 HUD all-tract workbook.
- Added Pass-20 synthesis for the exact national replay and C011 promotion.

### 0.19.0 — 2026-09-08

- Added R275–R279 and Pass-19 synthesis for D032 OF-45 prosecution.
- Resolved the historical/current rule and overlapping-release identification boundary.
- Kept OF-45 below C011 pending national empirical magnitude/cap-displacement replay.

### 0.18.0 — 2026-09-08

- Added R261–R274 and Pass-18 synthesis for D031 independent-channel triangulation.
- Recorded three pre-registration collapses and the three-channel convergence supporting OF-45 registration.
- Added the direct QCT ancestors, post-2016 regime-change evidence, public-data substrate, selective-classification ancestor and Soltas nearest neighbor.

### 0.17.0 — 2026-09-08

- Added R247–R260 and Pass-17 synthesis for D030 diversified review-first reconnaissance.
- Recorded five cross-domain pre-registration collapses and the second valid null-generation result.
- Redirected discovery toward theory/data/decision-channel convergence.

### 0.16.0 — 2026-09-08

- Added R231–R246 and Pass-16 synthesis for D029 review-first generation IV.
- Recorded seven pre-registration collapses, no new OF identifier, and the diversified-field next action.

### 0.15.0 — 2026-09-08

- Added R228–R230 and Pass-15 synthesis for OF-44 bounded screening.
- Recorded theorem-level occupation and the public heterogeneity-data limitation; OF-44 parked.

### 0.14.0 — 2026-09-08

- Added R218–R227 and Pass-14 synthesis for D027 review-first generation III.
- Collapsed the broad gridded-population/PPS uncertainty lead against imperfect-frame/MOS ancestors.
- Recorded OF-44 as a bounded-screening opportunity, with classical race-bridging and misclassification-sensitivity anti-novelty constraints.

### 0.13.0 — 2026-09-08

- Added R217 and Pass-13 synthesis for the OF-39 exact-enumeration theorem gate.
- Recorded the final anti-novelty conclusion: exact mechanism established, but the theorem is mechanically inherited from known non-ancillarity/replay logic.

### 0.12.0 — 2026-09-08

- Added R213–R216 and Pass-12 synthesis for the OF-39 bounded prosecution.
- Recorded the martingale-asymptotic constraint, sparse-GOF confound, and surviving finite-sample non-ancillarity calibration seam.

### 0.11.0 — 2026-09-08

- Added R195–R212 and Pass-11 synthesis for D024 cross-field opportunity generation II.
- Recorded OF-39 as the sole bounded prosecution lead while keeping C011 unassigned.
- Recorded direct ancestor/occupation evidence that downgrades OF-40–OF-43.

### 0.10.0 — 2026-09-07

- Added R189–R194 for the bounded OF-35 prosecution.
- Added Pass-10 synthesis and parked OF-35 after direct ranking-reliability overlap was established.

### 0.9.0 — 2026-09-07

- Added R170–R188 for cross-field review-first reconnaissance.
- Added Pass-9 synthesis and identified OF-35 as a prosecution lead without asserting novelty.
- Recorded classical-ancestor collapse of the broad meta-analysis content-coverage idea and high-competition status of synthetic-data inference.

### 0.8.0 — 2026-09-07

- Added R161–R169 and Pass-8 synthesis for OF-30 bounded screening.

### 0.7.0 — 2026-09-07

- Added R148–R160 for the fresh D013 four-channel opportunity-generation pass.
- Recorded OF-30 as the sole priority screening lead and preserved OF-31–OF-34 dispositions.
- Added Pass-7 synthesis while explicitly keeping C011 unassigned.

### 0.6.1 — 2026-09-07

- Corrected R143 authorship and its scope: it is an adjacent informative probability-sampling/nonresponse ancestor, not a direct NPS method.
- Added R147 (Lohr 2022) for explicit NPS diagnostics and use/do-not-use decision guidance.

### 0.6.0 — 2026-09-07

- Added R142–R146 for OF-19–OF-23 collapse-first triage.
- Updated R079 to its 2025 peer-reviewed publication and sharpened its decision relevance.
- Added Pass-6 synthesis and recorded that no opportunity earns C011.

### 0.5.0 — 2026-09-07

- Added R125–R141 for C010 four-channel screening/prosecution.
- Recorded direct prior-art collapse of the broad filter-before-reweighting claim.
- Added current Pew/Gallup/AAPOR active-work evidence and no-gold-standard classification ancestors.
- Added Pass-5 synthesis and the **PARKED / NO-GO FOR FIRST PROJECT** verdict for C010.

### 0.4.0 — 2026-09-07

- Added R120–R124 from the C009 stage-2 sensitivity/partial-identification prosecution.
- Recorded that the `delta`-only sensitivity operation and generic bounded-misclassification partial identification have strong prior art.
- Added Pass-4 synthesis and the final **PARKED / NO-GO FOR FIRST PROJECT** verdict for C009.

### 0.3.0 — 2026-09-07

- Added R113–R119 from C009 identification/nearest-neighbor prosecution.
- Recorded that the broad C009 novelty framing fails and the narrowed P/NPS-specific decomposition advances to PROSECUTION.
- Corrected the bridge-sample identification statement.
