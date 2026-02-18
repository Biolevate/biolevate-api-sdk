from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elise_annotation_config_type import EliseAnnotationConfigType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="EliseExternalDocumentStatement")


@_attrs_define
class EliseExternalDocumentStatement:
    """
    Attributes:
        type_ (EliseAnnotationConfigType | Unset):
        meta_data (JsonNode | Unset):
    """

    type_: EliseAnnotationConfigType | Unset = UNSET
    meta_data: JsonNode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_node import JsonNode

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: EliseAnnotationConfigType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EliseAnnotationConfigType(_type_)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: JsonNode | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = JsonNode.from_dict(_meta_data)

        elise_external_document_statement = cls(
            type_=type_,
            meta_data=meta_data,
        )

        elise_external_document_statement.additional_properties = d
        return elise_external_document_statement

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
