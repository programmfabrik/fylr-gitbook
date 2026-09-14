---
label: Plugin Overview
description: >-
  The plugins Programmfabrik offers in the fylr plugin marketplace, and the ones
  that are installed by URL.
---

# Plugin Overview

{% hint style="info" %}
**The list that counts is in your instance.** From fylr **6.35.0** the plugin manager's **plus** button opens the [marketplace](../for-administrators/plugin-manager/README.md#plugin-marketplace), which fylr pulls from Programmfabrik's published catalog when you open it. It is always current, it shows each plugin's version and release date, and it installs with one click — including anything a plugin depends on. This page is a snapshot of that catalog for reading offline, plus a list of plugins that exist but are not offered in the shop.
{% endhint %}

The name in the first column is the plugin's **internal name** — what the plugin manager, the API, the base configuration and the log lines call it. It is not always the repository name.

| Mark | Meaning |
| --- | --- |
| **licensed** | A paid plugin. It installs freely, but your fylr **license** has to grant it by name before it can be **enabled** — see [License management](../license-management.md). |
| private repository | The source is not public, so the repository link is omitted. The plugin itself installs normally: private and paid plugins are delivered **sealed** and fylr decrypts them during the install. |
| custom data type | The plugin contributes a new field type to the data model. |
| needs `…` | The plugin requires another plugin. Installing it from the marketplace offers the missing one first; it cannot be enabled without it. |

## In the marketplace

The sections below are the categories the marketplace groups by.

### Authority data and vocabularies

| Plugin | What it does | Repository |
| --- | --- | --- |
| `custom-data-type-cerlthesaurus`<br>custom data type, needs `commons-library` | Custom data type for fylr to link records to entities of the CERL Thesaurus (data.cerl.org). | [fylr-plugin-custom-data-type-cerlthesaurus](https://github.com/programmfabrik/fylr-plugin-custom-data-type-cerlthesaurus) |
| `custom-data-type-dante`<br>custom data type, needs `commons-library` | Custom data type for fylr linking records to vocabularies on the DANTE terminology server (dante.gbv.de). | [fylr-plugin-custom-data-type-dante](https://github.com/programmfabrik/fylr-plugin-custom-data-type-dante) |
| `custom-data-type-gazetteer`<br>custom data type | Custom data type linking records to places in the iDAI.gazetteer of the German Archaeological Institute. | [fylr-plugin-custom-data-type-gazetteer](https://github.com/programmfabrik/fylr-plugin-custom-data-type-gazetteer) |
| `custom-data-type-geonames`<br>custom data type, needs `commons-library` | Custom data type for fylr linking records to the GeoNames geographical database (geonames.org). | [fylr-plugin-custom-data-type-geonames](https://github.com/programmfabrik/fylr-plugin-custom-data-type-geonames) |
| `custom-data-type-getty`<br>custom data type, needs `commons-library` | Custom data type for fylr linking records to the Getty Vocabularies AAT, TGN and ULAN. | [fylr-plugin-custom-data-type-getty](https://github.com/programmfabrik/fylr-plugin-custom-data-type-getty) |
| `custom-data-type-gfbio`<br>custom data type, needs `commons-library` | Custom data type for fylr linking records to ontologies in the GFBio Terminology Service. | [fylr-plugin-custom-data-type-gfbio](https://github.com/programmfabrik/fylr-plugin-custom-data-type-gfbio) |
| `custom-data-type-gn250`<br>custom data type, needs `commons-library` | Custom data type for fylr linking records to the GN250 geodata of the German cartography agency BKG. | [fylr-plugin-custom-data-type-gn250](https://github.com/programmfabrik/fylr-plugin-custom-data-type-gn250) |
| `custom-data-type-gnd`<br>custom data type, needs `commons-library` | Custom data type for linking fylr records to entities of the Integrated Authority File (GND). | [fylr-plugin-custom-data-type-gnd](https://github.com/programmfabrik/fylr-plugin-custom-data-type-gnd) |
| `custom-data-type-goobi`<br>custom data type, needs `commons-library` | Custom data type for linking fylr records to processes in an intranda Goobi workflow production system. | [fylr-plugin-custom-data-type-goobi](https://github.com/programmfabrik/fylr-plugin-custom-data-type-goobi) |
| `custom-data-type-gvk`<br>custom data type, needs `commons-library` | Custom data type for linking fylr records to titles in the k10plus union catalogue (kxp.k10plus.de). | [fylr-plugin-custom-data-type-k10plus](https://github.com/programmfabrik/fylr-plugin-custom-data-type-k10plus) |
| `custom-data-type-iconclass`<br>custom data type, needs `commons-library` | Custom data type for linking fylr records to the Iconclass iconographic classification (iconclass.org). | [fylr-plugin-custom-data-type-iconclass](https://github.com/programmfabrik/fylr-plugin-custom-data-type-iconclass) |
| `custom-data-type-iucn`<br>custom data type | Custom data type linking records to species in the IUCN Red List. | [fylr-plugin-custom-data-type-iucn](https://github.com/programmfabrik/fylr-plugin-custom-data-type-iucn) |
| `custom-data-type-loc`<br>custom data type, needs `commons-library` | Custom data type for linking fylr records to Library of Congress authorities and vocabularies (id.loc.gov). | [fylr-plugin-custom-data-type-loc](https://github.com/programmfabrik/fylr-plugin-custom-data-type-loc) |
| `custom-data-type-nomisma`<br>custom data type, needs `commons-library` | Custom data type for linking fylr records to numismatic resources of the Nomisma project (nomisma.org). | [fylr-plugin-custom-data-type-nomisma](https://github.com/programmfabrik/fylr-plugin-custom-data-type-nomisma) |
| `custom-data-type-tnadiscovery`<br>custom data type, needs `commons-library` | Custom data type for fylr that links records to entities in The National Archives (London) Discovery system. | [fylr-plugin-custom-data-type-tnadiscovery](https://github.com/programmfabrik/fylr-plugin-custom-data-type-tnadiscovery) |
| `custom-data-type-wikidata`<br>custom data type, needs `commons-library` | Custom data type for fylr that links records to Wikidata entities with autocomplete and multilingual faceting. | [fylr-plugin-custom-data-type-wikidata](https://github.com/programmfabrik/fylr-plugin-custom-data-type-wikidata) |

### Editor

| Plugin | What it does | Repository |
| --- | --- | --- |
| `custom-data-type-html-editor`<br>custom data type | Adds a WYSIWYG editor and stores HTML content in a field. | [fylr-plugin-custom-data-type-html-editor](https://github.com/programmfabrik/fylr-plugin-custom-data-type-html-editor) |
| `editor-field-visibility` | Mask splitter that shows or hides editor fields depending on another field's value. | [fylr-plugin-editor-field-visibility](https://github.com/programmfabrik/fylr-plugin-editor-field-visibility) |
| `fylr-plugin-sequence` | Fills empty fields with sequential numbers, following a configurable template. | [fylr-plugin-sequence](https://github.com/programmfabrik/fylr-plugin-sequence) |
| `fylr-scancode-display`<br>needs `pdf-creator` | Mask splitter rendering barcodes and QR codes from field data, in masks and in PDF Creator templates. | [fylr-plugin-scancode-display](https://github.com/programmfabrik/fylr-plugin-scancode-display) |

### Geo

| Plugin | What it does | Repository |
| --- | --- | --- |
| `custom-data-type-georef`<br>custom data type, needs `commons-library` | Custom data type for fylr to draw and store points, lines and polygons on a map as GeoJSON. | [fylr-plugin-custom-data-type-georef](https://github.com/programmfabrik/fylr-plugin-custom-data-type-georef) |
| `custom-data-type-location`<br>custom data type | Custom data type for geographic coordinates, entered on a map. | [fylr-plugin-custom-data-type-location](https://github.com/programmfabrik/fylr-plugin-custom-data-type-location) |
| `geo-json`<br>private repository | GeoJSON support for fylr: map views and editors for geographic fields, geo search, and custom styles. | `fylr-plugin-geo-json` |

### Media

| Plugin | What it does | Repository |
| --- | --- | --- |
| `obscure-image`<br>**licensed**, private repository | Pixelate, blur, or blackout regions of an image as a new asset variant, from the fylr asset editor. | `fylr-plugin-obscure-image` |
| `pdf-creator`<br>private repository | HTML-to-PDF generation for fylr, with support for custom CSS styling. | `fylr-plugin-pdf-creator` |

### Integration

| Plugin | What it does | Repository |
| --- | --- | --- |
| `easydb-export-transport-ftp-plugin` | Export transport that delivers the produced files to an FTP or WebDAV server. | [fylr-plugin-export-transport-ftp](https://github.com/programmfabrik/fylr-plugin-export-transport-ftp) |
| `fylr-plugin-drupal`<br>**licensed**, private repository | Publish selected fylr assets straight into Drupal content, without manual download and re-upload. | `fylr-plugin-drupal` |
| `fylr-plugin-typo3`<br>**licensed**, private repository | Transport fylr records and media to a TYPO3 CMS site. | `fylr-plugin-typo3` |
| `fylr-plugin-wordpress`<br>**licensed**, private repository | Transport fylr media files and metadata to a WordPress CMS, with scheduled and incremental updates. | `fylr-plugin-wordpress` |

### AI

| Plugin | What it does | Repository |
| --- | --- | --- |
| `ai-metadata`<br>**licensed**, private repository | Sends an object’s image to a Large Language Model and writes the answers back into its fields. | `fylr-plugin-ai-metadata` |

### Other

| Plugin | What it does | Repository |
| --- | --- | --- |
| `custom-data-type-link`<br>custom data type | Custom data type for a web link: stores a URL together with its link text. | [fylr-plugin-custom-data-type-weblink](https://github.com/programmfabrik/fylr-plugin-custom-data-type-weblink) |
| `fylr-plugin-basemigration`<br>private repository | Plugin for fylr to export and import basetype settings. | `fylr-plugin-basemigration` |
| `fylr-plugin-coin-viewer` | Adds an interactive 3D coin viewer to the detail sidebar. | [fylr-plugin-coin-viewer](https://github.com/programmfabrik/fylr-plugin-coin-viewer) |
| `fylr-plugin-connector`<br>private repository | Includes other easydb5 or fylr installations in your search, across several instances at once. | `fylr-plugin-connector` |
| `fylr-plugin-custom-mask-splitter-detail-linked` | Mask splitter listing the records that link to the record shown — reverse references. | [fylr-plugin-custom-mask-splitter-detail-linked](https://github.com/programmfabrik/fylr-plugin-custom-mask-splitter-detail-linked) |
| `fylr-plugin-detail-map` | Shows a record's files on a map in the detail view. | [fylr-plugin-detail-map](https://github.com/programmfabrik/fylr-plugin-detail-map) |
| `fylr-plugin-display-field-values` | Mask splitter that displays field values of the current object. | [fylr-plugin-display-field-values](https://github.com/programmfabrik/fylr-plugin-display-field-values) |
| `fylr-plugin-easydb4migration`<br>private repository | Migrates an easydb4 installation into fylr. | `fylr-plugin-easydb4migration` |
| `fylr-plugin-editor-tagfilter-defaults` | Pre-fills editor fields with defaults chosen by the record’s tags and pool. | [fylr-plugin-editor-tagfilter-defaults](https://github.com/programmfabrik/fylr-plugin-editor-tagfilter-defaults) |
| `fylr-plugin-hijri-gregorian-converter` | Custom mask splitter converting between Hijri and Gregorian dates in the fylr editor. | [fylr-plugin-hijri-gregorian-converter](https://github.com/programmfabrik/fylr-plugin-hijri-gregorian-converter) |
| `fylr-plugin-orcid` | Connects users to ORCID, so each user can store their own ORCID iD. | [fylr-plugin-orcid](https://github.com/programmfabrik/fylr-plugin-orcid) |
| `presentation-pptx` | Export plugin for fylr: downloads the objects of a collection as a PowerPoint presentation (PPTX). | [fylr-plugin-presentation-pptx](https://github.com/programmfabrik/fylr-plugin-presentation-pptx) |


### The shared library

`commons-library` carries functions the VZG custom data types have in common. It is not browsable in the marketplace and needs no configuration — fylr installs it by itself as a dependency of the data types that need it, listed above. Source: [fylr-plugin-commons-library](https://github.com/programmfabrik/fylr-plugin-commons-library).

## Not in the marketplace

These plugins are not offered in the shop — they are specific to one customer, or a developer example. They install like any other **url** plugin: take the release URL from the repository's README and enter it in the plugin manager under **plus → URL**. They are not curated, so check the repository before you rely on one.

| Plugin | What it does | Repository |
| --- | --- | --- |
| `collection-csv-import` | Imports a CSV file into a collection, server side. | [fylr-plugin-collection-csv-import](https://github.com/programmfabrik/fylr-plugin-collection-csv-import) |
| `custom-vzg-validationhub` | Sends data to the validation centre of the [VZG](https://www.gbv.de/informationen/Verbundzentrale) for content validation. | [fylr-plugin-custom-vzg-validationhub](https://github.com/programmfabrik/fylr-plugin-custom-vzg-validationhub) |
| `default-values-from-pool` | Per-pool default values for fields, configured in the base configuration and applied from the data model. | [fylr-plugin-default-values-from-pool](https://github.com/programmfabrik/fylr-plugin-default-values-from-pool) |
| `edit-info-updater` | Updates an "Edited by" and an "Edit date" field whenever a watched field or tag changes. | [fylr-plugin-edit-info-updater](https://github.com/programmfabrik/fylr-plugin-edit-info-updater) |
| `find-duplicate-field-values` | Mask splitter on a text field that says in the editor whether the same value already exists in the user's visibility range. | [fylr-plugin-find-duplicate-field-values](https://github.com/programmfabrik/fylr-plugin-find-duplicate-field-values) |
| `fjc` | Stores the settings of the Attention-developed fylr Java classes. | [fylr-plugin-fjc](https://github.com/programmfabrik/fylr-plugin-fjc) |
| `formula-columns` | Computes a column's value from a small JavaScript snippet that runs on the server at every save. | [fylr-plugin-formula-columns](https://github.com/programmfabrik/fylr-plugin-formula-columns) |
| `fylr-plugin-ai-validator` | Runs AI and other validations over texts such as user comments, to flag what editorial staff should moderate. | [fylr-plugin-ai-validator](https://github.com/programmfabrik/fylr-plugin-ai-validator) |
| `fylr-plugin-custom-data-type-doris` | Custom data type "DoRIS", connecting fylr to the [DoRIS DMS](https://doris-dms.de/). | [fylr-plugin-custom-data-type-doris](https://github.com/programmfabrik/fylr-plugin-custom-data-type-doris) |
| `fylr-plugin-custom-data-type-finto` | Custom data type linking records to the Finnish thesaurus and ontology service [FINTO](https://finto.fi/). | [fylr-plugin-custom-data-type-finto](https://github.com/programmfabrik/fylr-plugin-custom-data-type-finto) |
| `fylr-plugin-custom-data-type-nfis-geometry` | Custom data type "Geometry link via WFS-T and Masterportal". | [fylr-plugin-custom-data-type-nfis-geometry](https://github.com/programmfabrik/fylr-plugin-custom-data-type-nfis-geometry) |
| `fylr-plugin-custom-l10n` | Adds new localization keys, or overwrites existing ones. | [fylr-plugin-custom-l10n](https://github.com/programmfabrik/fylr-plugin-custom-l10n) |
| `fylr-plugin-ejc`<br>private repository | Supports EJC classes. | `fylr-plugin-ejc` |
| `fylr-plugin-linked-object-use-once` | Allows a given object to be linked only once; a second link is refused with an API error, the way a TAN list is used up. | [fylr-plugin-linked-object-use-once](https://github.com/programmfabrik/fylr-plugin-linked-object-use-once) |
| `fylr-plugin-mask-splitter-custom-javascript` | Mask splitter that runs any custom JavaScript. | [fylr-plugin-mask-splitter-custom-javascript](https://github.com/programmfabrik/fylr-plugin-mask-splitter-custom-javascript) |
| `fylr-plugin-nfis-denkxweb-export` | Custom API endpoint for the NFIS DenkXweb export. | [fylr-plugin-nfis-denkxweb-export](https://github.com/programmfabrik/fylr-plugin-nfis-denkxweb-export) |
| `fylr-plugin-numeric-id-auto-incrementer` | Fills numeric ID fields automatically when a record is saved. | [fylr-plugin-numeric-id-auto-incrementer](https://github.com/programmfabrik/fylr-plugin-numeric-id-auto-incrementer) |
| `fylr-plugin-tray-link-manager` | Creates and manages the tray links in the app header. | [fylr-plugin-tray-link-manager](https://github.com/programmfabrik/fylr-plugin-tray-link-manager) |
| `fylr-plugin-ubhd-3d-viewer` | 3D viewer of Heidelberg University Library, based on 3DHOP, three.js and Relight. | [fylr-plugin-ubhd-3d-viewer](https://github.com/programmfabrik/fylr-plugin-ubhd-3d-viewer) |
| `fylr_example` | The developer example: one plugin demonstrating extensions, callbacks and frontend snippets. Not for production use. | [fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example) |
| `monitoring-endpoint` | Adds a monitoring endpoint at `GET /api/v1/plugin/base/monitoring/monitoring`. | [fylr-plugin-monitoring](https://github.com/programmfabrik/fylr-plugin-monitoring) |
| `pdf-creator-custom-value` | Lets a PDF Creator template compute values with custom JavaScript. | [fylr-plugin-pdf-creator-custom-value](https://github.com/programmfabrik/fylr-plugin-pdf-creator-custom-value) |
| `signaturegenerator` | Generates signatures automatically from predefined patterns. | [fylr-plugin-signature-generator](https://github.com/programmfabrik/fylr-plugin-signature-generator) |
| `user-logo` | Uses a user's own image as the logo in the frontend and in PDF Creator. | [fylr-plugin-user-logo](https://github.com/programmfabrik/fylr-plugin-user-logo) |

## Gone with fylr 6.35

Up to fylr 6.34 the distribution shipped a fixed set of plugins on disk. From 6.35 it ships none, and the plugins in your instance are converted to url plugins at the upgrade. Which plugin becomes what, and which ones are dropped, is the subject of its own page:

* [Disk to URL plugin migration](disk-to-url-migration.md)

Two entries that used to be on this page are worth naming here:

* **`server-pdf`** rendered the HTML for **PDF Creator**. PDF Creator has rendered its own PDFs since version 1.1.0, so `server-pdf` has left the catalog and the upgrade switches it off where PDF Creator is enabled — see [PDF Creator and the PDF Server](disk-to-url-migration.md#pdf-creator-and-the-pdf-server).
* **`easydb-barcode-display`** and **`easydb-barcode-display-pdf-plugin`** are succeeded by [`fylr-scancode-display`](https://github.com/programmfabrik/fylr-plugin-scancode-display), which contains both the mask splitter and the PDF Creator element.

The plugins in the easydb5 repositories (`easydb-*`) are not fylr plugins. Where a fylr successor exists it is listed above, under the successor's name.
