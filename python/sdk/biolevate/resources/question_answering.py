"""Question answering resource for QA jobs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate.models import (
        Annotation,
        Job,
        JobPage,
        QAJobInputs,
        QAJobOutputs,
    )
    from biolevate_client import ApiClient
    from biolevate_client.models import EliseQuestionInput


class QuestionAnsweringResource:
    """Resource for managing question answering jobs.

    Provides methods to create and manage QA jobs that
    answer questions based on indexed files.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the question answering resource.

        Args:
            client: The API client.
        """
        self._client = client

    async def list_jobs(
        self,
        page: int = 0,
        page_size: int = 20,
        sort_by: str | None = None,
        sort_order: str = "asc",
    ) -> JobPage:
        """List QA jobs with pagination.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_by: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of QA jobs.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering_api import QuestionAnsweringApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = QuestionAnsweringApi(self._client)

        try:
            return await api.list_qa_jobs(
                page=page,
                page_size=page_size,
                sort_property=sort_by,
                sort_order=sort_order,
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def create_job(
        self,
        questions: list[EliseQuestionInput],
        file_ids: list[str] | None = None,
        collection_ids: list[str] | None = None,
    ) -> Job:
        """Create a new QA job.

        Args:
            questions: List of questions to answer. Each QuestionInput has:
                - question: The question text (required)
                - id: Optional question ID
                - answer_type: Expected answer type (ExpectedAnswerTypeDto with
                  dataType like STRING, INT, FLOAT, BOOL, DATE, ENUM)
                - guidelines: Optional guidelines for answering
                - expected_answer: Optional expected answer for validation
                - input_question_ids: Optional list of dependent question IDs
            file_ids: List of file IDs to search for answers.
            collection_ids: List of collection IDs to search for answers.

        Returns:
            The created job.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering_api import QuestionAnsweringApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )
        from biolevate_client.models import CreateQARequest, FilesInput

        api = QuestionAnsweringApi(self._client)

        try:
            return await api.create_qa_job(
                create_qa_request=CreateQARequest(
                    files=FilesInput(
                        fileIds=file_ids,
                        collectionIds=collection_ids,
                    ),
                    questions=questions,
                )
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job(self, job_id: str) -> Job:
        """Get a QA job by ID.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job details.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering_api import QuestionAnsweringApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = QuestionAnsweringApi(self._client)

        try:
            return await api.get_qa_job(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_inputs(self, job_id: str) -> QAJobInputs:
        """Get the inputs for a QA job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job inputs.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering_api import QuestionAnsweringApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = QuestionAnsweringApi(self._client)

        try:
            return await api.get_qa_job_inputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_outputs(self, job_id: str) -> QAJobOutputs:
        """Get the outputs for a QA job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job outputs.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering_api import QuestionAnsweringApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = QuestionAnsweringApi(self._client)

        try:
            return await api.get_qa_job_outputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_annotations(self, job_id: str) -> list[Annotation]:
        """Get the annotations for a QA job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            List of annotations.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.question_answering_api import QuestionAnsweringApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = QuestionAnsweringApi(self._client)

        try:
            return await api.get_qa_job_annotations(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
