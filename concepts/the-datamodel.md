# The datamodel

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

The **datamodel** is the document that describes every objecttype in your instance — their fields, their links to other objecttypes, their masks, their tags. It is itself a versioned, committable object.

## Questions this page answers

- What does the datamodel define, and what doesn't it define?
- What's the difference between **HEAD**, **CURRENT** and a numeric datamodel version?
- Why does fylr keep both HEAD and CURRENT side by side?
- What happens during `POST /schema/commit`? What's different *after* a commit?
- Why does HEAD already have a version number before it's committed?
- When do datamodel changes trigger a reindex?
- What does `based_on_version` capture, and why does it matter for upgrades?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what the datamodel actually contains.
- [Masks](masks.md) — the per-mask layer on top of the datamodel.
- [FOR ADMINISTRATORS → Data Model](../for-administrators/) — editing the datamodel in the UI.
- [FOR DEVELOPERS → /schema](../for-developers/api/) — reading and writing it programmatically.
