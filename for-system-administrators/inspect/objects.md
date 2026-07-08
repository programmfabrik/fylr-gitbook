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

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [Anatomy of a Record](../../for-developers/record-json.md) — the record JSON shape.
