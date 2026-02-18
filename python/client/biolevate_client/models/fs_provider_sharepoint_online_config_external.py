from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fs_provider_configuration_external_type import FSProviderConfigurationExternalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FSProviderSharepointOnlineConfigExternal")


@_attrs_define
class FSProviderSharepointOnlineConfigExternal:
    """
    Attributes:
        site_url (str):
        document_library (str):
        tenant_id (str):
        type_ (FSProviderConfigurationExternalType | Unset):
    """

    site_url: str
    document_library: str
    tenant_id: str
    type_: FSProviderConfigurationExternalType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_url = self.site_url

        document_library = self.document_library

        tenant_id = self.tenant_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteUrl": site_url,
                "documentLibrary": document_library,
                "tenantId": tenant_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_url = d.pop("siteUrl")

        document_library = d.pop("documentLibrary")

        tenant_id = d.pop("tenantId")

        _type_ = d.pop("type", UNSET)
        type_: FSProviderConfigurationExternalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FSProviderConfigurationExternalType(_type_)

        fs_provider_sharepoint_online_config_external = cls(
            site_url=site_url,
            document_library=document_library,
            tenant_id=tenant_id,
            type_=type_,
        )

        fs_provider_sharepoint_online_config_external.additional_properties = d
        return fs_provider_sharepoint_online_config_external

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
