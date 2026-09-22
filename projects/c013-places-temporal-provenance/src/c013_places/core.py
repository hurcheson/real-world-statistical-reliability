from __future__ import annotations
from datetime import datetime
from pathlib import Path
import hashlib, json, re
DATASET_RE=re.compile(r'^[a-z0-9]{4}-[a-z0-9]{4}$')
SHA_RE=re.compile(r'^[0-9a-f]{64}$')
CARRY={'exact carry-forward','revised carry-forward','new source wave','ambiguous'}
BREAKS={'measure-definition','target-population-or-eligibility','geography-or-vintage','product-scope','poststratification-basis','confidence-interval-method','unresolved-or-conflicting-documentation'}
RETR_REQUIRED=set(['api_endpoint', 'byte_size', 'canonical_url', 'catalog', 'content_type', 'dataset_id', 'documentation_source', 'provider', 'request_parameters', 'result_status', 'retrieval_notes', 'retrieved_at_utc', 'row_count', 'schema_fingerprint', 'sha256', 'snapshot_id', 'snapshot_mode'])
CROSS_REQUIRED=set(['brfss_source_year', 'carried_forward_flag', 'carry_forward_classification', 'common_geography_count', 'comparability_breaks', 'confidence_interval_method_era', 'coverage_change', 'data_value_type', 'dataset_id', 'definition_comparability', 'display_name', 'documentation_source', 'eligibility', 'exact_copy_percentage', 'exact_definition', 'geography_level', 'geography_population_comparability', 'geography_vintage', 'measure_id', 'poststratification_population_base', 'predecessor', 'product', 'release_year', 'target_population', 'verification_note'])
COMPOSITE=('release_year','dataset_id','geography_level','measure_id','data_value_type','brfss_source_year')
def sha256_bytes(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def sha256_file(p:Path)->str:return sha256_bytes(p.read_bytes())
def parse_utc(s:str):
    if not s.endswith('Z'): raise ValueError('timestamp must use UTC Z suffix')
    return datetime.fromisoformat(s[:-1]+'+00:00')
def classify_carry_forward(same_source_wave:bool, exact_pct:float|None, exact_only:bool=False)->str:
    if exact_pct is None:return 'ambiguous' if same_source_wave else 'new source wave'
    if same_source_wave and exact_pct==100.0:return 'exact carry-forward'
    if same_source_wave and not exact_only and exact_pct>=99.5:return 'revised carry-forward'
    return 'new source wave' if not same_source_wave else 'ambiguous'
def comparability_status(breaks:list[str])->str:
    bad=set(breaks)-BREAKS
    if bad: raise ValueError(f'unknown breaks: {bad}')
    return 'break' if breaks else 'comparable'
def validate_retrieval(r:dict):
    miss=RETR_REQUIRED-r.keys()
    if miss: raise ValueError(f'missing retrieval fields: {sorted(miss)}')
    if not DATASET_RE.match(r['dataset_id']):raise ValueError('bad dataset id')
    if not SHA_RE.match(r['sha256']):raise ValueError('bad sha256')
    parse_utc(r['retrieved_at_utc'])
def validate_crosswalk(r:dict):
    miss=CROSS_REQUIRED-r.keys()
    if miss: raise ValueError(f'missing crosswalk fields: {sorted(miss)}')
    if not DATASET_RE.match(r['dataset_id']):raise ValueError('bad dataset id')
    if r['carry_forward_classification'] not in CARRY:raise ValueError('bad carry-forward classification')
    if not set(r['comparability_breaks'])<=BREAKS:raise ValueError('bad comparability break')
    if not isinstance(r['brfss_source_year'],int):raise ValueError('source year unresolved')
def unique_keys(rows:list[dict]):
    seen=set()
    for r in rows:
        key=tuple(r[k] for k in COMPOSITE)
        if key in seen:raise ValueError(f'duplicate crosswalk key: {key}')
        seen.add(key)
def immutable_write(path:Path, data:bytes):
    if path.exists():
        if path.read_bytes()!=data: raise FileExistsError(f'immutable snapshot collision: {path}')
        return False
    path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data); return True
