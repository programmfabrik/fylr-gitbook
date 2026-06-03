# /api/right

Access the ACL definitions and the per-context **right presets**
used elsewhere in the API (collections, objects, pools, ...).

### `GET /right` — List all right definitions known to this fylr instance.
{% swagger src="./fylr-openapi.yml" path="/right" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /right/{context}/presets` — List right presets for a context.
{% swagger src="./fylr-openapi.yml" path="/right/{context}/presets" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /right/{context}/presets` — Create or update right presets for a context.
{% swagger src="./fylr-openapi.yml" path="/right/{context}/presets" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /right/{context}/presets/{presetId}` — Retrieve a single right preset.
{% swagger src="./fylr-openapi.yml" path="/right/{context}/presets/{presetId}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /right/{context}/presets/{presetId}` — Delete a right preset.
{% swagger src="./fylr-openapi.yml" path="/right/{context}/presets/{presetId}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
