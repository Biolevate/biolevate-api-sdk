# EliseQAResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explanation** | **str** |  | [optional] 
**sourced_content** | **str** |  | [optional] 
**reference_ids** | [**List[AnnotationId]**](AnnotationId.md) |  | [optional] 
**question** | **str** |  | [optional] 
**expected_answer** | **str** |  | [optional] 
**validity_explaination** | **str** |  | [optional] 
**input_question_ids** | **List[str]** |  | [optional] 
**answer_validity** | **float** |  | [optional] 
**raw_value** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_qa_result import EliseQAResult

# TODO update the JSON string below
json = "{}"
# create an instance of EliseQAResult from a JSON string
elise_qa_result_instance = EliseQAResult.from_json(json)
# print the JSON string representation of the object
print(EliseQAResult.to_json())

# convert the object into a dict
elise_qa_result_dict = elise_qa_result_instance.to_dict()
# create an instance of EliseQAResult from a dict
elise_qa_result_from_dict = EliseQAResult.from_dict(elise_qa_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


