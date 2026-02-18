"""Biolevate CLI - Command line interface for the Biolevate API."""

from __future__ import annotations

import asyncio
import json
import sys
from typing import Any

import click

from biolevate import BiolevateClient, BiolevateError, NotFoundError


def run_async(coro: Any) -> Any:
    """Run an async coroutine synchronously."""
    return asyncio.run(coro)


@click.group()
@click.option(
    "--api-url",
    envvar="BIOLEVATE_API_URL",
    help="Biolevate API URL",
)
@click.option(
    "--token",
    envvar="BIOLEVATE_TOKEN",
    help="Authentication token",
)
@click.option(
    "--json",
    "output_json",
    is_flag=True,
    help="Output as JSON",
)
@click.pass_context
def cli(ctx: click.Context, api_url: str | None, token: str | None, output_json: bool) -> None:
    """Biolevate CLI - Interact with the Biolevate API."""
    ctx.ensure_object(dict)
    ctx.obj["api_url"] = api_url
    ctx.obj["token"] = token
    ctx.obj["json"] = output_json


def get_client(ctx: click.Context) -> BiolevateClient:
    """Get or create the BiolevateClient, validating credentials."""
    api_url = ctx.obj.get("api_url")
    token = ctx.obj.get("token")

    if not api_url:
        click.echo("Error: --api-url is required (or set BIOLEVATE_API_URL)", err=True)
        sys.exit(1)

    if not token:
        click.echo("Error: --token is required (or set BIOLEVATE_TOKEN)", err=True)
        sys.exit(1)

    return BiolevateClient(base_url=api_url, token=token)


@cli.group()
def providers() -> None:
    """Manage storage providers."""


@providers.command("list")
@click.option("--query", "-q", help="Search filter")
@click.option("--page", default=0, type=int, help="Page number (0-based)")
@click.option("--page-size", default=20, type=int, help="Items per page")
@click.pass_context
def providers_list(ctx: click.Context, query: str | None, page: int, page_size: int) -> None:
    """List all providers."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.providers.list(
                    page=page,
                    page_size=page_size,
                    query=query,
                )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    if isinstance(result.data, list):
                        for provider in result.data:
                            provider_id = provider.id.id if provider.id else "N/A"  # type: ignore[union-attr]
                            name = provider.name or "N/A"
                            type_ = provider.type_.value if provider.type_ else "N/A"  # type: ignore[union-attr]
                            click.echo(f"{provider_id}  {name}  ({type_})")
                    click.echo(f"\nPage {page + 1}/{result.total_pages or 1} | Total: {result.total_elements or 0}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@providers.command("get")
@click.argument("provider_id")
@click.pass_context
def providers_get(ctx: click.Context, provider_id: str) -> None:
    """Get a provider by ID."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                provider = await client.providers.get(provider_id)

                if output_json:
                    click.echo(json.dumps(provider.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"ID:      {provider.id.id if provider.id else 'N/A'}")  # type: ignore[union-attr]
                    click.echo(f"Name:    {provider.name or 'N/A'}")
                    click.echo(f"Type:    {provider.type_.value if provider.type_ else 'N/A'}")  # type: ignore[union-attr]
                    click.echo(f"Icon:    {provider.icon or 'N/A'}")
                    click.echo(f"System:  {provider.system}")
        except NotFoundError:
            click.echo(f"Provider '{provider_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@cli.group()
def items() -> None:
    """Manage files and folders within providers."""


@items.command("list")
@click.argument("provider_id")
@click.option("--path", "-p", default="/", help="Path to list")
@click.option("--query", "-q", help="Search filter")
@click.option("--limit", default=50, type=int, help="Max items to return")
@click.pass_context
def items_list(ctx: click.Context, provider_id: str, path: str, query: str | None, limit: int) -> None:
    """List files and folders at a path."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.items.list(
                    provider_id=provider_id,
                    path=path,
                    query=query,
                    limit=limit,
                )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    if isinstance(result.items, list):
                        for item in result.items:
                            type_icon = "📁" if item.type_ and item.type_.value == "FOLDER" else "📄"
                            click.echo(f"{type_icon} {item.name}")
                    click.echo(f"\nPath: {path}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@items.command("download-url")
@click.argument("provider_id")
@click.option("--path", "-p", required=True, help="Parent folder path")
@click.option("--name", "-n", required=True, help="File name")
@click.pass_context
def items_download_url(ctx: click.Context, provider_id: str, path: str, name: str) -> None:
    """Get a download URL for a file."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                result = await client.items.get_download_url(
                    provider_id=provider_id,
                    path=path,
                    name=name,
                )
                click.echo(result.url)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@items.command("delete")
@click.argument("provider_id")
@click.option("--path", "-p", required=True, help="Parent folder path")
@click.option("--name", "-n", required=True, help="Item name")
@click.option("--folder", is_flag=True, help="Item is a folder")
@click.pass_context
def items_delete(ctx: click.Context, provider_id: str, path: str, name: str, folder: bool) -> None:
    """Delete a file or folder."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                await client.items.delete(
                    provider_id=provider_id,
                    path=path,
                    name=name,
                    is_folder=folder,
                )
                click.echo(f"Deleted: {path}/{name}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@items.command("create-folder")
@click.argument("provider_id")
@click.option("--path", "-p", default="/", help="Parent folder path")
@click.option("--name", "-n", required=True, help="Folder name")
@click.pass_context
def items_create_folder(ctx: click.Context, provider_id: str, path: str, name: str) -> None:
    """Create a new folder."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.items.create_folder(
                    provider_id=provider_id,
                    path=path,
                    name=name,
                )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"Created folder: {path}{name}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@items.command("upload")
@click.argument("provider_id")
@click.argument("file_path", type=click.Path(exists=True))
@click.option("--path", "-p", default="/", help="Destination folder path")
@click.option("--name", "-n", help="File name (defaults to local file name)")
@click.pass_context
def items_upload(ctx: click.Context, provider_id: str, file_path: str, path: str, name: str | None) -> None:
    """Upload a file to a provider."""
    import os

    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    file_name = name or os.path.basename(file_path)

    async def _run() -> None:
        try:
            async with client:
                with open(file_path, "rb") as f:
                    result = await client.items.upload(
                        provider_id=provider_id,
                        path=path,
                        file=f,
                        file_name=file_name,
                    )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"Uploaded: {path}{file_name}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@items.command("rename")
@click.argument("provider_id")
@click.option("--path", "-p", required=True, help="Parent folder path")
@click.option("--name", "-n", required=True, help="Current item name")
@click.option("--new-name", required=True, help="New item name")
@click.option("--folder", is_flag=True, help="Item is a folder")
@click.pass_context
def items_rename(ctx: click.Context, provider_id: str, path: str, name: str, new_name: str, folder: bool) -> None:
    """Rename a file or folder."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.items.rename(
                    provider_id=provider_id,
                    path=path,
                    name=name,
                    new_name=new_name,
                    is_folder=folder,
                )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"Renamed: {name} -> {new_name}")
        except NotFoundError:
            click.echo(f"Item '{path}/{name}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@cli.group()
def files() -> None:
    """Manage indexed files."""


@files.command("list")
@click.argument("provider_id")
@click.option("--page", default=0, type=int, help="Page number (0-based)")
@click.option("--page-size", default=20, type=int, help="Items per page")
@click.pass_context
def files_list(ctx: click.Context, provider_id: str, page: int, page_size: int) -> None:
    """List indexed files for a provider."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.files.list(
                    provider_id=provider_id,
                    page=page,
                    page_size=page_size,
                )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    if isinstance(result.data, list):
                        for f in result.data:
                            file_id = f.id.id if f.id else "N/A"  # type: ignore[union-attr]
                            click.echo(f"{file_id}  {f.name or 'N/A'}")
                    click.echo(f"\nPage {page + 1}/{result.total_pages or 1} | Total: {result.total_elements or 0}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@files.command("get")
@click.argument("file_id")
@click.pass_context
def files_get(ctx: click.Context, file_id: str) -> None:
    """Get a file by ID."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                f = await client.files.get(file_id)

                if output_json:
                    click.echo(json.dumps(f.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"ID:       {f.id.id if f.id else 'N/A'}")  # type: ignore[union-attr]
                    click.echo(f"Name:     {f.name or 'N/A'}")
                    click.echo(f"Path:     {f.path or 'N/A'}")
                    click.echo(f"Size:     {f.size or 'N/A'}")
        except NotFoundError:
            click.echo(f"File '{file_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@files.command("create")
@click.argument("provider_id")
@click.option("--path", "-p", required=True, help="Parent folder path")
@click.option("--name", "-n", required=True, help="File name")
@click.pass_context
def files_create(ctx: click.Context, provider_id: str, path: str, name: str) -> None:
    """Create/index a file from a provider item."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                f = await client.files.create(
                    provider_id=provider_id,
                    path=path,
                    name=name,
                )

                if output_json:
                    click.echo(json.dumps(f.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"Created file: {f.id.id if f.id else 'N/A'}")  # type: ignore[union-attr]
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@files.command("delete")
@click.argument("file_id")
@click.pass_context
def files_delete(ctx: click.Context, file_id: str) -> None:
    """Delete a file."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                await client.files.delete(file_id)
                click.echo(f"Deleted file: {file_id}")
        except NotFoundError:
            click.echo(f"File '{file_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@files.command("reindex")
@click.argument("file_id")
@click.option("--reparse", is_flag=True, help="Reparse file content")
@click.pass_context
def files_reindex(ctx: click.Context, file_id: str, reparse: bool) -> None:
    """Force reindexation of a file."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                await client.files.reindex(file_id, reparse=reparse)
                click.echo(f"Reindexing file: {file_id}")
        except NotFoundError:
            click.echo(f"File '{file_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@cli.group()
def collections() -> None:
    """Manage file collections."""


@collections.command("list")
@click.option("--query", "-q", help="Search filter")
@click.option("--page", default=0, type=int, help="Page number (0-based)")
@click.option("--page-size", default=20, type=int, help="Items per page")
@click.pass_context
def collections_list(ctx: click.Context, query: str | None, page: int, page_size: int) -> None:
    """List collections."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.collections.list(
                    page=page,
                    page_size=page_size,
                    query=query,
                )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    if isinstance(result.data, list):
                        for c in result.data:
                            coll_id = c.id.id if c.id else "N/A"  # type: ignore[union-attr]
                            click.echo(f"{coll_id}  {c.name or 'N/A'}")
                    click.echo(f"\nPage {page + 1}/{result.total_pages or 1} | Total: {result.total_elements or 0}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@collections.command("get")
@click.argument("collection_id")
@click.pass_context
def collections_get(ctx: click.Context, collection_id: str) -> None:
    """Get a collection by ID."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                c = await client.collections.get(collection_id)

                if output_json:
                    click.echo(json.dumps(c.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"ID:          {c.id.id if c.id else 'N/A'}")  # type: ignore[union-attr]
                    click.echo(f"Name:        {c.name or 'N/A'}")
                    click.echo(f"Description: {c.description or 'N/A'}")
        except NotFoundError:
            click.echo(f"Collection '{collection_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@collections.command("create")
@click.option("--name", "-n", required=True, help="Collection name")
@click.option("--description", "-d", help="Collection description")
@click.pass_context
def collections_create(ctx: click.Context, name: str, description: str | None) -> None:
    """Create a new collection."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                c = await client.collections.create(name=name, description=description)

                if output_json:
                    click.echo(json.dumps(c.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"Created collection: {c.id.id if c.id else 'N/A'}")  # type: ignore[union-attr]
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@collections.command("delete")
@click.argument("collection_id")
@click.pass_context
def collections_delete(ctx: click.Context, collection_id: str) -> None:
    """Delete a collection."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                await client.collections.delete(collection_id)
                click.echo(f"Deleted collection: {collection_id}")
        except NotFoundError:
            click.echo(f"Collection '{collection_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@collections.command("files")
@click.argument("collection_id")
@click.option("--page", default=0, type=int, help="Page number (0-based)")
@click.option("--page-size", default=20, type=int, help="Items per page")
@click.pass_context
def collections_files(ctx: click.Context, collection_id: str, page: int, page_size: int) -> None:
    """List files in a collection."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.collections.list_files(
                    collection_id=collection_id,
                    page=page,
                    page_size=page_size,
                )

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    if isinstance(result.data, list):
                        for f in result.data:
                            file_id = f.id.id if f.id else "N/A"  # type: ignore[union-attr]
                            click.echo(f"{file_id}  {f.name or 'N/A'}")
                    click.echo(f"\nPage {page + 1}/{result.total_pages or 1} | Total: {result.total_elements or 0}")
        except NotFoundError:
            click.echo(f"Collection '{collection_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@collections.command("add-file")
@click.argument("collection_id")
@click.argument("file_id")
@click.pass_context
def collections_add_file(ctx: click.Context, collection_id: str, file_id: str) -> None:
    """Add a file to a collection."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                await client.collections.add_file(collection_id, file_id)
                click.echo(f"Added file {file_id} to collection {collection_id}")
        except NotFoundError:
            click.echo("Collection or file not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@collections.command("remove-file")
@click.argument("collection_id")
@click.argument("file_id")
@click.pass_context
def collections_remove_file(ctx: click.Context, collection_id: str, file_id: str) -> None:
    """Remove a file from a collection."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                await client.collections.remove_file(collection_id, file_id)
                click.echo(f"Removed file {file_id} from collection {collection_id}")
        except NotFoundError:
            click.echo("Collection or file association not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@cli.group()
def extraction() -> None:
    """Manage extraction jobs."""


@extraction.command("list")
@click.option("--page", default=0, type=int, help="Page number (0-based)")
@click.option("--page-size", default=20, type=int, help="Items per page")
@click.pass_context
def extraction_list(ctx: click.Context, page: int, page_size: int) -> None:
    """List extraction jobs."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.extraction.list(page=page, page_size=page_size)

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    if isinstance(result.data, list):
                        for job in result.data:
                            job_id = job.job_id or "N/A"
                            status = job.status.value if job.status else "N/A"  # type: ignore[union-attr]
                            click.echo(f"{job_id}  {status}")
                    click.echo(f"\nPage {page + 1}/{result.total_pages or 1} | Total: {result.total_elements or 0}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@extraction.command("get")
@click.argument("job_id")
@click.pass_context
def extraction_get(ctx: click.Context, job_id: str) -> None:
    """Get an extraction job by ID."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                job = await client.extraction.get(job_id)

                if output_json:
                    click.echo(json.dumps(job.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"Job ID:   {job.job_id or 'N/A'}")
                    click.echo(f"Status:   {job.status.value if job.status else 'N/A'}")  # type: ignore[union-attr]
                    click.echo(f"Task:     {job.task_type or 'N/A'}")
        except NotFoundError:
            click.echo(f"Job '{job_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@extraction.command("results")
@click.argument("job_id")
@click.pass_context
def extraction_results(ctx: click.Context, job_id: str) -> None:
    """Get extraction job results."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                outputs = await client.extraction.get_outputs(job_id)
                click.echo(json.dumps(outputs.to_dict(), indent=2, default=str))
        except NotFoundError:
            click.echo(f"Job '{job_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@cli.group()
def qa() -> None:
    """Manage question answering jobs."""


@qa.command("list")
@click.option("--page", default=0, type=int, help="Page number (0-based)")
@click.option("--page-size", default=20, type=int, help="Items per page")
@click.pass_context
def qa_list(ctx: click.Context, page: int, page_size: int) -> None:
    """List QA jobs."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                result = await client.qa.list(page=page, page_size=page_size)

                if output_json:
                    click.echo(json.dumps(result.to_dict(), indent=2, default=str))
                else:
                    if isinstance(result.data, list):
                        for job in result.data:
                            job_id = job.job_id or "N/A"
                            status = job.status.value if job.status else "N/A"  # type: ignore[union-attr]
                            click.echo(f"{job_id}  {status}")
                    click.echo(f"\nPage {page + 1}/{result.total_pages or 1} | Total: {result.total_elements or 0}")
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@qa.command("get")
@click.argument("job_id")
@click.pass_context
def qa_get(ctx: click.Context, job_id: str) -> None:
    """Get a QA job by ID."""
    client = get_client(ctx)
    output_json: bool = ctx.obj["json"]

    async def _run() -> None:
        try:
            async with client:
                job = await client.qa.get(job_id)

                if output_json:
                    click.echo(json.dumps(job.to_dict(), indent=2, default=str))
                else:
                    click.echo(f"Job ID:   {job.job_id or 'N/A'}")
                    click.echo(f"Status:   {job.status.value if job.status else 'N/A'}")  # type: ignore[union-attr]
                    click.echo(f"Task:     {job.task_type or 'N/A'}")
        except NotFoundError:
            click.echo(f"Job '{job_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


@qa.command("results")
@click.argument("job_id")
@click.pass_context
def qa_results(ctx: click.Context, job_id: str) -> None:
    """Get QA job results."""
    client = get_client(ctx)

    async def _run() -> None:
        try:
            async with client:
                outputs = await client.qa.get_outputs(job_id)
                click.echo(json.dumps(outputs.to_dict(), indent=2, default=str))
        except NotFoundError:
            click.echo(f"Job '{job_id}' not found.", err=True)
            sys.exit(1)
        except BiolevateError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    run_async(_run())


if __name__ == "__main__":
    cli()
