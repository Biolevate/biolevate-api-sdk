# PositionCellDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheet_name** | **str** |  | [optional] 
**row** | **int** |  | [optional] 
**col** | **int** |  | [optional] 

## Example

```python
from biolevate_client.models.position_cell_dto import PositionCellDto

# TODO update the JSON string below
json = "{}"
# create an instance of PositionCellDto from a JSON string
position_cell_dto_instance = PositionCellDto.from_json(json)
# print the JSON string representation of the object
print(PositionCellDto.to_json())

# convert the object into a dict
position_cell_dto_dict = position_cell_dto_instance.to_dict()
# create an instance of PositionCellDto from a dict
position_cell_dto_from_dict = PositionCellDto.from_dict(position_cell_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


