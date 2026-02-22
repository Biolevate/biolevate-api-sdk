# UploadUrlRequest

Request for presigned upload URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Target directory path | 
**file_name** | **str** | File name | 
**size** | **int** | File size in bytes | [optional] 
**media_type** | **str** | Media type | [optional] 

## Example

```python
from biolevate_client.models.upload_url_request import UploadUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadUrlRequest from a JSON string
upload_url_request_instance = UploadUrlRequest.from_json(json)
# print the JSON string representation of the object
print(UploadUrlRequest.to_json())

# convert the object into a dict
upload_url_request_dict = upload_url_request_instance.to_dict()
# create an instance of UploadUrlRequest from a dict
upload_url_request_from_dict = UploadUrlRequest.from_dict(upload_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


