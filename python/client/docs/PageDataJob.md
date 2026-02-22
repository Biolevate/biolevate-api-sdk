# PageDataJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Job]**](Job.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 

## Example

```python
from biolevate_client.models.page_data_job import PageDataJob

# TODO update the JSON string below
json = "{}"
# create an instance of PageDataJob from a JSON string
page_data_job_instance = PageDataJob.from_json(json)
# print the JSON string representation of the object
print(PageDataJob.to_json())

# convert the object into a dict
page_data_job_dict = page_data_job_instance.to_dict()
# create an instance of PageDataJob from a dict
page_data_job_from_dict = PageDataJob.from_dict(page_data_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


