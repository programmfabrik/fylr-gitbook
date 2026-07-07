---
description: >-
  The /inspect/recalcterms tool — rebuild the suggestion term list for every
  current record without re-saving them.
---

# Term Recalculation

The **Term Recalculation** page (`/inspect/recalcterms/`, also linked from `/inspect/terms/`) rebuilds the **term list** that powers the search bar's [suggestions](../../for-developers/concepts/search-and-events.md#suggestions-and-terms).

Terms are normally written when a record is saved, so a change to _how_ terms are extracted — a reworked custom-data-type field mapping, a datamodel change — only reaches records saved afterwards. A term recalculation applies the change to **every current record without re-saving them**.

## What it does

It rebuilds the term list for all current records in the background — below normal saves and below a re-index, so the instance stays usable while it works (it can take hours on a large instance). It also drops terms no longer carried by any record, and re-indexes the affected records afterwards. It never writes the records themselves, so it creates no new versions and no changelog entries.

On a fylr update, a release that changes term extraction can request the recalculation automatically.

## Running it

Start it from the page; it shows the current status and the last runs. Only one recalculation runs at a time. (In the JSON view, apitests poll `recalcterms/index` → `RecalcTerms` for the status.)

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [Search and events → Suggestions and terms](../../for-developers/concepts/search-and-events.md#suggestions-and-terms) — what the term list is.
