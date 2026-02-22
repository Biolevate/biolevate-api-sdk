# PositionDto

position

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.position_dto import PositionDto

# TODO update the JSON string below
json = "{}"
# create an instance of PositionDto from a JSON string
position_dto_instance = PositionDto.from_json(json)
# print the JSON string representation of the object
print(PositionDto.to_json())

# convert the object into a dict
position_dto_dict = position_dto_instance.to_dict()
# create an instance of PositionDto from a dict
position_dto_from_dict = PositionDto.from_dict(position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


