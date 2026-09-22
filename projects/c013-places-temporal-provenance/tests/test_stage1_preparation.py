from __future__ import annotations

import csv
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CODING = PROJECT / "docs" / "coding"


def test_stage1_schema_corpus_is_frozen_e1_e9():
    schema = json.loads((CODING / "STAGE1_CODING_SCHEMA.json").read_text(encoding="utf-8"))
    assert schema["corpus_ids"] == [f"E{i}" for i in range(1, 10)]
    assert schema["protocol_sha256"] == "fa87dc628428b9c9b613f20f2fa80769fe16d153e1f749962fc32b2ceb126629"


def _read_form(name: str):
    with (CODING / name).open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def test_coder_forms_are_separate_and_unscored():
    a = _read_form("CODER_A_FORM.csv")
    b = _read_form("CODER_B_FORM.csv")
    assert [r["work_id"] for r in a] == [f"E{i}" for i in range(1, 10)]
    assert [r["work_id"] for r in b] == [f"E{i}" for i in range(1, 10)]
    assert all(r["coder_id"] == "A" for r in a)
    assert all(r["coder_id"] == "B" for r in b)
    assert all(r["coding_status"] == "not_started" for r in a + b)
    for row in a + b:
        assert row["eligibility"] == ""
        assert row["temporal_role_primary"] == ""
        assert row["provenance_disclosure"] == ""
        assert row["decision_language_level"] == ""
        assert row["primary_fragility"] == ""


def test_neutral_registry_contains_no_prior_paper_specific_codes():
    registry = json.loads((CODING / "STAGE1_CORPUS_REGISTRY.json").read_text(encoding="utf-8"))
    forbidden = {"temporal_role","provenance_disclosure","decision_language","primary_fragility","primary_audit_risk"}
    for work in registry["works"]:
        assert forbidden.isdisjoint(work.keys())
