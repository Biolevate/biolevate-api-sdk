# EliseKnowledgeStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_knowledge_statement import EliseKnowledgeStatement

# TODO update the JSON string below
json = "{}"
# create an instance of EliseKnowledgeStatement from a JSON string
elise_knowledge_statement_instance = EliseKnowledgeStatement.from_json(json)
# print the JSON string representation of the object
print(EliseKnowledgeStatement.to_json())

# convert the object into a dict
elise_knowledge_statement_dict = elise_knowledge_statement_instance.to_dict()
# create an instance of EliseKnowledgeStatement from a dict
elise_knowledge_statement_from_dict = EliseKnowledgeStatement.from_dict(elise_knowledge_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


