from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elise_annotation_config_type import EliseAnnotationConfigType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EliseFullDocumentStatement")


@_attrs_define
class EliseFullDocumentStatement:
    """
    Attributes:
        type_ (EliseAnnotationConfigType | Unset):
        document_name (str | Unset):
        document_id (str | Unset):
    """

    type_: EliseAnnotationConfigType | Unset = UNSET
    document_name: str | Unset = UNSET
    document_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        document_name = self.document_name

        document_id = self.document_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if document_name is not UNSET:
            field_dict["documentName"] = document_name
        if document_id is not UNSET:
            field_dict["documentId"] = document_id

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

        document_name = d.pop("documentName", UNSET)

        document_id = d.pop("documentId", UNSET)

        elise_full_document_statement = cls(
            type_=type_,
            document_name=document_name,
            document_id=document_id,
        )

        elise_full_document_statement.additional_properties = d
        return elise_full_document_statement

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
