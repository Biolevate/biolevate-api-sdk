# FSProviderExternalConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**container_name** | **str** |  | 
**account_name** | **str** |  | [optional] 
**use_workload_identity** | **bool** |  | [optional] 
**workload_identity_enabled** | **bool** |  | [optional] 
**connection_string_enabled** | **bool** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 
**bucket_name** | **str** |  | 
**region** | **str** |  | 
**project_id** | **str** |  | 
**default_policy** | **str** |  | 
**name** | **str** |  | 
**site_url** | **str** |  | 
**document_library** | **str** |  | 
**tenant_id** | **str** |  | 

## Example

```python
from biolevate_client.models.fs_provider_external_config import FSProviderExternalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FSProviderExternalConfig from a JSON string
fs_provider_external_config_instance = FSProviderExternalConfig.from_json(json)
# print the JSON string representation of the object
print(FSProviderExternalConfig.to_json())

# convert the object into a dict
fs_provider_external_config_dict = fs_provider_external_config_instance.to_dict()
# create an instance of FSProviderExternalConfig from a dict
fs_provider_external_config_from_dict = FSProviderExternalConfig.from_dict(fs_provider_external_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


