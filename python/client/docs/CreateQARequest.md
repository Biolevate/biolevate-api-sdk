# CreateQARequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**FilesInput**](FilesInput.md) |  | [optional] 
**questions** | [**List[EliseQuestionInput]**](EliseQuestionInput.md) |  | [optional] 

## Example

```python
from biolevate_client.models.create_qa_request import CreateQARequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQARequest from a JSON string
create_qa_request_instance = CreateQARequest.from_json(json)
# print the JSON string representation of the object
print(CreateQARequest.to_json())

# convert the object into a dict
create_qa_request_dict = create_qa_request_instance.to_dict()
# create an instance of CreateQARequest from a dict
create_qa_request_from_dict = CreateQARequest.from_dict(create_qa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


