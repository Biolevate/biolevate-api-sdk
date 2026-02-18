# Biolevate SDK

High-level Python SDK for the Biolevate API.

## Installation

```bash
pip install biolevate
```

## Usage

```python
from biolevate import BiolevateClient

async with BiolevateClient(base_url="https://api.biolevate.com", token="your-token") as client:
    # Use the client
    pass
```

## Features

- High-level client wrapper around the generated API client
- Async-first design using httpx
- Type-safe with full type annotations
- Pipeline support for common workflows
