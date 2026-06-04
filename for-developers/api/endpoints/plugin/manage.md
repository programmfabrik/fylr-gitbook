# /manage

Management API for installed plugins. Every operation requires the system right `system.root` or `system.plugin`; a request lacking both (including an unauthenticated request) is rejected with `code: SystemRightRequired` (403).

### `GET /plugin/manage` — List all installed plugins.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /plugin/manage` — Create (install) a plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage" method="put" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/manage/{id}` — Read one installed plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage/{id}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /plugin/manage/{id}` — Update an installed plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage/{id}" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /plugin/manage/{id}` — Delete (uninstall) a plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage/{id}" method="delete" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
