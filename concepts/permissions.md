# Permissions

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

The fylr permission system end-to-end: who can do what, where. Built from a small number of pieces — **users**, **groups**, **system rights**, **ACL grants** on records / pools / collections / tags — combined in a consistent way.

## Questions this page answers

- Who is "who"? Users, groups, the synthetic `_owner` and `_pool_contact` principals.
- What's a **system right**? Where does it apply? (Instance-wide.)
- What's an **ACL grant**? Where can grants live? (On records, on pools, on collections, on tags, on users, on groups — never anywhere else.)
- What does each part of an ACL grant do?
  - `who` — who the grant addresses
  - `rights` — what they can do, with which constraints
  - `tagfilter` — only applies to records carrying / not carrying tags
  - `when` — only valid in a time window
  - `sticky` — survives lower-privileged updates
  - `active` — toggle without deleting
- What's a **right preset**? Why use one?
- What's the **rights catalog** at `GET /right`? How do plugins extend it?
- How does ACL inheritance flow from pool → object? What does `_private_acl` do?
- What does it mean for an objecttype to be `acl_table: true` or `acl_table: false`?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what gets permissioned.
- [Pools](pools.md) — the ACL container for live records.
- [Tags and transitions](tags-and-transitions.md) — tag filters as a permission lever.
- [FOR ADMINISTRATORS → Permissions](../for-administrators/permissions/) — administering it in the UI.
