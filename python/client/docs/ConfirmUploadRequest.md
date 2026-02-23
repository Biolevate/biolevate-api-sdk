# ConfirmUploadRequest

Confirm presigned upload request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Full file key (must not end with &#39;/&#39;) | 

## Example

```python
from biolevate_client.models.confirm_upload_request import ConfirmUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmUploadRequest from a JSON string
confirm_upload_request_instance = ConfirmUploadRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmUploadRequest.to_json())

# convert the object into a dict
confirm_upload_request_dict = confirm_upload_request_instance.to_dict()
# create an instance of ConfirmUploadRequest from a dict
confirm_upload_request_from_dict = ConfirmUploadRequest.from_dict(confirm_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


