from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elise_annotation_status import EliseAnnotationStatus
from ..models.elise_annotation_type import EliseAnnotationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_id import AnnotationId
    from ..models.elise_document_statement import EliseDocumentStatement
    from ..models.elise_external_document_statement import EliseExternalDocumentStatement
    from ..models.elise_full_document_statement import EliseFullDocumentStatement
    from ..models.elise_knowledge_statement import EliseKnowledgeStatement
    from ..models.elise_review_comment import EliseReviewComment
    from ..models.elise_web_statement import EliseWebStatement
    from ..models.entity_id import EntityId
    from ..models.user_id import UserId


T = TypeVar("T", bound="EliseAnnotation")


@_attrs_define
class EliseAnnotation:
    """
    Attributes:
        id (AnnotationId | Unset):
        created_time (int | Unset):
        owner (UserId | Unset):
        space (EntityId | Unset):
        data (EliseDocumentStatement | EliseExternalDocumentStatement | EliseFullDocumentStatement |
            EliseKnowledgeStatement | EliseReviewComment | EliseWebStatement | Unset):
        type_ (EliseAnnotationType | Unset):
        modified_time (int | Unset):
        last_modifier (UserId | Unset):
        status (EliseAnnotationStatus | Unset):
    """

    id: AnnotationId | Unset = UNSET
    created_time: int | Unset = UNSET
    owner: UserId | Unset = UNSET
    space: EntityId | Unset = UNSET
    data: (
        EliseDocumentStatement
        | EliseExternalDocumentStatement
        | EliseFullDocumentStatement
        | EliseKnowledgeStatement
        | EliseReviewComment
        | EliseWebStatement
        | Unset
    ) = UNSET
    type_: EliseAnnotationType | Unset = UNSET
    modified_time: int | Unset = UNSET
    last_modifier: UserId | Unset = UNSET
    status: EliseAnnotationStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.elise_document_statement import EliseDocumentStatement
        from ..models.elise_external_document_statement import EliseExternalDocumentStatement
        from ..models.elise_full_document_statement import EliseFullDocumentStatement
        from ..models.elise_knowledge_statement import EliseKnowledgeStatement
        from ..models.elise_review_comment import EliseReviewComment

        id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        created_time = self.created_time

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        space: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space, Unset):
            space = self.space.to_dict()

        data: dict[str, Any] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, EliseDocumentStatement):
            data = self.data.to_dict()
        elif isinstance(self.data, EliseExternalDocumentStatement):
            data = self.data.to_dict()
        elif isinstance(self.data, EliseFullDocumentStatement):
            data = self.data.to_dict()
        elif isinstance(self.data, EliseKnowledgeStatement):
            data = self.data.to_dict()
        elif isinstance(self.data, EliseReviewComment):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        modified_time = self.modified_time

        last_modifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modifier, Unset):
            last_modifier = self.last_modifier.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if owner is not UNSET:
            field_dict["owner"] = owner
        if space is not UNSET:
            field_dict["space"] = space
        if data is not UNSET:
            field_dict["data"] = data
        if type_ is not UNSET:
            field_dict["type"] = type_
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time
        if last_modifier is not UNSET:
            field_dict["lastModifier"] = last_modifier
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_id import AnnotationId
        from ..models.elise_document_statement import EliseDocumentStatement
        from ..models.elise_external_document_statement import EliseExternalDocumentStatement
        from ..models.elise_full_document_statement import EliseFullDocumentStatement
        from ..models.elise_knowledge_statement import EliseKnowledgeStatement
        from ..models.elise_review_comment import EliseReviewComment
        from ..models.elise_web_statement import EliseWebStatement
        from ..models.entity_id import EntityId
        from ..models.user_id import UserId

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: AnnotationId | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = AnnotationId.from_dict(_id)

        created_time = d.pop("createdTime", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: UserId | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = UserId.from_dict(_owner)

        _space = d.pop("space", UNSET)
        space: EntityId | Unset
        if isinstance(_space, Unset):
            space = UNSET
        else:
            space = EntityId.from_dict(_space)

        def _parse_data(
            data: object,
        ) -> (
            EliseDocumentStatement
            | EliseExternalDocumentStatement
            | EliseFullDocumentStatement
            | EliseKnowledgeStatement
            | EliseReviewComment
            | EliseWebStatement
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = EliseDocumentStatement.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = EliseExternalDocumentStatement.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_2 = EliseFullDocumentStatement.from_dict(data)

                return data_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_3 = EliseKnowledgeStatement.from_dict(data)

                return data_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_4 = EliseReviewComment.from_dict(data)

                return data_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_5 = EliseWebStatement.from_dict(data)

            return data_type_5

        data = _parse_data(d.pop("data", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: EliseAnnotationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EliseAnnotationType(_type_)

        modified_time = d.pop("modifiedTime", UNSET)

        _last_modifier = d.pop("lastModifier", UNSET)
        last_modifier: UserId | Unset
        if isinstance(_last_modifier, Unset):
            last_modifier = UNSET
        else:
            last_modifier = UserId.from_dict(_last_modifier)

        _status = d.pop("status", UNSET)
        status: EliseAnnotationStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EliseAnnotationStatus(_status)

        elise_annotation = cls(
            id=id,
            created_time=created_time,
            owner=owner,
            space=space,
            data=data,
            type_=type_,
            modified_time=modified_time,
            last_modifier=last_modifier,
            status=status,
        )

        elise_annotation.additional_properties = d
        return elise_annotation

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
