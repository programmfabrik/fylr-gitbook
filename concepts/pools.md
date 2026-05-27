# Pools

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

A **pool** is the primary container for live records in fylr. Every live record (of an objecttype that's _pooled_) belongs to exactly one pool. Pools themselves form a tree, and many properties — ACL, transitions, tags, default masks — flow from a parent pool down to its sub-pools unless explicitly overridden.

## Questions this page answers

- What does it mean for a record to "belong to" a pool? Why are pools the container?
- What's the pool tree, and how is it different from an objecttype hierarchy?
- What inherits from a parent pool down to a sub-pool? What is private?
- What's a **system pool**? Why can't you delete it?
- What does `_private_acl` / `_private_transitions` / `_private_tags` do?
- Which objecttypes are _not_ pooled? (See `pool_link: false` and `owned_by`.)
- What is a **pool contact**? Where does `who._pool_contact` resolve?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what lives in pools.
- [Permissions](permissions.md) — how pool ACLs interact with object ACLs.
- [Tags and transitions](tags-and-transitions.md) — what else inherits down the pool tree.
- [FOR ADMINISTRATORS → Pools](../for-administrators/permissions/pools.md) — administering pools.
