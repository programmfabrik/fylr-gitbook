---
description: >-
  With fylr 6.35, the plugins shipped on disk become url plugins installed from
  their own releases. What the upgrade will do, and what to check.
---

# Disk to URL plugin migration

{% hint style="info" %}
**The essentials**

* This page is only about the plugins **fylr shipped on disk**, inside the distribution. A plugin you installed yourself from the marketplace — `fylr-plugin-sequence`, `server-pdf`, `ai-metadata` and everything else in the [plugin overview](overview.md) — is already a url plugin and is **not affected**: it is not listed here, and the upgrade does not touch it.
* The shipped plugins become **url plugins**, installed from their own releases. The upgrade converts every enabled plugin that has a successor; the [few without one](disk-to-url-migration.md#plugins-that-will-be-removed) are removed.
* Your **configuration and permissions move with a plugin**, including where the plugin is renamed. There is nothing to write down before the upgrade.
* A distribution plugin that is **switched off** at that moment is removed instead of converted. Switch it on before you upgrade if it should stay — off again afterwards is fine.
* If your fylr **cannot reach the internet**, the plugin manager will mark the plugins it could not download and offer to **install them as ZIP** — your browser fetches the release and hands it to fylr.
* If you use the **Drupal, TYPO3 or WordPress** connector, you **must obtain an updated fylr license** that enables it — without that grant the plugin cannot be enabled after the upgrade. Contact Programmfabrik **before** you upgrade.
{% endhint %}

Until now, every fylr release shipped a fixed set of plugins inside the distribution: type `disk`, listed by path in `fylr.yml`, impossible to remove, and updated only by the next fylr release. From **fylr 6.35** on, fylr ships no plugins. Each plugin comes from its own release instead — with its own version, its own release notes and its own update cycle.

{% hint style="info" %}
fylr 6.35 has not been released yet — this page describes the upcoming upgrade. The mapping below reflects the current plan; the final mapping ships with the release.
{% endhint %}

## The three kinds of plugins

* **url** — fylr downloads the plugin from a release URL and keeps it up to date, following the update policy shown in the plugin manager. This is what the shipped plugins become.
* **zip** — a package uploaded by an administrator. It stays exactly as uploaded until a new ZIP replaces it — the choice when fylr cannot reach a release URL.
* **disk** — loaded from a server directory via `plugin.paths` in `fylr.yml`. From 6.35.0 on, this is only for developing and running [your own plugins](../for-system-administrators/configuration/custom-plugin.md); fylr no longer installs anything this way itself.

## What the upgrade will do

* Every **enabled** plugin from the distribution that has a successor in the table below becomes a **url plugin** pointing at the successor's release — enabled as before, and configured as before. Where a plugin is renamed, its configuration, its granted system rights and any export that uses it are moved to the new name by the upgrade.
* **Disabled** distribution plugins are removed. Their stored configuration is kept and applies again if a plugin of the same name is installed later.
* Plugins **you** installed from your own directories are not touched. The upgrade recognises a distribution plugin by its name **and** by its location inside the fylr Docker image (`/fylr/files/plugins/easydb/`); a plugin loaded from any other directory is left exactly as it is.
* Distribution plugins with **no successor** are removed — they are obsolete, or their function is part of fylr itself by now. See [the second table](disk-to-url-migration.md#plugins-that-will-be-removed).
* After the restart, each converted plugin downloads its release once and keeps itself up to date from then on. It is installed from exactly the release the plugin manager offers for a fresh installation — a migrated plugin and a newly installed one are the same package.

{% hint style="warning" %}
The downloads need **outbound HTTPS** to `github.com`, `*.githubusercontent.com` and `programmfabrik.github.io`. If your instance cannot reach these hosts, see [Installations without internet access](disk-to-url-migration.md#installations-without-internet-access).
{% endhint %}

## How plugins will migrate

The names in the table are the **internal plugin names**, as shown in the plugin manager.

| Plugin today | Will become | What to check |
| --- | --- | --- |
| `basemigration` | [`fylr-plugin-basemigration`](https://github.com/programmfabrik/fylr-plugin-basemigration) | new name |
| `custom-data-type-cerlthesaurus` | [`custom-data-type-cerlthesaurus`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-cerlthesaurus) | unchanged |
| `custom-data-type-dante` | [`custom-data-type-dante`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-dante) | unchanged |
| `custom-data-type-gazetteer` | [`custom-data-type-gazetteer`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-gazetteer) | unchanged |
| `custom-data-type-geonames` | [`custom-data-type-geonames`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-geonames) | unchanged |
| `custom-data-type-georef` | [`custom-data-type-georef`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-georef) | unchanged |
| `custom-data-type-getty` | [`custom-data-type-getty`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-getty) | unchanged |
| `custom-data-type-gn250` | [`custom-data-type-gn250`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-gn250) | unchanged |
| `custom-data-type-gnd` | [`custom-data-type-gnd`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-gnd) | unchanged |
| `custom-data-type-goobi` | [`custom-data-type-goobi`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-goobi) | unchanged |
| `custom-data-type-gvk` | [`custom-data-type-gvk`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-k10plus) | unchanged — the same custom type, delivered by the repository `fylr-plugin-custom-data-type-k10plus` |
| `custom-data-type-html-editor` | [`custom-data-type-html-editor`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-html-editor) | unchanged |
| `custom-data-type-iconclass` | [`custom-data-type-iconclass`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-iconclass) | unchanged |
| `custom-data-type-iucn` | [`custom-data-type-iucn`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-iucn) | unchanged |
| `custom-data-type-link` | [`custom-data-type-link`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-weblink) | unchanged — delivered by `fylr-plugin-custom-data-type-weblink` |
| `custom-data-type-location` | [`custom-data-type-location`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-location) | unchanged |
| `custom-data-type-nomisma` | [`custom-data-type-nomisma`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-nomisma) | unchanged |
| `custom-data-type-tnadiscovery` | [`custom-data-type-tnadiscovery`](https://github.com/programmfabrik/fylr-plugin-custom-data-type-tnadiscovery) | unchanged |
| `easydb-barcode-display` | [`fylr-scancode-display`](https://github.com/programmfabrik/fylr-plugin-scancode-display) | new name — the successor is a different plugin: your masks and PDF templates are re-pointed to it automatically, see [below](disk-to-url-migration.md#the-barcode-plugins) |
| `easydb-coin-viewer-plugin` | [`fylr-plugin-coin-viewer`](https://github.com/programmfabrik/fylr-plugin-coin-viewer) | new name |
| `easydb-connector-plugin` | [`fylr-plugin-connector`](https://github.com/programmfabrik/fylr-plugin-connector) | new name |
| `easydb-custom-mask-splitter-detail-linked-plugin` | [`fylr-plugin-custom-mask-splitter-detail-linked`](https://github.com/programmfabrik/fylr-plugin-custom-mask-splitter-detail-linked) | new name |
| `easydb-detail-map-plugin` | [`fylr-plugin-detail-map`](https://github.com/programmfabrik/fylr-plugin-detail-map) | new name |
| `easydb-display-field-values` | [`fylr-plugin-display-field-values`](https://github.com/programmfabrik/fylr-plugin-display-field-values) | new name |
| `easydb-drupal-plugin` | [`fylr-plugin-drupal`](https://github.com/programmfabrik/fylr-plugin-drupal) | new name, **licensed plugin** |
| `easydb-easydb4migration-plugin` | [`fylr-plugin-easydb4migration`](https://github.com/programmfabrik/fylr-plugin-easydb4migration) | new name |
| `easydb-editor-field-visibility` | [`editor-field-visibility`](https://github.com/programmfabrik/fylr-plugin-editor-field-visibility) | new name |
| `easydb-editor-tagfilter-defaults-plugin` | [`fylr-plugin-editor-tagfilter-defaults`](https://github.com/programmfabrik/fylr-plugin-editor-tagfilter-defaults) | new name |
| `easydb-export-transport-ftp-plugin` | [`easydb-export-transport-ftp-plugin`](https://github.com/programmfabrik/fylr-plugin-export-transport-ftp) | unchanged — delivered by `fylr-plugin-export-transport-ftp`; saved export transports keep working |
| `easydb-hijri-gregorian-converter` | [`fylr-plugin-hijri-gregorian-converter`](https://github.com/programmfabrik/fylr-plugin-hijri-gregorian-converter) | new name — ported to fylr; masks using its splitter keep working |
| `easydb-orcid-plugin` | [`fylr-plugin-orcid`](https://github.com/programmfabrik/fylr-plugin-orcid) | new name |
| `easydb-presentation-pptx-plugin` | [`presentation-pptx`](https://github.com/programmfabrik/fylr-plugin-presentation-pptx) | new name |
| `easydb-typo3-plugin` | [`fylr-plugin-typo3`](https://github.com/programmfabrik/fylr-plugin-typo3) | new name, **licensed plugin** |
| `easydb-wordpress-plugin` | [`fylr-plugin-wordpress`](https://github.com/programmfabrik/fylr-plugin-wordpress) | new name, **licensed plugin** |
| `pdf-creator` | [`pdf-creator`](https://github.com/programmfabrik/fylr-plugin-pdf-creator) | unchanged |

The custom data types `cerlthesaurus`, `dante`, `geonames`, `georef`, `getty`, `gn250`, `gnd`, `goobi`, `gvk`, `iconclass`, `nomisma` and `tnadiscovery` share a library plugin, `commons-library`, which fylr installs alongside them; it does nothing on its own and needs no configuration.

{% hint style="warning" %}
The Drupal, TYPO3 and WordPress connectors become **licensed plugins**: enabling one requires a fylr license that grants it by name. If you use one of these connectors, you **must obtain an updated license** from Programmfabrik that enables it — do this **before you upgrade**, or the plugin will be installed but cannot be enabled.
{% endhint %}

### The renamed plugins

Sixteen plugins change their internal name. This is the list to hold against the plugin manager afterwards — everything else keeps the name it has today.

| Today | After the upgrade |
| --- | --- |
| `basemigration` | `fylr-plugin-basemigration` |
| `easydb-barcode-display` | `fylr-scancode-display` |
| `easydb-coin-viewer-plugin` | `fylr-plugin-coin-viewer` |
| `easydb-connector-plugin` | `fylr-plugin-connector` |
| `easydb-custom-mask-splitter-detail-linked-plugin` | `fylr-plugin-custom-mask-splitter-detail-linked` |
| `easydb-detail-map-plugin` | `fylr-plugin-detail-map` |
| `easydb-display-field-values` | `fylr-plugin-display-field-values` |
| `easydb-drupal-plugin` | `fylr-plugin-drupal` |
| `easydb-easydb4migration-plugin` | `fylr-plugin-easydb4migration` |
| `easydb-editor-field-visibility` | `editor-field-visibility` |
| `easydb-editor-tagfilter-defaults-plugin` | `fylr-plugin-editor-tagfilter-defaults` |
| `easydb-hijri-gregorian-converter` | `fylr-plugin-hijri-gregorian-converter` |
| `easydb-orcid-plugin` | `fylr-plugin-orcid` |
| `easydb-presentation-pptx-plugin` | `presentation-pptx` |
| `easydb-typo3-plugin` | `fylr-plugin-typo3` |
| `easydb-wordpress-plugin` | `fylr-plugin-wordpress` |

You do not have to do anything with this list before upgrading — it is here so a changed name in the plugin manager is recognisable rather than alarming.

### Configuration, rights and exports

A plugin's configuration is stored under its **internal name**, and so are the system rights it defines. Where a plugin is renamed, the upgrade moves both to the new name, together with any export that produces or transports through that plugin. Nothing has to be written down beforehand and nothing has to be re-entered afterwards.

A plugin that is **not** converted — switched off, or loaded from your own directory — keeps its configuration under the old name, so nothing is lost there either.

### The barcode plugins

Everything a plugin contributes to your data model — custom data types, mask splitters, PDF Creator elements — survives the migration, renames or not. The barcode plugins are the only case where the successor is a genuinely **different** plugin: **Scancode Display** registers its mask splitter and its PDF Creator element under new names.

The upgrade rewrites both for you: masks that used the barcode splitter now use the Scancode splitter, and PDF Creator templates containing a barcode element now contain a Scancode element. There is nothing to edit by hand, and `easydb-barcode-display-pdf-plugin` disappears because Scancode Display already contains that PDF element.

### Plugins that will be removed

These plugins have no successor and are removed at the upgrade:

| Plugin | Why |
| --- | --- |
| `easydb-barcode-display-pdf-plugin` | absorbed: [`fylr-plugin-scancode-display`](https://github.com/programmfabrik/fylr-plugin-scancode-display) already contains this PDF Creator element, and the upgrade re-points your templates to it |
| `easydb-falconio-plugin` | the Falcon.io service no longer exists |
| `easydb-remote-plugin`, `server` | easydb5 infrastructure with no function in fylr. **`server` is the easydb5 "Server Status" page — not the [PDF Server](https://github.com/programmfabrik/fylr-plugin-server-pdf) (`server-pdf`), which is a separate marketplace plugin and is not affected by this migration. PDF Creator no longer needs it: it renders PDFs itself** |
| `easydb-auto-keyworder-plugin` | obsolete; automatic keywording is now the licensed **ai-metadata** plugin, which is configured differently and is not a drop-in replacement |
| `easydb-plugin-zooniverse-import` | a project-specific import |
| `easydb-hotfolder-plugin` | the hotfolder is part of fylr itself |
| `webhook-plugin` | no fylr successor |
| `example-plugin` | the developer example, continued as [`fylr-plugin-example`](https://github.com/programmfabrik/fylr-plugin-example) |

The last two are in the list for completeness: the fylr distribution has not loaded them for a long time, so most instances do not have them at all. If yours does — from an easydb5 migration, or a path you added yourself — it is removed like the rest.

If you actively use one of these, talk to us before upgrading.

{% hint style="info" %}
The plugins **`oai`, `easydb-ldap-plugin` and `easydb-sso-plugin`** are not in this list because fylr already ignores them: OAI-PMH, LDAP login and SSO have been part of fylr itself for some time, and the plugin loader skips these three by name. They are not installed today and nothing changes for them at the upgrade.
{% endhint %}

## After the upgrade

Open the **plugin manager** and check that every plugin you use is listed, enabled, and shows a version and a build date — the proof that its release was downloaded. Configure the renamed plugins, and check masks that use a custom mask splitter or a custom data type.

## Installations without internet access

If fylr cannot download a plugin's release, the plugin manager marks that plugin as **not installable** — the entry is there, but the plugin is not operational. Each such plugin offers a one-click **install as ZIP**: your **browser** downloads the release from the plugin's stored URL and uploads it to fylr as a ZIP package. It is the machine you administer from that needs to reach the release host, not the fylr server. If your browser cannot reach it either, download the ZIP on any machine that can, and upload it in the plugin manager yourself.

A plugin installed this way is a **zip plugin**: it stays as uploaded, and updating it means repeating the step with a newer ZIP.
