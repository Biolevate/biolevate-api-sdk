# biolevate_client.QuestionAnsweringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_qa_job**](QuestionAnsweringApi.md#create_qa_job) | **POST** /api/core/qa/jobs | Create QA job
[**get_qa_job**](QuestionAnsweringApi.md#get_qa_job) | **GET** /api/core/qa/jobs/{jobId} | Get QA job
[**get_qa_job_annotations**](QuestionAnsweringApi.md#get_qa_job_annotations) | **GET** /api/core/qa/jobs/{jobId}/annotations | Get QA job annotations
[**get_qa_job_inputs**](QuestionAnsweringApi.md#get_qa_job_inputs) | **GET** /api/core/qa/jobs/{jobId}/inputs | Get QA job inputs
[**get_qa_job_outputs**](QuestionAnsweringApi.md#get_qa_job_outputs) | **GET** /api/core/qa/jobs/{jobId}/results | Get QA job outputs
[**list_qa_jobs**](QuestionAnsweringApi.md#list_qa_jobs) | **GET** /api/core/qa/jobs | List QA jobs


# **create_qa_job**
> Job create_qa_job(create_qa_request)

Create QA job

Creates a new question answering job on the specified files

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.create_qa_request import CreateQARequest
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
    api_instance = biolevate_client.QuestionAnsweringApi(api_client)
    create_qa_request = biolevate_client.CreateQARequest() # CreateQARequest | 

    try:
        # Create QA job
        api_response = await api_instance.create_qa_job(create_qa_request)
        print("The response of QuestionAnsweringApi->create_qa_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnsweringApi->create_qa_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_qa_request** | [**CreateQARequest**](CreateQARequest.md)|  | 

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

# **get_qa_job**
> Job get_qa_job(job_id)

Get QA job

Returns a single question answering job by its ID

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
    api_instance = biolevate_client.QuestionAnsweringApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get QA job
        api_response = await api_instance.get_qa_job(job_id)
        print("The response of QuestionAnsweringApi->get_qa_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnsweringApi->get_qa_job: %s\n" % e)
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

# **get_qa_job_annotations**
> List[EliseAnnotation] get_qa_job_annotations(job_id)

Get QA job annotations

Returns the document annotations generated by the QA job

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
    api_instance = biolevate_client.QuestionAnsweringApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get QA job annotations
        api_response = await api_instance.get_qa_job_annotations(job_id)
        print("The response of QuestionAnsweringApi->get_qa_job_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnsweringApi->get_qa_job_annotations: %s\n" % e)
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

# **get_qa_job_inputs**
> QAJobInputs get_qa_job_inputs(job_id)

Get QA job inputs

Returns the input files and questions used for the QA job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.qa_job_inputs import QAJobInputs
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
    api_instance = biolevate_client.QuestionAnsweringApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get QA job inputs
        api_response = await api_instance.get_qa_job_inputs(job_id)
        print("The response of QuestionAnsweringApi->get_qa_job_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnsweringApi->get_qa_job_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**QAJobInputs**](QAJobInputs.md)

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

# **get_qa_job_outputs**
> QAJobOutputs get_qa_job_outputs(job_id)

Get QA job outputs

Returns the answers and results from the QA job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.qa_job_outputs import QAJobOutputs
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
    api_instance = biolevate_client.QuestionAnsweringApi(api_client)
    job_id = 'job_id_example' # str | The job Id

    try:
        # Get QA job outputs
        api_response = await api_instance.get_qa_job_outputs(job_id)
        print("The response of QuestionAnsweringApi->get_qa_job_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnsweringApi->get_qa_job_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 

### Return type

[**QAJobOutputs**](QAJobOutputs.md)

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

# **list_qa_jobs**
> PageDataJob list_qa_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)

List QA jobs

Returns a paginated list of question answering jobs for the current user

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
    api_instance = biolevate_client.QuestionAnsweringApi(api_client)
    page_size = 56 # int | Page size
    page = 56 # int | Page number
    sort_property = 'sort_property_example' # str | Sort property (optional)
    sort_order = 'sort_order_example' # str | Sort order (optional)

    try:
        # List QA jobs
        api_response = await api_instance.list_qa_jobs(page_size, page, sort_property=sort_property, sort_order=sort_order)
        print("The response of QuestionAnsweringApi->list_qa_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAnsweringApi->list_qa_jobs: %s\n" % e)
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

