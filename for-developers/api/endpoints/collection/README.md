# /api/v1/collection

Collections can store links to objects. It is possible to link other objects from **fylr** as well as foreign objects, unknown to **fylr**. Object links must be unique. Linked objects can be manually sorted.

### `POST /collection` — Create or update a collection.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /collection` — Create or update a collection.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection" method="put" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /collection/{collection_id}` — Retrieve a collection.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection/{collection_id}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /collection/{collection_id}` — Update collection.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection/{collection_id}" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /collection/{collection_id}` — Delete collection. All child collections will be deleted too.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/collection/{collection_id}" method="delete" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
