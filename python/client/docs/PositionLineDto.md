# PositionLineDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** |  | [optional] 
**column_index_start** | **int** |  | [optional] 
**column_index_stop** | **int** |  | [optional] 

## Example

```python
from biolevate_client.models.position_line_dto import PositionLineDto

# TODO update the JSON string below
json = "{}"
# create an instance of PositionLineDto from a JSON string
position_line_dto_instance = PositionLineDto.from_json(json)
# print the JSON string representation of the object
print(PositionLineDto.to_json())

# convert the object into a dict
position_line_dto_dict = position_line_dto_instance.to_dict()
# create an instance of PositionLineDto from a dict
position_line_dto_from_dict = PositionLineDto.from_dict(position_line_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


