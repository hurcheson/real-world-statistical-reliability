---
title: Origin and Research Journey
version: 0.21.0
last_updated: 2026-09-21
status: active
---

# Origin and Research Journey

## 1. Starting point

The project began with a practical objective:

> Use AI end-to-end to help discover a research problem, validate it, develop the question, identify data, design the methodology, and eventually execute the study.

The initial context was an Applied Statistics and Data Science student at UTRGV seeking a principled way to find research questions rather than inventing topics randomly.

The first test case centered on **Dr. Kristina P. Vatcheva** and the idea of mapping a researcher's body of work, connecting related papers, and identifying a defensible gap.

A key constraint was established early:

> Do one real end-to-end research discovery first. Do not begin by building a generalized research-intelligence system.

This constraint remains foundational.

## 2. Initial Vatcheva mapping

The early literature map identified recurring themes in Dr. Vatcheva's work:

- regression validity and multicollinearity;
- statistical interaction/effect modification;
- count-model selection;
- missing-data treatment;
- physiological time-series imputation;
- blood-pressure variability;
- cardiovascular and neurocognitive outcomes.

A candidate emerged by connecting her work on blood-pressure imputation with her collaborations involving blood-pressure variability.

## 3. Candidate C001 — imputation → BP variability → inference

The first candidate asked whether time-series imputation methods that reconstruct blood pressure well also preserve downstream scientific quantities such as blood-pressure variability and regression inference.

The initial attraction was strong:

- it directly connected multiple Vatcheva research streams;
- it was statistically meaningful;
- public data appeared available;
- it could combine missing data, time series, simulation, and inference.

A detailed protocol was sketched involving realistic missingness, multiple imputers, ARV and related variability metrics, semi-synthetic outcomes, and downstream coefficient bias.

### Why C001 was later killed

A more adversarial search showed that the conceptual core was already substantially occupied:

- task-oriented imputation evaluation already explicitly questions whether reconstruction quality predicts downstream-task quality;
- recent physiological-sensor work has studied how missingness affects derived variability metrics and downstream associations;
- blood-pressure variability is already known to be sensitive to measurement design;
- modern location-scale and joint models already address bias from naive person-level variability estimation.

The remaining novelty would have been a narrower application of an established principle to a particular blood-pressure setting.

**Verdict: KILLED as primary project.**

## 4. Candidate C002 — informative observation → BP variability

Attention then shifted from missing values to the process determining **when measurements occur**.

The central insight was that routine EHR blood-pressure measurements are not necessarily sampled innocently. Health state, treatment changes, symptoms, clinician concern, and healthcare use can influence observation frequency.

The candidate question became:

> How does informative, irregular measurement timing affect estimation of within-person blood-pressure variability and its association with outcomes?

This was more statistically fundamental because the sampling process itself could contaminate the apparent physiological variability.

### Why C002 was later parked/no-go

A deeper novelty prosecution found:

- informative observation/visit processes are an established statistical area;
- older joint models already combine observation, longitudinal, and terminal-event processes;
- BPV methodology papers had explicitly identified adding an informative measurement process as future work;
- newer location-scale joint modeling papers had also explicitly named this extension;
- active PhD-level work was found on within-subject variability under irregular and informative observation;
- active groups and software around location-scale joint models indicated meaningful scooping/competition risk;
- realistic EHR data can involve at least two observation mechanisms: whether a patient is seen and whether a particular biomarker is measured;
- the full problem raises difficult identification and sensitivity-analysis issues.

The exact combination may not have been fully published, but the remaining niche appeared too technically expensive and competitively exposed for a first project.

**Verdict: PARKED / NO-GO as primary project.**

## 5. Research-process realization

These two failed candidates produced a more important insight:

> The goal is not to find a mystical untouched gap. The goal is to identify an important, defensible, finishable contribution inside a productive research neighborhood.

The research process should reward killing attractive ideas when evidence weakens them.

## 6. Shift from “one gap” to “research program”

The discussion then addressed how productive researchers generate many papers.

The key conclusion was that established researchers usually develop **problem ecosystems**, not isolated questions. They repeatedly work within a neighborhood they understand deeply, accumulating:

- terminology;
- datasets;
- methods;
- competitors;
- unresolved weaknesses;
- software;
- domain knowledge;
- collaborators.

This reduces the marginal cost of generating each subsequent project.

The desired long-term identity therefore became broader than any one blood-pressure problem.

## 7. Program direction established at baseline v0.1

The selected neighborhood is:

> **Reliability and transportability of statistical/ML models under imperfect real-world data.**

Initial subthemes include:

- distribution shift;
- calibration;
- missingness;
- uncertainty;
- subgroup heterogeneity;
- external validation;
- model updating;
- transportability.

The initial application context will likely be biomedical/health data because it offers high-stakes reliability questions, public datasets, and a strong intersection of statistics and machine learning.

At baseline v0.1 this was **not yet the first paper**; the next planned task was to map the neighborhood, identify candidate contributions, prosecute them, and select one project for execution. Section 9 records the first completion of that mapping step.

## 8. Repository/project philosophy

The project itself is intended to become external research memory.

Instead of:

search → understand → forget → repeat,

the workflow should be:

search → verify → record → update.

Canonical Markdown records should preserve both successful and rejected ideas so future AI sessions do not reinvent previously examined paths.

## 9. First deep field-mapping pass — observation-process reliability

The first broad map did not begin by selecting one of C003–C007. Instead, it used **predictive reliability under real-world dataset shift** as the spine and then narrowed to a particularly consequential interface:

> **external predictive reliability under measurement / observation-process shift.**

The mapping connected four literatures that use different language and evaluation standards:

1. clinical prediction-model methodology;
2. distribution-shift / robust ML;
3. informative presence, observation and missingness;
4. post-deployment monitoring and updating.

### What the map ruled out

Several broad candidate families became less attractive as first projects:

- generic conformal/UQ under covariate shift is theoretically dense and active;
- generic dynamic updating is already a substantial methodology literature;
- generic missingness-shift robust prediction has current theory and algorithms;
- generic MIMIC/eICU cross-site calibration studies are now active;
- post-deployment missingness/latency monitoring has direct 2026 evidence.

This was an important anti-gap result: the program should not claim these areas are neglected.

### What remained interesting

The strongest surviving interface was narrower:

> Can external validation diagnose when a model has learned source-specific healthcare **observation-process signal**—for example measurement frequency, missingness or data-availability patterns—and distinguish that failure from ordinary case-mix or prevalence shift?

This became **C008 — Measurement-process-aware external-validation stress testing**.

### Why C008 was not immediately promoted

The same mapping found very close work:

- predictor measurement heterogeneity and missing-data compatibility in the clinical prediction literature;
- general conditional/context-shift robustness frameworks;
- explicit missingness-shift theory;
- a 2025 preprint formalizing clinical presence shift;
- a 2026 MIMIC-IV/eICU sepsis preprint showing observation-process features can improve internal discrimination while worsening external calibration;
- a 2026 MIMIC-IV/eICU mortality preprint already using calibration, recalibration, decision curves and subgroup analyses.

Therefore C008 was promoted only to **SCREENING**, not PROSECUTION or EXECUTION.

The next scientific task is to attack its possible differentiator: **shift attribution and controlled observation-process stress testing**, not merely another external validation.

## 10. Evidence infrastructure matured one step

Because this mapping pass involved dozens of primary sources, active preprints, datasets, repositories and research groups, a new canonical `11_REFERENCE_LEDGER.md` was created.

The ledger records stable IDs, URLs/DOIs, evidence types, what each source establishes, what it does not establish, and representative search queries.

This is intentionally still lightweight Markdown rather than a new research-information system, consistent with the original constraint against premature infrastructure building.

---


## 11. First neighborhood reconsidered after competitive-geometry evidence

After the observation-process map, the project owner raised a practical concern: the closest C008 frontier was populated by several major groups with direct current work, while the project lacked their domain infrastructure and accumulated expertise.

The correct interpretation was refined:

> Strong researchers existing in a field is not itself a reason to leave. The relevant question is whether the **marginal expertise, data and compute required to differentiate a first project** are proportionate to the expected contribution.

Under that criterion, C008 was parked as a no-go for the first project. The project did not delete the ML map; it preserved it as evidence that the discovery process successfully prevented premature execution.

## 12. Second deep field map — probability/nonprobability survey data integration

The next neighborhood examined was survey sampling/statistical data integration, specifically finite-population inference from nonprobability sources using probability references.

The map found a more favorable first-project structure:

- strong real-world demand from official statistics;
- a coherent inferential core around sampling, selection, calibration, measurement and sensitivity;
- public paired probability/nonprobability data through CDC/NCHS RANDS;
- moderate compute and mature R tooling;
- active but navigable research competition.

The map also killed several easy-looking ideas before commitment: generic nonignorable selection, multiple reference surveys, quantiles/CDFs, generic measurement-error+representativeness, regression targets and small-area NPS all have direct contemporary work.

## 13. Emergence of C009

A narrower interface survived initial screening:

> Standard integration procedures depend on adjustment variables shared across probability and nonprobability sources, but those variables may not be measured equivalently across sources or modes.

This became **C009 — Cross-source measurement mismatch in nonprobability-sample adjustment**.

The key evidence was not an absence-of-literature claim. It was a boundary between literatures:

- survey-integration methods formalize a common shared `X`;
- panel-methodology studies show measurement equivalence can fail;
- direct 2025 selection+misclassification work still assumes participation covariates are measured without error in both samples;
- classical IPW with error-prone covariates exists and may collapse the candidate if the extension is trivial.

Therefore C009 entered **SCREENING**, not execution.

## 14. Research state after second map — historical snapshot

The active first-project neighborhood is now:

> **Finite-population inference from integrated probability and nonprobability data sources, with emphasis on selection, measurement compatibility and robustness of adjustment.**

At that point, C009 was the priority SCREENING lead and the next task was identification/nearest-neighbor derivation. This state was superseded later the same day by the stage-1 prosecution milestone below.



## Milestone — C009 stage-1 prosecution narrows the candidate

**Date:** 2026-09-07

The first formal identification/nearest-neighbor prosecution of C009 did not validate the broad “cross-source measurement mismatch” framing. Older and adjacent work already covers erroneous auxiliary controls in calibration, differential measurement error in propensity-score covariates, generic error-prone IPW, and finite-population data integration with measurement error [R089, R113–R115].

Rather than abandon the survey-data-integration neighborhood, the candidate was narrowed around a more specific P/NPS interaction. A binary toy model separated naive calibration bias into a **wrong-scale benchmark** component and a **residual proxy-selection** component. It also showed that no-validation identification can fail, known source-specific error rates can identify the target under the toy assumptions, and a bridge sample measuring two fallible versions is not automatically a validation design.

C009 therefore moved from SCREENING to **PROSECUTION — NARROWED**, not to SURVIVES or EXECUTION. The next gate is whether bounded mismatch yields a useful sensitivity/partial-identification diagnostic with real decision value beyond the closest prior art.

This milestone reinforces the program's operating rule: prosecution is allowed to make a candidate smaller. A narrower true question is preferable to preserving an attractive but already-covered claim.


## Milestone — C009 stage-2 sensitivity prosecution parks the candidate

**Date:** 2026-09-07

The second prosecution executed the exact gate set at the end of stage 1: bounded cross-scale mismatch, partial identification under bounded source-specific misclassification, decision thresholds, empirical anchoring, and direct comparison with the nearest sensitivity literature.

The mathematics sharpened rather than disappeared. The binary model compressed into

`mu = mu_B + ((d_obs-delta) Delta_W)/kappa`,

where `delta` is the wrong-reference-scale discrepancy and `kappa=Corr(X,W_B|R=1)^2` under the toy assumptions is the fraction of latent selection correction recovered through the B-side proxy. Exact zones identify when naive calibration under-corrects, happens to be exact by cancellation, over-corrects but helps, becomes worse than no adjustment, or points in the wrong direction.

The literature and feasibility prosecution nevertheless failed the first-project promotion gate. Hartman & Huang [R120] substantially cover sensitivity to an unknown target-population weighting margin; Molinari [R121] covers generic bounded-misclassification partial identification; R122–R124 and earlier work occupy much of differential measurement-error sensitivity and error-prone weighting. RANDS supplies a credible provenance contrast but not gold-standard or source-specific validation information from which the key sensitivity parameters can be defensibly bounded.

C009 was therefore **PARKED / NO-GO FOR FIRST PROJECT**, not killed. Its joint `delta`-`kappa` lemma and reopening conditions are retained for reuse. The survey-data-integration neighborhood remains active, but no replacement priority candidate has yet been approved.

This milestone strengthens another operating principle:

> A decision-relevant derivation can be worth keeping even when it is not large enough to justify a paper. Project selection must judge the residual contribution after prior art and empirical anchoring, not the elegance of the algebra in isolation.

## Milestone — C010 four-channel prosecution parks response-quality filtering

**Date:** 2026-09-07

After C009 was parked, the program prosecuted OF-24 as C010 using the expanded four-channel discovery protocol rather than a literature-only gap search. The candidate asked whether response-quality filtering in a nonprobability sample should be treated as an additional selection mechanism when analysts remove flagged cases and then recalibrate the retained sample.

The channels converged strongly on importance. Literature and current practice show that bogus/careless responding is a real source of error in opt-in panels; theory shows that conditioning on a pass/fail screen can alter representativeness; empirical studies show that screening can improve some quality metrics while worsening other population estimates; and practitioners must choose exclusion thresholds without knowing every respondent's true quality status [R125–R140].

That convergence did not rescue novelty. Slamowicz et al. [R127] already demonstrate filter-before-reweighting bias reduction across four nonprobability panels. Mathur [R128] already formalizes selection bias from attention-check exclusion. Sen & Lahiri [R126] directly occupy the measurement-error × representativeness interface. Generic no-gold-standard classification and bounded-misclassification theory further constrain the residual claim [R141, R121].

The prosecution retained one useful conceptual lemma:

`post-filter error = retained response contamination + residual selection among retained cases`,

under ideal calibration to the target distribution of the observed adjustment variables. This makes explicit that removing cases is an inferential selection intervention, not neutral cleaning.

C010 was therefore classified **PARKED / NO-GO FOR FIRST PROJECT**. It can be reopened if credible respondent-quality validation data become available or if post-filter calibration structure yields a nontrivial identification, partial-identification or estimand-targeted threshold result beyond the existing component literatures.

The active D013 neighborhood remains intact; the next bounded triage now concerns OF-19–OF-23.

## Milestone — bounded OF-19–OF-23 triage produced no C011

After parking C010, the program executed the remaining bounded opportunity slate collapse-first rather than selecting the most attractive idea by intuition.

The result was deliberately negative:

- OF-19 collapsed against direct 2025–2026 nonignorable-selection and sensitivity work;
- OF-20 remained too generic relative to existing regression-integration methods;
- OF-21's borrow-or-reject decision is already directly studied by test-and-pool methods;
- OF-23's overlap-to-threshold/restrict decision is already represented by undercoverage and low-overlap thresholding work;
- OF-22 initially appeared least occupied, but Jackson et al. [R142] already ask whether NPS selection mechanisms change over recurring waves and show stale raking can distort trends.

The triage nevertheless exposed a narrower OF-22 residue: **intermittent probability anchors**. A future method might ask what can be detected or bounded about participation drift when the NPS is continuous but a probability/reference sample appears only on selected waves. That question was not promoted because its temporal identification assumptions, theorem-level differentiation and public validation data are not yet established.

The program therefore left **C011 unassigned**. This is an important process milestone: a bounded search is allowed to return “no candidate,” and the next move becomes fresh four-channel opportunity generation rather than relabeling a weak survivor.

Full record: `15_OF19_OF23_COLLAPSE_TRIAGE.md`.

## Milestone — fresh D013 four-channel generation yields OF-30, not C011

**Date:** 2026-09-07

After the OF-19–OF-23 slate collapsed, the program returned to fresh opportunity generation rather than narrowing crowded ideas further. The prior failure records were used as hard constraints: generic nonignorability, regression integration, safe borrowing, temporal drift, overlap thresholding, measurement mismatch and response-quality filtering were not allowed to re-enter under new names.

The four-channel pass generated several new directions but only one showed sufficient convergence to become the next screening priority: **OF-30 — finite-benchmark certification / benchmark-to-target transportability**.

The key observation is operational rather than cosmetic. Survey organizations often evaluate data quality using a finite set of variables with trusted external benchmarks, yet Pew explicitly cautions that observed benchmark error need not transfer to common unbenchmarked attitude targets [R150]. NCHS's 2026 RSS methodology uses benchmark bias as an ongoing quality metric and changed toward benchmark variables related to the survey's main content in Round 4 [R148]. This creates a concrete decision question: what does success on a finite benchmark set legitimately certify about the outcomes that matter but lack truth?

A benchmark-holdout design is feasible using Pew's multi-sample benchmarking studies [R151–R153], with NCHS RSS as an independent official-statistics validation environment. A simple discrepancy decomposition shows the identification warning: benchmark balance cannot universally bound an unrestricted held-out target without an assumption linking the target to the benchmark class.

The pass also generated OF-31 (benchmark reuse/selection optimism), OF-32 (target/control-universe mismatch), OF-33 (cross-vendor respondent overlap) and OF-34 (source redundancy), but these were respectively subsumed, watchlisted or parked because of strong generic-theory/direct-prior-art threats [R156–R160].

The program therefore still left **C011 unassigned**. OF-30 is **PRIORITY SCREENING**, with a bounded next gate: direct nearest-neighbor prosecution, held-out benchmark feasibility audit, and a theory/decision differentiation test.

Full record: `16_D013_FRESH_OPPORTUNITY_GENERATION.md`.

## Milestone — OF-30 passes the data gate but fails the theory/novelty gate

**Date:** 2026-09-07

The program executed the bounded screen ordered by D020 rather than promoting OF-30 on motivation alone.

The result was asymmetric. The empirical substrate is credible: Pew's six-source study has 28 benchmark variables, while NCHS RSS Round 7 evaluates 53 health benchmark outcomes and organizes results by domain [R166, R169]. This supports nested leave-domain-out experiments and confirms that benchmark-set dependence is a real production-quality issue.

However, the nearest-neighbor/theory screen substantially narrowed the gap. R-indicator methodology already distinguishes survey-level representativeness indicators from statistic-specific bias and has directly tested whether such indicators predict bias in other survey variables [R161–R164]. Worst-case/function-class balance theory already supplies the natural route from covariate balance to target-bias bounds [R161, R165]. Cross-field benchmark-selection work now formalizes selection of informative benchmark subsets to predict unobserved benchmark performance [R168].

The elementary OF-30 impossibility statement therefore remains useful but not novel: without a structure linking unseen targets to observed benchmarks, no finite benchmark set can certify arbitrary targets; once such structure is imposed, the problem moves into existing function-class, outcome-specific or predictive-validation frameworks.

Accordingly **OF-30 was parked after bounded screening and C011 remained unassigned**. The durable output is a validation protocol—nested tuning/certification/validation sets, leave-domain-out rather than random-item holdout, and explicit declaration of the outcome universe—not a first-project candidate.

Full record: `17_OF30_BOUNDED_SCREENING.md`.

## Milestone — review-first cross-field reconnaissance opens OF-35

**Date:** 2026-09-07

After OF-30 failed its theory/novelty gate, the program did not immediately generate another survey-data-integration mechanism. Instead it tested a different discovery mode: start from current statistical reviews and active methodological literatures, extract unresolved failures and decisions, then search direct methods, classical ancestors and active work before formulating a lead.

The pass screened synthetic-data inference, random-effects meta-analysis prediction intervals, multiverse/specification uncertainty, proper-scoring/survival evaluation, interval-censored regression/prediction evaluation and count-time-series diagnostics [R170–R188].

Several apparent openings collapsed constructively. Synthetic-data inference is a genuine frontier but competitively hot in mid-2026 [R170–R173]. The meta-analysis idea of replacing mean prediction-interval coverage with high-confidence content coverage maps directly to established tolerance intervals [R174–R175]. Broad formal inference for multiverse analysis is also already occupied [R176].

The strongest surviving **pre-candidate** question is OF-35: whether prediction-performance estimators under interval censoring and imperfect assessment preserve the oracle ordering of competing survival models. Existing interval-censored accuracy papers provide imputation, weighting and model-based approaches [R182–R185], while right-censoring work supplies strong ranking-reversal/dependent-censoring ancestors [R179–R180]. The possible contribution is therefore a decision-oriented failure map—wrong-winner probability or selection regret—not another score.

The program again leaves **C011 unassigned**. D022 supersedes D013 as the exclusive active discovery-neighborhood decision while preserving survey-data integration as canonical history and a future branch.

Full record: `18_CROSS_FIELD_STATISTICS_RECONNAISSANCE.md`.

## Milestone — OF-35 ranking-reliability lead collapses under direct 2026 work

**Date:** 2026-09-07

The program prosecuted OF-35 instead of launching a simulation immediately. Full-text extraction materially changed the assessment. Yang et al. already simulate three competing interval-censored prediction models, evaluate them using model-based/IPCW/naive procedures, and calculate exact-event-time AUC/Brier/EPCE as oracle references [R183]. Thus the proposed wrong-winner statistic could be calculated from a design already present in the nearest literature.

A broader problem-sentence search then surfaced an even stronger 2026 ICML direct neighbor: Bahrini et al. compare standard censored-data survival evaluation with oracle true-event-time evaluation and explicitly analyze **preservation of model ranking** across censoring mechanisms and rates [R189]. A separate ICML 2026 paper by Yanagisawa & Akiyama studies interval-censored scoring validity and monitoring assumptions [R190]. Informative Case-K model averaging/selection is also active [R191–R192].

The program therefore parked OF-35 rather than trying to rescue it with a toy simulation. The durable lesson is procedural: a mechanism-specific search can miss a direct conceptual competitor in an adjacent mechanism, and a new decision summary is not a contribution if it is mechanically recoverable from a recent nearest-neighbor experiment.

OF-38 preserves the only credible residue—sensitivity/partial ranking under genuinely informative Case-K assessment—as a theory-heavy watchlist. **C011 remains unassigned.**

Full record: `19_OF35_INTERVAL_CENSORING_RANKING_PROSECUTION.md`.

## Milestone — D024 review-first generation II yields OF-39, not C011

After OF-35 collapsed, the program executed a second cross-field reconnaissance using the strengthened adjacent-mechanism rule rather than immediately inventing another narrow combination.

Five leads survived long enough to be recorded. Four were downgraded before candidate creation: multisource spatial validation was constrained by general correlated/geospatial CV theory; no-gold-standard prediction validation was constrained by misclassification/partial-identification ancestors; count-time-series diagnostics were directly threatened by underreporting-robust dependence testing; and extreme conditional quantiles under measurement error appeared too theory-heavy for first-project geometry.

The sole prosecution lead became **OF-39 — calibration of Bradley–Terry diagnostics under outcome-adaptive comparison scheduling**. The seam arose because current work already repairs estimation when adaptive scheduling makes the realized comparison design non-ancillary [R195], while an established diagnostic framework supplies concrete GOF/overdispersion statistics [R196]. An older response-adaptive GOF paper [R197] immediately constrained the novelty claim, so the lead was kept at prosecution status rather than promoted.

This milestone adds another program pattern: **when data collection is adaptive, estimation may be corrected before model checking is**. That statement is a search heuristic, not a novelty claim.

C011 remains unassigned and no execution project is authorized.

## 21. OF-39 bounded prosecution — adaptive diagnostics survive only in narrowed form

The second cross-field pass produced OF-39: Bradley–Terry diagnostic calibration under outcome-adaptive comparison scheduling. The subsequent prosecution did not confirm the broad intuition that adaptivity automatically invalidates standard diagnostic asymptotics. Instead, the null score process retains a martingale structure under predictable scheduling.

The prosecution isolated a narrower finite-sample mechanism: the completed adaptive comparison graph is non-ancillary, so freezing it and regenerating outcomes can represent the wrong conditional experiment. A freeze-versus-replay control showed a real endogeneity effect beyond graph topology, and scheduler replay improved bounded null calibration. However, replay itself is prior art for adaptive Bradley–Terry estimation, sparse-cell GOF is a separate classical problem, and no new validity theorem has yet been established.

The project therefore preserved OF-39 as **SURVIVES / NARROWED — HOLD BEFORE C011** and set an exact-enumeration theorem gate rather than forcing candidate promotion.


## Milestone — OF-44 bounded screening collapses the theorem path before computation

The D027 lead was prosecuted exactly as gated. P1 surfaced a decisive generic ancestor: direct misclassification partial-identification theory already provides sharp identified regions for arbitrary downstream functionals under restrictions on a categorical transition matrix [R228], with older matrix methods directly covering corrected standardized rate ratios under polychotomous misclassification [R229]. The intended bridge-specific robustness/tipping theorem therefore did not survive as a distinct statistical object.

P2 confirmed that the official Phase-1 bridge is publicly reproducible [R223], but the heterogeneity required to make the question scientifically constrained is not: official Census material treats subnational/nativity/time variation as unresolved and uses linked 2015 NCT↔2020 Census evidence that is not an ideal public simultaneous dual-format validation substrate [R224]. Public content-test reports give aggregate format comparisons but not the required stratum-specific transition matrices [R230].

The program therefore applied its stop rule and did **not** run the planned toy theorem or consequentiality simulation. **OF-44 was parked as NO-GO FOR FIRST PROJECT; C011 remained unassigned.** The durable lesson is to translate standards bridges into generic transition/misclassification-matrix form before deriving application-branded robustness certificates.

## Milestone — Two null passes lead to triangulation; D033 finally earns C011

**Date:** 2026-09-08

After OF-44 collapsed, the program deliberately refused to manufacture a candidate. D029 and D030 were valid null generation passes across increasingly diversified fields. Their repeated null result changed the **discovery channel**, not the acceptance threshold: D031 required theory/data/decision convergence and registered OF-45 around HUD's post-2016 QCT precision screen.

D032 then established the exact historical/current rule, the overlapping-ACS identification boundary and the closest active neighbor, but withheld promotion because the national empirical magnitude was unknown. Once `qct_data_2026.xlsx` became available as a project source, D033 completed the missing same-data replay.

The current `<50%` implementation reproduces all 85,390 published QCT records. Relative to the otherwise identical `<100%` counterfactual, the stricter screen removes eligibility from 2,043 records and changes 2,825 final QCT statuses. The lower-population burden persists after conditioning on substantive-threshold distance, and the cap generates nonlocal reallocation, including 332 gains whose own precision-screen indicators never change.

This is the first post-C010 lead to clear the full Charter gate. **OF-45 is promoted to C011 — SURVIVES / PRE-EXECUTION.** The central contribution is deliberately narrower than “better accuracy”: public data identify a precision/coverage/designation policy effect, while latent true-classification accuracy remains model-dependent because the ACS releases overlap.

The program therefore exits primary-project discovery mode. The next phase is protocol freeze followed by repository-backed execution, not another opportunity search.

## Milestone — D034 freezes C011 before historical confirmation

**Date:** 2026-09-08

After C011 survived on the 2026 development workbook, the program deliberately separated discovery from confirmation rather than immediately mining earlier years. D034 freezes 2026 as the development/anchor analysis and reserves 2016–2025 as the confirmatory replication set. The primary policy estimands, population-burden adjustment, cap/nonlocal decomposition, robustness analyses and failure criteria are fixed prospectively in `20_C011_EXECUTION_PROTOCOL.md`.

D015's deferred repository decision is also resolved: the durable program repository will be `real-world-statistical-reliability`, with C011 as the first project under `projects/c011-qct-precision-screen/`. Git history is intended to preserve the protocol boundary visibly: canonical snapshot and frozen protocol first, tested 2026 regression fixture second, historical confirmation only afterward.

## Milestone — D035: the confirmatory reconstruction stop fires before 2024–2025

**Date:** 2026-09-09

C011 then moved through a long, deliberately firewall-preserving historical execution. Exact official `c=0.50` reconstruction and counterfactual replay succeeded for 2016 and, after several non-exact years, again for 2020, 2021 and 2022. Across those exact years the tighter precision screen consistently reduced eligibility, produced several-percent final designation churn, placed greater burden on lower-population tracts, and generated strict nonlocal allocation changes through the 20% cap.

The intervening failures were not treated as approximate successes. 2017–2018 exposed historical cap-geography/denominator provenance problems; 2019 reduced to 19 allocation mismatches associated with an incomplete Alabama workbook; and 2023 became a tract-boundary/reliability-identification problem after HUD moved to 2020 tracts. A final 2023 prosecution independently resolved all four older-release reliability decisions for 85,368 of 85,400 records with zero disagreements, but 32 target tracts remained unresolved because their >10% contributing-2010-tract population shares could not be fully identified from the bounded public-data route.

Under the protocol frozen before historical inspection, that is decisive. With exact Tier-A years only in 2016, 2020, 2021 and 2022, and 2017/2018/2019/2023 non-exact, even perfect 2024–2025 results could produce at most 6/10 exact years. The pre-specified 7/10 reconstruction-viability criterion therefore fires **before** 2024 or 2025 are opened.

This milestone separates two outcomes that would otherwise be easy to conflate: the exact-year evidence continues to support the precision/coverage/nonlocal-allocation mechanism, but the planned decade-wide confirmatory generalization is not executable from the currently available public operational record under the frozen exactness standard. C011 therefore moves to **scope reassessment**, not automatic scientific rejection and not post-hoc relaxation.


## Milestone — D036: the failed decade design yields a narrower first paper rather than candidate abandonment

The D035 stop was followed by an explicit parent-level scope reassessment rather than another attempt to reverse-engineer historical HUD implementation. The reassessment separated **candidate falsification** from **generalization-design failure**. C011's mechanism was not falsified: the exact confirmatory years 2016, 2020, 2021 and 2022 all show screen-induced eligibility loss, positive standardized lower-population burden and strict nonlocal cap-mediated designation changes. What failed was the prospective plan to support a decade-wide claim with at least 7/10 exactly reconstructable years.

D036 therefore retains C011 as the first-paper priority under a deliberately narrower scope. The admissible inferential evidence is frozen to the four exact confirmatory years; 2026 remains development/anchor context; 2017–2019 and 2023 remain provenance diagnostics with unopened counterfactuals; and 2024–2025 remain unopened. The paper may establish recurrence of the precision-screen → selective eligibility → allocation-propagation mechanism in exactly reconstructable years, but not its prevalence, average magnitude or representativeness across 2016–2025.

The reassessment also makes **reconstruction selection** explicit. Exact-year inclusion was determined by a prospectively frozen zero-mismatch gate and not by observed counterfactual effect, but reconstructability itself can depend on operational complexity, geography stability and file completeness. The narrowed paper therefore treats unavailable years as an inferential scope limit rather than missing-at-random observations to be modeled away.

Routine historical recovery is now closed. Only genuinely new authoritative operational material can reopen a non-exact year. This preserves the audit trail and redirects work from reconstruction rescue to manuscript-quality exact-year evidence, transparency and positioning.

## Milestone — D037: final reproducibility adjudication parks C011 as the first-paper project

**Date:** 2026-09-17

The final manuscript-grade reproducibility adjudication, preserved at Git commit `bdab3ffa12af914c7cfa9e549d26c14043baa0b8`, separated historical execution status from current manuscript admissibility. The 2016 replay is fully reproducible and continues to demonstrate the precision-screen mechanism. The previously reported Tier-A results for 2020, 2021 and 2022 could not be regenerated to the complete manuscript standard from retained provenance, and the 2026 development counterfactual likewise remains unresolved.

This later evidence does not make D036 irrational in retrospect and does not scientifically falsify C011. It removes the evidentiary basis for D036's four-year recurrence manuscript. With the decade claim already closed by D035, the narrowed manuscript is now closed as well. The program therefore parks C011 as the first-paper project and closes routine reconstruction or reverse engineering of the same public inputs.

C011 may reopen only if materially new authoritative operational provenance appears. The next bounded task is not C012 creation or broad opportunity generation; it is a literature/novelty prosecution of whether the forensic execution itself exposes a distinct, publishable problem in reproducibility, auditability and preservation of public administrative/statistical decision algorithms.

## Milestone — D038 kills C012 after the permitted narrowing

After C011 was parked, the program prosecuted decision-preserving disclosure control as C012. The candidate formalized release utility as the number or value of ranking, top-*k*, and threshold decisions that remain invariant over a disclosure-compatible fiber. Exhaustive synthetic experiments established monotonicity under nested feasible sets, decision identification without cell identification, safe-release synergy, non-submodularity, non-supermodularity, and objective disagreement with cell-width utility.

Those properties were useful but did not create an independent statistical contribution. The release problem remained an instance of established optimal tabular release, risk–utility optimization, and workload-aware task optimization with a substituted nonlinear utility. No new disclosure guarantee, release mechanism, inferential theory, scalable algorithm, or independently publishable statistical object survived. D038 therefore records **C012 — KILLED / NO-GO FOR FIRST PAPER** and prohibits another narrowing of the same candidate.

## Milestone — D039 promotes O002-A1 to C013

The next opportunity search moved from abstract method invention to a concrete public-data reliability problem: repeated CDC PLACES/500 Cities releases are commonly labeled and analyzed as annual local observations even though measure-specific BRFSS source years rotate, some releases carry estimates forward exactly, definitions and eligible populations change, and CDC states that its modeling procedure does not support local trend tracking.

O002-A1 survived a complete prosecution containing a deduplicated nine-work temporal-use corpus, dual-pass coding, a 2016–2025 release/measure provenance crosswalk, three contrasting public-archive reproductions, sensitivity rules, direct-collision search, and first-paper feasibility adjudication. Four nominal annual mammography pairs were exact tract-level copies, reducing nine releases to five source waves; Washington, DC supplied both a copied high-cholesterol outcome and four negative-control outcomes with distinct source years; and a county colorectal-screening contrast was not reproducible under either natural public-archive mapping while crossing a target-age definition change.

D039 therefore registers **C013 — release-provenance and temporal-interpretability audit of repeated PLACES/500 Cities estimates — SURVIVES / CONTROLLED EXECUTION DESIGN**. The candidate does not claim to estimate true local trends or that every repeated-release analysis is invalid. Its execution target is temporal admissibility and conclusion sensitivity after source-year alignment, carry-forward removal, definition/geography harmonization, and uncertainty-aware restriction.

## Change log

### 0.21.0 — 2026-09-21

- Recorded D039 and promotion of O002-A1 to C013.
- Preserved the nine-work corpus, provenance-crosswalk mechanism, three contrasting reproductions and bounded claim language.

### 0.20.0 — 2026-09-21

- Recorded D038 and the final C012 kill after the single permitted narrowing.

### 0.19.0 — 2026-09-17
- Recorded D037 and the final distinction between historical Tier-A execution status and current manuscript reproducibility.
- Parked C011 as the first-paper project while preserving the 2016 mechanism result and the historical integrity of D035/D036.
- Set the bounded derivative reproducibility/auditability prosecution as the next task.

### 0.18.0 — 2026-09-09
- Recorded D036: C011 survives the reconstruction stop as a narrowed exact-year paper and retains first-paper priority.
- Froze the admissible evidence set, reconstruction-selection limitation and closure of routine historical rescue.

### 0.17.0 — 2026-09-09
- Recorded the D035 confirmatory reconstruction stop: four exact Tier-A years, four non-exact diagnostics, and mathematical failure of the frozen 7/10 viability criterion before 2024–2025 inspection.
- Moved C011 from execution to bounded scope reassessment while preserving the distinction between mechanism evidence and decade-generalization feasibility.

### 0.16.0 — 2026-09-08
- Recorded D034 protocol freeze, discovery/confirmation split, and the resolved `real-world-statistical-reliability` repository plan.

### 0.15.0 — 2026-09-08
- Recorded the D029–D033 path from two valid null passes through independent-channel triangulation to C011 promotion.
- Marked C011 as SURVIVES / PRE-EXECUTION and ended primary-project discovery mode.

### 0.14.0 — 2026-09-08

- Recorded the OF-44 bounded-screening collapse, stop-rule application, and no-C011 disposition.

### 0.13.0 — 2026-09-08

- Recorded OF-39 bounded prosecution and the narrowed finite-sample calibration seam.
- Preserved C011 as unassigned pending exact-enumeration/theorem prosecution.

### 0.12.0 — 2026-09-08

- Recorded D024 cross-field generation II and the OF-39 adaptive-diagnostic prosecution lead.
- Recorded the early collapse/downgrade of OF-40–OF-43 and kept C011 unassigned.

### 0.11.0 — 2026-09-07

- Recorded completion of OF-35 prosecution and the direct 2026 model-ranking overlap.
- Recorded OF-35 as parked, OF-38 as watchlist only, and C011 as unassigned.

### 0.10.0 — 2026-09-07

- Recorded the review-first cross-field reconnaissance milestone.
- Recorded OF-35 as priority prosecution lead and the constructive collapse of synthetic/meta-analysis/multiverse broad formulations.
- Preserved C011 as unassigned.

### 0.9.0 — 2026-09-07

- Recorded the OF-30 bounded-screening milestone and no-C011 decision.

### 0.8.0 — 2026-09-07

- Recorded the fresh D013 four-channel generation milestone.
- Added OF-30 as priority screening while explicitly keeping C011 unassigned.
- Recorded the collapsed/subsumed dispositions of OF-31–OF-34.

### 0.7.0 — 2026-09-07

- Recorded completion of OF-19–OF-23 collapse-first triage and the deliberate decision not to create C011.
- Recorded direct collapse of broad OF-22 by recurring-hybrid selection-drift prior art and preserved the intermittent-anchor residue.
- Moved the program from bounded-slate triage to fresh four-channel opportunity generation.

### 0.6.0 — 2026-09-07

- Recorded C010 four-channel prosecution and the **PARKED / NO-GO FOR FIRST PROJECT** verdict.
- Preserved the lesson that quality filtering is an inferential selection intervention.
- Recorded OF-19–OF-23 as the remaining live triage set.

### 0.5.0 — 2026-09-07

- Recorded completion of C009 stage-2 sensitivity prosecution and the **PARKED / NO-GO FOR FIRST PROJECT** verdict.
- Preserved the `delta`-`kappa` decision lemma and the lesson that useful algebra need not imply a viable first paper.

### 0.4.0 — 2026-09-07

- Recorded the C009 stage-1 prosecution and narrowed status.

### 0.3.0 — 2026-09-07

- Recorded the evidence-based pivot away from C008 as a first project.
- Recorded the second deep map and adoption of survey data integration/NPS inference.
- Recorded emergence and screening status of C009.

### 0.2.0 — 2026-09-07

- Added the first deep field-mapping milestone.
- Recorded the narrowing from generic dataset shift to measurement/observation-process reliability.
- Recorded anti-gap findings and the emergence of C008 as SCREENING only.
- Recorded creation of the structured reference/search evidence ledger.
