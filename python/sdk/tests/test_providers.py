"""Tests for the providers resource."""

import pytest
import respx
from httpx import Response

from biolevate import (
    AuthenticationError,
    BiolevateClient,
    NotFoundError,
)


@pytest.mark.asyncio
class TestProvidersResource:
    """Tests for ProvidersResource."""

    @respx.mock
    async def test_list_providers_success(
        self,
        client: BiolevateClient,
        base_url: str,
        sample_providers_list_response: dict,
    ) -> None:
        """Test listing providers successfully."""
        route = respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(200, json=sample_providers_list_response)
        )

        result = await client.providers.list()

        assert route.called
        assert result.total_elements == 1
        assert result.has_next is False
        assert isinstance(result.data, list)
        assert len(result.data) == 1  # type: ignore[arg-type]
        assert result.data[0].name == "My S3 Bucket"  # type: ignore[index]

    @respx.mock
    async def test_list_providers_with_pagination(
        self,
        client: BiolevateClient,
        base_url: str,
        sample_providers_list_response: dict,
    ) -> None:
        """Test listing providers with pagination parameters."""
        route = respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(200, json=sample_providers_list_response)
        )

        await client.providers.list(page=1, page_size=10, sort_order="desc")

        assert route.called
        request = route.calls.last.request
        assert "page=1" in str(request.url)
        assert "pageSize=10" in str(request.url)
        assert "sortOrder=desc" in str(request.url)

    @respx.mock
    async def test_list_providers_with_query(
        self,
        client: BiolevateClient,
        base_url: str,
        sample_providers_list_response: dict,
    ) -> None:
        """Test listing providers with search query."""
        route = respx.get(f"{base_url}/api/core/providers").mock(
            return_value=Response(200, json=sample_providers_list_response)
        )

        await client.providers.list(query="s3")

        assert route.called
        request = route.calls.last.request
        assert "q=s3" in str(request.url)

    @respx.mock
    async def test_list_providers_unauthorized(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        """Test listing providers with invalid authentication."""
        respx.get(f"{base_url}/api/core/providers").mock(return_value=Response(401, json={"error": "Unauthorized"}))

        with pytest.raises(AuthenticationError, match="Authentication failed"):
            await client.providers.list()

    @respx.mock
    async def test_get_provider_success(
        self,
        client: BiolevateClient,
        base_url: str,
        sample_provider_response: dict,
    ) -> None:
        """Test getting a provider by ID successfully."""
        provider_id = "550e8400-e29b-41d4-a716-446655440000"
        route = respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(200, json=sample_provider_response)
        )

        result = await client.providers.get(provider_id)

        assert route.called
        assert result.name == "My S3 Bucket"

    @respx.mock
    async def test_get_provider_not_found(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        """Test getting a non-existent provider."""
        provider_id = "non-existent-id"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError, match="not found"):
            await client.providers.get(provider_id)

    @respx.mock
    async def test_get_provider_unauthorized(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        """Test getting a provider with invalid authentication."""
        provider_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(401, json={"error": "Unauthorized"})
        )

        with pytest.raises(AuthenticationError, match="Authentication failed"):
            await client.providers.get(provider_id)

    @respx.mock
    async def test_get_provider_forbidden(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        """Test getting a provider without access."""
        provider_id = "550e8400-e29b-41d4-a716-446655440000"
        respx.get(f"{base_url}/api/core/providers/{provider_id}").mock(
            return_value=Response(403, json={"error": "Forbidden"})
        )

        with pytest.raises(AuthenticationError, match="Access denied"):
            await client.providers.get(provider_id)
