from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_data_job import PageDataJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["page"] = page

    params["sortProperty"] = sort_property

    params["sortOrder"] = sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/extraction/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PageDataJob | None:
    if response.status_code == 200:
        response_200 = PageDataJob.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PageDataJob.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PageDataJob]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> Response[PageDataJob]:
    """List extraction jobs

     Returns a paginated list of extraction jobs for the current user

    Args:
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageDataJob]
    """

    kwargs = _get_kwargs(
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
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> PageDataJob | None:
    """List extraction jobs

     Returns a paginated list of extraction jobs for the current user

    Args:
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageDataJob
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page=page,
        sort_property=sort_property,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> Response[PageDataJob]:
    """List extraction jobs

     Returns a paginated list of extraction jobs for the current user

    Args:
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageDataJob]
    """

    kwargs = _get_kwargs(
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
    page_size: int,
    page: int,
    sort_property: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
) -> PageDataJob | None:
    """List extraction jobs

     Returns a paginated list of extraction jobs for the current user

    Args:
        page_size (int):
        page (int):
        sort_property (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageDataJob
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page=page,
            sort_property=sort_property,
            sort_order=sort_order,
        )
    ).parsed
