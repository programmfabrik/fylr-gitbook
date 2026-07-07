---
description: >-
  Map metadata between the XMP/IPTC/EXIF tags in a file and the fields of a fylr
  record — on upload (import) and on download (export).
---

# Metadata Mapping

A **metadata mapping** connects the metadata **tags** embedded in a file (XMP, IPTC, EXIF) with the **fields** of a fylr record. It works in both directions:

* **Import** — when a file is **uploaded**, the mapping reads tags from the file and writes them into the record's fields.
* **Export** — when a file is **downloaded**, the mapping writes the record's field values into the file's metadata.

A mapping is a named **profile** of individual rules, each pairing one field with one metadata tag. A profile can be chosen by the user when uploading or downloading a file, or set as a default per object type or pool — see [How to Set Default Metadata Mappings](../help/tutorials/for-administrators/default-export-metadata-mappings.md).

{% hint style="info" %}
Using a mapping needs the system right **Import Metadata** / **Export Metadata** (at least _Standard Profile Only_).
{% endhint %}

## Tags

Each rule targets a metadata tag. Standard XMP, IPTC and EXIF tags can be picked from the list. From fylr **6.34.0**, an **export** mapping can additionally write a **custom XMP tag**: type any `XMP-<group>:<tag>` path into the tag field.

* For a **known group** (for example `dc`), fylr extends the built-in table so the tag lands in its real namespace.
* For an **unknown group**, fylr defines the tag on the fly with an ExifTool-convention namespace named after the group.

Only XMP is extensible — custom EXIF or IPTC tags cannot be created. Custom tags typed starting with a lower-case letter are matched case-insensitively on import, so a round-trip mapping reads back what it wrote (ExifTool stores every tag with its first letter capitalized).

## Value shape — the _Typ_ selector

A tag can hold a single value, a list of values, or values localized per language. The mapping editor's **Typ** selector picks how a field's value is written:

* **single value** — one joined string.
* **list** — one entry per value (an XMP _Bag_ or _Seq_).
* **localized** — one value per language (an XMP _lang-alt_ structure).

From fylr **6.34.0** the offered options follow the selected tag's real capability: a built-in tag shows its fixed shape as pre-set, locked checkboxes (only the list opt-out — write a single joined value instead of a list — stays selectable where the tag supports lists), while a custom tag offers the options freely.

## Field types

Most field types round-trip through a mapping. A few notes:

* **Date ranges** (`daterange`) — from fylr **6.34.0** a daterange can also be **imported**, completing the export that already existed. The import reads the "from – to" form fylr's own export writes (including a single date and open-ended ranges), so a daterange survives an export/re-import cycle. Arbitrary external date-range metadata is not parsed, as there is no standard representation for it.
* **Linked and nested fields** — a mapping can target a field of a linked object through the linked object type's **preferred mask**, which governs how the linked record is loaded and mapped.

### Multi-column linked objects (import)

An import mapping can address **several columns of the same linked object** — for example a nested keyword's name and its localization. The columns zip positionally into one linked object per row:

* the **first** mapped column is the **lookup key**;
* a **key match** links the existing object (the file's further columns are discarded — a file import never edits a shared vocabulary record);
* an **unmatched key** creates the linked object with all imported columns;
* when several existing objects share the key name, the further columns pick the one the file agrees with.

Localized values are compared only for the languages both sides have, since exported files fill missing translations with the fallback language. All addressed columns must be part of the linked object type's preferred mask.
