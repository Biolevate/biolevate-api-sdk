from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position_dto_type import PositionDtoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionCellDto")


@_attrs_define
class PositionCellDto:
    """
    Attributes:
        type_ (PositionDtoType | Unset):
        sheet_name (str | Unset):
        row (int | Unset):
        col (int | Unset):
    """

    type_: PositionDtoType | Unset = UNSET
    sheet_name: str | Unset = UNSET
    row: int | Unset = UNSET
    col: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        sheet_name = self.sheet_name

        row = self.row

        col = self.col

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sheet_name is not UNSET:
            field_dict["sheet_name"] = sheet_name
        if row is not UNSET:
            field_dict["row"] = row
        if col is not UNSET:
            field_dict["col"] = col

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

        sheet_name = d.pop("sheet_name", UNSET)

        row = d.pop("row", UNSET)

        col = d.pop("col", UNSET)

        position_cell_dto = cls(
            type_=type_,
            sheet_name=sheet_name,
            row=row,
            col=col,
        )

        position_cell_dto.additional_properties = d
        return position_cell_dto

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
