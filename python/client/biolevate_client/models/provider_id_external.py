from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_id_external_entity_type import ProviderIdExternalEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderIdExternal")


@_attrs_define
class ProviderIdExternal:
    """
    Attributes:
        id (UUID | Unset):
        entity_type (ProviderIdExternalEntityType | Unset):
    """

    id: UUID | Unset = UNSET
    entity_type: ProviderIdExternalEntityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: ProviderIdExternalEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = ProviderIdExternalEntityType(_entity_type)

        provider_id_external = cls(
            id=id,
            entity_type=entity_type,
        )

        provider_id_external.additional_properties = d
        return provider_id_external

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
