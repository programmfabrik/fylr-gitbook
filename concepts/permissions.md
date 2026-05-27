# Permissions

Almost every interaction with fylr is gated by a permission check: can this user read this record, write to this pool, upload to this collection, edit the datamodel, see this tag. The mechanism that answers all of those questions is built out of a small set of pieces, combined in a consistent way. This page introduces those pieces.

## Two layers

Permissions in fylr come in two distinct layers, and the difference matters.

**System rights** are instance-wide capabilities — things a user can do that don't attach to a particular record. "May edit the datamodel." "May manage tags." "May reset other users' passwords." "May see deleted records." Each system right is yes-or-no, granted to a user (directly, or via the groups they're in), and applies across the whole instance.

**ACL grants** are per-thing rights — things a user can do _to a specific resource_. "May read this pool." "May edit this record." "May invite users to this collection." Each grant attaches to one resource and specifies who may do what on it.

The combination is what fylr actually enforces. A user with the system right to edit the datamodel _and_ an ACL grant to edit a particular pool will be allowed in both places. A user with neither will not. Most everyday checks are ACL grants; system rights kick in mostly for administrative actions that aren't tied to one record.

## Who a grant addresses

Every grant says **who** it addresses. The "who" can take any of four forms.

- **A specific user** — a single account, identified directly.
- **A specific group** — every member of that group, on its own terms; group membership changes flow through to every grant addressing the group.
- **The owner of the resource** — a _synthetic_ principal that resolves dynamically. A grant addressing "the owner" applies to whoever happens to own the record at the moment of the check. When ownership changes, the same grant follows.
- **The pool's contact** — another synthetic principal. A grant addressing "the pool contact" applies to whoever the pool currently names as its contact person.

The synthetic principals exist so grants survive personnel changes. "The pool contact may edit anything in this pool" stays correct after the contact is reassigned; "Susan may edit anything in this pool" doesn't.

## Where grants live

An ACL grant attaches to exactly one resource, and only certain kinds of resource accept grants. The list is short:

- **Pools** — grants here decide who can read, edit, create or otherwise operate on records inside the pool.
- **Records** — grants here override the pool's grants for one specific record, where the record's objecttype is one that carries its own permissions.
- **Collections** — grants on a collection say who can read it, edit its memberships, upload into it, share it.
- **Tags** — grants on a tag say who can apply it to records, see it as an option, or remove it.
- **Users and groups** — grants on a principal say who can see them in pickers, edit their profile, change their group memberships, manage their sessions.

These are the only places ACL grants live. Other kinds of object — messages, tasks, exports, transitions — are governed by system rights, by the grants on the records they touch, or by being not-permissioned (intentionally global).

Whether an objecttype's records carry their own ACL is a property of the objecttype set in the [datamodel](the-datamodel.md). Objecttypes that carry their own ACL are called **ACL-bearing**: each record gets its own list of grants on top of the pool's. Objecttypes that don't, inherit their permissions from the pool entirely; per-record grants aren't possible.

## What a grant says

A grant is more than "user X may do action Y". Each grant carries:

- **Who** it addresses (described above).
- **Which rights** it confers — one or more named permissions chosen from the [rights catalog](#the-rights-catalog), each with its own optional configuration. A single grant can confer several rights at once, which is the common case ("the editor may read and write").
- **An optional tag filter.** Restricts the grant to records carrying or not carrying particular tags. "May read photos tagged Public, but not photos tagged Embargoed." See [Tags and transitions](tags-and-transitions.md).
- **An optional time window.** The grant only takes effect between two timestamps; outside that window it is treated as inactive without being deleted. Useful for embargoed material or interns with fixed end-dates.
- **An active flag.** A pause switch — a grant can be suspended without being removed, and re-activated later. Distinct from deleting it, because the configuration is preserved.
- **A sticky flag.** Sticky grants survive lower-privileged updates. If an editor saves a record with a new ACL that doesn't include a sticky grant the system root previously placed there, the sticky grant stays. Only a sufficiently-privileged user can clear a sticky grant.

The grant as a whole is the unit fylr stores, edits and audits. Adding or removing a grant is an explicit, logged action.

## Pool ACLs and record ACLs

For records of an ACL-bearing objecttype, the record's effective permissions are the **combination** of the pool's grants and the record's own grants. Read access on the pool gives a baseline, an additional grant on the record may add more. The two work together by default.

A record can also be marked as having a **private ACL** — a switch that says "from here, the pool's grants don't apply at all; only what's on this record counts". Private ACLs are the right tool for material that needs to be locked down regardless of the pool it lives in: a contract uploaded to a generally-open project pool that should still only be visible to legal. Used sparingly, they're useful; used everywhere, they make the permission model unmaintainable, because every change to the pool stops propagating.

The same private-ACL switch exists at the [pool](pools.md) level too. A sub-pool with a private ACL doesn't inherit from its parent pool. The two switches do the same conceptual thing — break inheritance at one step — applied at different levels.

## Right presets

In an instance with many pools, ten editors and a single permission policy, writing the same five-right grant fifty times is mistake-prone. **Right presets** are a saved bundle of rights — "the editor role", "the reviewer role", "the freelancer role" — that grants instantiate by reference.

A grant from a preset records which preset it came from. Updating the preset propagates the change to every grant that references it. Hand-crafted grants are still possible alongside presets; the two coexist, the preset reference just provides a maintainable shortcut.

## The rights catalog

The list of named rights a grant can confer is not hard-coded into a particular permission grant. It is published by the server as a **rights catalog**: an enumeration of every right fylr knows about, with each entry describing what the right does, where it applies (which kinds of resource accept it), and what parameters it takes (some rights are simply yes-or-no; some carry constraints like "no more than 5 uploads per day").

Plugins can extend the catalog. When a plugin installs a new feature, it can register its own rights, and from that point on grants may reference those rights the same way they reference fylr's own. This is how plugin-introduced capabilities become first-class citizens of the permission system instead of bolted-on toggles.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what gets permissioned. Which objecttypes are ACL-bearing.
- [Pools](pools.md) — the ACL container for live records, and the inheritance flow.
- [Tags and transitions](tags-and-transitions.md) — tag filters as a permission lever, and the right that gates editing transitions.
- [Collections and publishing](collections-and-publishing.md) — collection-specific grants and the collection-bag rights.
- [FOR ADMINISTRATORS → Permissions](../for-administrators/permissions/) — administering all of the above in the UI.
