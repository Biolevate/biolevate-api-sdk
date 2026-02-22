# CreateExtractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**FilesInput**](FilesInput.md) |  | [optional] 
**metas** | [**List[EliseMetaInput]**](EliseMetaInput.md) |  | [optional] 

## Example

```python
from biolevate_client.models.create_extract_request import CreateExtractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExtractRequest from a JSON string
create_extract_request_instance = CreateExtractRequest.from_json(json)
# print the JSON string representation of the object
print(CreateExtractRequest.to_json())

# convert the object into a dict
create_extract_request_dict = create_extract_request_instance.to_dict()
# create an instance of CreateExtractRequest from a dict
create_extract_request_from_dict = CreateExtractRequest.from_dict(create_extract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


