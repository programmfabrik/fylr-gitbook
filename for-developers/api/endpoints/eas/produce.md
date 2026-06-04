# /produce

This endpoint is used to produce a new version of the file. It allows to crop and rotate images. The new file gets a new id. The `produce_version` setting from the parent is inherited.

Differs from easydb 5: easydb 5 accepts a `description` field (optional l10n) in the produce body; **fylr** ignores it — the request only reads `eas_parent_id`, `format` and `transform`.

### `POST /eas/produce`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/produce" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
