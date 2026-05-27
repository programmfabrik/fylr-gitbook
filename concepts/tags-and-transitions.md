# Tags and transitions

Two of fylr's most useful primitives are simple: a **tag** is a small label you can stick on a record, and a **transition** is a workflow step that fires when something changes. On their own they're modest. Together they're the main way a fylr instance encodes "the way work actually flows here" — embargoes, approvals, publication, notifications — without committing every detail to the datamodel.

## Tags

A **tag** is a discrete, named flag attached to a record. "Embargoed". "Approved for publication". "Needs caption". "Featured on the homepage". Tags are deliberately small: a tag is on or off on a record, with no associated text, no scale, no payload. The simplicity is the point — tags compose well, they index well, and the rest of the system (permissions, transitions, search) can react to them cleanly.

How tags differ from the things they're sometimes confused with:

- **A field value** is content. A tag is a label _about_ the content. The article's _title_ is a field value; "needs review" is a tag.
- **A category** picked from a select field is also a value — exactly one of N. A tag is a yes/no decoration that several other systems are designed to watch.
- **A search facet** is a derived view over a field. A tag is something the user explicitly puts there.

Tags are administered in groups. A **tag group** collects related tags and decides how the picker behaves: a **checkbox** group lets the user apply any number of its tags at once ("topics: Sport, Health, Politics"); a **choice** group lets the user pick at most one of its tags ("approval state: Pending / Approved / Rejected"). The group is a UI grouping with semantics — checkbox vs choice — not a folder.

Whether an objecttype's records accept tags at all is a property of the objecttype in the [datamodel](the-datamodel.md). Tags also propagate down the [pool tree](pools.md): a pool can declare its own tags for records inside its sub-tree, and those flow down to sub-pools unless the sub-pool says otherwise.

## Tag filters

A **tag filter** picks records by which tags they carry. It is the same data structure used in three places — [ACL grants](permissions.md), right presets, and transitions — and it has three independent slots:

- **All.** Every tag in this slot must be present on the record. "All of these tags."
- **Any.** At least one tag in this slot must be present. "Any of these tags."
- **Not.** None of the tags in this slot may be present. "None of these tags."

Slots are empty by default. Setting more than one slot combines them with AND: a filter with both _all_ and _not_ requires every _all_ tag to be present and every _not_ tag to be absent.

So "every published, non-embargoed photo of an animal" reads, as a tag filter: _all_ = [published, animal], _not_ = [embargoed]. The same shape powers "may read photos tagged Public, but not photos tagged Embargoed" as an ACL constraint, and "fire this transition whenever a photo becomes Published" as a transition trigger.

## Transitions

A **transition** is a workflow step the datamodel declares once and the engine applies many times. Each transition says: when it fires, who may fire it, what it does, and which records it concerns. The three kinds differ in how they fire:

- **Manual transitions** show up as a button in the front-end. A user with the right permissions picks the record (or a batch of records) and clicks. Used for human-driven steps: "submit for review", "publish", "send to legal".
- **Automatic transitions** fire on changes to the record — when it's saved, when a tag is added or removed, when the pool changes. Used for steps that should happen without anyone having to click: "when 'Approved' is set, copy this record into the Press collection".
- **Event transitions** fire on a matching entry in the event log — see [search and events](search-and-events.md). Used for steps that hang off something other than a direct record save: "when an export completes, send a notification".

Each transition also lists the **operations** it watches (insert, update, delete, tag, pool change) and may restrict itself to one or more **objecttypes**.

## How tag filters trigger automatic transitions

A tag filter on an automatic transition normally describes _which records the transition concerns_. There is a fourth slot — **changed** — that means something different and only applies to transitions: the tags whose addition _or removal_ should _trigger_ this transition.

"Changed" turns the tag filter from a static predicate into a trigger condition. A transition with `changed = [Approved]` and `before: any = [Approved]` fires whenever the Approved tag changes — added or removed — on a record that currently has it (or just lost it). This is how fylr models tag-driven workflow: state lives in tags, transitions watch tag deltas.

## What a transition does

Each transition carries an ordered list of **actions** that run when it fires. Actions are the building blocks of automation; the catalogue is open-ended and extended by plugins, but the most-used ones are:

- **Set or remove tags** on the target record (often the next state in the workflow).
- **Change the owner** to a specific user or group, or to a synthetic principal.
- **Move the record to a different pool.**
- **Send an email** — to the owner, the pool contact, a fixed address, or a tag-defined list.
- **Invoke a webhook** — call out to an external system with a configured payload.
- **Run a plugin operation** — execute whatever the plugin exposes.

Actions run in order. If one fails, the rest are skipped and the transition rolls back so the record isn't left half-transitioned.

A transition can also describe **before** and **after** tag-filter conditions: the state the record must be in to be eligible, and the state it should end up in. The engine uses these to enforce the post-condition and to keep the workflow honest.

## Who may invoke a transition

Manual transitions are gated by both system rights and ACL: the user has to be allowed to operate on the record, and they have to be in the transition's allowed-users list. The list can be expressed positively ("only these users / groups can run this transition") or as a deny-list ("everyone except these users").

Automatic and event transitions don't have a clicker. They are gated only by their match conditions: when the conditions are met, fylr runs them as the system.

## How tags and transitions cooperate

The two pieces compose into a workflow like this:

1. The data team defines tags that represent the states: _Draft_, _In Review_, _Approved_, _Embargoed_, _Published_.
2. They define transitions that move records between those states. _Approve_ adds the Approved tag and notifies the editor. _Embargo_ adds Embargoed and sets a `when` window on the public-read grant so the embargo lifts automatically.
3. ACL grants and right presets use the same tags as their tag filters, so permission propagates from state: the public can read records with Published _and not_ Embargoed; freelancers can edit records with Draft.

That's the entire workflow apparatus: states are tags, steps are transitions, permissions are grants with tag filters. Each piece is replaceable and the three speak the same vocabulary.

## The right that gates editing

Managing tags and transitions — creating new ones, editing existing ones, deleting them — is a system-rights operation: it isn't tied to a particular record or pool. The system right that authorises it is `system.tagmanager`. Users without it can _apply_ existing tags and _invoke_ existing transitions (subject to per-grant rules), but not change the catalogue. See [Permissions](permissions.md).

## See also

- [Permissions](permissions.md) — tag filters as a permission lever, and the system right that gates this catalogue.
- [Pools](pools.md) — both tags and transitions inherit down the pool tree, with a private switch to break inheritance.
- [Search and events](search-and-events.md) — what event transitions hang off.
- [FOR ADMINISTRATORS → Tags & Workflows](../for-administrators/permissions/tags-and-workflows.md) — administering them in the UI.
