from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expected_answer_type_dto import ExpectedAnswerTypeDto


T = TypeVar("T", bound="EliseMetaInput")


@_attrs_define
class EliseMetaInput:
    """
    Attributes:
        meta (str | Unset):
        answer_type (ExpectedAnswerTypeDto | Unset):
        description (str | Unset):
    """

    meta: str | Unset = UNSET
    answer_type: ExpectedAnswerTypeDto | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta = self.meta

        answer_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answer_type, Unset):
            answer_type = self.answer_type.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if answer_type is not UNSET:
            field_dict["answerType"] = answer_type
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expected_answer_type_dto import ExpectedAnswerTypeDto

        d = dict(src_dict)
        meta = d.pop("meta", UNSET)

        _answer_type = d.pop("answerType", UNSET)
        answer_type: ExpectedAnswerTypeDto | Unset
        if isinstance(_answer_type, Unset):
            answer_type = UNSET
        else:
            answer_type = ExpectedAnswerTypeDto.from_dict(_answer_type)

        description = d.pop("description", UNSET)

        elise_meta_input = cls(
            meta=meta,
            answer_type=answer_type,
            description=description,
        )

        elise_meta_input.additional_properties = d
        return elise_meta_input

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
