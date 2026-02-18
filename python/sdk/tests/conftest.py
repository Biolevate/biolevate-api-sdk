"""Test fixtures for Biolevate SDK tests."""

import pytest

from biolevate import BiolevateClient


@pytest.fixture
def base_url() -> str:
    """Test API base URL."""
    return "https://api.test.biolevate.com"


@pytest.fixture
def token() -> str:
    """Test authentication token."""
    return "test-jwt-token"


@pytest.fixture
def client(base_url: str, token: str) -> BiolevateClient:
    """Create a test Biolevate client."""
    return BiolevateClient(base_url=base_url, token=token)


@pytest.fixture
def sample_provider_response() -> dict:
    """Sample provider API response."""
    return {
        "id": {"id": "550e8400-e29b-41d4-a716-446655440000", "entityType": "PROVIDER"},
        "createdTime": 1708123456789,
        "owner": {"id": "user-123"},
        "name": "My S3 Bucket",
        "icon": "aws",
        "type": "S3",
        "system": False,
        "config": {
            "type": "S3",
            "bucketName": "my-bucket",
            "region": "us-east-1",
        },
    }


@pytest.fixture
def sample_providers_list_response(sample_provider_response: dict) -> dict:
    """Sample providers list API response."""
    return {
        "data": [sample_provider_response],
        "totalPages": 1,
        "totalElements": 1,
        "hasNext": False,
    }
