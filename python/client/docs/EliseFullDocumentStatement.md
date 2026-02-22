# EliseFullDocumentStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_name** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_full_document_statement import EliseFullDocumentStatement

# TODO update the JSON string below
json = "{}"
# create an instance of EliseFullDocumentStatement from a JSON string
elise_full_document_statement_instance = EliseFullDocumentStatement.from_json(json)
# print the JSON string representation of the object
print(EliseFullDocumentStatement.to_json())

# convert the object into a dict
elise_full_document_statement_dict = elise_full_document_statement_instance.to_dict()
# create an instance of EliseFullDocumentStatement from a dict
elise_full_document_statement_from_dict = EliseFullDocumentStatement.from_dict(elise_full_document_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


