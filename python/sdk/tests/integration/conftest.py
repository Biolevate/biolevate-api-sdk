"""Integration test fixtures.

Integration tests require a live server. Set the following environment variables
before running:

    BIOLEVATE_API_URL=http://localhost:8080
    BIOLEVATE_TOKEN=<your-personal-access-token>

Run only integration tests with:

    pytest -m integration sdk/tests/integration/

Skip integration tests (default):

    pytest sdk/tests/unit/
"""

from __future__ import annotations

import asyncio
import contextlib
import io
import os
import time
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio

from biolevate import BiolevateClient

_BASE_URL = os.getenv("BIOLEVATE_API_URL", "")
_TOKEN = os.getenv("BIOLEVATE_TOKEN", "")

_REQUIRES_SERVER = pytest.mark.skipif(
    not _BASE_URL or not _TOKEN,
    reason="BIOLEVATE_API_URL and BIOLEVATE_TOKEN must be set to run integration tests",
)


# Apply the skip marker to every test in this directory automatically.
def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    for item in items:
        if "integration" in str(item.fspath):
            item.add_marker(_REQUIRES_SERVER)
            item.add_marker(pytest.mark.integration)


# ---------------------------------------------------------------------------
# Session-scoped live client
# ---------------------------------------------------------------------------


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def live_client() -> AsyncGenerator[BiolevateClient, None]:
    async with BiolevateClient(base_url=_BASE_URL, token=_TOKEN) as client:
        yield client


# ---------------------------------------------------------------------------
# Session-scoped state: discovered / created resources shared across modules
# ---------------------------------------------------------------------------

_TEST_RUN_ID = str(int(time.time()))


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def provider_id(live_client: BiolevateClient) -> str:
    """Return the ID of the first available provider."""
    page = await live_client.providers.list(page=0, page_size=1)
    if not page.data:
        pytest.skip("No providers configured on this server")
    provider = page.data[0]
    return str(provider.id.id)


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def test_folder_key(provider_id: str, live_client: BiolevateClient) -> AsyncGenerator[str, None]:
    """Create a temporary folder in the provider and clean it up after the session."""
    folder_key = f"sdk-integration-tests-{_TEST_RUN_ID}/"
    await live_client.items.create_folder(provider_id, key=folder_key)
    yield folder_key
    with contextlib.suppress(Exception):
        await live_client.items.delete(provider_id, key=folder_key)


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def uploaded_item_key(
    provider_id: str,
    test_folder_key: str,
    live_client: BiolevateClient,
) -> str:
    """Upload a small text file used by the files and AI job tests."""
    file_name = "sdk-test-sample.txt"
    content = (
        b"Biolevate is a document intelligence company founded in 2021. "
        b"The CEO is John Smith. The company has 42 employees and offers "
        b"products including Elise, a platform for AI-powered document analysis."
    )

    await live_client.items.upload(
        provider_id,
        key=test_folder_key,
        file=io.BytesIO(content),
        file_name=file_name,
        mime_type="text/plain",
    )
    return f"{test_folder_key}{file_name}"


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def indexed_file_id(
    provider_id: str,
    uploaded_item_key: str,
    live_client: BiolevateClient,
) -> AsyncGenerator[str, None]:
    """Create an indexed file and wait for indexation to complete."""
    file_info = await live_client.files.create(provider_id, key=uploaded_item_key)
    file_id = str(file_info.id.id)

    # Poll until indexed (up to 120 s with exponential back-off)
    elapsed = 0.0
    interval = 2.0
    while elapsed < 120.0:
        info = await live_client.files.get(file_id)
        if getattr(info, "indexed", False):
            break
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 1.5, 12.0)
    else:
        pytest.skip(f"File {file_id} was not indexed within 120 s — skipping AI-dependent tests")

    yield file_id

    with contextlib.suppress(Exception):
        await live_client.files.delete(file_id)


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def collection_id(live_client: BiolevateClient) -> AsyncGenerator[str, None]:
    """Create a throwaway collection and delete it after the session."""
    collection = await live_client.collections.create(
        name=f"SDK Integration Test {_TEST_RUN_ID}",
        description="Temporary collection created by the integration test suite",
    )
    collection_id = str(collection.id.id)
    yield collection_id
    with contextlib.suppress(Exception):
        await live_client.collections.delete(collection_id)
