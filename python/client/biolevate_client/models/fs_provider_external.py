from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fs_provider_external_type import FSProviderExternalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_provider_azure_config_external import FSProviderAzureConfigExternal
    from ..models.fs_provider_gcs_config_external import FSProviderGCSConfigExternal
    from ..models.fs_provider_leanear_config_external import FSProviderLeanearConfigExternal
    from ..models.fs_provider_local_config_external import FSProviderLocalConfigExternal
    from ..models.fs_provider_s3_config_external import FSProviderS3ConfigExternal
    from ..models.fs_provider_sharepoint_online_config_external import FSProviderSharepointOnlineConfigExternal
    from ..models.policy_id_external import PolicyIdExternal
    from ..models.provider_id_external import ProviderIdExternal
    from ..models.user_id_external import UserIdExternal


T = TypeVar("T", bound="FSProviderExternal")


@_attrs_define
class FSProviderExternal:
    """
    Attributes:
        id (ProviderIdExternal | Unset):
        created_time (int | Unset):
        owner (UserIdExternal | Unset):
        policy (PolicyIdExternal | Unset):
        name (str | Unset):
        icon (str | Unset):
        config (FSProviderAzureConfigExternal | FSProviderGCSConfigExternal | FSProviderLeanearConfigExternal |
            FSProviderLocalConfigExternal | FSProviderS3ConfigExternal | FSProviderSharepointOnlineConfigExternal | Unset):
        type_ (FSProviderExternalType | Unset):
        system (bool | Unset):
    """

    id: ProviderIdExternal | Unset = UNSET
    created_time: int | Unset = UNSET
    owner: UserIdExternal | Unset = UNSET
    policy: PolicyIdExternal | Unset = UNSET
    name: str | Unset = UNSET
    icon: str | Unset = UNSET
    config: (
        FSProviderAzureConfigExternal
        | FSProviderGCSConfigExternal
        | FSProviderLeanearConfigExternal
        | FSProviderLocalConfigExternal
        | FSProviderS3ConfigExternal
        | FSProviderSharepointOnlineConfigExternal
        | Unset
    ) = UNSET
    type_: FSProviderExternalType | Unset = UNSET
    system: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_provider_azure_config_external import FSProviderAzureConfigExternal
        from ..models.fs_provider_gcs_config_external import FSProviderGCSConfigExternal
        from ..models.fs_provider_leanear_config_external import FSProviderLeanearConfigExternal
        from ..models.fs_provider_local_config_external import FSProviderLocalConfigExternal
        from ..models.fs_provider_s3_config_external import FSProviderS3ConfigExternal

        id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        created_time = self.created_time

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        name = self.name

        icon = self.icon

        config: dict[str, Any] | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, FSProviderAzureConfigExternal):
            config = self.config.to_dict()
        elif isinstance(self.config, FSProviderGCSConfigExternal):
            config = self.config.to_dict()
        elif isinstance(self.config, FSProviderLeanearConfigExternal):
            config = self.config.to_dict()
        elif isinstance(self.config, FSProviderLocalConfigExternal):
            config = self.config.to_dict()
        elif isinstance(self.config, FSProviderS3ConfigExternal):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        system = self.system

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if owner is not UNSET:
            field_dict["owner"] = owner
        if policy is not UNSET:
            field_dict["policy"] = policy
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if config is not UNSET:
            field_dict["config"] = config
        if type_ is not UNSET:
            field_dict["type"] = type_
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_provider_azure_config_external import FSProviderAzureConfigExternal
        from ..models.fs_provider_gcs_config_external import FSProviderGCSConfigExternal
        from ..models.fs_provider_leanear_config_external import FSProviderLeanearConfigExternal
        from ..models.fs_provider_local_config_external import FSProviderLocalConfigExternal
        from ..models.fs_provider_s3_config_external import FSProviderS3ConfigExternal
        from ..models.fs_provider_sharepoint_online_config_external import FSProviderSharepointOnlineConfigExternal
        from ..models.policy_id_external import PolicyIdExternal
        from ..models.provider_id_external import ProviderIdExternal
        from ..models.user_id_external import UserIdExternal

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: ProviderIdExternal | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = ProviderIdExternal.from_dict(_id)

        created_time = d.pop("createdTime", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: UserIdExternal | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = UserIdExternal.from_dict(_owner)

        _policy = d.pop("policy", UNSET)
        policy: PolicyIdExternal | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = PolicyIdExternal.from_dict(_policy)

        name = d.pop("name", UNSET)

        icon = d.pop("icon", UNSET)

        def _parse_config(
            data: object,
        ) -> (
            FSProviderAzureConfigExternal
            | FSProviderGCSConfigExternal
            | FSProviderLeanearConfigExternal
            | FSProviderLocalConfigExternal
            | FSProviderS3ConfigExternal
            | FSProviderSharepointOnlineConfigExternal
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = FSProviderAzureConfigExternal.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = FSProviderGCSConfigExternal.from_dict(data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_2 = FSProviderLeanearConfigExternal.from_dict(data)

                return config_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_3 = FSProviderLocalConfigExternal.from_dict(data)

                return config_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_4 = FSProviderS3ConfigExternal.from_dict(data)

                return config_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type_5 = FSProviderSharepointOnlineConfigExternal.from_dict(data)

            return config_type_5

        config = _parse_config(d.pop("config", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: FSProviderExternalType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FSProviderExternalType(_type_)

        system = d.pop("system", UNSET)

        fs_provider_external = cls(
            id=id,
            created_time=created_time,
            owner=owner,
            policy=policy,
            name=name,
            icon=icon,
            config=config,
            type_=type_,
            system=system,
        )

        fs_provider_external.additional_properties = d
        return fs_provider_external

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
