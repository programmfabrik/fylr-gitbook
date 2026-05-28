# Masks

A **mask** is a view of one objecttype. It selects a subset of the objecttype's fields, decides how each is shown, and has a name. An objecttype usually has several masks for different tasks: a full editing form for a cataloguer, a short form for a reviewer, a summary for a search result.

## What a mask controls

For each field it includes, a mask decides:

- **Whether the field is shown.** A field not listed by the mask is not shown when that mask is in use.
- **Whether it is editable or read-only.** A field can be editable in one mask and read-only in another.
- **Whether it is required.** A mask can require a field on top of what the objecttype requires.
- **Its default value.** A quick-entry mask can pre-fill a field so the user types less.
- **How a linked record is shown.** When the field links to another record, the mask sets which sub-mask renders that record (see below).

A mask can also set how a record's own system information is shown — which system fields appear, their labels and defaults. This is separate from the field list because it concerns information fylr maintains rather than fields the objecttype defines.

A mask does not change the record. The data is the same whichever mask views it; the mask sets what is shown and what can be edited through that view.

## Standard mask, preferred mask, all-fields view

- **Standard mask.** Each objecttype has one mask set as its standard mask in the datamodel. fylr uses it when nothing has overridden the choice.
- **Preferred mask.** A [pool](pools.md) can override the standard mask for an objecttype: within that pool, records of the objecttype use the preferred mask instead of the objecttype's standard mask.
- **All-fields view.** A built-in view that returns every field of the objecttype with no filtering. It is restricted to the system administrator, since it bypasses the field selection that masks apply.

The choice is usually automatic: the interface uses the pool's preferred mask, or the standard mask if there is none.

## Sub-masks

When a field links to another record, that record has to be shown somehow. A **sub-mask** is a mask used inside another mask's field to render the linked record — for example a Photo mask showing the photographer's name and portrait inline where it links to the Photographer. A sub-mask is an ordinary mask, with its own field list and rules, chosen by the parent field rather than by a pool or screen. Sub-masks can contain sub-masks; fylr stops at one level of nesting when rendering.

Some mask features apply only at the top level. The system-field settings are top-level only; a sub-mask renders part of another record and does not redefine that record's system information.

## Masks versus permissions for hiding a field

A field can be hidden from a view in two ways, used for different reasons.

- **To leave a field off a screen,** use a mask. A reviewer mask that omits a field omits it for that screen only; the same user, through another mask, would see it.
- **To prevent a user from seeing a field anywhere,** use [field-level permissions](permissions.md). A field hidden by a mask is still readable through another mask; a field restricted by permissions is not.

The test: if a user with a different mask may see the field, a mask is enough. If not, use permissions.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what a mask is a view of.
- [The datamodel](the-datamodel.md) — where masks are declared.
- [Pools](pools.md) — the per-pool preferred mask.
- [Permissions](permissions.md) — for hiding a field as a restriction rather than as decluttering.
