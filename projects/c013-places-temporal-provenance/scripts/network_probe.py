#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, urllib.parse, urllib.request\nfrom concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'config/dataset_anchors.json').read_text())
OUT=ROOT/'outputs'/'machine'/'network_probe.json'

def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'c013-stage0-provenance/0.2 research'})
    with urllib.request.urlopen(req,timeout=20) as r:
        body=r.read()
        return body,r.status,r.headers.get('Content-Type')

def call(url):
    try:
        body,status,ct=get(url)
        parsed=json.loads(body)
        return {'ok':True,'url':url,'status':status,'content_type':ct,'bytes':len(body),
                'sha256':hashlib.sha256(body).hexdigest(),'json':parsed}
    except Exception as e:
        return {'ok':False,'url':url,'error':type(e).__name__+': '+str(e)}

def probe_anchor(a):
    did=a['dataset_id']
    urls={
        'meta':f'https://data.cdc.gov/api/views/{did}',
        'count':f'https://data.cdc.gov/resource/{did}.json?%24select=count%28%2A%29',
        'sample':f'https://data.cdc.gov/resource/{did}.json?%24limit=1'
    }
    with ThreadPoolExecutor(max_workers=3) as inner:
        futures={inner.submit(call,url):name for name,url in urls.items()}
        got={futures[future]:future.result() for future in as_completed(futures)}
    meta,count,sample=got['meta'],got['count'],got['sample']
    fields=[]
    title=None
    if meta['ok']:
        title=meta['json'].get('name')
        fields=[col.get('fieldName') for col in meta['json'].get('columns',[]) if col.get('fieldName')]
    row_count=None
    if count['ok'] and isinstance(count['json'],list) and count['json']:
        row_count=count['json'][0].get('count')
    sample_keys=[]
    if sample['ok'] and isinstance(sample['json'],list) and sample['json']:
        sample_keys=sorted(sample['json'][0].keys())
    return {
        'release_year':a['release_year'],'product':a['product'],'geography_level':a['geography_level'],
        'dataset_id':did,'title':title,'metadata_ok':meta['ok'],'count_ok':count['ok'],
        'sample_ok':sample['ok'],'row_count':row_count,'metadata_sha256':meta.get('sha256'),
        'metadata_bytes':meta.get('bytes'),'field_names':fields,'sample_keys':sample_keys,
        'errors':[x.get('error') for x in (meta,count,sample) if not x['ok']]
    }

with ThreadPoolExecutor(max_workers=8) as pool:
    records=list(pool.map(probe_anchor,CFG['anchors']))
OUT.write_text(json.dumps({'retrieved_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
                           'records':records},indent=2,sort_keys=True)+'\n')
for r in records:
    print(json.dumps({k:r[k] for k in ('release_year','geography_level','dataset_id','metadata_ok','count_ok','sample_ok','row_count','metadata_bytes','title','errors')},sort_keys=True))
print('probe_sha256',hashlib.sha256(OUT.read_bytes()).hexdigest())
