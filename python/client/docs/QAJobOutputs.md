# QAJobOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EliseQAResult]**](EliseQAResult.md) |  | [optional] 

## Example

```python
from biolevate_client.models.qa_job_outputs import QAJobOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of QAJobOutputs from a JSON string
qa_job_outputs_instance = QAJobOutputs.from_json(json)
# print the JSON string representation of the object
print(QAJobOutputs.to_json())

# convert the object into a dict
qa_job_outputs_dict = qa_job_outputs_instance.to_dict()
# create an instance of QAJobOutputs from a dict
qa_job_outputs_from_dict = QAJobOutputs.from_dict(qa_job_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


