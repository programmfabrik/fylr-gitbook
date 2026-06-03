# /api/collection/remove

Unlink the listed objects from the collection identified by
`collectionId`. The body is a bare JSON array of objects (each by
`_global_object_id` or `lookup:_global_object_id`); if any object is not
currently linked the call fails with `400 CollectionRemoveNotAllObjectsFound`.
The collection `_version` is not changed.

### `POST /collection/remove/{collection_id}` — Remove the listed objects from a collection.
{% swagger src="../fylr-openapi.yml" path="/collection/remove/{collection_id}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
