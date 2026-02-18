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


if __name__ == "__main__":
    cli()
