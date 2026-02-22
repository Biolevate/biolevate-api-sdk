# PageDataEliseCollectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EliseCollectionInfo]**](EliseCollectionInfo.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**has_next** | **bool** |  | [optional] 

## Example

```python
from biolevate_client.models.page_data_elise_collection_info import PageDataEliseCollectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageDataEliseCollectionInfo from a JSON string
page_data_elise_collection_info_instance = PageDataEliseCollectionInfo.from_json(json)
# print the JSON string representation of the object
print(PageDataEliseCollectionInfo.to_json())

# convert the object into a dict
page_data_elise_collection_info_dict = page_data_elise_collection_info_instance.to_dict()
# create an instance of PageDataEliseCollectionInfo from a dict
page_data_elise_collection_info_from_dict = PageDataEliseCollectionInfo.from_dict(page_data_elise_collection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


