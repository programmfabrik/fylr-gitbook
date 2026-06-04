# /api/v1/group

Manage user **groups**. A group bundles a set of users together so they can be addressed by the ACL system. Each group has an owner (`_owner`), an optional set of ACL items (`_acl`), system rights (`_system_rights`), auth-method group mappings (`_auth_method_group_maps`) and IP/subnet filters (`_ip_subnet_filter`). Groups are stored in the `group` table; create / update / delete take effect immediately on the request transaction (there is no working-copy / commit step).

Creating, updating (`POST` / `PUT`) and deleting (`DELETE`) groups require the `system.group` (or `system.root`) system right. Listing and reading groups (`GET`) require no system right — the results are filtered to the groups the current session may read (`bag_read`); a `system.root` user sees all groups.

Differs from easydb 5: easydb 5 requires an authenticated session with the `system.group` right to read groups. fylr requires no system right on `GET`; an unauthenticated list request returns an empty array rather than an error.

### `GET /group` — List all groups visible to the current session.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/group" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /group` — Create or update one or more groups.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/group" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /group` — Create or update one or more groups (alias for POST).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/group" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /group/{id}` — Retrieve a single group by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/group/{id}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /group/{id}` — Delete a group by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/group/{id}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
