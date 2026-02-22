# ExtractJobOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EliseMetaResult]**](EliseMetaResult.md) |  | [optional] 

## Example

```python
from biolevate_client.models.extract_job_outputs import ExtractJobOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractJobOutputs from a JSON string
extract_job_outputs_instance = ExtractJobOutputs.from_json(json)
# print the JSON string representation of the object
print(ExtractJobOutputs.to_json())

# convert the object into a dict
extract_job_outputs_dict = extract_job_outputs_instance.to_dict()
# create an instance of ExtractJobOutputs from a dict
extract_job_outputs_from_dict = ExtractJobOutputs.from_dict(extract_job_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


