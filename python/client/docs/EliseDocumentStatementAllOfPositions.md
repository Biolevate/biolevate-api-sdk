# EliseDocumentStatementAllOfPositions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**bbox** | [**BboxDto**](BboxDto.md) |  | [optional] 
**page_number** | **int** |  | [optional] 
**sheet_name** | **str** |  | [optional] 
**row** | **int** |  | [optional] 
**col** | **int** |  | [optional] 
**line_number** | **int** |  | [optional] 
**column_index_start** | **int** |  | [optional] 
**column_index_stop** | **int** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_document_statement_all_of_positions import EliseDocumentStatementAllOfPositions

# TODO update the JSON string below
json = "{}"
# create an instance of EliseDocumentStatementAllOfPositions from a JSON string
elise_document_statement_all_of_positions_instance = EliseDocumentStatementAllOfPositions.from_json(json)
# print the JSON string representation of the object
print(EliseDocumentStatementAllOfPositions.to_json())

# convert the object into a dict
elise_document_statement_all_of_positions_dict = elise_document_statement_all_of_positions_instance.to_dict()
# create an instance of EliseDocumentStatementAllOfPositions from a dict
elise_document_statement_all_of_positions_from_dict = EliseDocumentStatementAllOfPositions.from_dict(elise_document_statement_all_of_positions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


