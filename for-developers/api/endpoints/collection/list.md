# /api/collection/list

List and create collections. `GET` returns every collection the user has
`BAG_READ` for, as a flat array (not nested into a tree); `PUT` creates new
collections from an array payload.

### `GET /collection/list` — Retrieve a list of collections.
{% swagger src="../fylr-openapi.yml" path="/collection/list" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `PUT /collection/list` — Create new collections.
{% swagger src="../fylr-openapi.yml" path="/collection/list" method="put" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /collection/list/{parentId}` — Retrieve all children of the given parent collection. This returns only the immediate children.
{% swagger src="../fylr-openapi.yml" path="/collection/list/{parentId}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
