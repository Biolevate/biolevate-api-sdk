from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_url_request import UploadUrlRequest
from ...models.upload_url_response import UploadUrlResponse
from ...types import Response


def _get_kwargs(
    provider_id: str,
    *,
    body: UploadUrlRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/providers/{provider_id}/items/upload-url".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UploadUrlResponse | None:
    if response.status_code == 200:
        response_200 = UploadUrlResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = UploadUrlResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UploadUrlResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UploadUrlResponse]:
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
    body: UploadUrlRequest,
) -> Response[UploadUrlResponse]:
    """Get presigned upload URL

     Returns a presigned URL for direct upload to storage (for large files)

    Args:
        provider_id (str):
        body (UploadUrlRequest): Request for presigned upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadUrlResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadUrlRequest,
) -> UploadUrlResponse | None:
    """Get presigned upload URL

     Returns a presigned URL for direct upload to storage (for large files)

    Args:
        provider_id (str):
        body (UploadUrlRequest): Request for presigned upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadUrlResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadUrlRequest,
) -> Response[UploadUrlResponse]:
    """Get presigned upload URL

     Returns a presigned URL for direct upload to storage (for large files)

    Args:
        provider_id (str):
        body (UploadUrlRequest): Request for presigned upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadUrlResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadUrlRequest,
) -> UploadUrlResponse | None:
    """Get presigned upload URL

     Returns a presigned URL for direct upload to storage (for large files)

    Args:
        provider_id (str):
        body (UploadUrlRequest): Request for presigned upload URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadUrlResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            body=body,
        )
    ).parsed
