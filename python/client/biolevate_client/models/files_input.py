from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilesInput")


@_attrs_define
class FilesInput:
    """
    Attributes:
        file_ids (list[str] | Unset):
        collection_ids (list[str] | Unset):
    """

    file_ids: list[str] | Unset = UNSET
    collection_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        collection_ids: list[str] | Unset = UNSET
        if not isinstance(self.collection_ids, Unset):
            collection_ids = self.collection_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_ids is not UNSET:
            field_dict["fileIds"] = file_ids
        if collection_ids is not UNSET:
            field_dict["collectionIds"] = collection_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_ids = cast(list[str], d.pop("fileIds", UNSET))

        collection_ids = cast(list[str], d.pop("collectionIds", UNSET))

        files_input = cls(
            file_ids=file_ids,
            collection_ids=collection_ids,
        )

        files_input.additional_properties = d
        return files_input

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
