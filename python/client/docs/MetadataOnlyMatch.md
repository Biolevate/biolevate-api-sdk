# MetadataOnlyMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_result_id** | **str** |  | [optional] 
**ontologies** | [**List[EliseOntology]**](EliseOntology.md) |  | [optional] 

## Example

```python
from biolevate_client.models.metadata_only_match import MetadataOnlyMatch

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOnlyMatch from a JSON string
metadata_only_match_instance = MetadataOnlyMatch.from_json(json)
# print the JSON string representation of the object
print(MetadataOnlyMatch.to_json())

# convert the object into a dict
metadata_only_match_dict = metadata_only_match_instance.to_dict()
# create an instance of MetadataOnlyMatch from a dict
metadata_only_match_from_dict = MetadataOnlyMatch.from_dict(metadata_only_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


