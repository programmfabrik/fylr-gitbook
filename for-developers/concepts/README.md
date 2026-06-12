# Concepts

This section explains what fylr is built out of. The same words show up everywhere — in the user interface, in the admin screens, in plugin manifests, in the API documentation — so it pays to read these pages once before working with the [API](../api/README.md).

The pages are ordered. Each one only uses words that earlier pages introduced. The prose stays at vocabulary level; each page ends with an **In the API** block that maps its terms to what requests and responses actually say.

## Coming from a classical DAM

In most DAM systems the **asset** is the central object: a file, with metadata attached to it. fylr inverts this. The central object is the [record](records-and-objecttypes.md) — a structured set of fields — and files hang off the record in fields of type file. A record can carry no file at all (a person, a location, an exhibition), one file, or many. What a classical DAM calls an asset corresponds in fylr to a record with a file field; the metadata is not a description attached to "the file" but a record in its own right, which references its files.

Because the metadata lives on the record, several files share one set of it: the front and back of a postcard are two files in one record — where a classical DAM holds two assets with duplicated metadata. See [Files and assets](files-and-assets.md) for the two forms this takes (variants in one file field, nested rows per file).

Rough equivalences, each explained on its page:

| Classical DAM | fylr |
| --- | --- |
| Asset (file + metadata) | [Record](records-and-objecttypes.md) with a file field |
| Related assets with duplicated metadata (front/back, detail shots) | One record holding several files ([variants or nested rows](files-and-assets.md)) |
| Asset type, metadata schema | [Objecttype](records-and-objecttypes.md) in the [datamodel](the-datamodel.md) |
| Derivatives, proxies, previews | [Renditions](files-and-assets.md) of an original |
| Workspace, archive | [Pool](pools.md) tree — the permission container a record lives in |
| Folder tree, category tree, taxonomy | [Hierarchical objecttype](hierarchies-and-polyhierarchies.md) the record links to |
| Lightbox, basket, share set | [Collection](collections-and-publishing.md) |
| Metadata form, view | [Mask](masks.md) |
| Keywords, labels, flags | [Tags](tags-and-transitions.md) |

One term is a known trap: in fylr, a **version** is a record's metadata version, not a file derivative. The derived files are renditions — see [Files and assets](files-and-assets.md).

## Read in this order

1. **[Records and objecttypes](records-and-objecttypes.md)** — start here. What is a record? What is an objecttype? How do they relate?
2. **[Files and assets](files-and-assets.md)** — files versus records; a file field holds variants; originals and renditions.
3. **[The datamodel](the-datamodel.md)** — the schema for all your objecttypes. Versions, HEAD vs CURRENT, how changes are committed.
4. **[Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md)** — when objecttypes form trees; single-parent vs multiple-parent.
5. **[Nested and reverse-nested tables](nested-and-reverse-nested.md)** — rows that live inside another record instead of standing on their own.
6. **[Pools](pools.md)** — the primary container for live objects. Pool trees, what inherits down.
7. **[Masks](masks.md)** — different views of the same objecttype. Mask hierarchy. The "preferred" mask.
8. **[Permissions](permissions.md)** — who can do what, where. System rights, ACL grants, right presets.
9. **[Tags and transitions](tags-and-transitions.md)** — tags, tag filters, workflow transitions.
10. **[Collections and publishing](collections-and-publishing.md)** — collections, presentations, share links, deep links.
11. **[Search and events](search-and-events.md)** — how search differs from direct lookup; the event log; change history.

After these pages, the [API reference](../api/README.md) is the natural next step.

## How these pages are written

- **Plain English, vocabulary level.** The prose explains the concepts; field names and endpoint paths are confined to the **In the API** block ending each page.
- **One concrete example per concept**, drawn from a real-world use case (museums cataloguing photos, retailers cataloguing products, an archive of articles).
- **fylr is the easydb 6 product line** — a Go rewrite that keeps the easydb 5 API contract. easydb 5 comes up only when it explains historical naming.

## See also

- **[API reference](../api/README.md)** — the endpoints these pages give you the vocabulary for.
- **[Glossary](../../help/glossary.md)** — one-line definitions of every term used here.
- **[FOR ADMINISTRATORS](../../for-administrators/permissions/)** — administering the concepts described here.
- **[FOR USERS](../../for-users/getting-started.md)** — the interface guide.
