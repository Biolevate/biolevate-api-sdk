# EliseAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**AnnotationId**](AnnotationId.md) |  | [optional] 
**created_time** | **int** |  | [optional] 
**owner** | [**UserId**](UserId.md) |  | [optional] 
**space** | [**EntityId**](EntityId.md) |  | [optional] 
**data** | [**EliseAnnotationData**](EliseAnnotationData.md) |  | [optional] 
**type** | **str** |  | [optional] 
**modified_time** | **int** |  | [optional] 
**last_modifier** | [**UserId**](UserId.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_annotation import EliseAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of EliseAnnotation from a JSON string
elise_annotation_instance = EliseAnnotation.from_json(json)
# print the JSON string representation of the object
print(EliseAnnotation.to_json())

# convert the object into a dict
elise_annotation_dict = elise_annotation_instance.to_dict()
# create an instance of EliseAnnotation from a dict
elise_annotation_from_dict = EliseAnnotation.from_dict(elise_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


