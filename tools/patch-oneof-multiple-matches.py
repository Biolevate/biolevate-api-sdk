#!/usr/bin/env python3
"""Patch generated oneOf classes to accept first match instead of failing on multiple matches.

OpenAPI Generator's Python client raises ValueError when multiple oneOf schemas match,
which happens when schemas share optional fields. This patch changes the behavior to
use the first successful match.

Run after `make generate-python`.
"""

from pathlib import Path

CLIENT_MODELS_DIR = Path(__file__).resolve().parent.parent / "python" / "client" / "biolevate_client" / "models"

OLD_BLOCK = '''        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into '''

NEW_BLOCK = '''        if match > 1:
            # More than 1 match - use first successful parse (patched behavior)
            pass  # raise ValueError("Multiple matches found when deserializing the JSON string into '''


def patch_file(path: Path) -> bool:
    """Patch a single file. Returns True if patched."""
    content = path.read_text()
    
    if OLD_BLOCK not in content:
        return False
    
    if "# More than 1 match - use first successful parse (patched behavior)" in content:
        return False
    
    new_content = content.replace(OLD_BLOCK, NEW_BLOCK)
    
    if new_content != content:
        path.write_text(new_content)
        return True
    return False


def main() -> int:
    if not CLIENT_MODELS_DIR.is_dir():
        print(f"Models directory not found: {CLIENT_MODELS_DIR}")
        return 1
    
    patched = []
    for py_file in CLIENT_MODELS_DIR.glob("*.py"):
        if patch_file(py_file):
            patched.append(py_file.name)
    
    if patched:
        print(f"Patched {len(patched)} files with oneOf multiple-match fix:")
        for name in sorted(patched):
            print(f"  - {name}")
    else:
        print("No files needed patching (already patched or no oneOf issues).")
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
