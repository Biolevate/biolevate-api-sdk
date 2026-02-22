# PolicyIdExternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.policy_id_external import PolicyIdExternal

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyIdExternal from a JSON string
policy_id_external_instance = PolicyIdExternal.from_json(json)
# print the JSON string representation of the object
print(PolicyIdExternal.to_json())

# convert the object into a dict
policy_id_external_dict = policy_id_external_instance.to_dict()
# create an instance of PolicyIdExternal from a dict
policy_id_external_from_dict = PolicyIdExternal.from_dict(policy_id_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


