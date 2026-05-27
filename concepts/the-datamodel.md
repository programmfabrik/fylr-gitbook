# The datamodel

Your fylr instance has a datamodel. It is the document that describes every objecttype you've defined — Photo, Product, Article, Person — together with their fields, their links to one another, the masks that view them, the tag groups that label them, the transitions that move them through workflows. Almost every choice an administrator makes about the shape of the data ends up recorded in the datamodel.

This page explains what the datamodel is, what makes it different from the records that conform to it, and how it changes safely while an instance is live.

## What the datamodel does and doesn't describe

The datamodel describes **shape**: which objecttypes exist, what fields each has, what type each field is, which fields are mandatory, which link to other objecttypes, how those links behave, and which masks the UI offers over each objecttype.

It does _not_ describe **content**. The records themselves — the photographs, the products, the articles — are not part of the datamodel. They _conform_ to it, and a saved record carries the version of the datamodel it was saved against, but the data itself lives separately and survives datamodel edits.

The datamodel is also not the same as fylr's configuration. Mail server settings, storage backends, plugin enablement, language settings — those live in the base configuration, not the datamodel. The two evolve independently.

## Versions: HEAD, CURRENT and the numbered past

The datamodel is **itself a versioned object**, and at any moment three labels are useful.

- **CURRENT.** The most recently committed datamodel. This is the version every live record is being saved against, the version search is indexing under, the version the UI is rendering. Most of the time, when something says "the datamodel", it means CURRENT.
- **HEAD.** The administrator's working copy — the draft they are editing right now. HEAD diverges from CURRENT as soon as the first change is made and stays divergent until the administrator commits it. HEAD is visible only to those with the right to edit the datamodel; ordinary users keep seeing CURRENT.
- **Numbered past versions** (1, 2, 3, …). Every previous commit of the datamodel is kept. They are read-only — you can look up exactly what the datamodel said in version 7, but you can't go back and edit it.

So a typical edit flow looks like this. The administrator opens HEAD, adds a new field to the Photo objecttype, renames a mask, fixes a typo in a tag label. While they work, every cataloguer in the building keeps using CURRENT. When the administrator is satisfied, they **commit** HEAD: it becomes the new CURRENT, gets a fresh numeric version, and the previous CURRENT is moved into the numbered past.

HEAD is given a future-looking version number even before it is committed — the number it would carry _if it were committed right now_. That number doesn't change while the draft is edited, but the way to tell HEAD apart from a committed version is to ask whether the version has a commit timestamp: HEAD's is empty.

## What a commit actually does

A commit isn't just a label change. When HEAD is promoted to CURRENT, fylr **applies the structural difference between the old CURRENT and the new one to the underlying database**: tables are added, columns are added or renamed, defaults are written, constraints are tightened or relaxed. Anything the old data structure no longer matches gets migrated.

This is why a commit is a deliberate act, not an autosave. Some changes are cheap (adding a new optional field on an objecttype with no rows yet). Some are expensive — turning on full-text indexing for a field across hundreds of thousands of existing records, or splitting a previously-single-parent objecttype into a polyhierarchy. The administrator running the commit sees the cost up front, and on a large instance the commit may queue a background reindex that runs after the schema change itself has landed.

Changes that touch the way records are searched (a field becoming searchable, an objecttype joining the main search index, a language being added) trigger a **reindex** of the affected records. The reindex is itself something other clients can observe — fylr writes events for index progress so the UI and any subscribers can show "rebuild in progress".

## Why HEAD and CURRENT live side by side

Keeping them separate gives the administrator a safe place to work. Without HEAD, every change to a typo in a mask label would be a live change visible to every cataloguer. With HEAD, the administrator can stage a coherent set of edits, sanity-check them, and commit them as one unit.

It also makes upgrades possible. fylr ships baseline datamodel content — for example, when a plugin contributes objecttypes, or when a customer's instance is updated to a newer release. The baseline arrives as a fresh CURRENT-or-newer; the administrator's HEAD knows which **baseline** it was forked off, so a later upgrade can tell what's a customer customisation and what was the previous ship-default. When the baseline moves underneath, the administrator can rebase their edits onto the new baseline without losing local work — the same way a developer rebases a feature branch.

## What records remember about the datamodel

A saved record records the datamodel version it was saved against. That sounds bureaucratic until you need it: when the datamodel evolves, history needs to be readable as it was at the time. A field that no longer exists on the live objecttype may still exist on a record saved against version 12, and showing that record means using the version-12 datamodel to interpret it. Numbered past versions exist for exactly this reason.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what the datamodel actually contains.
- [Masks](masks.md) — the per-mask layer on top of the datamodel.
- [Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md) — datamodel choices that change how records link to one another.
- [Search and events](search-and-events.md) — what reindex actually does, what events a commit emits.
- [FOR ADMINISTRATORS](../for-administrators/) — editing the datamodel in the UI.
- [FOR DEVELOPERS](../for-developers/api/) — reading and writing it programmatically.
