from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.item_reference import ItemReference
from ...models.provider_item import ProviderItem
from ...types import UNSET, Response


def _get_kwargs(
    provider_id: str,
    *,
    body: ItemReference,
    new_name: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["newName"] = new_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/core/providers/{provider_id}/items".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProviderItem | None:
    if response.status_code == 200:
        response_200 = ProviderItem.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProviderItem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProviderItem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProviderItem.from_dict(response.json())

        return response_403

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
    body: ItemReference,
    new_name: str,
) -> Response[ProviderItem]:
    """Rename item

     Renames a file or folder

    Args:
        provider_id (str):
        new_name (str):
        body (ItemReference): Reference to an item for delete operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderItem]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        new_name=new_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ItemReference,
    new_name: str,
) -> ProviderItem | None:
    """Rename item

     Renames a file or folder

    Args:
        provider_id (str):
        new_name (str):
        body (ItemReference): Reference to an item for delete operations

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
        new_name=new_name,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ItemReference,
    new_name: str,
) -> Response[ProviderItem]:
    """Rename item

     Renames a file or folder

    Args:
        provider_id (str):
        new_name (str):
        body (ItemReference): Reference to an item for delete operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderItem]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        new_name=new_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ItemReference,
    new_name: str,
) -> ProviderItem | None:
    """Rename item

     Renames a file or folder

    Args:
        provider_id (str):
        new_name (str):
        body (ItemReference): Reference to an item for delete operations

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
            new_name=new_name,
        )
    ).parsed
