# ExtractJobInputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**FilesInput**](FilesInput.md) |  | [optional] 
**metas** | [**List[EliseMetaInput]**](EliseMetaInput.md) |  | [optional] 

## Example

```python
from biolevate_client.models.extract_job_inputs import ExtractJobInputs

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractJobInputs from a JSON string
extract_job_inputs_instance = ExtractJobInputs.from_json(json)
# print the JSON string representation of the object
print(ExtractJobInputs.to_json())

# convert the object into a dict
extract_job_inputs_dict = extract_job_inputs_instance.to_dict()
# create an instance of ExtractJobInputs from a dict
extract_job_inputs_from_dict = ExtractJobInputs.from_dict(extract_job_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


