from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fs_provider_configuration_external_type import FSProviderConfigurationExternalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FSProviderAzureConfigExternal")


@_attrs_define
class FSProviderAzureConfigExternal:
    """
    Attributes:
        container_name (str):
        type_ (FSProviderConfigurationExternalType | Unset):
        account_name (str | Unset):
        use_workload_identity (bool | Unset):
        workload_identity_enabled (bool | Unset):
        connection_string_enabled (bool | Unset):
        endpoint_url (str | Unset):
    """

    container_name: str
    type_: FSProviderConfigurationExternalType | Unset = UNSET
    account_name: str | Unset = UNSET
    use_workload_identity: bool | Unset = UNSET
    workload_identity_enabled: bool | Unset = UNSET
    connection_string_enabled: bool | Unset = UNSET
    endpoint_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_name = self.container_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        account_name = self.account_name

        use_workload_identity = self.use_workload_identity

        workload_identity_enabled = self.workload_identity_enabled

        connection_string_enabled = self.connection_string_enabled

        endpoint_url = self.endpoint_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerName": container_name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if use_workload_identity is not UNSET:
            field_dict["useWorkloadIdentity"] = use_workload_identity
        if workload_identity_enabled is not UNSET:
            field_dict["workloadIdentityEnabled"] = workload_identity_enabled
        if connection_string_enabled is not UNSET:
            field_dict["connectionStringEnabled"] = connection_string_enabled
        if endpoint_url is not UNSET:
            field_dict["endpointUrl"] = endpoint_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_name = d.pop("containerName")

        _type_ = d.pop("type", UNSET)
        type_: FSProviderConfigurationExternalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FSProviderConfigurationExternalType(_type_)

        account_name = d.pop("accountName", UNSET)

        use_workload_identity = d.pop("useWorkloadIdentity", UNSET)

        workload_identity_enabled = d.pop("workloadIdentityEnabled", UNSET)

        connection_string_enabled = d.pop("connectionStringEnabled", UNSET)

        endpoint_url = d.pop("endpointUrl", UNSET)

        fs_provider_azure_config_external = cls(
            container_name=container_name,
            type_=type_,
            account_name=account_name,
            use_workload_identity=use_workload_identity,
            workload_identity_enabled=workload_identity_enabled,
            connection_string_enabled=connection_string_enabled,
            endpoint_url=endpoint_url,
        )

        fs_provider_azure_config_external.additional_properties = d
        return fs_provider_azure_config_external

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
