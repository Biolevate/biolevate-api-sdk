from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_url_response import DownloadUrlResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider_id: str,
    *,
    path: str,
    name: str,
    expiration_minutes: int | Unset = 15,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params["name"] = name

    params["expirationMinutes"] = expiration_minutes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/providers/{provider_id}/items/download-url".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DownloadUrlResponse | None:
    if response.status_code == 200:
        response_200 = DownloadUrlResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DownloadUrlResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DownloadUrlResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DownloadUrlResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DownloadUrlResponse]:
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
    path: str,
    name: str,
    expiration_minutes: int | Unset = 15,
) -> Response[DownloadUrlResponse]:
    """Get download URL

     Returns a URL to download the file

    Args:
        provider_id (str):
        path (str):
        name (str):
        expiration_minutes (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadUrlResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        path=path,
        name=name,
        expiration_minutes=expiration_minutes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    name: str,
    expiration_minutes: int | Unset = 15,
) -> DownloadUrlResponse | None:
    """Get download URL

     Returns a URL to download the file

    Args:
        provider_id (str):
        path (str):
        name (str):
        expiration_minutes (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadUrlResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        path=path,
        name=name,
        expiration_minutes=expiration_minutes,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    name: str,
    expiration_minutes: int | Unset = 15,
) -> Response[DownloadUrlResponse]:
    """Get download URL

     Returns a URL to download the file

    Args:
        provider_id (str):
        path (str):
        name (str):
        expiration_minutes (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadUrlResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        path=path,
        name=name,
        expiration_minutes=expiration_minutes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str,
    name: str,
    expiration_minutes: int | Unset = 15,
) -> DownloadUrlResponse | None:
    """Get download URL

     Returns a URL to download the file

    Args:
        provider_id (str):
        path (str):
        name (str):
        expiration_minutes (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadUrlResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            path=path,
            name=name,
            expiration_minutes=expiration_minutes,
        )
    ).parsed
