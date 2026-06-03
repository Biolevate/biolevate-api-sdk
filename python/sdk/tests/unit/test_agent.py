"""Unit tests for AgentResource."""

import pytest
import respx
from httpx import Response

from biolevate import APIError, AuthenticationError, BiolevateClient, NotFoundError

JOB_ID = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
FILE_ID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
CONVERSATION_ID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"


@pytest.mark.asyncio
class TestAgentListJobs:
    @respx.mock
    async def test_returns_page_of_jobs(
        self,
        client: BiolevateClient,
        base_url: str,
        job_page_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(200, json=job_page_payload))

        page = await client.agent.list_jobs()

        assert page.total_elements == 1
        assert len(page.data) == 1

    @respx.mock
    async def test_sends_pagination_and_conversation_params(
        self,
        client: BiolevateClient,
        base_url: str,
        job_page_payload: dict,
    ) -> None:
        route = respx.get(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(200, json=job_page_payload))

        await client.agent.list_jobs(page=2, page_size=5, conversation_id=CONVERSATION_ID)

        url = str(route.calls.last.request.url)
        assert "page=2" in url
        assert "pageSize=5" in url
        assert f"conversationId={CONVERSATION_ID}" in url

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.agent.list_jobs()

    @respx.mock
    async def test_raises_authentication_error_on_403(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(403))

        with pytest.raises(AuthenticationError):
            await client.agent.list_jobs()


@pytest.mark.asyncio
class TestAgentCreateJob:
    @respx.mock
    async def test_creates_job_with_message(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        respx.post(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(200, json=job_payload))

        job = await client.agent.create_job(
            message="Summarize the attached report.",
            file_ids=[FILE_ID],
        )

        assert job.job_id == JOB_ID

    @respx.mock
    async def test_creates_job_with_messages(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        from biolevate import AgentMessage

        route = respx.post(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(200, json=job_payload))

        messages = [AgentMessage(role="USER", content="What are the main risks?")]
        job = await client.agent.create_job(messages=messages, collection_ids=["c0ffee00-dead-beef-cafe-123456789abc"])

        assert job.job_id == JOB_ID
        body = route.calls.last.request.content.decode()
        assert "messages" in body

    @respx.mock
    async def test_creates_job_with_output_schema(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        route = respx.post(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(200, json=job_payload))

        job = await client.agent.create_job(
            message="Give a verdict.",
            file_ids=[FILE_ID],
            output_model_schema={"type": "object", "properties": {"verdict": {"type": "string"}}},
            max_iterations=5,
        )

        assert job.job_id == JOB_ID
        body = route.calls.last.request.content.decode()
        assert "output_model_schema" in body

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.agent.create_job(message="Hi", file_ids=[FILE_ID])

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.post(f"{base_url}/api/core/agent/jobs").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.agent.create_job(message="Hi", file_ids=[FILE_ID])

        assert exc_info.value.status_code == 500


@pytest.mark.asyncio
class TestAgentGetJob:
    @respx.mock
    async def test_returns_job_by_id(
        self,
        client: BiolevateClient,
        base_url: str,
        job_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}").mock(return_value=Response(200, json=job_payload))

        job = await client.agent.get_job(JOB_ID)

        assert job.job_id == JOB_ID
        assert job.status == "SUCCESS"

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError, match="not found"):
            await client.agent.get_job(JOB_ID)

    @respx.mock
    async def test_raises_authentication_error_on_401(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}").mock(return_value=Response(401))

        with pytest.raises(AuthenticationError):
            await client.agent.get_job(JOB_ID)


@pytest.mark.asyncio
class TestAgentGetJobInputs:
    @respx.mock
    async def test_returns_stateless_job_inputs(
        self,
        client: BiolevateClient,
        base_url: str,
        agent_job_inputs_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/inputs").mock(
            return_value=Response(200, json=agent_job_inputs_payload)
        )

        inputs = await client.agent.get_job_inputs(JOB_ID)

        assert inputs.files is not None
        assert inputs.message is None
        assert inputs.messages is not None
        assert len(inputs.messages) == 1
        assert inputs.messages[0].content == "Summarize the attached report and list the main risks."

    @respx.mock
    async def test_returns_stateful_job_inputs(
        self,
        client: BiolevateClient,
        base_url: str,
        agent_job_inputs_stateful_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/inputs").mock(
            return_value=Response(200, json=agent_job_inputs_stateful_payload)
        )

        inputs = await client.agent.get_job_inputs(JOB_ID)

        assert inputs.message == "And what about the secondary endpoints?"
        assert inputs.messages is None
        assert inputs.conversation_id is not None

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/inputs").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.agent.get_job_inputs(JOB_ID)


@pytest.mark.asyncio
class TestAgentGetJobOutputs:
    @respx.mock
    async def test_returns_job_outputs(
        self,
        client: BiolevateClient,
        base_url: str,
        agent_job_outputs_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/results").mock(
            return_value=Response(200, json=agent_job_outputs_payload)
        )

        outputs = await client.agent.get_job_outputs(JOB_ID)

        assert outputs.answer == {"verdict": "low risk", "summary": "The report shows stable results."}
        assert outputs.reference_ids is not None
        assert len(outputs.reference_ids) == 1

    @respx.mock
    async def test_returns_string_answer(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/results").mock(
            return_value=Response(200, json={"answer": "A plain text answer.", "referenceIds": []})
        )

        outputs = await client.agent.get_job_outputs(JOB_ID)

        assert outputs.answer == "A plain text answer."

    @respx.mock
    async def test_raises_not_found_on_404(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/results").mock(
            return_value=Response(404, json={"error": "Not found"})
        )

        with pytest.raises(NotFoundError):
            await client.agent.get_job_outputs(JOB_ID)


@pytest.mark.asyncio
class TestAgentGetJobAnnotations:
    @respx.mock
    async def test_returns_list_of_annotations(
        self,
        client: BiolevateClient,
        base_url: str,
        annotation_payload: dict,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/annotations").mock(
            return_value=Response(200, json=[annotation_payload])
        )

        annotations = await client.agent.get_job_annotations(JOB_ID)

        assert isinstance(annotations, list)
        assert len(annotations) == 1
        assert annotations[0].type == "DOCUMENT_STATEMENT"

    @respx.mock
    async def test_returns_empty_list(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/annotations").mock(return_value=Response(200, json=[]))

        annotations = await client.agent.get_job_annotations(JOB_ID)

        assert annotations == []

    @respx.mock
    async def test_raises_api_error_on_500(
        self,
        client: BiolevateClient,
        base_url: str,
    ) -> None:
        respx.get(f"{base_url}/api/core/agent/jobs/{JOB_ID}/annotations").mock(return_value=Response(500))

        with pytest.raises(APIError) as exc_info:
            await client.agent.get_job_annotations(JOB_ID)

        assert exc_info.value.status_code == 500
