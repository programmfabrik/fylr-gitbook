# Hierarchies and polyhierarchies

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

When records of an objecttype form a tree. fylr supports two shapes:

- **Hierarchical** — every record has at most one parent. The classic tree.
- **Polyhierarchical** — every record can have any number of parents. The directed acyclic graph (DAG).

These two are **mutually exclusive**: an objecttype is one, the other, or neither — never both.

## Questions this page answers

- What does "hierarchical" mean for an objecttype, and what does it give you in the UI / API?
- What's the difference between a single-parent tree and a polyhierarchy (DAG)?
- Why can't an objecttype be both `is_hierarchical` and `polyhierarchical`? Why can't a `polyhierarchical` objecttype also be `acl_table`?
- When should you choose each? (Org charts and taxonomies vs. category systems where one item belongs in multiple categories.)
- How does `_id_parent` differ from `_object_parents`?
- What's a **reverse-hierarchical** column, and where does it show up?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — the building blocks.
- [Nested and reverse-nested tables](nested-and-reverse-nested.md) — a different sort of nesting (rows inside records, not records inside records).
- [Pools](pools.md) — pools also form a tree, but for a different reason.
