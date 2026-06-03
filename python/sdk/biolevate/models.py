"""Re-exported models with cleaner names for SDK users.

This module provides simplified aliases for the generated client models,
making the SDK more user-friendly while decoupling from internal naming.
"""

from biolevate_client.models import (
    AgentCompletionConfig,
    AgentJobInputs,
    AgentJobOutputs,
    FileMatch,
    Job,
    JobStatistics,
    KnowledgeSource,
    ListItemsResponse,
    MDEJobInputs,
    MDEJobOutputs,
    MetadataOnlyMatch,
    ProviderItem,
    QAJobInputs,
    QAJobOutputs,
    SearchSources,
    SourceIdentifiers,
    SourceMatches,
)
from biolevate_client.models import (
    AgentInput as AgentMessage,
)
from biolevate_client.models import (
    EliseAnnotation as Annotation,
)
from biolevate_client.models import (
    EliseCollectionInfo as Collection,
)
from biolevate_client.models import (
    EliseEntityCellResult as EntityCellResult,
)
from biolevate_client.models import (
    EliseEntityColumnInput as EntityColumnInput,
)
from biolevate_client.models import (
    EliseEntityExtractionResult as EntityExtractionResult,
)
from biolevate_client.models import (
    EliseEntityRowResult as EntityRowResult,
)
from biolevate_client.models import (
    EliseEntitySchemaInput as EntitySchemaInput,
)
from biolevate_client.models import (
    EliseFileInfo as File,
)
from biolevate_client.models import (
    EliseMetaInput as MetaInput,
)
from biolevate_client.models import (
    EliseMetaResult as ExtractionResult,
)
from biolevate_client.models import (
    EliseOntology as Ontology,
)
from biolevate_client.models import (
    EliseQAResult as QAResult,
)
from biolevate_client.models import (
    EliseQuestionInput as QuestionInput,
)
from biolevate_client.models import (
    ExpectedAnswerTypeDto as AnswerType,
)
from biolevate_client.models import (
    ExtractJobInputs as ExtractionJobInputs,
)
from biolevate_client.models import (
    ExtractJobOutputs as ExtractionJobOutputs,
)
from biolevate_client.models import (
    FindSimilarApiJobDto as FindSimilarJob,
)
from biolevate_client.models import (
    FSProviderExternal as Provider,
)
from biolevate_client.models import (
    PageDataEliseCollectionInfo as CollectionPage,
)
from biolevate_client.models import (
    PageDataEliseFileInfo as FilePage,
)
from biolevate_client.models import (
    PageDataFindSimilarApiJobDto as FindSimilarJobPage,
)
from biolevate_client.models import (
    PageDataFSProviderExternal as ProviderPage,
)
from biolevate_client.models import (
    PageDataJob as JobPage,
)

__all__ = [
    "AgentCompletionConfig",
    "AgentJobInputs",
    "AgentJobOutputs",
    "AgentMessage",
    "Annotation",
    "AnswerType",
    "Collection",
    "CollectionPage",
    "EntityCellResult",
    "EntityColumnInput",
    "EntityExtractionResult",
    "EntityRowResult",
    "EntitySchemaInput",
    "ExtractionJobInputs",
    "ExtractionJobOutputs",
    "ExtractionResult",
    "File",
    "FileMatch",
    "FilePage",
    "FindSimilarJob",
    "FindSimilarJobPage",
    "Job",
    "JobPage",
    "JobStatistics",
    "KnowledgeSource",
    "ListItemsResponse",
    "MDEJobInputs",
    "MDEJobOutputs",
    "MetaInput",
    "MetadataOnlyMatch",
    "Ontology",
    "Provider",
    "ProviderItem",
    "ProviderPage",
    "QAJobInputs",
    "QAJobOutputs",
    "QAResult",
    "QuestionInput",
    "SearchSources",
    "SourceIdentifiers",
    "SourceMatches",
]
