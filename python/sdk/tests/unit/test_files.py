"""Unit tests for FilesResource."""

import pytest
import respx
from httpx import Response

from biolevate import APIError, AuthenticationError, BiolevateClient, NotFoundError

PROVIDER_ID = "550e8400-e29b-41d4-a716-446655440000"
FILE_ID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"


@pytest.mark.asyncio
class TestFilesList:
    @respx.mock
    async def test_returns_page_of_files(
        self,
        client: BiolevateClient,
        base_url: str,
        file_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/files").mock(return_value=Response(200, json=file_page_payload))

        page = await client.files.list(PROVIDER_ID)

        assert page.total_elements == 1
        assert len(page.data) == 1

    @respx.mock
    async def test_sends_provider_id_param(
        self,
        client: BiolevateClient,
        base_url: str,
        file_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/files").mock(
            return_value=Response(200, json=file_page_payload)
        )

        await client.files.list(PROVIDER_ID)

        assert f"providerId={PROVIDER_ID}" in str(route.calls.last.request.url)

    @respx.mock
    async def test_sends_pagination_params(
        self,
        client: BiolevateClient,
        base_url: str,
        file_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/files").mock(
            return_value=Response(200, json=file_page_payload)
        )

        await client.files.list(PROVIDER_ID, page=1, page_size=5)

        assert "page=1" in str(route.calls.last.request.url)
        assert "pageSize=5" in str(route.calls.last.request.url)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files").mock(return_value=Response(401, json={"error": "Unauthorized"}))

        with pytest.raises(AuthenticationError):
            await client.files.list(PROVIDER_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files").mock(return_value=Response(403, json={"error": "Forbidden"}))

        with pytest.raises(AuthenticationError):
            await client.files.list(PROVIDER_ID)


@pytest.mark.asyncio
class TestFilesCreate:
    @respx.mock
    async def test_creates_indexed_file(
        self,
        client: BiolevateClient,
        base_url: str,
        file_payload: dict,
    ) -> None:
        respx.post(f"{base_url}/api/core/files").mock(return_value=Response(201, json=file_payload))

        file = await client.files.create(PROVIDER_ID, key="documents/report.pdf")

        assert file.name == "report.pdf"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files").mock(return_value=Response(404, json={"error": "Not found"}))

        with pytest.raises(NotFoundError):
            await client.files.create(PROVIDER_ID, key="missing/file.pdf")

    @respx.mock
    async def test_raises_api_error_on_400(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files").mock(
            return_value=Response(400, json={"error": "Bad Request"})
        )

        with pytest.raises(APIError) as exc_info:
            await client.files.create(PROVIDER_ID, key="bad-request.pdf")

        assert exc_info.value.status_code == 400

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files").mock(return_value=Response(401, json={"error": "Unauthorized"}))

        with pytest.raises(AuthenticationError):
            await client.files.create(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.files.create(PROVIDER_ID, key="x.pdf")

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.files.create(PROVIDER_ID, key="x.pdf")

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestFilesGet:
    @respx.mock
    async def test_returns_file_by_id(
        self,
        client: BiolevateClient,
        base_url: str,
        file_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}").mock(return_value=Response(200, json=file_payload))

        file = await client.files.get(FILE_ID)

        assert file.name == "report.pdf"
        assert file.indexed is True

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError, match="not found"):
            await client.files.get(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}").mock(
            return_value=Response(401, json={"error": "Unauthorized"})
        )

        with pytest.raises(AuthenticationError):
            await client.files.get(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.files.get(FILE_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.files.get(FILE_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestFilesDelete:
    @respx.mock
    async def test_deletes_file(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/files/{FILE_ID}").mock(return_value=Response(204))

        await client.files.delete(FILE_ID)

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/files/{FILE_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.files.delete(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/files/{FILE_ID}").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.files.delete(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/files/{FILE_ID}").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.files.delete(FILE_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.delete(f"{base_url}/api/core/files/{FILE_ID}").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.files.delete(FILE_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestFilesReindex:
    @respx.mock
    async def test_triggers_reindex(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/files/{FILE_ID}/reindex").mock(return_value=Response(202))

        await client.files.reindex(FILE_ID)

        assert route.called

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/reindex").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.files.reindex(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/reindex").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.files.reindex(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/reindex").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.files.reindex(FILE_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/reindex").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.files.reindex(FILE_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestFilesGetOntologies:
    @respx.mock
    async def test_returns_list_of_ontologies(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        payload = [
            {
                "conceptId": {"id": "d290f1ee-6c54-4b01-90e6-d701748f0851", "entityType": "CONCEPT_NOTE"},
                "name": "Company",
                "metas": {},
            },
        ]
        respx.get(f"{base_url}/api/core/files/{FILE_ID}/ontologies").mock(
            return_value=Response(200, json=payload)
        )

        result = await client.files.get_ontologies(FILE_ID)

        assert isinstance(result, list)
        assert len(result) == 1

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}/ontologies").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.files.get_ontologies(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}/ontologies").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.files.get_ontologies(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}/ontologies").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.files.get_ontologies(FILE_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/files/{FILE_ID}/ontologies").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.files.get_ontologies(FILE_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestFilesRecomputeOntologies:
    @respx.mock
    async def test_triggers_recompute(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/files/{FILE_ID}/recompute-ontologies").mock(
            return_value=Response(202)
        )

        await client.files.recompute_ontologies(FILE_ID)

        assert route.called

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/recompute-ontologies").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.files.recompute_ontologies(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/recompute-ontologies").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.files.recompute_ontologies(FILE_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/recompute-ontologies").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.files.recompute_ontologies(FILE_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/files/{FILE_ID}/recompute-ontologies").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.files.recompute_ontologies(FILE_ID)

        assert exc_info.value.status_code == 500
