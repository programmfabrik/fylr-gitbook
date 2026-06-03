# /api/system/share_link

Shortens url paths and generates an url friendly share id to be accessed via
/share/<share_id>.
* The creating user is stored alongside with the share link. If that user is archived
  the system user `system:deleted_user`.
* There is no API to revoke an existing share link.
* Share links are removed only after they expire.

### `POST /system/share_link`
{% swagger src="../fylr-openapi.yml" path="/system/share_link" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /system/share_link/{id}`
{% swagger src="../fylr-openapi.yml" path="/system/share_link/{id}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
