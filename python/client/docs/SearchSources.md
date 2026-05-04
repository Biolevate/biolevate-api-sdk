# SearchSources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_identifiers** | [**List[SourceIdentifiers]**](SourceIdentifiers.md) |  | [optional] 

## Example

```python
from biolevate_client.models.search_sources import SearchSources

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSources from a JSON string
search_sources_instance = SearchSources.from_json(json)
# print the JSON string representation of the object
print(SearchSources.to_json())

# convert the object into a dict
search_sources_dict = search_sources_instance.to_dict()
# create an instance of SearchSources from a dict
search_sources_from_dict = SearchSources.from_dict(search_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


