# /api/v1/export

Manage **exports** — long-running jobs that bundle objects and their files into a downloadable archive (TAR.GZ or ZIP). All `/export` endpoints require an authenticated user (a valid access token, sent as `Authorization: Bearer`, `X-Fylr-Authorization: Bearer`, or the `access_token` query parameter); there is no dedicated system right for the feature. Exports are user-scoped: each export records the `user_id` that saved it, and the handlers permit access only to that owner or to a `system.root` user.

Since fylr 6.35, while the Janitor is enabled, downloads expire after `system.config.janitor.exports.download_expire_days` days without a run (default: `1`). Clearing this setting restores the default; `0` makes idle downloads eligible on the next pass. Unscheduled exports can expire after `system.config.janitor.exports.export_expire_days` days without a run; the default is `null` (disabled), and `0` makes idle exports eligible on the next pass. The age is measured from the latest run's start, including failed and empty runs, or creation if never run. Starting another run renews retention. Reading or downloading existing output does not. Scheduled, pending, and processing exports are kept. See [Janitor settings](../../../for-administrators/readme/services.md#settings-for-exports-and-downloads).

Since fylr 6.35, the download routes (`file/`, `zip/`, `tar_gz/`) also accept the export's `_download_signature` as `?x-fylr-signature=` in place of a session, the way `/eas/download` accepts a signed file URL, so a browser downloads without its access token in the URL. The export carries the signature when it is loaded, listed, created, updated, started or stopped with `?sign_url=1`; it is valid for one day, and a wrong or expired signature is refused with `403`.

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
