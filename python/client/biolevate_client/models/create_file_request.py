from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateFileRequest")


@_attrs_define
class CreateFileRequest:
    """Request to create EliseFile from provider item

    Attributes:
        provider_id (str): Source provider ID Example: 01a91a21-3136-4094-96da-ded4dce3824f.
        path (str): File path in provider Example: documents/.
        name (str): File name Example: report.pdf.
    """

    provider_id: str
    path: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        path = self.path

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "providerId": provider_id,
                "path": path,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("providerId")

        path = d.pop("path")

        name = d.pop("name")

        create_file_request = cls(
            provider_id=provider_id,
            path=path,
            name=name,
        )

        create_file_request.additional_properties = d
        return create_file_request

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
