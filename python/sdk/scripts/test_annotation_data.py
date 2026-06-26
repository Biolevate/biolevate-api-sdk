#!/usr/bin/env python3
"""Verify EliseAnnotation.data deserializes correctly from annotation endpoints.

Regression check for: annotation.data was None at runtime while the raw HTTP
response still contained a populated "data" object.

Run from the python workspace:
    uv run python sdk/scripts/test_annotation_data.py
"""

from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx
import respx

from biolevate import BiolevateClient
from biolevate_client import ApiClient, Configuration
from biolevate_client.models.elise_annotation import EliseAnnotation
from biolevate_client.models.elise_document_statement import EliseDocumentStatement
from biolevate_client.models.elise_web_statement import EliseWebStatement

BASE_URL = "https://example.test"
JOB_ID = "job-123"
EXPECTED_CONTENT = "Biolevate is a leading company in document intelligence."

# Shape returned by /api/core/*/jobs/{id}/annotations
SAMPLE_ANNOTATION_RESPONSE: list[dict[str, Any]] = [
    {
        "id": {"id": "aaaabbbb-cccc-dddd-eeee-ffffaaaabbbb", "entityType": "ANNOTATION"},
        "type": "DOCUMENT_STATEMENT",
        "status": "VALID",
        "data": {
            "type": "DOCUMENT_STATEMENT",
            "documentName": "report.pdf",
            "documentId": "file-001",
            "content": EXPECTED_CONTENT,
            "positions": [
                {
                    "type": "BBOX",
                    "page_number": 1,
                    "bbox": {"x0": 10.0, "y0": 20.0, "x1": 110.0, "y1": 40.0},
                }
            ],
        },
    },
    {
        "type": "WEB_STATEMENT",
        "status": "VALID",
        "data": {
            "type": "WEB_STATEMENT",
            "url": "https://example.com/article",
            "source": "WEB",
        },
    },
]

ANNOTATION_ENDPOINTS: list[tuple[str, str]] = [
    ("extraction", f"/api/core/extraction/jobs/{JOB_ID}/annotations"),
    ("question_answering", f"/api/core/qa/jobs/{JOB_ID}/annotations"),
    ("multi_dimensional_extraction", f"/api/core/multi-dim-extraction/jobs/{JOB_ID}/annotations"),
    ("agent", f"/api/core/agent/jobs/{JOB_ID}/annotations"),
]


class CheckFailed(Exception):
    pass


def check(name: str, condition: bool, detail: str = "") -> None:
    if condition:
        print(f"  PASS  {name}")
        return
    message = f"  FAIL  {name}"
    if detail:
        message += f"\n        {detail}"
    raise CheckFailed(message)


def assert_annotation_data_parsed(annotation: EliseAnnotation, *, label: str) -> None:
    check(f"{label}: data is not None", annotation.data is not None)
    assert annotation.data is not None

    if annotation.type == "DOCUMENT_STATEMENT":
        check(
            f"{label}: data is EliseDocumentStatement",
            isinstance(annotation.data, EliseDocumentStatement),
            f"got {type(annotation.data).__name__}",
        )
        check(
            f"{label}: content preserved",
            annotation.data.content == EXPECTED_CONTENT,
            f"expected {EXPECTED_CONTENT!r}, got {annotation.data.content!r}",
        )
        check(
            f"{label}: positions parsed",
            annotation.data.positions is not None and len(annotation.data.positions) == 1,
        )
    elif annotation.type == "WEB_STATEMENT":
        check(
            f"{label}: data is EliseWebStatement",
            isinstance(annotation.data, EliseWebStatement),
            f"got {type(annotation.data).__name__}",
        )
        check(
            f"{label}: url preserved",
            annotation.data.url == "https://example.com/article",
        )


def test_model_from_dict() -> None:
    print("\n[1] EliseAnnotation.from_dict (direct model)")
    for index, payload in enumerate(SAMPLE_ANNOTATION_RESPONSE):
        annotation = EliseAnnotation.from_dict(payload)
        assert annotation is not None
        assert_annotation_data_parsed(annotation, label=f"annotation[{index}]")


def test_api_client_deserialize() -> None:
    print("\n[2] ApiClient.deserialize (generated HTTP client path)")
    config = Configuration(host=BASE_URL)
    api_client = ApiClient(config)
    raw_json = json.dumps(SAMPLE_ANNOTATION_RESPONSE)

    annotations = api_client.deserialize(raw_json, "List[EliseAnnotation]", "application/json")

    check("response is a list", isinstance(annotations, list))
    check("response length", len(annotations) == len(SAMPLE_ANNOTATION_RESPONSE))

    for index, annotation in enumerate(annotations):
        assert_annotation_data_parsed(annotation, label=f"annotation[{index}]")


async def test_sdk_annotation_endpoints() -> None:
    print("\n[3] Biolevate SDK (mocked annotation endpoints)")

    async with BiolevateClient(base_url=BASE_URL, token="test-token") as client:
        for resource_name, path in ANNOTATION_ENDPOINTS:
            with respx.mock(base_url=BASE_URL, assert_all_called=False) as router:
                route = router.get(path).mock(return_value=httpx.Response(200, json=SAMPLE_ANNOTATION_RESPONSE))

                if resource_name == "extraction":
                    annotations = await client.extraction.get_job_annotations(JOB_ID)
                elif resource_name == "question_answering":
                    annotations = await client.qa.get_job_annotations(JOB_ID)
                elif resource_name == "multi_dimensional_extraction":
                    annotations = await client.mde.get_job_annotations(JOB_ID)
                else:
                    annotations = await client.agent.get_job_annotations(JOB_ID)

                check(f"{resource_name}: endpoint called", route.called)
                check(
                    f"{resource_name}: returns list",
                    isinstance(annotations, list) and len(annotations) == 2,
                )
                assert_annotation_data_parsed(annotations[0], label=f"{resource_name}[0]")
                assert_annotation_data_parsed(annotations[1], label=f"{resource_name}[1]")


async def main() -> int:
    print("Annotation data deserialization regression test")
    print("Checking that EliseAnnotation.data is populated from raw JSON responses.")

    try:
        test_model_from_dict()
        test_api_client_deserialize()
        await test_sdk_annotation_endpoints()
    except CheckFailed as exc:
        print(f"\n{exc}")
        return 1
    except Exception as exc:
        print(f"\n  FAIL  unexpected error: {exc}")
        raise

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
