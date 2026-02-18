"""Providers resource for managing storage providers."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate_client import AuthenticatedClient
    from biolevate_client.models import FSProviderExternal, PageDataFSProviderExternal


class ProvidersResource:
    """Resource for managing storage providers.

    Provides methods to list and retrieve storage providers.
    """

    def __init__(self, client: AuthenticatedClient) -> None:
        """Initialize the providers resource.

        Args:
            client: The authenticated API client.
        """
        self._client = client

    async def list(
        self,
        page: int = 0,
        page_size: int = 20,
        sort_by: str | None = None,
        sort_order: str = "asc",
        query: str | None = None,
    ) -> PageDataFSProviderExternal:
        """List all storage providers with pagination.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_by: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').
            query: Text search filter.

        Returns:
            Paginated list of providers.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.providers import list_providers
        from biolevate_client.types import UNSET

        response = await list_providers.asyncio_detailed(
            client=self._client,
            page=page,
            page_size=page_size,
            sort_by=sort_by if sort_by is not None else UNSET,
            sort_order=sort_order,
            q=query if query is not None else UNSET,
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to list providers")

        return response.parsed

    async def get(self, provider_id: str) -> FSProviderExternal:
        """Get a storage provider by ID.

        Args:
            provider_id: The unique identifier of the provider.

        Returns:
            The provider details.

        Raises:
            NotFoundError: If the provider is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.providers import get_provider

        response = await get_provider.asyncio_detailed(
            id=provider_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Provider '{provider_id}' not found")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get provider")

        return response.parsed
