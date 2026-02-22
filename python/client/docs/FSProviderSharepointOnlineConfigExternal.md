# FSProviderSharepointOnlineConfigExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_url** | **str** |  | 
**document_library** | **str** |  | 
**tenant_id** | **str** |  | 

## Example

```python
from biolevate_client.models.fs_provider_sharepoint_online_config_external import FSProviderSharepointOnlineConfigExternal

# TODO update the JSON string below
json = "{}"
# create an instance of FSProviderSharepointOnlineConfigExternal from a JSON string
fs_provider_sharepoint_online_config_external_instance = FSProviderSharepointOnlineConfigExternal.from_json(json)
# print the JSON string representation of the object
print(FSProviderSharepointOnlineConfigExternal.to_json())

# convert the object into a dict
fs_provider_sharepoint_online_config_external_dict = fs_provider_sharepoint_online_config_external_instance.to_dict()
# create an instance of FSProviderSharepointOnlineConfigExternal from a dict
fs_provider_sharepoint_online_config_external_from_dict = FSProviderSharepointOnlineConfigExternal.from_dict(fs_provider_sharepoint_online_config_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


