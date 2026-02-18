from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_id import CollectionId
    from ..models.collection_view_id import CollectionViewId
    from ..models.policy_id import PolicyId
    from ..models.user_id import UserId


T = TypeVar("T", bound="EliseCollectionInfo")


@_attrs_define
class EliseCollectionInfo:
    """
    Attributes:
        id (CollectionId | Unset):
        created_time (int | Unset):
        owner (UserId | Unset):
        policy (PolicyId | Unset):
        name (str | Unset):
        description (str | Unset):
        icon (str | Unset):
        owner_first_name (str | Unset):
        owner_last_name (str | Unset):
        owner_email (str | Unset):
        owner_avatar_url (str | Unset):
        files_count (int | Unset):
        derived_from_collection_id (CollectionId | Unset):
        derived_from_collection_name (str | Unset):
        derived_from_view_id (CollectionViewId | Unset):
        derived_from_view_name (str | Unset):
        chained (bool | Unset):
        derived_to_collection_id (CollectionId | Unset):
        derived_to_collection_name (str | Unset):
    """

    id: CollectionId | Unset = UNSET
    created_time: int | Unset = UNSET
    owner: UserId | Unset = UNSET
    policy: PolicyId | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    owner_first_name: str | Unset = UNSET
    owner_last_name: str | Unset = UNSET
    owner_email: str | Unset = UNSET
    owner_avatar_url: str | Unset = UNSET
    files_count: int | Unset = UNSET
    derived_from_collection_id: CollectionId | Unset = UNSET
    derived_from_collection_name: str | Unset = UNSET
    derived_from_view_id: CollectionViewId | Unset = UNSET
    derived_from_view_name: str | Unset = UNSET
    chained: bool | Unset = UNSET
    derived_to_collection_id: CollectionId | Unset = UNSET
    derived_to_collection_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        description = self.description

        icon = self.icon

        owner_first_name = self.owner_first_name

        owner_last_name = self.owner_last_name

        owner_email = self.owner_email

        owner_avatar_url = self.owner_avatar_url

        files_count = self.files_count

        derived_from_collection_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_from_collection_id, Unset):
            derived_from_collection_id = self.derived_from_collection_id.to_dict()

        derived_from_collection_name = self.derived_from_collection_name

        derived_from_view_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_from_view_id, Unset):
            derived_from_view_id = self.derived_from_view_id.to_dict()

        derived_from_view_name = self.derived_from_view_name

        chained = self.chained

        derived_to_collection_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_to_collection_id, Unset):
            derived_to_collection_id = self.derived_to_collection_id.to_dict()

        derived_to_collection_name = self.derived_to_collection_name

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
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if owner_first_name is not UNSET:
            field_dict["ownerFirstName"] = owner_first_name
        if owner_last_name is not UNSET:
            field_dict["ownerLastName"] = owner_last_name
        if owner_email is not UNSET:
            field_dict["ownerEmail"] = owner_email
        if owner_avatar_url is not UNSET:
            field_dict["ownerAvatarUrl"] = owner_avatar_url
        if files_count is not UNSET:
            field_dict["filesCount"] = files_count
        if derived_from_collection_id is not UNSET:
            field_dict["derivedFromCollectionId"] = derived_from_collection_id
        if derived_from_collection_name is not UNSET:
            field_dict["derivedFromCollectionName"] = derived_from_collection_name
        if derived_from_view_id is not UNSET:
            field_dict["derivedFromViewId"] = derived_from_view_id
        if derived_from_view_name is not UNSET:
            field_dict["derivedFromViewName"] = derived_from_view_name
        if chained is not UNSET:
            field_dict["chained"] = chained
        if derived_to_collection_id is not UNSET:
            field_dict["derivedToCollectionId"] = derived_to_collection_id
        if derived_to_collection_name is not UNSET:
            field_dict["derivedToCollectionName"] = derived_to_collection_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_id import CollectionId
        from ..models.collection_view_id import CollectionViewId
        from ..models.policy_id import PolicyId
        from ..models.user_id import UserId

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: CollectionId | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = CollectionId.from_dict(_id)

        created_time = d.pop("createdTime", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: UserId | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = UserId.from_dict(_owner)

        _policy = d.pop("policy", UNSET)
        policy: PolicyId | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = PolicyId.from_dict(_policy)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        owner_first_name = d.pop("ownerFirstName", UNSET)

        owner_last_name = d.pop("ownerLastName", UNSET)

        owner_email = d.pop("ownerEmail", UNSET)

        owner_avatar_url = d.pop("ownerAvatarUrl", UNSET)

        files_count = d.pop("filesCount", UNSET)

        _derived_from_collection_id = d.pop("derivedFromCollectionId", UNSET)
        derived_from_collection_id: CollectionId | Unset
        if isinstance(_derived_from_collection_id, Unset):
            derived_from_collection_id = UNSET
        else:
            derived_from_collection_id = CollectionId.from_dict(_derived_from_collection_id)

        derived_from_collection_name = d.pop("derivedFromCollectionName", UNSET)

        _derived_from_view_id = d.pop("derivedFromViewId", UNSET)
        derived_from_view_id: CollectionViewId | Unset
        if isinstance(_derived_from_view_id, Unset):
            derived_from_view_id = UNSET
        else:
            derived_from_view_id = CollectionViewId.from_dict(_derived_from_view_id)

        derived_from_view_name = d.pop("derivedFromViewName", UNSET)

        chained = d.pop("chained", UNSET)

        _derived_to_collection_id = d.pop("derivedToCollectionId", UNSET)
        derived_to_collection_id: CollectionId | Unset
        if isinstance(_derived_to_collection_id, Unset):
            derived_to_collection_id = UNSET
        else:
            derived_to_collection_id = CollectionId.from_dict(_derived_to_collection_id)

        derived_to_collection_name = d.pop("derivedToCollectionName", UNSET)

        elise_collection_info = cls(
            id=id,
            created_time=created_time,
            owner=owner,
            policy=policy,
            name=name,
            description=description,
            icon=icon,
            owner_first_name=owner_first_name,
            owner_last_name=owner_last_name,
            owner_email=owner_email,
            owner_avatar_url=owner_avatar_url,
            files_count=files_count,
            derived_from_collection_id=derived_from_collection_id,
            derived_from_collection_name=derived_from_collection_name,
            derived_from_view_id=derived_from_view_id,
            derived_from_view_name=derived_from_view_name,
            chained=chained,
            derived_to_collection_id=derived_to_collection_id,
            derived_to_collection_name=derived_to_collection_name,
        )

        elise_collection_info.additional_properties = d
        return elise_collection_info

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
