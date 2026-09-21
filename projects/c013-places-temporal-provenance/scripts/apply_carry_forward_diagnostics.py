#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"outputs/machine/full_provenance_crosswalk.jsonl"
DIAG=ROOT/"outputs/machine/carry_forward_diagnostics.jsonl"
OUT=ROOT/"outputs/machine/provenance_crosswalk.jsonl"

def read_jsonl(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]

base=read_jsonl(BASE)
diag=read_jsonl(DIAG)

def diag_key_current(d):
    c=d["current"]
    return (c["release_year"],c["dataset_id"],c["geography_level"],c["measure_id"],c["data_value_type"],c["brfss_source_year"])

dmap={diag_key_current(d):d for d in diag}
updated=0
for r in base:
    key=(r["release_year"],r["dataset_id"],r["geography_level"],r["measure_id"],r["data_value_type"],r["brfss_source_year"])
    d=dmap.get(key)
    if not d:
        continue
    r["exact_copy_percentage"]=d["exact_copy_percentage"]
    r["common_geography_count"]=d["common_geography_count"]
    r["coverage_change"]=(
        f'predecessor_rows={d["predecessor_rows"]}; current_rows={d["current_rows"]}; '
        f'common={d["common_geography_count"]}; predecessor_only={d["predecessor_only_count"]}; '
        f'current_only={d["current_only_count"]}; comparable_common={d["comparable_common_geography_count"]}'
    )
    r["carry_forward_classification"]=d["carry_forward_classification"]
    r["verification_note"] += (
        f' Row-level public-data comparison completed; predecessor query SHA-256 '
        f'{d["predecessor_query_sha256"]}; current query SHA-256 {d["current_query_sha256"]}.'
    )
    updated+=1

if updated!=len(diag):
    raise ValueError(f"diagnostic/crosswalk mismatch: applied {updated} of {len(diag)} diagnostics")

OUT.write_text("".join(json.dumps(r,sort_keys=True)+"\n" for r in base))
print(json.dumps({
    "records":len(base),
    "diagnostics_applied":updated,
    "exact":sum(r["carry_forward_classification"]=="exact carry-forward" for r in base),
    "revised":sum(r["carry_forward_classification"]=="revised carry-forward" for r in base),
    "ambiguous":sum(r["carry_forward_classification"]=="ambiguous" for r in base),
    "new_source_wave":sum(r["carry_forward_classification"]=="new source wave" for r in base),
},sort_keys=True))
