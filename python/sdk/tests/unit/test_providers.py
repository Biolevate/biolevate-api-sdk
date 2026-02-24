"""Unit tests for ProvidersResource."""

import pytest
import respx
from httpx import Response

from biolevate import APIError, AuthenticationError, BiolevateClient, NotFoundError


@pytest.mark.asyncio
class TestProvidersList:
    @respx.mock
    async def test_returns_page_of_providers(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(200, json=provider_page_payload)
        )

        page = await client.providers.list()

        assert page.total_elements == 1
        assert page.has_next is False
        assert len(page.data) == 1
        assert page.data[0].name == "My S3 Bucket"

    @respx.mock
    async def test_empty_page(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        payload = {"data": [], "totalPages": 0, "totalElements": 0, "hasNext": False}
        respx.get(f"{base_url}/api/core/providers").mock(return_value=Response(200, json=payload))

        page = await client.providers.list()

        assert page.total_elements == 0
        assert page.data == []

    @respx.mock
    async def test_sends_pagination_params(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(200, json=provider_page_payload)
        )

        await client.providers.list(page=2, page_size=5, sort_order="desc")

        request = route.calls.last.request
        assert "page=2" in str(request.url)
        assert "pageSize=5" in str(request.url)
        assert "sortOrder=desc" in str(request.url)

    @respx.mock
    async def test_sends_sort_by_param(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(200, json=provider_page_payload)
        )

        await client.providers.list(sort_by="name")

        assert "sortBy=name" in str(route.calls.last.request.url)

    @respx.mock
    async def test_sends_query_param(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(200, json=provider_page_payload)
        )

        await client.providers.list(query="s3")

        assert "q=s3" in str(route.calls.last.request.url)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(401, json={"error": "Unauthorized"})
        )

        with pytest.raises(AuthenticationError, match="Authentication failed"):
            await client.providers.list()

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(403, json={"error": "Forbidden"})
        )

        with pytest.raises(AuthenticationError, match="Access denied"):
            await client.providers.list()

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(500, json={"error": "Internal Server Error"})
        )

        with pytest.raises(APIError) as exc_info:
            await client.providers.list()

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestProvidersGet:
    @respx.mock
    async def test_returns_provider_by_id(
        self,
        client: BiolevateClient,
        base_url: str,
        provider_payload: dict,
    ) -> None:
        provider_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(200, json=provider_payload)
        )

        provider = await client.providers.get(provider_id)

        assert provider.name == "My S3 Bucket"
        assert provider.type == "S3"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        provider_id = "does-not-exist"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError, match="not found"):
            await client.providers.get(provider_id)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        provider_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(401, json={"error": "Unauthorized"})
        )

        with pytest.raises(AuthenticationError, match="Authentication failed"):
            await client.providers.get(provider_id)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        provider_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(403, json={"error": "Forbidden"})
        )

        with pytest.raises(AuthenticationError, match="Access denied"):
            await client.providers.get(provider_id)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        provider_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(500, json={"error": "Internal Server Error"})
        )

        with pytest.raises(APIError) as exc_info:
            await client.providers.get(provider_id)

        assert exc_info.value.status_code == 500
