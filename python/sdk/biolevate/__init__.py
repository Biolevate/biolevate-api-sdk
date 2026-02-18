"""Biolevate SDK - High-level Python SDK for the Biolevate API."""

from biolevate.client import BiolevateClient
from biolevate.exceptions import (
    APIError,
    AuthenticationError,
    BiolevateError,
    NotFoundError,
)

from biolevate_client.models import (
    EliseAnnotation as Annotation,
    EliseCollectionInfo as Collection,
    EliseFileInfo as File,
    EliseMetaInput as MetaInput,
    EliseMetaResult as ExtractionResult,
    EliseOntology as Ontology,
    EliseQAResult as QAResult,
    EliseQuestionInput as QuestionInput,
    FSProviderExternal as Provider,
    FSProviderExternalType as ProviderType,
    Job,
    JobStatus,
    ListItemsResponse,
    PageDataEliseCollectionInfo as CollectionPage,
    PageDataEliseFileInfo as FilePage,
    PageDataFSProviderExternal as ProviderPage,
    PageDataJob as JobPage,
    ProviderItem,
    ProviderItemType,
)

__all__ = [
    # Client
    "BiolevateClient",
    # Exceptions
    "BiolevateError",
    "APIError",
    "AuthenticationError",
    "NotFoundError",
    # Providers
    "Provider",
    "ProviderType",
    "ProviderPage",
    "ProviderItem",
    "ProviderItemType",
    "ListItemsResponse",
    # Files
    "File",
    "FilePage",
    # Collections
    "Collection",
    "CollectionPage",
    # Jobs
    "Job",
    "JobStatus",
    "JobPage",
    # Extraction
    "MetaInput",
    "ExtractionResult",
    # QA
    "QuestionInput",
    "QAResult",
    # Shared
    "Annotation",
    "Ontology",
]
__version__ = "0.1.0"
