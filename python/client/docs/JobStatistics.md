# JobStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources_queried** | **int** |  | [optional] 
**sources_matched_locally** | **int** |  | [optional] 
**sources_matched_remotely** | **int** |  | [optional] 
**sources_unmatched** | **int** |  | [optional] 
**remote_search_status** | **str** |  | [optional] 
**total_file_matches** | **int** |  | [optional] 
**total_metadata_only_matches** | **int** |  | [optional] 
**errors_by_search_result_id** | **Dict[str, str]** |  | [optional] 

## Example

```python
from biolevate_client.models.job_statistics import JobStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatistics from a JSON string
job_statistics_instance = JobStatistics.from_json(json)
# print the JSON string representation of the object
print(JobStatistics.to_json())

# convert the object into a dict
job_statistics_dict = job_statistics_instance.to_dict()
# create an instance of JobStatistics from a dict
job_statistics_from_dict = JobStatistics.from_dict(job_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


