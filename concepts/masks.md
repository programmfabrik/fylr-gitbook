# Masks

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

A **mask** is a view onto an objecttype. It chooses a subset of the objecttype's fields, decides how each one renders (read-only, editable, embedded sub-mask), and gives the result a name. The same objecttype usually has several masks for different audiences and tasks.

## Questions this page answers

- Why aren't records just edited through their objecttype directly? What does a mask add?
- What's the difference between the **standard mask**, a **preferred mask** and `_all_fields`?
- What's a **sub-mask** (mask inside a mask), and when do you use one?
- What are **system fields** on a mask? How do they differ from data fields?
- How does the **mask hierarchy** work — what does one mask inherit from another?
- When do you use a mask to **hide** a field, and when do you use the field's own ACL?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what a mask is a view of.
- [The datamodel](the-datamodel.md) — where masks are declared.
- [Permissions](permissions.md) — masks vs ACLs as ways to control visibility.
