#!/usr/bin/env python3
"""Integration tests for the Collections resource."""

from __future__ import annotations

import asyncio
import time
from typing import Any

from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner


async def main() -> None:
    parser = get_base_parser("Test Collections resource")
    parser.add_argument(
        "--provider-id",
        type=str,
        default=None,
        help="ID of the provider to use (default: first available)",
    )
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="collections", api_url=args.api_url)

    timestamp = int(time.time())
    test_collection_name = f"SDK-TEST-COLL-{timestamp}"
    test_collection_id: str | None = None
    file_id_for_collection: str | None = None

    async with client:

        async def test_setup_file_for_collection() -> dict[str, Any]:
            nonlocal file_id_for_collection
            provider_id: str | None = None
            if args.provider_id:
                provider_id = args.provider_id
            else:
                providers = await client.providers.list(page=0, page_size=1)
                if not providers.data or len(providers.data) == 0:
                    return {"provider_id": None, "file_id": None}
                provider_id = str(providers.data[0].id.id) if providers.data[0].id else None
            if not provider_id:
                return {"provider_id": None, "file_id": None}
            files_page = await client.files.list(provider_id, page=0, page_size=1)
            if files_page.data and len(files_page.data) > 0:
                first_file = files_page.data[0]
                file_id_for_collection = str(first_file.id.id) if first_file.id else None
            return {
                "provider_id": provider_id,
                "file_id": file_id_for_collection,
            }

        await runner.run_test(
            name="setup_file_for_collection",
            test_fn=test_setup_file_for_collection,
            expected_message="Resolved provider and optional file for add/remove tests",
        )

        async def test_list_collections() -> dict[str, Any]:
            result = await client.collections.list(page=0, page_size=10)
            assert result.data is not None, "data should not be None"
            assert isinstance(result.data, list), "data should be a list"
            return {
                "total_elements": result.total_elements,
                "total_pages": result.total_pages,
                "count": len(result.data) if result.data else 0,
            }

        await runner.run_test(
            name="list_collections",
            test_fn=test_list_collections,
            expected_message="Listed collections",
        )

        async def test_list_collections_pagination() -> dict[str, Any]:
            result = await client.collections.list(page=0, page_size=1)
            assert result.data is not None, "data should not be None"
            return {
                "page_size_requested": 1,
                "items_returned": len(result.data) if result.data else 0,
                "has_more": result.has_next,
            }

        await runner.run_test(
            name="list_collections_pagination",
            test_fn=test_list_collections_pagination,
            expected_message="Pagination works correctly",
        )

        async def test_create_collection() -> dict[str, Any]:
            nonlocal test_collection_id
            result = await client.collections.create(
                name=test_collection_name,
                description="SDK integration test collection",
            )
            test_collection_id = str(result.id.id) if result.id else None
            assert test_collection_id, "Collection ID should be set"
            return {
                "collection_id": test_collection_id,
                "name": result.name,
                "description": result.description,
            }

        await runner.run_test(
            name="create_collection",
            test_fn=test_create_collection,
            expected_message=f"Created collection {test_collection_name}",
        )

        if not test_collection_id:
            runner.skip_test("get_collection", "Create did not return ID")
            runner.skip_test("update_collection", "No collection ID")
            runner.skip_test("list_collection_files", "No collection ID")
            runner.skip_test("add_file_to_collection", "No collection ID")
            runner.skip_test("list_collection_files_after_add", "No collection ID")
            runner.skip_test("remove_file_from_collection", "No collection ID")
            runner.skip_test("list_collection_files_after_remove", "No collection ID")
            runner.skip_test("delete_collection", "No collection ID")
        else:
            cid: str = test_collection_id

            async def test_get_collection() -> dict[str, Any]:
                result = await client.collections.get(cid)
                assert result is not None, "Collection should not be None"
                assert result.id is not None, "Collection ID should not be None"
                return {
                    "id": str(result.id.id) if result.id else None,
                    "name": result.name,
                    "description": result.description,
                }

            await runner.run_test(
                name="get_collection",
                test_fn=test_get_collection,
                expected_message="Retrieved collection by ID",
            )

            async def test_update_collection() -> dict[str, Any]:
                new_name = f"{test_collection_name}-UPDATED"
                result = await client.collections.update(
                    cid,
                    name=new_name,
                    description="Updated description",
                )
                return {
                    "name": result.name,
                    "description": result.description,
                }

            await runner.run_test(
                name="update_collection",
                test_fn=test_update_collection,
                expected_message="Updated collection",
            )

            async def test_list_collection_files() -> dict[str, Any]:
                result = await client.collections.list_files(cid, page=0, page_size=10)
                assert result.data is not None, "data should not be None"
                return {
                    "total_elements": result.total_elements,
                    "count": len(result.data) if result.data else 0,
                }

            await runner.run_test(
                name="list_collection_files",
                test_fn=test_list_collection_files,
                expected_message="Listed files in collection",
            )

            if file_id_for_collection:
                fid_file: str = file_id_for_collection

                async def test_add_file_to_collection() -> dict[str, Any]:
                    await client.collections.add_file(cid, fid_file)
                    return {"file_id": fid_file}

                await runner.run_test(
                    name="add_file_to_collection",
                    test_fn=test_add_file_to_collection,
                    expected_message="Added file to collection",
                )

                async def test_list_collection_files_after_add() -> dict[str, Any]:
                    result = await client.collections.list_files(cid, page=0, page_size=10)
                    assert result.data is not None, "data should not be None"
                    count = len(result.data) if result.data else 0
                    assert count >= 1, "Collection should contain at least one file after add"
                    return {"total_elements": result.total_elements, "count": count}

                await runner.run_test(
                    name="list_collection_files_after_add",
                    test_fn=test_list_collection_files_after_add,
                    expected_message="Collection contains added file",
                )

                async def test_remove_file_from_collection() -> dict[str, Any]:
                    await client.collections.remove_file(cid, fid_file)
                    return {"file_id": fid_file}

                await runner.run_test(
                    name="remove_file_from_collection",
                    test_fn=test_remove_file_from_collection,
                    expected_message="Removed file from collection",
                )

                async def test_list_collection_files_after_remove() -> dict[str, Any]:
                    result = await client.collections.list_files(cid, page=0, page_size=10)
                    assert result.data is not None, "data should not be None"
                    count = len(result.data) if result.data else 0
                    assert count == 0, "Collection should be empty after remove"
                    return {"total_elements": result.total_elements, "count": count}

                await runner.run_test(
                    name="list_collection_files_after_remove",
                    test_fn=test_list_collection_files_after_remove,
                    expected_message="Collection empty after remove",
                )
            else:
                runner.skip_test("add_file_to_collection", "No file available in any provider")
                runner.skip_test("list_collection_files_after_add", "No file available")
                runner.skip_test("remove_file_from_collection", "No file available")
                runner.skip_test("list_collection_files_after_remove", "No file available")

            async def test_delete_collection() -> dict[str, Any]:
                await client.collections.delete(cid)
                return {"deleted_collection_id": cid}

            await runner.run_test(
                name="delete_collection",
                test_fn=test_delete_collection,
                expected_message="Deleted collection",
            )

        async def test_get_collection_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.collections.get("00000000-0000-0000-0000-000000000000")
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_collection_not_found",
            test_fn=test_get_collection_not_found,
            expected_message="NotFoundError raised for non-existent collection",
        )

        async def test_delete_collection_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.collections.delete("00000000-0000-0000-0000-000000000000")
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="delete_collection_not_found",
            test_fn=test_delete_collection_not_found,
            expected_message="NotFoundError raised for delete non-existent collection",
        )

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
