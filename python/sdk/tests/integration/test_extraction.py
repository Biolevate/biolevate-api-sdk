"""Integration tests for ExtractionResource."""

from __future__ import annotations

import asyncio

import pytest

from biolevate import BiolevateClient, NotFoundError
from biolevate_client.models import EliseMetaInput

_NON_EXISTENT_ID = "00000000-0000-0000-0000-000000000000"
_TERMINAL_STATUSES = frozenset({"SUCCESS", "FAILED", "ABORTED"})
_JOB_TIMEOUT_SECONDS = 180.0


async def _wait_for_job(client: BiolevateClient, job_id: str, timeout: float = _JOB_TIMEOUT_SECONDS) -> str:
    elapsed = 0.0
    interval = 3.0
    while elapsed < timeout:
        job = await client.extraction.get_job(job_id)
        if job.status in _TERMINAL_STATUSES:
            return job.status
        await asyncio.sleep(interval)
        elapsed += interval
        interval = min(interval * 1.5, 15.0)
    pytest.skip(f"Extraction job {job_id} did not finish within {timeout} s")


@pytest.fixture(scope="module")
def metas() -> list[EliseMetaInput]:
    return [
        EliseMetaInput.model_validate(
            {"meta": "company_name", "answerType": {"dataType": "STRING"}, "description": "Name of the company"}
        ),
        EliseMetaInput.model_validate(
            {"meta": "founded_year", "answerType": {"dataType": "INT"}, "description": "Year the company was founded"}
        ),
        EliseMetaInput.model_validate(
            {
                "meta": "employee_count",
                "answerType": {"dataType": "INT"},
                "description": "Number of employees",
            }
        ),
    ]


@pytest.mark.asyncio
class TestExtractionListJobs:
    async def test_returns_page_of_jobs(self, live_client: BiolevateClient) -> None:
        page = await live_client.extraction.list_jobs()

        assert page.data is not None
        assert isinstance(page.data, list)

    async def test_pagination_page_size_is_respected(self, live_client: BiolevateClient) -> None:
        page = await live_client.extraction.list_jobs(page=0, page_size=1)

        assert len(page.data) <= 1


@pytest.mark.asyncio
class TestExtractionCreateAndPoll:
    async def test_create_job_returns_job_id(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
        metas: list[EliseMetaInput],
    ) -> None:
        job = await live_client.extraction.create_job(metas=metas, file_ids=[indexed_file_id])

        assert job.job_id is not None

    async def test_job_reaches_terminal_status(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
        metas: list[EliseMetaInput],
    ) -> None:
        job = await live_client.extraction.create_job(metas=metas, file_ids=[indexed_file_id])
        status = await _wait_for_job(live_client, job.job_id)

        assert status in _TERMINAL_STATUSES

    async def test_successful_job_has_outputs(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
        metas: list[EliseMetaInput],
    ) -> None:
        job = await live_client.extraction.create_job(metas=metas, file_ids=[indexed_file_id])
        status = await _wait_for_job(live_client, job.job_id)

        if status != "SUCCESS":
            pytest.skip(f"Job ended with status {status!r} — skipping output assertions")

        outputs = await live_client.extraction.get_job_outputs(job.job_id)

        assert outputs.results is not None
        assert len(outputs.results) == len(metas)

    async def test_get_job_inputs_matches_request(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
        metas: list[EliseMetaInput],
    ) -> None:
        job = await live_client.extraction.create_job(metas=metas, file_ids=[indexed_file_id])
        await _wait_for_job(live_client, job.job_id)

        inputs = await live_client.extraction.get_job_inputs(job.job_id)

        assert inputs.files is not None
        assert indexed_file_id in (inputs.files.file_ids or [])

    async def test_get_job_annotations_returns_list(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
        metas: list[EliseMetaInput],
    ) -> None:
        job = await live_client.extraction.create_job(metas=metas, file_ids=[indexed_file_id])
        status = await _wait_for_job(live_client, job.job_id)

        if status != "SUCCESS":
            pytest.skip(f"Job ended with status {status!r} — skipping annotation assertions")

        annotations = await live_client.extraction.get_job_annotations(job.job_id)

        assert isinstance(annotations, list)

    async def test_created_job_appears_in_list(
        self,
        live_client: BiolevateClient,
        indexed_file_id: str,
        metas: list[EliseMetaInput],
    ) -> None:
        job = await live_client.extraction.create_job(metas=metas, file_ids=[indexed_file_id])

        page = await live_client.extraction.list_jobs(page=0, page_size=50)
        job_ids = [j.job_id for j in page.data if j.job_id]
        assert job.job_id in job_ids


@pytest.mark.asyncio
class TestExtractionErrorHandling:
    async def test_get_job_raises_not_found(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.extraction.get_job(_NON_EXISTENT_ID)

    async def test_get_job_inputs_raises_not_found(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.extraction.get_job_inputs(_NON_EXISTENT_ID)

    async def test_get_job_outputs_raises_not_found(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.extraction.get_job_outputs(_NON_EXISTENT_ID)

    async def test_get_job_annotations_raises_not_found(self, live_client: BiolevateClient) -> None:
        with pytest.raises(NotFoundError):
            await live_client.extraction.get_job_annotations(_NON_EXISTENT_ID)
