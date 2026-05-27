# Search and events

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

How fylr finds records (**search**, distinct from the lookup-by-id `/db`) and how it remembers what happened (**events**, the append-only log of every change).

## Questions this page answers

- Why is search a different endpoint from `/db`? What does each one do?
- What does it mean for a field to be **expert-searchable**, **fulltext-searchable**, **facetable**, or **nested-searchable**?
- What's a **search context**?
- What's an **aggregation** in a search request? What does the response carry?
- What's the **point-in-time** mechanism, and when do you use it?
- What's an **event**? What kinds of events does fylr write?
- What's the difference between **polling** (`/event/poll/{fromEventId}`) and **streaming** (`/event/stream`)?
- What does the **event log** let you recover? (Change history per record.)
- What's a **user event**, and what system right do you need to write one?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what gets indexed and observed.
- [The datamodel](the-datamodel.md) — datamodel changes that trigger reindexing.
- [FOR DEVELOPERS → /search](../for-developers/api/) and **/event** in the API reference.
