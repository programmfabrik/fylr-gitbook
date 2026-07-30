---
description: >-
  fylr 6.35 will no longer ship plugins on disk. The plugins that are installed
  and enabled in your instance will be migrated to their successors in the
  plugin marketplace at the upgrade. What will change, and what to do before it.
---

# From disk plugins to the marketplace

Today a fylr installation carries a set of plugins **on disk**: they arrive inside the fylr distribution, are listed by path in `fylr.yml`, and appear in the plugin manager as type `disk` — impossible to remove, only to disable. Their versions are tied to the fylr release: a plugin fix needs a fylr release, and a plugin that has lost its purpose stays forever.

**fylr 6.35 will end that.** fylr will no longer ship plugins on disk. Plugins will be found in the **plugin marketplace** inside the plugin manager and installed from their own release — with their own version, their own release notes and their own update cycle, independent of the fylr release train.

{% hint style="info" %}
fylr 6.35 has not been released yet. This page describes what will happen when you upgrade an installation to it. The plugin mapping below reflects the current plan; the final mapping will ship with the release.
{% endhint %}

## What the upgrade will do

The upgrade will migrate your installation for you. Nothing has to be prepared in `fylr.yml`, and no plugin has to be re-installed by hand:

* Every plugin that came from the fylr distribution and is **installed and enabled** in your instance will be converted from a `disk` plugin into a **`url` plugin** pointing at its successor's release. It will stay enabled, and keep its configuration if it keeps its name (see [below](disk-to-marketplace.md#configuration-and-renamed-plugins)).
* A distribution plugin that is **disabled** at the time of the upgrade will not be carried over: only what is in use will be migrated. **If you want to keep a disabled plugin, enable it before you upgrade** — you can disable it again afterwards.
* Plugins **you** installed from your own directories — the `plugin.paths` you added yourself, see [Load Custom Plugins](../for-system-administrators/configuration/custom-plugin.md) — will **not be touched**. Loading a plugin from disk stays a supported way to run your own plugins.
* Distribution plugins that have **no successor** will be removed. They are either obsolete, or their function is part of fylr itself by now. See [the second table](disk-to-marketplace.md#plugins-that-will-be-removed).
* Shortly after the restart, each migrated plugin will **download its own release** and from then on keep itself up to date, following the update policy shown in the plugin manager.

{% hint style="warning" %}
**Your fylr instance will need outbound HTTPS access** for this — a migrated plugin becomes functional once its release has been downloaded. If your installation reaches the internet through a proxy or a firewall allowlist, make sure these hosts are reachable **before** the upgrade:

* `github.com` and GitHub's asset hosts (`*.githubusercontent.com`) — the plugin releases
* `programmfabrik.github.io` — releases published as GitHub Pages
* `docs.google.com` — the marketplace catalog

An installation that has no internet access at all can install its plugins [from a ZIP](disk-to-marketplace.md#installations-without-internet-access) instead.
{% endhint %}

## How plugins will migrate

The names in the table are the **internal plugin names**, as shown in the plugin manager.

| Plugin today | Will become | What to check |
| --- | --- | --- |
| `easydb-barcode-display` | `fylr-scancode-display` | The two barcode plugins will be **merged** into one; it needs `fylr-plugin-pdf-creator`, which fylr will install alongside it |
| `easydb-barcode-display-pdf-plugin` | `fylr-scancode-display` | see above — after the upgrade there will be one plugin instead of two |
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
| `custom-data-type-gvk` | `custom-data-type-gvk` | unchanged — the same custom type, delivered by its successor repository `fylr-plugin-custom-data-type-k10plus` |
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
| `easydb-easydb4migration-plugin` | `fylr-plugin-easydb4migration` | new name; the configuration (section `easydb4migration`) will carry over, but the new system right `plugin.fylr-plugin-easydb4migration.migration` has to be granted to the users who run migrations |
| `easydb-editor-field-visibility` | `editor-field-visibility` | new name — **masks and configurations that reference the old name have to be updated** |
| `easydb-editor-tagfilter-defaults-plugin` | `fylr-plugin-editor-tagfilter-defaults` | new name |
| `easydb-export-transport-ftp-plugin` | `easydb-export-transport-ftp-plugin` | unchanged — delivered by `fylr-plugin-export-transport-ftp` |
| `easydb-orcid-plugin` | `fylr-plugin-orcid` | new name |
| `easydb-presentation-pptx-plugin` | `presentation-pptx` | new name |
| `pdf-creator` | `fylr-plugin-pdf-creator` | new name |
| `easydb-typo3-plugin` | `fylr-plugin-typo3` | new name, **licensed plugin** |
| `easydb-wordpress-plugin` | `fylr-plugin-wordpress` | new name, **licensed plugin** |

The custom data types `cerlthesaurus`, `dante`, `geonames`, `georef`, `getty`, `gn250`, `gnd`, `gvk`, `iconclass` and `nomisma` share a library plugin, `commons-library`. fylr will install it alongside them; it does nothing on its own and needs no configuration.

### Configuration and renamed plugins

A plugin's configuration is stored under its **internal name**. Where the name is unchanged in the table above, the configuration carries over untouched and there is nothing to do.

Where the successor has a **new name**, its configuration starts empty — with the exception noted in the table (`fylr-plugin-easydb4migration` deliberately keeps its configuration section). Two things follow from that:

* Configure the successor after the upgrade. It is worth **writing down or exporting the old plugin's configuration before you upgrade**, so you can transfer the values.
* Where a plugin's name appears in the **data model** — a custom mask splitter chosen in a mask, for example `editor-field-visibility` — the mask has to be pointed at the new plugin by hand.

### Plugins that will be removed

These plugins have no successor and will be removed at the upgrade:

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

* every plugin you use is listed, enabled, and shows a version and a build date — that is the proof that its release was downloaded;
* the renamed plugins from the table are configured;
* masks that use a custom mask splitter or a custom data type still render as expected.

## The marketplace

The plugin manager also offers the **marketplace**: the catalog of plugins you can install, with their descriptions, their licensing and the other plugins they need. Installing is one click — no download link to request, no ZIP to upload, and dependencies come along automatically. Programmfabrik maintains the catalog and it refreshes itself, so a new plugin becomes available without a fylr release.

Beyond that catalog, an organisation can add **its own sources** in `fylr.yml`, so plugins developed in-house or by a partner appear in the same list, attributed to where they came from. The marketplace can also be **switched off** in the configuration, for installations where plugins are chosen centrally and administrators should not be offered a catalog.

**Plugins that cost money** — among the migrated ones the Drupal, TYPO3 and WordPress connectors — are marked as such in the marketplace and in the plugin manager. Anybody can install them, but enabling one requires a fylr license that includes it, which is the case for every license that contains it today. Their download is protected, so there is no secret link to keep and to pass around. See [License](../license-management.md).

## When a plugin has a problem

A plugin whose release cannot be reached — a download that fails, a source that is unavailable — is shown in the plugin manager with a **warning**, so a plugin that needs attention is visible at a glance instead of quietly staying behind. fylr also recognises when it has no internet access at all and marks the affected plugins accordingly, instead of presenting each of them as an individual failure.

From that warning, the plugin manager offers to **fix the plugin on the spot**: it can be installed from a ZIP instead of from its URL, without touching its configuration.

## Installations without internet access

An instance that cannot reach the internet — by policy, or because it runs in a closed network — installs its plugins **from a ZIP**: download the plugin package once on a machine that does have access, then hand that package to fylr in the plugin manager. fylr uses the uploaded package instead of the URL, and the plugin keeps the configuration it already has.

That is also how a plugin reaches such an instance after the migration described above: the migrated plugins point at a release URL, and wherever that URL cannot be reached, the ZIP takes its place.
