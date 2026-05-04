# FindSimilarApiJobDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_time** | **int** |  | [optional] 
**modified_time** | **int** |  | [optional] 
**execution_time_ms** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**sources** | [**SearchSources**](SearchSources.md) |  | [optional] 
**result** | [**List[SourceMatches]**](SourceMatches.md) |  | [optional] 
**statistics** | [**JobStatistics**](JobStatistics.md) |  | [optional] 

## Example

```python
from biolevate_client.models.find_similar_api_job_dto import FindSimilarApiJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of FindSimilarApiJobDto from a JSON string
find_similar_api_job_dto_instance = FindSimilarApiJobDto.from_json(json)
# print the JSON string representation of the object
print(FindSimilarApiJobDto.to_json())

# convert the object into a dict
find_similar_api_job_dto_dict = find_similar_api_job_dto_instance.to_dict()
# create an instance of FindSimilarApiJobDto from a dict
find_similar_api_job_dto_from_dict = FindSimilarApiJobDto.from_dict(find_similar_api_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


