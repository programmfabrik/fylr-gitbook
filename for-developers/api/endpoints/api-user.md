# /api/v1/user

Manage user accounts. The required rights differ per operation:
listing and reading users need only an authenticated session (reading
the password hash via `include_password` requires `system.root`);
creating or updating users is governed by a per-user save-right check
(a user may save their own record, but changing a protected field of it
— email, `_acl`, `_system_rights`, `_password`, … — still requires the
corresponding right); deleting a user requires the `system.user` system
right (or `system.root`); and changing the password requires the
`system.user.change_password` system right (or `system.root`). Some
properties additionally require `system.root`.

### `GET /user` — List all users visible to the authenticated user.
{% swagger src="./fylr-openapi.yml" path="/user" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /user` — Create or update one or more users.
{% swagger src="./fylr-openapi.yml" path="/user" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `PUT /user` — Create or update one or more users (alias for POST).
{% swagger src="./fylr-openapi.yml" path="/user" method="put" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /user/session` — Information about the current session.
{% swagger src="./fylr-openapi.yml" path="/user/session" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /user/change_password` — Change the authenticated user's password.
{% swagger src="./fylr-openapi.yml" path="/user/change_password" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /user/{id}` — Retrieve a single user by id.
{% swagger src="./fylr-openapi.yml" path="/user/{id}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /user/{id}` — Delete a user by id.
{% swagger src="./fylr-openapi.yml" path="/user/{id}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
