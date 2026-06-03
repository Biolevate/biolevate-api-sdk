# AgentJobInputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**messages** | [**List[AgentInput]**](AgentInput.md) |  | [optional] 
**files** | [**FilesInput**](FilesInput.md) |  | [optional] 
**output_model_schema** | **object** |  | [optional] 
**completion_config** | [**AgentCompletionConfig**](AgentCompletionConfig.md) |  | [optional] 
**max_iterations** | **int** |  | [optional] 
**conversation_id** | **UUID** |  | [optional] 

## Example

```python
from biolevate_client.models.agent_job_inputs import AgentJobInputs

# TODO update the JSON string below
json = "{}"
# create an instance of AgentJobInputs from a JSON string
agent_job_inputs_instance = AgentJobInputs.from_json(json)
# print the JSON string representation of the object
print(AgentJobInputs.to_json())

# convert the object into a dict
agent_job_inputs_dict = agent_job_inputs_instance.to_dict()
# create an instance of AgentJobInputs from a dict
agent_job_inputs_from_dict = AgentJobInputs.from_dict(agent_job_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


