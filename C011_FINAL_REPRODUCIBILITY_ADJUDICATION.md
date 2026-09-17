# C011 Final Reproducibility Adjudication

**Date:** 2026-09-17  
**Scope:** admitted exact years only; 2017–2019 and 2023–2025 were not opened  
**Canonical records:** unchanged  
**Manuscript:** not drafted

## Final decision

The maximum currently reproducible historical evidence set is **2016 only**. This is a
narrower result than the earlier research record, which classified 2016, 2020, 2021 and
2022 as Tier A after historical executions. That history is preserved, but manuscript
admissibility now additionally requires recoverable operational provenance, a durable
pipeline, deterministic reruns and independently identified c=1.00 behavior.

## Year classification

| Year | Role | Historical execution | Current reproducibility | Manuscript admissible |
|---|---|---|---|---:|
| 2016 | Historical | prior Tier A | counterfactual identified across defensible arithmetic variants | **Yes** |
| 2020 | Historical | prior Tier A | allocation construction and c=1.00 arithmetic unresolved | No |
| 2021 | Historical | prior Tier A | blank-geography provenance unresolved | No |
| 2022 | Historical | prior Tier A | two-record cap-boundary swap | No |
| 2026 | Development anchor | prior exact c=.50 | c=1.00 discrepancy not uniquely adjudicated | No |

## 2016 final reproducible result

The official c=.50 replay has 13,619 official and reconstructed QCT records and zero
record-level mismatches. Three frozen income-arithmetic variants all reproduce c=.50 exactly
and produce identical c=1.00 E/Q sets, decompositions and digests. The counterfactual is thus
identified from the retained public provenance.

Final results:

- E(1.00) 17,042; E(.50) 16,368; losses 674; ELR 3.9549349%.
- Q(1.00) 14,057; Q(.50) 13,619.
- designation losses 651; gains 213; churn 864; CHR 6.1464039%; NDR −3.1158853%.
- L1/L2/L3/G1/G2 = 473/159/19/71/142; the partition sums to 864.
- strict nonlocal = 161 (18.6342593% of churn), across 75 allocation areas and 31 states.
- binding areas: 175 under c=1.00 and 162 under c=.50; 13 binding→nonbinding and zero
  nonbinding→binding transitions.
- population-quintile loss rates: 10.61895%, 3.90144%, 2.78511%, 1.43906%, 1.02700%.
- regenerated BRD = 0.12239634180436126 (12.2396342 percentage points).

The earlier BRD diagnostic was 0.1223915232729. The difference is 0.0000048185 in probability
units and reflects numerical/binning reconstruction rather than any E/Q-set change. All
record-level policy sets and the substantive interpretation are unchanged.

Two clean executions produced byte-identical analysis records, annual result, decomposition
inputs, burden tables, precision tables, mismatch file and set digests.

## 2026 development adjudication

The old Q(1.00)=15,797 anchor was **not confirmed**. The surviving newer reconstruction gives
15,798, but the durable material does not preserve the exact c=.50 allocation-area
construction needed to establish that implementation independently from start to finish.
Simple public-field interpretations of `cbsa` and `cbsasub25` do not reproduce c=.50 exactly,
so neither 15,797 nor 15,798 is promoted by numerical preference. The source-justified final
classification is **c=1.00 not uniquely adjudicated from retained public provenance**. The old
15,797 number is therefore neither retained as ground truth nor formally corrected to 15,798.

## 2020 adjudication

The earlier execution history records an exact c=.50 replay, but its operational allocation
construction did not survive. A direct `cbsa` implementation using retained workbook averages
produces 51 false designations concentrated in CBSA 35620; direct `cbsasub` grouping produces
many more errors. This establishes that neither raw field alone is the statutory allocation
key. Without a recovered first-party area crosswalk or the original exact implementation,
the required zero-mismatch freeze cannot be recreated responsibly.

Consequently, the candidate c=1.00 result (Q=14,772; churn 561; strict nonlocal 167) and the
older approximately 3.771%/166 result remain research-history diagnostics only. The 2020
counterfactual is **not currently identified from retained public provenance** and is not
manuscript-admissible.

## 2021 and 2022 final disposition

The bounded final workspace check found no new first-party artifacts beyond those previously
audited.

- **2021:** the Bedford City record has valid poverty inputs but blank geography and income
  fields. No retained operational rule independently justifies exclusion. Inadmissible.
- **2022:** the public workbook retains only the float32-like three-decimal poverty values and
  supplies no hidden formula, pre-rounded value or general ranking rule resolving the two Los
  Angeles boundary records. Inadmissible.

Their `prior_Tier_A` history remains explicit in the classification file.

## Answers to the required questions

1. **Is 2016 completely reproducible?** Yes, under the twelve-part standard.
2. **Final 2016 result?** The complete result is stated above and serialized in the final CSVs.
3. **Final source-justified 2026 result?** c=.50 remains historical exact; c=1.00 is not uniquely adjudicated.
4. **Was 15,797 confirmed or corrected?** Neither: it was not confirmed, and 15,798 was not promoted without a complete exact-c=.50 derivation.
5. **Is 2020 c=1.00 uniquely identified?** No, not from the retained public provenance.
6. **Final reproducible 2020 result?** None admitted; candidate outputs remain diagnostic.
7. **Are 2021 and 2022 admissible?** No.
8. **Which historical results changed?** The admissible historical set contracted to 2016; its BRD received a negligible numerical correction.
9. **What caused the changes?** Missing durable operational provenance for 2020/2026, undocumented blank handling in 2021, and an unresolved cap-boundary tie in 2022.
10. **Maximum reproducible historical evidence set?** `{2016}`.
11. **Are manuscript tables/figures derivable from durable files?** Yes for the surviving 2016 evidence; the final CSVs are table/figure-source data.
12. **Can another researcher rerun it without chat history?** Yes for 2016, after acquiring the registered official workbook and running the documented scripts.

## Reproduction command

From `projects/c011-qct-precision-screen/`:

```bash
PYTHONPATH=src python scripts/01_register_data.py
PYTHONPATH=src python scripts/03_run_2016.py --output outputs/determinism/run1/2016
PYTHONPATH=src python scripts/03_run_2016.py --output outputs/determinism/run2/2016
diff -qr outputs/determinism/run1/2016 outputs/determinism/run2/2016
PYTHONPATH=src python scripts/04_build_final_outputs.py
```

The raw official XLSX files remain excluded from the portable package; their URLs, byte sizes
and SHA-256 hashes are recorded under `provenance/`.
