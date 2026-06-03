"""Biolevate SDK - High-level Python SDK for the Biolevate API."""

from biolevate.client import BiolevateClient
from biolevate.exceptions import (
    APIError,
    AuthenticationError,
    BiolevateError,
    NotFoundError,
)
from biolevate.models import (
    AgentCompletionConfig,
    AgentJobInputs,
    AgentJobOutputs,
    AgentMessage,
    Annotation,
    Collection,
    CollectionPage,
    EntityCellResult,
    EntityColumnInput,
    EntityExtractionResult,
    EntityRowResult,
    EntitySchemaInput,
    ExtractionJobInputs,
    ExtractionJobOutputs,
    ExtractionResult,
    File,
    FileMatch,
    FilePage,
    FindSimilarJob,
    FindSimilarJobPage,
    Job,
    JobPage,
    JobStatistics,
    KnowledgeSource,
    ListItemsResponse,
    MDEJobInputs,
    MDEJobOutputs,
    MetadataOnlyMatch,
    MetaInput,
    Ontology,
    Provider,
    ProviderItem,
    ProviderPage,
    QAJobInputs,
    QAJobOutputs,
    QAResult,
    QuestionInput,
    SearchSources,
    SourceIdentifiers,
    SourceMatches,
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
    "ProviderPage",
    "ProviderItem",
    "ListItemsResponse",
    # Files
    "File",
    "FilePage",
    # Collections
    "Collection",
    "CollectionPage",
    # Jobs
    "Job",
    "JobPage",
    # Extraction
    "MetaInput",
    "ExtractionResult",
    "ExtractionJobInputs",
    "ExtractionJobOutputs",
    # Multi-dimensional extraction
    "EntitySchemaInput",
    "EntityColumnInput",
    "EntityExtractionResult",
    "EntityRowResult",
    "EntityCellResult",
    "MDEJobInputs",
    "MDEJobOutputs",
    # Find similar
    "SourceIdentifiers",
    "SearchSources",
    "FindSimilarJob",
    "FindSimilarJobPage",
    "SourceMatches",
    "FileMatch",
    "MetadataOnlyMatch",
    "JobStatistics",
    # QA
    "QuestionInput",
    "QAResult",
    "QAJobInputs",
    "QAJobOutputs",
    # Agent
    "AgentMessage",
    "AgentCompletionConfig",
    "AgentJobInputs",
    "AgentJobOutputs",
    # Shared
    "Annotation",
    "Ontology",
    "KnowledgeSource",
]
__version__ = "0.6.1"  # x-release-please-version
