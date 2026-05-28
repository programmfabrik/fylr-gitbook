# Masks

A **mask** is a view of one objecttype. It selects a subset of the objecttype's fields, decides how each one is shown and whether it can be edited, and has a name. An objecttype usually has several masks for different tasks: a full editing form for a cataloguer, a short form for a reviewer, a summary for a search result.

## All data goes through a mask

Every read and every write of a record names a mask. There is no direct, mask-less access to record data — data comes in and goes out through a mask, always. The mask selects which fields are present in the data and whether each one is read-only or editable.

This makes the mask the point where field-level access is decided. The fields a user can read and write are exactly the fields of the mask they use. A user restricted to a mask that omits a field cannot read or write that field, because no request reaches the data except through a mask. There is no separate per-field permission at the data level; the mask is that control. (An objecttype can also carry per-field display settings, but those affect only the frontend, not what the data interface returns or accepts.)

## What a mask controls

For each field it includes, a mask decides:

- **Whether the field is present.** A field not listed by the mask is not read or written through it.
- **Whether it is editable or read-only.** A field can be editable in one mask and read-only in another.
- **Whether it is required.** A mask can require a field on top of what the objecttype requires.
- **Its default value.** A quick-entry mask can pre-fill a field so the user enters less.

A mask can also set how a record's system information is presented — which system fields appear, their labels and defaults.

A mask does not change the record. The stored data is the same whichever mask is used; the mask sets which fields are exchanged and whether they can be edited.

## Standard mask, preferred mask, all-fields view

- **Standard mask.** Each objecttype has one mask set as its standard mask in the datamodel. fylr uses it when nothing has overridden the choice.
- **Preferred mask.** A [pool](pools.md) can override the standard mask for an objecttype: within that pool, records of the objecttype use the preferred mask instead.
- **All-fields view.** A built-in view returning every field of the objecttype with no filtering. It is restricted to the system administrator, since it bypasses the field selection masks apply.

The choice is usually automatic: the interface uses the pool's preferred mask, or the standard mask if there is none.

## Sub-masks

A mask field that holds a [nested or reverse-nested table](nested-and-reverse-nested.md) is itself rendered by a mask — a **sub-mask**, which is simply a mask used at a deeper level to select and present the fields of those sub-rows. It is an ordinary mask; nothing about it is special beyond sitting one level down.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what a mask is a view of.
- [The datamodel](the-datamodel.md) — where masks are declared.
- [Pools](pools.md) — the per-pool preferred mask.
- [Permissions](permissions.md) — which masks a user may use; masks are how field access is controlled.
