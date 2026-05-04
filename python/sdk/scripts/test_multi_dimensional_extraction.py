#!/usr/bin/env python3
"""Integration smoke tests for the Multi-Dimensional Extraction resource."""

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import TYPE_CHECKING, Any

from biolevate import EntityColumnInput, EntitySchemaInput
from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner

if TYPE_CHECKING:
    from biolevate.resources.files import FilesResource
    from biolevate.resources.multi_dimensional_extraction import MultiDimensionalExtractionResource

TERMINAL_STATUSES = ("SUCCESS", "FAILED", "ABORTED")


def _default_test_resources_dir() -> Path:
    return Path(__file__).resolve().parent / "test_resources"


def _get_mde_sample(test_files_dir: Path, test_file_path: Path | None) -> Path | None:
    if test_file_path is not None:
        if test_file_path.is_file():
            return test_file_path
        return None

    for sample_name in ("mde_sample.txt", "extraction_sample.txt", "sample.txt"):
        sample = test_files_dir / sample_name
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


def build_schema() -> EntitySchemaInput:
    return EntitySchemaInput(
        name="ClinicalOutcome",
        columns=[
            EntityColumnInput.model_validate(
                {
                    "key": "study_id",
                    "label": "Study ID",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_IDENTIFIER",
                    "description": "Stable trial, PubMed, DOI, or registry identifier if available",
                    "isRowKey": True,
                }
            ),
            EntityColumnInput.model_validate(
                {
                    "key": "treatment_arm",
                    "label": "Treatment arm",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_GROUP",
                    "description": "Treatment arm, cohort, or subgroup",
                    "isRowKey": True,
                }
            ),
            EntityColumnInput.model_validate(
                {
                    "key": "timepoint",
                    "label": "Timepoint",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_TIMEPOINT",
                    "description": "Visit, week, month, or follow-up duration for the measurement",
                    "isRowKey": True,
                }
            ),
            EntityColumnInput.model_validate(
                {
                    "key": "outcome_value",
                    "label": "Outcome value",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_VALUE",
                    "description": "Measured outcome, score, percentage, p-value, or textual result",
                    "isRowKey": False,
                }
            ),
            EntityColumnInput.model_validate(
                {
                    "key": "unit",
                    "label": "Unit",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_UNIT",
                    "description": "Unit or scale when reported separately from the value",
                    "isRowKey": False,
                }
            ),
            EntityColumnInput.model_validate(
                {
                    "key": "note",
                    "label": "Note",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_COMMENT",
                    "description": "Caveat, footnote, or extraction note",
                    "isRowKey": False,
                }
            ),
        ],
    )


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
    mde_resource: MultiDimensionalExtractionResource,
    job_id: str,
    timeout_seconds: float,
    initial_interval: float = 3.0,
    max_interval: float = 15.0,
) -> tuple[str, float]:
    elapsed = 0.0
    interval = initial_interval
    while elapsed < timeout_seconds:
        job = await mde_resource.get_job(job_id)
        status = getattr(job, "status", None)
        if status in TERMINAL_STATUSES:
            return status, elapsed
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 2, max_interval)
    return "", elapsed


async def main() -> None:
    parser = get_base_parser("Test Multi-Dimensional Extraction resource")
    parser.add_argument(
        "--provider-id",
        type=str,
        default=None,
        help="ID of the provider to use when no file or collection is provided (default: first available)",
    )
    parser.add_argument(
        "--file-id",
        action="append",
        default=[],
        help="Indexed EliseFile ID to use. Can be passed multiple times.",
    )
    parser.add_argument(
        "--collection-id",
        action="append",
        default=[],
        help="Collection ID to use. Can be passed multiple times.",
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
        help="Max seconds to wait for file indexation when uploading a sample file (default: 120)",
    )
    parser.add_argument(
        "--test-files-dir",
        type=Path,
        default=None,
        help="Directory for MDE sample files (default: scripts/test_resources)",
    )
    parser.add_argument(
        "--test-file",
        type=Path,
        default=None,
        help="Path to MDE sample file when no file or collection is provided",
    )
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="multi_dimensional_extraction", api_url=args.api_url)

    test_files_dir = args.test_files_dir or _default_test_resources_dir()
    provider_id: str | None = None
    file_ids: list[str] = list(args.file_id)
    test_folder_name = f"SDK-TEST-MDE-{int(time.time())}"
    uploaded_key: str | None = None
    job_id: str | None = None

    async with client:

        async def test_setup_provider_and_file() -> dict[str, Any]:
            nonlocal provider_id, uploaded_key, file_ids

            if file_ids:
                return {
                    "file_ids": file_ids,
                    "collection_ids": args.collection_id,
                    "source": "cli_file_id",
                }

            if args.collection_id:
                return {
                    "file_ids": file_ids,
                    "collection_ids": args.collection_id,
                    "source": "cli_collection_id",
                }

            sample_path = _get_mde_sample(test_files_dir, args.test_file)
            if not sample_path:
                raise AssertionError(
                    f"No MDE sample file found in {test_files_dir}. "
                    "Provide --file-id, --collection-id, --test-file, or add mde_sample.txt."
                )

            if args.provider_id:
                provider_id = args.provider_id
            else:
                providers = await client.providers.list(page=0, page_size=1)
                if not providers.data or len(providers.data) == 0:
                    raise AssertionError("No provider available. Cannot run MDE tests.")
                provider_id = str(providers.data[0].id.id) if providers.data[0].id else None

            if not provider_id:
                raise AssertionError("Provider ID is missing.")

            with open(sample_path, "rb") as f:
                await client.items.upload(
                    provider_id,
                    key=f"{test_folder_name}/",
                    file=f,
                    file_name=sample_path.name,
                    mime_type=_mime_type_for_path(sample_path),
                )
            uploaded_key = f"{test_folder_name}/{sample_path.name}"

            file_info = await client.files.create(provider_id, key=uploaded_key)
            file_id = str(file_info.id.id) if file_info.id else None
            if not file_id:
                raise AssertionError("Failed to create indexed file.")

            indexed, waited = await wait_until_indexed(client.files, file_id, timeout_seconds=args.index_timeout)
            if not indexed:
                raise AssertionError(f"File indexation timed out after {waited:.1f}s")

            file_ids = [file_id]
            state_path = Path("test-reports/mde-test-state.json")
            state_path.parent.mkdir(parents=True, exist_ok=True)
            state_path.write_text(
                json.dumps(
                    {
                        "provider_id": provider_id,
                        "file_id": file_id,
                        "key": uploaded_key,
                        "folder_name": test_folder_name,
                    },
                    indent=2,
                )
            )
            return {
                "provider_id": provider_id,
                "file_ids": file_ids,
                "source": "uploaded_sample",
                "sample_file": sample_path.name,
                "indexed_after_seconds": round(waited, 1),
            }

        await runner.run_test(
            name="setup_provider_and_file",
            test_fn=test_setup_provider_and_file,
            expected_message="Provider and file ready for MDE",
        )

        async def test_list_jobs() -> dict[str, Any]:
            result = await client.mde.list_jobs(page=0, page_size=10)
            assert result.data is not None, "data should not be None"
            assert isinstance(result.data, list), "data should be a list"
            return {
                "total_elements": result.total_elements,
                "total_pages": result.total_pages,
                "count": len(result.data),
            }

        await runner.run_test(
            name="list_jobs",
            test_fn=test_list_jobs,
            expected_message="Successfully listed MDE jobs",
        )

        if not file_ids and not args.collection_id:
            runner.skip_test("create_job", "No file_id or collection_id available for MDE")
            runner.skip_test("get_job", "MDE job was not created")
            runner.skip_test("get_job_inputs", "MDE job was not created")
            runner.skip_test("wait_and_results", "MDE job was not created")
            runner.skip_test("get_job_annotations", "MDE job was not created")
        else:

            async def test_create_job() -> dict[str, Any]:
                nonlocal job_id

                job = await client.mde.create_job(
                    schema=build_schema(),
                    file_ids=file_ids or None,
                    collection_ids=args.collection_id or None,
                )
                job_id = job.job_id
                if not job_id:
                    raise AssertionError("MDE job ID is missing.")

                return {
                    "job_id": job_id,
                    "status": job.status,
                    "file_ids": file_ids,
                    "collection_ids": args.collection_id,
                }

            await runner.run_test(
                name="create_job",
                test_fn=test_create_job,
                expected_message="MDE job created",
            )

            if job_id:

                async def test_get_job() -> dict[str, Any]:
                    current_job_id = job_id
                    if current_job_id is None:
                        raise AssertionError("MDE job was not created")

                    job = await client.mde.get_job(current_job_id)
                    return {
                        "job_id": job.job_id,
                        "status": job.status,
                        "task_type": job.task_type,
                    }

                await runner.run_test(
                    name="get_job",
                    test_fn=test_get_job,
                    expected_message=f"Successfully retrieved MDE job {job_id}",
                )

                async def test_get_job_inputs() -> dict[str, Any]:
                    current_job_id = job_id
                    if current_job_id is None:
                        raise AssertionError("MDE job was not created")

                    inputs = await client.mde.get_job_inputs(current_job_id)
                    schema = inputs.var_schema
                    return {
                        "has_files": inputs.files is not None,
                        "schema_name": schema.name if schema else None,
                        "column_count": len(schema.columns or []) if schema else 0,
                    }

                await runner.run_test(
                    name="get_job_inputs",
                    test_fn=test_get_job_inputs,
                    expected_message="Successfully retrieved MDE inputs",
                )

                async def test_wait_and_results() -> dict[str, Any]:
                    current_job_id = job_id
                    if current_job_id is None:
                        raise AssertionError("MDE job was not created")

                    status, waited = await wait_until_job_terminal(
                        client.mde,
                        current_job_id,
                        timeout_seconds=args.job_timeout,
                    )
                    if not status:
                        raise AssertionError(f"MDE job timed out after {waited:.1f}s")

                    details: dict[str, Any] = {
                        "job_id": current_job_id,
                        "status": status,
                        "waited_seconds": round(waited, 1),
                    }

                    if status == "SUCCESS":
                        outputs = await client.mde.get_job_outputs(current_job_id)
                        entity_extraction = outputs.entity_extraction
                        rows = entity_extraction.rows if entity_extraction else []
                        details["row_count"] = len(rows or [])
                        if rows:
                            details["first_row"] = [
                                {"column_key": cell.column_key, "value": cell.value} for cell in (rows[0].cells or [])
                            ]

                    return details

                await runner.run_test(
                    name="wait_and_results",
                    test_fn=test_wait_and_results,
                    expected_message="MDE job reached terminal status",
                )

                async def test_get_job_annotations() -> dict[str, Any]:
                    current_job_id = job_id
                    if current_job_id is None:
                        raise AssertionError("MDE job was not created")

                    annotations = await client.mde.get_job_annotations(current_job_id)
                    return {
                        "count": len(annotations),
                    }

                await runner.run_test(
                    name="get_job_annotations",
                    test_fn=test_get_job_annotations,
                    expected_message="Successfully retrieved MDE annotations",
                )
            else:
                runner.skip_test("get_job", "MDE job was not created")
                runner.skip_test("get_job_inputs", "MDE job was not created")
                runner.skip_test("wait_and_results", "MDE job was not created")
                runner.skip_test("get_job_annotations", "MDE job was not created")

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
