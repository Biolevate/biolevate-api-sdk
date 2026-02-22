# PageDataEliseFileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EliseFileInfo]**](EliseFileInfo.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 

## Example

```python
from biolevate_client.models.page_data_elise_file_info import PageDataEliseFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageDataEliseFileInfo from a JSON string
page_data_elise_file_info_instance = PageDataEliseFileInfo.from_json(json)
# print the JSON string representation of the object
print(PageDataEliseFileInfo.to_json())

# convert the object into a dict
page_data_elise_file_info_dict = page_data_elise_file_info_instance.to_dict()
# create an instance of PageDataEliseFileInfo from a dict
page_data_elise_file_info_from_dict = PageDataEliseFileInfo.from_dict(page_data_elise_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


