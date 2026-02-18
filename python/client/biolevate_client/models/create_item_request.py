from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_item_request_type import CreateItemRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateItemRequest")


@_attrs_define
class CreateItemRequest:
    """Create folder request (for JSON body). For file upload, use multipart form.

    Attributes:
        type_ (CreateItemRequestType): Item type Example: FOLDER.
        name (str): Item name Example: new-folder.
        path (str | Unset): Parent directory path Example: /reports/.
    """

    type_: CreateItemRequestType
    name: str
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CreateItemRequestType(d.pop("type"))

        name = d.pop("name")

        path = d.pop("path", UNSET)

        create_item_request = cls(
            type_=type_,
            name=name,
            path=path,
        )

        create_item_request.additional_properties = d
        return create_item_request

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
