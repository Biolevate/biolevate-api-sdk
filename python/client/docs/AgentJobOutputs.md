# AgentJobOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **object** |  | [optional] 
**explanation** | **str** |  | [optional] 
**reference_ids** | **List[UUID]** |  | [optional] 

## Example

```python
from biolevate_client.models.agent_job_outputs import AgentJobOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of AgentJobOutputs from a JSON string
agent_job_outputs_instance = AgentJobOutputs.from_json(json)
# print the JSON string representation of the object
print(AgentJobOutputs.to_json())

# convert the object into a dict
agent_job_outputs_dict = agent_job_outputs_instance.to_dict()
# create an instance of AgentJobOutputs from a dict
agent_job_outputs_from_dict = AgentJobOutputs.from_dict(agent_job_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


