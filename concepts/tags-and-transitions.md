# Tags and transitions

A **tag** is a label attached to a record. A **transition** is a workflow step that runs when something changes or when a user triggers it. Together they are how an instance encodes its workflow — embargoes, approvals, publication, notifications.

## Tags

A **tag** is a named flag on a record: "Embargoed", "Approved for publication", "Needs caption", "Featured". A tag is either present or absent on a record; it has no value or text of its own.

How a tag differs from related things:

- A **field value** is content. A tag is a label about the content. The article's title is a field value; "needs review" is a tag.
- A **category** from a select field is a value — one of several. A tag is present or absent and is watched by other parts of the system.
- A **search facet** is derived from a field. A tag is set explicitly by a user.

Tags are organised in **tag groups**. A tag group decides how its tags are picked: a **checkbox** group allows any number of its tags to be set at once; a **choice** group allows at most one. Whether an objecttype's records accept tags is set on the objecttype in the [datamodel](the-datamodel.md). Tags also propagate down the [pool tree](pools.md): a pool can hold tags for records in its sub-tree, and sub-pools inherit them unless set to private.

## Tag filters

A **tag filter** selects records by the tags they carry. The same structure is used by [grants](permissions.md), right presets and transitions. It has three slots:

- **All** — every tag in this slot must be present.
- **Any** — at least one tag in this slot must be present.
- **Not** — none of the tags in this slot may be present.

Empty slots impose no condition. Set slots combine with AND. "Every published, non-embargoed photo of an animal" is _all_ = [published, animal], _not_ = [embargoed]. The same structure serves a grant ("read photos tagged Public but not Embargoed") and a transition trigger.

## Transitions

A **transition** is a workflow step defined once and applied many times. It states when it runs, who may run it, what it does, and which records it applies to. The three kinds differ in how they run:

- **Manual** — shown as a button in the interface. A user with the right permissions selects one or more records and runs it. Used for human steps: submit for review, publish, send to legal.
- **Automatic** — runs on a change to the record: a save, a tag added or removed, a pool change. Used for steps that should happen without a click.
- **Event** — runs on a matching entry in the [event log](search-and-events.md). Used for steps tied to something other than a direct record save, such as an export completing.

A transition also lists the operations it watches — insert, update, delete, tag, pool change — and may apply only to certain objecttypes.

## Triggering an automatic transition by tag

On an automatic transition, a tag filter usually states which records the transition applies to. A fourth slot — **changed** — applies only to transitions and names the tags whose addition or removal triggers the transition. A transition that watches the "Approved" tag runs when that tag is added to or removed from a record. This is how tag changes drive workflow: state is held in tags, transitions watch the changes.

## What a transition does

A transition runs an ordered list of **actions** when it fires. The set is extended by plugins; the common ones:

- Set tags on the record.
- Change the owner to a user or group.
- Send an email.
- Call a configured webhook.
- Run a plugin operation.

Actions run in order. If one fails, the rest are skipped and the transition rolls back, so the record is not left in a half-changed state.

A transition can also state the tag conditions a record must meet before it runs and the conditions it should meet after, which the engine uses to check eligibility and enforce the result.

## Who may run a transition

A manual transition is gated by permissions on the record and by the transition's list of allowed users. The list can be an allow-list (only these users or groups) or a deny-list (everyone except these). Automatic and event transitions have no user running them; they run when their conditions are met.

## How tags and transitions form a workflow

1. Tags represent the states: Draft, In Review, Approved, Embargoed, Published.
2. Transitions move records between states. Approve adds the Approved tag and notifies the editor. Embargo adds Embargoed and sets a time window on the public-read grant so the embargo lifts on its own.
3. Grants and right presets use the same tags as filters, so permission follows from state: the public can read Published and not Embargoed records; freelancers can edit Draft records.

## The right that gates editing

Creating, editing and deleting tags and transitions is a system-right action, not tied to a record or pool. It is gated by the tag-manager system right. Users without it can apply existing tags and run existing transitions, subject to per-grant rules, but cannot change the set of tags and transitions. See [Permissions](permissions.md).

## See also

- [Permissions](permissions.md) — tag filters in grants, and the right that gates this set.
- [Pools](pools.md) — tags and transitions inherit down the pool tree, with a private switch to break inheritance.
- [Search and events](search-and-events.md) — what event transitions run on.
- [FOR ADMINISTRATORS → Tags & Workflows](../for-administrators/permissions/tags-and-workflows.md) — administering them.
