---
title: C011 Prospective Execution Protocol and Repository Specification
version: 0.1.0
last_updated: 2026-09-08
status: frozen-pre-execution
---

# C011 Prospective Execution Protocol and Repository Specification

## Protocol status

This document freezes the execution design for:

> **C011 — precision-screen reliability versus geographic coverage in HUD Qualified Census Tract designation.**

C011 entered `SURVIVES / PRE-EXECUTION` after D033. The 2026 national replay is a **development/anchor analysis** and has already been seen. It is therefore not eligible to serve as the untouched confirmatory replication set.

The confirmatory replication set is **QCT designation years 2016–2025**, analyzed only after this protocol is frozen. Substantive changes to primary estimands, decomposition definitions, or stop criteria after historical outcomes are inspected require a dated protocol amendment that states whether the change was made before or after seeing the affected results.

This protocol authorizes repository initialization and reproducible-pipeline construction. It does **not** authorize silent expansion of the estimand to latent true QCT classification accuracy.

---

# 1. Locked research question and claim boundary

## 1.1 Primary question

For each QCT designation year `y`, what changes when the HUD QCT algorithm is run on the **same observed tract-level inputs** under:

- the post-2016 precision threshold `c = 0.50`; versus
- the historical looser threshold `c = 1.00`;

while holding all other year-specific eligibility, ranking, geography, tie-breaking and population-cap rules fixed?

Write the year-specific policy map as:

`D_y(c) = HUD_QCT_algorithm_y(observed inputs_y; precision threshold = c)`.

The core identified contrast is therefore a deterministic same-data policy contrast between `D_y(0.50)` and `D_y(1.00)`.

## 1.2 Claims the core project may make

The core project may estimate and describe:

1. how many release/criterion inputs pass or fail each precision screen;
2. how much union eligibility changes;
3. how final QCT designation changes;
4. how the eligibility-loss burden varies with tract population after accounting for substantive-threshold proximity;
5. how ranking and the 20% population cap propagate the screen into local and strict nonlocal designation changes; and
6. how the precision profile of accepted inputs changes mechanically under the tighter screen.

## 1.3 Claims the core project may not make from the replay alone

Without an explicit additional model, the project must not claim that `c = 0.50`:

- reduces the true QCT misclassification rate;
- improves latent classification accuracy by a known amount;
- identifies true false-positive or false-negative rates;
- identifies the joint error law of overlapping ACS releases; or
- proves a normative fairness conclusion.

Consecutive ACS 5-year releases overlap, and the published marginal MoEs do not identify the joint sampling-error covariance plus temporal evolution of the latent tract quantities. The headline contribution remains the **precision/coverage/designation tradeoff**, not latent truth accuracy.

---

# 2. Development, confirmatory and exploratory analysis sets

## 2.1 Development/anchor year

**2026** is the development year.

It has already been used to:

- validate exact reconstruction of the current QCT algorithm;
- discover the magnitude of the `0.50` versus `1.00` contrast;
- identify the population gradient; and
- identify cap-mediated strict nonlocal changes.

The 2026 numbers remain the empirical anchor and a regression-test fixture, but they are not counted as independent confirmation of hypotheses generated from D033.

## 2.2 Confirmatory replication years

**2016–2025** are the primary confirmatory generalization set.

For each year:

1. acquire the official HUD all-tract QCT inputs and the contemporaneous public rule documentation;
2. reconstruct the official year-specific algorithm under its published `c = 0.50` rule;
3. validate the reconstruction against HUD's published QCT designation output;
4. only after validation, rerun the identical year-specific algorithm with the precision threshold changed to `c = 1.00`;
5. compute the pre-specified estimands and decomposition below.

All non-precision components of the algorithm remain year-specific. The counterfactual changes **only the precision threshold**.

## 2.3 Optional exploratory years

A pre-2016 year, especially 2015, may be added later as a transition/history illustration if its public data and rules can be reconstructed. It is **exploratory** and does not enter the primary 2016–2025 replication summary.

---

# 3. Analysis unit, keys and data provenance

## 3.1 Primary analysis unit

The primary unit is the **HUD QCT record**, not naïvely the Census tract ID alone.

A stable record key must distinguish any HUD split records created by HMFA/area treatment. The 2026 source contains 85,390 records but 85,385 unique Census tract IDs, so collapsing by tract ID before replay is prohibited.

## 3.2 Raw-data rule

Official raw files are immutable inputs.

- Never edit a raw HUD workbook in place.
- Record source URL, retrieval date, filename, byte size and SHA-256 checksum.
- Derived tabular files must be reproducible from raw inputs by code.
- Raw binaries should not be committed to ordinary Git history by default; store their provenance/checksums and fetch instructions instead.

## 3.3 Annual rule provenance

Every year receives a machine-readable rule configuration plus a human-readable provenance note containing:

- source notice/algorithm URL or citation;
- exact precision-screen operator;
- substantive income and poverty thresholds;
- two-of-three logic;
- ranking variables and both-criteria treatment;
- allocation-area definition;
- population-cap rule;
- tie handling; and
- any year-specific exceptions.

---

# 4. Reconstruction validation gate

No year enters the confirmatory counterfactual summary until the official `c = 0.50` reconstruction is validated.

## 4.1 Tier A — exact validation

A year is **Tier A** if the reconstructed final QCT flag has **zero record-level mismatches** against the official HUD flag.

Tier A years enter all primary analyses.

## 4.2 Non-exact years

Any nonzero mismatch triggers rule/data debugging before counterfactual analysis is interpreted.

A non-exact year may be reported diagnostically, but it does not enter the primary confirmatory summary unless the discrepancy is resolved to exact reproduction. The protocol must not introduce an arbitrary tolerance after seeing historical effect sizes.

## 4.3 Replication viability stop

If fewer than **7 of the 10** years from 2016–2025 can be reconstructed exactly from public materials after a documented rule-reconstruction effort, pause the multi-year generalization claim and reassess scope before manuscript-level inference.

---

# 5. Core annual estimands

For year `y`, let:

- `E_y(c)` be the set of records eligible under either QCT substantive criterion after precision screening at threshold `c`;
- `Q_y(c)` be the set of records finally designated QCT after ranking/cap allocation at threshold `c`;
- `S_iy(c)` be the complete vector of record `i`'s own release-level precision-screen indicators at threshold `c`.

## P1 — union-eligibility loss rate

`ELR_y = |E_y(1.00) \ E_y(0.50)| / |E_y(1.00)|`.

This is the primary selective-coverage estimand.

Also report income-criterion and poverty-criterion eligibility changes separately.

## P2 — final-status churn rate

`CHR_y = |Q_y(0.50) Δ Q_y(1.00)| / |Q_y(1.00)|`,

where `Δ` is the symmetric difference.

This is primary because the net QCT count can conceal offsetting losses and gains.

Also report the net designation-rate change:

`NDR_y = (|Q_y(0.50)| - |Q_y(1.00)|) / |Q_y(1.00)|`.

`NDR_y` is descriptive and must not replace churn as the main allocation metric.

## P3 — population-burden contrast

Restrict to records in `E_y(1.00)` and define

`L_iy = 1{i ∉ E_y(0.50)}`.

For each criterion, define the **substantive margin** from the second-highest criterion value among releases usable under the `c = 1.00` rule:

- income margin: second-highest income criterion score minus its eligibility cutoff;
- poverty margin: second-highest poverty criterion score divided by `0.25`, minus `1`.

For a record eligible under `c = 1.00`, define its operative substantive-threshold distance as the larger available qualifying margin. Record eligibility type as income-only, poverty-only or both.

The primary burden display is the annual loss rate across **population quintiles**.

The primary threshold-adjusted contrast is a direct standardization over the cross-classification of:

- `c = 1.00` eligibility type; and
- quintile of operative substantive-threshold distance.

Within each year, estimate the bottom-versus-top population-quintile loss-rate difference inside each stratum and average those differences using the stratum distribution of all `E_y(1.00)` records as weights.

Call this standardized finite-population contrast `BRD_y` (burden risk difference). Positive `BRD_y` means the tighter screen removes eligibility more often among lower-population records even after coarsened adjustment for substantive-threshold proximity and eligibility type.

If a required stratum has no observations in either extreme population quintile, report the missing cell explicitly; do not silently merge bins in the primary specification. Model-based standardization is then used only as a secondary robustness analysis.

## P4 — strict nonlocal designation displacement

A final-status change is **strict nonlocal** when:

- `Q_y(0.50)` and `Q_y(1.00)` differ for record `i`; and
- `S_iy(0.50) = S_iy(1.00)`.

Report strict nonlocal gains and losses separately, their share of all changed final statuses, the number of affected allocation areas, and the number of states.

This definition is intentionally stronger than simply saying a record remained eligible.

---

# 6. Mutually exclusive designation-change decomposition

Every record whose final QCT status changes between `c = 1.00` and `c = 0.50` must enter exactly one of the following categories.

## Loss categories

**L1 — direct eligibility loss**

- designated at `c = 1.00`;
- not designated at `c = 0.50`; and
- no longer eligible at `c = 0.50`.

**L2 — own-screen ranking/cap loss**

- designated at `c = 1.00`;
- not designated at `c = 0.50`;
- remains eligible at `c = 0.50`; and
- own precision-screen vector changes.

**L3 — strict nonlocal loss**

- designated at `c = 1.00`;
- not designated at `c = 0.50`;
- remains eligible at `c = 0.50`; and
- own precision-screen vector is unchanged.

## Gain categories

**G1 — own-screen ranking/cap gain**

- not designated at `c = 1.00`;
- designated at `c = 0.50`; and
- own precision-screen vector changes.

**G2 — strict nonlocal gain**

- not designated at `c = 1.00`;
- designated at `c = 0.50`; and
- own precision-screen vector is unchanged.

The implementation must assert that `L1 + L2 + L3 + G1 + G2` equals the total symmetric-difference count exactly.

At allocation-area level, also report transitions in whether the 20% population cap binds under each threshold.

---

# 7. Precision purchased by screening

This project must not equate improved precision among retained inputs with improved truth accuracy.

For income and poverty release inputs separately, report:

1. count/share passing at `c = 1.00` and `c = 0.50`;
2. count/share newly rejected by tightening;
3. median, mean, 25th/75th and 90th percentile of the relevant relative-MoE quantity among accepted inputs;
4. the poverty-screen failure decomposition into numerator-only, denominator-only and both when the official rule requires both components.

These quantities describe the mechanical precision profile purchased by selective exclusion.

---

# 8. Confirmatory generalization summaries

The 2016–2025 confirmatory result will be summarized without treating the national tract universe as a random sample requiring conventional null-hypothesis significance tests.

For each primary annual estimand, report all validated years individually plus:

- median across validated years;
- minimum and maximum;
- number of years with the same direction as the 2026 development result.

No pooled p-value is required for the deterministic finite-population policy contrasts.

The 2026 development year is plotted for context but is visually and textually marked as development/anchor rather than confirmatory replication.

---

# 9. Pre-specified robustness and secondary analyses

## 9.1 Population-burden robustness

Secondary only:

1. population deciles instead of quintiles;
2. population-weighted rather than record-weighted summaries;
3. income-only, poverty-only and both-criteria strata separately;
4. metro versus nonmetro summaries;
5. state-specific descriptive summaries where cell counts are adequate;
6. a continuous descriptive model of eligibility loss using `log2(population)`, flexible substantive-margin terms, eligibility type, state and metro status, followed by g-standardized risks.

Any model standard errors are diagnostic and must not be presented as if the 85k-record national universe were a simple random sample.

## 9.2 Record-key robustness

The official HUD-record analysis is primary. As a secondary diagnostic, summarize effects after collapsing the rare split records to unique Census tract IDs using a documented rule. This analysis cannot replace the official-record replay.

## 9.3 Precision-threshold frontier

The historical anchors `0.50` and `1.00` are confirmatory.

A threshold grid from `0.25` through `1.00` in increments of `0.05` is **exploratory mechanism analysis**. It may be used to display the precision/coverage frontier and cap discontinuities, but no post hoc threshold from this grid may replace the historical-anchor primary contrast.

## 9.4 Latent-accuracy sensitivity

Latent true-classification accuracy is **omitted from the core execution protocol**.

A correlated-error/temporal-state sensitivity appendix may be added only through a separate dated amendment specifying the covariance/state assumptions **before** its results are run. Such an appendix is secondary and cannot be used to rescue a weak core precision/coverage result.

---

# 10. Pre-specified falsification, weakening and stop criteria

C011 remains a viable first project only if the multi-year evidence shows that D033 was not an isolated development-year artifact.

## 10.1 Reconstruction stop

Pause the generalization project if fewer than 7/10 confirmatory years achieve exact Tier-A reconstruction.

## 10.2 Consequentiality weakening criterion

The candidate is materially weakened if, across validated confirmatory years, **both**:

- median `ELR_y < 0.02`; and
- median `CHR_y < 0.02`.

This would imply that the 2026 effect is atypically large and that the policy-screen consequences are generally small.

## 10.3 Population-burden falsification criterion

The lower-population burden claim fails as a general multi-year claim if `BRD_y <= 0` in a **majority** of validated confirmatory years.

If direction is positive but small/inconsistent, narrow the claim to the years/mechanisms actually supported rather than averaging away heterogeneity.

## 10.4 Nonlocal-mechanism weakening criterion

The cap-mediated nonlocal mechanism is downgraded from a central empirical contribution if strict nonlocal changes are absent in a majority of validated years or constitute less than **1% of all changed final statuses** in at least 80% of validated years.

## 10.5 Novelty stop

If monitoring surfaces a paper/preprint that directly evaluates the post-2016 QCT precision threshold with an equivalent national multi-year coverage/population/cap decomposition, stop manuscript positioning and re-prosecute differentiation before further execution.

## 10.6 Identification stop

If the only remaining publishable claim after historical replication requires asserting improvement in latent true classification accuracy, stop rather than smuggling an unidentified estimand into the project.

---

# 11. Planned tables and figures

## Confirmatory tables

**Table 1 — annual reconstruction validation**

Year, source vintages, record count, official QCT count, reconstructed QCT count, mismatch count, validation tier.

**Table 2 — annual precision/coverage/designation effects**

Release-screen pass/fail counts, `ELR_y`, income/poverty eligibility changes, QCT counts, `CHR_y`, `NDR_y`.

**Table 3 — population-burden results**

Loss rates by population quintile, threshold-distance/eligibility-type standardized `BRD_y`, plus confirmatory-year consistency summary.

**Table 4 — designation-change decomposition**

`L1`, `L2`, `L3`, `G1`, `G2`, cap-binding-area transitions and strict nonlocal geography counts.

## Confirmatory figures

**Figure 1 — mechanism diagram**

Precision screen → release acceptance → two-of-three eligibility → ranking → 20% cap → local/nonlocal final designation.

**Figure 2 — annual policy-effect panel**

2016–2025 confirmatory `ELR_y` and `CHR_y`, with 2026 shown separately as development anchor.

**Figure 3 — population burden**

Annual eligibility-loss rates across population quintiles, optionally faceted by substantive-threshold-distance strata.

**Figure 4 — allocation decomposition**

Annual composition of status churn into `L1/L2/L3/G1/G2`.

## Secondary/exploratory figures

**Figure S1 — precision/coverage frontier** across the pre-specified threshold grid.

**Figure S2 — map or area-level display** of strict nonlocal displacement, only if geographic visualization adds information beyond the allocation-area table.

**Figure S3 — accepted-input relative-MoE distributions** by threshold and criterion.

---

# 12. Manuscript framing frozen before execution

## Core headline

The paper is **QCT-first**, not a generic theorem paper.

The empirical claim to test is:

> A hard precision screen in a threshold-and-cap allocation system can purchase a tighter precision profile by selectively reducing coverage; in QCT designation, this burden may be population-dependent and can propagate through the cap to records whose own evidence never changes.

The broader statistical contribution is a carefully identified **selective precision-screen + downstream allocation** reliability pattern. A general theorem or universal fairness claim is not required for C011 to succeed.

Any broader abstraction must be earned after the multi-year QCT evidence is established and must not delay the core empirical paper.

---

# 13. Repository specification

## 13.1 Repository identity

The D015 deferred rename is now resolved prospectively.

**Recommended GitHub repository name:**

`real-world-statistical-reliability`

This is the research-program repository. C011 is its first execution project and lives in a dedicated project directory rather than forcing the entire program history into a QCT-specific repository name.

Recommended description:

> Reproducible research on statistical reliability under imperfect real-world data; first execution project: precision-screen reliability and QCT geographic coverage.

## 13.2 Directory layout

```text
real-world-statistical-reliability/
├── README.md
├── .gitignore
├── research/
│   └── canonical/
│       ├── README.md
│       ├── 00_RESEARCH_CHARTER.md
│       ├── ...
│       ├── 20_C011_EXECUTION_PROTOCOL.md
│       └── MANIFEST.json
├── projects/
│   └── c011-qct-precision-screen/
│       ├── README.md
│       ├── protocol/
│       │   └── C011_EXECUTION_PROTOCOL.md
│       ├── pyproject.toml
│       ├── uv.lock
│       ├── config/
│       │   └── rules/
│       │       ├── 2016.yml
│       │       ├── ...
│       │       └── 2026.yml
│       ├── data/
│       │   ├── README.md
│       │   ├── manifest.csv
│       │   ├── raw/          # gitignored public source binaries
│       │   ├── interim/      # gitignored derived intermediates
│       │   └── processed/    # reproducible derived tables; commit selectively
│       ├── src/
│       │   └── qct_reliability/
│       │       ├── ingest.py
│       │       ├── rules.py
│       │       ├── replay.py
│       │       ├── validate.py
│       │       ├── estimands.py
│       │       └── decomposition.py
│       ├── scripts/
│       │   ├── 01_fetch_or_register_data.py
│       │   ├── 02_validate_official_replays.py
│       │   ├── 03_run_counterfactuals.py
│       │   ├── 04_build_analysis_tables.py
│       │   └── 05_build_figures.py
│       ├── tests/
│       │   ├── test_2026_exact_reconstruction.py
│       │   ├── test_screen_monotonicity.py
│       │   ├── test_decomposition_partition.py
│       │   └── test_strict_nonlocal_definition.py
│       ├── notebooks/
│       │   └── README.md      # exploratory only; never the source of final results
│       ├── outputs/
│       │   ├── tables/
│       │   ├── figures/
│       │   └── diagnostics/
│       └── docs/
│           ├── rule_provenance/
│           └── amendments/
└── .github/
    └── workflows/
        └── tests.yml
```

## 13.3 Software baseline

Preferred execution baseline:

- Python 3.12;
- `uv`/`pyproject.toml` for a locked environment;
- tabular/XLSX tooling chosen for deterministic large-workbook ingestion;
- `pytest` for algorithm and decomposition tests;
- `ruff` for basic code quality;
- GitHub Actions running unit tests on pushes/pull requests.

The exact dataframe engine is an implementation detail as long as the outputs and tests are deterministic. No GPU or distributed-compute stack is justified.

## 13.4 Required first tests

Before any 2016–2025 result is inspected, the repository must pass:

1. **2026 exact reconstruction:** zero mismatches across all 85,390 HUD records;
2. **screen monotonicity:** every release input accepted at `c = 0.50` is also accepted at `c = 1.00` under the same valid-data conditions;
3. **eligibility monotonicity:** `E_y(0.50) ⊆ E_y(1.00)` for every year;
4. **decomposition partition:** `L1+L2+L3+G1+G2` equals the exact final-status symmetric difference;
5. **strict nonlocal invariant:** every `L3/G2` record has an unchanged own screen vector by construction;
6. **determinism:** rerunning the same raw files/configuration produces byte-identical key analysis tables or stable content hashes.

## 13.5 Data/version-control policy

- Commit source URLs, hashes and metadata; do not rely on mutable web locations alone.
- Do not commit raw XLSX binaries to ordinary Git history initially.
- If public-source persistence later becomes a problem, decide separately whether to use Git LFS or an archival release; do not introduce it preemptively.
- Commit small final tables/figures needed to reproduce manuscript claims, but regenerate bulky intermediates.

## 13.6 Branch/commit policy

Start with a protected conceptual baseline:

1. `main` — reproducible, passing state;
2. first baseline commit — canonical research records + frozen protocol only;
3. second commit — C011 project skeleton/environment/tests;
4. third commit — 2026 exact-replay implementation passing all baseline tests;
5. only then add 2016–2025 acquisition/configuration and inspect confirmatory outputs.

The purpose of this ordering is to make the prospective boundary visible in Git history.

---

# 14. Protocol amendment rule

After this freeze, any change to Sections 2, 4, 5, 6 or 10 requires an amendment file under:

`projects/c011-qct-precision-screen/docs/amendments/`

Each amendment must state:

- date;
- section changed;
- old rule;
- new rule;
- reason;
- whether any affected 2016–2025 results had already been viewed; and
- whether the change alters confirmatory versus exploratory status.

No amendment may retroactively relabel an analysis as prospective.

---

# 15. Frozen next action

With this protocol frozen, the next executable action is:

> **Initialize the `real-world-statistical-reliability` Git repository, import the canonical research snapshot, create the C011 project skeleton and locked Python environment, implement the 2026 replay as a tested regression fixture, and stop before inspecting 2016–2025 confirmatory outputs until the baseline tests pass.**

That repository/desktop stage is the point at which Work/GitHub tooling becomes materially useful.

---

## Change log

### 0.1.0 — 2026-09-08

- Froze 2026 as development/anchor and 2016–2025 as the untouched confirmatory replication set.
- Locked primary estimands, population-burden adjustment, mutually exclusive cap/ranking decomposition, robustness analyses and stop criteria.
- Excluded latent truth accuracy from the core identified estimand.
- Froze the program repository name and C011 reproducible directory/test specification.
