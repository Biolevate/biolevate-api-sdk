# EliseEntityRowResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cells** | [**List[EliseEntityCellResult]**](EliseEntityCellResult.md) |  | [optional] 
**explanation** | **str** |  | [optional] 
**reference_ids** | [**List[AnnotationId]**](AnnotationId.md) |  | [optional] 

## Example

```python
from biolevate_client.models.elise_entity_row_result import EliseEntityRowResult

# TODO update the JSON string below
json = "{}"
# create an instance of EliseEntityRowResult from a JSON string
elise_entity_row_result_instance = EliseEntityRowResult.from_json(json)
# print the JSON string representation of the object
print(EliseEntityRowResult.to_json())

# convert the object into a dict
elise_entity_row_result_dict = elise_entity_row_result_instance.to_dict()
# create an instance of EliseEntityRowResult from a dict
elise_entity_row_result_from_dict = EliseEntityRowResult.from_dict(elise_entity_row_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


