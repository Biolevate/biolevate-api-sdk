# FSProviderS3ConfigExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | 
**region** | **str** |  | 

## Example

```python
from biolevate_client.models.fs_provider_s3_config_external import FSProviderS3ConfigExternal

# TODO update the JSON string below
json = "{}"
# create an instance of FSProviderS3ConfigExternal from a JSON string
fs_provider_s3_config_external_instance = FSProviderS3ConfigExternal.from_json(json)
# print the JSON string representation of the object
print(FSProviderS3ConfigExternal.to_json())

# convert the object into a dict
fs_provider_s3_config_external_dict = fs_provider_s3_config_external_instance.to_dict()
# create an instance of FSProviderS3ConfigExternal from a dict
fs_provider_s3_config_external_from_dict = FSProviderS3ConfigExternal.from_dict(fs_provider_s3_config_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


