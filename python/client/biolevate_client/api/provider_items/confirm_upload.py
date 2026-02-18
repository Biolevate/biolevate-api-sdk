from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirm_upload_request import ConfirmUploadRequest
from ...models.provider_item import ProviderItem
from ...types import Response


def _get_kwargs(
    provider_id: str,
    *,
    body: ConfirmUploadRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/providers/{provider_id}/items/confirm".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProviderItem | None:
    if response.status_code == 200:
        response_200 = ProviderItem.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ProviderItem.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ProviderItem.from_dict(response.json())

        return response_404

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
    body: ConfirmUploadRequest,
) -> Response[ProviderItem]:
    """Confirm presigned upload

     Confirms that a file was uploaded via presigned URL

    Args:
        provider_id (str):
        body (ConfirmUploadRequest): Confirm presigned upload request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderItem]
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
    body: ConfirmUploadRequest,
) -> ProviderItem | None:
    """Confirm presigned upload

     Confirms that a file was uploaded via presigned URL

    Args:
        provider_id (str):
        body (ConfirmUploadRequest): Confirm presigned upload request

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
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmUploadRequest,
) -> Response[ProviderItem]:
    """Confirm presigned upload

     Confirms that a file was uploaded via presigned URL

    Args:
        provider_id (str):
        body (ConfirmUploadRequest): Confirm presigned upload request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderItem]
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
    body: ConfirmUploadRequest,
) -> ProviderItem | None:
    """Confirm presigned upload

     Confirms that a file was uploaded via presigned URL

    Args:
        provider_id (str):
        body (ConfirmUploadRequest): Confirm presigned upload request

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
        )
    ).parsed
