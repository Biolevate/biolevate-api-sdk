"""Re-exported models with cleaner names for SDK users.

This module provides simplified aliases for the generated client models,
making the SDK more user-friendly while decoupling from internal naming.
"""

from biolevate_client.models import (
    EliseAnnotation as Annotation,
    EliseCollectionInfo as Collection,
    EliseFileInfo as File,
    EliseMetaInput as MetaInput,
    EliseMetaResult as ExtractionResult,
    EliseOntology as Ontology,
    EliseQAResult as QAResult,
    EliseQuestionInput as QuestionInput,
    ExpectedAnswerTypeDto as AnswerType,
    ExtractJobInputs as ExtractionJobInputs,
    ExtractJobOutputs as ExtractionJobOutputs,
    FSProviderExternal as Provider,
    Job,
    ListItemsResponse,
    PageDataEliseCollectionInfo as CollectionPage,
    PageDataEliseFileInfo as FilePage,
    PageDataFSProviderExternal as ProviderPage,
    PageDataJob as JobPage,
    ProviderItem,
    QAJobInputs,
    QAJobOutputs,
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
