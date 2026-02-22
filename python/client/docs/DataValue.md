# DataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**str_value** | **str** |  | [optional] 
**bool_value** | **bool** |  | [optional] 
**long_value** | **int** |  | [optional] 
**double_value** | **float** |  | [optional] 
**date_value** | **datetime** |  | [optional] 
**str_list_value** | **List[str]** |  | [optional] 
**bool_list_value** | **List[bool]** |  | [optional] 
**long_list_value** | **List[int]** |  | [optional] 
**double_list_value** | **List[float]** |  | [optional] 
**date_list_value** | **List[datetime]** |  | [optional] 

## Example

```python
from biolevate_client.models.data_value import DataValue

# TODO update the JSON string below
json = "{}"
# create an instance of DataValue from a JSON string
data_value_instance = DataValue.from_json(json)
# print the JSON string representation of the object
print(DataValue.to_json())

# convert the object into a dict
data_value_dict = data_value_instance.to_dict()
# create an instance of DataValue from a dict
data_value_from_dict = DataValue.from_dict(data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


