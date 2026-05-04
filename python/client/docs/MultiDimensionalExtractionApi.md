# biolevate_client.MultiDimensionalExtractionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mde_job**](MultiDimensionalExtractionApi.md#create_mde_job) | **POST** /api/core/multi-dim-extraction/jobs | Create multi-dimensional extraction job
[**get_mde_job**](MultiDimensionalExtractionApi.md#get_mde_job) | **GET** /api/core/multi-dim-extraction/jobs/{jobId} | Get multi-dimensional extraction job
[**get_mde_job_annotations**](MultiDimensionalExtractionApi.md#get_mde_job_annotations) | **GET** /api/core/multi-dim-extraction/jobs/{jobId}/annotations | Get multi-dimensional extraction job annotations
[**get_mde_job_inputs**](MultiDimensionalExtractionApi.md#get_mde_job_inputs) | **GET** /api/core/multi-dim-extraction/jobs/{jobId}/inputs | Get multi-dimensional extraction job inputs
[**get_mde_job_outputs**](MultiDimensionalExtractionApi.md#get_mde_job_outputs) | **GET** /api/core/multi-dim-extraction/jobs/{jobId}/results | Get multi-dimensional extraction job outputs
[**list_mde_jobs**](MultiDimensionalExtractionApi.md#list_mde_jobs) | **GET** /api/core/multi-dim-extraction/jobs | List multi-dimensional extraction jobs


# **create_mde_job**
> Job create_mde_job(create_mde_request)

Create multi-dimensional extraction job

Creates a new entity extraction job using a structured schema (multi-column) on the specified files

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.create_mde_request import CreateMDERequest
from biolevate_client.models.job import Job
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
    api_instance = biolevate_client.MultiDimensionalExtractionApi(api_client)
    create_mde_request = biolevate_client.CreateMDERequest() # CreateMDERequest | 

    try:
        # Create multi-dimensional extraction job
        api_response = await api_instance.create_mde_job(create_mde_request)
        print("The response of MultiDimensionalExtractionApi->create_mde_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiDimensionalExtractionApi->create_mde_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_mde_request** | [**CreateMDERequest**](CreateMDERequest.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied |  -  |
**200** | Job created successfully |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mde_job**
> Job get_mde_job(job_id)

Get multi-dimensional extraction job

Returns a single multi-dimensional extraction job by its ID

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.job import Job
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
    api_instance = biolevate_client.MultiDimensionalExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get multi-dimensional extraction job
        api_response = await api_instance.get_mde_job(job_id)
        print("The response of MultiDimensionalExtractionApi->get_mde_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiDimensionalExtractionApi->get_mde_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**Job**](Job.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved job |  -  |
**403** | Access denied - not the job owner |  -  |
**404** | Job not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mde_job_annotations**
> List[EliseAnnotation] get_mde_job_annotations(job_id)

Get multi-dimensional extraction job annotations

Returns the document annotations generated by the multi-dimensional extraction job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.elise_annotation import EliseAnnotation
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
    api_instance = biolevate_client.MultiDimensionalExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get multi-dimensional extraction job annotations
        api_response = await api_instance.get_mde_job_annotations(job_id)
        print("The response of MultiDimensionalExtractionApi->get_mde_job_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiDimensionalExtractionApi->get_mde_job_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**List[EliseAnnotation]**](EliseAnnotation.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied - not the job owner |  -  |
**200** | Successfully retrieved annotations |  -  |
**404** | Job not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mde_job_inputs**
> MDEJobInputs get_mde_job_inputs(job_id)

Get multi-dimensional extraction job inputs

Returns the input files and entity schema used for the multi-dimensional extraction job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.mde_job_inputs import MDEJobInputs
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
    api_instance = biolevate_client.MultiDimensionalExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get multi-dimensional extraction job inputs
        api_response = await api_instance.get_mde_job_inputs(job_id)
        print("The response of MultiDimensionalExtractionApi->get_mde_job_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiDimensionalExtractionApi->get_mde_job_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**MDEJobInputs**](MDEJobInputs.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied - not the job owner |  -  |
**200** | Successfully retrieved inputs |  -  |
**404** | Job not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mde_job_outputs**
> MDEJobOutputs get_mde_job_outputs(job_id)

Get multi-dimensional extraction job outputs

Returns the entity extraction results from the multi-dimensional extraction job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.mde_job_outputs import MDEJobOutputs
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
    api_instance = biolevate_client.MultiDimensionalExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get multi-dimensional extraction job outputs
        api_response = await api_instance.get_mde_job_outputs(job_id)
        print("The response of MultiDimensionalExtractionApi->get_mde_job_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiDimensionalExtractionApi->get_mde_job_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**MDEJobOutputs**](MDEJobOutputs.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access denied - not the job owner |  -  |
**200** | Successfully retrieved outputs |  -  |
**404** | Job not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mde_jobs**
> PageDataJob list_mde_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)

List multi-dimensional extraction jobs

Returns a paginated list of multi-dimensional extraction jobs for the current user

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.page_data_job import PageDataJob
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
    api_instance = biolevate_client.MultiDimensionalExtractionApi(api_client)
    page_size = 56 # int | Page size
    page = 56 # int | Page number
    sort_property = 'sort_property_example' # str | Sort property (optional)
    sort_order = 'sort_order_example' # str | Sort order (optional)

    try:
        # List multi-dimensional extraction jobs
        api_response = await api_instance.list_mde_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)
        print("The response of MultiDimensionalExtractionApi->list_mde_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiDimensionalExtractionApi->list_mde_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | 
 **page** | **int**| Page number | 
 **sort_property** | **str**| Sort property | [optional] 
 **sort_order** | **str**| Sort order | [optional] 

### Return type

[**PageDataJob**](PageDataJob.md)

### Authorization

[TOKEN](../README.md#TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved jobs |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

