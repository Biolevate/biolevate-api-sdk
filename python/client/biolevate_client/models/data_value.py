from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataValue")


@_attrs_define
class DataValue:
    """
    Attributes:
        str_value (str | Unset):
        bool_value (bool | Unset):
        long_value (int | Unset):
        double_value (float | Unset):
        date_value (datetime.datetime | Unset):
        str_list_value (list[str] | Unset):
        bool_list_value (list[bool] | Unset):
        long_list_value (list[int] | Unset):
        double_list_value (list[float] | Unset):
        date_list_value (list[datetime.datetime] | Unset):
    """

    str_value: str | Unset = UNSET
    bool_value: bool | Unset = UNSET
    long_value: int | Unset = UNSET
    double_value: float | Unset = UNSET
    date_value: datetime.datetime | Unset = UNSET
    str_list_value: list[str] | Unset = UNSET
    bool_list_value: list[bool] | Unset = UNSET
    long_list_value: list[int] | Unset = UNSET
    double_list_value: list[float] | Unset = UNSET
    date_list_value: list[datetime.datetime] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        str_value = self.str_value

        bool_value = self.bool_value

        long_value = self.long_value

        double_value = self.double_value

        date_value: str | Unset = UNSET
        if not isinstance(self.date_value, Unset):
            date_value = self.date_value.isoformat()

        str_list_value: list[str] | Unset = UNSET
        if not isinstance(self.str_list_value, Unset):
            str_list_value = self.str_list_value

        bool_list_value: list[bool] | Unset = UNSET
        if not isinstance(self.bool_list_value, Unset):
            bool_list_value = self.bool_list_value

        long_list_value: list[int] | Unset = UNSET
        if not isinstance(self.long_list_value, Unset):
            long_list_value = self.long_list_value

        double_list_value: list[float] | Unset = UNSET
        if not isinstance(self.double_list_value, Unset):
            double_list_value = self.double_list_value

        date_list_value: list[str] | Unset = UNSET
        if not isinstance(self.date_list_value, Unset):
            date_list_value = []
            for date_list_value_item_data in self.date_list_value:
                date_list_value_item = date_list_value_item_data.isoformat()
                date_list_value.append(date_list_value_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if str_value is not UNSET:
            field_dict["strValue"] = str_value
        if bool_value is not UNSET:
            field_dict["boolValue"] = bool_value
        if long_value is not UNSET:
            field_dict["longValue"] = long_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if date_value is not UNSET:
            field_dict["dateValue"] = date_value
        if str_list_value is not UNSET:
            field_dict["strListValue"] = str_list_value
        if bool_list_value is not UNSET:
            field_dict["boolListValue"] = bool_list_value
        if long_list_value is not UNSET:
            field_dict["longListValue"] = long_list_value
        if double_list_value is not UNSET:
            field_dict["doubleListValue"] = double_list_value
        if date_list_value is not UNSET:
            field_dict["dateListValue"] = date_list_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        str_value = d.pop("strValue", UNSET)

        bool_value = d.pop("boolValue", UNSET)

        long_value = d.pop("longValue", UNSET)

        double_value = d.pop("doubleValue", UNSET)

        _date_value = d.pop("dateValue", UNSET)
        date_value: datetime.datetime | Unset
        if isinstance(_date_value, Unset):
            date_value = UNSET
        else:
            date_value = isoparse(_date_value)

        str_list_value = cast(list[str], d.pop("strListValue", UNSET))

        bool_list_value = cast(list[bool], d.pop("boolListValue", UNSET))

        long_list_value = cast(list[int], d.pop("longListValue", UNSET))

        double_list_value = cast(list[float], d.pop("doubleListValue", UNSET))

        _date_list_value = d.pop("dateListValue", UNSET)
        date_list_value: list[datetime.datetime] | Unset = UNSET
        if _date_list_value is not UNSET:
            date_list_value = []
            for date_list_value_item_data in _date_list_value:
                date_list_value_item = isoparse(date_list_value_item_data)

                date_list_value.append(date_list_value_item)

        data_value = cls(
            str_value=str_value,
            bool_value=bool_value,
            long_value=long_value,
            double_value=double_value,
            date_value=date_value,
            str_list_value=str_list_value,
            bool_list_value=bool_list_value,
            long_list_value=long_list_value,
            double_list_value=double_list_value,
            date_list_value=date_list_value,
        )

        data_value.additional_properties = d
        return data_value

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
