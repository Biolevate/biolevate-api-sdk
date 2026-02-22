# biolevate_client.ExtractionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extraction_job**](ExtractionApi.md#create_extraction_job) | **POST** /api/core/extraction/jobs | Create extraction job
[**get_extraction_job**](ExtractionApi.md#get_extraction_job) | **GET** /api/core/extraction/jobs/{jobId} | Get extraction job
[**get_extraction_job_annotations**](ExtractionApi.md#get_extraction_job_annotations) | **GET** /api/core/extraction/jobs/{jobId}/annotations | Get extraction job annotations
[**get_extraction_job_inputs**](ExtractionApi.md#get_extraction_job_inputs) | **GET** /api/core/extraction/jobs/{jobId}/inputs | Get extraction job inputs
[**get_extraction_job_outputs**](ExtractionApi.md#get_extraction_job_outputs) | **GET** /api/core/extraction/jobs/{jobId}/results | Get extraction job outputs
[**list_extraction_jobs**](ExtractionApi.md#list_extraction_jobs) | **GET** /api/core/extraction/jobs | List extraction jobs


# **create_extraction_job**
> Job create_extraction_job(create_extract_request)

Create extraction job

Creates a new metadata extraction job on the specified files

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.create_extract_request import CreateExtractRequest
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
    api_instance = biolevate_client.ExtractionApi(api_client)
    create_extract_request = biolevate_client.CreateExtractRequest() # CreateExtractRequest | 

    try:
        # Create extraction job
        api_response = await api_instance.create_extraction_job(create_extract_request)
        print("The response of ExtractionApi->create_extraction_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtractionApi->create_extraction_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_extract_request** | [**CreateExtractRequest**](CreateExtractRequest.md)|  | 

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

# **get_extraction_job**
> Job get_extraction_job(job_id)

Get extraction job

Returns a single extraction job by its ID

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
    api_instance = biolevate_client.ExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get extraction job
        api_response = await api_instance.get_extraction_job(job_id)
        print("The response of ExtractionApi->get_extraction_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtractionApi->get_extraction_job: %s\n" % e)
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

# **get_extraction_job_annotations**
> List[EliseAnnotation] get_extraction_job_annotations(job_id)

Get extraction job annotations

Returns the document annotations generated by the extraction job

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
    api_instance = biolevate_client.ExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get extraction job annotations
        api_response = await api_instance.get_extraction_job_annotations(job_id)
        print("The response of ExtractionApi->get_extraction_job_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtractionApi->get_extraction_job_annotations: %s\n" % e)
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

# **get_extraction_job_inputs**
> ExtractJobInputs get_extraction_job_inputs(job_id)

Get extraction job inputs

Returns the input files and meta configurations used for the extraction job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.extract_job_inputs import ExtractJobInputs
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
    api_instance = biolevate_client.ExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get extraction job inputs
        api_response = await api_instance.get_extraction_job_inputs(job_id)
        print("The response of ExtractionApi->get_extraction_job_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtractionApi->get_extraction_job_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**ExtractJobInputs**](ExtractJobInputs.md)

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

# **get_extraction_job_outputs**
> ExtractJobOutputs get_extraction_job_outputs(job_id)

Get extraction job outputs

Returns the extracted metadata results from the job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.extract_job_outputs import ExtractJobOutputs
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
    api_instance = biolevate_client.ExtractionApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get extraction job outputs
        api_response = await api_instance.get_extraction_job_outputs(job_id)
        print("The response of ExtractionApi->get_extraction_job_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtractionApi->get_extraction_job_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**ExtractJobOutputs**](ExtractJobOutputs.md)

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

# **list_extraction_jobs**
> PageDataJob list_extraction_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)

List extraction jobs

Returns a paginated list of extraction jobs for the current user

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
    api_instance = biolevate_client.ExtractionApi(api_client)
    page_size = 56 # int | Page size
    page = 56 # int | Page number
    sort_property = 'sort_property_example' # str | Sort property (optional)
    sort_order = 'sort_order_example' # str | Sort order (optional)

    try:
        # List extraction jobs
        api_response = await api_instance.list_extraction_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)
        print("The response of ExtractionApi->list_extraction_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtractionApi->list_extraction_jobs: %s\n" % e)
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

