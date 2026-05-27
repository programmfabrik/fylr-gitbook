# Concepts

This section explains what fylr is built out of. The same words show up everywhere — in the user interface, in the admin screens, in plugin manifests, in the API documentation — so it pays to read these pages once before diving into the role-specific guides.

The pages are ordered. Each one only uses words that earlier pages introduced.

## Status

**This section is a working draft.** Each linked page below is currently a stub that captures the questions it needs to answer; the prose is being filled in incrementally on the `docs-concepts` branch. Pages still marked _stub_ have no real content yet.

## Read in this order

1. **[Records and objecttypes](records-and-objecttypes.md)** — start here. What is a record? What is an objecttype? How do they relate?
2. **[Files and assets](files-and-assets.md)** — files versus records; originals, versions, variants, renditions.
3. **[The datamodel](the-datamodel.md)** — the schema for all your objecttypes. Versions, HEAD vs CURRENT, how changes are committed.
4. **[Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md)** — when objecttypes form trees; single-parent vs DAG.
5. **[Nested and reverse-nested tables](nested-and-reverse-nested.md)** — rows that live inside another record instead of standing on their own.
6. **[Pools](pools.md)** — the primary container for live objects. Pool trees, what inherits down.
7. **[Masks](masks.md)** — different views of the same objecttype. Mask hierarchy. The "preferred" mask.
8. **[Permissions](permissions.md)** — who can do what, where. System rights, ACL grants, right presets.
9. **[Tags and transitions](tags-and-transitions.md)** — tags, tag filters, workflow transitions.
10. **[Collections and publishing](collections-and-publishing.md)** — collections, presentations, share links, deep links.
11. **[Search and events](search-and-events.md)** — how search differs from `/db`; the event log; change history.

## Writing style for these pages

These are the rules the section commits to. If you spot a page breaking one of them, file an issue (or, better, fix it):

- **Plain English.** No code, no Go internals, no HTTP method names where a sentence will do.
- **One concrete example per concept**, drawn from a real-world use case (museums cataloguing photos, retailers cataloguing products, an archive of articles).
- **No internal file paths.** Don't link to or mention `internal/api/...`; readers can't reach them and they're noise in a public document.
- **Cross-link liberally.** The first time another concept appears on a page, link to its concept page.
- **Each page ends with a "See also"** block pointing at neighbouring concepts and at the relevant role-specific deep-dive (administrators / developers / system administrators) where one exists.
- **`fylr` is the easydb 6 product line** — a Go rewrite that keeps the easydb 5 API contract. Mention easydb 5 only when explaining historical naming (`owned_by`, `_id_parent`, …); the present tense is fylr.

## See also

- **[Glossary](../help/glossary.md)** — one-line definitions of every term used here.
- **[FOR USERS](../for-users/getting-started.md)** — how to do things, once you know the vocabulary.
- **[FOR ADMINISTRATORS](../for-administrators/permissions/)** — administering the concepts described here.
- **[FOR DEVELOPERS](../for-developers/api/)** — the API reference that uses this vocabulary.
