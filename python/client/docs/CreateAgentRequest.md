# CreateAgentRequest

Request to schedule a new agent run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Stateful mode: the new user message for this turn. Prior turns are loaded server-side from &#x60;conversationId&#x60;. Mutually exclusive with &#x60;messages&#x60;.  | [optional] 
**messages** | [**List[AgentInput]**](AgentInput.md) |  | [optional] 
**files** | [**FilesInput**](FilesInput.md) | Files the agent can read from | [optional] 
**history_input_valid** | **bool** |  | [optional] 
**conversation_id_valid** | **bool** |  | [optional] 
**output_model_schema** | **object** | Optional JSON Schema constraining the agent&#39;s final answer to a structured object. Free-form: any valid JSON Schema is accepted | [optional] 
**completion_config** | [**AgentCompletionConfig**](AgentCompletionConfig.md) | Per-completion LLM knobs (model preset, temperature, max tokens) | [optional] 
**max_iterations** | **int** | Hard cap on the number of agent-loop iterations | [optional] 
**conversation_id** | **UUID** | Stateful only: continue an existing server session. Omit to start a new conversation. Must not be set for stateless runs. | [optional] 

## Example

```python
from biolevate_client.models.create_agent_request import CreateAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentRequest from a JSON string
create_agent_request_instance = CreateAgentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAgentRequest.to_json())

# convert the object into a dict
create_agent_request_dict = create_agent_request_instance.to_dict()
# create an instance of CreateAgentRequest from a dict
create_agent_request_from_dict = CreateAgentRequest.from_dict(create_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


