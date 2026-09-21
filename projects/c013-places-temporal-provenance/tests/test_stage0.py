from pathlib import Path
import json, hashlib, tempfile, pytest
from c013_places.core import *
from c013_places.pipeline import read_jsonl,validate_project
ROOT=Path(__file__).resolve().parents[1]
def test_required_manifest_fields():
    for r in read_jsonl(ROOT/'data/manifests/retrieval_manifest.jsonl'): validate_retrieval(r)
def test_required_crosswalk_fields_and_unique_key():
    rows=read_jsonl(ROOT/'outputs/machine/preliminary_provenance_crosswalk.jsonl')
    for r in rows: validate_crosswalk(r)
    unique_keys(rows)
def test_permitted_categories():
    assert classify_carry_forward(True,100)=='exact carry-forward'
    assert classify_carry_forward(True,99.5)=='revised carry-forward'
    assert classify_carry_forward(True,99.49)=='ambiguous'
    assert classify_carry_forward(True,99.9,exact_only=True)=='ambiguous'
    assert classify_carry_forward(False,100)=='new source wave'
def test_dataset_id_and_sha():
    r=read_jsonl(ROOT/'data/manifests/retrieval_manifest.jsonl')[0]
    assert DATASET_RE.match(r['dataset_id']) and SHA_RE.match(r['sha256'])
def test_utc_timestamp():
    for r in read_jsonl(ROOT/'data/manifests/retrieval_manifest.jsonl'): parse_utc(r['retrieved_at_utc'])
    with pytest.raises(ValueError): parse_utc('2026-09-21T12:00:00-05:00')
def test_missing_source_year_rejected():
    r=read_jsonl(ROOT/'outputs/machine/preliminary_provenance_crosswalk.jsonl')[0].copy(); r['brfss_source_year']=None
    with pytest.raises(ValueError): validate_crosswalk(r)
def test_conflicting_source_year_can_be_flagged_without_guessing():
    r=read_jsonl(ROOT/'outputs/machine/preliminary_provenance_crosswalk.jsonl')[0].copy(); r['comparability_breaks']=['unresolved-or-conflicting-documentation']; r['carry_forward_classification']='ambiguous'; validate_crosswalk(r)
def test_comparability_logic():
    assert comparability_status([])=='comparable'; assert comparability_status(['geography-or-vintage'])=='break'
    with pytest.raises(ValueError): comparability_status(['invented'])
def test_duplicate_retrieval_detected_by_pipeline_semantics():
    rows=read_jsonl(ROOT/'data/manifests/retrieval_manifest.jsonl'); pairs=[(r['dataset_id'],r['snapshot_id']) for r in rows]; assert len(pairs)==len(set(pairs))
def test_raw_snapshot_immutability():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'x'; assert immutable_write(p,b'a') is True; assert immutable_write(p,b'a') is False
        with pytest.raises(FileExistsError): immutable_write(p,b'b')
def test_frozen_protocol_integrity():
    exp=(ROOT/'protocol/PROTOCOL_SHA256').read_text().split()[0]; assert sha256_file(ROOT/'protocol/C013_CONTROLLED_EXECUTION_PROTOCOL.md')==exp
def test_canonical_v028_consistency():
    m=json.loads((ROOT.parents[1]/'research/canonical/MANIFEST.json').read_text()); assert m['canonical_version']=='0.28.0'; assert m['file_count_including_manifest']==25
    assert len(m['canonical_files'])==24
    for fn,exp in m['sha256'].items(): assert sha256_file(ROOT.parents[1]/'research/canonical'/fn)==exp
def test_deterministic_fixture_serialization():
    rows=read_jsonl(ROOT/'outputs/machine/preliminary_provenance_crosswalk.jsonl'); a=''.join(json.dumps(r,sort_keys=True)+'\\n' for r in rows).encode(); b=''.join(json.dumps(r,sort_keys=True)+'\\n' for r in rows).encode(); assert hashlib.sha256(a).digest()==hashlib.sha256(b).digest()
def test_full_project_validation():
    assert validate_project(ROOT)=={'retrieval_records':16,'crosswalk_records':128}
