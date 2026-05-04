# KnowledgeSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.knowledge_source import KnowledgeSource

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeSource from a JSON string
knowledge_source_instance = KnowledgeSource.from_json(json)
# print the JSON string representation of the object
print(KnowledgeSource.to_json())

# convert the object into a dict
knowledge_source_dict = knowledge_source_instance.to_dict()
# create an instance of KnowledgeSource from a dict
knowledge_source_from_dict = KnowledgeSource.from_dict(knowledge_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


