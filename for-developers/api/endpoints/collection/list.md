# /list

List and create collections. `GET` returns every collection the user has `BAG_READ` for, as a flat array (not nested into a tree); `PUT` creates new collections from an array payload.

### `GET /collection/list` — Retrieve a list of collections.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection/list" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /collection/list` — Create new collections.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection/list" method="put" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /collection/list/{parentId}` — Retrieve all children of the given parent collection. This returns only the immediate children.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection/list/{parentId}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
