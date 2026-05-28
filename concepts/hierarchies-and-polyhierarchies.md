# Hierarchies and polyhierarchies

An objecttype can be configured so that its records form a tree or a graph, with records standing in a parent relationship to one another. fylr supports two shapes for this.

## Two shapes

A **hierarchical** objecttype gives each record at most one parent. Its records form a tree: a location structure (Continent → Country → Region → City), an editorial structure (Imprint → Series → Title), a taxonomy where each term has one broader term.

A **polyhierarchical** objecttype gives each record any number of parents. Its records form a directed acyclic graph (DAG): a subject "Beach holiday" under both "Travel" and "Leisure", an ingredient under both "Vegetable" and "Vitamin source", a subject heading under several broader headings.

An objecttype is hierarchical, polyhierarchical, or neither — never both.

## How parents are held

In a hierarchical objecttype, each record holds a single parent reference, pointing to one other record of the same objecttype, or to none if the record is at the root. Reading the record gives its parent.

In a polyhierarchical objecttype, each record holds a list of parents — zero, one or many. fylr maintains the list as parent references are added and removed.

In both cases fylr also provides the reverse direction: given a record, it can list the records whose parent reference points to it. This reverse view drives tree-shaped pickers in the interface and traversal from the top of the structure downward.

## Polyhierarchy and per-record permissions

A polyhierarchical objecttype cannot also carry its own per-record permissions. With more than one parent, there is no single parent for a record to inherit permissions from, and the datamodel rejects the combination. A polyhierarchical objecttype's records take their permissions from their pool.

This is the usual reason to reconsider a polyhierarchy. If records must carry their own permissions, the relationship has to be a single-parent tree, or the permissions have to sit on the pool.

## Choosing between them

The deciding question is whether a single record can belong to more than one parent in the real world.

- **Hierarchy** — when it cannot. Locations, departments, reporting structures, folder-shaped taxonomies where each term has one broader term.
- **Polyhierarchy** — when it can, and the record should be reachable from each of its parents. Subject headings, faceted classification, items that fall into several categories.

A third option is to use an ordinary link between records rather than a structural parent relationship. This gives up the tree-aware interface and the reverse view, and suits relationships closer to "see also" than "is a kind of".

## See also

- [Records and objecttypes](records-and-objecttypes.md) — the objecttype these are configured on.
- [Nested and reverse-nested tables](nested-and-reverse-nested.md) — rows held inside a single record, a different kind of nesting.
- [Pools](pools.md) — pools also form a tree, with different mechanics.
- [Permissions](permissions.md) — why per-record permissions and polyhierarchy are mutually exclusive.
