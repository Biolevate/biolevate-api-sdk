# EliseEntitySchemaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**columns** | [**List[EliseEntityColumnInput]**](EliseEntityColumnInput.md) |  | [optional] 

## Example

```python
from biolevate_client.models.elise_entity_schema_input import EliseEntitySchemaInput

# TODO update the JSON string below
json = "{}"
# create an instance of EliseEntitySchemaInput from a JSON string
elise_entity_schema_input_instance = EliseEntitySchemaInput.from_json(json)
# print the JSON string representation of the object
print(EliseEntitySchemaInput.to_json())

# convert the object into a dict
elise_entity_schema_input_dict = elise_entity_schema_input_instance.to_dict()
# create an instance of EliseEntitySchemaInput from a dict
elise_entity_schema_input_from_dict = EliseEntitySchemaInput.from_dict(elise_entity_schema_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


