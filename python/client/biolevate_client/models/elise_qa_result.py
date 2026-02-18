from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_id import AnnotationId


T = TypeVar("T", bound="EliseQAResult")


@_attrs_define
class EliseQAResult:
    """
    Attributes:
        explanation (str | Unset):
        sourced_content (str | Unset):
        reference_ids (list[AnnotationId] | Unset):
        question (str | Unset):
        expected_answer (str | Unset):
        validity_explaination (str | Unset):
        input_question_ids (list[str] | Unset):
        answer_validity (float | Unset):
        raw_value (str | Unset):
    """

    explanation: str | Unset = UNSET
    sourced_content: str | Unset = UNSET
    reference_ids: list[AnnotationId] | Unset = UNSET
    question: str | Unset = UNSET
    expected_answer: str | Unset = UNSET
    validity_explaination: str | Unset = UNSET
    input_question_ids: list[str] | Unset = UNSET
    answer_validity: float | Unset = UNSET
    raw_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        explanation = self.explanation

        sourced_content = self.sourced_content

        reference_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reference_ids, Unset):
            reference_ids = []
            for reference_ids_item_data in self.reference_ids:
                reference_ids_item = reference_ids_item_data.to_dict()
                reference_ids.append(reference_ids_item)

        question = self.question

        expected_answer = self.expected_answer

        validity_explaination = self.validity_explaination

        input_question_ids: list[str] | Unset = UNSET
        if not isinstance(self.input_question_ids, Unset):
            input_question_ids = self.input_question_ids

        answer_validity = self.answer_validity

        raw_value = self.raw_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if sourced_content is not UNSET:
            field_dict["sourcedContent"] = sourced_content
        if reference_ids is not UNSET:
            field_dict["referenceIds"] = reference_ids
        if question is not UNSET:
            field_dict["question"] = question
        if expected_answer is not UNSET:
            field_dict["expectedAnswer"] = expected_answer
        if validity_explaination is not UNSET:
            field_dict["validityExplaination"] = validity_explaination
        if input_question_ids is not UNSET:
            field_dict["inputQuestionIds"] = input_question_ids
        if answer_validity is not UNSET:
            field_dict["answerValidity"] = answer_validity
        if raw_value is not UNSET:
            field_dict["rawValue"] = raw_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_id import AnnotationId

        d = dict(src_dict)
        explanation = d.pop("explanation", UNSET)

        sourced_content = d.pop("sourcedContent", UNSET)

        _reference_ids = d.pop("referenceIds", UNSET)
        reference_ids: list[AnnotationId] | Unset = UNSET
        if _reference_ids is not UNSET:
            reference_ids = []
            for reference_ids_item_data in _reference_ids:
                reference_ids_item = AnnotationId.from_dict(reference_ids_item_data)

                reference_ids.append(reference_ids_item)

        question = d.pop("question", UNSET)

        expected_answer = d.pop("expectedAnswer", UNSET)

        validity_explaination = d.pop("validityExplaination", UNSET)

        input_question_ids = cast(list[str], d.pop("inputQuestionIds", UNSET))

        answer_validity = d.pop("answerValidity", UNSET)

        raw_value = d.pop("rawValue", UNSET)

        elise_qa_result = cls(
            explanation=explanation,
            sourced_content=sourced_content,
            reference_ids=reference_ids,
            question=question,
            expected_answer=expected_answer,
            validity_explaination=validity_explaination,
            input_question_ids=input_question_ids,
            answer_validity=answer_validity,
            raw_value=raw_value,
        )

        elise_qa_result.additional_properties = d
        return elise_qa_result

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
