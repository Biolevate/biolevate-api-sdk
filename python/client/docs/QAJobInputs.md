# QAJobInputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**FilesInput**](FilesInput.md) |  | [optional] 
**questions** | [**List[EliseQuestionInput]**](EliseQuestionInput.md) |  | [optional] 

## Example

```python
from biolevate_client.models.qa_job_inputs import QAJobInputs

# TODO update the JSON string below
json = "{}"
# create an instance of QAJobInputs from a JSON string
qa_job_inputs_instance = QAJobInputs.from_json(json)
# print the JSON string representation of the object
print(QAJobInputs.to_json())

# convert the object into a dict
qa_job_inputs_dict = qa_job_inputs_instance.to_dict()
# create an instance of QAJobInputs from a dict
qa_job_inputs_from_dict = QAJobInputs.from_dict(qa_job_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


