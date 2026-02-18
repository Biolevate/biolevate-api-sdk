from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elise_annotation_config_type import EliseAnnotationConfigType
from ..models.elise_web_statement_source import EliseWebStatementSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="EliseWebStatement")


@_attrs_define
class EliseWebStatement:
    """
    Attributes:
        type_ (EliseAnnotationConfigType | Unset):
        url (str | Unset):
        source (EliseWebStatementSource | Unset):
    """

    type_: EliseAnnotationConfigType | Unset = UNSET
    url: str | Unset = UNSET
    source: EliseWebStatementSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if source is not UNSET:
            field_dict["source"] = source

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

        url = d.pop("url", UNSET)

        _source = d.pop("source", UNSET)
        source: EliseWebStatementSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = EliseWebStatementSource(_source)

        elise_web_statement = cls(
            type_=type_,
            url=url,
            source=source,
        )

        elise_web_statement.additional_properties = d
        return elise_web_statement

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
