# PolicyId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.policy_id import PolicyId

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyId from a JSON string
policy_id_instance = PolicyId.from_json(json)
# print the JSON string representation of the object
print(PolicyId.to_json())

# convert the object into a dict
policy_id_dict = policy_id_instance.to_dict()
# create an instance of PolicyId from a dict
policy_id_from_dict = PolicyId.from_dict(policy_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


