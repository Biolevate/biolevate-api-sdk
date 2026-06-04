# AgentCompletionConfig

Per-completion LLM knobs for an agent run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Semantic model preset (defaults to BALANCED when omitted) | [optional] 
**temperature** | **float** | Sampling temperature | [optional] 
**max_completion_tokens** | **int** | Hard cap on response tokens | [optional] 

## Example

```python
from biolevate_client.models.agent_completion_config import AgentCompletionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCompletionConfig from a JSON string
agent_completion_config_instance = AgentCompletionConfig.from_json(json)
# print the JSON string representation of the object
print(AgentCompletionConfig.to_json())

# convert the object into a dict
agent_completion_config_dict = agent_completion_config_instance.to_dict()
# create an instance of AgentCompletionConfig from a dict
agent_completion_config_from_dict = AgentCompletionConfig.from_dict(agent_completion_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


