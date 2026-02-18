from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.elise_meta_input import EliseMetaInput
    from ..models.files_input import FilesInput


T = TypeVar("T", bound="ExtractJobInputs")


@_attrs_define
class ExtractJobInputs:
    """
    Attributes:
        files (FilesInput | Unset):
        metas (list[EliseMetaInput] | Unset):
    """

    files: FilesInput | Unset = UNSET
    metas: list[EliseMetaInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        metas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metas, Unset):
            metas = []
            for metas_item_data in self.metas:
                metas_item = metas_item_data.to_dict()
                metas.append(metas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if metas is not UNSET:
            field_dict["metas"] = metas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.elise_meta_input import EliseMetaInput
        from ..models.files_input import FilesInput

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: FilesInput | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = FilesInput.from_dict(_files)

        _metas = d.pop("metas", UNSET)
        metas: list[EliseMetaInput] | Unset = UNSET
        if _metas is not UNSET:
            metas = []
            for metas_item_data in _metas:
                metas_item = EliseMetaInput.from_dict(metas_item_data)

                metas.append(metas_item)

        extract_job_inputs = cls(
            files=files,
            metas=metas,
        )

        extract_job_inputs.additional_properties = d
        return extract_job_inputs

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
