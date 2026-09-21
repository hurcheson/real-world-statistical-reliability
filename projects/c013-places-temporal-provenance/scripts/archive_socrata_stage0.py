#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "config/dataset_anchors.json").read_text())
RAW = ROOT / "data/raw/network"
MANIFEST = ROOT / "data/manifests/retrieval_manifest.jsonl"
COVERAGE = ROOT / "outputs/machine/measure_coverage.jsonl"

def now_utc():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()

def get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "c013-stage0-provenance/0.3 research"})
    last = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read(), int(r.status), r.headers.get("Content-Type")
        except (TimeoutError, urllib.error.URLError) as exc:
            last = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise last

def snapshot(dataset_id: str, kind: str, url: str):
    body, status, content_type = get(url)
    digest = sha256_bytes(body)
    rel = Path("data/raw/network") / dataset_id / f"{kind}.{digest}.json"
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists() and out.read_bytes() != body:
        raise RuntimeError(f"immutable snapshot collision: {rel}")
    if not out.exists():
        out.write_bytes(body)
    return body, status, content_type, digest, rel

def build_urls(dataset_id: str):
    fields = ["year", "measureid", "measure", "datavaluetypeid", "data_value_type", "short_question_text"]
    select = ",".join(fields) + ",count(*) as row_count"
    group = ",".join(fields)
    query = urllib.parse.urlencode({"$select": select, "$group": group, "$order": "year,measureid,datavaluetypeid"})
    return {
        "metadata": f"https://data.cdc.gov/api/views/{dataset_id}",
        "count": f"https://data.cdc.gov/resource/{dataset_id}.json?%24select=count%28%2A%29",
        "sample": f"https://data.cdc.gov/resource/{dataset_id}.json?%24limit=1",
        "coverage": f"https://data.cdc.gov/resource/{dataset_id}.json?{query}",
    }

def parse_count(body: bytes) -> int:
    obj = json.loads(body)
    return int(obj[0]["count"])

def schema_fingerprint(metadata_body: bytes) -> str:
    obj = json.loads(metadata_body)
    fields = [c.get("fieldName") for c in obj.get("columns", []) if c.get("fieldName")]
    return sha256_bytes("\n".join(sorted(fields)).encode())

def fetch_anchor(anchor: dict):
    did = anchor["dataset_id"]
    urls = build_urls(did)
    got = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {kind: pool.submit(snapshot, did, kind, url) for kind, url in urls.items()}
        for kind, future in futures.items():
            got[kind] = future.result()

    count = parse_count(got["count"][0])
    schema_fp = schema_fingerprint(got["metadata"][0])
    retrieved = now_utc()
    manifest = []
    for kind in ("metadata", "count", "sample", "coverage"):
        body, status, content_type, digest, rel = got[kind]
        manifest.append({
            "provider": "CDC",
            "catalog": "data.cdc.gov / Socrata",
            "dataset_id": did,
            "canonical_url": anchor["catalog_url"],
            "api_endpoint": urls[kind],
            "request_parameters": {"query_kind": kind},
            "retrieved_at_utc": retrieved,
            "result_status": f"HTTP {status}",
            "content_type": content_type,
            "snapshot_id": str(rel).replace("\\", "/"),
            "byte_size": len(body),
            "row_count": count,
            "schema_fingerprint": schema_fp,
            "sha256": digest,
            "documentation_source": anchor["catalog_url"],
            "retrieval_notes": "Direct raw HTTP response archived by GitHub Actions network runner; content-addressed and immutable.",
            "snapshot_mode": "frozen snapshot",
        })

    coverage = json.loads(got["coverage"][0])
    coverage_rows = []
    for row in coverage:
        coverage_rows.append({
            "release_year": anchor["release_year"],
            "product": anchor["product"],
            "geography_level": anchor["geography_level"],
            "dataset_id": did,
            "year": row.get("year"),
            "measureid": row.get("measureid"),
            "measure": row.get("measure"),
            "datavaluetypeid": row.get("datavaluetypeid"),
            "data_value_type": row.get("data_value_type"),
            "short_question_text": row.get("short_question_text"),
            "row_count": int(row.get("row_count", "0")),
            "coverage_snapshot_sha256": got["coverage"][3],
        })
    return manifest, coverage_rows

all_manifest = []
all_coverage = []
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch_anchor, CFG["anchors"]))

for manifest, coverage in results:
    all_manifest.extend(manifest)
    all_coverage.extend(coverage)

all_manifest.sort(key=lambda r: (r["dataset_id"], r["request_parameters"]["query_kind"]))
all_coverage.sort(key=lambda r: (
    r["release_year"], r["geography_level"], r["dataset_id"],
    str(r["year"]), str(r["measureid"]), str(r["datavaluetypeid"])
))

MANIFEST.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in all_manifest))
COVERAGE.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in all_coverage))

print(json.dumps({
    "retrieval_records": len(all_manifest),
    "coverage_records": len(all_coverage),
    "manifest_sha256": sha256_bytes(MANIFEST.read_bytes()),
    "coverage_sha256": sha256_bytes(COVERAGE.read_bytes()),
}, sort_keys=True))
