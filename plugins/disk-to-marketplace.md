---
description: >-
  With fylr 6.35 the distribution no longer ships plugins on disk. Plugins that
  are installed today are migrated to their marketplace successors automatically
  at the upgrade. What changes, what to check, and what is still to come.
---

# From disk plugins to the marketplace

Until now, a fylr installation carried a set of plugins **on disk**: they came inside the fylr distribution (the docker image), were listed by path in `fylr.yml`, and appeared in the plugin manager as type `disk` — impossible to remove, only to disable. Their versions were tied to the fylr release: a plugin fix required a fylr release, and a plugin that no longer had a purpose stayed forever.

With **fylr 6.35** this ends. fylr ships **no plugins on disk** any more. Plugins are discovered in the **plugin marketplace** inside the plugin manager and installed from their own release — with their own version, their own release notes and their own update cycle, independent of the fylr release train.

{% hint style="info" %}
This page describes what happens when you upgrade an installation to fylr 6.35. The plugin mapping below reflects the current plan; the final mapping ships with the release.
{% endhint %}

## What the upgrade does

The upgrade migrates your installation for you. There is nothing to prepare in `fylr.yml`, and no plugin needs to be re-installed by hand:

* Every plugin that came from the fylr distribution and is **installed** in your instance is converted from a `disk` plugin into a **`url` plugin** pointing at its successor's release. The plugin keeps its enabled/disabled state, and its configuration if it keeps its name (see [below](disk-to-marketplace.md#configuration-and-renamed-plugins)).
* Plugins **you** installed from your own directories — the `plugin.paths` you added yourself, see [Load Custom Plugins](../for-system-administrators/configuration/custom-plugin.md) — are **not touched**. Loading a plugin from disk stays a supported way to run your own plugins.
* Plugins from the distribution that have **no successor** are removed. They are either obsolete, or their function is now part of fylr itself. See [the second table](disk-to-marketplace.md#plugins-that-are-removed).
* Shortly after the restart each migrated plugin **downloads its own release** and then keeps itself up to date, following the update policy shown in the plugin manager.

{% hint style="warning" %}
**Your fylr instance needs outbound HTTPS access** for this — a migrated plugin is only functional once its release has been downloaded once. If your installation reaches the internet through a proxy or a firewall allowlist, make sure these hosts are reachable **before** the upgrade:

* `github.com` and GitHub's asset hosts (`*.githubusercontent.com`) — the plugin releases
* `programmfabrik.github.io` — releases published as GitHub Pages
* `docs.google.com` — the marketplace catalog

fylr keeps retrying, so a plugin appears as soon as the connection works; an installation with no internet access at all is covered under [Still to come](disk-to-marketplace.md#still-to-come).
{% endhint %}

## How plugins migrate

Names in the table are the **internal plugin names**, as shown in the plugin manager.

| Plugin today | Becomes | What to check |
| --- | --- | --- |
| `easydb-barcode-display` | `fylr-scancode-display` | The two barcode plugins are **merged** into one plugin; it needs `fylr-plugin-pdf-creator`, which fylr installs alongside it |
| `easydb-barcode-display-pdf-plugin` | `fylr-scancode-display` | see above — after the upgrade there is one plugin instead of two |
| `basemigration` | `fylr-plugin-basemigration` | new name |
| `custom-data-type-cerlthesaurus` | `custom-data-type-cerlthesaurus` | unchanged |
| `custom-data-type-dante` | `custom-data-type-dante` | unchanged |
| `custom-data-type-gazetteer` | `custom-data-type-gazetteer` | unchanged |
| `custom-data-type-geonames` | `custom-data-type-geonames` | unchanged |
| `custom-data-type-georef` | `custom-data-type-georef` | unchanged |
| `custom-data-type-getty` | `custom-data-type-getty` | unchanged |
| `custom-data-type-gn250` | `custom-data-type-gn250` | unchanged |
| `custom-data-type-gnd` | `custom-data-type-gnd` | unchanged |
| `custom-data-type-goobi` | `custom-data-type-goobi` | unchanged |
| `custom-data-type-gvk` | `custom-data-type-gvk` | unchanged — the same custom type, now delivered by its successor repository `fylr-plugin-custom-data-type-k10plus` |
| `custom-data-type-html-editor` | `custom-data-type-html-editor` | unchanged |
| `custom-data-type-iconclass` | `custom-data-type-iconclass` | unchanged |
| `custom-data-type-iucn` | `custom-data-type-iucn` | unchanged |
| `custom-data-type-link` | `custom-data-type-link` | unchanged — delivered by `fylr-plugin-custom-data-type-weblink` |
| `custom-data-type-location` | `custom-data-type-location` | unchanged |
| `custom-data-type-nomisma` | `custom-data-type-nomisma` | unchanged |
| `custom-data-type-tnadiscovery` | `custom-data-type-tnadiscovery` | unchanged |
| `custom-mask-splitter-detail-linked` | `fylr-plugin-custom-mask-splitter-detail-linked` | new name |
| `easydb-coin-viewer-plugin` | `fylr-plugin-coin-viewer` | new name |
| `easydb-connector-plugin` | `fylr-plugin-connector` | new name |
| `easydb-detail-map-plugin` | `fylr-plugin-detail-map` | new name |
| `easydb-display-field-values` | `fylr-plugin-display-field-values` | new name |
| `easydb-drupal-plugin` | `fylr-plugin-drupal` | new name, **licensed plugin** |
| `easydb-easydb4migration-plugin` | `fylr-plugin-easydb4migration` | new name; the configuration (section `easydb4migration`) carries over, but the new system right `plugin.fylr-plugin-easydb4migration.migration` has to be granted to the users who run migrations |
| `easydb-editor-field-visibility` | `editor-field-visibility` | new name — **masks and configurations that reference the old name have to be updated** |
| `easydb-editor-tagfilter-defaults-plugin` | `fylr-plugin-editor-tagfilter-defaults` | new name |
| `easydb-export-transport-ftp-plugin` | `easydb-export-transport-ftp-plugin` | unchanged — now delivered by `fylr-plugin-export-transport-ftp` |
| `easydb-orcid-plugin` | `fylr-plugin-orcid` | new name |
| `easydb-presentation-pptx-plugin` | `presentation-pptx` | new name |
| `pdf-creator` | `fylr-plugin-pdf-creator` | new name |
| `easydb-typo3-plugin` | `fylr-plugin-typo3` | new name, **licensed plugin** |
| `easydb-wordpress-plugin` | `fylr-plugin-wordpress` | new name, **licensed plugin** |

The custom data types `cerlthesaurus`, `dante`, `geonames`, `georef`, `getty`, `gn250`, `gnd`, `gvk`, `iconclass` and `nomisma` share a library plugin, `commons-library`. fylr installs it alongside them; it does nothing on its own and needs no configuration.

**Licensed plugins** (the Drupal, TYPO3 and WordPress connectors) stay installed and keep working under a license that grants them — which is the case for every license that contains them today. Without such a grant a licensed plugin can be installed, but not enabled. See [License](../license-management.md).

### Configuration and renamed plugins

A plugin's configuration is stored under its **internal name**. Where the name is unchanged in the table above, the configuration is carried over untouched and there is nothing to do.

Where the successor has a **new name**, its configuration starts empty — with the exception noted in the table (`fylr-plugin-easydb4migration` deliberately keeps its configuration section). Two things follow:

* Configure the successor after the upgrade. It is worth **writing down or exporting the old plugin's configuration before you upgrade**, so you can transfer the values.
* Where the plugin's name appears in the **data model** — a custom mask splitter chosen in a mask, for example `editor-field-visibility` — the mask has to be pointed at the new plugin by hand.

### Plugins that are removed

These plugins have no successor and are removed at the upgrade:

| Plugin | Why |
| --- | --- |
| `easydb-hotfolder-plugin` | the hotfolder is part of fylr |
| `easydb-ldap-plugin` | LDAP login is part of fylr |
| `oai` | OAI-PMH is part of fylr |
| `easydb-auto-keyworder-plugin` | obsolete; automatic keywording is now the licensed **ai-metadata** plugin, which is configured differently and is not a drop-in replacement |
| `easydb-falconio-plugin` | the Falcon.io service no longer exists |
| `easydb-hijri-gregorian-converter` | a project-specific mask splitter for Hijri dates; available again on request |
| `easydb-plugin-zooniverse-import` | a project-specific import |
| `easydb-remote-plugin`, `server` | easydb5 infrastructure with no function in fylr |
| `example-plugin` | the developer example, continued as `fylr-plugin-example` |

If you actively use one of these, talk to us before upgrading.

## After the upgrade

Open the **plugin manager** and check that:

* every plugin you use is listed, enabled, and shows a version and a build date — that is the proof its release was downloaded;
* the renamed plugins from the table are configured;
* masks that use a custom mask splitter or a custom data type still render as expected.

The plugin manager now also has the **marketplace**: the catalog of plugins you can install, with their descriptions and dependencies. Installing from it is one click — no download link to request, no ZIP to upload. The catalog is maintained by Programmfabrik and updates itself, so a new plugin becomes available without a fylr release.

Beyond that catalog, an organisation can add **its own marketplace sources** in `fylr.yml`, so plugins developed in-house or by a partner appear in the same list. The mechanics are described in [Plugin marketplace and secure delivery](../for-developers/concepts/white-papers/secure-plugin-delivery.md).

## Still to come

The following is planned on top of the 6.35 changes. It is **not available yet** — this section is here so you can plan with it, and it will be updated as the pieces ship.

* **Installations without internet access.** After the migration a plugin is fetched from its release URL. For instances that cannot reach the internet at all, the plugin manager will offer the same plugin as a **ZIP upload**: you download the package once on a machine that has access and hand it to fylr, which then uses the uploaded package instead of the URL.
* **fylr notices that it is offline.** Instead of quietly retrying, fylr will recognise that it cannot reach the outside world and mark the affected plugins accordingly, so the cause is visible at a glance.
* **A "warning" state per plugin.** The plugin manager will show a plugin whose release cannot be reached — or that is otherwise not in working order — in a dedicated warning state, and offer to **fix it right there**, for example by switching that plugin from its URL to an uploaded ZIP.
* **Encrypted delivery for paid plugins.** Paid plugins will be published as **sealed packages**: the download is encrypted for your installation and is opened by fylr at install time, so a package is worthless to anyone else and its URL can be published openly. The API will hand out those encrypted URLs; the plugin's source is no longer carried by a link that must be kept secret. The design is documented in [Plugin marketplace and secure delivery](../for-developers/concepts/white-papers/secure-plugin-delivery.md).
* **Turning the marketplace off.** A switch in `fylr.yml` for installations that do not want the catalog offered in the plugin manager at all — for example because plugin selection is governed centrally.
