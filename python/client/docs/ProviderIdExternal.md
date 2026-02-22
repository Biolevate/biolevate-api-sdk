# ProviderIdExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.provider_id_external import ProviderIdExternal

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderIdExternal from a JSON string
provider_id_external_instance = ProviderIdExternal.from_json(json)
# print the JSON string representation of the object
print(ProviderIdExternal.to_json())

# convert the object into a dict
provider_id_external_dict = provider_id_external_instance.to_dict()
# create an instance of ProviderIdExternal from a dict
provider_id_external_from_dict = ProviderIdExternal.from_dict(provider_id_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


