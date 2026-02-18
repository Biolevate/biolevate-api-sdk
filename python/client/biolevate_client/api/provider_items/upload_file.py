from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_item_request import CreateItemRequest
from ...models.provider_item import ProviderItem
from ...models.upload_file_files_body import UploadFileFilesBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider_id: str,
    *,
    body: UploadFileFilesBody | CreateItemRequest | Unset = UNSET,
    path: str | Unset = "/",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/providers/{provider_id}/items".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, UploadFileFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"
    if isinstance(body, CreateItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProviderItem | None:
    if response.status_code == 201:
        response_201 = ProviderItem.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ProviderItem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProviderItem.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProviderItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileFilesBody | CreateItemRequest | Unset = UNSET,
    path: str | Unset = "/",
) -> Response[ProviderItem]:
    """Create folder

     Creates a new folder in the provider

    Args:
        provider_id (str):
        path (str | Unset):  Default: '/'.
        body (UploadFileFilesBody):
        body (CreateItemRequest): Create folder request (for JSON body). For file upload, use
            multipart form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderItem]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileFilesBody | CreateItemRequest | Unset = UNSET,
    path: str | Unset = "/",
) -> ProviderItem | None:
    """Create folder

     Creates a new folder in the provider

    Args:
        provider_id (str):
        path (str | Unset):  Default: '/'.
        body (UploadFileFilesBody):
        body (CreateItemRequest): Create folder request (for JSON body). For file upload, use
            multipart form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderItem
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        body=body,
        path=path,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileFilesBody | CreateItemRequest | Unset = UNSET,
    path: str | Unset = "/",
) -> Response[ProviderItem]:
    """Create folder

     Creates a new folder in the provider

    Args:
        provider_id (str):
        path (str | Unset):  Default: '/'.
        body (UploadFileFilesBody):
        body (CreateItemRequest): Create folder request (for JSON body). For file upload, use
            multipart form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderItem]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileFilesBody | CreateItemRequest | Unset = UNSET,
    path: str | Unset = "/",
) -> ProviderItem | None:
    """Create folder

     Creates a new folder in the provider

    Args:
        provider_id (str):
        path (str | Unset):  Default: '/'.
        body (UploadFileFilesBody):
        body (CreateItemRequest): Create folder request (for JSON body). For file upload, use
            multipart form.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderItem
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            body=body,
            path=path,
        )
    ).parsed
