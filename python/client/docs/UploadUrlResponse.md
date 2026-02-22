# UploadUrlResponse

Presigned upload URL response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Presigned URL for direct upload (null if not supported) | [optional] 
**expires_in_seconds** | **int** | Time in seconds until the URL expires | [optional] 
**supported** | **bool** | Whether presigned upload is supported by this provider | [optional] 

## Example

```python
from biolevate_client.models.upload_url_response import UploadUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadUrlResponse from a JSON string
upload_url_response_instance = UploadUrlResponse.from_json(json)
# print the JSON string representation of the object
print(UploadUrlResponse.to_json())

# convert the object into a dict
upload_url_response_dict = upload_url_response_instance.to_dict()
# create an instance of UploadUrlResponse from a dict
upload_url_response_from_dict = UploadUrlResponse.from_dict(upload_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


