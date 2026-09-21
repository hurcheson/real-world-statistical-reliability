#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COVERAGE=ROOT/"outputs/machine/measure_coverage.jsonl"
OUT=ROOT/"outputs/machine/full_provenance_crosswalk.jsonl"

def read_jsonl(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]

def geography_vintage(release_year, level):
    if level=="tract":
        return "2020 Census tracts" if release_year>=2024 else "2010 Census tracts"
    return "county/county-equivalent FIPS geography"

def poststrat_base(release_year, level):
    if level=="tract":
        return "2020 Census fixed subcounty population" if release_year>=2024 else "2010 Census fixed subcounty population"
    return "annual county population estimate"

def ci_era(release_year):
    return "2023+ revised simulation/random-effect treatment" if release_year>=2023 else "pre-2023"

def source_eligibility(definition):
    if not definition:
        return "Not separately stated in frozen Socrata measure text"
    lower=definition.lower()
    marker=" among "
    idx=lower.rfind(marker)
    if idx>=0:
        return definition[idx+len(marker):].strip()
    return "Not separately stated in frozen Socrata measure text"

rows=read_jsonl(COVERAGE)
rows.sort(key=lambda r:(r["geography_level"],r["measureid"],r["datavaluetypeid"],r["release_year"],str(r["year"])))

history={}
out=[]
for r in rows:
    key=(r["geography_level"],r["measureid"],r["datavaluetypeid"])
    prev=history.get(key)
    source_year=int(r["year"]) if r.get("year") not in (None,"") else None
    if source_year is None:
        raise ValueError(f"unresolved source year: {r}")

    breaks=[]
    definition_status="unresolved"
    geo_status="unresolved"
    predecessor=None
    carried=False
    classification="new source wave"

    if prev and prev["release_year"]==r["release_year"]-1:
        predecessor=f'{prev["release_year"]}:{prev["dataset_id"]}:{prev["measureid"]}:{prev["datavaluetypeid"]}'
        carried=prev["brfss_source_year"]==source_year
        classification="ambiguous" if carried else "new source wave"
        if prev["exact_definition"]==r["measure"]:
            definition_status="comparable"
        else:
            definition_status="break"
            breaks.append("measure-definition")

        if prev["geography_vintage"]==geography_vintage(r["release_year"],r["geography_level"]) and prev["product"]==r["product"]:
            geo_status="comparable"
        else:
            geo_status="break"
            if prev["product"]!=r["product"]:
                breaks.append("product-scope")
            if prev["geography_vintage"]!=geography_vintage(r["release_year"],r["geography_level"]):
                breaks.append("geography-or-vintage")
    else:
        definition_status="unresolved"
        geo_status="unresolved"

    rec={
        "release_year":r["release_year"],
        "product":r["product"],
        "dataset_id":r["dataset_id"],
        "geography_level":r["geography_level"],
        "geography_vintage":geography_vintage(r["release_year"],r["geography_level"]),
        "measure_id":r["measureid"],
        "display_name":r.get("short_question_text") or r.get("measure"),
        "exact_definition":r.get("measure"),
        "target_population":source_eligibility(r.get("measure")),
        "eligibility":source_eligibility(r.get("measure")),
        "data_value_type":r.get("data_value_type") or r.get("datavaluetypeid"),
        "brfss_source_year":source_year,
        "carried_forward_flag":carried,
        "predecessor":predecessor,
        "exact_copy_percentage":None,
        "common_geography_count":None,
        "coverage_change":None if prev is None else f'{r["row_count"]-prev["row_count"]:+d} grouped-row records versus predecessor cell',
        "poststratification_population_base":poststrat_base(r["release_year"],r["geography_level"]),
        "confidence_interval_method_era":ci_era(r["release_year"]),
        "definition_comparability":definition_status,
        "geography_population_comparability":geo_status,
        "documentation_source":f'Frozen CDC/Socrata coverage snapshot {r["coverage_snapshot_sha256"]}',
        "verification_note":"Exact measure definition and source year observed directly in frozen grouped CDC response. Target-population/eligibility text is extracted only from the source measure wording after 'among' when present; otherwise it is explicitly marked not separately stated. Row-level exact-copy/common-geography diagnostics are applied separately.",
        "carry_forward_classification":classification,
        "comparability_breaks":sorted(set(breaks)),
    }
    out.append(rec)
    history[key]=rec | {"row_count":r["row_count"],"measureid":r["measureid"],"datavaluetypeid":r["datavaluetypeid"]}

OUT.write_text("".join(json.dumps(r,sort_keys=True)+"\n" for r in out))
print(json.dumps({
    "records":len(out),
    "carried_forward_candidates":sum(r["carried_forward_flag"] for r in out),
    "definition_breaks":sum("measure-definition" in r["comparability_breaks"] for r in out),
    "product_scope_breaks":sum("product-scope" in r["comparability_breaks"] for r in out),
    "geography_breaks":sum("geography-or-vintage" in r["comparability_breaks"] for r in out),
},sort_keys=True))
