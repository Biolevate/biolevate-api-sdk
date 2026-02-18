from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_id import AnnotationId
    from ..models.elise_ontology_meta_meta_value import EliseOntologyMetaMetaValue


T = TypeVar("T", bound="EliseOntologyMeta")


@_attrs_define
class EliseOntologyMeta:
    """
    Attributes:
        explanation (str | Unset):
        annotation_ids (list[AnnotationId] | Unset):
        meta_name (str | Unset):
        meta_value (EliseOntologyMetaMetaValue | Unset):
    """

    explanation: str | Unset = UNSET
    annotation_ids: list[AnnotationId] | Unset = UNSET
    meta_name: str | Unset = UNSET
    meta_value: EliseOntologyMetaMetaValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        explanation = self.explanation

        annotation_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.annotation_ids, Unset):
            annotation_ids = []
            for annotation_ids_item_data in self.annotation_ids:
                annotation_ids_item = annotation_ids_item_data.to_dict()
                annotation_ids.append(annotation_ids_item)

        meta_name = self.meta_name

        meta_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_value, Unset):
            meta_value = self.meta_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if annotation_ids is not UNSET:
            field_dict["annotationIds"] = annotation_ids
        if meta_name is not UNSET:
            field_dict["metaName"] = meta_name
        if meta_value is not UNSET:
            field_dict["metaValue"] = meta_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_id import AnnotationId
        from ..models.elise_ontology_meta_meta_value import EliseOntologyMetaMetaValue

        d = dict(src_dict)
        explanation = d.pop("explanation", UNSET)

        _annotation_ids = d.pop("annotationIds", UNSET)
        annotation_ids: list[AnnotationId] | Unset = UNSET
        if _annotation_ids is not UNSET:
            annotation_ids = []
            for annotation_ids_item_data in _annotation_ids:
                annotation_ids_item = AnnotationId.from_dict(annotation_ids_item_data)

                annotation_ids.append(annotation_ids_item)

        meta_name = d.pop("metaName", UNSET)

        _meta_value = d.pop("metaValue", UNSET)
        meta_value: EliseOntologyMetaMetaValue | Unset
        if isinstance(_meta_value, Unset):
            meta_value = UNSET
        else:
            meta_value = EliseOntologyMetaMetaValue.from_dict(_meta_value)

        elise_ontology_meta = cls(
            explanation=explanation,
            annotation_ids=annotation_ids,
            meta_name=meta_name,
            meta_value=meta_value,
        )

        elise_ontology_meta.additional_properties = d
        return elise_ontology_meta

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
