# EliseCollectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**CollectionId**](CollectionId.md) |  | [optional] 
**created_time** | **int** |  | [optional] 
**owner** | [**UserId**](UserId.md) |  | [optional] 
**policy** | [**PolicyId**](PolicyId.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**owner_first_name** | **str** |  | [optional] 
**owner_last_name** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**owner_avatar_url** | **str** |  | [optional] 
**files_count** | **int** |  | [optional] 
**derived_from_collection_id** | [**CollectionId**](CollectionId.md) |  | [optional] 
**derived_from_collection_name** | **str** |  | [optional] 
**derived_from_view_id** | [**CollectionViewId**](CollectionViewId.md) |  | [optional] 
**derived_from_view_name** | **str** |  | [optional] 
**chained** | **bool** |  | [optional] 
**derived_to_collection_id** | [**CollectionId**](CollectionId.md) |  | [optional] 
**derived_to_collection_name** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_collection_info import EliseCollectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EliseCollectionInfo from a JSON string
elise_collection_info_instance = EliseCollectionInfo.from_json(json)
# print the JSON string representation of the object
print(EliseCollectionInfo.to_json())

# convert the object into a dict
elise_collection_info_dict = elise_collection_info_instance.to_dict()
# create an instance of EliseCollectionInfo from a dict
elise_collection_info_from_dict = EliseCollectionInfo.from_dict(elise_collection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


