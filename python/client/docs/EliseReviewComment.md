# EliseReviewComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**positions** | [**List[EliseDocumentStatementAllOfPositions]**](EliseDocumentStatementAllOfPositions.md) |  | [optional] 

## Example

```python
from biolevate_client.models.elise_review_comment import EliseReviewComment

# TODO update the JSON string below
json = "{}"
# create an instance of EliseReviewComment from a JSON string
elise_review_comment_instance = EliseReviewComment.from_json(json)
# print the JSON string representation of the object
print(EliseReviewComment.to_json())

# convert the object into a dict
elise_review_comment_dict = elise_review_comment_instance.to_dict()
# create an instance of EliseReviewComment from a dict
elise_review_comment_from_dict = EliseReviewComment.from_dict(elise_review_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


