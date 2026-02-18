from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elise_file_info_type import EliseFileInfoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_id import FileId
    from ..models.json_node import JsonNode
    from ..models.lib_item_indexation_infos import LibItemIndexationInfos
    from ..models.policy_id import PolicyId
    from ..models.provider_id import ProviderId
    from ..models.user_id import UserId


T = TypeVar("T", bound="EliseFileInfo")


@_attrs_define
class EliseFileInfo:
    """
    Attributes:
        id (FileId | Unset):
        created_time (int | Unset):
        owner (UserId | Unset):
        policy (PolicyId | Unset):
        provider_id (ProviderId | Unset):
        name (str | Unset):
        path (str | Unset):
        size (int | Unset):
        checksum (str | Unset):
        media_type (str | Unset):
        extension (str | Unset):
        indexed (bool | Unset):
        match_computed (bool | Unset):
        display_name (str | Unset):
        db_name (str | Unset):
        last_indexation_infos (LibItemIndexationInfos | Unset):
        owner_first_name (str | Unset):
        owner_last_name (str | Unset):
        owner_email (str | Unset):
        owner_avatar_url (str | Unset):
        provider_name (str | Unset):
        additional_info (JsonNode | Unset):
        description (str | Unset):
        authors (str | Unset):
        title (str | Unset):
        additional_infos (JsonNode | Unset):
        type_ (EliseFileInfoType | Unset):
    """

    id: FileId | Unset = UNSET
    created_time: int | Unset = UNSET
    owner: UserId | Unset = UNSET
    policy: PolicyId | Unset = UNSET
    provider_id: ProviderId | Unset = UNSET
    name: str | Unset = UNSET
    path: str | Unset = UNSET
    size: int | Unset = UNSET
    checksum: str | Unset = UNSET
    media_type: str | Unset = UNSET
    extension: str | Unset = UNSET
    indexed: bool | Unset = UNSET
    match_computed: bool | Unset = UNSET
    display_name: str | Unset = UNSET
    db_name: str | Unset = UNSET
    last_indexation_infos: LibItemIndexationInfos | Unset = UNSET
    owner_first_name: str | Unset = UNSET
    owner_last_name: str | Unset = UNSET
    owner_email: str | Unset = UNSET
    owner_avatar_url: str | Unset = UNSET
    provider_name: str | Unset = UNSET
    additional_info: JsonNode | Unset = UNSET
    description: str | Unset = UNSET
    authors: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_infos: JsonNode | Unset = UNSET
    type_: EliseFileInfoType | Unset = UNSET
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

        provider_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_id, Unset):
            provider_id = self.provider_id.to_dict()

        name = self.name

        path = self.path

        size = self.size

        checksum = self.checksum

        media_type = self.media_type

        extension = self.extension

        indexed = self.indexed

        match_computed = self.match_computed

        display_name = self.display_name

        db_name = self.db_name

        last_indexation_infos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_indexation_infos, Unset):
            last_indexation_infos = self.last_indexation_infos.to_dict()

        owner_first_name = self.owner_first_name

        owner_last_name = self.owner_last_name

        owner_email = self.owner_email

        owner_avatar_url = self.owner_avatar_url

        provider_name = self.provider_name

        additional_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = self.additional_info.to_dict()

        description = self.description

        authors = self.authors

        title = self.title

        additional_infos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_infos, Unset):
            additional_infos = self.additional_infos.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if size is not UNSET:
            field_dict["size"] = size
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if extension is not UNSET:
            field_dict["extension"] = extension
        if indexed is not UNSET:
            field_dict["indexed"] = indexed
        if match_computed is not UNSET:
            field_dict["matchComputed"] = match_computed
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if db_name is not UNSET:
            field_dict["dbName"] = db_name
        if last_indexation_infos is not UNSET:
            field_dict["lastIndexationInfos"] = last_indexation_infos
        if owner_first_name is not UNSET:
            field_dict["ownerFirstName"] = owner_first_name
        if owner_last_name is not UNSET:
            field_dict["ownerLastName"] = owner_last_name
        if owner_email is not UNSET:
            field_dict["ownerEmail"] = owner_email
        if owner_avatar_url is not UNSET:
            field_dict["ownerAvatarUrl"] = owner_avatar_url
        if provider_name is not UNSET:
            field_dict["providerName"] = provider_name
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info
        if description is not UNSET:
            field_dict["description"] = description
        if authors is not UNSET:
            field_dict["authors"] = authors
        if title is not UNSET:
            field_dict["title"] = title
        if additional_infos is not UNSET:
            field_dict["additionalInfos"] = additional_infos
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_id import FileId
        from ..models.json_node import JsonNode
        from ..models.lib_item_indexation_infos import LibItemIndexationInfos
        from ..models.policy_id import PolicyId
        from ..models.provider_id import ProviderId
        from ..models.user_id import UserId

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: FileId | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = FileId.from_dict(_id)

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

        _provider_id = d.pop("providerId", UNSET)
        provider_id: ProviderId | Unset
        if isinstance(_provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = ProviderId.from_dict(_provider_id)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        size = d.pop("size", UNSET)

        checksum = d.pop("checksum", UNSET)

        media_type = d.pop("mediaType", UNSET)

        extension = d.pop("extension", UNSET)

        indexed = d.pop("indexed", UNSET)

        match_computed = d.pop("matchComputed", UNSET)

        display_name = d.pop("displayName", UNSET)

        db_name = d.pop("dbName", UNSET)

        _last_indexation_infos = d.pop("lastIndexationInfos", UNSET)
        last_indexation_infos: LibItemIndexationInfos | Unset
        if isinstance(_last_indexation_infos, Unset):
            last_indexation_infos = UNSET
        else:
            last_indexation_infos = LibItemIndexationInfos.from_dict(_last_indexation_infos)

        owner_first_name = d.pop("ownerFirstName", UNSET)

        owner_last_name = d.pop("ownerLastName", UNSET)

        owner_email = d.pop("ownerEmail", UNSET)

        owner_avatar_url = d.pop("ownerAvatarUrl", UNSET)

        provider_name = d.pop("providerName", UNSET)

        _additional_info = d.pop("additionalInfo", UNSET)
        additional_info: JsonNode | Unset
        if isinstance(_additional_info, Unset):
            additional_info = UNSET
        else:
            additional_info = JsonNode.from_dict(_additional_info)

        description = d.pop("description", UNSET)

        authors = d.pop("authors", UNSET)

        title = d.pop("title", UNSET)

        _additional_infos = d.pop("additionalInfos", UNSET)
        additional_infos: JsonNode | Unset
        if isinstance(_additional_infos, Unset):
            additional_infos = UNSET
        else:
            additional_infos = JsonNode.from_dict(_additional_infos)

        _type_ = d.pop("type", UNSET)
        type_: EliseFileInfoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EliseFileInfoType(_type_)

        elise_file_info = cls(
            id=id,
            created_time=created_time,
            owner=owner,
            policy=policy,
            provider_id=provider_id,
            name=name,
            path=path,
            size=size,
            checksum=checksum,
            media_type=media_type,
            extension=extension,
            indexed=indexed,
            match_computed=match_computed,
            display_name=display_name,
            db_name=db_name,
            last_indexation_infos=last_indexation_infos,
            owner_first_name=owner_first_name,
            owner_last_name=owner_last_name,
            owner_email=owner_email,
            owner_avatar_url=owner_avatar_url,
            provider_name=provider_name,
            additional_info=additional_info,
            description=description,
            authors=authors,
            title=title,
            additional_infos=additional_infos,
            type_=type_,
        )

        elise_file_info.additional_properties = d
        return elise_file_info

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
