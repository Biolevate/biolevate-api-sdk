"""Unit tests for MultiDimensionalExtractionResource."""

import json

import pytest  # type: ignore[reportMissingImports]
import respx  # type: ignore[reportMissingImports]
from httpx import Response  # type: ignore[reportMissingImports]

from biolevate import APIError, AuthenticationError, BiolevateClient, EntitySchemaInput, NotFoundError

JOB_ID = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
FILE_ID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"


def _schema_input() -> EntitySchemaInput:
    return EntitySchemaInput.model_validate(
        {
            "name": "compounds",
            "columns": [
                {
                    "key": "compound",
                    "label": "Compound",
                    "type": "ENTITY_COLUMN_TYPE_STRING",
                    "role": "ENTITY_COLUMN_ROLE_IDENTIFIER",
                }
            ],
        }
    )


@pytest.mark.asyncio
class TestMultiDimensionalExtractionListJobs:
    @respx.mock
    async def test_returns_page_of_jobs(
        self,
        client: BiolevateClient,
        base_url: str,
        job_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(
            return_value=Response(200, json=job_page_payload)
        )

        page = await client.mde.list_jobs()

        assert page.total_elements == 1
        assert page.data is not None
        assert len(page.data) == 1

    @respx.mock
    async def test_sends_pagination_params(
        self,
        client: BiolevateClient,
        base_url: str,
        job_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(
            return_value=Response(200, json=job_page_payload)
        )

        await client.mde.list_jobs(page=2, page_size=10)

        url = str(route.calls.last.request.url)
        assert "page=2" in url
        assert "pageSize=10" in url

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.mde.list_jobs()


@pytest.mark.asyncio
class TestMultiDimensionalExtractionCreateJob:
    @respx.mock
    async def test_creates_job_with_schema_and_file_ids(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(
            return_value=Response(200, json=job_payload)
        )

        job = await client.mde.create_job(schema=_schema_input(), file_ids=[FILE_ID])

        body = json.loads(route.calls.last.request.content)
        assert job.job_id == JOB_ID
        assert body["files"]["fileIds"] == [FILE_ID]
        assert body["schema"]["name"] == "compounds"

    @respx.mock
    async def test_sends_prompt_with_fixed_schema(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(
            return_value=Response(200, json=job_payload)
        )
        schema = _schema_input()

        await client.mde.create_job(
            schema=schema,
            file_ids=[FILE_ID],
            prompt="Extract one row per study arm.",
        )

        body = json.loads(route.calls.last.request.content)
        assert body["prompt"] == "Extract one row per study arm."
        assert body["schema"]["name"] == "compounds"
        assert schema.description is None

    @respx.mock
    async def test_creates_prompt_only_job(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(
            return_value=Response(200, json=job_payload)
        )

        await client.mde.create_job(
            file_ids=[FILE_ID],
            prompt="Infer a table of study arms and reported outcomes.",
        )

        body = json.loads(route.calls.last.request.content)
        assert body["prompt"] == "Infer a table of study arms and reported outcomes."
        assert "schema" not in body

    async def test_requires_prompt_or_schema(
        self,
        client: BiolevateClient,
    ) -> None:
        with pytest.raises(ValueError, match="prompt or schema is required"):
            await client.mde.create_job(file_ids=[FILE_ID])

    async def test_rejects_blank_prompt_without_schema(
        self,
        client: BiolevateClient,
    ) -> None:
        with pytest.raises(ValueError, match="prompt or schema is required"):
            await client.mde.create_job(file_ids=[FILE_ID], prompt="   ")

    @respx.mock
    async def test_ignores_blank_prompt_when_schema_exists(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(
            return_value=Response(200, json=job_payload)
        )

        await client.mde.create_job(
            schema=_schema_input(),
            file_ids=[FILE_ID],
            prompt="   ",
        )

        body = json.loads(route.calls.last.request.content)
        assert "prompt" not in body

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/multi-dim-extraction/jobs").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.mde.create_job(schema=_schema_input(), file_ids=[FILE_ID])

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestMultiDimensionalExtractionGetters:
    @respx.mock
    async def test_returns_job_by_id(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs/{JOB_ID}").mock(
            return_value=Response(200, json=job_payload)
        )

        job = await client.mde.get_job(JOB_ID)

        assert job.job_id == JOB_ID

    @respx.mock
    async def test_returns_job_inputs(
        self,
        client: BiolevateClient,
        base_url: str,
        mde_job_inputs_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs/{JOB_ID}/inputs").mock(
            return_value=Response(200, json=mde_job_inputs_payload)
        )

        inputs = await client.mde.get_job_inputs(JOB_ID)

        assert inputs.var_schema is not None
        assert inputs.var_schema.name == "compounds"
        assert inputs.prompt == "Extract one row per compound."

    @respx.mock
    async def test_returns_job_outputs(
        self,
        client: BiolevateClient,
        base_url: str,
        mde_job_outputs_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs/{JOB_ID}/results").mock(
            return_value=Response(200, json=mde_job_outputs_payload)
        )

        outputs = await client.mde.get_job_outputs(JOB_ID)

        assert outputs.entity_extraction is not None
        assert outputs.entity_extraction.rows is not None
        assert outputs.entity_extraction.rows[0].cells is not None
        assert outputs.entity_extraction.rows[0].cells[0].column_key == "compound"

    @respx.mock
    async def test_returns_job_annotations(
        self,
        client: BiolevateClient,
        base_url: str,
        annotation_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs/{JOB_ID}/annotations").mock(
            return_value=Response(200, json=[annotation_payload])
        )

        annotations = await client.mde.get_job_annotations(JOB_ID)

        assert len(annotations) == 1

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/multi-dim-extraction/jobs/{JOB_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.mde.get_job(JOB_ID)
