from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_file_request import CreateFileRequest
from ...models.elise_file_info import EliseFileInfo
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/core/files",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EliseFileInfo | None:
    if response.status_code == 201:
        response_201 = EliseFileInfo.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = EliseFileInfo.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EliseFileInfo.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = EliseFileInfo.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EliseFileInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileRequest,
) -> Response[EliseFileInfo]:
    """Create a file

     Creates an EliseFile from an existing provider item and triggers indexation

    Args:
        body (CreateFileRequest): Request to create EliseFile from provider item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EliseFileInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileRequest,
) -> EliseFileInfo | None:
    """Create a file

     Creates an EliseFile from an existing provider item and triggers indexation

    Args:
        body (CreateFileRequest): Request to create EliseFile from provider item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EliseFileInfo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileRequest,
) -> Response[EliseFileInfo]:
    """Create a file

     Creates an EliseFile from an existing provider item and triggers indexation

    Args:
        body (CreateFileRequest): Request to create EliseFile from provider item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EliseFileInfo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFileRequest,
) -> EliseFileInfo | None:
    """Create a file

     Creates an EliseFile from an existing provider item and triggers indexation

    Args:
        body (CreateFileRequest): Request to create EliseFile from provider item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EliseFileInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
