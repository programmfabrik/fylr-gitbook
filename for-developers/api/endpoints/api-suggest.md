# /api/v1/suggest

Auto-suggest / autocomplete. Given the user's current input, returns candidate completions either as token frequencies (`tokens`) or as per-field value matches (`fields`), plus optionally the full linked-object descriptors for picker UIs (`linked_objects`). Backed by the search index — the same language settings apply.

Read-only: the request runs in a read transaction; nothing is written. The handler enforces no specific right and no login — an anonymous request is accepted; results are scoped to whatever the session is allowed to see via the per-user best-mask filter.

### `GET /suggest` — Auto-suggest with the request encoded in the URL.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/suggest" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /suggest` — Auto-suggest with the request as a JSON body.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/suggest" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
