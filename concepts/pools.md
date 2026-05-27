# Pools

Most records in a fylr instance live inside a **pool**. The pool is fylr's primary container — like a folder, but with the kind of administrative behaviour that ordinary folders don't have. Pools carry permissions, decide which workflow transitions are available, hold their own tags, and pick which mask is preferred for each objecttype. Sub-pools inherit those choices from their parent unless an administrator explicitly says otherwise.

This page explains what it means for a record to "belong to" a pool, how the pool tree works, and what is inherited down it.

## What a pool actually is

A pool is a record in its own right (basetype `pool`). It has a name, a description, an owner, optional sub-pools, and a configuration that other things check whenever a record in the pool is read, edited or moved.

Why a pool, and not just a label? Because a pool is the **unit administrators reason about**. A museum has one pool per department; a publisher has one per imprint; an agency has one per client. Granting "the editorial team can edit this client's photos" is one grant on the client's pool; without pools, it would be one grant on every photo. Pools collapse that fan-out to a single place.

Most user-content objecttypes are configured as **pooled** — every record of those objecttypes is required to sit in some pool. A handful of administrative objecttypes are instance-global instead and have no pool. (Whether an objecttype is pooled is a choice the datamodel makes about that objecttype.)

## The pool tree

Pools form a tree. There is a root pool at the top (or a small number of root pools), every other pool has exactly one parent, and the depth of the tree is whatever the administrator decides it should be. The tree is shown in the UI as a folder-like navigation; under the hood, every pool knows its parent and fylr can walk from any pool back up to the root.

This is not the same tree as a [hierarchical objecttype](hierarchies-and-polyhierarchies.md) builds. The objecttype hierarchy is about how records of _one kind_ relate (a Department under a Department). The pool tree is about how _containers_ relate, and pooled records of any kind live in them. A photo of a department head can sit in a pool while the department itself sits in an objecttype hierarchy elsewhere; the two trees are independent.

## What flows down a sub-pool from its parent

A pool isn't only a container — it carries policy. By default, several pieces of that policy are inherited from the parent pool down to its sub-pools. The administrator gets to decide which.

The inheritable pieces:

- **Access control.** Permission grants attached to a pool apply to every record inside that pool and, by default, to every record inside every sub-pool. Granting an editor read access on the "Publishing" pool gives them read access throughout the Publishing sub-tree.
- **Transitions.** [Workflow transitions](tags-and-transitions.md) configured on a pool are offered to records in that pool, and by default to records in its sub-pools.
- **Tags.** A pool can carry tag definitions of its own — tags that exist for records inside this pool's sub-tree but not elsewhere. Sub-pools inherit them by default.
- **Default masks per objecttype.** Each pool can prefer a particular [mask](masks.md) for records of a given objecttype. The preference is inherited.

Each of these has a corresponding switch — _private access control, private transitions, private tags_ — that the administrator can flip on a sub-pool to **break inheritance**. A sub-pool with private access control starts with an empty ACL: it gets to specify its own permissions from scratch, none of the parent's grants come through. The same goes for transitions and tags. The switches are deliberate, blunt instruments: each one says "from here down, the parent's <thing> doesn't apply".

Some pieces are **not** inherited. The pool's own name and description are local. The list of records the pool _contains_ is local. Whether a pool is the root is local. These belong to the pool itself, not to a policy that should propagate.

## The system pool

Every fylr instance has a special pool — the **system pool** — that fylr ships and uses for objects that need a pool but don't sit in any of the administrator's pools. It can't be deleted, and the flag that marks a pool as the system pool can't be moved to a different pool: there is one and only one.

In day-to-day use you won't think about the system pool. When you do encounter it, treat it as a fixed point: every instance has it, you can put records in it, but it's there for fylr to rely on.

## Owners and pool contacts

A pool has an **owner**, like any record. The owner is set when the pool is created, and ACL grants can address "whoever owns this pool" rather than naming a specific user — useful when departments change personnel.

A pool can also nominate a **pool contact** — a specific user fylr knows to be the responsible party for things in this pool. ACL grants can address the pool contact in the same way they address the owner; the two are independent principals. A pool contact change immediately changes who any "address the pool contact" grant resolves to. Pools without a configured contact still work; grants that reference the contact simply have no one to resolve to.

The point of these synthetic principals is to keep grants stable through personnel changes. Granting "the pool contact may edit anything in this pool" is one ACL grant once; updating the actual person fylr considers the contact is a separate, lightweight change that doesn't touch the grant.

## Which records don't live in pools

A handful of objecttypes are deliberately not pooled. The [datamodel itself](the-datamodel.md), users, groups, tags, masks, transitions, system messages — these are instance-global. They aren't placed in a pool, their permissions aren't inherited from any pool, and they don't appear in pool-based navigation. The pages on those concepts explain where their administration lives.

[Nested rows](nested-and-reverse-nested.md) are a separate case again: nested rows are part of their containing record and inherit _its_ pool by inheriting the parent itself. They aren't put into pools directly.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what lives in pools.
- [Permissions](permissions.md) — how pool ACLs interact with object ACLs, what "private ACL" actually does.
- [Tags and transitions](tags-and-transitions.md) — what else inherits down the pool tree.
- [Masks](masks.md) — the per-pool preferred-mask choice.
- [FOR ADMINISTRATORS → Pools](../for-administrators/permissions/pools.md) — administering pools.
