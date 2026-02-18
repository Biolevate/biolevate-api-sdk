#!/usr/bin/env python3
"""List all providers from the Biolevate API."""

from __future__ import annotations

import asyncio

from scripts.common import create_client, get_base_parser, print_table


async def main() -> None:
    """List providers with optional filtering."""
    parser = get_base_parser("List providers from the Biolevate API")
    parser.add_argument("--query", "-q", help="Search filter")
    parser.add_argument("--page", type=int, default=0, help="Page number (0-based)")
    parser.add_argument("--page-size", type=int, default=20, help="Items per page")
    args = parser.parse_args()

    async with create_client(args) as client:
        page = await client.providers.list(
            page=args.page,
            page_size=args.page_size,
            query=args.query,
        )

        rows: list[list[str]] = []
        if isinstance(page.data, list):
            for provider in page.data:
                provider_id = provider.id.id if provider.id else "N/A"  # type: ignore[union-attr]
                name = provider.name if provider.name else "N/A"  # type: ignore[union-attr]
                type_ = str(provider.type_.value) if provider.type_ else "N/A"  # type: ignore[union-attr]
                rows.append([str(provider_id), str(name), type_])

        print_table(["ID", "Name", "Type"], rows)
        print(f"\nPage {args.page + 1}/{page.total_pages or 1} | Total: {page.total_elements or 0}")


if __name__ == "__main__":
    asyncio.run(main())
