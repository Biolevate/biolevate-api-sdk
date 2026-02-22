# UpdateCollectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.update_collection_request import UpdateCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCollectionRequest from a JSON string
update_collection_request_instance = UpdateCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCollectionRequest.to_json())

# convert the object into a dict
update_collection_request_dict = update_collection_request_instance.to_dict()
# create an instance of UpdateCollectionRequest from a dict
update_collection_request_from_dict = UpdateCollectionRequest.from_dict(update_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


