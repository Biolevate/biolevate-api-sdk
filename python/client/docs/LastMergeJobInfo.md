# LastMergeJobInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from biolevate_client.models.last_merge_job_info import LastMergeJobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LastMergeJobInfo from a JSON string
last_merge_job_info_instance = LastMergeJobInfo.from_json(json)
# print the JSON string representation of the object
print(LastMergeJobInfo.to_json())

# convert the object into a dict
last_merge_job_info_dict = last_merge_job_info_instance.to_dict()
# create an instance of LastMergeJobInfo from a dict
last_merge_job_info_from_dict = LastMergeJobInfo.from_dict(last_merge_job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


