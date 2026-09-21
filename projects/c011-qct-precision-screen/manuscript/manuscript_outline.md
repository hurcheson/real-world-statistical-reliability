# Evidence-locked manuscript outline

**Title:** Precision Screening and Geographic Coverage in HUD Qualified Census Tract Designation

**Subtitle:** A deterministic 2016 policy-sensitivity analysis

**Scope:** 74,272 HUD records; 13,619 official designations; zero mismatches

**Disposition:** Manuscript-grade technical record; C011 remains parked as a first-paper project under D037.

## 1. Introduction

- Administrative formulas combine survey estimates, data-quality rules, and constrained allocation.
- Research questions: aggregate sensitivity, churn propagation, and population gradient.
- Contribution stated without causal, fairness, or unverified novelty claims.

## 2. Institutional setting

- QCT designation and enhanced basis eligibility under Section 42.
- Three overlapping ACS five-year releases.
- Strict income and poverty precision screens.
- Two-of-three eligibility, ranking, and 20% population cap.

## 3. Data and reconstruction

- Registered HUD workbook: 27,467,633 bytes; fixed SHA-256.
- 74,272 HUD records and 13,619 official designations.
- Zero-mismatch `c=0.50` replay.
- Arithmetic variants, duplicate-run determinism, and invariant tests.

## 4. Sensitivity design

- Hold all inputs and non-screen rules fixed.
- Compare `c=1.00` with `c=0.50` using strict `<` inequalities.
- Define ELR, CHR, NDR, own-screen vector, five-part partition, strict non-local count, and BRD.

## 5. Results

- Eligibility: 17,042 to 16,368; loss 674.
- Designation: 14,057 to 13,619; net −438.
- Churn: 651 losses, 213 gains, total 864.
- Decomposition: 473 / 159 / 19 / 71 / 142.
- Strict non-local: 161 across 75 areas and 31 state codes.
- Binding areas: 175 to 162; 13 binding-to-nonbinding transitions.
- Population-quintile rates: 10.619%, 3.901%, 2.785%, 1.439%, 1.027%.
- BRD: 0.122396.

## 6. Interpretation and limitations

- Administrative sensitivity, not latent accuracy.
- QCT status, not project funding or housing outcomes.
- Descriptive population contrast, not a demographic causal effect.
- One admissible year; no recurrence or representativeness claim.
- Overlapping ACS releases block independent-replication interpretation.

## 7. Conclusion and evidence-state decision

- Preserve the exact 2016 mechanism result.
- Do not reduce the original multi-year paper to a one-year first-paper claim.
- Reopen publication positioning only with materially new authoritative operational provenance.
