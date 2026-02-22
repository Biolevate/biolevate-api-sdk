# EliseFileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**FileId**](FileId.md) |  | [optional] 
**created_time** | **int** |  | [optional] 
**owner** | [**UserId**](UserId.md) |  | [optional] 
**policy** | [**PolicyId**](PolicyId.md) |  | [optional] 
**provider_id** | [**ProviderId**](ProviderId.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**checksum** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**extension** | **str** |  | [optional] 
**indexed** | **bool** |  | [optional] 
**match_computed** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**db_name** | **str** |  | [optional] 
**last_indexation_infos** | [**LibItemIndexationInfos**](LibItemIndexationInfos.md) |  | [optional] 
**owner_first_name** | **str** |  | [optional] 
**owner_last_name** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**owner_avatar_url** | **str** |  | [optional] 
**provider_name** | **str** |  | [optional] 
**additional_info** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**authors** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**additional_infos** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_file_info import EliseFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EliseFileInfo from a JSON string
elise_file_info_instance = EliseFileInfo.from_json(json)
# print the JSON string representation of the object
print(EliseFileInfo.to_json())

# convert the object into a dict
elise_file_info_dict = elise_file_info_instance.to_dict()
# create an instance of EliseFileInfo from a dict
elise_file_info_from_dict = EliseFileInfo.from_dict(elise_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


