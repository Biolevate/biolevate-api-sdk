# SourceMatches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**SourceIdentifiers**](SourceIdentifiers.md) |  | [optional] 
**files** | [**List[FileMatch]**](FileMatch.md) |  | [optional] 
**metadata_only** | [**List[MetadataOnlyMatch]**](MetadataOnlyMatch.md) |  | [optional] 

## Example

```python
from biolevate_client.models.source_matches import SourceMatches

# TODO update the JSON string below
json = "{}"
# create an instance of SourceMatches from a JSON string
source_matches_instance = SourceMatches.from_json(json)
# print the JSON string representation of the object
print(SourceMatches.to_json())

# convert the object into a dict
source_matches_dict = source_matches_instance.to_dict()
# create an instance of SourceMatches from a dict
source_matches_from_dict = SourceMatches.from_dict(source_matches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


