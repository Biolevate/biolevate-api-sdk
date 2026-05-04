#!/usr/bin/env python3
"""Integration smoke tests for the Multi-Dimensional Extraction resource."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any

from biolevate import EntityColumnInput, EntitySchemaInput
from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner

if TYPE_CHECKING:
    from biolevate.resources.multi_dimensional_extraction import MultiDimensionalExtractionResource

TERMINAL_STATUSES = ("SUCCESS", "FAILED", "ABORTED")


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
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="multi_dimensional_extraction", api_url=args.api_url)

    job_id: str | None = None

    async with client:

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

        if not args.file_id and not args.collection_id:
            runner.skip_test("create_job", "Provide --file-id or --collection-id to run MDE")
            runner.skip_test("get_job", "MDE job was not created")
            runner.skip_test("get_job_inputs", "MDE job was not created")
            runner.skip_test("wait_and_results", "MDE job was not created")
            runner.skip_test("get_job_annotations", "MDE job was not created")
        else:

            async def test_create_job() -> dict[str, Any]:
                nonlocal job_id

                job = await client.mde.create_job(
                    schema=build_schema(),
                    file_ids=args.file_id or None,
                    collection_ids=args.collection_id or None,
                )
                job_id = job.job_id
                if not job_id:
                    raise AssertionError("MDE job ID is missing.")

                return {
                    "job_id": job_id,
                    "status": job.status,
                    "file_ids": args.file_id,
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
