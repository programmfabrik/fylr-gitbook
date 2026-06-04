# /api/v1/right

Access the ACL definitions and the per-context **right presets** used elsewhere in the API (collections, objects, pools, ...).

### `GET /right` — List all right definitions known to this fylr instance.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/right" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /right/{context}/presets` — List right presets for a context.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/right/{context}/presets" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /right/{context}/presets` — Create or update right presets for a context.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/right/{context}/presets" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /right/{context}/presets/{presetId}` — Retrieve a single right preset.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/right/{context}/presets/{presetId}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /right/{context}/presets/{presetId}` — Delete a right preset.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/right/{context}/presets/{presetId}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
