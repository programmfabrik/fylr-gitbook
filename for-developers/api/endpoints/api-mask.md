# /api/mask

Access the **mask** definitions of a datamodel version. Masks
project objecttypes to a subset of fields and are the unit through
which the frontend renders forms and detail views. `version` can
be:

  * `HEAD` — the working copy (uncommitted edits). Readable by any
    authenticated user (`GET` requires only an authenticated user,
    not `system.datamodel`).
  * `CURRENT` — the most recently committed version. Resolved
    server-side; equivalent to the highest committed number.
  * a positive integer pointing at a specific committed version.

### `GET /mask/{version}` — Retrieve all masks for a datamodel version.
{% swagger src="./fylr-openapi.yml" path="/mask/{version}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /mask/{version}/{mask}` — Retrieve a single mask of a datamodel version.
{% swagger src="./fylr-openapi.yml" path="/mask/{version}/{mask}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /mask/HEAD` — Write masks into the working datamodel (`HEAD`).
{% swagger src="./fylr-openapi.yml" path="/mask/HEAD" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
