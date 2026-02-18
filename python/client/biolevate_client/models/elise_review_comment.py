from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elise_annotation_config_type import EliseAnnotationConfigType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position_bbox_dto import PositionBboxDto
    from ..models.position_cell_dto import PositionCellDto
    from ..models.position_line_dto import PositionLineDto


T = TypeVar("T", bound="EliseReviewComment")


@_attrs_define
class EliseReviewComment:
    """
    Attributes:
        type_ (EliseAnnotationConfigType | Unset):
        content (str | Unset):
        document_name (str | Unset):
        document_id (str | Unset):
        positions (list[PositionBboxDto | PositionCellDto | PositionLineDto] | Unset):
    """

    type_: EliseAnnotationConfigType | Unset = UNSET
    content: str | Unset = UNSET
    document_name: str | Unset = UNSET
    document_id: str | Unset = UNSET
    positions: list[PositionBboxDto | PositionCellDto | PositionLineDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.position_bbox_dto import PositionBboxDto
        from ..models.position_cell_dto import PositionCellDto

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        content = self.content

        document_name = self.document_name

        document_id = self.document_id

        positions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.positions, Unset):
            positions = []
            for positions_item_data in self.positions:
                positions_item: dict[str, Any]
                if isinstance(positions_item_data, PositionBboxDto):
                    positions_item = positions_item_data.to_dict()
                elif isinstance(positions_item_data, PositionCellDto):
                    positions_item = positions_item_data.to_dict()
                else:
                    positions_item = positions_item_data.to_dict()

                positions.append(positions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content
        if document_name is not UNSET:
            field_dict["documentName"] = document_name
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if positions is not UNSET:
            field_dict["positions"] = positions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position_bbox_dto import PositionBboxDto
        from ..models.position_cell_dto import PositionCellDto
        from ..models.position_line_dto import PositionLineDto

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: EliseAnnotationConfigType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EliseAnnotationConfigType(_type_)

        content = d.pop("content", UNSET)

        document_name = d.pop("documentName", UNSET)

        document_id = d.pop("documentId", UNSET)

        _positions = d.pop("positions", UNSET)
        positions: list[PositionBboxDto | PositionCellDto | PositionLineDto] | Unset = UNSET
        if _positions is not UNSET:
            positions = []
            for positions_item_data in _positions:

                def _parse_positions_item(data: object) -> PositionBboxDto | PositionCellDto | PositionLineDto:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        positions_item_type_0 = PositionBboxDto.from_dict(data)

                        return positions_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        positions_item_type_1 = PositionCellDto.from_dict(data)

                        return positions_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    positions_item_type_2 = PositionLineDto.from_dict(data)

                    return positions_item_type_2

                positions_item = _parse_positions_item(positions_item_data)

                positions.append(positions_item)

        elise_review_comment = cls(
            type_=type_,
            content=content,
            document_name=document_name,
            document_id=document_id,
            positions=positions,
        )

        elise_review_comment.additional_properties = d
        return elise_review_comment

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
