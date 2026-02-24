"""Providers resource for managing storage providers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate.models import Provider, ProviderPage
    from biolevate_client import ApiClient


class ProvidersResource:
    """Resource for managing storage providers.

    Provides methods to list and retrieve storage providers.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the providers resource.

        Args:
            client: The API client.
        """
        self._client = client

    async def list(
        self,
        page: int = 0,
        page_size: int = 20,
        sort_by: str | None = None,
        sort_order: str = "asc",
        query: str | None = None,
    ) -> ProviderPage:
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
        from biolevate_client.api.providers_api import ProvidersApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = ProvidersApi(self._client)

        try:
            return await api.list_providers(
                page=page,
                page_size=page_size,
                sort_by=sort_by,
                sort_order=sort_order,
                q=query,
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get(self, provider_id: str) -> Provider:
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
        from biolevate_client.api.providers_api import ProvidersApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = ProvidersApi(self._client)

        try:
            return await api.get_provider(id=provider_id)
        except NotFoundException as e:
            raise NotFoundError(f"Provider '{provider_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied to provider") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
