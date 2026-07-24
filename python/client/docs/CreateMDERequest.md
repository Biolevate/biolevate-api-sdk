# CreateMDERequest

Multi-dimensional extraction request. Provide a prompt, a schema, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**FilesInput**](FilesInput.md) |  | [optional]
**var_schema** | [**EliseEntitySchemaInput**](EliseEntitySchemaInput.md) | Optional fixed output schema. Per-column descriptions define each field. When omitted, the schema is inferred from prompt. | [optional]
**prompt** | **str** | Optional global extraction guidelines. Required when schema is omitted. | [optional]
**config** | [**JobLaunchConfig**](JobLaunchConfig.md) |  | [optional]

## Example

```python
from biolevate_client.models.create_mde_request import CreateMDERequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMDERequest from a JSON string
create_mde_request_instance = CreateMDERequest.from_json(json)
# print the JSON string representation of the object
print(CreateMDERequest.to_json())

# convert the object into a dict
create_mde_request_dict = create_mde_request_instance.to_dict()
# create an instance of CreateMDERequest from a dict
create_mde_request_from_dict = CreateMDERequest.from_dict(create_mde_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
