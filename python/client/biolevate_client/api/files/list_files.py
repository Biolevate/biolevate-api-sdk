from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_data_elise_file_info import PageDataEliseFileInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider_id: str,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["providerId"] = provider_id

    params["pageSize"] = page_size

    params["page"] = page

    params["sortProperty"] = sort_property

    params["sortOrder"] = sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/files",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageDataEliseFileInfo | None:
    if response.status_code == 200:
        response_200 = PageDataEliseFileInfo.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PageDataEliseFileInfo.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PageDataEliseFileInfo.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PageDataEliseFileInfo.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PageDataEliseFileInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider_id: str,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> Response[PageDataEliseFileInfo]:
    """List files in a provider

     Returns paginated file infos for a provider

    Args:
        provider_id (str):
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageDataEliseFileInfo]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        page_size=page_size,
        page=page,
        sort_property=sort_property,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    provider_id: str,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> PageDataEliseFileInfo | None:
    """List files in a provider

     Returns paginated file infos for a provider

    Args:
        provider_id (str):
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageDataEliseFileInfo
    """

    return sync_detailed(
        client=client,
        provider_id=provider_id,
        page_size=page_size,
        page=page,
        sort_property=sort_property,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    provider_id: str,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> Response[PageDataEliseFileInfo]:
    """List files in a provider

     Returns paginated file infos for a provider

    Args:
        provider_id (str):
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageDataEliseFileInfo]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        page_size=page_size,
        page=page,
        sort_property=sort_property,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    provider_id: str,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> PageDataEliseFileInfo | None:
    """List files in a provider

     Returns paginated file infos for a provider

    Args:
        provider_id (str):
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageDataEliseFileInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            provider_id=provider_id,
            page_size=page_size,
            page=page,
            sort_property=sort_property,
            sort_order=sort_order,
        )
    ).parsed
