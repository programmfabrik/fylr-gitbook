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
* Your **configuration and permissions move with a plugin**, including where the plugin is renamed. There is nothing to write down before the upgrade. The one exception is an instance where you **already replaced a shipped plugin by hand** with its successor: there the old settings stay where they are, see [below](disk-to-url-migration.md#if-you-already-replaced-a-shipped-plugin-by-hand).
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
* A plugin **you** maintain yourself under one of the distribution's names is converted as well. The upgrade recognises a distribution plugin by its **name**, wherever it is loaded from — so your own copy of, say, `easydb-orcid-plugin` in your own directory becomes the published `fylr-plugin-orcid` release. If you want to keep running your own build of it, install that again as a ZIP or from your directory after the upgrade. A plugin whose name is not in the table below is never touched.
* Where you had **already installed the successor yourself** from the marketplace, the distribution plugin is left alone rather than renamed onto it — two plugins cannot share a name. The old row is then dropped like any other distribution plugin, and its configuration stays under the old name. Nothing is lost, but the settings the successor uses are the ones you entered for it — see [If you already replaced a shipped plugin by hand](disk-to-url-migration.md#if-you-already-replaced-a-shipped-plugin-by-hand) for carrying the old ones over.
* Distribution plugins with **no successor** are removed — they are obsolete, or their function is part of fylr itself by now. See [the second table](disk-to-url-migration.md#plugins-that-will-be-removed).
* After the restart, each converted plugin downloads its release once and keeps itself up to date from then on. It is installed from exactly the release the plugin manager offers for a fresh installation — a migrated plugin and a newly installed one are the same package.

{% hint style="info" %}
**A converted plugin is inactive until its release has been downloaded.** A url plugin whose ZIP has not arrived cannot run, so fylr holds it off and the plugin manager shows it as **not installed**. This is a runtime state, not a change to your settings: the stored *Active* flag stays as you had it, and the plugin starts by itself as soon as the download succeeds. fylr does **not** wait for the downloads while it starts — the instance comes up as usual and fetches the releases in the background — so shortly after the first start some converted plugins are still marked *not installed*. One still in that state minutes later is one whose download did not work.
{% endhint %}

{% hint style="warning" %}
The downloads need **outbound HTTPS** to `github.com`, `*.githubusercontent.com` and `programmfabrik.github.io`. The plugin **marketplace** additionally reads its catalog from `docs.google.com` — see [Network access in restricted setups](../for-administrators/plugin-manager/README.md#network-access-in-restricted-setups). If your instance cannot reach these hosts, see [Installations without internet access](disk-to-url-migration.md#installations-without-internet-access).
{% endhint %}

{% hint style="info" %}
**Docker and the downloadable archives are both converted.** The upgrade matches a distribution plugin by name, wherever it was installed from, so the **binary archives** (Windows, macOS, Linux) — which shipped the same plugins in an `easydb-plugins` folder beside the binary — are migrated the same way as a Docker installation. 6.35 ships no such folder any more; the plugins that used to live there come from their own releases from now on.
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

A plugin's configuration is stored under its **internal name**, and so are the system rights it defines. Where a plugin is renamed, the upgrade moves both to the new name, together with any export that produces or transports through that plugin.

The successors read the same settings: **every settings block, every field in it and every system right keeps its internal key**. The values arrive under the new name exactly as they were — nothing has to be written down beforehand and nothing has to be re-entered afterwards, the connector's partner instances with their logins and client secrets included. In detail:

| After the upgrade | Settings carried over | System rights moved |
| --- | --- | --- |
| `fylr-plugin-basemigration` | none — the plugin has no settings | `migration` |
| `fylr-scancode-display` | none | — |
| `fylr-plugin-coin-viewer` | none | — |
| `fylr-plugin-connector` | `connector` (the partner instances with login, password, client ID and secret; *enable all*), `fylr_url`, `connector_easydb4` | `allow_use`, `allow_use_as_server` |
| `fylr-plugin-custom-mask-splitter-detail-linked` | none | — |
| `fylr-plugin-detail-map` | `detail_map` (enabled, tiles, Mapbox token) | — |
| `fylr-plugin-display-field-values` | none | — |
| `fylr-plugin-drupal` | `drupal` (active, send files, maximum file size) | — |
| `fylr-plugin-easydb4migration` | `easydb4migration` (fylr URL, user, instance) | — the successor **adds** a right, see below |
| `editor-field-visibility` | none | — |
| `fylr-plugin-editor-tagfilter-defaults` | `editor-tagfilter-defaults` (the filter table) | — |
| `fylr-plugin-hijri-gregorian-converter` | none | — |
| `fylr-plugin-orcid` | none | — |
| `presentation-pptx` | none | — |
| `fylr-plugin-typo3` | `typo3` (active, send files, maximum file size, profile mapping) | — |
| `fylr-plugin-wordpress` | `wordpress` (the WordPress instances) | `wordpress` — the settings block is shown only to holders of this right, and the grant moves with it |

The plugins that keep their name keep their settings untouched, and the successor reads them as they are — the FTP transport's `rclone` block, the HTML editor's and the web link's settings among them. Two things are **new** rather than moved:

* **`fylr-plugin-easydb4migration` introduces a system right**, *easydb 4 Migration*, which the shipped plugin did not have. Its tool is shown only to users who hold the right, and after the upgrade nobody does — grant it to the groups or users who run the migration.
* **`pdf-creator` no longer has the `fylr_url` setting** — the value is carried along and ignored, see [PDF Creator and the PDF Server](disk-to-url-migration.md#pdf-creator-and-the-pdf-server).

#### The custom data types configure their updates differently

The custom data types keep their names, so the upgrade leaves their settings where they are — but it installs newer releases, and those define the **automatic update** differently from the versions fylr shipped. The shipped versions carried an easydb5 block, *Update interval* (`update_interval_<type>`, a number of days), which has no effect on fylr: fylr runs the update on its own schedule. The new releases replace it with a block of their own, `update_<type>`, that the update really reads — a time window, an expiry in days, for `gnd` and `dante` a URI replacement — and it starts at its **defaults**. Where the old block also held a value the plugin did use, enter it again in the new one: the **default language** for `dante`, `geonames` and `iconclass`, and the **GeoNames user name** for `geonames`, which now has a block of its own, `config_geonames`. The new block of `gvk` is called `update_k10plus`. `gazetteer` and `iucn` drop the old block without a replacement, and `iucn` also drops its easydb login block, which the fylr version does not need.

This is the plugin's new version, not the migration: an instance that already updated these data types from the marketplace has seen the change already. After the upgrade, open each data type's **Config** tab in the plugin manager and check the update settings.

### If you already replaced a shipped plugin by hand

Where a successor was installed by URL or from the marketplace **before** the upgrade, next to the shipped plugin, the upgrade finds it already there. For these the upgrade does **not** move the settings: the successor is there, so the shipped plugin is not renamed onto it, and its settings stay under the old name (see [What the upgrade will do](disk-to-url-migration.md#what-the-upgrade-will-do)). The successor uses the settings you entered for it, and nothing else.

If you have not entered them yet, carry them over through the plugin manager — the keys are the same for every renamed plugin, so the file of one is accepted by the other:

1. Open the shipped plugin and its **Config** tab, and choose **Download Config** from the tab's gear menu. The tab exists only while the plugin is **enabled**; switch it on for the moment if you have to.
2. Open the successor and its **Config** tab, choose **Upload Config**, pick the file, and **save**.

The file holds the settings as the plugin manager shows them, passwords and client secrets included, in plain text: keep it out of shared places and delete it when you are done. Do this **before** the upgrade — afterwards the shipped plugin is gone, and with it the tab; the settings themselves stay in the database under the old name, but nothing shows them any more.

If you can wait for 6.35, do not replace a shipped plugin by hand at all: the upgrade does it, and carries the settings and rights with it.

### The barcode plugins

Everything a plugin contributes to your data model — custom data types, mask splitters, PDF Creator elements — survives the migration, renames or not. The barcode plugins are the only case where the successor is a genuinely **different** plugin: **Scancode Display** registers its mask splitter and its PDF Creator element under new names.

The upgrade rewrites both for you: masks that used the barcode splitter now use the Scancode splitter, and PDF Creator templates containing a barcode element now contain a Scancode element. There is nothing to edit by hand, and `easydb-barcode-display-pdf-plugin` disappears because Scancode Display already contains that PDF element.

**Scancode Display requires PDF Creator.** It carries the PDF element, so it declares `pdf-creator` as a dependency and cannot be enabled without it. Nothing to do before you upgrade: where the barcode plugin is converted, the upgrade makes sure PDF Creator is installed and **switches it on**, including on an instance that had it switched off — otherwise Scancode Display would arrive unable to load while your masks had already been rewritten to its splitter. If you deliberately ran the barcodes without PDF Creator, this is the one place the upgrade turns a plugin on for you.

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
* The **custom data types' update settings** are at their defaults, because the new releases define them differently — see [above](disk-to-url-migration.md#the-custom-data-types-configure-their-updates-differently).
* `fylr-plugin-easydb4migration` has a **new system right** that nobody holds yet — see [Configuration, rights and exports](disk-to-url-migration.md#configuration-rights-and-exports).

Then check the things a plugin contributes to the data model: masks that use a **custom mask splitter** or a **custom data type**, and PDF Creator templates.

## Installations without internet access

If fylr cannot download a plugin's release, the plugin manager marks the row with a red **warning triangle** and the state **not installed**: the entry is there, the plugin is not running. Open it, go to the **Type** tab, and you get two buttons — **check now**, which asks the server to try the URL again, and **install as ZIP**, which routes the download through your browser instead of the server.

How much that second button does depends on where the plugin is hosted:

* Plugins delivered from **`programmfabrik.github.io`** — every paid and private one — are fetched by the browser directly and installed in one click.
* Plugins delivered from a **GitHub release** cannot be fetched by a browser at all: GitHub sends no CORS headers on release downloads, so the button falls back to a dialog showing the plugin's URL. Download that ZIP yourself — the link downloads normally — and upload it in the same dialog.

Either way it is the machine you administer from that needs to reach the release host, not the fylr server. If it cannot reach it either, fetch the ZIP on any machine that can and bring it over.

A plugin installed this way becomes a **zip plugin**: fylr keeps the bytes you uploaded, the **source URL is dropped** and the update policy is fixed to **never**. It stays exactly as uploaded until you repeat the step with a newer ZIP. To hand it back to the updater once the network allows, set its type back to **url** and enter the release URL again.
