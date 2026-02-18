from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_provider_external import FSProviderExternal


T = TypeVar("T", bound="PageDataFSProviderExternal")


@_attrs_define
class PageDataFSProviderExternal:
    """
    Attributes:
        data (list[FSProviderExternal] | Unset):
        total_pages (int | Unset):
        total_elements (int | Unset):
        has_next (bool | Unset):
    """

    data: list[FSProviderExternal] | Unset = UNSET
    total_pages: int | Unset = UNSET
    total_elements: int | Unset = UNSET
    has_next: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        total_pages = self.total_pages

        total_elements = self.total_elements

        has_next = self.has_next

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if has_next is not UNSET:
            field_dict["hasNext"] = has_next

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_provider_external import FSProviderExternal

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[FSProviderExternal] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = FSProviderExternal.from_dict(data_item_data)

                data.append(data_item)

        total_pages = d.pop("totalPages", UNSET)

        total_elements = d.pop("totalElements", UNSET)

        has_next = d.pop("hasNext", UNSET)

        page_data_fs_provider_external = cls(
            data=data,
            total_pages=total_pages,
            total_elements=total_elements,
            has_next=has_next,
        )

        page_data_fs_provider_external.additional_properties = d
        return page_data_fs_provider_external

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
