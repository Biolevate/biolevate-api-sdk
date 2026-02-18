from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lib_item_indexation_infos_status import LibItemIndexationInfosStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LibItemIndexationInfos")


@_attrs_define
class LibItemIndexationInfos:
    """
    Attributes:
        status (LibItemIndexationInfosStatus | Unset):
        error_message (str | Unset):
        error_traceback (str | Unset):
    """

    status: LibItemIndexationInfosStatus | Unset = UNSET
    error_message: str | Unset = UNSET
    error_traceback: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error_message = self.error_message

        error_traceback = self.error_traceback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if error_traceback is not UNSET:
            field_dict["errorTraceback"] = error_traceback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: LibItemIndexationInfosStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LibItemIndexationInfosStatus(_status)

        error_message = d.pop("errorMessage", UNSET)

        error_traceback = d.pop("errorTraceback", UNSET)

        lib_item_indexation_infos = cls(
            status=status,
            error_message=error_message,
            error_traceback=error_traceback,
        )

        lib_item_indexation_infos.additional_properties = d
        return lib_item_indexation_infos

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
