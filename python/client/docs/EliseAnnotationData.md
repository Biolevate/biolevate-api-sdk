# EliseAnnotationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**positions** | [**List[EliseDocumentStatementAllOfPositions]**](EliseDocumentStatementAllOfPositions.md) |  | [optional] 
**meta_data** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_annotation_data import EliseAnnotationData

# TODO update the JSON string below
json = "{}"
# create an instance of EliseAnnotationData from a JSON string
elise_annotation_data_instance = EliseAnnotationData.from_json(json)
# print the JSON string representation of the object
print(EliseAnnotationData.to_json())

# convert the object into a dict
elise_annotation_data_dict = elise_annotation_data_instance.to_dict()
# create an instance of EliseAnnotationData from a dict
elise_annotation_data_from_dict = EliseAnnotationData.from_dict(elise_annotation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


