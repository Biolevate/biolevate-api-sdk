"""Unit test fixtures: mock HTTP client via respx."""

import pytest
import respx

from biolevate import BiolevateClient


@pytest.fixture
def base_url() -> str:
    return "https://api.test.biolevate.com"


@pytest.fixture
def token() -> str:
    return "test-jwt-token"


@pytest.fixture
def client(base_url: str, token: str) -> BiolevateClient:
    return BiolevateClient(base_url=base_url, token=token)


@pytest.fixture
def mock_http():
    """Activate respx mock transport for the duration of a test."""
    with respx.mock:
        yield respx
