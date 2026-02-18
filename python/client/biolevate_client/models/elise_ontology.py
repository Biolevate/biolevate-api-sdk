from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.elise_ontology_metas import EliseOntologyMetas
    from ..models.entity_id import EntityId


T = TypeVar("T", bound="EliseOntology")


@_attrs_define
class EliseOntology:
    """
    Attributes:
        concept_id (EntityId):
        name (str):
        metas (EliseOntologyMetas | Unset):
    """

    concept_id: EntityId
    name: str
    metas: EliseOntologyMetas | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concept_id = self.concept_id.to_dict()

        name = self.name

        metas: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metas, Unset):
            metas = self.metas.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conceptId": concept_id,
                "name": name,
            }
        )
        if metas is not UNSET:
            field_dict["metas"] = metas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.elise_ontology_metas import EliseOntologyMetas
        from ..models.entity_id import EntityId

        d = dict(src_dict)
        concept_id = EntityId.from_dict(d.pop("conceptId"))

        name = d.pop("name")

        _metas = d.pop("metas", UNSET)
        metas: EliseOntologyMetas | Unset
        if isinstance(_metas, Unset):
            metas = UNSET
        else:
            metas = EliseOntologyMetas.from_dict(_metas)

        elise_ontology = cls(
            concept_id=concept_id,
            name=name,
            metas=metas,
        )

        elise_ontology.additional_properties = d
        return elise_ontology

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
