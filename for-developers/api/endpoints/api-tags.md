# /api/v1/tags

Manages the complete set of tag groups and tags. `GET` returns every
taggroup and its tags and requires only an authenticated user; `POST`
replaces the entire set from the request body, deleting any group or tag
absent from it, writes the `taggroup` and `tag` tables directly in the
request transaction (effective immediately, no working copy or commit
step), and requires the `system.tagmanager` system right.

### `GET /tags` — Get all tags
{% swagger src="./fylr-openapi.yml" path="/tags" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /tags` — Create, update or delete taggroups and tags
{% swagger src="./fylr-openapi.yml" path="/tags" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
