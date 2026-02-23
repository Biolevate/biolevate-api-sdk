# ProviderItem

Provider item (file or folder)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Provider ID | [optional] 
**key** | **str** | Full item key. Files: &#39;path/to/file.pdf&#39;, Folders: &#39;path/to/folder/&#39; | [optional] 
**type** | **str** | Item type | [optional] 
**size** | **int** | File size in bytes (null for folders) | [optional] 
**extension** | **str** | File extension (null for folders) | [optional] 
**media_type** | **str** | Media type (null for folders) | [optional] 
**last_modified** | **int** | Last modified timestamp in milliseconds | [optional] 

## Example

```python
from biolevate_client.models.provider_item import ProviderItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderItem from a JSON string
provider_item_instance = ProviderItem.from_json(json)
# print the JSON string representation of the object
print(ProviderItem.to_json())

# convert the object into a dict
provider_item_dict = provider_item_instance.to_dict()
# create an instance of ProviderItem from a dict
provider_item_from_dict = ProviderItem.from_dict(provider_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


