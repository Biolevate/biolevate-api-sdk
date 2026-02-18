"""Provider items resource for managing files and folders within providers."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, BinaryIO

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate_client import AuthenticatedClient
    from biolevate_client.models import (
        DownloadUrlResponse,
        ListItemsResponse,
        ProviderItem,
        UploadUrlResponse,
    )


class ProviderItemsResource:
    """Resource for managing files and folders within storage providers."""

    def __init__(self, client: AuthenticatedClient) -> None:
        """Initialize the provider items resource.

        Args:
            client: The authenticated API client.
        """
        self._client = client

    async def list(
        self,
        provider_id: str,
        path: str = "/",
        query: str | None = None,
        cursor: str | None = None,
        limit: int = 50,
    ) -> ListItemsResponse:
        """List files and folders at a path in a provider.

        Args:
            provider_id: The provider UUID.
            path: The path to list items from.
            query: Optional search filter.
            cursor: Pagination cursor for next page.
            limit: Maximum number of items to return.

        Returns:
            Paginated list of provider items.

        Raises:
            NotFoundError: If the provider or path is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import list_items
        from biolevate_client.types import UNSET

        response = await list_items.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            path=path,
            q=query if query is not None else UNSET,
            cursor=cursor if cursor is not None else UNSET,
            limit=limit,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Provider or path not found: {provider_id}{path}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to list items")

        return response.parsed

    async def get_download_url(
        self,
        provider_id: str,
        path: str,
        name: str,
        expiration_minutes: int = 15,
    ) -> DownloadUrlResponse:
        """Get a presigned download URL for a file.

        Args:
            provider_id: The provider UUID.
            path: The path to the file's parent folder.
            name: The file name.
            expiration_minutes: URL expiration time in minutes.

        Returns:
            Response containing the download URL.

        Raises:
            NotFoundError: If the file is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import get_download_url

        response = await get_download_url.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            path=path,
            name=name,
            expiration_minutes=expiration_minutes,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"File not found: {path}/{name}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to file")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get download URL")

        return response.parsed

    async def create_folder(
        self,
        provider_id: str,
        path: str,
        name: str,
    ) -> ProviderItem:
        """Create a new folder.

        Args:
            provider_id: The provider UUID.
            path: The parent directory path.
            name: The folder name.

        Returns:
            The created folder item.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import upload_file
        from biolevate_client.models import CreateItemRequest, CreateItemRequestType

        request = CreateItemRequest(
            type_=CreateItemRequestType.FOLDER,
            name=name,
            path=path,
        )

        response = await upload_file.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            body=request,
            path=path,
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to create folder")

        return response.parsed

    async def upload(
        self,
        provider_id: str,
        path: str,
        file: BinaryIO,
        file_name: str,
        mime_type: str = "application/octet-stream",
    ) -> ProviderItem:
        """Upload a file directly via multipart form.

        Args:
            provider_id: The provider UUID.
            path: The destination folder path.
            file: The file content as a binary stream.
            file_name: The file name.
            mime_type: The file MIME type.

        Returns:
            The created file item.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import upload_file
        from biolevate_client.models import UploadFileFilesBody
        from biolevate_client.types import File

        file_obj = File(
            payload=file,
            file_name=file_name,
            mime_type=mime_type,
        )
        body = UploadFileFilesBody(file=file_obj)

        response = await upload_file.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            body=body,
            path=path,
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to upload file")

        return response.parsed

    async def get_upload_url(
        self,
        provider_id: str,
        path: str,
        name: str,
        size: int,
        content_type: str = "application/octet-stream",
    ) -> UploadUrlResponse:
        """Get a presigned upload URL for direct upload to storage.

        Args:
            provider_id: The provider UUID.
            path: The destination folder path.
            name: The file name.
            size: The file size in bytes.
            content_type: The file MIME type.

        Returns:
            Response containing the upload URL.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import get_upload_url
        from biolevate_client.models import UploadUrlRequest

        request = UploadUrlRequest(
            path=path,
            file_name=name,
            size=size,
            media_type=content_type,
        )

        response = await get_upload_url.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            body=request,
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to provider")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get upload URL")

        return response.parsed

    async def confirm_upload(
        self,
        provider_id: str,
        path: str,
        name: str,
    ) -> ProviderItem:
        """Confirm a presigned upload has completed.

        Args:
            provider_id: The provider UUID.
            path: The folder path where the file was uploaded.
            name: The uploaded file name.

        Returns:
            The created provider item.

        Raises:
            NotFoundError: If the upload is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import confirm_upload
        from biolevate_client.models import ConfirmUploadRequest

        request = ConfirmUploadRequest(
            path=path,
            file_name=name,
        )

        response = await confirm_upload.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            body=request,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Upload not found: {path}/{name}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to confirm upload")

        return response.parsed

    async def rename(
        self,
        provider_id: str,
        path: str,
        name: str,
        new_name: str,
        is_folder: bool = False,
    ) -> ProviderItem:
        """Rename a file or folder.

        Args:
            provider_id: The provider UUID.
            path: The path to the item's parent folder.
            name: The current item name.
            new_name: The new name for the item.
            is_folder: Whether the item is a folder.

        Returns:
            The renamed provider item.

        Raises:
            NotFoundError: If the item is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import rename_item
        from biolevate_client.models import ItemReference, ItemReferenceType

        item_ref = ItemReference(
            path=path,
            name=name,
            type_=ItemReferenceType.FOLDER if is_folder else ItemReferenceType.FILE,
        )

        response = await rename_item.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            body=item_ref,
            new_name=new_name,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Item not found: {path}/{name}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to rename item")

        return response.parsed

    async def delete(
        self,
        provider_id: str,
        path: str,
        name: str,
        is_folder: bool = False,
    ) -> None:
        """Delete a file or folder.

        Args:
            provider_id: The provider UUID.
            path: The path to the item's parent folder.
            name: The item name.
            is_folder: Whether the item is a folder.

        Raises:
            NotFoundError: If the item is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.provider_items import delete_item
        from biolevate_client.models import ItemReference, ItemReferenceType

        item_ref = ItemReference(
            path=path,
            name=name,
            type_=ItemReferenceType.FOLDER if is_folder else ItemReferenceType.FILE,
        )

        response = await delete_item.asyncio_detailed(
            provider_id=provider_id,
            client=self._client,
            body=item_ref,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"Item not found: {path}/{name}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied")

        if response.status_code not in (HTTPStatus.NO_CONTENT, HTTPStatus.OK):
            raise APIError(response.status_code.value, "Failed to delete item")
