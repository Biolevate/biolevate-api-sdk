from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadUrlResponse")


@_attrs_define
class DownloadUrlResponse:
    """Download URL response

    Attributes:
        url (str | Unset): URL to download the file
        expires_in_seconds (int | Unset): Time in seconds until the URL expires
    """

    url: str | Unset = UNSET
    expires_in_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        expires_in_seconds = self.expires_in_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if expires_in_seconds is not UNSET:
            field_dict["expiresInSeconds"] = expires_in_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        expires_in_seconds = d.pop("expiresInSeconds", UNSET)

        download_url_response = cls(
            url=url,
            expires_in_seconds=expires_in_seconds,
        )

        download_url_response.additional_properties = d
        return download_url_response

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
