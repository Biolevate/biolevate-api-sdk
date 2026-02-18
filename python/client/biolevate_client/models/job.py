from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """
    Attributes:
        job_id (str | Unset):
        status (JobStatus | Unset):
        task_type (str | Unset):
        created_time (int | Unset):
        execution_time (float | Unset):
        error_message (str | Unset):
        name (str | Unset):
        archived (bool | Unset):
    """

    job_id: str | Unset = UNSET
    status: JobStatus | Unset = UNSET
    task_type: str | Unset = UNSET
    created_time: int | Unset = UNSET
    execution_time: float | Unset = UNSET
    error_message: str | Unset = UNSET
    name: str | Unset = UNSET
    archived: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        task_type = self.task_type

        created_time = self.created_time

        execution_time = self.execution_time

        error_message = self.error_message

        name = self.name

        archived = self.archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if status is not UNSET:
            field_dict["status"] = status
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if execution_time is not UNSET:
            field_dict["executionTime"] = execution_time
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if name is not UNSET:
            field_dict["name"] = name
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        task_type = d.pop("taskType", UNSET)

        created_time = d.pop("createdTime", UNSET)

        execution_time = d.pop("executionTime", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        name = d.pop("name", UNSET)

        archived = d.pop("archived", UNSET)

        job = cls(
            job_id=job_id,
            status=status,
            task_type=task_type,
            created_time=created_time,
            execution_time=execution_time,
            error_message=error_message,
            name=name,
            archived=archived,
        )

        job.additional_properties = d
        return job

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
