# FSProviderGCSConfigExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | 
**region** | **str** |  | 
**project_id** | **str** |  | 

## Example

```python
from biolevate_client.models.fs_provider_gcs_config_external import FSProviderGCSConfigExternal

# TODO update the JSON string below
json = "{}"
# create an instance of FSProviderGCSConfigExternal from a JSON string
fs_provider_gcs_config_external_instance = FSProviderGCSConfigExternal.from_json(json)
# print the JSON string representation of the object
print(FSProviderGCSConfigExternal.to_json())

# convert the object into a dict
fs_provider_gcs_config_external_dict = fs_provider_gcs_config_external_instance.to_dict()
# create an instance of FSProviderGCSConfigExternal from a dict
fs_provider_gcs_config_external_from_dict = FSProviderGCSConfigExternal.from_dict(fs_provider_gcs_config_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


