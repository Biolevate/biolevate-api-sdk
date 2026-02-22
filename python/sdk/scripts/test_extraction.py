#!/usr/bin/env python3
"""Integration tests for the Extraction resource.

Uses a file with meaningful content (title, authors, etc.) from
test_resources/extraction_sample.txt. If no indexed file exists, uploads
that file, creates it, and waits for indexation before running extraction.
"""

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import Any, TYPE_CHECKING

from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner

from biolevate_client.models import EliseMetaInput

if TYPE_CHECKING:
    from biolevate.resources.extraction import ExtractionResource
    from biolevate.resources.files import FilesResource

TERMINAL_STATUSES = ("SUCCESS", "FAILED", "ABORTED")


def _default_test_resources_dir() -> Path:
    return Path(__file__).resolve().parent / "test_resources"


def _get_extraction_sample(test_files_dir: Path, test_file_path: Path | None) -> Path | None:
    """Get extraction_sample.txt (required). Returns None only if file doesn't exist."""
    if test_file_path is not None:
        if test_file_path.is_file():
            return test_file_path
        return None
    sample = test_files_dir / "extraction_sample.txt"
    if sample.is_file():
        return sample
    return None


def _mime_type_for_path(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "application/pdf"
    if suffix == ".txt":
        return "text/plain"
    return "application/octet-stream"


async def wait_until_indexed(
    files_resource: FilesResource,
    file_id: str,
    timeout_seconds: float,
    initial_interval: float = 2.0,
    max_interval: float = 10.0,
) -> tuple[bool, float]:
    elapsed = 0.0
    interval = initial_interval
    while elapsed < timeout_seconds:
        file_info = await files_resource.get(file_id)
        if getattr(file_info, "indexed", None) is True:
            return True, elapsed
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 2, max_interval)
    return False, elapsed


async def wait_until_job_terminal(
    extraction_resource: ExtractionResource,
    job_id: str,
    timeout_seconds: float,
    initial_interval: float = 3.0,
    max_interval: float = 15.0,
) -> tuple[str, float]:
    elapsed = 0.0
    interval = initial_interval
    while elapsed < timeout_seconds:
        job = await extraction_resource.get_job(job_id)
        status = getattr(job, "status", None)
        if status in TERMINAL_STATUSES:
            return status, elapsed
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 2, max_interval)
    return "", elapsed


async def main() -> None:
    parser = get_base_parser("Test Extraction resource")
    parser.add_argument(
        "--file-id",
        type=str,
        default=None,
        help="Use this file ID and skip file discovery/setup",
    )
    parser.add_argument(
        "--job-timeout",
        type=float,
        default=180.0,
        help="Max seconds to wait for job to reach terminal state (default: 180)",
    )
    parser.add_argument(
        "--index-timeout",
        type=float,
        default=120.0,
        help="Max seconds to wait for file indexation when using ensure-file (default: 120)",
    )
    parser.add_argument(
        "--test-files-dir",
        type=Path,
        default=None,
        help="Directory for extraction_sample.txt (default: scripts/test_resources)",
    )
    parser.add_argument(
        "--test-file",
        type=Path,
        default=None,
        help="Path to extraction sample file for ensure-file",
    )
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="extraction", api_url=args.api_url)

    test_files_dir = args.test_files_dir or _default_test_resources_dir()
    provider_id: str | None = None
    file_id: str | None = args.file_id
    test_folder_name = f"SDK-TEST-EXTRACTION-{int(time.time())}"
    uploaded_path: str | None = None
    uploaded_name: str | None = None
    job_id: str | None = None

    async with client:
        async def test_setup_provider_and_file() -> dict[str, Any]:
            nonlocal provider_id, file_id, uploaded_path, uploaded_name

            sample_path = _get_extraction_sample(test_files_dir, args.test_file)
            if not sample_path:
                raise AssertionError(
                    f"extraction_sample.txt not found in {test_files_dir}. "
                    "This file is required for extraction tests."
                )

            if args.file_id:
                file_id = args.file_id
                return {
                    "file_id": file_id,
                    "source": "cli",
                    "sample_file": sample_path.name,
                }

            providers = await client.providers.list(page=0, page_size=1)
            if not providers.data or len(providers.data) == 0:
                raise AssertionError("No provider available. Cannot run extraction tests.")

            provider_id = str(providers.data[0].id.id) if providers.data[0].id else None
            if not provider_id:
                raise AssertionError("Provider ID is missing.")

            with open(sample_path, "rb") as f:
                await client.items.upload(
                    provider_id,
                    path=f"/{test_folder_name}",
                    file=f,
                    file_name=sample_path.name,
                    mime_type=_mime_type_for_path(sample_path),
                )
            uploaded_path = f"/{test_folder_name}"
            uploaded_name = sample_path.name

            file_info = await client.files.create(
                provider_id, uploaded_path, uploaded_name
            )
            file_id = str(file_info.id.id) if file_info.id else None
            if not file_id:
                raise AssertionError("Failed to create indexed file.")

            indexed, waited = await wait_until_indexed(
                client.files, file_id, timeout_seconds=args.index_timeout
            )
            if not indexed:
                raise AssertionError(
                    f"File indexation timed out after {waited:.1f}s"
                )

            state_path = Path("test-reports/extraction-test-state.json")
            state_path.parent.mkdir(parents=True, exist_ok=True)
            state_path.write_text(
                json.dumps(
                    {
                        "provider_id": provider_id,
                        "file_id": file_id,
                        "path": uploaded_path,
                        "name": uploaded_name,
                        "folder_name": test_folder_name,
                    },
                    indent=2,
                )
            )
            return {
                "provider_id": provider_id,
                "file_id": file_id,
                "source": "uploaded_sample",
                "sample_file": sample_path.name,
                "indexed_after_seconds": round(waited, 1),
            }

        await runner.run_test(
            name="setup_provider_and_file",
            test_fn=test_setup_provider_and_file,
            expected_message="Provider and file ready for extraction",
        )

        async def test_list_jobs() -> dict[str, Any]:
            result = await client.extraction.list_jobs(page=0, page_size=10)
            assert result.data is not None, "data should not be None"
            assert isinstance(result.data, list), "data should be a list"
            return {
                "total_elements": result.total_elements,
                "total_pages": result.total_pages,
                "count": len(result.data) if result.data else 0,
            }

        await runner.run_test(
            name="list_jobs",
            test_fn=test_list_jobs,
            expected_message="Listed extraction jobs",
        )

        async def test_list_jobs_pagination() -> dict[str, Any]:
            result = await client.extraction.list_jobs(page=0, page_size=1)
            assert result.data is not None, "data should not be None"
            return {
                "page_size_requested": 1,
                "items_returned": len(result.data) if result.data else 0,
                "has_more": result.has_next,
            }

        await runner.run_test(
            name="list_jobs_pagination",
            test_fn=test_list_jobs_pagination,
            expected_message="Pagination works correctly",
        )

        if not file_id:
            for name in (
                "create_job",
                "wait_until_job_terminal",
                "get_job",
                "get_job_inputs",
                "get_job_outputs",
                "get_job_annotations",
                "list_jobs_after_create",
            ):
                runner.skip_test(name, "No file_id available for extraction job")
        else:
            fid: str = file_id

            async def test_create_job() -> dict[str, Any]:
                nonlocal job_id
                metas = [
                    EliseMetaInput.model_validate({
                        "meta": "title",
                        "description": "The title of the document",
                        "answerType": {"dataType": "STRING"},
                    }),
                    EliseMetaInput.model_validate({
                        "meta": "authors",
                        "description": "The authors of the document",
                        "answerType": {"dataType": "STRING", "multiValued": True},
                    }),
                    EliseMetaInput.model_validate({
                        "meta": "date",
                        "description": "The publication date",
                        "answerType": {"dataType": "DATE", "dateFormat": "ISO"},
                    }),
                ]
                job = await client.extraction.create_job(
                    metas=metas,
                    file_ids=[fid],
                )
                job_id = getattr(job, "job_id", None)
                assert job_id, "job_id should be set"
                return {
                    "job_id": job_id,
                    "status": getattr(job, "status", None),
                    "task_type": getattr(job, "task_type", None),
                }

            await runner.run_test(
                name="create_job",
                test_fn=test_create_job,
                expected_message="Created extraction job",
            )

            if job_id:
                jid: str = job_id

                async def test_wait_until_job_terminal() -> dict[str, Any]:
                    status, waited = await wait_until_job_terminal(
                        client.extraction,
                        jid,
                        timeout_seconds=args.job_timeout,
                    )
                    if status not in TERMINAL_STATUSES:
                        raise AssertionError(
                            f"Job did not reach terminal state within {args.job_timeout}s (waited {waited:.1f}s)"
                        )
                    return {"status": status, "waited_seconds": round(waited, 1)}

                await runner.run_test(
                    name="wait_until_job_terminal",
                    test_fn=test_wait_until_job_terminal,
                    expected_message="Job reached terminal state",
                )

                async def test_get_job() -> dict[str, Any]:
                    job = await client.extraction.get_job(jid)
                    status = getattr(job, "status", None)
                    return {
                        "job_id": getattr(job, "job_id", None),
                        "status": status,
                        "execution_time": getattr(job, "execution_time", None),
                        "error_message": getattr(job, "error_message", None),
                    }

                await runner.run_test(
                    name="get_job",
                    test_fn=test_get_job,
                    expected_message="Retrieved extraction job",
                )

                async def test_get_job_inputs() -> dict[str, Any]:
                    inputs = await client.extraction.get_job_inputs(jid)
                    files = getattr(inputs, "files", None)
                    assert files is not None, "inputs.files should be present"
                    input_file_ids = getattr(files, "file_ids", None) or []
                    input_collection_ids = getattr(files, "collection_ids", None) or []
                    metas = getattr(inputs, "metas", None) or []
                    meta_names = [getattr(m, "meta", None) for m in metas]
                    assert fid in input_file_ids, f"Requested file_id {fid} should be in inputs"
                    return {
                        "file_ids": input_file_ids,
                        "collection_ids": input_collection_ids,
                        "metas_requested": meta_names,
                    }

                await runner.run_test(
                    name="get_job_inputs",
                    test_fn=test_get_job_inputs,
                    expected_message="Retrieved job inputs",
                )

                async def test_get_job_outputs() -> dict[str, Any]:
                    outputs = await client.extraction.get_job_outputs(jid)
                    results = getattr(outputs, "results", None)
                    assert results is not None, "outputs.results should be present"
                    assert isinstance(results, list), "outputs.results should be a list"

                    extracted_data: list[dict[str, Any]] = []
                    for r in results:
                        meta_name = getattr(r, "meta", None)
                        answer = getattr(r, "answer", None)
                        raw_value = getattr(r, "raw_value", None)
                        explanation = getattr(r, "explanation", None)
                        answer_value: Any = None
                        if answer:
                            for field in (
                                "str_value", "str_list_value", "bool_value",
                                "long_value", "double_value", "date_value",
                            ):
                                val = getattr(answer, field, None)
                                if val is not None:
                                    answer_value = val
                                    break
                        extracted_data.append({
                            "meta": meta_name,
                            "answer": answer_value,
                            "raw_value": raw_value,
                            "explanation": explanation[:100] if explanation else None,
                        })
                    return {
                        "results_count": len(results),
                        "extracted": extracted_data,
                    }

                await runner.run_test(
                    name="get_job_outputs",
                    test_fn=test_get_job_outputs,
                    expected_message="Retrieved job outputs",
                )

                async def test_get_job_annotations() -> dict[str, Any]:
                    annotations = await client.extraction.get_job_annotations(jid)
                    assert isinstance(annotations, list), "annotations should be a list"
                    annotation_summaries: list[dict[str, Any]] = []
                    for a in annotations[:5]:
                        ann_type = getattr(a, "type", None)
                        ann_status = getattr(a, "status", None)
                        annotation_summaries.append({
                            "type": ann_type,
                            "status": ann_status,
                        })
                    return {
                        "annotations_count": len(annotations),
                        "sample_annotations": annotation_summaries,
                    }

                await runner.run_test(
                    name="get_job_annotations",
                    test_fn=test_get_job_annotations,
                    expected_message="Retrieved job annotations",
                )

                async def test_list_jobs_after_create() -> dict[str, Any]:
                    result = await client.extraction.list_jobs(page=0, page_size=50)
                    assert result.data is not None, "data should not be None"
                    job_ids = [
                        getattr(j, "job_id", None)
                        for j in (result.data or [])
                        if getattr(j, "job_id", None)
                    ]
                    assert jid in job_ids, f"Created job {jid} should appear in list"
                    return {"job_found": True, "total": len(result.data or [])}

                await runner.run_test(
                    name="list_jobs_after_create",
                    test_fn=test_list_jobs_after_create,
                    expected_message="Created job appears in list",
                )

        non_existent_id = "00000000-0000-0000-0000-000000000000"

        async def test_get_job_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.extraction.get_job(non_existent_id)
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_job_not_found",
            test_fn=test_get_job_not_found,
            expected_message="NotFoundError raised for non-existent job",
        )

        async def test_get_job_inputs_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.extraction.get_job_inputs(non_existent_id)
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_job_inputs_not_found",
            test_fn=test_get_job_inputs_not_found,
            expected_message="NotFoundError raised for get_job_inputs",
        )

        async def test_get_job_outputs_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.extraction.get_job_outputs(non_existent_id)
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_job_outputs_not_found",
            test_fn=test_get_job_outputs_not_found,
            expected_message="NotFoundError raised for get_job_outputs",
        )

        async def test_get_job_annotations_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.extraction.get_job_annotations(non_existent_id)
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_job_annotations_not_found",
            test_fn=test_get_job_annotations_not_found,
            expected_message="NotFoundError raised for get_job_annotations",
        )

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
