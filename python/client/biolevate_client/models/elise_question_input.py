from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expected_answer_type_dto import ExpectedAnswerTypeDto


T = TypeVar("T", bound="EliseQuestionInput")


@_attrs_define
class EliseQuestionInput:
    """
    Attributes:
        id (str | Unset):
        question (str | Unset):
        answer_type (ExpectedAnswerTypeDto | Unset):
        guidelines (str | Unset):
        expected_answer (str | Unset):
        input_question_ids (list[str] | Unset):
    """

    id: str | Unset = UNSET
    question: str | Unset = UNSET
    answer_type: ExpectedAnswerTypeDto | Unset = UNSET
    guidelines: str | Unset = UNSET
    expected_answer: str | Unset = UNSET
    input_question_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        question = self.question

        answer_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.answer_type, Unset):
            answer_type = self.answer_type.to_dict()

        guidelines = self.guidelines

        expected_answer = self.expected_answer

        input_question_ids: list[str] | Unset = UNSET
        if not isinstance(self.input_question_ids, Unset):
            input_question_ids = self.input_question_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if question is not UNSET:
            field_dict["question"] = question
        if answer_type is not UNSET:
            field_dict["answerType"] = answer_type
        if guidelines is not UNSET:
            field_dict["guidelines"] = guidelines
        if expected_answer is not UNSET:
            field_dict["expectedAnswer"] = expected_answer
        if input_question_ids is not UNSET:
            field_dict["inputQuestionIds"] = input_question_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expected_answer_type_dto import ExpectedAnswerTypeDto

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        question = d.pop("question", UNSET)

        _answer_type = d.pop("answerType", UNSET)
        answer_type: ExpectedAnswerTypeDto | Unset
        if isinstance(_answer_type, Unset):
            answer_type = UNSET
        else:
            answer_type = ExpectedAnswerTypeDto.from_dict(_answer_type)

        guidelines = d.pop("guidelines", UNSET)

        expected_answer = d.pop("expectedAnswer", UNSET)

        input_question_ids = cast(list[str], d.pop("inputQuestionIds", UNSET))

        elise_question_input = cls(
            id=id,
            question=question,
            answer_type=answer_type,
            guidelines=guidelines,
            expected_answer=expected_answer,
            input_question_ids=input_question_ids,
        )

        elise_question_input.additional_properties = d
        return elise_question_input

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
