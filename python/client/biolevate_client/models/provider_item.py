from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_item_type import ProviderItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderItem")


@_attrs_define
class ProviderItem:
    """Provider item (file or folder)

    Attributes:
        provider_id (str | Unset): Provider ID Example: 550e8400-e29b-41d4-a716-446655440000.
        name (str | Unset): Item name Example: document.pdf.
        path (str | Unset): Directory path Example: /reports/.
        type_ (ProviderItemType | Unset): Item type Example: FILE.
        size (int | Unset): File size in bytes (null for folders) Example: 1048576.
        extension (str | Unset): File extension (null for folders) Example: pdf.
        media_type (str | Unset): Media type (null for folders) Example: application/pdf.
        last_modified (int | Unset): Last modified timestamp in milliseconds Example: 1708123456789.
    """

    provider_id: str | Unset = UNSET
    name: str | Unset = UNSET
    path: str | Unset = UNSET
    type_: ProviderItemType | Unset = UNSET
    size: int | Unset = UNSET
    extension: str | Unset = UNSET
    media_type: str | Unset = UNSET
    last_modified: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        name = self.name

        path = self.path

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        size = self.size

        extension = self.extension

        media_type = self.media_type

        last_modified = self.last_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_
        if size is not UNSET:
            field_dict["size"] = size
        if extension is not UNSET:
            field_dict["extension"] = extension
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("providerId", UNSET)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ProviderItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProviderItemType(_type_)

        size = d.pop("size", UNSET)

        extension = d.pop("extension", UNSET)

        media_type = d.pop("mediaType", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        provider_item = cls(
            provider_id=provider_id,
            name=name,
            path=path,
            type_=type_,
            size=size,
            extension=extension,
            media_type=media_type,
            last_modified=last_modified,
        )

        provider_item.additional_properties = d
        return provider_item

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
