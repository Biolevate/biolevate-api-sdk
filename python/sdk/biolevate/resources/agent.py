"""Agent resource for conversational agent jobs."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate.models import (
        AgentJobInputs,
        AgentJobOutputs,
        AgentMessage,
        Annotation,
        Job,
        JobPage,
    )
    from biolevate_client import ApiClient
    from biolevate_client.models import AgentCompletionConfig, JobLaunchConfig


class AgentResource:
    """Resource for managing conversational agent jobs.

    Provides methods to create and manage agent jobs that reason over
    indexed files and conversation history, optionally returning a
    structured answer constrained by a JSON Schema.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the agent resource.

        Args:
            client: The API client.
        """
        self._client = client

    @staticmethod
    def _parse_conversation_id(conversation_id: str | None) -> UUID | None:
        """Parse a conversation id into a UUID.

        Args:
            conversation_id: The conversation id as a string, or None.

        Returns:
            The parsed UUID, or None if no id was provided.

        Raises:
            ValueError: If ``conversation_id`` is not a valid UUID string.
        """
        if conversation_id is None:
            return None
        try:
            return UUID(conversation_id)
        except ValueError as e:
            raise ValueError(f"Invalid conversation_id: {conversation_id!r} is not a valid UUID") from e

    async def list_jobs(
        self,
        page: int = 0,
        page_size: int = 20,
        conversation_id: str | None = None,
    ) -> JobPage:
        """List agent jobs with pagination.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            conversation_id: Restrict results to a single conversation.

        Returns:
            Paginated list of agent jobs.

        Raises:
            ValueError: If ``conversation_id`` is not a valid UUID string.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.agent_api import AgentApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = AgentApi(self._client)
        conversation_uuid = self._parse_conversation_id(conversation_id)

        try:
            return await api.list_agent_jobs(
                page=page,
                page_size=page_size,
                conversation_id=conversation_uuid,
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def create_job(
        self,
        message: str | None = None,
        messages: list[AgentMessage] | None = None,
        file_ids: list[str] | None = None,
        collection_ids: list[str] | None = None,
        output_model_schema: dict[str, Any] | None = None,
        completion_config: AgentCompletionConfig | None = None,
        max_iterations: int | None = None,
        conversation_id: str | None = None,
        idempotency_key: str | None = None,
        config: JobLaunchConfig | None = None,
    ) -> Job:
        """Create a new agent job.

        Provide either ``message`` (stateful turn, optionally continuing an
        existing ``conversation_id``) or ``messages`` (stateless list of
        role/content items). The two are mutually exclusive.

        Args:
            message: New user message for a stateful turn.
            messages: Full list of role/content items for a stateless run.
            file_ids: File IDs the agent can read from.
            collection_ids: Collection IDs the agent can read from.
            output_model_schema: Optional JSON Schema constraining the final
                answer to a structured object.
            completion_config: Per-completion LLM knobs (model preset,
                temperature, max tokens).
            max_iterations: Hard cap on the number of agent-loop iterations.
            conversation_id: Continue an existing server-side conversation
                (stateful only). Omit to start a new conversation.
            idempotency_key: Optional idempotency key for safe retries.
            config: Optional job launch behaviour. Set
                ``JobLaunchConfig(skip_unindexed_files=True)`` to exclude
                unindexed input files instead of rejecting the request.

        Returns:
            The created job.

        Raises:
            ValueError: If both ``message`` and ``messages`` are provided, or
                if ``conversation_id`` is not a valid UUID string.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.agent_api import AgentApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )
        from biolevate_client.models import CreateAgentRequest, FilesInput

        if message is not None and messages is not None:
            raise ValueError("Provide either 'message' or 'messages', not both.")

        api = AgentApi(self._client)
        conversation_uuid = self._parse_conversation_id(conversation_id)

        files = None
        if file_ids is not None or collection_ids is not None:
            files = FilesInput(fileIds=file_ids, collectionIds=collection_ids)

        request = CreateAgentRequest(
            message=message,
            messages=messages,
            files=files,
            output_model_schema=output_model_schema,
            completion_config=completion_config,
            max_iterations=max_iterations,
            conversation_id=conversation_uuid,
            config=config,
        )

        try:
            return await api.create_agent_job(
                create_agent_request=request,
                idempotency_key=idempotency_key,
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job(self, job_id: str) -> Job:
        """Get an agent job by ID.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job details.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.agent_api import AgentApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = AgentApi(self._client)

        try:
            return await api.get_agent_job(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_inputs(self, job_id: str) -> AgentJobInputs:
        """Get the inputs for an agent job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job inputs.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.agent_api import AgentApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = AgentApi(self._client)

        try:
            return await api.get_agent_job_inputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_outputs(self, job_id: str) -> AgentJobOutputs:
        """Get the outputs for an agent job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job outputs, including the agent's answer and references.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.agent_api import AgentApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = AgentApi(self._client)

        try:
            return await api.get_agent_job_outputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_annotations(self, job_id: str) -> list[Annotation]:
        """Get the annotations for an agent job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            List of annotations linking the answer to source passages.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.agent_api import AgentApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = AgentApi(self._client)

        try:
            return await api.get_agent_job_annotations(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
