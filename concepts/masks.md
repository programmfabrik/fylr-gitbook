# Masks

A record's objecttype lists every field a record of that kind _can_ carry. That's rarely the same as the fields you want a particular user to _see_ on a particular screen. A cataloguer entering metadata wants the full editing form. A junior reviewer only needs the caption and the rights notice. The summary card in a search result wants the title, the thumbnail and nothing else.

fylr offers all three of those views through **masks**. A mask is a named view onto a single objecttype that picks a subset of its fields, decides how each one renders, and gets used wherever fylr has to show or accept records of that kind.

## What a mask actually controls

A mask is a list of decisions about how its objecttype's data is presented. For each field the mask includes, it can say:

- **Whether the field shows up at all.** A field on the objecttype that isn't mentioned by the mask simply isn't shown when the mask is in use.
- **Whether it's editable or read-only.** The same field can be editable in the cataloguer's mask and read-only in the reviewer's.
- **Whether the user must fill it in.** Some masks add their own required-fields rule on top of what the objecttype requires.
- **What its default value is.** A "quick-create" mask might pre-fill the licence to "internal" so a user only has to type the title.
- **How a linked record gets rendered inside the form.** When the field is a link to another record, the mask says which sub-mask to use to display that record — see [sub-masks](#sub-masks) below.

A mask can also override what fylr shows about a record's own metadata — which system properties appear in the header strip, what they're labelled, what their default value is for a new record. That layer is the mask's _system fields_; it's separate from the regular field list because it concerns properties fylr maintains, not properties the objecttype owns.

The mask doesn't change what the record _is_. The underlying data is the same regardless of which mask was used to view it; the mask only chooses what the user sees and is allowed to touch through that screen.

## Standard mask, preferred mask, and `_all_fields`

Three terms come up so often it's worth defining them once.

- **Standard mask.** Each objecttype has one mask designated as its standard mask in the datamodel. When fylr has to pick a mask for an objecttype and nothing has overridden it, this is the one it picks. Think of it as the objecttype's default form.
- **Preferred mask.** A [pool](pools.md) can override the standard mask choice for any objecttype the pool contains: "in this pool, use this other mask for Photos rather than the objecttype's default". The pool's preferred mask wins over the objecttype's standard mask within that pool's sub-tree.
- **`_all_fields`.** Not a mask defined in the datamodel, but a built-in pseudo-mask that returns the objecttype's complete field set with no filtering — useful when a tool needs to read every column without being affected by per-mask omissions. Access is restricted: only the system root sees `_all_fields`, since it deliberately bypasses any per-mask restrictions.

Picking one of these is normally automatic. The reader doesn't have to choose — the UI picks the preferred mask for the pool they're in, or the standard mask if none. Naming the choice matters mostly when a developer is building a new screen and has to be explicit about which mask their request uses.

## Sub-masks

When a field on a mask links to another record, the linked record has to be rendered somehow. The simplest rendering is just a name and a link icon. A richer one shows several of the linked record's own fields right inside the parent form: a Photo mask that, where it links to the Photographer, shows the photographer's name, biography snippet and portrait thumbnail without making the user click through.

That richer rendering is a **sub-mask**: a mask used inside another mask's field. The sub-mask is itself just a mask — it has its own field list, its own per-field rules — but instead of being chosen by a pool or by a UI screen, it's chosen by the parent field. Sub-masks can themselves contain sub-masks; fylr stops at one level of nesting when rendering, so the screen doesn't grow endlessly.

A handful of mask features only apply at the top level. System-field overrides (the metadata header strip) are top-level only; sub-masks don't redefine the record's metadata, they're rendering a piece of someone else's record.

## Masks vs ACLs: hiding a field

There are two reasons you might want a field to disappear from a user's view, and they need different tools.

- **The field doesn't belong on this screen.** Use a mask. The "reviewer" mask leaves the photographer's birthday out, not for security, but because reviewers don't need to see it on their screen. Switching the same user to a mask that includes the field — through another screen, through the API — would happily show it.
- **The user mustn't see this field, anywhere.** Use [field-level permissions](permissions.md). A licence-sensitive field that should be invisible to junior staff regardless of which screen they happen to be looking through belongs in an ACL, not in a mask omission.

The clean test: would it be acceptable for a power user with a different mask to see the field? If yes, the mask is the right tool. If no, the ACL is.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what a mask is a view of.
- [The datamodel](the-datamodel.md) — where masks are declared.
- [Pools](pools.md) — where the per-pool preferred-mask choice lives.
- [Permissions](permissions.md) — the right tool when you mean to enforce, not to declutter.
