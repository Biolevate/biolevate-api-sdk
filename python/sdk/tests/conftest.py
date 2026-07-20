"""Shared test fixtures for unit and integration test suites."""

import pytest

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


# ---------------------------------------------------------------------------
# Reusable model payloads shared across unit test modules
# ---------------------------------------------------------------------------


@pytest.fixture
def provider_payload() -> dict:
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
def provider_page_payload(provider_payload: dict) -> dict:
    return {
        "data": [provider_payload],
        "totalPages": 1,
        "totalElements": 1,
        "hasNext": False,
    }


@pytest.fixture
def provider_item_payload() -> dict:
    return {
        "providerId": "550e8400-e29b-41d4-a716-446655440000",
        "key": "documents/report.pdf",
        "type": "FILE",
        "size": 204800,
    }


@pytest.fixture
def list_items_payload(provider_item_payload: dict) -> dict:
    return {
        "items": [provider_item_payload],
        "cursor": None,
    }


@pytest.fixture
def file_payload() -> dict:
    return {
        "id": {"id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "entityType": "FILE"},
        "createdTime": 1708123456789,
        "owner": {"id": "user-123"},
        "name": "report.pdf",
        "indexed": True,
    }


@pytest.fixture
def file_page_payload(file_payload: dict) -> dict:
    return {
        "data": [file_payload],
        "totalPages": 1,
        "totalElements": 1,
        "hasNext": False,
    }


@pytest.fixture
def collection_payload() -> dict:
    return {
        "id": {"id": "c0ffee00-dead-beef-cafe-123456789abc", "entityType": "COLLECTION"},
        "createdTime": 1708123456789,
        "owner": {"id": "user-123"},
        "name": "Quarterly Reports",
        "description": "All quarterly reports",
    }


@pytest.fixture
def collection_page_payload(collection_payload: dict) -> dict:
    return {
        "data": [collection_payload],
        "totalPages": 1,
        "totalElements": 1,
        "hasNext": False,
    }


@pytest.fixture
def job_payload() -> dict:
    return {
        "jobId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
        "status": "SUCCESS",
        "taskType": "QA",
        "createdTime": 1708123456789,
        "executionTime": 4210,
    }


@pytest.fixture
def job_page_payload(job_payload: dict) -> dict:
    return {
        "data": [job_payload],
        "totalPages": 1,
        "totalElements": 1,
        "hasNext": False,
    }


@pytest.fixture
def qa_job_inputs_payload() -> dict:
    return {
        "files": {"fileIds": ["a1b2c3d4-e5f6-7890-abcd-ef1234567890"], "collectionIds": []},
        "questions": [
            {"id": "q1", "question": "What is the company name?", "answerType": {"dataType": "STRING"}},
        ],
    }


@pytest.fixture
def qa_job_outputs_payload() -> dict:
    return {
        "results": [
            {
                "question": "What is the company name?",
                "rawValue": "Biolevate",
                "explanation": "The document states the company is Biolevate.",
                "sourcedContent": "Biolevate is a leading company...",
                "answerValidity": 1,
                "referenceIds": [],
            }
        ]
    }


@pytest.fixture
def extraction_job_inputs_payload() -> dict:
    return {
        "files": {"fileIds": ["a1b2c3d4-e5f6-7890-abcd-ef1234567890"], "collectionIds": []},
        "metas": [
            {"meta": "title", "answerType": {"dataType": "STRING"}, "description": "Document title"},
        ],
    }


@pytest.fixture
def extraction_job_outputs_payload() -> dict:
    return {
        "results": [
            {
                "meta": "title",
                "rawValue": "Annual Report 2024",
                "referenceIds": [],
            }
        ]
    }


@pytest.fixture
def mde_job_inputs_payload() -> dict:
    return {
        "files": {"fileIds": ["a1b2c3d4-e5f6-7890-abcd-ef1234567890"], "collectionIds": []},
        "schema": {
            "name": "compounds",
            "columns": [
                {
                    "key": "compound",
                    "label": "Compound",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_IDENTIFIER",
                }
            ],
        },
        "prompt": "Extract one row per compound.",
    }


@pytest.fixture
def mde_job_outputs_payload() -> dict:
    return {
        "entityExtraction": {
            "meta": "compounds",
            "schema": {
                "name": "compounds",
                "columns": [{"key": "compound", "label": "Compound"}],
            },
            "rows": [
                {
                    "cells": [
                        {
                            "columnKey": "compound",
                            "value": {"strValue": "aspirin"},
                            "explanation": "Aspirin is mentioned in the document.",
                        }
                    ]
                }
            ],
            "referenceIds": [],
        }
    }


@pytest.fixture
def find_similar_job_payload() -> dict:
    return {
        "jobId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
        "status": "COMPLETED",
        "createdTime": 1708123456789,
        "modifiedTime": 1708123460000,
        "sources": {"sourceIdentifiers": [{"doi": "10.1000/example"}]},
        "result": [],
        "statistics": {
            "sourcesQueried": 1,
            "sourcesMatchedLocally": 0,
            "sourcesMatchedRemotely": 0,
            "sourcesUnmatched": 1,
            "totalFileMatches": 0,
            "totalMetadataOnlyMatches": 0,
        },
    }


@pytest.fixture
def find_similar_job_page_payload(find_similar_job_payload: dict) -> dict:
    return {
        "data": [find_similar_job_payload],
        "totalPages": 1,
        "totalElements": 1,
        "hasNext": False,
    }


# Stateless mode: the inputs carry the full ``messages`` list.
@pytest.fixture
def agent_job_inputs_payload() -> dict:
    return {
        "messages": [
            {"role": "USER", "content": "Summarize the attached report and list the main risks."},
        ],
        "files": {"fileIds": ["a1b2c3d4-e5f6-7890-abcd-ef1234567890"], "collectionIds": []},
        "maxIterations": 10,
    }


# Stateful mode: the inputs carry a single ``message`` and a ``conversationId``.
@pytest.fixture
def agent_job_inputs_stateful_payload() -> dict:
    return {
        "message": "And what about the secondary endpoints?",
        "files": {"fileIds": ["a1b2c3d4-e5f6-7890-abcd-ef1234567890"], "collectionIds": []},
        "maxIterations": 10,
        "conversationId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    }


@pytest.fixture
def agent_job_outputs_payload() -> dict:
    return {
        "answer": {"verdict": "low risk", "summary": "The report shows stable results."},
        "explanation": "Derived from the attached report.",
        "referenceIds": ["aaaabbbb-cccc-dddd-eeee-ffffaaaabbbb"],
    }


@pytest.fixture
def annotation_payload() -> dict:
    return {
        "id": {"id": "aaaabbbb-cccc-dddd-eeee-ffffaaaabbbb", "entityType": "ANNOTATION"},
        "type": "DOCUMENT_STATEMENT",
        "status": "VALID",
        "data": {
            "type": "DOCUMENT_STATEMENT",
            "documentName": "report.pdf",
            "content": "Biolevate is a leading company in document intelligence.",
            "positions": [{"type": "BBOX", "pageNumber": 1, "x": 0, "y": 0, "width": 100, "height": 20}],
        },
    }
