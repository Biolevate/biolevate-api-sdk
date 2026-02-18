from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_id import AnnotationId
    from ..models.data_value import DataValue
    from ..models.elise_meta_result_raw_value import EliseMetaResultRawValue
    from ..models.expected_answer_type_dto import ExpectedAnswerTypeDto


T = TypeVar("T", bound="EliseMetaResult")


@_attrs_define
class EliseMetaResult:
    """
    Attributes:
        id (UUID | Unset):
        explanation (str | Unset):
        answer_type (ExpectedAnswerTypeDto | Unset):
        answer (DataValue | Unset):
        reference_ids (list[AnnotationId] | Unset):
        meta (str | Unset):
        raw_value (EliseMetaResultRawValue | Unset):
    """

    id: UUID | Unset = UNSET
    explanation: str | Unset = UNSET
    answer_type: ExpectedAnswerTypeDto | Unset = UNSET
    answer: DataValue | Unset = UNSET
    reference_ids: list[AnnotationId] | Unset = UNSET
    meta: str | Unset = UNSET
    raw_value: EliseMetaResultRawValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        explanation = self.explanation

        answer_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answer_type, Unset):
            answer_type = self.answer_type.to_dict()

        answer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        reference_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reference_ids, Unset):
            reference_ids = []
            for reference_ids_item_data in self.reference_ids:
                reference_ids_item = reference_ids_item_data.to_dict()
                reference_ids.append(reference_ids_item)

        meta = self.meta

        raw_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw_value, Unset):
            raw_value = self.raw_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if answer_type is not UNSET:
            field_dict["answerType"] = answer_type
        if answer is not UNSET:
            field_dict["answer"] = answer
        if reference_ids is not UNSET:
            field_dict["referenceIds"] = reference_ids
        if meta is not UNSET:
            field_dict["meta"] = meta
        if raw_value is not UNSET:
            field_dict["rawValue"] = raw_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_id import AnnotationId
        from ..models.data_value import DataValue
        from ..models.elise_meta_result_raw_value import EliseMetaResultRawValue
        from ..models.expected_answer_type_dto import ExpectedAnswerTypeDto

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        explanation = d.pop("explanation", UNSET)

        _answer_type = d.pop("answerType", UNSET)
        answer_type: ExpectedAnswerTypeDto | Unset
        if isinstance(_answer_type, Unset):
            answer_type = UNSET
        else:
            answer_type = ExpectedAnswerTypeDto.from_dict(_answer_type)

        _answer = d.pop("answer", UNSET)
        answer: DataValue | Unset
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = DataValue.from_dict(_answer)

        _reference_ids = d.pop("referenceIds", UNSET)
        reference_ids: list[AnnotationId] | Unset = UNSET
        if _reference_ids is not UNSET:
            reference_ids = []
            for reference_ids_item_data in _reference_ids:
                reference_ids_item = AnnotationId.from_dict(reference_ids_item_data)

                reference_ids.append(reference_ids_item)

        meta = d.pop("meta", UNSET)

        _raw_value = d.pop("rawValue", UNSET)
        raw_value: EliseMetaResultRawValue | Unset
        if isinstance(_raw_value, Unset):
            raw_value = UNSET
        else:
            raw_value = EliseMetaResultRawValue.from_dict(_raw_value)

        elise_meta_result = cls(
            id=id,
            explanation=explanation,
            answer_type=answer_type,
            answer=answer,
            reference_ids=reference_ids,
            meta=meta,
            raw_value=raw_value,
        )

        elise_meta_result.additional_properties = d
        return elise_meta_result

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
