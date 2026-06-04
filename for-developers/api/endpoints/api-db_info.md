# /api/v1/db\_info

Read-only permission probe for object creation. For a given `objecttype`, `pool_id` and `tag_ids` combination it reports where the requesting user may create objects, returning `_available_objecttypes`, `_available_masks` and `_available_tags`. No object is created.

### `POST /db_info/create`

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/db_info/create" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /db_info/update`

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/db_info/update" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
