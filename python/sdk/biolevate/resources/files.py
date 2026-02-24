"""Files resource for managing indexed files."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate.models import File, FilePage, Ontology
    from biolevate_client import ApiClient


class FilesResource:
    """Resource for managing indexed files (EliseFiles).

    Provides methods to list, create, retrieve, and delete files,
    as well as manage indexation and ontologies.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the files resource.

        Args:
            client: The API client.
        """
        self._client = client

    async def list(
        self,
        provider_id: str,
        page: int = 0,
        page_size: int = 20,
        sort_property: str | None = None,
        sort_order: str | None = None,
    ) -> FilePage:
        """List indexed files with pagination.

        Args:
            provider_id: The provider ID to list files for.
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_property: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of files.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files_api import FilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = FilesApi(self._client)

        try:
            return await api.list_files(
                provider_id=provider_id,
                page=page,
                page_size=page_size,
                sort_property=sort_property,
                sort_order=sort_order,
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def create(
        self,
        provider_id: str,
        key: str,
    ) -> File:
        """Create an indexed file from an existing provider item.

        This triggers indexation of the file for search and analysis.

        Args:
            provider_id: The provider ID where the file exists.
            path: The directory path containing the file.
            name: The file name.

        Returns:
            The created file info.

        Raises:
            NotFoundError: If the provider item is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files_api import FilesApi
        from biolevate_client.exceptions import (
            ApiException,
            BadRequestException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )
        from biolevate_client.models import CreateFileRequest

        api = FilesApi(self._client)

        try:
            return await api.create_file(
                create_file_request=CreateFileRequest(
                    providerId=provider_id,
                    key=key,
                )
            )
        except NotFoundException as e:
            raise NotFoundError(f"Provider item not found: {key}") from e
        except BadRequestException as e:
            raise APIError(400, str(e.body or e.reason)) from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get(self, file_id: str) -> File:
        """Get an indexed file by ID.

        Args:
            file_id: The unique identifier of the file.

        Returns:
            The file info.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files_api import FilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = FilesApi(self._client)

        try:
            return await api.get_file(id=file_id)
        except NotFoundException as e:
            raise NotFoundError(f"File '{file_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def delete(self, file_id: str) -> None:
        """Delete an indexed file.

        Args:
            file_id: The unique identifier of the file.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files_api import FilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = FilesApi(self._client)

        try:
            await api.delete_file(id=file_id)
        except NotFoundException as e:
            raise NotFoundError(f"File '{file_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def reindex(self, file_id: str) -> None:
        """Trigger re-indexation of a file.

        Re-indexation runs asynchronously on the server. This method returns
        when the request is accepted; it does not wait for indexation to finish.

        Args:
            file_id: The unique identifier of the file.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files_api import FilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = FilesApi(self._client)

        try:
            await api.reindex_file(id=file_id)
        except NotFoundException as e:
            raise NotFoundError(f"File '{file_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_ontologies(self, file_id: str) -> list[Ontology]:  # type: ignore[valid-type]
        """Get computed ontologies for a file.

        Args:
            file_id: The unique identifier of the file.

        Returns:
            List of computed ontologies.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files_api import FilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = FilesApi(self._client)

        try:
            return await api.get_file_ontologies(id=file_id)
        except NotFoundException as e:
            raise NotFoundError(f"File '{file_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def recompute_ontologies(self, file_id: str) -> None:
        """Trigger re-computation of ontologies for a file.

        Ontology computation runs asynchronously on the server. This method
        returns when the request is accepted; it does not wait for completion.

        Args:
            file_id: The unique identifier of the file.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.files_api import FilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = FilesApi(self._client)

        try:
            await api.recompute_file_ontologies(id=file_id)
        except NotFoundException as e:
            raise NotFoundError(f"File '{file_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
