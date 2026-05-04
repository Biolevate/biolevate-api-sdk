"""Find-similar resource for bibliographic and local file matching jobs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from biolevate.exceptions import APIError, AuthenticationError, NotFoundError

if TYPE_CHECKING:
    from biolevate.models import FindSimilarJob, FindSimilarJobPage, SearchSources, SourceIdentifiers
    from biolevate_client import ApiClient


class FindSimilarResource:
    """Resource for managing find-similar jobs.

    Find-similar jobs match source identifiers against local files and remote
    bibliographic search results.
    """

    def __init__(self, client: ApiClient) -> None:
        """Initialize the find-similar resource.

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
    ) -> FindSimilarJobPage:
        """List find-similar jobs with pagination.

        Args:
            page: Page number (0-based).
            page_size: Number of items per page.
            sort_by: Field to sort by.
            sort_order: Sort direction ('asc' or 'desc').

        Returns:
            Paginated list of find-similar jobs.

        Raises:
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.find_similar_files_api import FindSimilarFilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )

        api = FindSimilarFilesApi(self._client)

        try:
            return await api.list_jobs(
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
        source_identifiers: list[SourceIdentifiers] | None = None,
        search_sources: SearchSources | None = None,
    ) -> FindSimilarJob:
        """Create a new find-similar job.

        Args:
            source_identifiers: Source identifiers to match. Each item can
                include a DOI, an internal ID, or an open access ID.
            search_sources: Pre-built SearchSources request. If provided, it is
                used instead of source_identifiers.

        Returns:
            The created find-similar job.

        Raises:
            AuthenticationError: If authentication fails.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.find_similar_files_api import FindSimilarFilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            UnauthorizedException,
        )
        from biolevate_client.models import SearchSources

        api = FindSimilarFilesApi(self._client)
        request = search_sources or SearchSources(sourceIdentifiers=source_identifiers)

        try:
            return await api.create_job(search_sources=request)
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e

    async def get_job(self, job_id: str) -> FindSimilarJob:
        """Get a find-similar job by ID.

        Args:
            job_id: The unique identifier of the job.

        Returns:
            The job details, including results and statistics when completed.

        Raises:
            NotFoundError: If the job is not found.
            AuthenticationError: If authentication fails or access is denied.
            APIError: If the API returns an unexpected error.
        """
        from biolevate_client.api.find_similar_files_api import FindSimilarFilesApi
        from biolevate_client.exceptions import (
            ApiException,
            ForbiddenException,
            NotFoundException,
            UnauthorizedException,
        )

        api = FindSimilarFilesApi(self._client)

        try:
            return await api.get_job(job_id=job_id)
        except NotFoundException as e:
            raise NotFoundError(f"Job '{job_id}' not found") from e
        except UnauthorizedException as e:
            raise AuthenticationError("Authentication failed") from e
        except ForbiddenException as e:
            raise AuthenticationError("Access denied") from e
        except ApiException as e:
            raise APIError(e.status or 500, str(e.reason)) from e
