from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elise_annotation_config_type import EliseAnnotationConfigType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EliseKnowledgeStatement")


@_attrs_define
class EliseKnowledgeStatement:
    """
    Attributes:
        type_ (EliseAnnotationConfigType | Unset):
        name (str | Unset):
        value (str | Unset):
    """

    type_: EliseAnnotationConfigType | Unset = UNSET
    name: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: EliseAnnotationConfigType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EliseAnnotationConfigType(_type_)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        elise_knowledge_statement = cls(
            type_=type_,
            name=name,
            value=value,
        )

        elise_knowledge_statement.additional_properties = d
        return elise_knowledge_statement

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
