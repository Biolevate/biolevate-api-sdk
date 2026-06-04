#!/usr/bin/env python3
"""Integration tests for the Agent resource.

Uses a file with meaningful content from test_resources. If no file or
collection is provided, uploads a sample file, creates it, and waits for
indexation before running the agent job.
"""

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import TYPE_CHECKING, Any

from scripts.common import create_client, get_base_parser
from scripts.test_utils import TestRunner

if TYPE_CHECKING:
    from biolevate.resources.agent import AgentResource
    from biolevate.resources.files import FilesResource

TERMINAL_STATUSES = ("SUCCESS", "FAILED", "ABORTED")

DEFAULT_MESSAGE = "Summarize the attached document and list its key facts in a few bullet points."


def _default_test_resources_dir() -> Path:
    return Path(__file__).resolve().parent / "test_resources"


def _get_agent_sample(test_files_dir: Path, test_file_path: Path | None) -> Path | None:
    if test_file_path is not None:
        if test_file_path.is_file():
            return test_file_path
        return None

    for sample_name in ("agent_sample.txt", "qa_sample.txt", "extraction_sample.txt", "sample.txt"):
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
    agent_resource: AgentResource,
    job_id: str,
    timeout_seconds: float,
    initial_interval: float = 3.0,
    max_interval: float = 15.0,
) -> tuple[str, float]:
    elapsed = 0.0
    interval = initial_interval
    while elapsed < timeout_seconds:
        job = await agent_resource.get_job(job_id)
        status = getattr(job, "status", None)
        if status in TERMINAL_STATUSES:
            return status, elapsed
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 2, max_interval)
    return "", elapsed


async def main() -> None:
    parser = get_base_parser("Test Agent resource")
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
        help="Indexed EliseFile ID the agent can read. Can be passed multiple times.",
    )
    parser.add_argument(
        "--collection-id",
        action="append",
        default=[],
        help="Collection ID the agent can read. Can be passed multiple times.",
    )
    parser.add_argument(
        "--message",
        type=str,
        default=DEFAULT_MESSAGE,
        help="User message to send to the agent",
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
        help="Directory for agent sample files (default: scripts/test_resources)",
    )
    parser.add_argument(
        "--test-file",
        type=Path,
        default=None,
        help="Path to agent sample file when no file or collection is provided",
    )
    args = parser.parse_args()

    client = create_client(args)
    runner = TestRunner(resource="agent", api_url=args.api_url)

    test_files_dir = args.test_files_dir or _default_test_resources_dir()
    provider_id: str | None = None
    file_ids: list[str] = list(args.file_id)
    test_folder_name = f"SDK-TEST-AGENT-{int(time.time())}"
    uploaded_key: str | None = None
    job_id: str | None = None

    async with client:

        async def test_setup_provider_and_file() -> dict[str, Any]:
            nonlocal provider_id, uploaded_key, file_ids

            if file_ids:
                return {"file_ids": file_ids, "collection_ids": args.collection_id, "source": "cli_file_id"}

            if args.collection_id:
                return {"file_ids": file_ids, "collection_ids": args.collection_id, "source": "cli_collection_id"}

            sample_path = _get_agent_sample(test_files_dir, args.test_file)
            if not sample_path:
                raise AssertionError(
                    f"No agent sample file found in {test_files_dir}. "
                    "Provide --file-id, --collection-id, --test-file, or add agent_sample.txt."
                )

            if args.provider_id:
                provider_id = args.provider_id
            else:
                providers = await client.providers.list(page=0, page_size=1)
                if not providers.data or len(providers.data) == 0:
                    raise AssertionError("No provider available. Cannot run agent tests.")
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
            state_path = Path("test-reports/agent-test-state.json")
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
            expected_message="Provider and file ready for agent",
        )

        async def test_list_jobs() -> dict[str, Any]:
            result = await client.agent.list_jobs(page=0, page_size=10)
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
            expected_message="Successfully listed agent jobs",
        )

        if not file_ids and not args.collection_id:
            for name in (
                "create_job",
                "get_job",
                "get_job_inputs",
                "wait_and_results",
                "get_job_annotations",
            ):
                runner.skip_test(name, "No file_id or collection_id available for agent job")
        else:

            async def test_create_job() -> dict[str, Any]:
                nonlocal job_id

                job = await client.agent.create_job(
                    message=args.message,
                    file_ids=file_ids or None,
                    collection_ids=args.collection_id or None,
                    output_model_schema={
                        "type": "object",
                        "properties": {
                            "summary": {"type": "string"},
                            "key_facts": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["summary"],
                    },
                    max_iterations=10,
                )
                job_id = job.job_id
                if not job_id:
                    raise AssertionError("Agent job ID is missing.")

                return {
                    "job_id": job_id,
                    "status": job.status,
                    "file_ids": file_ids,
                    "collection_ids": args.collection_id,
                }

            await runner.run_test(
                name="create_job",
                test_fn=test_create_job,
                expected_message="Agent job created",
            )

            if job_id:
                jid: str = job_id

                async def test_get_job() -> dict[str, Any]:
                    job = await client.agent.get_job(jid)
                    return {
                        "job_id": job.job_id,
                        "status": job.status,
                        "task_type": getattr(job, "task_type", None),
                    }

                await runner.run_test(
                    name="get_job",
                    test_fn=test_get_job,
                    expected_message=f"Successfully retrieved agent job {job_id}",
                )

                async def test_get_job_inputs() -> dict[str, Any]:
                    inputs = await client.agent.get_job_inputs(jid)
                    return {
                        "has_files": inputs.files is not None,
                        "message": inputs.message,
                        "max_iterations": inputs.max_iterations,
                    }

                await runner.run_test(
                    name="get_job_inputs",
                    test_fn=test_get_job_inputs,
                    expected_message="Successfully retrieved agent inputs",
                )

                async def test_wait_and_results() -> dict[str, Any]:
                    status, waited = await wait_until_job_terminal(
                        client.agent,
                        jid,
                        timeout_seconds=args.job_timeout,
                    )
                    if not status:
                        raise AssertionError(f"Agent job timed out after {waited:.1f}s")

                    details: dict[str, Any] = {
                        "job_id": jid,
                        "status": status,
                        "waited_seconds": round(waited, 1),
                    }

                    if status == "SUCCESS":
                        outputs = await client.agent.get_job_outputs(jid)
                        details["answer"] = outputs.answer
                        details["explanation"] = (outputs.explanation or "")[:200]
                        details["reference_count"] = len(outputs.reference_ids or [])

                    return details

                await runner.run_test(
                    name="wait_and_results",
                    test_fn=test_wait_and_results,
                    expected_message="Agent job reached terminal status",
                )

                async def test_get_job_annotations() -> dict[str, Any]:
                    annotations = await client.agent.get_job_annotations(jid)
                    return {"count": len(annotations)}

                await runner.run_test(
                    name="get_job_annotations",
                    test_fn=test_get_job_annotations,
                    expected_message="Successfully retrieved agent annotations",
                )

        non_existent_id = "00000000-0000-0000-0000-000000000000"

        async def test_get_job_not_found() -> dict[str, Any]:
            from biolevate import NotFoundError

            try:
                await client.agent.get_job(non_existent_id)
                raise AssertionError("Expected NotFoundError was not raised")
            except NotFoundError:
                return {"error_type": "NotFoundError", "correctly_raised": True}

        await runner.run_test(
            name="get_job_not_found",
            test_fn=test_get_job_not_found,
            expected_message="NotFoundError raised for non-existent job",
        )

    runner.print_and_save()


if __name__ == "__main__":
    asyncio.run(main())
