#!/usr/bin/env python3
"""Integration tests for the Providers resource."""

from __future__ import annotations

import asyncio

from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner


async def main() -> None:
    parser = get_base_parser("Test Providers resource")
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="providers", api_url=args.api_url)

    async with client:
        # Test 1: List providers
        async def test_list_providers():
            result = await client.providers.list(page=0, page_size=10)
            assert result.data is not None, "data should not be None"
            assert isinstance(result.data, list), "data should be a list"
            return {
                "total_elements": result.total_elements,
                "total_pages": result.total_pages,
                "count": len(result.data) if result.data else 0,
            }

        await runner.run_test(
            name="list_providers",
            test_fn=test_list_providers,
            expected_message="Successfully listed providers",
        )

        # Test 2: List providers with pagination
        async def test_list_providers_pagination():
            result = await client.providers.list(page=0, page_size=1)
            assert result.data is not None, "data should not be None"
            return {
                "page_size_requested": 1,
                "items_returned": len(result.data) if result.data else 0,
                "has_more": result.has_next,
            }

        await runner.run_test(
            name="list_providers_pagination",
            test_fn=test_list_providers_pagination,
            expected_message="Pagination works correctly",
        )

        # Test 3: Get provider by ID (requires at least one provider)
        first_provider_id: str | None = None

        async def test_get_provider_setup():
            nonlocal first_provider_id
            result = await client.providers.list(page=0, page_size=1)
            if result.data and len(result.data) > 0:
                provider = result.data[0]
                first_provider_id = str(provider.id.id) if provider.id else None
                return {"found_provider_id": first_provider_id}
            raise AssertionError("No providers available for testing get")

        await runner.run_test(
            name="get_provider_setup",
            test_fn=test_get_provider_setup,
            expected_message="Found provider for get test",
        )

        if first_provider_id:

            async def test_get_provider():
                result = await client.providers.get(first_provider_id)  # type: ignore[arg-type]
                assert result is not None, "Provider should not be None"
                assert result.id is not None, "Provider ID should not be None"
                return {
                    "id": result.id.id if result.id else None,
                    "name": result.name,
                    "type": result.type,
                }

            await runner.run_test(
                name="get_provider",
                test_fn=test_get_provider,
                expected_message=f"Successfully retrieved provider {first_provider_id}",
            )

            # Test 4: Get provider - verify fields
            async def test_get_provider_fields():
                result = await client.providers.get(first_provider_id)  # type: ignore[arg-type]
                fields_present = {
                    "id": result.id is not None,
                    "name": result.name is not None,
                    "type": result.type is not None,
                    "config": result.config is not None,
                }
                return {"fields_present": fields_present}

            await runner.run_test(
                name="get_provider_fields",
                test_fn=test_get_provider_fields,
                expected_message="Provider has expected fields",
            )
        else:
            runner.skip_test("get_provider", "No provider available")
            runner.skip_test("get_provider_fields", "No provider available")

        # Test 5: Get non-existent provider (should raise NotFoundError)
        async def test_get_provider_not_found():
            from biolevate import NotFoundError

            try:
                await client.providers.get("00000000-0000-0000-0000-000000000000")
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_provider_not_found",
            test_fn=test_get_provider_not_found,
            expected_message="NotFoundError raised for non-existent provider",
        )

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
