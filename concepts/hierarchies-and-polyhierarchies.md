# Hierarchies and polyhierarchies

Some kinds of record only make sense as a tree. A Department has a parent department. A Taxonomy term has a broader term. A Subject heading has a more general subject heading. The relationship between a record and its "parent" is special enough that fylr offers two purpose-built shapes for it.

This page is about those two shapes — when each is the right tool, and the consequences of choosing one over the other.

## Two shapes

When the datamodel marks an objecttype as **hierarchical**, every record of that objecttype can have **at most one parent**. The records of that objecttype together form a classic tree: the museum's location hierarchy (Continent → Country → Region → City), the publishing house's editorial structure (Imprint → Series → Title), a taxonomy where every term has exactly one broader term.

When the datamodel marks an objecttype as **polyhierarchical**, every record of that objecttype can have **any number of parents**. The records form a directed acyclic graph (DAG) rather than a tree: a Photo Subject "Beach holiday" might sit under both "Travel" and "Leisure", a Recipe Ingredient under both "Vegetable" and "Vitamin source", a Subject Heading under several broader headings.

The two are **mutually exclusive**. An objecttype is hierarchical, polyhierarchical, or neither — never both. They model different things, and the difference matters as soon as the tooling for parent-aware behaviour kicks in.

## How parents are kept

When the objecttype is hierarchical, every record carries a single **parent link** — a pointer to one other record of the same objecttype (or no parent at all, in which case the record is at the root of the tree). The link is a stored value on the record, just like any other field; reading the record gives you its parent immediately.

When the objecttype is polyhierarchical, every record carries a **list of parents** instead. There can be zero, one, or many entries. The list is exposed as a system field on the record — fylr maintains it automatically as parent links are added and removed.

In both cases, fylr lets you ask for the child side of the relationship too: given a record, the **reverse view** lists every record whose parent link points back at it. The reverse view is what powers tree-shaped pickers in the UI ("show me the children of Country=Germany") and what makes it possible to traverse the structure from the top down.

## Why polyhierarchies can't also be ACL-bearing

If a polyhierarchical objecttype were also configured to carry its own per-record permissions, fylr would have to decide what those permissions inherit from when a record has more than one parent. There is no honest answer to that question: each parent might confer different permissions, and silently picking one would surprise an administrator who had granted the other. fylr's datamodel validator rejects the combination outright. A polyhierarchical objecttype either takes its permissions from its pool or has no per-record permissions at all.

This is the most common reason a modeller pulls back from polyhierarchy. If the records absolutely need their own ACL — sensitive material that must be locked down per item — then either the parent relationship must collapse to a single-parent tree, or the ACL has to move to the pool.

## When to pick which

The most useful question is: _can a single record honestly belong to more than one parent in the real world?_

- **Pick hierarchy** when the answer is no. Locations, departments, subordination structures, file-system-shaped folders, dictionary-style taxonomies where one term has one broader term.
- **Pick polyhierarchy** when the answer is yes and the user expects to navigate from any of those parents to the record. Tag-style categorisation, subject headings, faceted classification, recipe ingredients that fall into multiple food groups.

A third option is to **pick neither** — treat the parent relationship as an ordinary link between records, not a structural relation. This costs you the tree-aware UI and the reverse view, but it's the right call when the relationship is more like "see also" than "is a kind of".

## See also

- [Records and objecttypes](records-and-objecttypes.md) — the building blocks. The flags on an objecttype.
- [Nested and reverse-nested tables](nested-and-reverse-nested.md) — a different kind of nesting (rows inside a single record, not records inside records).
- [Pools](pools.md) — pools also form a tree, but for a different reason and with different mechanics.
- [Permissions](permissions.md) — why ACLs and polyhierarchy can't coexist on the same objecttype.
