# Records and objecttypes

A **record** is a single stored thing in fylr — one photograph, one product, one article, one person. An **objecttype** is the definition that all records of one kind follow: which fields they have, what type each field is, which are required, which link to other objecttypes. "Photo", "Product", "Article", "Person" are objecttypes; the individual photographs and products are records.

The relationship is the same as between a table and its rows. The objecttype is the definition; a record is one entry that follows it. An objecttype can exist with no records yet.

## What a record carries

Every record carries a set of system information regardless of its objecttype: a set of identifiers, a version, an owner, a creation timestamp, and the fields defined by its objecttype.

### Identifiers

A record has four identifiers, each unique at a different scope.

- **Object ID** — unique within the objecttype. The first Photo created is Object ID 1; the first Product created is also Object ID 1. The objecttype together with the Object ID identifies a record.
- **System Object ID** — unique within the instance. No two records of any objecttype share a System Object ID. References from elsewhere in fylr — collection memberships, tag references, permission grants, the event log — use the System Object ID.
- **UUID** — assigned once when the record is created. It is preserved across database renames and re-imports, so it identifies a record when records move between systems.
- **Global Object ID** — the System Object ID qualified with the database it originated in. It identifies a record when more than one fylr instance is involved. (The interface also labels this Global-System-ID.)

The Object ID and System Object ID are settable while a record is new (version 1) and become fixed once the record has been saved.

### Version

A record has a **version**, starting at 1 when it is created and incrementing by 1 on each save. A save must supply the version it started from. If the record has already moved to a higher version — because another user saved it in the meantime — the save is rejected rather than applied on top of the newer data.

A museum cataloguer who creates the photograph _Strandkorb, Sylt, 1928_ as the first record in a new instance gets Object ID 1, System Object ID 1, a new UUID, and version 1. After three rounds of caption edits the record is at version 4; its identifiers are unchanged.

### Owner and creation

A record records its **owner** — the user or group set as owner when it was created — and the timestamp of its creation. The owner can be referenced by permission grants (see [Permissions](permissions.md)).

## What an objecttype can do

An objecttype is one of the kinds of record defined in the [datamodel](the-datamodel.md): Photo, Product, Article. These are defined per instance to match the data being stored.

Beyond listing the fields a record has, an objecttype sets how its records behave. Each of these is described on its own page:

- Its records can live in a [pool](pools.md), or be instance-global.
- Its records can carry their own [permissions](permissions.md), or inherit them from the pool.
- Its records can accept [tags](tags-and-transitions.md).
- It can form a tree, or a [polyhierarchy](hierarchies-and-polyhierarchies.md).
- It can be a [nested table](nested-and-reverse-nested.md), whose records exist only inside records of another objecttype.

Around the records sit the structures fylr provides to organize them. [Pools](pools.md) and [collections](collections-and-publishing.md) gather records into buckets — a pool is the container a record lives in; a collection is a curated set that can draw records from anywhere. Tags label records, and users and groups own and access them. These structures come with fylr; the objecttypes are the part defined per instance.

## Versions, history and the trash

A record is stored copy-on-write: each save writes a new version of the record while the previous version is kept. The newest version is returned by default. The earlier versions are the record's **history** and are read by requesting a specific version.

Deletion is a soft delete. A deleted record is moved to the **trash**: it is no longer returned by normal reads, no longer found by search, and no longer counted in pool sizes. From the trash a record can be **undeleted**, which returns it to active use with its identifiers and history intact, or **purged**, which removes it. After a purge the record can be recovered only from a backup.

## In the API

Records are exchanged through the [`/db` endpoint](../api/endpoints/api-db.md) as JSON. The system information sits at the top level of the object; the content fields sit in a nested object named after the objecttype:

- `_objecttype` names the objecttype, `_mask` the [mask](masks.md) the data is shaped by; both are part of every exchange.
- Inside the content object: the Object ID is `_id`, the version is `_version`. At the top level: the System Object ID is `_system_object_id`, the UUID is `_uuid`, the Global Object ID is `_global_object_id` (`<system object id>@<database uuid>`).
- The owner is `_owner`, the creation timestamp `_created`.
- A single record is read at `/db/{objecttype}/{mask}/{objectId}`. A save POSTs the object back to `/db/{objecttype}` carrying the `_version` it was read at; if the record has moved on, the save is rejected as a version conflict.

## See also

- [Files and assets](files-and-assets.md) — files attach to records but are not records themselves.
- [The datamodel](the-datamodel.md) — the definition that holds every objecttype.
- [Masks](masks.md) — views over the fields of an objecttype.
- [Pools](pools.md) — the container most data records live in.
- [Permissions](permissions.md) — how the owner and permission grants apply to records.
- [FOR ADMINISTRATORS → Object Types](../../for-administrators/permissions/object-types.md) — administering objecttypes.
