from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position_dto_type import PositionDtoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionLineDto")


@_attrs_define
class PositionLineDto:
    """
    Attributes:
        type_ (PositionDtoType | Unset):
        line_number (int | Unset):
        column_index_start (int | Unset):
        column_index_stop (int | Unset):
    """

    type_: PositionDtoType | Unset = UNSET
    line_number: int | Unset = UNSET
    column_index_start: int | Unset = UNSET
    column_index_stop: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        line_number = self.line_number

        column_index_start = self.column_index_start

        column_index_stop = self.column_index_stop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if line_number is not UNSET:
            field_dict["line_number"] = line_number
        if column_index_start is not UNSET:
            field_dict["column_index_start"] = column_index_start
        if column_index_stop is not UNSET:
            field_dict["column_index_stop"] = column_index_stop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: PositionDtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PositionDtoType(_type_)

        line_number = d.pop("line_number", UNSET)

        column_index_start = d.pop("column_index_start", UNSET)

        column_index_stop = d.pop("column_index_stop", UNSET)

        position_line_dto = cls(
            type_=type_,
            line_number=line_number,
            column_index_start=column_index_start,
            column_index_stop=column_index_stop,
        )

        position_line_dto.additional_properties = d
        return position_line_dto

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
