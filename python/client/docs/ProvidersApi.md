# biolevate_client.ProvidersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provider**](ProvidersApi.md#get_provider) | **GET** /api/core/providers/{id} | Get a provider
[**list_providers**](ProvidersApi.md#list_providers) | **GET** /api/core/providers | List providers


# **get_provider**
> FSProviderExternal get_provider(id)

Get a provider

Returns a single storage provider by its ID. Secret fields are redacted.

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.fs_provider_external import FSProviderExternal
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
    api_instance = biolevate_client.ProvidersApi(api_client)
    id = 'id_example' # str | Provider ID

    try:
        # Get a provider
        api_response = await api_instance.get_provider(id)
        print("The response of ProvidersApi->get_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->get_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Provider ID | 

### Return type

[**FSProviderExternal**](FSProviderExternal.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Successfully retrieved provider |  -  |
**404** | Provider not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> PageDataFSProviderExternal list_providers(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, q=q)

List providers

Returns a paginated list of storage providers the caller has access to. Secret fields are redacted.

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.page_data_fs_provider_external import PageDataFSProviderExternal
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
    api_instance = biolevate_client.ProvidersApi(api_client)
    page = 0 # int | Page number (0-based) (optional) (default to 0)
    page_size = 20 # int | Page size (optional) (default to 20)
    sort_by = 'sort_by_example' # str | Sort field (optional)
    sort_order = 'asc' # str | Sort direction (asc/desc) (optional) (default to 'asc')
    q = 'q_example' # str | Text search filter (optional)

    try:
        # List providers
        api_response = await api_instance.list_providers(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, q=q)
        print("The response of ProvidersApi->list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->list_providers: %s\n" % e)
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

[**PageDataFSProviderExternal**](PageDataFSProviderExternal.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved providers |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

