# biolevate_client.FindSimilarFilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](FindSimilarFilesApi.md#create_job) | **POST** /api/core/find-similar/jobs | Create find-similar job
[**get_job**](FindSimilarFilesApi.md#get_job) | **GET** /api/core/find-similar/jobs/{jobId} | Get find-similar job
[**list_jobs**](FindSimilarFilesApi.md#list_jobs) | **GET** /api/core/find-similar/jobs | List find-similar jobs


# **create_job**
> FindSimilarApiJobDto create_job(search_sources)

Create find-similar job

Creates a find-similar job for the supplied source identifiers. The endpoint returns immediately with a PENDING/RUNNING job; poll GET /find-similar/jobs/{id} for completion.

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.find_similar_api_job_dto import FindSimilarApiJobDto
from biolevate_client.models.search_sources import SearchSources
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
    api_instance = biolevate_client.FindSimilarFilesApi(api_client)
    search_sources = biolevate_client.SearchSources() # SearchSources | 

    try:
        # Create find-similar job
        api_response = await api_instance.create_job(search_sources)
        print("The response of FindSimilarFilesApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindSimilarFilesApi->create_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_sources** | [**SearchSources**](SearchSources.md)|  | 

### Return type

[**FindSimilarApiJobDto**](FindSimilarApiJobDto.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid SearchSources |  -  |
**200** | Job created |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> FindSimilarApiJobDto get_job(job_id)

Get find-similar job

Returns a find-similar job by id, including the unified result and statistics when COMPLETED.

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.find_similar_api_job_dto import FindSimilarApiJobDto
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
    api_instance = biolevate_client.FindSimilarFilesApi(api_client)
    job_id = 'job_id_example' # str | The job id

    try:
        # Get find-similar job
        api_response = await api_instance.get_job(job_id)
        print("The response of FindSimilarFilesApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindSimilarFilesApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job id | 

### Return type

[**FindSimilarApiJobDto**](FindSimilarApiJobDto.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied - not the job owner |  -  |
**200** | Job retrieved |  -  |
**404** | Job not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> PageDataFindSimilarApiJobDto list_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)

List find-similar jobs

Returns a paginated list of find-similar jobs owned by the current user.

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.page_data_find_similar_api_job_dto import PageDataFindSimilarApiJobDto
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
    api_instance = biolevate_client.FindSimilarFilesApi(api_client)
    page_size = 56 # int | Page size
    page = 56 # int | Page number
    sort_property = 'sort_property_example' # str | Sort property (optional)
    sort_order = 'sort_order_example' # str | Sort order (optional)

    try:
        # List find-similar jobs
        api_response = await api_instance.list_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)
        print("The response of FindSimilarFilesApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindSimilarFilesApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | 
 **page** | **int**| Page number | 
 **sort_property** | **str**| Sort property | [optional] 
 **sort_order** | **str**| Sort order | [optional] 

### Return type

[**PageDataFindSimilarApiJobDto**](PageDataFindSimilarApiJobDto.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jobs retrieved |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

