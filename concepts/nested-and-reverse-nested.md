# Nested and reverse-nested tables

Most objecttypes describe things that exist on their own. A Photo exists. A Person exists. You can look one up by ID, change its permissions, give it to someone, find it in search. The page on [records and objecttypes](records-and-objecttypes.md) is about that kind of objecttype.

Some kinds of data don't make sense on their own. The line items on an invoice only mean anything attached to that invoice. The mailing addresses of a contact aren't independent things that have their own permissions — they belong to the contact. fylr offers a special kind of objecttype for exactly this case: the **nested table**.

## What a nested table is

A **nested table** is an objecttype whose records have no independent existence. They live as a list of rows _inside_ a top-level record on a different objecttype. The Invoice is the top-level objecttype; the Invoice Line is a nested table under Invoice. Reading the invoice gives you its lines, embedded in the invoice itself. Saving the invoice saves the lines along with it.

Because nested rows are part of their containing record, they don't get the apparatus that stand-alone records do:

- **They can't be addressed directly.** You don't look up "line 7" on its own; you look up its invoice and read the line out of it.
- **They have no permissions of their own.** Whoever can read the invoice can read its lines; whoever can edit the invoice can edit its lines. There is no separate ACL on a line.
- **They have no owner.** The invoice has an owner; the lines just belong to the invoice.
- **They don't go into the trash separately.** Deleting a line removes it from the invoice on save. Deleting the invoice takes the lines with it.

Used correctly, a nested table makes data structurally honest: it lets the modeller say "these aren't separate things, they're parts of one thing", and have the system enforce that.

## When to nest, and when to link instead

The choice between nesting a sub-thing and linking to it is one of the most consequential the modeller makes about an objecttype.

- **Nest** when the sub-thing is _part of_ the parent. The lines on an invoice. The contact methods on a person. The price tiers on a product. The choices on a multiple-choice question. None of these have meaning except as part of their parent, and none of them are referenced from anywhere else.
- **Link** when the sub-thing is a _separately existing record_ that the parent points at. The photographer of a photo (also the photographer of many other photos). The exhibition a photo appears in. The product category. These are shared entities; they have their own existence, their own permissions, their own history, and many records can refer to the same one.

Two cheap tells: if more than one parent might want to point at the same sub-thing, you want a link, not a nest. If you would ever want to permission the sub-thing differently from the parent, you want a link, not a nest.

## Reverse-nested: the view from a nested row

When the modeller declares a nested table, the relationship has two natural sides.

From the **parent's side**, the parent objecttype carries the list of nested rows as a field. Reading an Invoice gives you the lines under it; saving an Invoice saves them.

From the **nested row's side**, fylr also offers the reverse: a **reverse-nested** view exposes, from the perspective of a nested row, the parent record it belongs to. The reverse-nested view is what lets the UI render a nested row in isolation — say, in a search result — while still being able to navigate "up" to its containing record.

The two are descriptions of the same relationship, not two separate things being maintained side by side: fylr derives the reverse-nested view automatically from the nested declaration.

## Why the descriptor is called "owned_by"

The relationship is configured in the datamodel under a descriptor called **`owned_by`**, which sounds like it ought to be about who has access to the row. It isn't: it's about which top-level objecttype the nested rows live inside. The name is historical.

fylr is a Go rewrite of easydb 5 and keeps its API contract. In easydb 5, nested tables were implemented as real database tables with a foreign key pointing at the "owning" top-level table — hence the name. fylr stores the nested rows inside the parent record's JSON instead, but the descriptor name (and the slot in the datamodel that holds it) stayed. The word _owned_ in `owned_by` refers to that owning-table relationship, not to the record's owner.

The constraint that follows from this is worth knowing: a nested table can't declare a link _back_ from one of its columns to a top-level record (a "reverse link"). The datamodel validator rejects that combination. If you find yourself wanting one, the data probably wants to be a top-level objecttype with a regular link instead.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what nested rows are nested under.
- [Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md) — a different kind of nesting (record-in-record, not row-in-record).
- [The datamodel](the-datamodel.md) — where the nested-table descriptor lives.
- [Permissions](permissions.md) — why nested rows inherit their parent's ACL rather than carrying their own.
