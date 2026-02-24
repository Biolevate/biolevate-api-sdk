"""Re-exported models with cleaner names for SDK users.

This module provides simplified aliases for the generated client models,
making the SDK more user-friendly while decoupling from internal naming.
"""

from biolevate_client.models import (
    EliseAnnotation as Annotation,
)
from biolevate_client.models import (
    EliseCollectionInfo as Collection,
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
    FSProviderExternal as Provider,
)
from biolevate_client.models import (
    Job,
    ListItemsResponse,
    ProviderItem,
    QAJobInputs,
    QAJobOutputs,
)
from biolevate_client.models import (
    PageDataEliseCollectionInfo as CollectionPage,
)
from biolevate_client.models import (
    PageDataEliseFileInfo as FilePage,
)
from biolevate_client.models import (
    PageDataFSProviderExternal as ProviderPage,
)
from biolevate_client.models import (
    PageDataJob as JobPage,
)

__all__ = [
    "Annotation",
    "AnswerType",
    "Collection",
    "CollectionPage",
    "ExtractionJobInputs",
    "ExtractionJobOutputs",
    "ExtractionResult",
    "File",
    "FilePage",
    "Job",
    "JobPage",
    "ListItemsResponse",
    "MetaInput",
    "Ontology",
    "Provider",
    "ProviderItem",
    "ProviderPage",
    "QAJobInputs",
    "QAJobOutputs",
    "QAResult",
    "QuestionInput",
]
