# PositionBboxDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**BboxDto**](BboxDto.md) |  | [optional] 
**page_number** | **int** |  | [optional] 

## Example

```python
from biolevate_client.models.position_bbox_dto import PositionBboxDto

# TODO update the JSON string below
json = "{}"
# create an instance of PositionBboxDto from a JSON string
position_bbox_dto_instance = PositionBboxDto.from_json(json)
# print the JSON string representation of the object
print(PositionBboxDto.to_json())

# convert the object into a dict
position_bbox_dto_dict = position_bbox_dto_instance.to_dict()
# create an instance of PositionBboxDto from a dict
position_bbox_dto_from_dict = PositionBboxDto.from_dict(position_bbox_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


