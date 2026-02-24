# biolevate-api-sdk

[![PyPI](https://img.shields.io/pypi/v/biolevate?v=1)](https://pypi.org/project/biolevate/)
[![Python](https://img.shields.io/pypi/pyversions/biolevate?v=1)](https://pypi.org/project/biolevate/)
[![Coverage](https://raw.githubusercontent.com/Biolevate/biolevate-api-sdk/main/python/sdk/coverage-badge.svg)](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml)
[![CI](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml)

Client SDKs for the [Biolevate API](https://api-docs.biolevatecloud.com/biolevateapi/intro) — the core REST API for the Elise platform.

## Available SDKs

| Language | Package | Version | Source |
|---|---|---|---|
| Python | `biolevate` | [![PyPI](https://img.shields.io/pypi/v/biolevate?v=1)](https://pypi.org/project/biolevate/) | [`python/sdk/`](python/sdk/) |

## Repository Structure

```
├── openapi/                         # OpenAPI specification
│   └── biolevate-api.json
├── python/
│   ├── client/                      # Generated low-level client (biolevate-client)
│   └── sdk/                         # High-level SDK (biolevate)
│       ├── biolevate/               # SDK source
│       ├── tests/
│       │   ├── unit/
│       │   └── integration/
│       └── README.md
├── tools/
│   ├── docker/
│   ├── openapi-generator-config.yaml
│   └── patch-*.py                   # Post-generation patches
└── Makefile
```

The `python/client/` package is auto-generated from the OpenAPI spec and should not be edited manually. The `python/sdk/` package is the hand-written high-level SDK built on top of it.

## Python SDK

### Installation

```bash
pip install biolevate
```

### Quick Start

```python
import asyncio
from biolevate import BiolevateClient

async def main():
    async with BiolevateClient(
        base_url="https://<your-elise-domain>",
        token="<your-pat>",
    ) as client:
        providers = await client.providers.list()
        for provider in providers.data:
            print(provider.name, provider.type_)

asyncio.run(main())
```

See [`python/sdk/README.md`](python/sdk/README.md) for the full API reference, examples for all resources, and error handling.

## Development

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- Docker (for client generation only)

### Setup

```bash
cd python && uv sync --all-extras
```

Or via Make:

```bash
make install-python
```

### Regenerating the Python Client

The low-level client is generated from the OpenAPI spec using [OpenAPI Generator](https://openapi-generator.tech) (v7.20.0). Post-generation patches are applied automatically.

```bash
make generate-python
```

This removes `python/client/`, regenerates it from `openapi/biolevate-api.json`, then applies patches for known quirks in the generated output.

### Testing

```bash
# Unit tests (no server required)
make test-python

# Integration tests (requires a live Elise instance)
cd python && BIOLEVATE_API_URL=https://<your-elise-domain> BIOLEVATE_TOKEN=<your-pat> \
  uv run pytest sdk/tests/integration -v
```

### Linting

```bash
make lint-python
```

## Releases

Releases are automated via [release-please](https://github.com/googleapis/release-please). Merging a conventional commit to `main` creates a release PR. Merging the release PR creates a tag and triggers the PyPI publish workflow.

Commit convention:

| Prefix | Effect |
|---|---|
| `fix:` | Patch version bump |
| `feat:` | Minor version bump |
| `feat!:` or `BREAKING CHANGE` | Major version bump |

## Links

- [Biolevate API documentation](https://api-docs.biolevatecloud.com/biolevateapi/intro)
- [API Reference](https://api-docs.biolevatecloud.com/apis/biolevateapi)
- [Guides & Tutorials](https://api-docs.biolevatecloud.com/biolevateapi/guides/introduction)
