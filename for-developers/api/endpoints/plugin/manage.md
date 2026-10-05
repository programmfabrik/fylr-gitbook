# /manage

Management API for installed plugins. Every operation requires the system right `system.root` or `system.plugin`; a request lacking both (including an unauthenticated request) is rejected with `code: SystemRightRequired` (403).

### `GET /plugin/manage` — List all installed plugins.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /plugin/manage` — Create (install) a plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage" method="put" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/manage/{id}` — Read one installed plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage/{id}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /plugin/manage/{id}` — Update an installed plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage/{id}" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /plugin/manage/{id}` — Delete (uninstall) a plugin.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/manage/{id}" method="delete" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### README, ZIP and source check

From **6.35.0**:

* `GET /plugin/manage/{id}/readme` — the plugin's `README.md`, the file next to its `manifest.yml`. The manage listing marks a plugin that ships one with `manifest.has_readme`; the retired `plugin.webfrontend.readme` manifest key is no longer read.
* `PUT /plugin/manage/upload` — install a plugin from a ZIP sent as the raw request body; `POST /plugin/manage/{id}/upload` replaces the ZIP of an installed plugin (a `url` plugin becomes a `zip` plugin, keeping its name, configuration and enabled state); `GET /plugin/manage/{id}/zip` returns the stored ZIP. A plugin ZIP is exempt from the file-production settings (allowed file types, maximum upload size) and no longer travels as an asset; `zip_file` is gone from the API.
* `POST /plugin/manage/{id}/check` — force a source check right away instead of waiting for the update policy's window.

A plugin row reports `enabled` as the flag the administrator stored, and `state` as the reason it cannot run: `not_installed` while a `url` plugin's ZIP has not arrived, `not_licensed` while the license does not grant it. A plugin whose source cannot be fetched carries a `warning` (`url_unreachable`, `url_http_error`, `zip_invalid`) with the time it was first seen, cleared by the next successful fetch. The stored URL of a plugin installed from a catalog-private entry is withheld (`url_hidden`); a `null` URL in a save keeps the stored one.
