"""Integration tests for CollectionsResource."""

import contextlib

import pytest

from biolevate import BiolevateClient, NotFoundError

_NON_EXISTENT_ID = "00000000-0000-0000-0000-000000000000"


@pytest.mark.asyncio
class TestCollectionsList:
    async def test_returns_page_of_collections(self, live_client: BiolevateClient) -> None:
        page = await live_client.collections.list()

        assert page.data is not None
        assert isinstance(page.data, list)

    async def test_pagination_page_size_is_respected(self, live_client: BiolevateClient) -> None:
        page = await live_client.collections.list(page=0, page_size=1)

        assert len(page.data) <= 1


@pytest.mark.asyncio
class TestCollectionsGet:
    async def test_returns_collection_by_id(
        self,
        live_client: BiolevateClient,
        collection_id: str,
    ) -> None:
        collection = await live_client.collections.get(collection_id)

        assert str(collection.id.id) == collection_id
        assert collection.name is not None

    async def test_raises_not_found_for_missing_id(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.collections.get(_NON_EXISTENT_ID)


@pytest.mark.asyncio
class TestCollectionsUpdate:
    async def test_updates_name(
        self,
        live_client: BiolevateClient,
        collection_id: str,
    ) -> None:
        collection = await live_client.collections.update(collection_id, name="Updated by Integration Test")

        assert collection.name == "Updated by Integration Test"

    async def test_updates_description(
        self,
        live_client: BiolevateClient,
        collection_id: str,
    ) -> None:
        collection = await live_client.collections.update(
            collection_id, description="Updated description from integration test"
        )

        assert collection.description == "Updated description from integration test"

    async def test_raises_not_found_for_missing_id(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.collections.update(_NON_EXISTENT_ID, name="Ghost")


@pytest.mark.asyncio
class TestCollectionsFiles:
    async def test_add_file_and_list(
        self,
        live_client: BiolevateClient,
        collection_id: str,
        indexed_file_id: str,
    ) -> None:
        await live_client.collections.add_file(collection_id, indexed_file_id)

        page = await live_client.collections.list_files(collection_id)

        ids = [str(f.id.id) for f in page.data if f.id]
        assert indexed_file_id in ids

    async def test_remove_file(
        self,
        live_client: BiolevateClient,
        collection_id: str,
        indexed_file_id: str,
    ) -> None:
        # Ensure the file is in the collection before removing it.
        with contextlib.suppress(Exception):
            await live_client.collections.add_file(collection_id, indexed_file_id)

        await live_client.collections.remove_file(collection_id, indexed_file_id)

        page = await live_client.collections.list_files(collection_id)
        ids = [str(f.id.id) for f in page.data if f.id]
        assert indexed_file_id not in ids

    async def test_list_files_raises_not_found_for_missing_collection(
        self,
        live_client: BiolevateClient,
    ) -> None:
        with pytest.raises(NotFoundError):
            await live_client.collections.list_files(_NON_EXISTENT_ID)
