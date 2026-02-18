#!/usr/bin/env python3
"""Get a single provider by ID from the Biolevate API."""

from __future__ import annotations

import asyncio
import json

from biolevate import NotFoundError

from scripts.common import create_client, get_base_parser


async def main() -> None:
    """Get a provider by ID and display its details."""
    parser = get_base_parser("Get a provider by ID from the Biolevate API")
    parser.add_argument("provider_id", help="The provider UUID")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    async with create_client(args) as client:
        try:
            provider = await client.providers.get(args.provider_id)
        except NotFoundError:
            print(f"Provider '{args.provider_id}' not found.")
            return

        if args.json:
            print(json.dumps(provider.to_dict(), indent=2, default=str))
        else:
            print(f"ID:      {provider.id.id if provider.id else 'N/A'}")  # type: ignore[union-attr]
            print(f"Name:    {provider.name or 'N/A'}")
            print(f"Type:    {provider.type_.value if provider.type_ else 'N/A'}")  # type: ignore[union-attr]
            print(f"Icon:    {provider.icon or 'N/A'}")
            print(f"System:  {provider.system}")
            if provider.config:
                print(f"Config:  {type(provider.config).__name__}")


if __name__ == "__main__":
    asyncio.run(main())
