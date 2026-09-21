#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COVERAGE=ROOT/"outputs/machine/measure_coverage.jsonl"
RAW=ROOT/"data/raw/carry_forward_pages"
DIAG=ROOT/"outputs/machine/carry_forward_diagnostics.jsonl"
QMAN=ROOT/"data/manifests/carry_forward_query_manifest.jsonl"

def read_jsonl(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]

def now_utc():
    return datetime.now(timezone.utc).isoformat().replace("+00:00","Z")

def geo_fields(release_year, level):
    if level=="county":
        return ["stateabbr","locationname"]
    if level=="tract" and release_year<=2019:
        return ["uniqueid"]
    return ["locationid"]

def norm_num(x):
    if x in (None,"","NA","null"):
        return None
    try:
        return Decimal(str(x))
    except InvalidOperation:
        return str(x)

def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":"c013-stage0-provenance/0.4 research"})
    last=None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req,timeout=90) as r:
                return r.read(),int(r.status),r.headers.get("Content-Type")
        except (TimeoutError,urllib.error.URLError) as exc:
            last=exc
            if attempt<3:
                time.sleep(2**attempt)
    raise last

def cell_descriptor(r):
    return {
        "release_year":r["release_year"],
        "dataset_id":r["dataset_id"],
        "geography_level":r["geography_level"],
        "measure_id":r["measureid"],
        "data_value_type_id":r["datavaluetypeid"],
        "data_value_type":r.get("data_value_type"),
        "brfss_source_year":int(r["year"]),
    }

def fetch_cell(r):
    did=r["dataset_id"]
    gfs=geo_fields(r["release_year"],r["geography_level"])
    select=",".join(gfs+["data_value","low_confidence_limit","high_confidence_limit"])
    where=(
        f"measureid='{r['measureid']}' AND datavaluetypeid='{r['datavaluetypeid']}' "
        f"AND year='{r['year']}' AND " + " AND ".join(f"{gf} IS NOT NULL" for gf in gfs)
    )
    base=f"https://data.cdc.gov/resource/{did}.csv"
    limit=50000
    offset=0
    values={}
    page_shas=[]
    raw_hasher=hashlib.sha256()
    total_bytes=0
    retrieval_time=now_utc()
    page_records=[]
    while True:
        params={"$select":select,"$where":where,"$order":",".join(gfs),"$limit":str(limit),"$offset":str(offset)}
        url=base+"?"+urllib.parse.urlencode(params)
        raw,status,content_type=get(url)
        sha=hashlib.sha256(raw).hexdigest()
        page_shas.append(sha)
        raw_hasher.update(len(raw).to_bytes(8,"big"))
        raw_hasher.update(raw)
        total_bytes+=len(raw)
        cell_name=f"{r['release_year']}_{r['measureid']}_{r['datavaluetypeid']}_{r['year']}"
        rel=Path("data/raw/carry_forward_pages")/did/cell_name/f"offset_{offset}.{sha}.csv.gz"
        out=ROOT/rel
        out.parent.mkdir(parents=True,exist_ok=True)
        packed=gzip.compress(raw,compresslevel=9,mtime=0)
        if out.exists() and out.read_bytes()!=packed:
            raise RuntimeError(f"immutable raw-page collision: {rel}")
        if not out.exists():
            out.write_bytes(packed)
        reader=list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
        for row in reader:
            key="|".join(str(row.get(gf,"")) for gf in gfs)
            if key in values:
                raise ValueError(f"duplicate geography key {key} in {cell_name}")
            values[key]=(norm_num(row.get("data_value")),norm_num(row.get("low_confidence_limit")),norm_num(row.get("high_confidence_limit")))
        page_records.append({"offset":offset,"rows":len(reader),"sha256":sha,"snapshot_id":str(rel).replace("\\","/"),"url":url})
        if len(reader)<limit:
            break
        offset+=limit
    manifest=cell_descriptor(r)|{
        "geography_id_fields":gfs,
        "retrieved_at_utc":retrieval_time,
        "rows":len(values),
        "raw_bytes":total_bytes,
        "combined_raw_sha256":raw_hasher.hexdigest(),
        "pages":page_records,
    }
    return values,manifest

rows=read_jsonl(COVERAGE)
by_key={(r["geography_level"],r["measureid"],r["datavaluetypeid"],r["release_year"]):r for r in rows}
candidates=[]
for cur in rows:
    prev=by_key.get((cur["geography_level"],cur["measureid"],cur["datavaluetypeid"],cur["release_year"]-1))
    if prev and str(prev.get("year"))==str(cur.get("year")):
        candidates.append((prev,cur))
candidates.sort(key=lambda pair:(pair[1]["release_year"],pair[1]["geography_level"],pair[1]["measureid"],pair[1]["datavaluetypeid"]))

ap=argparse.ArgumentParser()
ap.add_argument("--max-pairs",type=int,default=None)
args=ap.parse_args()
if args.max_pairs is not None:
    candidates=candidates[:args.max_pairs]

diagnostics=[]
query_manifest=[]
for i,(prev,cur) in enumerate(candidates,1):
    print(f"[{i}/{len(candidates)}] {cur['release_year']} {cur['geography_level']} {cur['measureid']} {cur['datavaluetypeid']} source={cur['year']}",flush=True)
    a,ma=fetch_cell(prev)
    b,mb=fetch_cell(cur)
    query_manifest.extend([ma,mb])
    common=set(a)&set(b)
    comparable=[g for g in common if None not in a[g] and None not in b[g]]
    exact=sum(a[g]==b[g] for g in comparable)
    pct=(100.0*exact/len(comparable)) if comparable else None
    if pct==100.0:
        cls="exact carry-forward"
    elif pct is not None and pct>=99.5:
        cls="revised carry-forward"
    else:
        cls="ambiguous"
    diagnostics.append({
        "predecessor":cell_descriptor(prev),
        "current":cell_descriptor(cur),
        "predecessor_rows":len(a),
        "current_rows":len(b),
        "common_geography_count":len(common),
        "comparable_common_geography_count":len(comparable),
        "predecessor_only_count":len(set(a)-set(b)),
        "current_only_count":len(set(b)-set(a)),
        "exact_equal_count":exact,
        "exact_copy_percentage":pct,
        "carry_forward_classification":cls,
        "predecessor_query_sha256":ma["combined_raw_sha256"],
        "current_query_sha256":mb["combined_raw_sha256"],
    })

DIAG.write_text("".join(json.dumps(r,sort_keys=True)+"\n" for r in diagnostics))
QMAN.write_text("".join(json.dumps(r,sort_keys=True)+"\n" for r in query_manifest))
print(json.dumps({
    "pairs":len(diagnostics),
    "exact":sum(r["carry_forward_classification"]=="exact carry-forward" for r in diagnostics),
    "revised":sum(r["carry_forward_classification"]=="revised carry-forward" for r in diagnostics),
    "ambiguous":sum(r["carry_forward_classification"]=="ambiguous" for r in diagnostics),
    "diagnostics_sha256":hashlib.sha256(DIAG.read_bytes()).hexdigest(),
    "query_manifest_sha256":hashlib.sha256(QMAN.read_bytes()).hexdigest(),
},sort_keys=True))
