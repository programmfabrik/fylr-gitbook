---
description: >-
  The /inspect/objects tool — dump a record's raw data and render it against any
  datamodel version.
---

# Objects

The **Objects** page (`/inspect/objects/`) shows a single record's stored data and lets you **render it against any datamodel version** — the tool for debugging a record whose datamodel has changed (a polyhierarchy-to-hierarchy switch, a migration, a mapping change).

## What it shows

Enter a record's `_system_object_id` (and optionally its objecttype). The page loads the record and shows:

* its raw stored values, across all versions;
* how it **renders** — `_standard`, parents / children, links — under a **datamodel selector**. Because objecttypes are not versioned per datamodel, the parent and hierarchy sections reflect the datamodel you pick; that is what makes the page useful for a before/after comparison.

The JSON view (used by monitoring) reports the reindex ids, the current / rendering / object datamodel ids and any warning.

## The IIIF viewer

**From version 6.36.0** the record page lists **/api/objects (IIIF Clover)** under **Resources**. It opens the record's IIIF manifest in the [Clover](https://github.com/samvera-labs/clover-iiif) viewer on an inspect page of its own, in the mask chosen there. **/api/objects (IIIF Mirador)** opens the same manifest on projectmirador.org in a new tab.

The viewer requests the manifest like any IIIF client, as a deep link without the inspect login, so it needs deep link access in the base configuration; the page warns when that is off. The browser loads Clover from cdn.jsdelivr.net: when a firewall or proxy blocks that host, the page says so, and the manifest link on the page opens in any other IIIF viewer.

## The object list

`/inspect/objects/` lists the objecttypes with their record counts; picking one opens that objecttype's **object list**, a paged table of its records with id, system object id, version, pool and standard info.

The **Sort By** select sorts that table (↑ ascending, ↓ descending); the list opens with the newest records first. Besides system object id and internal id, **from version 6.35.0** it sorts by **version count**: "Version ↓" puts the records with the most versions first — how you spot records that collect versions unexpectedly. The version number on a record's latest row is its number of versions, so no separate count is involved; on a large objecttype that order reads all its records, so give the page a moment.

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [Anatomy of a Record](../../for-developers/record-json.md) — the record JSON shape.
