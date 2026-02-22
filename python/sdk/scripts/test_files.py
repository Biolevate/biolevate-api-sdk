#!/usr/bin/env python3
"""Integration tests for the Files resource.

Does not delete the created file or provider item so that async reindex/recompute
on the server are not interrupted. After this run, use test_files_cleanup.py
to remove test artifacts (reads test-reports/files-test-state.json).
"""

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import Any, TYPE_CHECKING

from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner

if TYPE_CHECKING:
    from biolevate.resources.files import FilesResource


def _default_test_resources_dir() -> Path:
    return Path(__file__).resolve().parent / "test_resources"


def _pick_test_file(test_files_dir: Path, test_file_path: Path | None) -> Path | None:
    if test_file_path is not None:
        if test_file_path.is_file():
            return test_file_path
        return None
    if not test_files_dir.is_dir():
        return None
    for ext in (".pdf", ".txt"):
        for p in sorted(test_files_dir.glob(f"*{ext}")):
            if p.is_file():
                return p
    return None


def _mime_type_for_path(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "application/pdf"
    if suffix == ".txt":
        return "text/plain"
    return "application/octet-stream"


async def wait_until_indexed(
    files_resource: FilesResource,
    file_id: str,
    timeout_seconds: float,
    initial_interval: float = 2.0,
    max_interval: float = 10.0,
) -> tuple[bool, float]:
    elapsed = 0.0
    interval = initial_interval
    while elapsed < timeout_seconds:
        file_info = await files_resource.get(file_id)
        if getattr(file_info, "indexed", None) is True:
            return True, elapsed
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 2, max_interval)
    return False, elapsed


async def wait_until_ontologies_ready(
    files_resource: FilesResource,
    file_id: str,
    timeout_seconds: float,
    initial_interval: float = 2.0,
    max_interval: float = 10.0,
) -> tuple[bool, float]:
    elapsed = 0.0
    interval = initial_interval
    while elapsed < timeout_seconds:
        ontologies = await files_resource.get_ontologies(file_id)
        if isinstance(ontologies, list) and len(ontologies) > 0:
            return True, elapsed
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 2, max_interval)
    return False, elapsed


async def main() -> None:
    parser = get_base_parser("Test Files resource")
    parser.add_argument(
        "--test-files-dir",
        type=Path,
        default=None,
        help="Directory containing test files (default: scripts/test_resources)",
    )
    parser.add_argument(
        "--test-file",
        type=Path,
        default=None,
        help="Path to a single test file to upload",
    )
    parser.add_argument(
        "--index-timeout",
        type=float,
        default=120.0,
        help="Max seconds to wait for file indexation (default: 120)",
    )
    parser.add_argument(
        "--ontology-timeout",
        type=float,
        default=120.0,
        help="Max seconds to wait for ontologies to be computed (default: 120)",
    )
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="files", api_url=args.api_url)

    test_files_dir = args.test_files_dir or _default_test_resources_dir()
    test_file_path: Path | None = _pick_test_file(test_files_dir, args.test_file)

    provider_id: str | None = None
    test_folder_name = f"SDK-TEST-FILES-{int(time.time())}"
    uploaded_path: str | None = None
    uploaded_name: str | None = None
    file_id: str | None = None

    async with client:
        async def test_setup() -> dict[str, Any]:
            nonlocal provider_id
            result = await client.providers.list(page=0, page_size=1)
            if result.data and len(result.data) > 0:
                provider = result.data[0]
                provider_id = str(provider.id.id) if provider.id else None
                return {"provider_id": provider_id, "provider_name": provider.name}
            raise AssertionError("No providers available for testing")

        await runner.run_test(
            name="setup_get_provider",
            test_fn=test_setup,
            expected_message="Found provider for files testing",
        )

        if not provider_id:
            runner.skip_test("list_files", "No provider available")
            runner.skip_test("pick_test_file", "No provider available")
            runner.print_and_save()
            return

        async def test_list_files() -> dict[str, Any]:
            result = await client.files.list(
                provider_id, page=0, page_size=10  # type: ignore[arg-type]
            )
            assert result.data is not None, "data should not be None"
            assert isinstance(result.data, list), "data should be a list"
            return {
                "total_elements": result.total_elements,
                "total_pages": result.total_pages,
                "count": len(result.data) if result.data else 0,
            }

        await runner.run_test(
            name="list_files",
            test_fn=test_list_files,
            expected_message="Listed files for provider",
        )

        if test_file_path is None:
            runner.skip_test("pick_test_file", "No test file in test_resources")
            for name in (
                "upload_test_file",
                "create_file",
                "wait_until_indexed",
                "wait_until_ontologies",
                "get_ontologies",
                "get_file",
                "reindex",
                "recompute_ontologies",
            ):
                runner.skip_test(name, "No test file available")
        else:
            async def test_pick_test_file() -> dict[str, Any]:
                return {"test_file": str(test_file_path), "name": test_file_path.name}

            await runner.run_test(
                name="pick_test_file",
                test_fn=test_pick_test_file,
                expected_message="Picked test file for upload",
            )

            async def test_upload_test_file() -> dict[str, Any]:
                nonlocal uploaded_path, uploaded_name
                with open(test_file_path, "rb") as f:
                    await client.items.upload(
                        provider_id,  # type: ignore[arg-type]
                        path=f"/{test_folder_name}",
                        file=f,
                        file_name=test_file_path.name,
                        mime_type=_mime_type_for_path(test_file_path),
                    )
                uploaded_path = f"/{test_folder_name}"
                uploaded_name = test_file_path.name
                return {
                    "path": uploaded_path,
                    "name": uploaded_name,
                    "folder": test_folder_name,
                }

            await runner.run_test(
                name="upload_test_file",
                test_fn=test_upload_test_file,
                expected_message=f"Uploaded {test_file_path.name} to provider",
            )

            async def test_create_file() -> dict[str, Any]:
                nonlocal file_id
                assert uploaded_path is not None and uploaded_name is not None
                file_info = await client.files.create(
                    provider_id, uploaded_path, uploaded_name  # type: ignore[arg-type]
                )
                file_id = str(file_info.id.id) if file_info.id else None
                assert file_id, "File ID should be set"
                return {
                    "file_id": file_id,
                    "indexed": getattr(file_info, "indexed", None),
                }

            await runner.run_test(
                name="create_file",
                test_fn=test_create_file,
                expected_message="Created indexed file",
            )

            if file_id:
                fid: str = file_id
                async def test_wait_until_indexed() -> dict[str, Any]:
                    indexed, waited = await wait_until_indexed(
                        client.files,
                        fid,
                        timeout_seconds=args.index_timeout,
                    )
                    if not indexed:
                        raise AssertionError(
                            f"File not indexed within {args.index_timeout}s (waited {waited:.1f}s)"
                        )
                    return {"indexed": True, "waited_seconds": round(waited, 1)}

                await runner.run_test(
                    name="wait_until_indexed",
                    test_fn=test_wait_until_indexed,
                    expected_message="File indexed",
                )

                async def test_wait_until_ontologies() -> dict[str, Any]:
                    ready, waited = await wait_until_ontologies_ready(
                        client.files,
                        fid,
                        timeout_seconds=args.ontology_timeout,
                    )
                    if not ready:
                        raise AssertionError(
                            f"Ontologies not computed within {args.ontology_timeout}s (waited {waited:.1f}s)"
                        )
                    return {"ontologies_ready": True, "waited_seconds": round(waited, 1)}

                await runner.run_test(
                    name="wait_until_ontologies",
                    test_fn=test_wait_until_ontologies,
                    expected_message="Ontologies computed",
                )

                async def test_get_ontologies() -> dict[str, Any]:
                    ontologies = await client.files.get_ontologies(fid)
                    assert isinstance(ontologies, list), "ontologies should be a list"
                    assert len(ontologies) > 0, "ontologies list must not be empty after wait"
                    return {"count": len(ontologies)}

                await runner.run_test(
                    name="get_ontologies",
                    test_fn=test_get_ontologies,
                    expected_message="Retrieved file ontologies",
                )

                async def test_get_file() -> dict[str, Any]:
                    file_info = await client.files.get(fid)
                    assert getattr(file_info, "indexed", None) is True
                    return {
                        "file_id": fid,
                        "name": getattr(file_info, "name", None),
                        "indexed": getattr(file_info, "indexed", None),
                    }

                await runner.run_test(
                    name="get_file",
                    test_fn=test_get_file,
                    expected_message="Retrieved file by ID",
                )

                async def test_reindex() -> dict[str, Any]:
                    await client.files.reindex(fid)
                    return {"triggered": True}

                await runner.run_test(
                    name="reindex",
                    test_fn=test_reindex,
                    expected_message="Triggered reindex",
                )

                async def test_recompute_ontologies() -> dict[str, Any]:
                    await client.files.recompute_ontologies(fid)
                    return {"triggered": True}

                await runner.run_test(
                    name="recompute_ontologies",
                    test_fn=test_recompute_ontologies,
                    expected_message="Triggered recompute ontologies",
                )

                state_path = Path("test-reports/files-test-state.json")
                state_path.parent.mkdir(parents=True, exist_ok=True)
                state_path.write_text(
                    json.dumps(
                        {
                            "provider_id": provider_id,
                            "file_id": fid,
                            "path": uploaded_path,
                            "name": uploaded_name,
                            "folder_name": test_folder_name,
                        },
                        indent=2,
                    )
                )

        async def test_get_file_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.files.get("00000000-0000-0000-0000-000000000000")
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_file_not_found",
            test_fn=test_get_file_not_found,
            expected_message="NotFoundError raised for non-existent file",
        )

        async def test_delete_file_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.files.delete("00000000-0000-0000-0000-000000000000")
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="delete_file_not_found",
            test_fn=test_delete_file_not_found,
            expected_message="NotFoundError raised for delete non-existent file",
        )

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
