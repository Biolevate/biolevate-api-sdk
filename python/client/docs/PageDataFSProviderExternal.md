# PageDataFSProviderExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FSProviderExternal]**](FSProviderExternal.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 

## Example

```python
from biolevate_client.models.page_data_fs_provider_external import PageDataFSProviderExternal

# TODO update the JSON string below
json = "{}"
# create an instance of PageDataFSProviderExternal from a JSON string
page_data_fs_provider_external_instance = PageDataFSProviderExternal.from_json(json)
# print the JSON string representation of the object
print(PageDataFSProviderExternal.to_json())

# convert the object into a dict
page_data_fs_provider_external_dict = page_data_fs_provider_external_instance.to_dict()
# create an instance of PageDataFSProviderExternal from a dict
page_data_fs_provider_external_from_dict = PageDataFSProviderExternal.from_dict(page_data_fs_provider_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


