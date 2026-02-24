"""Unit tests for ExtractionResource."""

import pytest
import respx
from httpx import Response

from biolevate import APIError, AuthenticationError, BiolevateClient, NotFoundError

JOB_ID = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
FILE_ID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"


def _meta_input() -> dict:
    return {"meta": "title", "answerType": {"dataType": "STRING"}, "description": "Document title"}


@pytest.mark.asyncio
class TestExtractionListJobs:
    @respx.mock
    async def test_returns_page_of_jobs(
        self,
        client: BiolevateClient,
        base_url: str,
        job_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs").mock(return_value=Response(200, json=job_page_payload))

        page = await client.extraction.list_jobs()

        assert page.total_elements == 1
        assert len(page.data) == 1

    @respx.mock
    async def test_sends_pagination_params(
        self,
        client: BiolevateClient,
        base_url: str,
        job_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/extraction/jobs").mock(
            return_value=Response(200, json=job_page_payload)
        )

        await client.extraction.list_jobs(page=1, page_size=25)

        url = str(route.calls.last.request.url)
        assert "page=1" in url
        assert "pageSize=25" in url

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.extraction.list_jobs()

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.extraction.list_jobs()


@pytest.mark.asyncio
class TestExtractionCreateJob:
    @respx.mock
    async def test_creates_job_with_file_ids(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        from biolevate_client.models import EliseMetaInput

        respx.post(f"{base_url}/api/core/extraction/jobs").mock(return_value=Response(200, json=job_payload))

        meta = EliseMetaInput.model_validate(_meta_input())
        job = await client.extraction.create_job(metas=[meta], file_ids=[FILE_ID])

        assert job.job_id == JOB_ID

    @respx.mock
    async def test_creates_job_with_collection_ids(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        from biolevate_client.models import EliseMetaInput

        respx.post(f"{base_url}/api/core/extraction/jobs").mock(return_value=Response(200, json=job_payload))

        meta = EliseMetaInput.model_validate(_meta_input())
        job = await client.extraction.create_job(metas=[meta], collection_ids=["c0ffee00-dead-beef-cafe-123456789abc"])

        assert job.job_id == JOB_ID

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        from biolevate_client.models import EliseMetaInput

        respx.post(f"{base_url}/api/core/extraction/jobs").mock(return_value=Response(401))

        meta = EliseMetaInput.model_validate(_meta_input())
        with pytest.raises(AuthenticationError):
            await client.extraction.create_job(metas=[meta], file_ids=[FILE_ID])

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        from biolevate_client.models import EliseMetaInput

        respx.post(f"{base_url}/api/core/extraction/jobs").mock(return_value=Response(500))

        meta = EliseMetaInput.model_validate(_meta_input())
        with pytest.raises(APIError) as exc_info:
            await client.extraction.create_job(metas=[meta], file_ids=[FILE_ID])

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestExtractionGetJob:
    @respx.mock
    async def test_returns_job_by_id(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}").mock(return_value=Response(200, json=job_payload))

        job = await client.extraction.get_job(JOB_ID)

        assert job.job_id == JOB_ID
        assert job.status == "SUCCESS"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError, match="not found"):
            await client.extraction.get_job(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job(JOB_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.extraction.get_job(JOB_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestExtractionGetJobInputs:
    @respx.mock
    async def test_returns_job_inputs(
        self,
        client: BiolevateClient,
        base_url: str,
        extraction_job_inputs_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/inputs").mock(
            return_value=Response(200, json=extraction_job_inputs_payload)
        )

        inputs = await client.extraction.get_job_inputs(JOB_ID)

        assert inputs.files is not None
        assert len(inputs.metas) == 1

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/inputs").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.extraction.get_job_inputs(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/inputs").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job_inputs(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/inputs").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job_inputs(JOB_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/inputs").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.extraction.get_job_inputs(JOB_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestExtractionGetJobOutputs:
    @respx.mock
    async def test_returns_job_outputs(
        self,
        client: BiolevateClient,
        base_url: str,
        extraction_job_outputs_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/results").mock(
            return_value=Response(200, json=extraction_job_outputs_payload)
        )

        outputs = await client.extraction.get_job_outputs(JOB_ID)

        assert len(outputs.results) == 1
        assert outputs.results[0].meta == "title"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/results").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.extraction.get_job_outputs(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/results").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job_outputs(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/results").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job_outputs(JOB_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/results").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.extraction.get_job_outputs(JOB_ID)

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestExtractionGetJobAnnotations:
    @respx.mock
    async def test_returns_list_of_annotations(
        self,
        client: BiolevateClient,
        base_url: str,
        annotation_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/annotations").mock(
            return_value=Response(200, json=[annotation_payload])
        )

        annotations = await client.extraction.get_job_annotations(JOB_ID)

        assert isinstance(annotations, list)
        assert len(annotations) == 1
        assert annotations[0].type == "DOCUMENT_STATEMENT"

    @respx.mock
    async def test_returns_empty_list(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/annotations").mock(return_value=Response(200, json=[]))

        annotations = await client.extraction.get_job_annotations(JOB_ID)

        assert annotations == []

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/annotations").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.extraction.get_job_annotations(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/annotations").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job_annotations(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/annotations").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.extraction.get_job_annotations(JOB_ID)

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/extraction/jobs/{JOB_ID}/annotations").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.extraction.get_job_annotations(JOB_ID)

        assert exc_info.value.status_code == 500
