# /api/v1/WebDAV

The **read/write** [WebDAV](http://www.webdav.org/specs/rfc4918.html) (RFC 4918) interface to **fylr**'s collections, mounted at `/api/v1/WebDAV`. Each WebDAV directory maps to a **fylr** collection; each WebDAV file maps to a file linked from that collection — so you can browse, download, upload, rename and delete a collection's files live. For the separate **drop-only** ingest share, see `/api/v1/hotfolder` below; the two are independent mounts with independent enable flags.

Must be enabled in the base config (`webdav.read_write_access = true`), otherwise every request returns 503 with `code: WebdavNotEnabled`. The same flag gates both reading and writing.

This endpoint performs **no client authentication** — the route is registered with no token check. Knowledge of the collection's UUID, which forms the path, is the only access capability: anyone who can reach the URL with a valid collection UUID can mount it. Clients must connect **as guest** and send no credentials — for example, in macOS Finder's _Connect to Server_ dialog, choose _Connect As: Guest_. There is no Bearer-token, `X-Fylr-Authorization`, `access_token` or HTTP Basic authentication here; the only gate is whether WebDAV is enabled (above). Server-side, the operation acts as the owner of the target collection.

**WebDAV methods.** `GET`, `HEAD`, `OPTIONS`, `POST`, `PUT` and `DELETE` are documented as operations below. The collection-specific WebDAV verbs — which the OpenAPI renderer cannot list as operations — behave as follows:

* `PROPFIND` — the WebDAV directory listing: list a collection's contents. The `Depth` header must be `0` or `1` (`400` otherwise); the response is a `207` multistatus XML body.
* `PROPPATCH` — accepted for client compatibility only; no properties are stored. It behaves like `PROPFIND` and echoes the current property values.
* `MKCOL` — create a collection (`201`; idempotent — also `201` if the collection already exists). `409` when a parent in the path is missing or the path already exists as a file.
* `MOVE` — rename a collection within its parent (`201`). `409` for a missing source, an existing destination, a non-collection target, or a cross-parent move; files cannot be moved.
* `LOCK` / `UNLOCK` — WebDAV write locks. `LOCK` returns `200` (refresh) or `201` (new) with a `Lock-Token` header and an XML lock-discovery body; `UNLOCK` returns `204`. A token mismatch returns `423`.

`COPY` is not supported and returns `405`. As with the operations below, every verb returns `503` with `code: WebdavNotEnabled` when WebDAV is disabled, and writes return `400` `ReadOnlyMode` in read-only mode.

### `GET /WebDAV/{collectionUuid}/{path}` — Download a file (or list a collection — depending on path).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/WebDAV/{collectionUuid}/{path}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /WebDAV/{collectionUuid}/{path}` — WebDAV POST — handled by the same code path as GET/HEAD. fylr

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/WebDAV/{collectionUuid}/{path}" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /WebDAV/{collectionUuid}/{path}` — Upload a file and link it to the collection.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/WebDAV/{collectionUuid}/{path}" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /WebDAV/{collectionUuid}/{path}` — Delete a file.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/WebDAV/{collectionUuid}/{path}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `HEAD /WebDAV/{collectionUuid}/{path}` — Probe a file's existence and metadata.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/WebDAV/{collectionUuid}/{path}" method="head" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `OPTIONS /WebDAV/{collectionUuid}/{path}` — Advertise the supported WebDAV methods for this resource.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/WebDAV/{collectionUuid}/{path}" method="options" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
