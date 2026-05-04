# MDEJobInputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**FilesInput**](FilesInput.md) |  | [optional] 
**var_schema** | [**EliseEntitySchemaInput**](EliseEntitySchemaInput.md) |  | [optional] 

## Example

```python
from biolevate_client.models.mde_job_inputs import MDEJobInputs

# TODO update the JSON string below
json = "{}"
# create an instance of MDEJobInputs from a JSON string
mde_job_inputs_instance = MDEJobInputs.from_json(json)
# print the JSON string representation of the object
print(MDEJobInputs.to_json())

# convert the object into a dict
mde_job_inputs_dict = mde_job_inputs_instance.to_dict()
# create an instance of MDEJobInputs from a dict
mde_job_inputs_from_dict = MDEJobInputs.from_dict(mde_job_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


