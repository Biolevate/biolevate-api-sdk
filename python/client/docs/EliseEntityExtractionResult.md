# EliseEntityExtractionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_id** | **UUID** |  | [optional] 
**meta** | **str** |  | [optional] 
**var_schema** | [**EliseEntitySchemaInput**](EliseEntitySchemaInput.md) |  | [optional] 
**rows** | [**List[EliseEntityRowResult]**](EliseEntityRowResult.md) |  | [optional] 
**explanation** | **str** |  | [optional] 
**reference_ids** | [**List[AnnotationId]**](AnnotationId.md) |  | [optional] 

## Example

```python
from biolevate_client.models.elise_entity_extraction_result import EliseEntityExtractionResult

# TODO update the JSON string below
json = "{}"
# create an instance of EliseEntityExtractionResult from a JSON string
elise_entity_extraction_result_instance = EliseEntityExtractionResult.from_json(json)
# print the JSON string representation of the object
print(EliseEntityExtractionResult.to_json())

# convert the object into a dict
elise_entity_extraction_result_dict = elise_entity_extraction_result_instance.to_dict()
# create an instance of EliseEntityExtractionResult from a dict
elise_entity_extraction_result_from_dict = EliseEntityExtractionResult.from_dict(elise_entity_extraction_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


