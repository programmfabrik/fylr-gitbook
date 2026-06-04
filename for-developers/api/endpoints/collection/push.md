# /api/v1/collection/push

Append objects to the end of the collection identified by `collectionId`,
in request order. Objects already linked are moved to the end. The
collection `_version` is not changed.

### `POST /collection/push/{collection_id}` — Append objects to a collection.
{% swagger src="../fylr-openapi.yml" path="/collection/push/{collection_id}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
