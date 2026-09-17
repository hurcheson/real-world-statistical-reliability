# C011 Local Reproducibility Handoff

**Execution date:** 2026-09-17  
**Scope:** post-D036 exact-year consolidation only  
**Frozen protocol:** preserved byte-for-byte; SHA-256 `f1e7e8e331e4016cbf6eb7243450364cfc97da2066ebf7215f42251ae7184ae1`

## Bottom line

This execution recovered and cryptographically registered all five official workbooks,
reconstructed a portable repository skeleton, implemented deterministic primitive
operations and invariants, and completed workbook-level forensics for the known 2021 and
2022 blockers. It did **not** recover any earlier C011 code or processed artifacts.

The acceptance gate is intentionally strict. On the material available here, no year may
yet be declared manuscript-admissible: 2016 has the strongest independently regenerated
numerical record, but its durable code-to-output rerun and two-run digest were not recovered;
2020, 2021, 2022 and 2026 retain substantive reproducibility blockers described below.

## Artifact search result

The accessible Work/project filesystem contained the canonical Markdown set and two pasted
handoffs only. No earlier C011 repository, `.git` directory belonging to C011, ZIP handback,
CSV/JSON result set, notebook, Python implementation, processed table, annual configuration,
or execution log survived. The raw binaries in this workspace were therefore reacquired from
HUD USER, except the 2026 workbook, whose existing Project copy was materialized and matched
the canonical R280 hash.

## Classification

| Year | Role | c=.50 exact | c=1.00 reproducible | Provenance resolved | Deterministic | Manuscript admissible |
|---|---|---:|---:|---:|---:|---:|
| 2016 | Historical exact-year candidate | Yes (prior independent regeneration) | Yes (prior independent regeneration) | Yes | Not yet re-established locally | **No, pending durable rerun/digests** |
| 2020 | Historical exact-year candidate | Yes (prior replay) | **No** | **No** | No | **No** |
| 2021 | Historical exact-year candidate | Yes only under unexplained blank-geography handling | **No** | **No** | No | **No** |
| 2022 | Historical exact-year candidate | Count exact; two record swaps | **No** | **No** | No | **No** |
| 2026 | Development anchor | Yes (prior replay) | **No** | **No** | No | **No** |

“Not yet re-established locally” is deliberately different from scientific contradiction:
the previously regenerated 2016 results remain the strongest evidence, but remembered output
is not a substitute for executable provenance.

## Year findings

### 2016

The post-D036 handoff reports exact c=.50 replay (13,619), Q(1.00)=14,057, churn 864,
decomposition 473/159/19/71/142, strict nonlocal 161, and BRD
0.1223915232729. The official workbook is now registered, but no original implementation or
processed results survived. This execution therefore preserves these as regression anchors
rather than falsely claiming a new durable rerun.

### 2020

The official workbook is registered and its stored float32-like intermediates are preserved.
The unresolved c=1.00 replay remains Q(1.00)=14,772, churn 561, decomposition
188/158/28/48/139 and strict nonlocal 167, versus surviving historical anchors of about
3.771% churn and 166 strict-nonlocal changes. No tuning was performed. A preliminary
first-divergence audit also demonstrated that neither raw `cbsa` nor `cbsasub` alone is the
operational allocation-area key; this construction must be recovered before a credible
differential replay can be finalized.

### 2021

Workbook forensics confirm that `510190501000` has valid poverty inputs and two qualifying
stored poverty releases, but blank metro/CBSA/HMFA and adjusted-income fields. The workbook
has no hidden sheet, defined name, formula/comment metadata, or embedded operational rule
justifying exclusion. Blank/exclusion handling is therefore not adopted merely because it
matches the official flag. Manuscript reproducibility remains unresolved.

### 2022

Workbook forensics confirm float32-like cached poverty values for both Los Angeles boundary
records, no hidden sheets, no defined names and no comment metadata. The public workbook
does not expose pre-rounded values capable of resolving the rank swap. Because generic rank
changes create additional errors and local exceptions are prohibited, 2022 remains unresolved.

### 2026

The recovered workbook exactly matches canonical hash R280. The latest known independent
counterfactual result remains 15,798 rather than the surviving 15,797 anchor. The exact
boundary record and globally justified rule were not recovered from surviving artifacts, so
the development fixture is not yet accepted as a deterministic counterfactual regression.

## Reproducibility assets created

- immutable raw hashes and source URLs;
- machine-readable annual configurations;
- environment/platform record;
- workbook structure audit;
- deterministic helpers for screening, positive half-up poverty rounding, average ranks,
  population tie-breaking, greedy skip-and-continue allocation, and five-part decomposition;
- executable invariant tests;
- machine-readable year-status table;
- per-year forensic provenance notes.

## Answers

1. **Which historical years are now fully reproducible?** None under the complete twelve-part
   manuscript acceptance standard. 2016 remains numerically reproduced in the authoritative
   handoff and is nearest to acceptance, but still lacks a recovered durable rerun and stable
   two-run output digest in this repository.
2. **Which are not?** 2020, 2021 and 2022 are unresolved for the reasons above. The 2026
   development fixture is also unresolved at c=1.00. No forbidden year was opened.

## Next permitted action

Continue only with the admitted years. First recover or independently derive the statutory
allocation-area key globally; then re-run 2016 twice and freeze its digests. Next use the first
record-level divergence to resolve 2020 and the 2026 boundary. Treat 2021/2022 as unresolved
unless new first-party operational evidence appears.
