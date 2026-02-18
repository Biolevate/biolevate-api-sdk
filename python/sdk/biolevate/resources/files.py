"""Files resource for managing indexed files."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate_client import AuthenticatedClient
    from biolevate_client.models import (
        EliseFileInfo,
        EliseOntology,
        PageDataEliseFileInfo,
    )


class FilesResource:
    """Resource for managing indexed files.

    Provides methods to list, create, retrieve, delete, and reindex files.
    """

    def __init__(self, client: AuthenticatedClient) -> None:
        """Initialize the files resource.

        Args:
            client: The authenticated API client.
        """
        self._client = client

    async def list(
        self,
        provider_id: str,
        page: int = 0,
        page_size: int = 20,
        sort_property: str | None = None,
        sort_order: str | None = None,
    ) -> PageDataEliseFileInfo:
        """List indexed files for a provider.

        Args:
            provider_id: The provider UUID.
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_property: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of files.

        Raises:
            NotFoundError: If the provider is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files import list_files
        from biolevate_client.types import UNSET

        response = await list_files.asyncio_detailed(
            client=self._client,
            provider_id=provider_id,
            page=page,
            page_size=page_size,
            sort_property=sort_property if sort_property is not None else UNSET,
            sort_order=sort_order if sort_order is not None else UNSET,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Provider not found: {provider_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to list files")

        return response.parsed

    async def create(
        self,
        provider_id: str,
        path: str,
        name: str,
    ) -> EliseFileInfo:
        """Create an indexed file from a provider item.

        This triggers indexation of the file for use with extraction and QA.

        Args:
            provider_id: The provider UUID.
            path: The path to the file's parent folder.
            name: The file name.

        Returns:
            The created file info.

        Raises:
            NotFoundError: If the provider item is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files import create_file
        from biolevate_client.models import CreateFileRequest

        request = CreateFileRequest(
            provider_id=provider_id,
            path=path,
            name=name,
        )

        response = await create_file.asyncio_detailed(
            client=self._client,
            body=request,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Provider item not found: {path}/{name}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.BAD_REQUEST:
            raise APIError(response.status_code.value, "Invalid request")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to create file")

        return response.parsed

    async def get(self, file_id: str) -> EliseFileInfo:
        """Get a file by ID.

        Args:
            file_id: The file UUID.

        Returns:
            The file info.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files import get_file

        response = await get_file.asyncio_detailed(
            id=file_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"File not found: {file_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to file")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get file")

        return response.parsed

    async def delete(self, file_id: str) -> None:
        """Delete a file.

        Args:
            file_id: The file UUID.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files import delete_file

        response = await delete_file.asyncio_detailed(
            id=file_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"File not found: {file_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to file")

        if response.status_code not in (HTTPStatus.NO_CONTENT, HTTPStatus.OK):
            raise APIError(response.status_code.value, "Failed to delete file")

    async def reindex(self, file_id: str, reparse: bool = False) -> EliseFileInfo:
        """Force reindexation of a file.

        Args:
            file_id: The file UUID.
            reparse: Whether to reparse the file content.

        Returns:
            The updated file info.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files import reindex_file

        response = await reindex_file.asyncio_detailed(
            id=file_id,
            client=self._client,
            reparse=reparse,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"File not found: {file_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to file")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to reindex file")

        return response.parsed

    async def get_ontologies(self, file_id: str) -> "list[EliseOntology]": # type: ignore[valid-type]
        """Get computed ontologies for a file.

        Args:
            file_id: The file UUID.

        Returns:
            List of ontologies computed for the file.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files import get_file_ontologies

        response = await get_file_ontologies.asyncio_detailed(
            id=file_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"File not found: {file_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to file")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get ontologies")

        return response.parsed  # type: ignore[return-value]

    async def recompute_ontologies(self, file_id: str) -> EliseFileInfo:
        """Force recomputation of ontologies and metadata for a file.

        Args:
            file_id: The file UUID.

        Returns:
            The updated file info.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files import recompute_file_ontologies

        response = await recompute_file_ontologies.asyncio_detailed(
            id=file_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"File not found: {file_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to file")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to recompute ontologies")

        return response.parsed
