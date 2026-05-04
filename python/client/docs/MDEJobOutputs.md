# MDEJobOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_extraction** | [**EliseEntityExtractionResult**](EliseEntityExtractionResult.md) |  | [optional] 

## Example

```python
from biolevate_client.models.mde_job_outputs import MDEJobOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of MDEJobOutputs from a JSON string
mde_job_outputs_instance = MDEJobOutputs.from_json(json)
# print the JSON string representation of the object
print(MDEJobOutputs.to_json())

# convert the object into a dict
mde_job_outputs_dict = mde_job_outputs_instance.to_dict()
# create an instance of MDEJobOutputs from a dict
mde_job_outputs_from_dict = MDEJobOutputs.from_dict(mde_job_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


