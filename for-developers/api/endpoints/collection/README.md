# /api/collection

Collections can store links to objects. It is possible to link other objects
from **fylr** as well as foreign objects, unknown to **fylr**. Object links must be unique.
Linked objects can be manually sorted.

### `POST /collection` — Create or update a collection.
{% swagger src="../fylr-openapi.yml" path="/collection" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `PUT /collection` — Create or update a collection.
{% swagger src="../fylr-openapi.yml" path="/collection" method="put" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /collection/{collection_id}` — Retrieve a collection.
{% swagger src="../fylr-openapi.yml" path="/collection/{collection_id}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /collection/{collection_id}` — Update collection.
{% swagger src="../fylr-openapi.yml" path="/collection/{collection_id}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `DELETE /collection/{collection_id}` — Delete collection. All child collections will be deleted too.
{% swagger src="../fylr-openapi.yml" path="/collection/{collection_id}" method="delete" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
