from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.elise_question_input import EliseQuestionInput
    from ..models.files_input import FilesInput


T = TypeVar("T", bound="QAJobInputs")


@_attrs_define
class QAJobInputs:
    """
    Attributes:
        files (FilesInput | Unset):
        questions (list[EliseQuestionInput] | Unset):
    """

    files: FilesInput | Unset = UNSET
    questions: list[EliseQuestionInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        questions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.questions, Unset):
            questions = []
            for questions_item_data in self.questions:
                questions_item = questions_item_data.to_dict()
                questions.append(questions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.elise_question_input import EliseQuestionInput
        from ..models.files_input import FilesInput

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: FilesInput | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = FilesInput.from_dict(_files)

        _questions = d.pop("questions", UNSET)
        questions: list[EliseQuestionInput] | Unset = UNSET
        if _questions is not UNSET:
            questions = []
            for questions_item_data in _questions:
                questions_item = EliseQuestionInput.from_dict(questions_item_data)

                questions.append(questions_item)

        qa_job_inputs = cls(
            files=files,
            questions=questions,
        )

        qa_job_inputs.additional_properties = d
        return qa_job_inputs

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
