# AnnotationId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.annotation_id import AnnotationId

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationId from a JSON string
annotation_id_instance = AnnotationId.from_json(json)
# print the JSON string representation of the object
print(AnnotationId.to_json())

# convert the object into a dict
annotation_id_dict = annotation_id_instance.to_dict()
# create an instance of AnnotationId from a dict
annotation_id_from_dict = AnnotationId.from_dict(annotation_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


