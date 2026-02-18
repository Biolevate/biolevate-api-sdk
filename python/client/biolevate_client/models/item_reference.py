from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_reference_type import ItemReferenceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemReference")


@_attrs_define
class ItemReference:
    """Reference to an item for delete operations

    Attributes:
        name (str): Item name Example: document.pdf.
        type_ (ItemReferenceType): Item type Example: FILE.
        path (str | Unset): Directory path containing the item Example: /reports/.
    """

    name: str
    type_: ItemReferenceType
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ItemReferenceType(d.pop("type"))

        path = d.pop("path", UNSET)

        item_reference = cls(
            name=name,
            type_=type_,
            path=path,
        )

        item_reference.additional_properties = d
        return item_reference

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
