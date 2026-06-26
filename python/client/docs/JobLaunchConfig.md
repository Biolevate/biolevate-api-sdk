# JobLaunchConfig

Optional job launch behaviour for input files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_unindexed_files** | **bool** | When false or omitted, the request is rejected if any input file is not indexed. When true, unindexed files are excluded and the job runs on indexed files only.  | [optional] 

## Example

```python
from biolevate_client.models.job_launch_config import JobLaunchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of JobLaunchConfig from a JSON string
job_launch_config_instance = JobLaunchConfig.from_json(json)
# print the JSON string representation of the object
print(JobLaunchConfig.to_json())

# convert the object into a dict
job_launch_config_dict = job_launch_config_instance.to_dict()
# create an instance of JobLaunchConfig from a dict
job_launch_config_from_dict = JobLaunchConfig.from_dict(job_launch_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


