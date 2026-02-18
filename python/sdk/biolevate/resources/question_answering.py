"""Question answering resource for managing QA jobs."""

from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate_client import AuthenticatedClient
    from biolevate_client.models import (
        EliseAnnotation,
        EliseQuestionInput,
        Job,
        PageDataJob,
        QAJobInputs,
        QAJobOutputs,
    )


class QuestionAnsweringResource:
    """Resource for managing question answering jobs.

    Provides methods to create QA jobs and retrieve their results.
    """

    def __init__(self, client: AuthenticatedClient) -> None:
        """Initialize the question answering resource.

        Args:
            client: The authenticated API client.
        """
        self._client = client

    async def create(
        self,
        questions: list[EliseQuestionInput],
        file_ids: list[str] | None = None,
        collection_ids: list[str] | None = None,
    ) -> Job:
        """Create a question answering job.

        Args:
            questions: List of questions to ask.
            file_ids: List of file UUIDs to process.
            collection_ids: List of collection UUIDs to process.

        Returns:
            The created job.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering import create_qa_job
        from biolevate_client.models import CreateQARequest, FilesInput
        from biolevate_client.types import UNSET

        files_input = FilesInput(
            file_ids=file_ids if file_ids else UNSET,
            collection_ids=collection_ids if collection_ids else UNSET,
        )

        request = CreateQARequest(
            files=files_input,
            questions=questions,
        )

        response = await create_qa_job.asyncio_detailed(
            client=self._client,
            body=request,
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied")

        if response.status_code == HTTPStatus.BAD_REQUEST:
            raise APIError(response.status_code.value, "Invalid request")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to create QA job")

        return response.parsed

    async def list(
        self,
        page: int = 0,
        page_size: int = 20,
        sort_property: str | None = None,
        sort_order: str | None = None,
    ) -> PageDataJob:
        """List QA jobs for the current user.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_property: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of jobs.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering import list_qa_jobs
        from biolevate_client.types import UNSET

        response = await list_qa_jobs.asyncio_detailed(
            client=self._client,
            page=page,
            page_size=page_size,
            sort_property=sort_property if sort_property is not None else UNSET,
            sort_order=sort_order if sort_order is not None else UNSET,
        )

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to list QA jobs")

        return response.parsed

    async def get(self, job_id: str) -> Job:
        """Get a QA job by ID.

        Args:
            job_id: The job UUID.

        Returns:
            The job details.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering import get_qa_job

        response = await get_qa_job.asyncio_detailed(
            job_id=job_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"QA job not found: {job_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to job")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get QA job")

        return response.parsed

    async def get_inputs(self, job_id: str) -> QAJobInputs:
        """Get the inputs used for a QA job.

        Args:
            job_id: The job UUID.

        Returns:
            The job inputs (files and questions).

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering import get_qa_job_inputs

        response = await get_qa_job_inputs.asyncio_detailed(
            job_id=job_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"QA job not found: {job_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to job")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get QA job inputs")

        return response.parsed

    async def get_outputs(self, job_id: str) -> QAJobOutputs:
        """Get the answers from a QA job.

        Args:
            job_id: The job UUID.

        Returns:
            The QA results.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering import get_qa_job_outputs

        response = await get_qa_job_outputs.asyncio_detailed(
            job_id=job_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"QA job not found: {job_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to job")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get QA job outputs")

        return response.parsed

    async def get_annotations(self, job_id: str) -> "list[EliseAnnotation]": # type: ignore[valid-type]
        """Get document annotations from a QA job.

        Args:
            job_id: The job UUID.

        Returns:
            List of annotations generated by the job.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering import get_qa_job_annotations

        response = await get_qa_job_annotations.asyncio_detailed(
            job_id=job_id,
            client=self._client,
        )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise NotFoundError(f"QA job not found: {job_id}")

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthenticationError("Authentication failed")

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise AuthenticationError("Access denied to job")

        if response.parsed is None:
            raise APIError(response.status_code.value, "Failed to get QA job annotations")

        return response.parsed  # type: ignore[return-value]
