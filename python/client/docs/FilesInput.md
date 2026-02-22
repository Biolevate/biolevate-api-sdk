# FilesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[str]** |  | [optional] 
**collection_ids** | **List[str]** |  | [optional] 

## Example

```python
from biolevate_client.models.files_input import FilesInput

# TODO update the JSON string below
json = "{}"
# create an instance of FilesInput from a JSON string
files_input_instance = FilesInput.from_json(json)
# print the JSON string representation of the object
print(FilesInput.to_json())

# convert the object into a dict
files_input_dict = files_input_instance.to_dict()
# create an instance of FilesInput from a dict
files_input_from_dict = FilesInput.from_dict(files_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


