# /api/v1/db_info

Read-only permission probe for object creation. For a given `objecttype`,
`pool_id` and `tag_ids` combination it reports where the requesting user may
create objects, returning `_available_objecttypes`, `_available_masks` and
`_available_tags`. No object is created.

### `POST /db_info/create`
{% swagger src="./fylr-openapi.yml" path="/db_info/create" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /db_info/update`
{% swagger src="./fylr-openapi.yml" path="/db_info/update" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
