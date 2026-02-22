# FSProviderExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ProviderIdExternal**](ProviderIdExternal.md) |  | [optional] 
**created_time** | **int** |  | [optional] 
**owner** | [**UserIdExternal**](UserIdExternal.md) |  | [optional] 
**policy** | [**PolicyIdExternal**](PolicyIdExternal.md) |  | [optional] 
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**config** | [**FSProviderExternalConfig**](FSProviderExternalConfig.md) |  | [optional] 
**type** | **str** |  | [optional] 
**system** | **bool** |  | [optional] 

## Example

```python
from biolevate_client.models.fs_provider_external import FSProviderExternal

# TODO update the JSON string below
json = "{}"
# create an instance of FSProviderExternal from a JSON string
fs_provider_external_instance = FSProviderExternal.from_json(json)
# print the JSON string representation of the object
print(FSProviderExternal.to_json())

# convert the object into a dict
fs_provider_external_dict = fs_provider_external_instance.to_dict()
# create an instance of FSProviderExternal from a dict
fs_provider_external_from_dict = FSProviderExternal.from_dict(fs_provider_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


