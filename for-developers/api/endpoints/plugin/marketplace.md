# /marketplace

The plugin marketplace: a curated catalog of plugins offered for installation (from fylr **6.35.0**). Like the manage API, every operation requires the system right `system.root` or `system.plugin`.

### `GET /plugin/marketplace` — Read the plugin marketplace catalog.

The catalog is pulled from Programmfabrik's published catalog sheet at request time and cached with a refresh window; while it cannot be loaded at all, the marketplace answers `503` (`PluginMarketplaceUnavailable`). Entries of **private** repositories are served **without** their install `url` — they are installed by name (see below).

Each entry carries a localized short description, a category, and optionally a `version` and an `updated_at` date. A plugin's version **is the release tag name** of its install artifact — there is no `version` key in `manifest.yml` any more; for an installed plugin the tag is exposed as `build_info.release`. `installable` marks an entry that can be installed by name, `licensed` a paid one, `repo_name` the repository it is published from. The catalog is not compiled into fylr: what the sheet offers changes without a fylr update. `plugin.marketplace.enabled: false` in `fylr.yml` switches the shop off entirely — no catalog or source URL is fetched, and these endpoints answer `400 PluginMarketplaceDisabled`.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/marketplace" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /plugin/marketplace/{name}/install` — Install a marketplace plugin by name.

Installs the named catalog entry. The install URL is resolved on the server — private release URLs never leave it — and missing dependencies are resolved from the catalog and installed first, dependency-first. A paid (`licensed`) plugin lands installed but **disabled**: enabling it needs the instance license to grant it — unless the license already grants it by name, in which case it is enabled right away.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/marketplace/{name}/install" method="post" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /plugin/marketplace/{name}/readme` — Read a marketplace plugin's README.

The full README of a marketplace plugin — its "more information" documentation, shown in the marketplace behind a button.

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/plugin/marketplace/{name}/readme" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
