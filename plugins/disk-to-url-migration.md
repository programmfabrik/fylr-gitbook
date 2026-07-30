---
description: >-
  With fylr 6.35, the plugins shipped on disk become url plugins installed from
  their own releases. What the upgrade will do, and what to check.
---

# Disk to URL plugin migration

{% hint style="info" %}
**The essentials**

* The plugins that fylr ships on disk today will become **url plugins**, installed from their own releases. The upgrade converts every enabled plugin that has a successor; the [few without one](disk-to-url-migration.md#plugins-that-will-be-removed) are removed.
* A distribution plugin that is **switched off** at that moment is removed instead of converted. Switch it on before you upgrade if it should stay — off again afterwards is fine.
* If your fylr **cannot reach the internet**, the plugin manager will mark the plugins it could not download and offer to **install them as ZIP** — your browser fetches the release and hands it to fylr.
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

* Every **enabled** plugin from the distribution that has a successor in the table below becomes a **url plugin** pointing at the successor's release — enabled as before, and configured as before if the name is unchanged.
* **Disabled** distribution plugins are removed. Their stored configuration is kept and applies again if a plugin of the same name is installed later.
* Plugins **you** installed from your own directories are not touched.
* Distribution plugins with **no successor** are removed — they are obsolete, or their function is part of fylr itself by now. See [the second table](disk-to-url-migration.md#plugins-that-will-be-removed).
* After the restart, each converted plugin downloads its release once and keeps itself up to date from then on.

{% hint style="warning" %}
The downloads need **outbound HTTPS** to `github.com`, `*.githubusercontent.com` and `programmfabrik.github.io`. If your instance cannot reach these hosts, see [Installations without internet access](disk-to-url-migration.md#installations-without-internet-access).
{% endhint %}

## How plugins will migrate

The names in the table are the **internal plugin names**, as shown in the plugin manager.

| Plugin today | Will become | What to check |
| --- | --- | --- |
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
| `easydb-easydb4migration-plugin` | `fylr-plugin-easydb4migration` | new name; the configuration (section `easydb4migration`) carries over, but the new system right `plugin.fylr-plugin-easydb4migration.migration` has to be granted to the users who run migrations |
| `easydb-editor-field-visibility` | `editor-field-visibility` | new name; masks using its mask splitter are **not** affected, but the plugin's own configuration starts empty |
| `easydb-editor-tagfilter-defaults-plugin` | `fylr-plugin-editor-tagfilter-defaults` | new name |
| `easydb-export-transport-ftp-plugin` | `easydb-export-transport-ftp-plugin` | unchanged — delivered by `fylr-plugin-export-transport-ftp` |
| `easydb-orcid-plugin` | `fylr-plugin-orcid` | new name |
| `easydb-presentation-pptx-plugin` | `presentation-pptx` | new name |
| `pdf-creator` | `fylr-plugin-pdf-creator` | new name |
| `easydb-typo3-plugin` | `fylr-plugin-typo3` | new name, **licensed plugin** |
| `easydb-wordpress-plugin` | `fylr-plugin-wordpress` | new name, **licensed plugin** |

The custom data types `cerlthesaurus`, `dante`, `geonames`, `georef`, `getty`, `gn250`, `gnd`, `gvk`, `iconclass` and `nomisma` share a library plugin, `commons-library`, which fylr installs alongside them; it does nothing on its own and needs no configuration.

The **licensed plugins** — the Drupal, TYPO3 and WordPress connectors — keep working under a license that grants them, which is the case for every license that contains them today.

### Configuration and renamed plugins

A plugin's configuration is stored under its **internal name**. Where the name is unchanged, it carries over untouched. Where the successor has a **new name**, it starts unconfigured (`fylr-plugin-easydb4migration` is the exception noted in the table) — so **note the old plugin's configuration before you upgrade** and transfer the values afterwards.

### Mask splitters and custom data types

**Custom data types** are addressed via the plugin that delivers them — that is why every custom data type above keeps its name. Columns using them keep working; nothing changes in the data model.

**Mask splitters** are addressed by the splitter itself, not by the plugin name, so the renames do not affect any mask: the splitters of `editor-field-visibility`, `fylr-plugin-display-field-values` and `fylr-plugin-custom-mask-splitter-detail-linked` keep working, with their options.

The exception is the **barcode plugins**, which are [removed](disk-to-url-migration.md#plugins-that-will-be-removed): their replacement **Scancode Display** delivers the splitter under a different identity. Masks containing the old barcode splitter show it as an *unknown splitter* — a marked block that still renders the fields inside it and survives saving the mask, so nothing is lost. Install `fylr-plugin-scancode-display`, then edit the mask and put the Scancode splitter in the block's place, with the same options. The same *unknown splitter* block appears for any splitter whose plugin is currently absent; installing the plugin makes those masks render normally again.

### Plugins that will be removed

These plugins have no successor and will be removed at the upgrade:

| Plugin | Why |
| --- | --- |
| `easydb-barcode-display`, `easydb-barcode-display-pdf-plugin` | continued as one plugin, `fylr-plugin-scancode-display` — a different plugin rather than a drop-in successor: install it and re-point the masks, see [above](disk-to-url-migration.md#mask-splitters-and-custom-data-types) |
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

Open the **plugin manager** and check that every plugin you use is listed, enabled, and shows a version and a build date — the proof that its release was downloaded. Configure the renamed plugins, and check masks that use a custom mask splitter or a custom data type.

## Installations without internet access

If fylr cannot download a plugin's release, the plugin manager marks that plugin as **not installable** — the entry is there, but the plugin is not operational. Each such plugin offers a one-click **install as ZIP**: your **browser** downloads the release from the plugin's stored URL and uploads it to fylr as a ZIP package. It is the machine you administer from that needs to reach the release host, not the fylr server. If your browser cannot reach it either, download the ZIP on any machine that can, and upload it in the plugin manager yourself.

A plugin installed this way is a **zip plugin**: it stays as uploaded, and updating it means repeating the step with a newer ZIP.
