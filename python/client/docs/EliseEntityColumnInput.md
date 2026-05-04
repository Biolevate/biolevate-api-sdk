# EliseEntityColumnInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**allowed_values** | **List[str]** |  | [optional] 
**is_row_key** | **bool** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_entity_column_input import EliseEntityColumnInput

# TODO update the JSON string below
json = "{}"
# create an instance of EliseEntityColumnInput from a JSON string
elise_entity_column_input_instance = EliseEntityColumnInput.from_json(json)
# print the JSON string representation of the object
print(EliseEntityColumnInput.to_json())

# convert the object into a dict
elise_entity_column_input_dict = elise_entity_column_input_instance.to_dict()
# create an instance of EliseEntityColumnInput from a dict
elise_entity_column_input_from_dict = EliseEntityColumnInput.from_dict(elise_entity_column_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


