# CollectionId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.collection_id import CollectionId

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionId from a JSON string
collection_id_instance = CollectionId.from_json(json)
# print the JSON string representation of the object
print(CollectionId.to_json())

# convert the object into a dict
collection_id_dict = collection_id_instance.to_dict()
# create an instance of CollectionId from a dict
collection_id_from_dict = CollectionId.from_dict(collection_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


