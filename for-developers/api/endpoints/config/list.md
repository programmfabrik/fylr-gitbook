# /api/config/list

Read the list of available base-config variable definitions. The list is
compiled dynamically from fylr's fixed core config items plus any items
contributed by loaded plugins, so it varies with the installed plugin set.
It describes the config schema (the items a frontend renders into a config
form); the stored values are read and written through `/config`. Requires
the `system.config` system right (`system.root` always satisfies it).

### `GET /config/list` — Get config list
{% swagger src="../fylr-openapi.yml" path="/config/list" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
