from pathlib import Path
import json
from .core import validate_retrieval, validate_crosswalk, unique_keys, sha256_file

def read_jsonl(path:Path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
def validate_project(root:Path):
    retrieval=read_jsonl(root/'data/manifests/retrieval_manifest.jsonl')
    for r in retrieval: validate_retrieval(r)
    if len({(r['dataset_id'],r['snapshot_id']) for r in retrieval})!=len(retrieval): raise ValueError('duplicate retrieval entry')
    for r in retrieval:
        p=root/r['snapshot_id']; assert p.exists(); assert sha256_file(p)==r['sha256']
    cross=read_jsonl(root/'outputs/machine/preliminary_provenance_crosswalk.jsonl')
    for r in cross: validate_crosswalk(r)
    unique_keys(cross)
    return {'retrieval_records':len(retrieval),'crosswalk_records':len(cross)}
