# /api/v1/export

Manage **exports** — long-running jobs that bundle objects and their files into a downloadable archive (TAR.GZ or ZIP). All `/export` endpoints require an authenticated user (a valid access token, sent as `Authorization: Bearer`, `X-Fylr-Authorization: Bearer`, or the `access_token` query parameter); there is no dedicated system right for the feature. Exports are user-scoped: each export records the `user_id` that saved it, and the handlers permit access only to that owner or to a `system.root` user.

### `GET /export` — List the authenticated user's exports.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /export` — Create a new export.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /export` — Create a new export (alias for POST).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /export/{exportId}` — Retrieve an export.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /export/{exportId}` — Update an existing export.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /export/{exportId}` — Delete an export.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /export/{exportId}/start` — Start (or restart) the export's generation.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/start" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /export/{exportId}/stop` — Stop a running export.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/stop" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /export/{exportId}/tar_gz/` — Download the generated TAR.GZ archive (or a path inside it).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/tar_gz/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /export/{exportId}/zip/` — Download the generated ZIP archive (or a path inside it).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/zip/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /export/{exportId}/uuid/{uuid}/tar_gz/` — Download the TAR.GZ produced for a specific export run UUID.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/uuid/{uuid}/tar_gz/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /export/{exportId}/uuid/{uuid}/zip/` — Download the ZIP produced for a specific export run UUID.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/uuid/{uuid}/zip/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /export/{exportId}/file/` — Download a single file from the export, or list the export's files.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/file/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `HEAD /export/{exportId}/file/` — Headers for a single export file (or the file index).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/file/" method="head" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /export/{exportId}/uuid/{uuid}/file/` — Download a single file (or list files) for a specific export run UUID.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/uuid/{uuid}/file/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `HEAD /export/{exportId}/uuid/{uuid}/file/` — Headers for a single export file (or the file index) for a run UUID.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/export/{exportId}/uuid/{uuid}/file/" method="head" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
