from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expected_answer_type_dto_data_type import ExpectedAnswerTypeDtoDataType
from ..models.expected_answer_type_dto_date_format import ExpectedAnswerTypeDtoDateFormat
from ..models.expected_answer_type_dto_decimal_precision import ExpectedAnswerTypeDtoDecimalPrecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expected_answer_type_dto_enum_colors import ExpectedAnswerTypeDtoEnumColors


T = TypeVar("T", bound="ExpectedAnswerTypeDto")


@_attrs_define
class ExpectedAnswerTypeDto:
    """
    Attributes:
        data_type (ExpectedAnswerTypeDtoDataType | Unset):
        multi_valued (bool | Unset):
        enum_values (list[str] | Unset): List of possible values for enum types
        enum_colors (ExpectedAnswerTypeDtoEnumColors | Unset): Map of enum values to their associated colors
        enum_suggestions_enabled (bool | Unset):
        rejected_enum_values (list[str] | Unset):
        date_format (ExpectedAnswerTypeDtoDateFormat | Unset):
        decimal_precision (ExpectedAnswerTypeDtoDecimalPrecision | Unset):
    """

    data_type: ExpectedAnswerTypeDtoDataType | Unset = UNSET
    multi_valued: bool | Unset = UNSET
    enum_values: list[str] | Unset = UNSET
    enum_colors: ExpectedAnswerTypeDtoEnumColors | Unset = UNSET
    enum_suggestions_enabled: bool | Unset = UNSET
    rejected_enum_values: list[str] | Unset = UNSET
    date_format: ExpectedAnswerTypeDtoDateFormat | Unset = UNSET
    decimal_precision: ExpectedAnswerTypeDtoDecimalPrecision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_type: str | Unset = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        multi_valued = self.multi_valued

        enum_values: list[str] | Unset = UNSET
        if not isinstance(self.enum_values, Unset):
            enum_values = self.enum_values

        enum_colors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enum_colors, Unset):
            enum_colors = self.enum_colors.to_dict()

        enum_suggestions_enabled = self.enum_suggestions_enabled

        rejected_enum_values: list[str] | Unset = UNSET
        if not isinstance(self.rejected_enum_values, Unset):
            rejected_enum_values = self.rejected_enum_values

        date_format: str | Unset = UNSET
        if not isinstance(self.date_format, Unset):
            date_format = self.date_format.value

        decimal_precision: str | Unset = UNSET
        if not isinstance(self.decimal_precision, Unset):
            decimal_precision = self.decimal_precision.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if multi_valued is not UNSET:
            field_dict["multiValued"] = multi_valued
        if enum_values is not UNSET:
            field_dict["enumValues"] = enum_values
        if enum_colors is not UNSET:
            field_dict["enumColors"] = enum_colors
        if enum_suggestions_enabled is not UNSET:
            field_dict["enumSuggestionsEnabled"] = enum_suggestions_enabled
        if rejected_enum_values is not UNSET:
            field_dict["rejectedEnumValues"] = rejected_enum_values
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if decimal_precision is not UNSET:
            field_dict["decimalPrecision"] = decimal_precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expected_answer_type_dto_enum_colors import ExpectedAnswerTypeDtoEnumColors

        d = dict(src_dict)
        _data_type = d.pop("dataType", UNSET)
        data_type: ExpectedAnswerTypeDtoDataType | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = ExpectedAnswerTypeDtoDataType(_data_type)

        multi_valued = d.pop("multiValued", UNSET)

        enum_values = cast(list[str], d.pop("enumValues", UNSET))

        _enum_colors = d.pop("enumColors", UNSET)
        enum_colors: ExpectedAnswerTypeDtoEnumColors | Unset
        if isinstance(_enum_colors, Unset):
            enum_colors = UNSET
        else:
            enum_colors = ExpectedAnswerTypeDtoEnumColors.from_dict(_enum_colors)

        enum_suggestions_enabled = d.pop("enumSuggestionsEnabled", UNSET)

        rejected_enum_values = cast(list[str], d.pop("rejectedEnumValues", UNSET))

        _date_format = d.pop("dateFormat", UNSET)
        date_format: ExpectedAnswerTypeDtoDateFormat | Unset
        if isinstance(_date_format, Unset):
            date_format = UNSET
        else:
            date_format = ExpectedAnswerTypeDtoDateFormat(_date_format)

        _decimal_precision = d.pop("decimalPrecision", UNSET)
        decimal_precision: ExpectedAnswerTypeDtoDecimalPrecision | Unset
        if isinstance(_decimal_precision, Unset):
            decimal_precision = UNSET
        else:
            decimal_precision = ExpectedAnswerTypeDtoDecimalPrecision(_decimal_precision)

        expected_answer_type_dto = cls(
            data_type=data_type,
            multi_valued=multi_valued,
            enum_values=enum_values,
            enum_colors=enum_colors,
            enum_suggestions_enabled=enum_suggestions_enabled,
            rejected_enum_values=rejected_enum_values,
            date_format=date_format,
            decimal_precision=decimal_precision,
        )

        expected_answer_type_dto.additional_properties = d
        return expected_answer_type_dto

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
