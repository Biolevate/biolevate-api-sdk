# biolevate_client.FilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /api/core/files | Create a file
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /api/core/files/{id} | Delete a file
[**get_file**](FilesApi.md#get_file) | **GET** /api/core/files/{id} | Get a file
[**get_file_ontologies**](FilesApi.md#get_file_ontologies) | **GET** /api/core/files/{id}/ontologies | Get file ontologies
[**list_files**](FilesApi.md#list_files) | **GET** /api/core/files | List files in a provider
[**recompute_file_ontologies**](FilesApi.md#recompute_file_ontologies) | **POST** /api/core/files/{id}/recompute-ontologies | Recompute file ontologies
[**reindex_file**](FilesApi.md#reindex_file) | **POST** /api/core/files/{id}/reindex | Reindex a file


# **create_file**
> EliseFileInfo create_file(create_file_request)

Create a file

Creates an EliseFile from an existing provider item and triggers indexation

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.create_file_request import CreateFileRequest
from biolevate_client.models.elise_file_info import EliseFileInfo
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
    api_instance = biolevate_client.FilesApi(api_client)
    create_file_request = biolevate_client.CreateFileRequest() # CreateFileRequest | 

    try:
        # Create a file
        api_response = await api_instance.create_file(create_file_request)
        print("The response of FilesApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_file_request** | [**CreateFileRequest**](CreateFileRequest.md)|  | 

### Return type

[**EliseFileInfo**](EliseFileInfo.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | File created successfully |  -  |
**400** | Invalid request or unsupported file extension |  -  |
**404** | File not found in provider |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(id)

Delete a file

Deletes a file

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
    api_instance = biolevate_client.FilesApi(api_client)
    id = 'id_example' # str | File ID

    try:
        # Delete a file
        await api_instance.delete_file(id)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File ID | 

### Return type

void (empty response body)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**204** | File deleted successfully |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> EliseFileInfo get_file(id)

Get a file

Returns a file by its ID

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.elise_file_info import EliseFileInfo
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
    api_instance = biolevate_client.FilesApi(api_client)
    id = 'id_example' # str | File ID

    try:
        # Get a file
        api_response = await api_instance.get_file(id)
        print("The response of FilesApi->get_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File ID | 

### Return type

[**EliseFileInfo**](EliseFileInfo.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Successfully retrieved file |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_ontologies**
> List[EliseOntology] get_file_ontologies(id)

Get file ontologies

Returns computed ontologies for a file

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.elise_ontology import EliseOntology
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
    api_instance = biolevate_client.FilesApi(api_client)
    id = 'id_example' # str | File ID

    try:
        # Get file ontologies
        api_response = await api_instance.get_file_ontologies(id)
        print("The response of FilesApi->get_file_ontologies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_ontologies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File ID | 

### Return type

[**List[EliseOntology]**](EliseOntology.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Successfully retrieved ontologies |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> PageDataEliseFileInfo list_files(provider_id, page_size, page, sort_property=sort_property, sort_order=sort_order)

List files in a provider

Returns paginated file infos for a provider

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.page_data_elise_file_info import PageDataEliseFileInfo
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
    api_instance = biolevate_client.FilesApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID
    page_size = 56 # int | Page size
    page = 56 # int | Page number
    sort_property = 'sort_property_example' # str | Sort property (optional)
    sort_order = 'sort_order_example' # str | Sort order (optional)

    try:
        # List files in a provider
        api_response = await api_instance.list_files(provider_id, page_size, page, sort_property=sort_property, sort_order=sort_order)
        print("The response of FilesApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID | 
 **page_size** | **int**| Page size | 
 **page** | **int**| Page number | 
 **sort_property** | **str**| Sort property | [optional] 
 **sort_order** | **str**| Sort order | [optional] 

### Return type

[**PageDataEliseFileInfo**](PageDataEliseFileInfo.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Successfully retrieved files |  -  |
**404** | Provider not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recompute_file_ontologies**
> recompute_file_ontologies(id)

Recompute file ontologies

Forces recomputation of ontologies and metadata for a file

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
    api_instance = biolevate_client.FilesApi(api_client)
    id = 'id_example' # str | File ID

    try:
        # Recompute file ontologies
        await api_instance.recompute_file_ontologies(id)
    except Exception as e:
        print("Exception when calling FilesApi->recompute_file_ontologies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File ID | 

### Return type

void (empty response body)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**202** | Ontology recomputation started |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reindex_file**
> reindex_file(id, reparse=reparse)

Reindex a file

Forces reindexation of a file. Optionally reparses the document.

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
    api_instance = biolevate_client.FilesApi(api_client)
    id = 'id_example' # str | File ID
    reparse = False # bool | Reparse document content (optional) (default to False)

    try:
        # Reindex a file
        await api_instance.reindex_file(id, reparse=reparse)
    except Exception as e:
        print("Exception when calling FilesApi->reindex_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File ID | 
 **reparse** | **bool**| Reparse document content | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Reindexation started |  -  |
**403** | Access denied |  -  |
**404** | File not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

