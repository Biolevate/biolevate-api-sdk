"""Extraction resource for metadata extraction jobs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate_client import ApiClient
    from biolevate_client.models import EliseMetaInput
    from biolevate.models import (
        Annotation,
        ExtractionJobInputs,
        ExtractionJobOutputs,
        Job,
        JobPage,
    )


class ExtractionResource:
    """Resource for managing metadata extraction jobs.

    Provides methods to create and manage extraction jobs that
    extract structured metadata from indexed files.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the extraction resource.

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
        """List extraction jobs with pagination.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_by: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of extraction jobs.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.extraction_api import ExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = ExtractionApi(self._client)

        try:
            return await api.list_extraction_jobs(
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
        metas: "list[EliseMetaInput]",
        file_ids: list[str] | None = None,
        collection_ids: list[str] | None = None,
    ) -> Job:
        """Create a new extraction job.

        Args:
            metas: List of metadata fields to extract. Each MetaInput specifies:
                - meta: Field name (e.g. "title", "authors", "date")
                - answer_type: Expected data type (ExpectedAnswerTypeDto with
                  dataType like STRING, INT, FLOAT, BOOL, DATE, ENUM)
                - description: Description of what to extract
            file_ids: List of file IDs to extract from.
            collection_ids: List of collection IDs to extract from.

        Returns:
            The created job.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.extraction_api import ExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )
        from biolevate_client.models import CreateExtractRequest, FilesInput

        api = ExtractionApi(self._client)

        try:
            return await api.create_extraction_job(
                create_extract_request=CreateExtractRequest(
                    files=FilesInput(
                        fileIds=file_ids,
                        collectionIds=collection_ids,
                    ),
                    metas=metas,
                )
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job(self, job_id: str) -> Job:
        """Get an extraction job by ID.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job details.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.extraction_api import ExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = ExtractionApi(self._client)

        try:
            return await api.get_extraction_job(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_inputs(self, job_id: str) -> ExtractionJobInputs:
        """Get the inputs for an extraction job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job inputs.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.extraction_api import ExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = ExtractionApi(self._client)

        try:
            return await api.get_extraction_job_inputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_outputs(self, job_id: str) -> ExtractionJobOutputs:
        """Get the outputs for an extraction job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job outputs.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.extraction_api import ExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = ExtractionApi(self._client)

        try:
            return await api.get_extraction_job_outputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_annotations(self, job_id: str) -> "list[Annotation]":
        """Get the annotations for an extraction job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            List of annotations.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.extraction_api import ExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = ExtractionApi(self._client)

        try:
            return await api.get_extraction_job_annotations(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
