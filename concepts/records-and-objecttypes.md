# Records and objecttypes

Two words do more work in fylr than any others: **record** and **objecttype**. Almost every other concept on this site — masks, pools, permissions, files, collections — is ultimately a way of choosing _which records_ you mean, or _what shape_ they have, or _who can do what_ with them. Read this page first, then come back to it whenever a later page mentions one of these words and you want to be sure what it refers to.

## A record is a single stored thing

A **record** is one entry in your fylr instance: one photograph, one product, one article, one person. If you imagine your data as a long set of filing cabinets, a record is one card in one drawer.

Every record carries a small bundle of system information no matter what kind it is: a few identifiers, a version number, a creator, a creation timestamp, and whatever fields its objecttype defines.

### How a record is identified

Records carry four different identifiers — each one answers a different question.

- **`_id`** is the record's number _within its objecttype_. The first Photo you ever store is `_id 1`; the first Product you ever store is also `_id 1`. The two are different records — the objecttype name plus the `_id` is what makes the pair unique.
- **`_system_object_id`** is the record's number _within the whole instance_. Across every kind of record, no two share a `_system_object_id`. Tag references, collection memberships, permission grants and the event log all use the `_system_object_id` to point at a record.
- **`_uuid`** is a UUID assigned once when the record is created. It survives database renames and re-imports, which makes it the right identifier to keep on file when records flow between systems.
- **`_global_object_id`** is the `_system_object_id` qualified with the database it came from (written `<_system_object_id>@<database uuid>`). It is what's used when the same record might be referenced from a second fylr instance.

Which one to use:

- Talking about one specific kind of record (Photos, Products) — `_id`.
- Linking from elsewhere inside the same instance (collections, tags, permission grants, the event log) — `_system_object_id`.
- Identifying the same record across two instances or after an import — `_uuid` or `_global_object_id`.

### How a record changes over time

A record carries a **version number** that starts at 1 the moment it is created and goes up by one on every edit. When you save a change, you send back the version you started from; if someone else has already moved past it, fylr rejects your save. That is how two cataloguers can work on the same instance without silently overwriting each other.

If a museum cataloguer creates the photograph _"Strandkorb, Sylt, 1928"_ as the first Photo in a fresh instance, fylr issues `_id 1`, `_system_object_id 1` (it is also the first record of any kind), a fresh `_uuid`, and version 1. After three rounds of caption edits the record is at version 4; its identifiers have not moved.

## An objecttype is the shape every record of one kind must take

An **objecttype** is the schema for a kind of record: which fields exist, what types they have, which are required, which link to other objecttypes. "Photo", "Product", "Article", "Person", "Exhibition" are all objecttypes a real instance might define.

A record and its objecttype are not the same thing in the same way a row and a table are not the same thing. The objecttype is the description; the record is the instance. You can have a Photo objecttype with no Photo records yet, in the same way you can have an empty filing cabinet with the labels already printed.

Objecttypes are defined in the [datamodel](the-datamodel.md). Several choices the datamodel offers about an objecttype carry across this whole site and are worth meeting now:

- An objecttype may live **inside a pool** (most user-content objecttypes do) or be **instance-global** (a handful of administrative ones are). See [Pools](pools.md).
- An objecttype may carry **its own permissions** per record, or inherit them from the pool it lives in. See [Permissions](permissions.md).
- An objecttype may **accept tags**, or not. See [Tags and transitions](tags-and-transitions.md).
- An objecttype may form a **tree** (each record has at most one parent) or a **polyhierarchy** (each record can have any number of parents). See [Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md).
- An objecttype may be **a nested table** — records of this type don't stand on their own, they ship embedded inside records of another objecttype. See [Nested and reverse-nested tables](nested-and-reverse-nested.md).

Each later page picks up one of these threads.

## Objecttype vs basetype

The two words sound similar and do related work, but they sit on opposite sides of a clear line.

- **Objecttypes** are the kinds of record _you_ design. Photo, Product, Article, Person, Exhibition — they encode the shape of your own data.
- **Basetypes** are the object families _fylr_ provides out of the box to organise that data. You don't define basetypes; fylr ships them.

The basetypes you'll meet across this section:

- **Pool** — a container for records. See [Pools](pools.md).
- **Collection** — a curated bundle of references to records. See [Collections and publishing](collections-and-publishing.md).
- **Tag** and **taggroup** — labels users attach to records, and the groups admins organise tags into. See [Tags and transitions](tags-and-transitions.md).
- **Term** — an indexed value that drives autocomplete and inspection lookups; distinct from tags.
- **User** and **group** — accounts and groupings of accounts.

Plus a handful that live mostly behind the scenes — events, messages, exports, right presets, tasks — surfaced where they matter (the event log, system messages) but not usually the thing a reader is looking up.

So the **datamodel is the part you design**, and the basetypes are the scaffolding fylr already provides for organising, permissioning, tagging and discovering the records your datamodel produces.

## Versions, history and the trash

A record's lifetime is more than a single row. fylr stores records **copy-on-write**: every save writes a fresh version of the record alongside the previous one. The newest version is what fylr returns by default; the older ones make up the record's **history** and can be read back by asking for a specific version explicitly.

**Deletion is a soft delete.** A deleted record is moved into the **trash**: no longer searchable, no longer returned by normal reads, no longer counted in pool sizes — but recoverable. From the trash a record can be:

- **undeleted**, returning it to active use with its identifiers and history intact, or
- **purged**, removing it for good. After a purge, only a backup can bring it back.

When other pages talk about "the current version" of a record they mean the newest copy-on-write row; "version 7" means an older row; "restoring" means lifting a record out of the trash back into active use.

## See also

- [Files and assets](files-and-assets.md) — files attach to records but aren't records themselves.
- [The datamodel](the-datamodel.md) — the document that holds every objecttype definition.
- [Masks](masks.md) — different views over the same objecttype.
- [Pools](pools.md) — the basetype most user-content records live inside.
- [Permissions](permissions.md) — what owners, ACLs and system rights actually grant.
- [FOR ADMINISTRATORS → Object Types](../for-administrators/permissions/object-types.md) — administering objecttypes in the UI.
