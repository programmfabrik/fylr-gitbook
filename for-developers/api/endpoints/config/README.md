# /api/config

Administrators can define base configuration using this API. fylr has a basic
set of configuration items which are in the core system, such as the name of
the instance, administrator's main address, language definitions and so on.

Frontends are required to implement a generic form editor for base
configuration items. The list of items can be retrieved using the
[config/list](list/) API.

This list is not stable and can be changed without API change in any new
version of fylr. Plugins can extend the list of configuration items. So,
depending on the list of loaded plugins in fylr, the list has a various number
of items.

### `GET /config` — Get all base configuration
{% swagger src="../fylr-openapi.yml" path="/config" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /config` — Write all base configuration
{% swagger src="../fylr-openapi.yml" path="/config" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /config/{path}` — Read a single base-config item or nested value
{% swagger src="../fylr-openapi.yml" path="/config/{path}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /config/{path}` — Set a single base-config item or nested value
{% swagger src="../fylr-openapi.yml" path="/config/{path}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `DELETE /config/{path}` — Remove a single base-config item or nested value
{% swagger src="../fylr-openapi.yml" path="/config/{path}" method="delete" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
