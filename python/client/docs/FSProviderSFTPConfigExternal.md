# FSProviderSFTPConfigExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**port** | **int** |  | 
**username** | **str** |  | 
**root_path** | **str** |  | [optional] 
**allow_unknown_hosts** | **bool** |  | [optional] 
**timeout_ms** | **int** |  | [optional] 

## Example

```python
from biolevate_client.models.fs_provider_sftp_config_external import FSProviderSFTPConfigExternal

# TODO update the JSON string below
json = "{}"
# create an instance of FSProviderSFTPConfigExternal from a JSON string
fs_provider_sftp_config_external_instance = FSProviderSFTPConfigExternal.from_json(json)
# print the JSON string representation of the object
print(FSProviderSFTPConfigExternal.to_json())

# convert the object into a dict
fs_provider_sftp_config_external_dict = fs_provider_sftp_config_external_instance.to_dict()
# create an instance of FSProviderSFTPConfigExternal from a dict
fs_provider_sftp_config_external_from_dict = FSProviderSFTPConfigExternal.from_dict(fs_provider_sftp_config_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


