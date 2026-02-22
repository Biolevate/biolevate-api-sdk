# EliseMetaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | **str** |  | [optional] 
**answer_type** | [**ExpectedAnswerTypeDto**](ExpectedAnswerTypeDto.md) |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.elise_meta_input import EliseMetaInput

# TODO update the JSON string below
json = "{}"
# create an instance of EliseMetaInput from a JSON string
elise_meta_input_instance = EliseMetaInput.from_json(json)
# print the JSON string representation of the object
print(EliseMetaInput.to_json())

# convert the object into a dict
elise_meta_input_dict = elise_meta_input_instance.to_dict()
# create an instance of EliseMetaInput from a dict
elise_meta_input_from_dict = EliseMetaInput.from_dict(elise_meta_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


