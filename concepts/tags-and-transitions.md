# Tags and transitions

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

**Tags** are flags fylr attaches to records — small, discrete labels. **Tag filters** select records by tag combinations. **Transitions** are workflow steps that observe tag changes (or that the user triggers manually) and run actions.

## Questions this page answers

- What's a tag, and how is it different from a field value or a category?
- What is the **tag tree**? Why do tags form a tree?
- What is a **tag filter**? What do `all` / `any` / `not` / `changed` mean? Which fields support `changed` (the trigger semantics)?
- What's a **transition**? What kinds exist (`manual` / `automatic` / `event`)?
- What does a transition do — what kinds of `actions` can it run?
- How do tags + transitions cooperate to form a workflow?
- What system right gates editing transitions? (`system.tagmanager`.)

## See also

- [Permissions](permissions.md) — tag filters as a permission lever.
- [Pools](pools.md) — both tags and transitions inherit down the pool tree by default.
- [FOR ADMINISTRATORS → Tags & Workflows](../for-administrators/permissions/tags-and-workflows.md) — administering them.
