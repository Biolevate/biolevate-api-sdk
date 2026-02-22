# ProviderId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.provider_id import ProviderId

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderId from a JSON string
provider_id_instance = ProviderId.from_json(json)
# print the JSON string representation of the object
print(ProviderId.to_json())

# convert the object into a dict
provider_id_dict = provider_id_instance.to_dict()
# create an instance of ProviderId from a dict
provider_id_from_dict = ProviderId.from_dict(provider_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


