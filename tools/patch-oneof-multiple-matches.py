#!/usr/bin/env python3
"""Patch generated oneOf classes to return the first successful parse.

OpenAPI Generator's Python client raises ValueError when multiple oneOf schemas
match, which happens when schemas share optional fields. This patch returns as
soon as the first schema deserializes successfully instead of trying all variants.

Run after `make generate-python`.
"""

from __future__ import annotations

from pathlib import Path

CLIENT_MODELS_DIR = (
    Path(__file__).resolve().parent.parent / "python" / "client" / "biolevate_client" / "models"
)

MATCH_INCREMENT = """            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))"""

RETURN_ON_MATCH = """            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))"""

FROM_JSON_MARKER = "def from_json(cls, json_str: str)"
TAIL_IF_MATCH = "        if match > 1:"
TAIL_ELIF_MATCH = "        elif match == 0:"
TAIL_ELSE_RETURN = "        else:\n            return instance"


def patch_from_json_method(method: str) -> str | None:
    """Patch a from_json method body. Returns None if unchanged."""
    if MATCH_INCREMENT not in method:
        return None

    updated = method.replace(MATCH_INCREMENT, RETURN_ON_MATCH)

    if_match = updated.find(TAIL_IF_MATCH)
    elif_match = updated.find(TAIL_ELIF_MATCH, if_match)
    else_match = updated.find(TAIL_ELSE_RETURN, elif_match)
    if if_match == -1 or elif_match == -1 or else_match == -1:
        return None

    elif_body_start = updated.find("\n", elif_match) + 1
    raise_line = None
    for line in updated[elif_body_start:else_match].splitlines():
        stripped = line.strip()
        if stripped.startswith("raise ValueError"):
            raise_line = stripped
            break
    if raise_line is None:
        return None

    tail = f"\n        # no match\n        {raise_line}\n"
    updated = updated[:if_match] + tail + updated[else_match + len(TAIL_ELSE_RETURN) :]

    if updated == method:
        return None
    return updated


def patch_file(path: Path) -> bool:
    """Patch a single file. Returns True if changed."""
    content = path.read_text()
    marker = content.find(FROM_JSON_MARKER)
    if marker == -1:
        return False

    next_method = content.find("\n    def ", marker + 1)
    if next_method == -1:
        next_method = len(content)

    method = content[marker:next_method]
    patched_method = patch_from_json_method(method)
    if patched_method is None:
        return False

    path.write_text(content[:marker] + patched_method + content[next_method:])
    return True


def main() -> int:
    if not CLIENT_MODELS_DIR.is_dir():
        print(f"Models directory not found: {CLIENT_MODELS_DIR}")
        return 1

    patched = []
    for py_file in sorted(CLIENT_MODELS_DIR.glob("*.py")):
        if patch_file(py_file):
            patched.append(py_file.name)

    if patched:
        print(f"Patched {len(patched)} files with oneOf first-match fix:")
        for name in patched:
            print(f"  - {name}")
    else:
        print("No files needed patching (already patched or no oneOf issues).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
