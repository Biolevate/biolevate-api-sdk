from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position_dto_type import PositionDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bbox_dto import BboxDto


T = TypeVar("T", bound="PositionBboxDto")


@_attrs_define
class PositionBboxDto:
    """
    Attributes:
        type_ (PositionDtoType | Unset):
        bbox (BboxDto | Unset):
        page_number (int | Unset):
    """

    type_: PositionDtoType | Unset = UNSET
    bbox: BboxDto | Unset = UNSET
    page_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        bbox: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox.to_dict()

        page_number = self.page_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if page_number is not UNSET:
            field_dict["page_number"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bbox_dto import BboxDto

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: PositionDtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PositionDtoType(_type_)

        _bbox = d.pop("bbox", UNSET)
        bbox: BboxDto | Unset
        if isinstance(_bbox, Unset):
            bbox = UNSET
        else:
            bbox = BboxDto.from_dict(_bbox)

        page_number = d.pop("page_number", UNSET)

        position_bbox_dto = cls(
            type_=type_,
            bbox=bbox,
            page_number=page_number,
        )

        position_bbox_dto.additional_properties = d
        return position_bbox_dto

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
