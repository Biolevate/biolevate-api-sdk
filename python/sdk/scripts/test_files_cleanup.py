#!/usr/bin/env python3
"""Clean up test artifacts created by test_files.py.

Reads state from test-reports/files-test-state.json (written by test_files.py
after the create/index/ontologies/reindex/recompute flow), then deletes the
indexed file and the provider item and folder. Run this after test_files.py
so that async reindex/recompute on the server are not interrupted by immediate
deletion in the same run.
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from scripts.common import create_client, get_base_parser

DEFAULT_STATE_FILE = Path("test-reports/files-test-state.json")


async def main() -> int:
    parser = get_base_parser("Clean up Files test artifacts")
    parser.add_argument(
        "--state-file",
        type=Path,
        default=DEFAULT_STATE_FILE,
        help=f"Path to state JSON from test_files.py (default: {DEFAULT_STATE_FILE})",
    )
    parser.add_argument(
        "--remove-state",
        action="store_true",
        help="Delete the state file after successful cleanup",
    )
    args = parser.parse_args()

    state_path = args.state_file.resolve()
    if not state_path.is_file():
        print("No state file found; nothing to clean.", file=sys.stderr)
        return 0

    try:
        state = json.loads(state_path.read_text())
    except (json.JSONDecodeError, OSError) as e:
        print(f"Failed to read state file: {e}", file=sys.stderr)
        return 1

    provider_id = state.get("provider_id")
    file_id = state.get("file_id")
    key = state.get("key")
    folder_name = state.get("folder_name")

    if not file_id or not provider_id:
        print("State file missing provider_id or file_id; nothing to clean.", file=sys.stderr)
        return 0

    client = create_client(args)
    async with client:
        if file_id:
            try:
                await client.files.delete(file_id)
                print(f"Deleted indexed file: {file_id}")
            except Exception as e:
                print(f"Warning: files.delete failed: {e}", file=sys.stderr)

        if key:
            try:
                await client.items.delete(
                    provider_id,
                    key=key,
                )
                print(f"Deleted provider file: {key}")
            except Exception as e:
                print(f"Warning: items.delete file failed: {e}", file=sys.stderr)

        if folder_name:
            try:
                await client.items.delete(
                    provider_id,
                    key=f"{folder_name}/",
                )
                print(f"Deleted provider folder: {folder_name}/")
            except Exception as e:
                print(f"Warning: items.delete folder failed: {e}", file=sys.stderr)

    if args.remove_state:
        try:
            state_path.unlink()
            print("Removed state file.")
        except OSError as e:
            print(f"Warning: could not remove state file: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
