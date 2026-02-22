# EliseMetaResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**explanation** | **str** |  | [optional] 
**answer_type** | [**ExpectedAnswerTypeDto**](ExpectedAnswerTypeDto.md) |  | [optional] 
**answer** | [**DataValue**](DataValue.md) |  | [optional] 
**reference_ids** | [**List[AnnotationId]**](AnnotationId.md) |  | [optional] 
**meta** | **str** |  | [optional] 
**raw_value** | **object** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_meta_result import EliseMetaResult

# TODO update the JSON string below
json = "{}"
# create an instance of EliseMetaResult from a JSON string
elise_meta_result_instance = EliseMetaResult.from_json(json)
# print the JSON string representation of the object
print(EliseMetaResult.to_json())

# convert the object into a dict
elise_meta_result_dict = elise_meta_result_instance.to_dict()
# create an instance of EliseMetaResult from a dict
elise_meta_result_from_dict = EliseMetaResult.from_dict(elise_meta_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


