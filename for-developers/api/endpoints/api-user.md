# /api/v1/user

Manage user accounts. The required rights differ per operation: listing and reading users need only an authenticated session (reading the password hash via `include_password` requires `system.root`); creating or updating users is governed by a per-user save-right check (a user may save their own record, but changing a protected field of it — email, `_acl`, `_system_rights`, `_password`, … — still requires the corresponding right); deleting a user requires the `system.user` system right (or `system.root`); and changing the password requires the `system.user.change_password` system right (or `system.root`). Some properties additionally require `system.root`.

### `GET /user` — List all users visible to the authenticated user.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/user" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /user` — Create or update one or more users.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/user" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /user` — Create or update one or more users (alias for POST).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/user" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /user/session` — Information about the current session.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/user/session" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /user/change_password` — Change the authenticated user's password.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/user/change_password" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /user/{id}` — Retrieve a single user by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/user/{id}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /user/{id}` — Delete a user by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/user/{id}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
