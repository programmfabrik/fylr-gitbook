# /api/v1/system

System-administration endpoints for operating a fylr instance:
statistics and status, search-index rebuild, backups, storage
locations, share links, sending mail, and wiping the instance
(factory reset). Most operations require a `system.*` right (often
`system.root`).

### `GET /system/status` — System object/index/file statistics.
{% swagger src="../fylr-openapi.yml" path="/system/status" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/errortest` — Trigger a test error (for error-handling validation).
{% swagger src="../fylr-openapi.yml" path="/system/errortest" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/openapi/spec.json` — The OpenAPI specification for the v1 API (JSON).
{% swagger src="../fylr-openapi.yml" path="/system/openapi/spec.json" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /system/reindex` — Rebuild the search index from scratch.
{% swagger src="../fylr-openapi.yml" path="/system/reindex" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /system/purgeall` — Wipe and re-initialize the entire instance (factory reset).
{% swagger src="../fylr-openapi.yml" path="/system/purgeall" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `PUT /system/backup/new` — Create a new backup.
{% swagger src="../fylr-openapi.yml" path="/system/backup/new" method="put" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/backup/list` — List backups on file.
{% swagger src="../fylr-openapi.yml" path="/system/backup/list" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/backup/{id}` — Retrieve a backup descriptor.
{% swagger src="../fylr-openapi.yml" path="/system/backup/{id}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `DELETE /system/backup/{id}` — Delete a backup.
{% swagger src="../fylr-openapi.yml" path="/system/backup/{id}" method="delete" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/backup/{id}/download` — Download a backup archive.
{% swagger src="../fylr-openapi.yml" path="/system/backup/{id}/download" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /system/location/new` — Create a new storage location.
{% swagger src="../fylr-openapi.yml" path="/system/location/new" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/location/list` — List configured storage locations.
{% swagger src="../fylr-openapi.yml" path="/system/location/list" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/location/{id}` — Retrieve a single storage location.
{% swagger src="../fylr-openapi.yml" path="/system/location/{id}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `PUT /system/location/{id}` — Update a storage location.
{% swagger src="../fylr-openapi.yml" path="/system/location/{id}" method="put" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `DELETE /system/location/{id}` — Delete a storage location.
{% swagger src="../fylr-openapi.yml" path="/system/location/{id}" method="delete" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
