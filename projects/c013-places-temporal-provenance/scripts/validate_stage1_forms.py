#!/usr/bin/env python3
"""Validate C013 Stage 1 dual-human coding CSVs without making scientific judgments."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "docs" / "coding" / "STAGE1_CODING_SCHEMA.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def validate(path: Path, allow_incomplete: bool = False) -> list[str]:
    schema = load_schema()
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
        fieldnames = list(rows[0].keys()) if rows else []

    missing_columns = [c for c in schema["required_columns"] if c not in fieldnames]
    extra_columns = [c for c in fieldnames if c not in schema["required_columns"]]
    if missing_columns:
        errors.append(f"missing columns: {missing_columns}")
    if extra_columns:
        errors.append(f"unexpected columns: {extra_columns}")

    expected_ids = schema["corpus_ids"]
    ids = [r.get("work_id", "") for r in rows]
    if len(rows) != len(expected_ids):
        errors.append(f"expected {len(expected_ids)} rows, found {len(rows)}")
    if sorted(ids) != sorted(expected_ids):
        errors.append(f"work_id set mismatch: {ids}")
    if len(ids) != len(set(ids)):
        errors.append("duplicate work_id values")

    enums = schema["enums"]
    for i, row in enumerate(rows, start=2):
        for field, allowed in enums.items():
            if field == "binary_or_unclear":
                continue
            value = row.get(field, "")
            if value and value not in allowed:
                errors.append(f"row {i} {field}: invalid value {value!r}")
        for field in [
            "discl_dataset_product","discl_release_years","discl_dataset_ids",
            "discl_source_years","discl_modeled_estimate_status",
            "discl_carry_forward_rotation","discl_definition_change",
            "discl_geography_population_change","discl_uncertainty_dependence"
        ]:
            value = row.get(field, "")
            if value and value not in enums["binary_or_unclear"]:
                errors.append(f"row {i} {field}: invalid value {value!r}")

        if not allow_incomplete and row.get("coding_status") != "complete_locked":
            errors.append(f"row {i}: coding_status must be complete_locked")
        if row.get("coding_status") == "complete_locked":
            required_completed = [
                "evidence_access","eligibility","eligibility_basis",
                "temporal_role_primary","dataset_product_reported",
                "source_mapping_completeness","year_semantics",
                "provenance_disclosure","decision_language_level",
                "causal_language_flag","primary_fragility","coder_confidence"
            ]
            for field in required_completed:
                if not row.get(field):
                    errors.append(f"row {i}: locked row missing {field}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--allow-incomplete", action="store_true")
    args = parser.parse_args()

    path = args.csv_path.resolve()
    errors = validate(path, allow_incomplete=args.allow_incomplete)
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print(f"OK: {path}")
    print(f"SHA256: {sha256(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
