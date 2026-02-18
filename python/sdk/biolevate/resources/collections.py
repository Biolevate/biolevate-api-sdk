"""Collections resource for managing file collections."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate_client import AuthenticatedClient
    from biolevate_client.models import (
        EliseCollectionInfo,
        EliseFileInfo,
        PageDataEliseCollectionInfo,
        PageDataEliseFileInfo,
    )


class CollectionsResource:
    """Resource for managing file collections.

    Provides methods to create, list, retrieve, update, and delete collections,
    as well as manage files within collections.
    """

    def __init__(self, client: AuthenticatedClient) -> None:
        """Initialize the collections resource.

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
    ) -> PageDataEliseCollectionInfo:
        """List collections accessible to the current user.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_by: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').
            query: Text search filter.

        Returns:
            Paginated list of collections.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import list_collections
        from biolevate_client.types import UNSET

        response = await list_collections.asyncio_detailed(
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
            raise APIError(response.status_code.value, "Failed to list collections")

        return response.parsed

    async def create(
        self,
        name: str,
        description: str | None = None,
    ) -> EliseCollectionInfo:
        """Create a new collection.

        Args:
            name: The collection name.
            description: Optional description.

        Returns:
            The created collection info.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import create_collection
        from biolevate_client.models import CreateCollectionRequest
        from biolevate_client.types import UNSET

        request = CreateCollectionRequest(
            name=name,
            description=description if description is not None else UNSET,
        )

        response = await create_collection.asyncio_detailed(
            client=self._client,
            body=request,
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.BAD_REQUEST:
            raise APIError(response.status_code.value, "Invalid request")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to create collection")

        return response.parsed

    async def get(self, collection_id: str) -> EliseCollectionInfo:
        """Get a collection by ID.

        Args:
            collection_id: The collection UUID.

        Returns:
            The collection info.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import get_collection

        response = await get_collection.asyncio_detailed(
            id=collection_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Collection not found: {collection_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to collection")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get collection")

        return response.parsed

    async def update(
        self,
        collection_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> EliseCollectionInfo:
        """Update a collection.

        Args:
            collection_id: The collection UUID.
            name: New name (optional).
            description: New description (optional).

        Returns:
            The updated collection info.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import update_collection
        from biolevate_client.models import UpdateCollectionRequest
        from biolevate_client.types import UNSET

        request = UpdateCollectionRequest(
            name=name if name is not None else UNSET,
            description=description if description is not None else UNSET,
        )

        response = await update_collection.asyncio_detailed(
            id=collection_id,
            client=self._client,
            body=request,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Collection not found: {collection_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to collection")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to update collection")

        return response.parsed

    async def delete(self, collection_id: str) -> None:
        """Delete a collection.

        Args:
            collection_id: The collection UUID.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import delete_collection

        response = await delete_collection.asyncio_detailed(
            id=collection_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Collection not found: {collection_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to collection")

        if response.status_code not in (HTTPStatus.NO_CONTENT, HTTPStatus.OK):
            raise APIError(response.status_code.value, "Failed to delete collection")

    async def list_files(
        self,
        collection_id: str,
        page: int = 0,
        page_size: int = 20,
    ) -> PageDataEliseFileInfo:
        """List files in a collection.

        Args:
            collection_id: The collection UUID.
            page: Page number (0-based).
            page_size: Number of items per page.

        Returns:
            Paginated list of files.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import list_collection_files

        response = await list_collection_files.asyncio_detailed(
            id=collection_id,
            client=self._client,
            page=page,
            page_size=page_size,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Collection not found: {collection_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to collection")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to list collection files")

        return response.parsed

    async def add_file(self, collection_id: str, file_id: str) -> EliseFileInfo:
        """Add a file to a collection.

        Args:
            collection_id: The collection UUID.
            file_id: The file UUID to add.

        Returns:
            The added file info.

        Raises:
            NotFoundError: If the collection or file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import add_file_to_collection
        from biolevate_client.models import AddFileToCollectionRequest

        request = AddFileToCollectionRequest(file_id=file_id)

        response = await add_file_to_collection.asyncio_detailed(
            id=collection_id,
            client=self._client,
            body=request,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Collection or file not found")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to add file to collection")

        return response.parsed

    async def remove_file(self, collection_id: str, file_id: str) -> None:
        """Remove a file from a collection.

        Args:
            collection_id: The collection UUID.
            file_id: The file UUID to remove.

        Raises:
            NotFoundError: If the collection or file association is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections import remove_file_from_collection

        response = await remove_file_from_collection.asyncio_detailed(
            id=collection_id,
            file_id=file_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Collection or file association not found")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied")

        if response.status_code not in (HTTPStatus.NO_CONTENT, HTTPStatus.OK):
            raise APIError(response.status_code.value, "Failed to remove file from collection")
