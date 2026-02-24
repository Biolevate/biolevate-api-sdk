# Biolevate Python SDK

[![PyPI](https://img.shields.io/pypi/v/biolevate)](https://pypi.org/project/biolevate/)
[![Python](https://img.shields.io/pypi/pyversions/biolevate)](https://pypi.org/project/biolevate/)
[![Coverage](https://raw.githubusercontent.com/Biolevate/biolevate-api-sdk/main/python/sdk/coverage-badge.svg)](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml)
[![CI](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/Biolevate/biolevate-api-sdk/actions/workflows/ci.yml)

Python SDK for the [Biolevate API](https://api-docs.biolevatecloud.com/biolevateapi/intro) — the core REST API for the Elise platform. Connect to your storage backends, index documents with AI, organise collections, and run Question Answering or Extraction jobs.

## Installation

```bash
pip install biolevate
```

Requires Python 3.11+.

## Authentication

The Biolevate API uses Bearer token authentication via a Personal Access Token (PAT). Tokens are provided by Biolevate upon request. Self-service token management through the Elise admin portal is coming soon.

```python
from biolevate import BiolevateClient

client = BiolevateClient(
    base_url="https://<your-elise-domain>",
    token="<your-pat>",
)
```

The client can also be used as an async context manager:

```python
async with BiolevateClient(base_url="...", token="...") as client:
    providers = await client.providers.list()
```

## Quick Start

```python
import asyncio
from biolevate import BiolevateClient

async def main():
    async with BiolevateClient(base_url="https://<your-elise-domain>", token="<your-pat>") as client:
        providers = await client.providers.list()
        for provider in providers.data:
            print(provider.name, provider.type_)

asyncio.run(main())
```

## Resources

### Providers

Browse the storage backends connected to your Elise instance. Providers are configured through the admin UI and are read-only from the API.

```python
page = await client.providers.list(page=0, page_size=20, query="s3")
print(f"{page.total_elements} providers found")

for provider in page.data:
    print(provider.id.id)   # UUID used in subsequent calls
    print(provider.name)
    print(provider.type_)   # S3, AZURE, GCS, LOCAL, ...

provider = await client.providers.get("uuid-here")
```

### Provider Items

Manage files and folders within a provider's storage backend.

```python
# List items at a path
items = await client.provider_items.list(provider_id="uuid", key="path/to/folder/")

# Upload a file
with open("report.pdf", "rb") as f:
    item = await client.provider_items.upload(
        provider_id="uuid",
        key="reports/report.pdf",
        content=f.read(),
        content_type="application/pdf",
    )

# Create a folder
folder = await client.provider_items.create_folder(provider_id="uuid", key="reports/2024/")

# Get a pre-signed download URL
url = await client.provider_items.get_download_url(provider_id="uuid", key="reports/report.pdf")

# Delete an item
await client.provider_items.delete(provider_id="uuid", key="reports/old-report.pdf")
```

### Files

Index a provider item as an EliseFile to make it available for AI-powered analysis.

```python
# Index a file (triggers AI analysis)
file = await client.files.create(
    provider_id="provider-uuid",
    key="reports/report.pdf",
)
print(file.id.id)  # UUID of the indexed EliseFile

# Get an indexed file
file = await client.files.get("file-uuid")

# List indexed files
page = await client.files.list(provider_id="provider-uuid", page=0, page_size=20)

# Trigger reindexing after the source file changes
await client.files.reindex("file-uuid")

# Delete the indexed file (does not delete the source from storage)
await client.files.delete("file-uuid")
```

### Collections

Organise indexed files into named collections for structured workflows.

```python
# Create a collection
collection = await client.collections.create(name="Q4 Reports", description="All Q4 2024 reports")

# List collections
page = await client.collections.list(query="Q4")

# Add/remove files
await client.collections.add_file(collection_id=collection.id.id, file_id="file-uuid")
await client.collections.remove_file(collection_id=collection.id.id, file_id="file-uuid")

# List files in a collection
files = await client.collections.list_files(collection_id=collection.id.id)

# Update or delete
await client.collections.update(collection_id=collection.id.id, name="Q4 Reports 2024")
await client.collections.delete(collection_id=collection.id.id)
```

### Question Answering

Ask natural-language questions about indexed documents. Jobs run asynchronously — submit, poll until complete, then retrieve results.

```python
from biolevate import QuestionInput

job = await client.question_answering.create_job(
    file_ids=["file-uuid-1", "file-uuid-2"],
    collection_ids=[],
    questions=[
        QuestionInput(
            id="q1",
            question="What is the main conclusion of this document?",
            answer_type={"dataType": "STRING", "multiValued": False},
        ),
        QuestionInput(
            id="q2",
            question="What is the publication date?",
            answer_type={"dataType": "DATE", "multiValued": False},
        ),
    ],
)

# Poll until complete
import asyncio
while True:
    status = await client.question_answering.get_job(job.id.id)
    if status.status in ("SUCCESS", "FAILED"):
        break
    await asyncio.sleep(2)

# Retrieve answers
results = await client.question_answering.get_job_outputs(job.id.id)
for result in results:
    print(result.question, "->", result.raw_value)
    print("Source:", result.explanation)

# Retrieve source annotations (passages used by the AI)
annotations = await client.question_answering.get_job_annotations(job.id.id)
```

### Extraction

Extract typed metadata fields from indexed documents. The AI extracts structured values based on field definitions you provide.

```python
from biolevate import MetaInput

job = await client.extraction.create_job(
    file_ids=["file-uuid"],
    collection_ids=[],
    metas=[
        MetaInput(
            meta="document_title",
            description="The full title of the document",
            answer_type={"dataType": "STRING", "multiValued": False},
        ),
        MetaInput(
            meta="study_year",
            description="The year the study was conducted or published",
            answer_type={"dataType": "INT", "multiValued": False},
        ),
        MetaInput(
            meta="risk_level",
            description="The assessed risk level",
            answer_type={"dataType": "ENUM", "multiValued": False, "enumValues": ["LOW", "MEDIUM", "HIGH"]},
        ),
    ],
)

# Poll until complete
import asyncio
while True:
    status = await client.extraction.get_job(job.id.id)
    if status.status in ("SUCCESS", "FAILED"):
        break
    await asyncio.sleep(2)

# Retrieve extracted values
results = await client.extraction.get_job_outputs(job.id.id)
for result in results:
    print(result.meta, "->", result.answer)
    print("Explanation:", result.explanation)
```

## Error Handling

```python
from biolevate import BiolevateClient, NotFoundError, AuthenticationError, APIError, BiolevateError

try:
    file = await client.files.get("unknown-uuid")
except NotFoundError:
    print("File not found")
except AuthenticationError:
    print("Invalid token or insufficient permissions")
except APIError as e:
    print(f"API error {e.status_code}: {e.message}")
except BiolevateError:
    print("Unexpected SDK error")
```

| Exception | HTTP status | When raised |
|---|---|---|
| `AuthenticationError` | 401, 403 | Invalid token or insufficient permissions |
| `NotFoundError` | 404 | Resource does not exist |
| `APIError` | Any other 4xx/5xx | Unexpected API error |
| `BiolevateError` | — | Base class for all SDK exceptions |

## Development

```bash
# Install with dev dependencies
cd python && uv sync --all-extras

# Run unit tests
uv run pytest sdk/tests/unit -v

# Run integration tests (requires a live Elise instance)
BIOLEVATE_API_URL=https://<your-elise-domain> BIOLEVATE_TOKEN=<your-pat> \
  uv run pytest sdk/tests/integration -v

# Lint and format
uv run ruff check sdk/
uv run ruff format sdk/
```

## Links

- [Official API documentation](https://api-docs.biolevatecloud.com/biolevateapi/intro)
- [API Reference](https://api-docs.biolevatecloud.com/apis/biolevateapi)
- [Guides & Tutorials](https://api-docs.biolevatecloud.com/biolevateapi/guides/introduction)
