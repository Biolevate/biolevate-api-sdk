from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fs_provider_configuration_external_type import FSProviderConfigurationExternalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FSProviderLeanearConfigExternal")


@_attrs_define
class FSProviderLeanearConfigExternal:
    """
    Attributes:
        project_id (str):
        bucket_name (str):
        default_policy (str):
        type_ (FSProviderConfigurationExternalType | Unset):
    """

    project_id: str
    bucket_name: str
    default_policy: str
    type_: FSProviderConfigurationExternalType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        bucket_name = self.bucket_name

        default_policy = self.default_policy

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "bucketName": bucket_name,
                "defaultPolicy": default_policy,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        bucket_name = d.pop("bucketName")

        default_policy = d.pop("defaultPolicy")

        _type_ = d.pop("type", UNSET)
        type_: FSProviderConfigurationExternalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FSProviderConfigurationExternalType(_type_)

        fs_provider_leanear_config_external = cls(
            project_id=project_id,
            bucket_name=bucket_name,
            default_policy=default_policy,
            type_=type_,
        )

        fs_provider_leanear_config_external.additional_properties = d
        return fs_provider_leanear_config_external

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
