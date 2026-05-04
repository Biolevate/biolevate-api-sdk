# SourceIdentifiers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doi** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**open_access_id** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.source_identifiers import SourceIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of SourceIdentifiers from a JSON string
source_identifiers_instance = SourceIdentifiers.from_json(json)
# print the JSON string representation of the object
print(SourceIdentifiers.to_json())

# convert the object into a dict
source_identifiers_dict = source_identifiers_instance.to_dict()
# create an instance of SourceIdentifiers from a dict
source_identifiers_from_dict = SourceIdentifiers.from_dict(source_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


