# /api/pool

Manage **pools** — fylr's hierarchical containers for storage,
permissions and metadata defaults. Pools form a tree; each pool can
inherit ACL items and configuration from its parent.

Differs from easydb 5: a save that touches collection ACLs is
confirmed with the `allow_invalid_acl` / `background_invalid_acl` /
`background_invalid_acl_timelimit` query parameters instead of
easydb 5's single `collection_rights_policy` parameter.

Differs from easydb 5: there is no separate `system.rights_management`
right for updating rights-management attributes on the root pool —
every save is gated on `system.poolmanager` (or `system.root`) plus
the per-pool `bag_*` rights. (easydb 5 required `system.rights_management`
for root-pool rights changes.)

### `GET /pool` — List all pools visible to the authenticated user.
{% swagger src="./fylr-openapi.yml" path="/pool" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /pool` — Create or update one or more pools.
{% swagger src="./fylr-openapi.yml" path="/pool" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `PUT /pool` — Create or update one or more pools (alias for POST).
{% swagger src="./fylr-openapi.yml" path="/pool" method="put" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /pool/{poolID}` — Retrieve a single pool by id.
{% swagger src="./fylr-openapi.yml" path="/pool/{poolID}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /pool/{poolID}` — Delete a pool by id.
{% swagger src="./fylr-openapi.yml" path="/pool/{poolID}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /pool/{poolID}/stats` — Statistics for a single pool.
{% swagger src="./fylr-openapi.yml" path="/pool/{poolID}/stats" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
