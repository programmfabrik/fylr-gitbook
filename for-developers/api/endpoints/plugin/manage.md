# /api/v1/plugin/manage

Management API for installed plugins. Every operation requires the
system right `system.root` or `system.plugin`; a request lacking
both (including an unauthenticated request) is rejected with
`code: SystemRightRequired` (403).

### `GET /plugin/manage` — List all installed plugins.
{% swagger src="../fylr-openapi.yml" path="/plugin/manage" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `PUT /plugin/manage` — Create (install) a plugin.
{% swagger src="../fylr-openapi.yml" path="/plugin/manage" method="put" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /plugin/manage/{id}` — Read one installed plugin.
{% swagger src="../fylr-openapi.yml" path="/plugin/manage/{id}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /plugin/manage/{id}` — Update an installed plugin.
{% swagger src="../fylr-openapi.yml" path="/plugin/manage/{id}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `DELETE /plugin/manage/{id}` — Delete (uninstall) a plugin.
{% swagger src="../fylr-openapi.yml" path="/plugin/manage/{id}" method="delete" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
