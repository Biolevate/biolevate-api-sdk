"""Integration tests for FilesResource."""

import pytest

from biolevate import BiolevateClient, NotFoundError

_NON_EXISTENT_ID = "00000000-0000-0000-0000-000000000000"


@pytest.mark.asyncio
class TestFilesList:
    async def test_returns_page_for_provider(
        self,
        live_client: BiolevateClient,
        provider_id: str,
    ) -> None:
        page = await live_client.files.list(provider_id)

        assert page.data is not None
        assert isinstance(page.data, list)

    async def test_pagination_page_size_is_respected(
        self,
        live_client: BiolevateClient,
        provider_id: str,
    ) -> None:
        page = await live_client.files.list(provider_id, page=0, page_size=1)

        assert len(page.data) <= 1


@pytest.mark.asyncio
class TestFilesCreate:
    async def test_created_file_appears_in_list(
        self,
        live_client: BiolevateClient,
        provider_id: str,
        indexed_file_id: str,
    ) -> None:
        page = await live_client.files.list(provider_id, page=0, page_size=100)

        ids = [str(f.id.id) for f in page.data if f.id]
        assert indexed_file_id in ids


@pytest.mark.asyncio
class TestFilesGet:
    async def test_returns_indexed_file(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
    ) -> None:
        file = await live_client.files.get(indexed_file_id)

        assert str(file.id.id) == indexed_file_id
        assert file.name is not None
        assert file.indexed is True

    async def test_raises_not_found_for_missing_id(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.files.get(_NON_EXISTENT_ID)


@pytest.mark.asyncio
class TestFilesGetOntologies:
    async def test_returns_non_empty_ontology_list(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
    ) -> None:
        ontologies = await live_client.files.get_ontologies(indexed_file_id)

        assert isinstance(ontologies, list)

    async def test_raises_not_found_for_missing_id(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.files.get_ontologies(_NON_EXISTENT_ID)


@pytest.mark.asyncio
class TestFilesReindex:
    async def test_triggers_reindex_without_error(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
    ) -> None:
        await live_client.files.reindex(indexed_file_id)

    async def test_raises_not_found_for_missing_id(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.files.reindex(_NON_EXISTENT_ID)


@pytest.mark.asyncio
class TestFilesRecomputeOntologies:
    async def test_triggers_recompute_without_error(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
    ) -> None:
        await live_client.files.recompute_ontologies(indexed_file_id)

    async def test_raises_not_found_for_missing_id(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.files.recompute_ontologies(_NON_EXISTENT_ID)


@pytest.mark.asyncio
class TestFilesDelete:
    async def test_raises_not_found_for_missing_id(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.files.delete(_NON_EXISTENT_ID)
