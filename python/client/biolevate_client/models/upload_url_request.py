from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadUrlRequest")


@_attrs_define
class UploadUrlRequest:
    """Request for presigned upload URL

    Attributes:
        path (str): Target directory path Example: /reports/.
        file_name (str): File name Example: document.pdf.
        size (int | Unset): File size in bytes Example: 1048576.
        media_type (str | Unset): Media type Example: application/pdf.
    """

    path: str
    file_name: str
    size: int | Unset = UNSET
    media_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        file_name = self.file_name

        size = self.size

        media_type = self.media_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "fileName": file_name,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        file_name = d.pop("fileName")

        size = d.pop("size", UNSET)

        media_type = d.pop("mediaType", UNSET)

        upload_url_request = cls(
            path=path,
            file_name=file_name,
            size=size,
            media_type=media_type,
        )

        upload_url_request.additional_properties = d
        return upload_url_request

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
