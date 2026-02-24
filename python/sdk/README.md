# Biolevate SDK

[![PyPI](https://img.shields.io/pypi/v/biolevate)](https://pypi.org/project/biolevate/)
[![Python](https://img.shields.io/pypi/pyversions/biolevate)](https://pypi.org/project/biolevate/)
[![Coverage](https://raw.githubusercontent.com/Biolevate/biolevate-api-sdk/main/python/sdk/.coverage-badge.svg)](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml)
[![CI](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml)

High-level Python SDK for the Biolevate API.

## Installation

```bash
pip install biolevate
```

## Quick Start

```python
import asyncio
from biolevate import BiolevateClient

async def main():
    async with BiolevateClient(
        base_url="https://api.biolevate.com",
        token="your-jwt-token"
    ) as client:
        # List all providers
        providers = await client.providers.list()
        for provider in providers.data:
            print(f"{provider.name} ({provider.type_})")

        # Get a specific provider
        provider = await client.providers.get("provider-uuid")
        print(f"Provider: {provider.name}")

asyncio.run(main())
```

## Features

- **Async-first**: Built on httpx for modern async Python
- **Type-safe**: Full type annotations for IDE support
- **Clean API**: High-level wrapper around the generated client
- **Error handling**: Custom exceptions for common error cases

## API Reference

### BiolevateClient

The main entry point for the SDK.

```python
from biolevate import BiolevateClient

client = BiolevateClient(base_url="...", token="...")
```

### Providers

List and retrieve storage providers.

```python
# List providers with pagination
page = await client.providers.list(
    page=0,
    page_size=20,
    sort_by="name",
    sort_order="asc",
    query="s3"  # Optional search filter
)

# Access pagination info
print(f"Total: {page.total_elements}")
print(f"Has more: {page.has_next}")

# Iterate providers
for provider in page.data:
    print(provider.name)
    print(provider.type_)  # S3, AZURE, GCS, LOCAL, etc.
    print(provider.id.id)  # UUID

# Get single provider
provider = await client.providers.get("uuid-here")
```

## Exception Handling

```python
from biolevate import (
    BiolevateClient,
    BiolevateError,
    NotFoundError,
    AuthenticationError,
    APIError,
)

try:
    provider = await client.providers.get("invalid-id")
except NotFoundError:
    print("Provider not found")
except AuthenticationError:
    print("Invalid token or access denied")
except APIError as e:
    print(f"API error {e.status_code}: {e.message}")
except BiolevateError:
    print("General SDK error")
```

## Models

The SDK re-exports commonly used models from the generated client:

```python
from biolevate import Provider, ProviderType, ProviderPage

# Provider is an alias for FSProviderExternal
# ProviderType is an alias for FSProviderExternalType  
# ProviderPage is an alias for PageDataFSProviderExternal
```

## Development

```bash
# Install with dev dependencies
cd python && uv sync --all-extras

# Run tests
uv run pytest sdk/tests -v

# Lint
uv run ruff check sdk/
uv run ruff format sdk/
```
