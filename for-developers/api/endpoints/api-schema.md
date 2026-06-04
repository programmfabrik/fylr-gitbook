# /api/v1/schema

The **schema** endpoint exposes the JSON-Schema view of a datamodel
version — the structural description that `/api/db` and `/api/search`
validate against. The same datamodel can also be rendered as a
diagram via `?format=svg` / `?format=png`.

`version` can be:

  * `HEAD` — the working copy (uncommitted edits).
  * `CURRENT` — the most recently committed version. Resolved
    server-side; equivalent to the highest committed number.
  * a positive integer pointing at a specific committed version.

Reading requires only an authenticated user; no `system.datamodel`
right is needed.

### `GET /schema/user/{version}` — Retrieve a datamodel snapshot.
{% swagger src="./fylr-openapi.yml" path="/schema/user/{version}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /schema/user/HEAD` — Update the working datamodel (`HEAD`).
{% swagger src="./fylr-openapi.yml" path="/schema/user/HEAD" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /schema/commit` — Commit the working datamodel (`HEAD`).
{% swagger src="./fylr-openapi.yml" path="/schema/commit" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
