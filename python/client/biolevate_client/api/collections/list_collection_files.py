from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_data_elise_file_info import PageDataEliseFileInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    page: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sortBy"] = sort_by

    params["sortOrder"] = sort_order

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/collections/{id}/files".format(
            id=quote(str(id), safe=""),
        ),
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = UNSET,
) -> Response[PageDataEliseFileInfo]:
    """List files in collection

     Returns a paginated list of files belonging to the collection

    Args:
        id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageDataEliseFileInfo]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = UNSET,
) -> PageDataEliseFileInfo | None:
    """List files in collection

     Returns a paginated list of files belonging to the collection

    Args:
        id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageDataEliseFileInfo
    """

    return sync_detailed(
        id=id,
        client=client,
        page=page,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        q=q,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = UNSET,
) -> Response[PageDataEliseFileInfo]:
    """List files in collection

     Returns a paginated list of files belonging to the collection

    Args:
        id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageDataEliseFileInfo]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_by: str | Unset = UNSET,
    sort_order: str | Unset = "asc",
    q: str | Unset = UNSET,
) -> PageDataEliseFileInfo | None:
    """List files in collection

     Returns a paginated list of files belonging to the collection

    Args:
        id (str):
        page (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_by (str | Unset):
        sort_order (str | Unset):  Default: 'asc'.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageDataEliseFileInfo
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            q=q,
        )
    ).parsed
