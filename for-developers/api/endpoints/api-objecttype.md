# /api/v1/objecttype

Read and write **objecttypes** — the per-record-type configuration that fylr layers on the datamodel definition (default masks, exposure flags, ACL, tags, transitions, mask / column filters, asset-filename policy, watermark and janitor policy). The objecttype itself (its name, fields and hierarchy) is part of the datamodel and is created through the schema endpoints; this endpoint only configures objecttypes that already exist in the current (committed) datamodel. A write updates the objecttype configuration directly and takes effect immediately when the request transaction commits — there is no working copy and no separate `schema/commit` step.

`GET` is open to any authenticated user; `POST` requires `system.objecttypemanager`. Authentication is by access token (a `Bearer` header or the `access_token` query parameter).

Differs from easydb 5: writes that touch collection ACLs are confirmed with the `confirm` / `allow_invalid_acl` / `background_invalid_acl` query parameters instead of easydb 5's single `collection_rights_policy` parameter.

### `GET /objecttype` — List all objecttypes in the current datamodel.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/objecttype" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /objecttype` — Create or update the settings of one or more objecttypes.

From **6.35.0** a change to an objecttype's standard masks is answered with `202` and a count of the records it re-indexes; repeat the request with `confirmReindex=yes` to queue them into the running index. See [Masks](../../concepts/masks.md#standard-masks-decide-what-is-indexed).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/objecttype" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /objecttype/{id}` — Retrieve a single objecttype.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/objecttype/{id}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /objecttype/{id}/stats` — Asset statistics for an objecttype.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/objecttype/{id}/stats" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
