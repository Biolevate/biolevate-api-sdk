"""Common utilities for scripts."""

from __future__ import annotations

import argparse
import os
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from biolevate import BiolevateClient


def get_base_parser(description: str = "Biolevate SDK script") -> argparse.ArgumentParser:
    """Create a base argument parser with common options.

    Args:
        description: Script description for help text.

    Returns:
        Configured argument parser with --api-url and --token options.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--api-url",
        default=os.getenv("BIOLEVATE_API_URL"),
        help="Biolevate API URL (or set BIOLEVATE_API_URL env var)",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("BIOLEVATE_TOKEN"),
        help="Authentication token (or set BIOLEVATE_TOKEN env var)",
    )
    return parser


def create_client(args: argparse.Namespace) -> BiolevateClient:
    """Create a BiolevateClient from parsed arguments.

    Args:
        args: Parsed command line arguments with api_url and token.

    Returns:
        Configured BiolevateClient instance.

    Raises:
        SystemExit: If required credentials are missing.
    """
    from biolevate import BiolevateClient

    if not args.api_url:
        print("Error: --api-url is required (or set BIOLEVATE_API_URL)", file=sys.stderr)
        sys.exit(1)

    if not args.token:
        print("Error: --token is required (or set BIOLEVATE_TOKEN)", file=sys.stderr)
        sys.exit(1)

    return BiolevateClient(base_url=args.api_url, token=args.token)


def print_table(headers: list[str], rows: list[list[str]]) -> None:
    """Print a simple formatted table.

    Args:
        headers: Column header names.
        rows: List of rows, each row is a list of column values.
    """
    if not rows:
        print("No results.")
        return

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    header_line = "  ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("-" * len(header_line))

    for row in rows:
        print("  ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))
