# EliseEntityCellResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_key** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**explanation** | **str** |  | [optional] 
**reference_ids** | [**List[AnnotationId]**](AnnotationId.md) |  | [optional] 

## Example

```python
from biolevate_client.models.elise_entity_cell_result import EliseEntityCellResult

# TODO update the JSON string below
json = "{}"
# create an instance of EliseEntityCellResult from a JSON string
elise_entity_cell_result_instance = EliseEntityCellResult.from_json(json)
# print the JSON string representation of the object
print(EliseEntityCellResult.to_json())

# convert the object into a dict
elise_entity_cell_result_dict = elise_entity_cell_result_instance.to_dict()
# create an instance of EliseEntityCellResult from a dict
elise_entity_cell_result_from_dict = EliseEntityCellResult.from_dict(elise_entity_cell_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


