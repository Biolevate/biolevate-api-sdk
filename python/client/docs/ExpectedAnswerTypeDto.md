# ExpectedAnswerTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | [optional] 
**multi_valued** | **bool** |  | [optional] 
**enum_values** | **List[str]** | List of possible values for enum types | [optional] 
**enum_colors** | **Dict[str, str]** | Map of enum values to their associated colors | [optional] 
**enum_suggestions_enabled** | **bool** |  | [optional] 
**rejected_enum_values** | **List[str]** |  | [optional] 
**date_format** | **str** |  | [optional] 
**decimal_precision** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.expected_answer_type_dto import ExpectedAnswerTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectedAnswerTypeDto from a JSON string
expected_answer_type_dto_instance = ExpectedAnswerTypeDto.from_json(json)
# print the JSON string representation of the object
print(ExpectedAnswerTypeDto.to_json())

# convert the object into a dict
expected_answer_type_dto_dict = expected_answer_type_dto_instance.to_dict()
# create an instance of ExpectedAnswerTypeDto from a dict
expected_answer_type_dto_from_dict = ExpectedAnswerTypeDto.from_dict(expected_answer_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


