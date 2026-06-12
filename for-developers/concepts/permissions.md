# Permissions

fylr checks a permission on almost every action: reading a record, writing to a pool, uploading to a collection, editing the datamodel, seeing a tag. The system is built from a small number of pieces.

## Two layers

**System rights** are instance-wide capabilities not tied to a particular record: editing the datamodel, managing tags, managing user accounts, seeing deleted records. Each is granted to a user, directly or through a group, and applies across the instance.

**Permission grants** apply to a specific resource: reading a pool, editing a record, inviting users to a collection. Each grant is attached to one resource and states who may do what on it.

fylr enforces the combination. Most everyday checks are grants; system rights apply to administrative actions not tied to one record.

## Who a grant addresses

A grant addresses one of four kinds of principal.

- **A user** — a single account.
- **A group** — every member of the group; membership changes flow through to grants addressing the group.
- **The owner of the resource** — resolved when the check runs, to whoever owns the record at that moment. If ownership changes, the grant follows.
- **The pool contact** — resolved to whoever the pool currently names as its contact.

The owner and pool contact let a grant stay correct across personnel changes, where a grant naming a specific user would not.

## Where grants live

A grant attaches to one resource, and only certain resources accept them:

- **Pools** — who can read, edit, create or otherwise act on records in the pool.
- **Records** — grants on a single record, where its objecttype carries its own permissions; these sit on top of the pool's grants.
- **Collections** — who can read a collection, change its memberships, upload into it, share it.
- **Tags** — who can apply a tag, see it as an option, or remove it.
- **Users and groups** — who can see them in pickers, edit their profile, change group memberships, manage their sessions.

Other objects — messages, tasks, exports, transitions — are governed by system rights or by the grants on the records they touch.

Whether an objecttype's records carry their own grants is set on the objecttype in the [datamodel](the-datamodel.md). Records of such an objecttype get their own list of grants in addition to the pool's. Records of an objecttype without this take their permissions from the pool.

## What a grant contains

A grant carries:

- **The principal** it addresses.
- **The rights** it confers — one or more named permissions from the rights catalogue, each with its own settings. One grant can confer several rights.
- **A tag filter** (optional) — limits the grant to records carrying or not carrying particular tags, for example "may read photos tagged Public but not photos tagged Embargoed". See [Tags and transitions](tags-and-transitions.md).
- **A time window** (optional) — the grant applies only between two times; outside the window it is inactive but not deleted.
- **An active flag** — suspends or resumes the grant without deleting it, preserving its settings.
- **A sticky flag** — a sticky grant is kept through a save by a lower-privileged user that omits it. Only a sufficiently privileged user can remove a sticky grant.

## Pool grants and record grants

For a record whose objecttype carries its own grants, the effective permissions are the combination of the pool's grants and the record's own. A read grant on the pool is a baseline; a grant on the record can add to it.

A record can be set to **private permissions**, which means the pool's grants no longer apply to it and only the record's own grants count. This suits material that must be restricted regardless of the pool it sits in — a contract in an otherwise open project pool. The same setting exists on a [pool](pools.md): a sub-pool with private permissions does not inherit from its parent. In both cases the setting breaks inheritance at one step.

## Right presets

A **right preset** is a saved set of rights — an editor role, a reviewer role, a freelancer role — that a grant can be created from. A grant created from a preset records which preset it came from, and updating the preset updates the grants that reference it. Hand-made grants remain possible alongside presets.

## The rights catalogue

The set of rights a grant can confer is published by the server as a **rights catalogue**: every right fylr knows about, with what it does, where it applies, and what settings it takes. Some rights are yes/no; some carry constraints, such as an upload limit per day.

Plugins extend the catalogue. A plugin can register its own rights, after which grants can confer them like any other right.

## In the API

- Grants ride on the resource they protect, as its `_acl` list — on a pool, a record, a collection.
- The rights catalogue is served by the [`/right` endpoint](../api/endpoints/api-right.md); right presets live under `/right/{context}/presets`.
- A tag filter is an object with `all`, `any` and `not` arrays of tag IDs (see [Tags and transitions](tags-and-transitions.md)).

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what gets permissioned.
- [Pools](pools.md) — the permission container for records, and the inheritance flow.
- [Tags and transitions](tags-and-transitions.md) — tag filters in grants, and the right that gates editing transitions.
- [Collections and publishing](collections-and-publishing.md) — collection grants.
- [FOR ADMINISTRATORS → Permissions](../../for-administrators/permissions/) — administering permissions in the interface.
