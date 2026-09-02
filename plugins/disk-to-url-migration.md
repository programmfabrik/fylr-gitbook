---
description: >-
  With fylr 6.35, the plugins shipped on disk become url plugins installed from
  their own releases. What the upgrade will do, and what to check.
---

# Disk to URL plugin migration

{% hint style="info" %}
**The essentials**

* This page is only about the plugins **fylr shipped on disk**, inside the distribution. A plugin you installed yourself — `fylr-plugin-sequence`, `ai-metadata` and everything else in the [plugin overview](overview.md) — is already a url plugin and is not converted. There is **one exception**: `server-pdf` is switched **off** where PDF Creator is enabled, because PDF Creator renders its own PDFs now — see [PDF Creator and the PDF Server](disk-to-url-migration.md#pdf-creator-and-the-pdf-server).
* The shipped plugins become **url plugins**, installed from their own releases. The upgrade converts every enabled plugin that has a successor; the [few without one](disk-to-url-migration.md#plugins-that-will-be-removed) are removed.
* Your **configuration and permissions move with a plugin**, including where the plugin is renamed. There is nothing to write down before the upgrade.
* A distribution plugin that is **switched off** at that moment is removed instead of converted. Switch it on before you upgrade if it should stay — off again afterwards is fine.
* If your fylr **cannot reach the internet**, the plugin manager marks the plugins whose release it could not download and offers to **install them as ZIP** — see [Installations without internet access](disk-to-url-migration.md#installations-without-internet-access). Plan for this before the upgrade rather than after it.
* If you use the **Drupal, TYPO3 or WordPress** connector, you **must obtain an updated fylr license** that enables it — without that grant the plugin cannot be enabled after the upgrade. Contact Programmfabrik **before** you upgrade.
{% endhint %}

Until now, every fylr release shipped a fixed set of plugins inside the distribution: type `disk`, listed by path in `fylr.yml`, impossible to remove, and updated only by the next fylr release. From **fylr 6.35** on, fylr ships no plugins. Each plugin comes from its own release instead — with its own version, its own release notes and its own update cycle.

{% hint style="info" %}
fylr 6.35 has not been released yet — this page describes the upgrade it will perform. The mapping below is the one the release carries.
{% endhint %}

## The three kinds of plugins

* **url** — fylr downloads the plugin from a release URL and keeps it up to date, following the update policy shown in the plugin manager. This is what the shipped plugins become.
* **zip** — a package uploaded by an administrator. It stays exactly as uploaded until a new ZIP replaces it — the choice when fylr cannot reach a release URL.
* **disk** — loaded from a server directory via `plugin.paths` in `fylr.yml`. From 6.35.0 on, this is only for developing and running [your own plugins](../for-system-administrators/configuration/custom-plugin.md); fylr no longer installs anything this way itself.

## What the upgrade will do

* Every **enabled** plugin from the distribution that has a successor in the table below becomes a **url plugin** pointing at the successor's release — enabled as before, and configured as before. Where a plugin is renamed, its configuration, its granted system rights and any export that uses it are moved to the new name by the upgrade.
* **Disabled** distribution plugins are removed. Their stored configuration is kept and applies again if a plugin of the same name is installed later.
* Plugins **you** installed from your own directories are not touched. The upgrade recognises a distribution plugin by its name **and** by its location inside the fylr Docker image (`/fylr/files/plugins/easydb/`); a plugin loaded from any other directory is left exactly as it is, and goes on loading from that directory.
* Where you had **already installed the successor yourself** from the marketplace, the distribution plugin is left alone rather than renamed onto it — two plugins cannot share a name. The old row is then dropped like any other distribution plugin, and its configuration stays under the old name. Nothing is lost, but the settings you want are the ones under the new name.
* Distribution plugins with **no successor** are removed — they are obsolete, or their function is part of fylr itself by now. See [the second table](disk-to-url-migration.md#plugins-that-will-be-removed).
* After the restart, each converted plugin downloads its release once and keeps itself up to date from then on. It is installed from exactly the release the plugin manager offers for a fresh installation — a migrated plugin and a newly installed one are the same package.

{% hint style="info" %}
**A converted plugin is inactive until its release has been downloaded.** A url plugin whose ZIP has not arrived cannot run, so fylr holds it off and the plugin manager shows it as **not installed**. This is a runtime state, not a change to your settings: the stored *Active* flag stays as you had it, and the plugin starts by itself as soon as the download succeeds. fylr fetches the releases at the first start after the upgrade, so that start takes noticeably longer than usual — a plugin still in this state afterwards is one whose download did not work.
{% endhint %}

{% hint style="warning" %}
The downloads need **outbound HTTPS** to `github.com`, `*.githubusercontent.com` and `programmfabrik.github.io`. The plugin **marketplace** additionally reads its catalog from `docs.google.com` — see [Network access in restricted setups](../for-administrators/plugin-manager/README.md#network-access-in-restricted-setups). If your instance cannot reach these hosts, see [Installations without internet access](disk-to-url-migration.md#installations-without-internet-access).
{% endhint %}

{% hint style="info" %}
**Only a Docker installation is converted.** The upgrade matches the distribution's own install location inside the fylr Docker image, `/fylr/files/plugins/easydb/`. The downloadable **binary archives** (Windows, macOS, Linux) shipped the same plugins in an `easydb-plugins` folder beside the binary, at a path that does not match — and 6.35 ships no such folder, so once the installation directory is replaced those plugins are simply gone and their entries are dropped rather than converted. On such an installation, note which plugins you use **before** upgrading and install them again from the marketplace afterwards; the mapping below tells you what each one is called now.
{% endhint %}

## How plugins will migrate

The names in the table are the **internal plugin names**, as shown in the plugin manager. A successor **without a link** lives in a private repository — the plugin installs and updates like any other, delivered sealed and decrypted by fylr, but its source is not public.

| Plugin today | Will become | What to check |
| --- | --- | --- |
| `basemigration` | `fylr-plugin-basemigration` | new name |
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
| `easydb-connector-plugin` | `fylr-plugin-connector` | new name |
| `easydb-custom-mask-splitter-detail-linked-plugin` | [`fylr-plugin-custom-mask-splitter-detail-linked`](https://github.com/programmfabrik/fylr-plugin-custom-mask-splitter-detail-linked) | new name |
| `easydb-detail-map-plugin` | [`fylr-plugin-detail-map`](https://github.com/programmfabrik/fylr-plugin-detail-map) | new name |
| `easydb-display-field-values` | [`fylr-plugin-display-field-values`](https://github.com/programmfabrik/fylr-plugin-display-field-values) | new name |
| `easydb-drupal-plugin` | `fylr-plugin-drupal` | new name, **licensed plugin** |
| `easydb-easydb4migration-plugin` | `fylr-plugin-easydb4migration` | new name |
| `easydb-editor-field-visibility` | [`editor-field-visibility`](https://github.com/programmfabrik/fylr-plugin-editor-field-visibility) | new name |
| `easydb-editor-tagfilter-defaults-plugin` | [`fylr-plugin-editor-tagfilter-defaults`](https://github.com/programmfabrik/fylr-plugin-editor-tagfilter-defaults) | new name |
| `easydb-export-transport-ftp-plugin` | [`easydb-export-transport-ftp-plugin`](https://github.com/programmfabrik/fylr-plugin-export-transport-ftp) | unchanged — delivered by `fylr-plugin-export-transport-ftp`; saved export transports keep working |
| `easydb-hijri-gregorian-converter` | [`fylr-plugin-hijri-gregorian-converter`](https://github.com/programmfabrik/fylr-plugin-hijri-gregorian-converter) | new name — ported to fylr; masks using its splitter keep working |
| `easydb-orcid-plugin` | [`fylr-plugin-orcid`](https://github.com/programmfabrik/fylr-plugin-orcid) | new name |
| `easydb-presentation-pptx-plugin` | [`presentation-pptx`](https://github.com/programmfabrik/fylr-plugin-presentation-pptx) | new name |
| `easydb-typo3-plugin` | `fylr-plugin-typo3` | new name, **licensed plugin** |
| `easydb-wordpress-plugin` | `fylr-plugin-wordpress` | new name, **licensed plugin** |
| `pdf-creator` | `pdf-creator` | unchanged |

The custom data types `cerlthesaurus`, `dante`, `geonames`, `georef`, `getty`, `gn250`, `gnd`, `goobi`, `gvk`, `iconclass`, `nomisma` and `tnadiscovery` all require a shared library plugin, `commons-library`. It does nothing on its own and needs no configuration, and the upgrade installs it alongside them. A data type cannot be enabled while it is missing, so if one of these reports `commons-library` after the upgrade, install the library — it comes with the data type when you install that from the marketplace, or directly from [its release](https://github.com/programmfabrik/fylr-plugin-commons-library/releases/latest/download/fylr-plugin-commons-library.zip).

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

**Scancode Display requires PDF Creator.** It carries the PDF element, so it declares `pdf-creator` as a dependency and cannot be enabled without it. If you used the barcode plugins but had the shipped `pdf-creator` switched **off**, switch it on before you upgrade — otherwise Scancode Display arrives with an unmet dependency while your masks have already been rewritten to its splitter, and you have to install PDF Creator from the marketplace to get them rendering again.

### PDF Creator and the PDF Server

Where PDF Creator renders changes with the upgrade, and it is worth knowing which
of the two plugins you have.

**The shipped `pdf-creator`** — the one this page is about — does not render PDFs
itself. It sends the HTML to whatever is configured in the base configuration
under `pdf_creator.fylr_url`, and if that is empty it looks for the
[PDF Server](https://github.com/programmfabrik/fylr-plugin-server-pdf)
(`server-pdf`) plugin and uses that. This is why many instances have `server-pdf`
installed at all.

**Its successor renders PDFs itself.** From version 1.1.0 the marketplace plugin
carries its own renderer and calls it directly. Three things follow:

* **The upgrade switches `server-pdf` off** where PDF Creator is enabled. Not
  because it is redundant — because the two plugins now declare the **same
  custom events**, `SERVER_PDF_GENERATE` and `SERVER_PDF_GENERATE_ERROR`, and an
  event name can belong to only one plugin. Left on, one of the two loses its
  declaration on every configuration load, and which one is not predictable.
* It is switched off, **not removed**. Its settings, its granted rights and its
  uploaded ZIP stay where they are, and the *Active* toggle turns it back on —
  which matters, because `server-pdf` has left the marketplace catalog and the
  plugin manager can no longer install it for you. Turn it back on only if you
  deliberately pin PDF Creator to a version that still delegates to it. Note that
  its `html2pdf` endpoint stops answering while the plugin is off, so if
  something of your own posts to it, that integration needs adjusting.
* `pdf_creator.fylr_url` is no longer used either — it is not a setting of the new
  plugin. If you pointed PDF Creator at an **external** rendering service under
  *Base configuration → Plugins → PDF Creator*, that service is no longer contacted
  after the upgrade; rendering happens on your own exec server instead. The value
  itself is carried over and then ignored. The fylr Docker image ships the
  required Chromium, so nothing needs installing; a custom exec server may need
  `SERVER_PDF_CHROME`.

{% hint style="info" %}
**The rendering change is not tied to 6.35.** If you already installed **PDF
Creator from the marketplace**, it stopped delegating when that plugin updated to
1.1.0 — the marketplace plugin follows its own update policy, independently of
your fylr version, and an instance can have been in this state for months. What
6.35 adds is the migration: it converts the shipped, on-disk `pdf-creator` to the
marketplace plugin, and it is the step that switches `server-pdf` off for you.
Before 6.35 you had to notice the duplicate events yourself.
{% endhint %}

### Plugins that will be removed

Three plugins fylr 6.34 still shipped have no successor. They are removed at the upgrade:

| Plugin | Why |
| --- | --- |
| `easydb-barcode-display-pdf-plugin` | absorbed: [`fylr-plugin-scancode-display`](https://github.com/programmfabrik/fylr-plugin-scancode-display) already contains this PDF Creator element, and the upgrade re-points your templates to it |
| `easydb-falconio-plugin` | the Falcon.io service no longer exists |
| `easydb-remote-plugin` | easydb5 infrastructure with no function in fylr |

A further set of easydb plugins has **no successor either**, but fylr **stopped loading them before 6.35**, so an instance that has been running 6.34 no longer has them and nothing happens to them now. They are named here because an upgrade from an older fylr, or an easydb5 migration, can still bring them along:

| Plugin | Why |
| --- | --- |
| `server` | the easydb5 "Server Status" page. **Not** the [PDF Server](https://github.com/programmfabrik/fylr-plugin-server-pdf) (`server-pdf`), which is a different plugin — see [PDF Creator and the PDF Server](disk-to-url-migration.md#pdf-creator-and-the-pdf-server) |
| `easydb-auto-keyworder-plugin` | obsolete; automatic keywording is now the licensed **ai-metadata** plugin, which is configured differently and is not a drop-in replacement |
| `easydb-plugin-zooniverse-import` | a project-specific import |
| `easydb-hotfolder-plugin` | the hotfolder is part of fylr itself |
| `webhook-plugin` | no fylr successor |
| `example-plugin` | the developer example, continued as [`fylr-plugin-example`](https://github.com/programmfabrik/fylr-plugin-example) |

One case is deliberately **not** covered by any of this: a plugin from the easydb set that you load from **your own** `plugin.paths` directory. The upgrade does not touch it and fylr goes on loading it from that directory — it is your copy, not the distribution's.

If you actively use one of these, talk to us before upgrading.

{% hint style="info" %}
The plugins **`oai`, `easydb-ldap-plugin` and `easydb-sso-plugin`** are not in this list because fylr already ignores them: OAI-PMH, LDAP login and SSO have been part of fylr itself for some time, and the plugin loader skips these three by name. They are not installed today and nothing changes for them at the upgrade.
{% endhint %}

## After the upgrade

Open the **plugin manager** and go down the list:

* Every plugin you use is **listed**. The renamed ones are under their new name — the [rename table](disk-to-url-migration.md#the-renamed-plugins) says which.
* Every plugin shows a **version** and a **build date**. That is the proof its release was downloaded; a plugin still marked **not installed** has not got its ZIP yet, and one with a **warning triangle** could not fetch it at all.
* No plugin reports a **missing dependency**. A plugin whose dependency is absent or switched off does not load at all, and the plugin manager names what it is waiting for. Install it from the marketplace — the two to expect are `commons-library` under the [VZG custom data types](disk-to-url-migration.md#how-plugins-will-migrate) and `pdf-creator` under [Scancode Display](disk-to-url-migration.md#the-barcode-plugins).
* The **licensed** plugins — Drupal, TYPO3, WordPress — are enabled rather than held off by the license.

Then check the things a plugin contributes to the data model: masks that use a **custom mask splitter** or a **custom data type**, and PDF Creator templates.

## Installations without internet access

If fylr cannot download a plugin's release, the plugin manager marks the row with a red **warning triangle** and the state **not installed**: the entry is there, the plugin is not running. Open it, go to the **Type** tab, and you get two buttons — **check now**, which asks the server to try the URL again, and **install as ZIP**, which routes the download through your browser instead of the server.

How much that second button does depends on where the plugin is hosted:

* Plugins delivered from **`programmfabrik.github.io`** — every paid and private one — are fetched by the browser directly and installed in one click.
* Plugins delivered from a **GitHub release** cannot be fetched by a browser at all: GitHub sends no CORS headers on release downloads, so the button falls back to a dialog showing the plugin's URL. Download that ZIP yourself — the link downloads normally — and upload it in the same dialog.

Either way it is the machine you administer from that needs to reach the release host, not the fylr server. If it cannot reach it either, fetch the ZIP on any machine that can and bring it over.

A plugin installed this way becomes a **zip plugin**: fylr keeps the bytes you uploaded, the **source URL is dropped** and the update policy is fixed to **never**. It stays exactly as uploaded until you repeat the step with a newer ZIP. To hand it back to the updater once the network allows, set its type back to **url** and enter the release URL again.
