# biolevate_client.ProviderItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_upload**](ProviderItemsApi.md#confirm_upload) | **POST** /api/core/providers/{providerId}/items/confirm | Confirm presigned upload
[**delete_item**](ProviderItemsApi.md#delete_item) | **DELETE** /api/core/providers/{providerId}/items | Delete item
[**get_download_url**](ProviderItemsApi.md#get_download_url) | **GET** /api/core/providers/{providerId}/items/download-url | Get download URL
[**get_file_content**](ProviderItemsApi.md#get_file_content) | **GET** /api/core/providers/{providerId}/items/content | Get file content
[**get_upload_url**](ProviderItemsApi.md#get_upload_url) | **POST** /api/core/providers/{providerId}/items/upload-url | Get presigned upload URL
[**list_items**](ProviderItemsApi.md#list_items) | **GET** /api/core/providers/{providerId}/items | List items
[**rename_item**](ProviderItemsApi.md#rename_item) | **PATCH** /api/core/providers/{providerId}/items | Rename item
[**upload_file**](ProviderItemsApi.md#upload_file) | **POST** /api/core/providers/{providerId}/items | Create folder


# **confirm_upload**
> ProviderItem confirm_upload(provider_id, confirm_upload_request)

Confirm presigned upload

Confirms that a file was uploaded via presigned URL

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.confirm_upload_request import ConfirmUploadRequest
from biolevate_client.models.provider_item import ProviderItem
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    confirm_upload_request = biolevate_client.ConfirmUploadRequest() # ConfirmUploadRequest | 

    try:
        # Confirm presigned upload
        api_response = await api_instance.confirm_upload(provider_id, confirm_upload_request)
        print("The response of ProviderItemsApi->confirm_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->confirm_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **confirm_upload_request** | [**ConfirmUploadRequest**](ConfirmUploadRequest.md)|  | 

### Return type

[**ProviderItem**](ProviderItem.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload confirmed |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(provider_id, item_reference)

Delete item

Deletes a file or folder

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.item_reference import ItemReference
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    item_reference = biolevate_client.ItemReference() # ItemReference | 

    try:
        # Delete item
        await api_instance.delete_item(provider_id, item_reference)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->delete_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **item_reference** | [**ItemReference**](ItemReference.md)|  | 

### Return type

void (empty response body)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**404** | Item not found |  -  |
**204** | Item deleted |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_url**
> DownloadUrlResponse get_download_url(provider_id, key, expiration_minutes=expiration_minutes)

Get download URL

Returns a URL to download the file

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.download_url_response import DownloadUrlResponse
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    key = 'key_example' # str | File key (must not end with '/')
    expiration_minutes = 15 # int | URL expiration in minutes (optional) (default to 15)

    try:
        # Get download URL
        api_response = await api_instance.get_download_url(provider_id, key, expiration_minutes=expiration_minutes)
        print("The response of ProviderItemsApi->get_download_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->get_download_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **key** | **str**| File key (must not end with &#39;/&#39;) | 
 **expiration_minutes** | **int**| URL expiration in minutes | [optional] [default to 15]

### Return type

[**DownloadUrlResponse**](DownloadUrlResponse.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Download URL generated |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_content**
> bytearray get_file_content(provider_id, key)

Get file content

Returns the raw file content (proxy for providers without presigned URLs)

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    key = 'key_example' # str | File key (must not end with '/')

    try:
        # Get file content
        api_response = await api_instance.get_file_content(provider_id, key)
        print("The response of ProviderItemsApi->get_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->get_file_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **key** | **str**| File key (must not end with &#39;/&#39;) | 

### Return type

**bytearray**

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | File content |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_url**
> UploadUrlResponse get_upload_url(provider_id, upload_url_request)

Get presigned upload URL

Returns a presigned URL for direct upload to storage (for large files)

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.upload_url_request import UploadUrlRequest
from biolevate_client.models.upload_url_response import UploadUrlResponse
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    upload_url_request = biolevate_client.UploadUrlRequest() # UploadUrlRequest | 

    try:
        # Get presigned upload URL
        api_response = await api_instance.get_upload_url(provider_id, upload_url_request)
        print("The response of ProviderItemsApi->get_upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->get_upload_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **upload_url_request** | [**UploadUrlRequest**](UploadUrlRequest.md)|  | 

### Return type

[**UploadUrlResponse**](UploadUrlResponse.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Upload URL generated |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_items**
> ListItemsResponse list_items(provider_id, key=key, q=q, cursor=cursor, limit=limit)

List items

Returns a paginated list of files and folders in the specified directory

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.list_items_response import ListItemsResponse
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    key = '' # str | Directory key (must end with '/' or be empty for root) (optional) (default to '')
    q = 'q_example' # str | Name filter (optional)
    cursor = 'cursor_example' # str | Pagination cursor (optional)
    limit = 50 # int | Max items to return (optional) (default to 50)

    try:
        # List items
        api_response = await api_instance.list_items(provider_id, key=key, q=q, cursor=cursor, limit=limit)
        print("The response of ProviderItemsApi->list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **key** | **str**| Directory key (must end with &#39;/&#39; or be empty for root) | [optional] [default to &#39;&#39;]
 **q** | **str**| Name filter | [optional] 
 **cursor** | **str**| Pagination cursor | [optional] 
 **limit** | **int**| Max items to return | [optional] [default to 50]

### Return type

[**ListItemsResponse**](ListItemsResponse.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**404** | Provider not found |  -  |
**200** | Successfully retrieved items |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_item**
> ProviderItem rename_item(provider_id, new_name, item_reference)

Rename item

Renames a file or folder

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.item_reference import ItemReference
from biolevate_client.models.provider_item import ProviderItem
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    new_name = 'new_name_example' # str | New name for the item
    item_reference = biolevate_client.ItemReference() # ItemReference | 

    try:
        # Rename item
        api_response = await api_instance.rename_item(provider_id, new_name, item_reference)
        print("The response of ProviderItemsApi->rename_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->rename_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **new_name** | **str**| New name for the item | 
 **item_reference** | [**ItemReference**](ItemReference.md)|  | 

### Return type

[**ProviderItem**](ProviderItem.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**404** | Item not found |  -  |
**400** | Invalid request or missing newName |  -  |
**200** | Item renamed |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ProviderItem upload_file(provider_id, file, key=key)

Create folder

Creates a new folder in the provider. Key must end with '/'.

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.provider_item import ProviderItem
from biolevate_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = biolevate_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): TOKEN
configuration = biolevate_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with biolevate_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = biolevate_client.ProviderItemsApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    file = None # bytearray | File to upload
    key = '' # str | Target directory key (must end with '/' or be empty for root) (optional) (default to '')

    try:
        # Create folder
        api_response = await api_instance.upload_file(provider_id, file, key=key)
        print("The response of ProviderItemsApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProviderItemsApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **file** | **bytearray**| File to upload | 
 **key** | **str**| Target directory key (must end with &#39;/&#39; or be empty for root) | [optional] [default to &#39;&#39;]

### Return type

[**ProviderItem**](ProviderItem.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**201** | Folder created |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

