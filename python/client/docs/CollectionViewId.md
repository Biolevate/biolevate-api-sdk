# CollectionViewId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.collection_view_id import CollectionViewId

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionViewId from a JSON string
collection_view_id_instance = CollectionViewId.from_json(json)
# print the JSON string representation of the object
print(CollectionViewId.to_json())

# convert the object into a dict
collection_view_id_dict = collection_view_id_instance.to_dict()
# create an instance of CollectionViewId from a dict
collection_view_id_from_dict = CollectionViewId.from_dict(collection_view_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


