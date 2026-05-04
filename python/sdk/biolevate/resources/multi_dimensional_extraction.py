"""Multi-dimensional extraction resource for entity extraction jobs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate.models import (
        Annotation,
        EntitySchemaInput,
        Job,
        JobPage,
        MDEJobInputs,
        MDEJobOutputs,
    )
    from biolevate_client import ApiClient


class MultiDimensionalExtractionResource:
    """Resource for managing multi-dimensional extraction jobs.

    Multi-dimensional extraction uses a structured entity schema to extract rows
    and columns from indexed files.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the multi-dimensional extraction resource.

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
        """List multi-dimensional extraction jobs with pagination.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_by: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of jobs.

        Raises:
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.multi_dimensional_extraction_api import MultiDimensionalExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = MultiDimensionalExtractionApi(self._client)

        try:
            return await api.list_mde_jobs(
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
        schema: EntitySchemaInput,
        file_ids: list[str] | None = None,
        collection_ids: list[str] | None = None,
    ) -> Job:
        """Create a new multi-dimensional extraction job.

        Args:
            schema: Entity schema describing the columns to extract.
            file_ids: List of file IDs to extract from.
            collection_ids: List of collection IDs to extract from.

        Returns:
            The created job.

        Raises:
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.multi_dimensional_extraction_api import MultiDimensionalExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )
        from biolevate_client.models import CreateMDERequest, FilesInput

        api = MultiDimensionalExtractionApi(self._client)

        try:
            return await api.create_mde_job(
                create_mde_request=CreateMDERequest(
                    files=FilesInput(
                        fileIds=file_ids,
                        collectionIds=collection_ids,
                    ),
                    schema=schema,
                )
            )
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job(self, job_id: str) -> Job:
        """Get a multi-dimensional extraction job by ID.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job details.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.multi_dimensional_extraction_api import MultiDimensionalExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = MultiDimensionalExtractionApi(self._client)

        try:
            return await api.get_mde_job(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_inputs(self, job_id: str) -> MDEJobInputs:
        """Get the inputs for a multi-dimensional extraction job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job inputs.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.multi_dimensional_extraction_api import MultiDimensionalExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = MultiDimensionalExtractionApi(self._client)

        try:
            return await api.get_mde_job_inputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_outputs(self, job_id: str) -> MDEJobOutputs:
        """Get the outputs for a multi-dimensional extraction job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job outputs.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.multi_dimensional_extraction_api import MultiDimensionalExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = MultiDimensionalExtractionApi(self._client)

        try:
            return await api.get_mde_job_outputs(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job_annotations(self, job_id: str) -> list[Annotation]:
        """Get the annotations for a multi-dimensional extraction job.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            List of annotations.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.multi_dimensional_extraction_api import MultiDimensionalExtractionApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = MultiDimensionalExtractionApi(self._client)

        try:
            return await api.get_mde_job_annotations(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
