from pathlib import Path
import json
from .core import validate_retrieval, validate_crosswalk, unique_keys, sha256_file

def read_jsonl(path:Path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]

def validate_project(root:Path):
    retrieval=read_jsonl(root/'data/manifests/retrieval_manifest.jsonl')
    for r in retrieval:
        validate_retrieval(r)
    if len({(r['dataset_id'],r['snapshot_id']) for r in retrieval})!=len(retrieval):
        raise ValueError('duplicate retrieval entry')
    for r in retrieval:
        p=root/r['snapshot_id']
        assert p.exists(), p
        assert sha256_file(p)==r['sha256'], p

    preliminary=read_jsonl(root/'outputs/machine/preliminary_provenance_crosswalk.jsonl')
    for r in preliminary:
        validate_crosswalk(r)
    unique_keys(preliminary)

    result={
        'retrieval_records':len(retrieval),
        'preliminary_crosswalk_records':len(preliminary),
    }

    final_path=root/'outputs/machine/provenance_crosswalk.jsonl'
    diag_path=root/'outputs/machine/carry_forward_diagnostics.jsonl'
    qman_path=root/'data/manifests/carry_forward_query_manifest.jsonl'
    archive_meta_path=root/'outputs/machine/carry_forward_raw_archive.json'

    if final_path.exists():
        final=read_jsonl(final_path)
        for r in final:
            validate_crosswalk(r)
        unique_keys(final)
        result['final_crosswalk_records']=len(final)
        result['carry_forward_rows']=sum(bool(r['carried_forward_flag']) for r in final)
        result['exact_carry_forwards']=sum(r['carry_forward_classification']=='exact carry-forward' for r in final)
        result['revised_carry_forwards']=sum(r['carry_forward_classification']=='revised carry-forward' for r in final)
        result['ambiguous_carry_forwards']=sum(r['carry_forward_classification']=='ambiguous' for r in final)

    if diag_path.exists():
        diag=read_jsonl(diag_path)
        result['carry_forward_diagnostics']=len(diag)
        for d in diag:
            cls=d['carry_forward_classification']
            if cls not in {'exact carry-forward','revised carry-forward','ambiguous'}:
                raise ValueError(f'bad diagnostic classification: {cls}')
            linked=d.get('linkage_status')=='linked common geography'
            if linked:
                assert d['common_geography_count'] is not None
                assert d['comparable_common_geography_count'] is not None
                assert d['exact_copy_percentage'] is not None
            else:
                assert d.get('linkage_status','').startswith('unlinked')
                assert d['common_geography_count'] is None
                assert d['exact_copy_percentage'] is None

    if qman_path.exists():
        qman=read_jsonl(qman_path)
        result['carry_forward_query_records']=len(qman)
        for q in qman:
            assert q['combined_raw_sha256']
            assert q['pages']
            assert q['rows'] >= 0

    if archive_meta_path.exists():
        meta=json.loads(archive_meta_path.read_text())
        archive=root/meta['repository_path'].removeprefix('projects/c013-places-temporal-provenance/')
        assert archive.exists(), archive
        assert archive.stat().st_size==meta['byte_size']
        assert sha256_file(archive)==meta['sha256']
        result['raw_archive_bytes']=meta['byte_size']
        result['raw_archive_sha256']=meta['sha256']

    return result
