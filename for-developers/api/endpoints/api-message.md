# /api/v1/message

Admin-managed **fylr** messages shown in the web front end, optionally requiring per-user confirmation (`confirm_every_version`, `show_always`) and optionally scoped to a `start_time`/`end_time` window. A message is addressed to user groups via `_groups`, not to individual users. All operations require the `system.message` system right (or `system.root`); a user who holds it sees and manages every message — there is no per-user sender/recipient scoping.

Differs from easydb 5: the message kind is the `webfrontend_type` field (free-form) and the body text is `message`; easydb 5 named these `type` (with values such as `eula`) and `message_html`.

### `GET /message` — List all messages.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/message" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /message` — Create or update one or more messages.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/message" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /message` — Create or update one or more messages (alias for POST).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/message" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /message/{id}` — Retrieve a single message by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/message/{id}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /message/{id}` — Delete a message by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/message/{id}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
