# EliseOntology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concept_id** | [**EntityId**](EntityId.md) |  | 
**name** | **str** |  | 
**metas** | [**Dict[str, EliseOntologyMeta]**](EliseOntologyMeta.md) |  | [optional] 

## Example

```python
from biolevate_client.models.elise_ontology import EliseOntology

# TODO update the JSON string below
json = "{}"
# create an instance of EliseOntology from a JSON string
elise_ontology_instance = EliseOntology.from_json(json)
# print the JSON string representation of the object
print(EliseOntology.to_json())

# convert the object into a dict
elise_ontology_dict = elise_ontology_instance.to_dict()
# create an instance of EliseOntology from a dict
elise_ontology_from_dict = EliseOntology.from_dict(elise_ontology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


