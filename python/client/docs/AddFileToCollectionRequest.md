# AddFileToCollectionRequest

Request to add a file to a collection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | EliseFile ID to add to the collection | 

## Example

```python
from biolevate_client.models.add_file_to_collection_request import AddFileToCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFileToCollectionRequest from a JSON string
add_file_to_collection_request_instance = AddFileToCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(AddFileToCollectionRequest.to_json())

# convert the object into a dict
add_file_to_collection_request_dict = add_file_to_collection_request_instance.to_dict()
# create an instance of AddFileToCollectionRequest from a dict
add_file_to_collection_request_from_dict = AddFileToCollectionRequest.from_dict(add_file_to_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


