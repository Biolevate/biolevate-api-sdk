"""Provider items resource for managing files/folders within providers."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, BinaryIO

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate.models import ListItemsResponse, ProviderItem
    from biolevate_client import ApiClient
    from biolevate_client.models import DownloadUrlResponse, UploadUrlResponse


class ProviderItemsResource:
    """Resource for managing files and folders within storage providers.

    Provides methods to list, upload, download, rename, and delete items.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the provider items resource.  Paths are relative to the provider root.

        Args:
            client: The API client.
        """
        self._client = client

    async def list(
        self,
        provider_id: str,
        key: str = "/",
    ) -> ListItemsResponse:
        """List items in a provider directory.

        Args:
            provider_id: The provider ID.
            path: Directory path to list (default: root).

        Returns:
            List of items in the directory.

        Raises:
            NotFoundError: If the provider or path is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items_api import ProviderItemsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = ProviderItemsApi(self._client)

        try:
            return await api.list_items(provider_id=provider_id, key=key)
        except NotFoundException as e:
            raise NotFoundError(f"Key not found: {key}") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied to provider") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def upload(
        self,
        provider_id: str,
        key: str,
        file: BinaryIO,
        file_name: str,
        mime_type: str = "application/octet-stream",
    ) -> ProviderItem:
        """Upload a file to a provider.

        Args:
            provider_id: The provider ID.
            key: Destination directory path.
            file: File-like object to upload.
            file_name: Name for the uploaded file.
            mime_type: MIME type of the file.

        Returns:
            The created provider item.

        Raises:
            NotFoundError: If the provider or path is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        import httpx

        from biolevate_client.models import ProviderItem as ProviderItemModel

        config = self._client.configuration
        base_url = config.host.rstrip("/")
        headers = {"Authorization": f"Bearer {config.access_token}"}

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(
                f"{base_url}/api/core/providers/{provider_id}/items",
                params={"key": key},
                files={"file": (file_name, file, mime_type)},
                headers=headers,
            )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Key not found: {key}")

        if response.status_code != HTTPStatus.CREATED:
            raise APIError(response.status_code, f"Failed to upload file: {response.text}")

        result = ProviderItemModel.from_dict(response.json())
        if result is None:
            raise APIError(500, "Failed to parse upload response")
        return result

    async def create_folder(
        self,
        provider_id: str,
        key: str,
    ) -> ProviderItem:
        """Create a folder in a provider.

        Args:
            provider_id: The provider ID.
            key: Directory path.

        Returns:
            The created folder item.

        Raises:
            NotFoundError: If the provider or path is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        import httpx

        from biolevate_client.models import ProviderItem as ProviderItemModel

        config = self._client.configuration
        base_url = config.host.rstrip("/")
        headers = {"Authorization": f"Bearer {config.access_token}"}

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(
                f"{base_url}/api/core/providers/{provider_id}/items",
                json={"key": key},
                headers=headers,
            )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Key not found: {key}")

        if response.status_code not in (HTTPStatus.OK, HTTPStatus.CREATED):
            raise APIError(response.status_code, f"Failed to create folder: {response.text}")

        result = ProviderItemModel.from_dict(response.json())
        if result is None:
            raise APIError(500, "Failed to parse folder response")
        return result

    async def rename(
        self,
        provider_id: str,
        key: str,
        new_name: str,
    ) -> ProviderItem:
        """Rename a file or folder in a provider.

        Args:
            provider_id: The provider ID.
            key: Current item key (path).
            new_name: New item name.

        Returns:
            The renamed item.

        Raises:
            NotFoundError: If the item is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items_api import ProviderItemsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )
        from biolevate_client.models import ItemReference

        api = ProviderItemsApi(self._client)

        try:
            return await api.rename_item(
                provider_id=provider_id,
                new_name=new_name,
                item_reference=ItemReference(
                    key=key,
                ),
            )
        except NotFoundException as e:
            raise NotFoundError(f"Item '{key}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied to provider") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def delete(
        self,
        provider_id: str,
        key: str,
    ) -> None:
        """Delete a file or folder in a provider.

        Args:
            provider_id: The provider ID.
            path: Directory path containing the item.
            name: Item name to delete.
            item_type: Type of item ('FILE' or 'FOLDER').

        Raises:
            NotFoundError: If the item is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items_api import ProviderItemsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )
        from biolevate_client.models import ItemReference

        api = ProviderItemsApi(self._client)

        try:
            await api.delete_item(
                provider_id=provider_id,
                item_reference=ItemReference(
                    key=key,
                ),
            )
        except NotFoundException as e:
            raise NotFoundError(f"Item '{key}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied to provider") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_download_url(
        self,
        provider_id: str,
        key: str,
        expiration_minutes: int | None = None,
    ) -> DownloadUrlResponse:
        """Get a presigned download URL for a file.

        Args:
            provider_id: The provider ID.
            path: Directory path containing the file.
            name: File name.
            expiration_minutes: Optional URL expiration time in minutes.

        Returns:
            Download URL response with the presigned URL.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items_api import ProviderItemsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = ProviderItemsApi(self._client)

        try:
            return await api.get_download_url(
                provider_id=provider_id,
                key=key,
                expiration_minutes=expiration_minutes,
            )
        except NotFoundException as e:
            raise NotFoundError(f"File not found: {key}") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied to provider") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_upload_url(
        self,
        provider_id: str,
        key: str,
        size: int | None = None,
        media_type: str | None = None,
    ) -> UploadUrlResponse:
        """Get a presigned upload URL for direct upload.

        Args:
            provider_id: The provider ID.
            path: Target directory path.
            file_name: Name for the file to upload.
            size: File size in bytes (optional).
            media_type: MIME type of the file (optional).

        Returns:
            Upload URL response with the presigned URL.

        Raises:
            NotFoundError: If the provider or path is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items_api import ProviderItemsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )
        from biolevate_client.models import UploadUrlRequest

        api = ProviderItemsApi(self._client)

        try:
            return await api.get_upload_url(
                provider_id=provider_id,
                upload_url_request=UploadUrlRequest(
                    key=key,
                    size=size,
                    mediaType=media_type,
                ),
            )
        except NotFoundException as e:
            raise NotFoundError(f"Key not found: {key}") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied to provider") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def confirm_upload(
        self,
        provider_id: str,
        key: str,
    ) -> ProviderItem:
        """Confirm that a presigned upload has completed.

        Args:
            provider_id: The provider ID.
            path: Directory path where the file was uploaded.
            file_name: Name of the uploaded file.

        Returns:
            The created provider item.

        Raises:
            NotFoundError: If the uploaded file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items_api import ProviderItemsApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )
        from biolevate_client.models import ConfirmUploadRequest

        api = ProviderItemsApi(self._client)

        try:
            return await api.confirm_upload(
                provider_id=provider_id,
                confirm_upload_request=ConfirmUploadRequest(
                    key=key,
                ),
            )
        except NotFoundException as e:
            raise NotFoundError(f"Uploaded file not found: {key}") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied to provider") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
