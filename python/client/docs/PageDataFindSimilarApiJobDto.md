# PageDataFindSimilarApiJobDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FindSimilarApiJobDto]**](FindSimilarApiJobDto.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 

## Example

```python
from biolevate_client.models.page_data_find_similar_api_job_dto import PageDataFindSimilarApiJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageDataFindSimilarApiJobDto from a JSON string
page_data_find_similar_api_job_dto_instance = PageDataFindSimilarApiJobDto.from_json(json)
# print the JSON string representation of the object
print(PageDataFindSimilarApiJobDto.to_json())

# convert the object into a dict
page_data_find_similar_api_job_dto_dict = page_data_find_similar_api_job_dto_instance.to_dict()
# create an instance of PageDataFindSimilarApiJobDto from a dict
page_data_find_similar_api_job_dto_from_dict = PageDataFindSimilarApiJobDto.from_dict(page_data_find_similar_api_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


