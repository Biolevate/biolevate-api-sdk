# FSProviderAzureConfigExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** |  | 
**account_name** | **str** |  | [optional] 
**use_workload_identity** | **bool** |  | [optional] 
**workload_identity_enabled** | **bool** |  | [optional] 
**connection_string_enabled** | **bool** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.fs_provider_azure_config_external import FSProviderAzureConfigExternal

# TODO update the JSON string below
json = "{}"
# create an instance of FSProviderAzureConfigExternal from a JSON string
fs_provider_azure_config_external_instance = FSProviderAzureConfigExternal.from_json(json)
# print the JSON string representation of the object
print(FSProviderAzureConfigExternal.to_json())

# convert the object into a dict
fs_provider_azure_config_external_dict = fs_provider_azure_config_external_instance.to_dict()
# create an instance of FSProviderAzureConfigExternal from a dict
fs_provider_azure_config_external_from_dict = FSProviderAzureConfigExternal.from_dict(fs_provider_azure_config_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


