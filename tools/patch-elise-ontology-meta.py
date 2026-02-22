#!/usr/bin/env python3
"""Re-apply meta_value type override after OpenAPI codegen.

The backend returns metaValue as an arbitrary Java-serialized value (object,
array, string, etc.). The generator emits Optional[Dict[str, Any]] for
type: object; we override to Optional[Any] so any JSON value is accepted.

Run after: make generate-python
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TARGET = REPO_ROOT / "python/client/biolevate_client/models/elise_ontology_meta.py"

OLD = '    meta_value: Optional[Dict[str, Any]] = Field(default=None, alias="metaValue")'
NEW = '    meta_value: Optional[Any] = Field(default=None, alias="metaValue")'


def main() -> int:
    if not TARGET.is_file():
        print(f"Target not found: {TARGET}", file=sys.stderr)
        return 1
    text = TARGET.read_text()
    if NEW in text:
        print("Patch already applied.")
        return 0
    if OLD not in text:
        print("Target line not found; generator output may have changed.", file=sys.stderr)
        return 1
    TARGET.write_text(text.replace(OLD, NEW, 1))
    print("Patched meta_value to Optional[Any].")
    return 0


if __name__ == "__main__":
    sys.exit(main())
