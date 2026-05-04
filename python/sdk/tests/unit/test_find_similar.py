"""Unit tests for FindSimilarResource."""

import json

import pytest
import respx
from httpx import Response

from biolevate import APIError, AuthenticationError, BiolevateClient, NotFoundError, SourceIdentifiers

JOB_ID = "f47ac10b-58cc-4372-a567-0e02b2c3d479"


@pytest.mark.asyncio
class TestFindSimilarListJobs:
    @respx.mock
    async def test_returns_page_of_jobs(
        self,
        client: BiolevateClient,
        base_url: str,
        find_similar_job_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/find-similar/jobs").mock(
            return_value=Response(200, json=find_similar_job_page_payload)
        )

        page = await client.find_similar.list_jobs()

        assert page.total_elements == 1
        assert len(page.data) == 1
        assert page.data[0].status == "COMPLETED"

    @respx.mock
    async def test_sends_pagination_params(
        self,
        client: BiolevateClient,
        base_url: str,
        find_similar_job_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/find-similar/jobs").mock(
            return_value=Response(200, json=find_similar_job_page_payload)
        )

        await client.find_similar.list_jobs(page=3, page_size=15)

        url = str(route.calls.last.request.url)
        assert "page=3" in url
        assert "pageSize=15" in url

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/find-similar/jobs").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.find_similar.list_jobs()


@pytest.mark.asyncio
class TestFindSimilarCreateJob:
    @respx.mock
    async def test_creates_job_from_source_identifiers(
        self,
        client: BiolevateClient,
        base_url: str,
        find_similar_job_payload: dict,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/find-similar/jobs").mock(
            return_value=Response(200, json=find_similar_job_payload)
        )

        job = await client.find_similar.create_job(source_identifiers=[SourceIdentifiers(doi="10.1000/example")])

        body = json.loads(route.calls.last.request.content)
        assert job.job_id == JOB_ID
        assert body["sourceIdentifiers"] == [{"doi": "10.1000/example"}]

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/find-similar/jobs").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.find_similar.create_job(source_identifiers=[SourceIdentifiers(doi="10.1000/example")])

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestFindSimilarGetJob:
    @respx.mock
    async def test_returns_job_by_id(
        self,
        client: BiolevateClient,
        base_url: str,
        find_similar_job_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/find-similar/jobs/{JOB_ID}").mock(
            return_value=Response(200, json=find_similar_job_payload)
        )

        job = await client.find_similar.get_job(JOB_ID)

        assert job.job_id == JOB_ID
        assert job.sources.source_identifiers[0].doi == "10.1000/example"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/find-similar/jobs/{JOB_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.find_similar.get_job(JOB_ID)
