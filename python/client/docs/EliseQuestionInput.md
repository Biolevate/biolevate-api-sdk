# EliseQuestionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**answer_type** | [**ExpectedAnswerTypeDto**](ExpectedAnswerTypeDto.md) |  | [optional] 
**guidelines** | **str** |  | [optional] 
**expected_answer** | **str** |  | [optional] 
**input_question_ids** | **List[str]** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_question_input import EliseQuestionInput

# TODO update the JSON string below
json = "{}"
# create an instance of EliseQuestionInput from a JSON string
elise_question_input_instance = EliseQuestionInput.from_json(json)
# print the JSON string representation of the object
print(EliseQuestionInput.to_json())

# convert the object into a dict
elise_question_input_dict = elise_question_input_instance.to_dict()
# create an instance of EliseQuestionInput from a dict
elise_question_input_from_dict = EliseQuestionInput.from_dict(elise_question_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


