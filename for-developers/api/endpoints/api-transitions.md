# /api/v1/transitions

Manage workflow **transitions** — rules that fire when objects are inserted, updated or deleted, gated on the object's tags, and run actions (set/unset tags, send email, call a webhook, change the owner, or invoke a plugin callback). This endpoint is the admin surface: list the defined transitions, replace them. The transitions themselves are evaluated implicitly during the object save pipeline, not through a separate endpoint.

Both operations require the `system.tagmanager` system right (a user holding `system.root` is always granted it). The endpoint takes no path, query, or header parameters; authentication uses the standard access token (see the API overview).

Differs from easydb 5: easydb 5 gated only the `POST`, and on the `system.rights_management` right; **fylr** gates both methods on `system.tagmanager`. easydb 5 returned `400` when the session was unauthenticated or lacked the right; **fylr** returns `401` (`UserRequired`) and `403` (`SystemRightRequired`) respectively.

### `GET /transitions` — List all defined transitions.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/transitions" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /transitions` — Replace the full set of transitions.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/transitions" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
