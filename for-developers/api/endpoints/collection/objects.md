# /api/collection/objects

Read or replace the objects linked to the collection identified by
`collectionId`. `GET` returns the linked objects; `POST` replaces the
entire list, linking exactly the objects in the body and unlinking any
that are absent. The collection `_version` is not changed.

### `GET /collection/objects/{collection_id}` — Retrieve objects of a collection.
{% swagger src="../fylr-openapi.yml" path="/collection/objects/{collection_id}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /collection/objects/{collection_id}` — Replace objects of a collection.
{% swagger src="../fylr-openapi.yml" path="/collection/objects/{collection_id}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
