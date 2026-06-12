# Pools

A **pool** is fylr's primary container for records. Most records live in a pool. A pool is like a folder, but it also carries permissions, decides which workflow transitions are available, holds tags, and sets which mask is preferred for each objecttype. Sub-pools inherit these from their parent unless configured otherwise.

## What a pool is

A pool is a record with a name, a description, an owner, optional sub-pools, and a configuration that applies to the records it contains. Permissions are the main reason data is organised into pools: a grant on a pool applies to every record in it, where the same grant would otherwise have to be repeated on each record. A museum can use one pool per department, a publisher one per imprint, an agency one per client.

Most objecttypes are configured so that their records must sit in a pool. A few administrative objecttypes are instance-global and have no pool. Whether an objecttype's records are pooled is set on the objecttype in the [datamodel](the-datamodel.md).

## The pool tree

Pools form a tree. There is a root pool at the top, every other pool has one parent, and the depth is set by the administrator. The interface shows the tree as folder-like navigation.

This tree is not the same as a [hierarchical objecttype's](hierarchies-and-polyhierarchies.md) tree. An objecttype hierarchy relates records of one kind (a Department under a Department). The pool tree relates containers, and records of any pooled objecttype live in them. The two are independent.

## What sub-pools inherit

By default, several parts of a pool's configuration are inherited by its sub-pools. The administrator chooses which.

- **Permissions.** Grants on a pool apply to records in that pool and, by default, in its sub-pools. A read grant on the "Publishing" pool applies throughout the Publishing sub-tree.
- **Transitions.** [Transitions](tags-and-transitions.md) on a pool are offered to records in it and, by default, in its sub-pools.
- **Tags.** A pool can hold tags that apply to records in its sub-tree. Sub-pools inherit them by default.
- **Preferred masks.** A pool can prefer a particular [mask](masks.md) for each objecttype. The preference is inherited.

Each of these has a switch — private permissions, private transitions, private tags — that breaks inheritance on a sub-pool. A sub-pool with private permissions starts with no inherited grants and sets its own. The switches apply from that pool downward.

A pool's name, description, contained records, and root status are local and are not inherited.

## System pools

fylr maintains its own **system pools** for objects that need a pool but do not belong to any administrator-created pool. They cannot be deleted, and the marker that identifies a pool as a system pool cannot be set or changed through the API.

## Owner and pool contact

A pool has an **owner**, set when it is created. A grant can address the owner of a pool rather than a named user.

A pool can also name a **pool contact** — a specific user designated as responsible for the pool. A grant can address the pool contact in the same way it addresses the owner; the two are independent. Changing the contact changes who such grants resolve to. A pool without a contact still works; grants that address the contact resolve to no one.

Both the owner and the pool contact let grants stay stable across personnel changes: a grant addressing "the pool contact" does not need editing when the responsible person changes.

## Records that are not pooled

Some objecttypes are not pooled: the [datamodel](the-datamodel.md), users, groups, tags, masks, transitions and system messages are instance-global. They are not placed in a pool and not shown in pool navigation.

[Nested rows](nested-and-reverse-nested.md) are a separate case: a nested row is part of its containing record and takes that record's pool. It is not placed in a pool directly.

## In the API

- A record names its pool in the `_pool` field of its content; the pool rides along as a linked object.
- Pools are managed through the [`/pool` endpoint](../api/endpoints/api-pool.md): `/pool`, `/pool/{poolID}`, and `/pool/{poolID}/stats` for record counts.
- A pool's grants are its `_acl` list, and the inheritance-breaking switch is `_private_acl` (see [Permissions](permissions.md)).

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what lives in pools.
- [Permissions](permissions.md) — how pool grants and record grants combine, and what private permissions do.
- [Tags and transitions](tags-and-transitions.md) — what else inherits down the pool tree.
- [Masks](masks.md) — the per-pool preferred mask.
- [FOR ADMINISTRATORS → Pools](../../for-administrators/permissions/pools.md) — administering pools.
