#!/usr/bin/env python3
"""Patch Dict[str, Any] fields to Any for arbitrary JSON values.

The backend returns certain fields as arbitrary Java-serialized values (object,
array, string, etc.). The generator emits Optional[Dict[str, Any]] for
type: object; we override to Optional[Any] so any JSON value is accepted.

Run after: make generate-python
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = REPO_ROOT / "python/client/biolevate_client/models"

PATCHES: list[tuple[str, str, str]] = [
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
            errors.append(f"{filename}: target line not found; generator output may have changed.")
            continue
        target.write_text(text.replace(old, new, 1))
        patched.append(filename)

    if patched:
        print(f"Patched {len(patched)} files to use Optional[Any]:")
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
