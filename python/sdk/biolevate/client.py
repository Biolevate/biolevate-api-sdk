"""High-level Biolevate client wrapper."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.resources.providers import ProvidersResource

if TYPE_CHECKING:
    from biolevate_client import AuthenticatedClient


class BiolevateClient:
    """High-level client for interacting with the Biolevate API.

    This client wraps the generated low-level client and provides
    a more ergonomic interface with additional features like pipelines.

    Example:
        ```python
        async with BiolevateClient(base_url="https://api.biolevate.com", token="...") as client:
            providers = await client.providers.list()
            for provider in providers.data:
                print(provider.name)
        ```
    """

    def __init__(self, base_url: str, token: str) -> None:
        """Initialize the Biolevate client.

        Args:
            base_url: The base URL of the Biolevate API.
            token: The authentication token (JWT).
        """
        self._base_url = base_url
        self._token = token
        self._client: AuthenticatedClient | None = None
        self._providers: ProvidersResource | None = None

    def _get_client(self) -> AuthenticatedClient:
        """Get or create the underlying authenticated client."""
        if self._client is None:
            from biolevate_client import AuthenticatedClient

            self._client = AuthenticatedClient(
                base_url=self._base_url,
                token=self._token,
            )
        return self._client

    @property
    def providers(self) -> ProvidersResource:
        """Access the providers resource for managing storage providers."""
        if self._providers is None:
            self._providers = ProvidersResource(self._get_client())
        return self._providers

    async def __aenter__(self) -> BiolevateClient:
        """Enter async context."""
        return self

    async def __aexit__(self, exc_type: type | None, exc_val: Exception | None, exc_tb: object) -> None:
        """Exit async context."""
        if self._client is not None:
            await self._client.__aexit__(exc_type, exc_val, exc_tb)
