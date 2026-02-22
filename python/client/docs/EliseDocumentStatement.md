# EliseDocumentStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**positions** | [**List[EliseDocumentStatementAllOfPositions]**](EliseDocumentStatementAllOfPositions.md) |  | [optional] 

## Example

```python
from biolevate_client.models.elise_document_statement import EliseDocumentStatement

# TODO update the JSON string below
json = "{}"
# create an instance of EliseDocumentStatement from a JSON string
elise_document_statement_instance = EliseDocumentStatement.from_json(json)
# print the JSON string representation of the object
print(EliseDocumentStatement.to_json())

# convert the object into a dict
elise_document_statement_dict = elise_document_statement_instance.to_dict()
# create an instance of EliseDocumentStatement from a dict
elise_document_statement_from_dict = EliseDocumentStatement.from_dict(elise_document_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


