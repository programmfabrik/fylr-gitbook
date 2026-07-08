---
description: >-
  The whitelisted /inspect JSON endpoints — the backend console's machine-readable
  projection, used by the test suite and by monitoring.
---

# /inspect

`/inspect` is fylr's backend introspection and maintenance console. Every page
renders an HTML dashboard by default and returns **JSON** when the request sends
`Accept: application/json` (or `?accept=application/json`). The JSON projection
is **whitelisted per page** — the operations below expose exactly the whitelisted
fields, never more.

These endpoints are **not** under `/api/v1` and are **not** token-authenticated.
On the public **webapp port** /inspect is reverse-proxied behind a session check
and requires the **`system.root`** right; on the **backend port** it is mounted
with no authentication and must stay on a private network. For the console itself
— the dashboards, filters and actions — see
[The /inspect Backend](../../../for-system-administrators/inspect/README.md).

## Instance

### `GET /inspect/` — Instance overview (home dashboard).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

## Data & model

### `GET /inspect/config/` — Compiled base configuration.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/config/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/plugins/` — Installed plugins.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/plugins/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/tags/` — Tags and tag groups.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/tags/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/objecttypes/{objecttype}/` — Statistics for one objecttype.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/objecttypes/{objecttype}/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/pools/{pool}/` — Statistics for one pool.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/pools/{pool}/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/objects/` — Paged object id list for an objecttype.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/objects/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/objects/list/` — Objects indexed by read table.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/objects/list/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/objects/{systemObjectId}/` — Render one object against a datamodel version.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/objects/{systemObjectId}/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/collections/` — Paged, searchable collection tree.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/collections/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/customdata/{id}/` — Custom-data-type event.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/customdata/{id}/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

## System & maintenance

### `GET /inspect/system/status/` — Server statistics.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/system/status/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/system/janitor/` — Janitor events.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/system/janitor/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/sqlquery/` — Run an SQL query (debug builds only).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/sqlquery/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/recalcterms/` — Term-recalculation status.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/recalcterms/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/migration/` — List backups.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/migration/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /inspect/migration/{backup}/` — One backup and its file listing.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/inspect/migration/{backup}/" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
