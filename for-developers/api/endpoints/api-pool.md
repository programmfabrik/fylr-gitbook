# /api/v1/pool

Manage **pools** — fylr's hierarchical containers for storage, permissions and metadata defaults. Pools form a tree; each pool can inherit ACL items and configuration from its parent.

Differs from easydb 5: a save that touches collection ACLs is confirmed with the `allow_invalid_acl` / `background_invalid_acl` / `background_invalid_acl_timelimit` query parameters instead of easydb 5's single `collection_rights_policy` parameter.

Differs from easydb 5: there is no separate `system.rights_management` right for updating rights-management attributes on the root pool — every save is gated on `system.poolmanager` (or `system.root`) plus the per-pool `bag_*` rights. (easydb 5 required `system.rights_management` for root-pool rights changes.)

### `GET /pool` — List all pools visible to the authenticated user.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/pool" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /pool` — Create or update one or more pools.

From **6.35.0** a change to a pool's standard masks is answered with `202` and a count of the records it re-indexes, because a record is indexed only under the standard masks of its pool. Repeat the request with the query parameter `confirmReindex=yes` to apply it; the affected records — of the pool and its sub-pools — are then queued into the running index at low priority. See [Masks](../../../concepts/masks.md#standard-masks-decide-what-is-indexed).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/pool" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /pool` — Create or update one or more pools (alias for POST).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/pool" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /pool/{poolID}` — Retrieve a single pool by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/pool/{poolID}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /pool/{poolID}` — Delete a pool by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/pool/{poolID}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /pool/{poolID}/stats` — Statistics for a single pool.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/pool/{poolID}/stats" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
