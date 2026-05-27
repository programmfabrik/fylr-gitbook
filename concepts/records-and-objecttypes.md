# Records and objecttypes

**Status: stub.** This page is part of the [Concepts](README.md) section. Below is the outline of what the page needs to answer; the prose is still being written.

## What this page covers

The two most foundational words in fylr: a **record** (a single stored thing — a photo, a product, an article) and an **objecttype** (the shape every record of a given kind must take — "Photo", "Product", "Article").

## Questions this page answers

- What is a record? What does fylr store on every record regardless of what kind it is?
- What is an objecttype? How is it different from the records that conform to it?
- What's the difference between an objecttype and a basetype?
- What identifies a record uniquely? (`_id`, `_uuid`, `_system_object_id`, `_global_object_id` — and when you use which.)
- What does it mean for a record to have a version (`_version`)?
- Why does fylr split "records" into "live", "history" and "deleted"?

## See also

- [Files and assets](files-and-assets.md) — files attach to records but aren't records themselves.
- [The datamodel](the-datamodel.md) — the document that holds all your objecttype definitions.
- [Masks](masks.md) — different views over the same objecttype.
- [FOR ADMINISTRATORS → Object Types](../for-administrators/permissions/object-types.md) — administering objecttypes.
