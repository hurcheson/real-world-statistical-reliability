#!/usr/bin/env python3
"""Network-enabled acquisition helper. Never overwrites raw snapshots.
Stage 0A execution environment could not route HTTP bytes into its local runtime, so this
script is committed for the required retry in Stage 0B or a network-enabled clean room.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, urllib.request
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'config/dataset_anchors.json').read_text())
RAW=ROOT/'data/raw/metadata'
def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'c013-stage0-provenance/0.1 research'})
    with urllib.request.urlopen(req,timeout=90) as r:return r.read(),r.headers.get('Content-Type'),r.status
for a in CFG['anchors']:
    did=a['dataset_id']; url=f'https://data.cdc.gov/api/views/{did}'
    body,ct,status=get(url); sha=hashlib.sha256(body).hexdigest(); out=RAW/f'{did}.{sha}.raw.json'
    if out.exists() and out.read_bytes()!=body: raise RuntimeError('hash/path collision')
    if not out.exists(): out.write_bytes(body)
    print(json.dumps({'dataset_id':did,'url':url,'retrieved_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'status':status,'content_type':ct,'bytes':len(body),'sha256':sha,'path':str(out.relative_to(ROOT))}))
