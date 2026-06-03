# biolevate_client.AgentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_job**](AgentApi.md#create_agent_job) | **POST** /api/core/agent/jobs | Create agent job
[**get_agent_job**](AgentApi.md#get_agent_job) | **GET** /api/core/agent/jobs/{jobId} | Get agent job
[**get_agent_job_annotations**](AgentApi.md#get_agent_job_annotations) | **GET** /api/core/agent/jobs/{jobId}/annotations | Get agent job annotations
[**get_agent_job_inputs**](AgentApi.md#get_agent_job_inputs) | **GET** /api/core/agent/jobs/{jobId}/inputs | Get agent job inputs
[**get_agent_job_outputs**](AgentApi.md#get_agent_job_outputs) | **GET** /api/core/agent/jobs/{jobId}/results | Get agent job outputs
[**list_agent_jobs**](AgentApi.md#list_agent_jobs) | **GET** /api/core/agent/jobs | List agent jobs


# **create_agent_job**
> Job create_agent_job(authorization, create_agent_request, idempotency_key=idempotency_key)

Create agent job

Schedules an asynchronous agent run and returns the initial Job (status PENDING).

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.create_agent_request import CreateAgentRequest
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
    api_instance = biolevate_client.AgentApi(api_client)
    authorization = 'authorization_example' # str | 
    create_agent_request = biolevate_client.CreateAgentRequest() # CreateAgentRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Create agent job
        api_response = await api_instance.create_agent_job(authorization, create_agent_request, idempotency_key=idempotency_key)
        print("The response of AgentApi->create_agent_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->create_agent_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **create_agent_request** | [**CreateAgentRequest**](CreateAgentRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

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

# **get_agent_job**
> Job get_agent_job(job_id, authorization)

Get agent job

Returns a single agent job by its ID

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
    api_instance = biolevate_client.AgentApi(api_client)
    job_id = 'job_id_example' # str | The job Id
    authorization = 'authorization_example' # str | 

    try:
        # Get agent job
        api_response = await api_instance.get_agent_job(job_id, authorization)
        print("The response of AgentApi->get_agent_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_agent_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 
 **authorization** | **str**|  | 

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

# **get_agent_job_annotations**
> List[EliseAnnotation] get_agent_job_annotations(job_id, authorization)

Get agent job annotations

Returns the document annotations the agent cited in its answer

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
    api_instance = biolevate_client.AgentApi(api_client)
    job_id = 'job_id_example' # str | The job Id
    authorization = 'authorization_example' # str | 

    try:
        # Get agent job annotations
        api_response = await api_instance.get_agent_job_annotations(job_id, authorization)
        print("The response of AgentApi->get_agent_job_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_agent_job_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 
 **authorization** | **str**|  | 

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

# **get_agent_job_inputs**
> AgentJobInputs get_agent_job_inputs(job_id, authorization)

Get agent job inputs

Returns the messages, files and configuration submitted for the agent job

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.agent_job_inputs import AgentJobInputs
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
    api_instance = biolevate_client.AgentApi(api_client)
    job_id = 'job_id_example' # str | The job Id
    authorization = 'authorization_example' # str | 

    try:
        # Get agent job inputs
        api_response = await api_instance.get_agent_job_inputs(job_id, authorization)
        print("The response of AgentApi->get_agent_job_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_agent_job_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 
 **authorization** | **str**|  | 

### Return type

[**AgentJobInputs**](AgentJobInputs.md)

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

# **get_agent_job_outputs**
> AgentJobOutputs get_agent_job_outputs(job_id, authorization)

Get agent job outputs

Returns the agent's answer (text or structured), explanation, and cited annotation ids

### Example

* Bearer (JWT) Authentication (TOKEN):

```python
import biolevate_client
from biolevate_client.models.agent_job_outputs import AgentJobOutputs
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
    api_instance = biolevate_client.AgentApi(api_client)
    job_id = 'job_id_example' # str | The job Id
    authorization = 'authorization_example' # str | 

    try:
        # Get agent job outputs
        api_response = await api_instance.get_agent_job_outputs(job_id, authorization)
        print("The response of AgentApi->get_agent_job_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->get_agent_job_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job Id | 
 **authorization** | **str**|  | 

### Return type

[**AgentJobOutputs**](AgentJobOutputs.md)

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

# **list_agent_jobs**
> PageDataJob list_agent_jobs(page_size, page, authorization, conversation_id=conversation_id)

List agent jobs

Returns a paginated list of agent jobs for the current user, ordered by creation time (most recent first). When `conversationId` is provided, the results are restricted to jobs attached to that conversation, which lets a client replay the sequence of questions asked in a single conversation.

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
    api_instance = biolevate_client.AgentApi(api_client)
    page_size = 56 # int | Page size
    page = 56 # int | Page number (0-based)
    authorization = 'authorization_example' # str | 
    conversation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Restrict the results to jobs attached to this conversation (optional)

    try:
        # List agent jobs
        api_response = await api_instance.list_agent_jobs(page_size, page, authorization, conversation_id=conversation_id)
        print("The response of AgentApi->list_agent_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->list_agent_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | 
 **page** | **int**| Page number (0-based) | 
 **authorization** | **str**|  | 
 **conversation_id** | **UUID**| Restrict the results to jobs attached to this conversation | [optional] 

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

