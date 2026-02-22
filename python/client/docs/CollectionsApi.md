# biolevate_client.CollectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_to_collection**](CollectionsApi.md#add_file_to_collection) | **POST** /api/core/collections/{id}/files | Add file to collection
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /api/core/collections | Create a collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /api/core/collections/{id} | Delete a collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /api/core/collections/{id} | Get a collection
[**list_collection_files**](CollectionsApi.md#list_collection_files) | **GET** /api/core/collections/{id}/files | List files in collection
[**list_collections**](CollectionsApi.md#list_collections) | **GET** /api/core/collections | List collections
[**remove_file_from_collection**](CollectionsApi.md#remove_file_from_collection) | **DELETE** /api/core/collections/{id}/files/{fileId} | Remove file from collection
[**update_collection**](CollectionsApi.md#update_collection) | **PATCH** /api/core/collections/{id} | Update a collection


# **add_file_to_collection**
> EliseFileInfo add_file_to_collection(id, add_file_to_collection_request)

Add file to collection

Associates an existing file with the collection

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.add_file_to_collection_request import AddFileToCollectionRequest
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
    api_instance = biolevate_client.CollectionsApi(api_client)
    id = 'id_example' # str | Collection ID
    add_file_to_collection_request = biolevate_client.AddFileToCollectionRequest() # AddFileToCollectionRequest | 

    try:
        # Add file to collection
        api_response = await api_instance.add_file_to_collection(id, add_file_to_collection_request)
        print("The response of CollectionsApi->add_file_to_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->add_file_to_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **add_file_to_collection_request** | [**AddFileToCollectionRequest**](AddFileToCollectionRequest.md)|  | 

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
**403** | Access denied |  -  |
**404** | Collection or file not found |  -  |
**201** | File added to collection |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> EliseCollectionInfo create_collection(create_collection_request)

Create a collection

Creates a new collection owned by the current user

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.create_collection_request import CreateCollectionRequest
from biolevate_client.models.elise_collection_info import EliseCollectionInfo
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
    api_instance = biolevate_client.CollectionsApi(api_client)
    create_collection_request = biolevate_client.CreateCollectionRequest() # CreateCollectionRequest | 

    try:
        # Create a collection
        api_response = await api_instance.create_collection(create_collection_request)
        print("The response of CollectionsApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collection_request** | [**CreateCollectionRequest**](CreateCollectionRequest.md)|  | 

### Return type

[**EliseCollectionInfo**](EliseCollectionInfo.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Collection created successfully |  -  |
**400** | Invalid request body |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> delete_collection(id)

Delete a collection

Deletes a collection. Only the owner can delete a collection.

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
    api_instance = biolevate_client.CollectionsApi(api_client)
    id = 'id_example' # str | Collection ID

    try:
        # Delete a collection
        await api_instance.delete_collection(id)
    except Exception as e:
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

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
**204** | Collection deleted successfully |  -  |
**403** | Access denied - only owner can delete |  -  |
**404** | Collection not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> EliseCollectionInfo get_collection(id)

Get a collection

Returns a single collection by its ID

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.elise_collection_info import EliseCollectionInfo
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
    api_instance = biolevate_client.CollectionsApi(api_client)
    id = 'id_example' # str | Collection ID

    try:
        # Get a collection
        api_response = await api_instance.get_collection(id)
        print("The response of CollectionsApi->get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

[**EliseCollectionInfo**](EliseCollectionInfo.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Successfully retrieved collection |  -  |
**404** | Collection not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collection_files**
> PageDataEliseFileInfo list_collection_files(id, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, q=q)

List files in collection

Returns a paginated list of files belonging to the collection

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
    api_instance = biolevate_client.CollectionsApi(api_client)
    id = 'id_example' # str | Collection ID
    page = 0 # int | Page number (0-based) (optional) (default to 0)
    page_size = 20 # int | Page size (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Sort field (optional)
    sort_order = 'asc' # str | Sort direction (asc/desc) (optional) (default to 'asc')
    q = 'q_example' # str | Text search filter (optional)

    try:
        # List files in collection
        api_response = await api_instance.list_collection_files(id, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, q=q)
        print("The response of CollectionsApi->list_collection_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->list_collection_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **page** | **int**| Page number (0-based) | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]
 **sort_by** | **str**| Sort field | [optional] 
 **sort_order** | **str**| Sort direction (asc/desc) | [optional] [default to &#39;asc&#39;]
 **q** | **str**| Text search filter | [optional] 

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
**404** | Collection not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> PageDataEliseCollectionInfo list_collections(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, q=q)

List collections

Returns a paginated list of collections the caller has access to

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.page_data_elise_collection_info import PageDataEliseCollectionInfo
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
    api_instance = biolevate_client.CollectionsApi(api_client)
    page = 0 # int | Page number (0-based) (optional) (default to 0)
    page_size = 20 # int | Page size (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Sort field (optional)
    sort_order = 'asc' # str | Sort direction (asc/desc) (optional) (default to 'asc')
    q = 'q_example' # str | Text search filter (optional)

    try:
        # List collections
        api_response = await api_instance.list_collections(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, q=q)
        print("The response of CollectionsApi->list_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->list_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (0-based) | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]
 **sort_by** | **str**| Sort field | [optional] 
 **sort_order** | **str**| Sort direction (asc/desc) | [optional] [default to &#39;asc&#39;]
 **q** | **str**| Text search filter | [optional] 

### Return type

[**PageDataEliseCollectionInfo**](PageDataEliseCollectionInfo.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved collections |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_file_from_collection**
> remove_file_from_collection(id, file_id)

Remove file from collection

Removes the association between a file and the collection

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
    api_instance = biolevate_client.CollectionsApi(api_client)
    id = 'id_example' # str | Collection ID
    file_id = 'file_id_example' # str | File ID

    try:
        # Remove file from collection
        await api_instance.remove_file_from_collection(id, file_id)
    except Exception as e:
        print("Exception when calling CollectionsApi->remove_file_from_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **file_id** | **str**| File ID | 

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
**204** | File removed from collection |  -  |
**404** | Collection or file not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> EliseCollectionInfo update_collection(id, update_collection_request)

Update a collection

Partially updates a collection. Only provided fields will be updated.

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.elise_collection_info import EliseCollectionInfo
from biolevate_client.models.update_collection_request import UpdateCollectionRequest
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
    api_instance = biolevate_client.CollectionsApi(api_client)
    id = 'id_example' # str | Collection ID
    update_collection_request = biolevate_client.UpdateCollectionRequest() # UpdateCollectionRequest | 

    try:
        # Update a collection
        api_response = await api_instance.update_collection(id, update_collection_request)
        print("The response of CollectionsApi->update_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **update_collection_request** | [**UpdateCollectionRequest**](UpdateCollectionRequest.md)|  | 

### Return type

[**EliseCollectionInfo**](EliseCollectionInfo.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**400** | Invalid request body |  -  |
**200** | Collection updated successfully |  -  |
**404** | Collection not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

