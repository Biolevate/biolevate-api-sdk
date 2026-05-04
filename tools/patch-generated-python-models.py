#!/usr/bin/env python3
"""Patch generated Python models to match backend response shapes.

Some OpenAPI-generated models are stricter than the JSON currently returned by
the backend. Run this after `make generate-python` so regenerated clients keep
accepting nullable IDs and arbitrary JSON values where the API can return them.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "python/client/biolevate_client/models"

PATCHES: list[tuple[str, str, str]] = [
    (
        "elise_ontology.py",
        '    concept_id: EntityId = Field(alias="conceptId")',
        '    concept_id: EntityId | None = Field(default=None, alias="conceptId")',
    ),
    (
        "elise_entity_cell_result.py",
        "    value: Optional[Dict[str, Any]] = None",
        "    value: Optional[Any] = None",
    ),
    (
        "elise_ontology_meta.py",
        '    meta_value: Optional[Dict[str, Any]] = Field(default=None, alias="metaValue")',
        '    meta_value: Optional[Any] = Field(default=None, alias="metaValue")',
    ),
    (
        "elise_meta_result.py",
        '    raw_value: Optional[Dict[str, Any]] = Field(default=None, alias="rawValue")',
        '    raw_value: Optional[Any] = Field(default=None, alias="rawValue")',
    ),
]


def main() -> int:
    patched = []
    skipped = []
    errors = []

    for filename, old, new in PATCHES:
        target = MODELS_DIR / filename
        if not target.is_file():
            errors.append(f"Target not found: {target}")
            continue
        text = target.read_text()
        if new in text:
            skipped.append(filename)
            continue
        if old not in text:
            errors.append(
                f"{filename}: target line not found; generator output may have changed."
            )
            continue
        target.write_text(text.replace(old, new, 1))
        patched.append(filename)

    if patched:
        print(f"Patched {len(patched)} generated model files:")
        for f in patched:
            print(f"  - {f}")
    if skipped:
        print(f"Already patched: {', '.join(skipped)}")
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
