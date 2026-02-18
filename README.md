# Biolevate API SDK

Monorepo for Biolevate API client SDKs.

## Structure

```
├── openapi/                    # OpenAPI specifications
│   └── biolevate-api.json
├── python/                     # Python SDK
│   ├── client/                 # Generated API client (biolevate-client)
│   └── sdk/                    # High-level SDK (biolevate)
├── tools/
│   ├── docker/                 # Generator Docker images
│   └── openapi-python-client.yml
└── Makefile
```

## Quick Start

### Prerequisites

- Docker
- Python 3.11+ (for development)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### Generate Python Client

```bash
make generate-python
```

### Install Python SDK

```bash
make install-python
```

### Development

```bash
# Lint and format
make lint-python

# Run tests
make test-python
```

## Python SDK Usage

```python
from biolevate import BiolevateClient

async with BiolevateClient(base_url="https://api.biolevate.com", token="your-token") as client:
    # Use the client
    pass
```

## Adding New Language SDKs

1. Create a new Dockerfile in `tools/docker/` for the generator
2. Add generator version and targets to `Makefile`
3. Create the language directory with `client/` and `sdk/` subdirectories

## Version Management

Generator versions are pinned in the Makefile. To upgrade:

1. Update the version in `Makefile`
2. Run `make generate-<lang>` to regenerate
3. Review diffs and run tests
4. Commit the version bump and regenerated code together
