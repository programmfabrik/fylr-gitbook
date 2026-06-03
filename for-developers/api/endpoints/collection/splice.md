# /api/collection/splice

Splice the object list of the collection identified by `collectionId`:
remove `count` objects at position `index` and insert the supplied
`objects` at that position. The request body is a single object carrying
the `index`, `count` and `objects` fields. The collection `_version` is
not changed.

### `POST /collection/splice/{collection_id}` — Remove and add objects to a collection.
{% swagger src="../fylr-openapi.yml" path="/collection/splice/{collection_id}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
