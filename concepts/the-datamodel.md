# The datamodel

The **datamodel** is the definition of every objecttype in an instance — Photo, Product, Article, Person — together with their fields, their links to one another, their masks, their tag groups and their transitions. Changes to the shape of the data are recorded in the datamodel.

## Shape, not content

The datamodel describes shape: which objecttypes exist, what fields each has, the type of each field, which fields are required, which link to other objecttypes, and which masks are offered over each objecttype.

It does not hold content. The records — the photographs, products and articles — are not part of the datamodel. They follow it. A saved record records the datamodel version it was saved against, but the record data is stored separately and is not affected by datamodel edits.

The datamodel is also distinct from the instance's configuration. Mail settings, storage backends, plugin enablement and language settings are part of the base configuration, not the datamodel.

## Versions: HEAD, CURRENT and numbered versions

The datamodel is versioned. Three labels describe its states.

- **CURRENT** — the most recently committed datamodel. Records are saved against it, search indexes under it, and the interface renders it. References to "the datamodel" usually mean CURRENT.
- **HEAD** — the working copy being edited. HEAD diverges from CURRENT as soon as a change is made, and stays divergent until it is committed. HEAD is visible only to those who can edit the datamodel; other users continue to see CURRENT.
- **Numbered versions** (1, 2, 3, …) — every previous commit. They are read-only.

A typical edit: an administrator opens HEAD, adds a field to the Photo objecttype, renames a mask, corrects a tag label. While they work, other users continue on CURRENT. When the edits are complete, the administrator **commits** HEAD. It becomes the new CURRENT and receives a new number; the previous CURRENT becomes a numbered version.

HEAD carries the version number it would receive if committed now. The number does not change while HEAD is edited. HEAD is distinguished from a committed version by having no commit timestamp.

## What a commit does

A commit applies the difference between the old CURRENT and the new one to the underlying database: tables and columns are added or renamed, defaults are written, constraints are changed, and data that no longer matches the new structure is migrated.

Almost any change to the datamodel also calls for the search index to be rebuilt for the affected records — adding, renaming or removing a field or objecttype, changing a field's type, changing the pool, turning hierarchy or polyhierarchy on or off, and so on. On commit, fylr works out whether the changes need a reindex, and, rather than running one silently, presents it as a task the administrator confirms before the commit completes. Changes that tighten or relax constraints prompt a separate confirmation in the same way.

A reindex rebuilds the index for the affected records, so its cost scales with how many records there are. On a new or lightly populated datamodel it does almost nothing: turning an objecttype's hierarchy or polyhierarchy on or off, for instance, is flagged for reindex like any other change but reindexes nothing when there are no records yet. On a large instance the reindex can take a while and runs in the background; fylr writes events for its progress, so the interface and any subscribers can show that a rebuild is underway.

## Why HEAD and CURRENT are separate

Without HEAD, every edit would be live the moment it was made. HEAD lets an administrator stage a set of edits and commit them together.

It also supports upgrades. fylr ships baseline datamodel content — for example when a plugin contributes objecttypes, or when an instance is updated to a new release. HEAD records which baseline it was forked from, so an upgrade can tell which parts are customer customisations and which were the previous defaults. When the baseline changes, the administrator can move their edits onto the new baseline without losing them.

## What records record

A saved record records the datamodel version it was saved against. When the datamodel changes, history still needs to be readable as it was at the time: a field removed from the live objecttype may still exist on a record saved against an earlier version, and reading that record correctly uses the datamodel from that version. The numbered versions exist for this.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what the datamodel defines.
- [Masks](masks.md) — the per-mask layer over the datamodel.
- [Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md) — datamodel choices about how records link.
- [Search and events](search-and-events.md) — what a reindex does and what events a commit emits.
- [FOR ADMINISTRATORS](../for-administrators/) — editing the datamodel in the interface.
