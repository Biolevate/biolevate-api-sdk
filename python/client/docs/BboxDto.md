# BboxDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x0** | **float** |  | [optional] 
**y0** | **float** |  | [optional] 
**x1** | **float** |  | [optional] 
**y1** | **float** |  | [optional] 

## Example

```python
from biolevate_client.models.bbox_dto import BboxDto

# TODO update the JSON string below
json = "{}"
# create an instance of BboxDto from a JSON string
bbox_dto_instance = BboxDto.from_json(json)
# print the JSON string representation of the object
print(BboxDto.to_json())

# convert the object into a dict
bbox_dto_dict = bbox_dto_instance.to_dict()
# create an instance of BboxDto from a dict
bbox_dto_from_dict = BboxDto.from_dict(bbox_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


