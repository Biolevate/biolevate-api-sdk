# DownloadUrlResponse

Download URL response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to download the file | [optional] 
**expires_in_seconds** | **int** | Time in seconds until the URL expires | [optional] 

## Example

```python
from biolevate_client.models.download_url_response import DownloadUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadUrlResponse from a JSON string
download_url_response_instance = DownloadUrlResponse.from_json(json)
# print the JSON string representation of the object
print(DownloadUrlResponse.to_json())

# convert the object into a dict
download_url_response_dict = download_url_response_instance.to_dict()
# create an instance of DownloadUrlResponse from a dict
download_url_response_from_dict = DownloadUrlResponse.from_dict(download_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


