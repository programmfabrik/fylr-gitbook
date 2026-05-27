# Nested and reverse-nested tables

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

A **nested table** is an objecttype whose records have no independent existence — they live as a list of rows inside a top-level record on a different objecttype. They don't have their own ACL, they don't have an owner, you don't address them directly.

A **reverse-nested table** is the same thing, seen from the other side: when an objecttype is nested under another, the parent objecttype can expose the list of nested rows back as a field.

## Questions this page answers

- Why do nested tables exist? Why isn't every objecttype just a regular top-level objecttype?
- When does the modeller use a nested table, and when do they use a linked objecttype instead?
- How do nested rows appear on the wire? (`_nested:<name>` and `_reverse_nested:<name>` fields on the top-level record.)
- What can't a nested objecttype do? (No `_acl`, no `_owner`, no `reverse_link` columns.)
- Why does the descriptor for "nested under" still say `owned_by`? The historical naming.
- What's the difference between a **nested** link and a regular **link**?
- When fylr was easydb 5, nested rows lived in their own DB table. Why doesn't fylr 6 (the Go rewrite) work that way any more?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what nested rows are nested under.
- [Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md) — a different kind of nesting (record-in-record, not row-in-record).
- [The datamodel](the-datamodel.md) — where nested tables are declared.
