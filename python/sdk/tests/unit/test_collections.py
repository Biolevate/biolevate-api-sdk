"""Unit tests for CollectionsResource."""

import pytest
import respx
from httpx import Response

from biolevate import APIError, AuthenticationError, BiolevateClient, NotFoundError

COLLECTION_ID = "c0ffee00-dead-beef-cafe-123456789abc"
FILE_ID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"


@pytest.mark.asyncio
class TestCollectionsList:
    @respx.mock
    async def test_returns_page_of_collections(
        self,
        client: BiolevateClient,
        base_url: str,
        collection_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections").mock(
            return_value=Response(200, json=collection_page_payload)
        )

        page = await client.collections.list()

        assert page.total_elements == 1
        assert len(page.data) == 1
        assert page.data[0].name == "Quarterly Reports"

    @respx.mock
    async def test_sends_pagination_params(
        self,
        client: BiolevateClient,
        base_url: str,
        collection_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/collections").mock(
            return_value=Response(200, json=collection_page_payload)
        )

        await client.collections.list(page=1, page_size=10, sort_order="desc")

        url = str(route.calls.last.request.url)
        assert "page=1" in url
        assert "pageSize=10" in url
        assert "sortOrder=desc" in url

    @respx.mock
    async def test_sends_query_param(
        self,
        client: BiolevateClient,
        base_url: str,
        collection_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/collections").mock(
            return_value=Response(200, json=collection_page_payload)
        )

        await client.collections.list(query="quarterly")

        assert "q=quarterly" in str(route.calls.last.request.url)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.collections.list()

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.collections.list()


@pytest.mark.asyncio
class TestCollectionsCreate:
    @respx.mock
    async def test_creates_collection(
        self,
        client: BiolevateClient,
        base_url: str,
        collection_payload: dict,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections").mock(
            return_value=Response(201, json=collection_payload)
        )

        collection = await client.collections.create(name="Quarterly Reports", description="All quarterly reports")

        assert collection.name == "Quarterly Reports"

    @respx.mock
    async def test_creates_collection_without_description(
        self,
        client: BiolevateClient,
        base_url: str,
        collection_payload: dict,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections").mock(
            return_value=Response(201, json=collection_payload)
        )

        collection = await client.collections.create(name="Quarterly Reports")

        assert collection.name == "Quarterly Reports"

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.collections.create(name="New")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.collections.create(name="New")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestCollectionsGet:
    @respx.mock
    async def test_returns_collection_by_id(
        self,
        client: BiolevateClient,
        base_url: str,
        collection_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(
            return_value=Response(200, json=collection_payload)
        )

        collection = await client.collections.get(COLLECTION_ID)

        assert collection.name == "Quarterly Reports"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError, match="not found"):
            await client.collections.get(COLLECTION_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.collections.get(COLLECTION_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.collections.get(COLLECTION_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.collections.get(COLLECTION_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestCollectionsUpdate:
    @respx.mock
    async def test_updates_collection(
        self,
        client: BiolevateClient,
        base_url: str,
        collection_payload: dict,
    ) -> None:
        updated = {**collection_payload, "name": "Updated Reports"}
        respx.patch(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(
            return_value=Response(200, json=updated)
        )

        collection = await client.collections.update(COLLECTION_ID, name="Updated Reports")

        assert collection.name == "Updated Reports"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.collections.update(COLLECTION_ID, name="New Name")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.collections.update(COLLECTION_ID, name="New Name")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.collections.update(COLLECTION_ID, name="New Name")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.patch(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.collections.update(COLLECTION_ID, name="New Name")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestCollectionsDelete:
    @respx.mock
    async def test_deletes_collection(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        route = respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(
            return_value=Response(204)
        )

        await client.collections.delete(COLLECTION_ID)

        assert route.called

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.collections.delete(COLLECTION_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.collections.delete(COLLECTION_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.collections.delete(COLLECTION_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.collections.delete(COLLECTION_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestCollectionsListFiles:
    @respx.mock
    async def test_returns_files_in_collection(
        self,
        client: BiolevateClient,
        base_url: str,
        file_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(
            return_value=Response(200, json=file_page_payload)
        )

        page = await client.collections.list_files(COLLECTION_ID)

        assert page.total_elements == 1
        assert len(page.data) == 1

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.collections.list_files(COLLECTION_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.collections.list_files(COLLECTION_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.collections.list_files(COLLECTION_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.collections.list_files(COLLECTION_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestCollectionsAddFile:
    @respx.mock
    async def test_adds_file_to_collection(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(
            return_value=Response(204)
        )

        await client.collections.add_file(COLLECTION_ID, FILE_ID)

        assert route.called

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.collections.add_file(COLLECTION_ID, "ghost-file-id")

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.collections.add_file(COLLECTION_ID, FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.collections.add_file(COLLECTION_ID, FILE_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/collections/{COLLECTION_ID}/files").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.collections.add_file(COLLECTION_ID, FILE_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestCollectionsRemoveFile:
    @respx.mock
    async def test_removes_file_from_collection(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        route = respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}/files/{FILE_ID}").mock(
            return_value=Response(204)
        )

        await client.collections.remove_file(COLLECTION_ID, FILE_ID)

        assert route.called

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}/files/{FILE_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.collections.remove_file(COLLECTION_ID, FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}/files/{FILE_ID}").mock(
            return_value=Response(401)
        )

        with pytest.raises(AuthenticationError):
            await client.collections.remove_file(COLLECTION_ID, FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}/files/{FILE_ID}").mock(
            return_value=Response(403)
        )

        with pytest.raises(AuthenticationError):
            await client.collections.remove_file(COLLECTION_ID, FILE_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/collections/{COLLECTION_ID}/files/{FILE_ID}").mock(
            return_value=Response(500)
        )

        with pytest.raises(APIError) as exc_info:
            await client.collections.remove_file(COLLECTION_ID, FILE_ID)

        assert exc_info.value.status_code == 500
