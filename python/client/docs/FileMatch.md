# FileMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**checksum** | **str** |  | [optional] 
**ontologies** | [**List[EliseOntology]**](EliseOntology.md) |  | [optional] 

## Example

```python
from biolevate_client.models.file_match import FileMatch

# TODO update the JSON string below
json = "{}"
# create an instance of FileMatch from a JSON string
file_match_instance = FileMatch.from_json(json)
# print the JSON string representation of the object
print(FileMatch.to_json())

# convert the object into a dict
file_match_dict = file_match_instance.to_dict()
# create an instance of FileMatch from a dict
file_match_from_dict = FileMatch.from_dict(file_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


