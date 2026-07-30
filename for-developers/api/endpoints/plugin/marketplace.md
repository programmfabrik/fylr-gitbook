# /marketplace

The plugin marketplace: a curated catalog of plugins offered for installation (from fylr **6.35.0**). Like the manage API, every operation requires the system right `system.root` or `system.plugin`.

### `GET /plugin/marketplace` — Read the plugin marketplace catalog.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/marketplace" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/marketplace/{name}/readme` — Read a marketplace plugin's README.

The full README of a marketplace plugin — its "more information" documentation, shown in the marketplace behind a button.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/marketplace/{name}/readme" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
