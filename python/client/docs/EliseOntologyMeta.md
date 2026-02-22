# EliseOntologyMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explanation** | **str** |  | [optional] 
**annotation_ids** | [**List[AnnotationId]**](AnnotationId.md) |  | [optional] 
**meta_name** | **str** |  | [optional] 
**meta_value** | **object** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_ontology_meta import EliseOntologyMeta

# TODO update the JSON string below
json = "{}"
# create an instance of EliseOntologyMeta from a JSON string
elise_ontology_meta_instance = EliseOntologyMeta.from_json(json)
# print the JSON string representation of the object
print(EliseOntologyMeta.to_json())

# convert the object into a dict
elise_ontology_meta_dict = elise_ontology_meta_instance.to_dict()
# create an instance of EliseOntologyMeta from a dict
elise_ontology_meta_from_dict = EliseOntologyMeta.from_dict(elise_ontology_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


