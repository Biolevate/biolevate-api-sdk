"""Collections resource for managing file collections."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate_client import ApiClient
    from biolevate.models import Collection, CollectionPage, FilePage


class CollectionsResource:
    """Resource for managing file collections.

    Collections are groups of indexed files that can be used together
    for extraction or question answering jobs.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the collections resource.

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
    ) -> CollectionPage:
        """List collections with pagination.

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
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = CollectionsApi(self._client)

        try:
            return await api.list_collections(
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

    async def create(
        self,
        name: str,
        description: str | None = None,
    ) -> Collection:
        """Create a new collection.

        Args:
            name: Collection name.
            description: Optional description.

        Returns:
            The created collection.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )
        from biolevate_client.models import CreateCollectionRequest

        api = CollectionsApi(self._client)

        try:
            return await api.create_collection(
                create_collection_request=CreateCollectionRequest(
                    name=name,
                    description=description,
                )
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get(self, collection_id: str) -> Collection:
        """Get a collection by ID.

        Args:
            collection_id: The unique identifier of the collection.

        Returns:
            The collection details.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = CollectionsApi(self._client)

        try:
            return await api.get_collection(id=collection_id)
        except NotFoundException as e:
            raise NotFoundError(f"Collection '{collection_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def update(
        self,
        collection_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> Collection:
        """Update a collection.

        Args:
            collection_id: The unique identifier of the collection.
            name: New name (optional).
            description: New description (optional).

        Returns:
            The updated collection.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )
        from biolevate_client.models import UpdateCollectionRequest

        api = CollectionsApi(self._client)

        try:
            return await api.update_collection(
                id=collection_id,
                update_collection_request=UpdateCollectionRequest(
                    name=name,
                    description=description,
                ),
            )
        except NotFoundException as e:
            raise NotFoundError(f"Collection '{collection_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def delete(self, collection_id: str) -> None:
        """Delete a collection.

        Args:
            collection_id: The unique identifier of the collection.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = CollectionsApi(self._client)

        try:
            await api.delete_collection(id=collection_id)
        except NotFoundException as e:
            raise NotFoundError(f"Collection '{collection_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def list_files(
        self,
        collection_id: str,
        page: int = 0,
        page_size: int = 20,
        sort_by: str | None = None,
        sort_order: str = "asc",
    ) -> FilePage:
        """List files in a collection.

        Args:
            collection_id: The unique identifier of the collection.
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_by: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of files in the collection.

        Raises:
            NotFoundError: If the collection is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = CollectionsApi(self._client)

        try:
            return await api.list_collection_files(
                id=collection_id,
                page=page,
                page_size=page_size,
                sort_by=sort_by,
                sort_order=sort_order,
            )
        except NotFoundException as e:
            raise NotFoundError(f"Collection '{collection_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def add_file(
        self,
        collection_id: str,
        file_id: str,
    ) -> None:
        """Add a file to a collection.

        Args:
            collection_id: The unique identifier of the collection.
            file_id: The unique identifier of the file to add.

        Raises:
            NotFoundError: If the collection or file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )
        from biolevate_client.models import AddFileToCollectionRequest

        api = CollectionsApi(self._client)

        try:
            await api.add_file_to_collection(
                id=collection_id,
                add_file_to_collection_request=AddFileToCollectionRequest(
                    fileId=file_id,
                ),
            )
        except NotFoundException as e:
            raise NotFoundError(f"Collection or file not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def remove_file(
        self,
        collection_id: str,
        file_id: str,
    ) -> None:
        """Remove a file from a collection.

        Args:
            collection_id: The unique identifier of the collection.
            file_id: The unique identifier of the file to remove.

        Raises:
            NotFoundError: If the collection or file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.collections_api import CollectionsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = CollectionsApi(self._client)

        try:
            await api.remove_file_from_collection(
                id=collection_id,
                file_id=file_id,
            )
        except NotFoundException as e:
            raise NotFoundError(f"Collection or file not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
