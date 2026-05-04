#!/usr/bin/env python3
"""Integration smoke tests for the Find Similar resource."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any

from biolevate import SourceIdentifiers
from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner

if TYPE_CHECKING:
    from biolevate.resources.find_similar import FindSimilarResource

TERMINAL_STATUSES = ("COMPLETED", "FAILED")


def build_source_identifiers(args) -> list[SourceIdentifiers]:
    identifiers: list[SourceIdentifiers] = []

    for doi in args.doi:
        identifiers.append(SourceIdentifiers(doi=doi))
    for source_id in args.source_id:
        identifiers.append(SourceIdentifiers(id=source_id))
    for open_access_id in args.open_access_id:
        identifiers.append(SourceIdentifiers.model_validate({"openAccessId": open_access_id}))

    if not identifiers:
        identifiers.append(SourceIdentifiers(id="35930681"))

    return identifiers


async def wait_until_job_terminal(
    find_similar_resource: FindSimilarResource,
    job_id: str,
    timeout_seconds: float,
    initial_interval: float = 3.0,
    max_interval: float = 15.0,
) -> tuple[str, float]:
    elapsed = 0.0
    interval = initial_interval
    while elapsed < timeout_seconds:
        job = await find_similar_resource.get_job(job_id)
        status = getattr(job, "status", None)
        if status in TERMINAL_STATUSES:
            return status, elapsed
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 2, max_interval)
    return "", elapsed


async def main() -> None:
    parser = get_base_parser("Test Find Similar resource")
    parser.add_argument(
        "--doi",
        action="append",
        default=[],
        help="DOI to use for find-similar. Can be passed multiple times.",
    )
    parser.add_argument(
        "--source-id",
        action="append",
        default=[],
        help="PubMed, Arxiv, or internal source ID. Can be passed multiple times.",
    )
    parser.add_argument(
        "--open-access-id",
        action="append",
        default=[],
        help="Open access identifier. Can be passed multiple times.",
    )
    parser.add_argument(
        "--job-timeout",
        type=float,
        default=180.0,
        help="Max seconds to wait for job to reach terminal state (default: 180)",
    )
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="find_similar", api_url=args.api_url)

    job_id: str | None = None

    async with client:

        async def test_list_jobs() -> dict[str, Any]:
            result = await client.find_similar.list_jobs(page=0, page_size=10)
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
            expected_message="Successfully listed find-similar jobs",
        )

        async def test_create_job() -> dict[str, Any]:
            nonlocal job_id

            identifiers = build_source_identifiers(args)
            job = await client.find_similar.create_job(source_identifiers=identifiers)
            job_id = job.job_id
            if not job_id:
                raise AssertionError("Find-similar job ID is missing.")

            return {
                "job_id": job_id,
                "status": job.status,
                "source_identifiers": [identifier.to_dict() for identifier in identifiers],
            }

        await runner.run_test(
            name="create_job",
            test_fn=test_create_job,
            expected_message="Find-similar job created",
        )

        if job_id:

            async def test_get_job() -> dict[str, Any]:
                current_job_id = job_id
                if current_job_id is None:
                    raise AssertionError("Find-similar job was not created")

                job = await client.find_similar.get_job(current_job_id)
                return {
                    "job_id": job.job_id,
                    "status": job.status,
                    "has_sources": job.sources is not None,
                }

            await runner.run_test(
                name="get_job",
                test_fn=test_get_job,
                expected_message=f"Successfully retrieved find-similar job {job_id}",
            )

            async def test_wait_and_results() -> dict[str, Any]:
                current_job_id = job_id
                if current_job_id is None:
                    raise AssertionError("Find-similar job was not created")

                status, waited = await wait_until_job_terminal(
                    client.find_similar,
                    current_job_id,
                    timeout_seconds=args.job_timeout,
                )
                if not status:
                    raise AssertionError(f"Find-similar job timed out after {waited:.1f}s")

                job = await client.find_similar.get_job(current_job_id)
                statistics = job.statistics
                return {
                    "job_id": current_job_id,
                    "status": status,
                    "waited_seconds": round(waited, 1),
                    "sources_queried": getattr(statistics, "sources_queried", None),
                    "local_file_matches": getattr(statistics, "total_file_matches", None),
                    "metadata_only_matches": getattr(statistics, "total_metadata_only_matches", None),
                    "result_count": len(job.result or []),
                }

            await runner.run_test(
                name="wait_and_results",
                test_fn=test_wait_and_results,
                expected_message="Find-similar job reached terminal status",
            )
        else:
            runner.skip_test("get_job", "Find-similar job was not created")
            runner.skip_test("wait_and_results", "Find-similar job was not created")

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
