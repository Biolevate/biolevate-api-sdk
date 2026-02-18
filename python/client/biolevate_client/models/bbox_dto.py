from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BboxDto")


@_attrs_define
class BboxDto:
    """
    Attributes:
        x0 (float | Unset):
        y0 (float | Unset):
        x1 (float | Unset):
        y1 (float | Unset):
    """

    x0: float | Unset = UNSET
    y0: float | Unset = UNSET
    x1: float | Unset = UNSET
    y1: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x0 = self.x0

        y0 = self.y0

        x1 = self.x1

        y1 = self.y1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x0 is not UNSET:
            field_dict["x0"] = x0
        if y0 is not UNSET:
            field_dict["y0"] = y0
        if x1 is not UNSET:
            field_dict["x1"] = x1
        if y1 is not UNSET:
            field_dict["y1"] = y1

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x0 = d.pop("x0", UNSET)

        y0 = d.pop("y0", UNSET)

        x1 = d.pop("x1", UNSET)

        y1 = d.pop("y1", UNSET)

        bbox_dto = cls(
            x0=x0,
            y0=y0,
            x1=x1,
            y1=y1,
        )

        bbox_dto.additional_properties = d
        return bbox_dto

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
