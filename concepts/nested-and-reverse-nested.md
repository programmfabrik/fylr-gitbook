# Nested and reverse-nested tables

Most objecttypes describe things that exist on their own: a Photo, a Person. Such a record can be looked up by ID, permissioned, and found in search.

Some data only exists as part of something else. The line items of an invoice mean nothing apart from that invoice; the contact methods of a person belong to that person. For this, fylr provides the **nested table**.

## Nested tables

A **nested table** is an objecttype whose records exist only inside a record of another objecttype, as a list of rows. The Invoice is the top-level objecttype; the Invoice Line is a nested table under Invoice. Reading the invoice returns its lines; saving the invoice saves the lines.

Because nested rows are part of their containing record, they lack what stand-alone records have:

- They are not addressed directly. A line is reached through its invoice, not on its own.
- They have no permissions of their own. Whoever can read the invoice can read its lines; whoever can edit the invoice can edit its lines.
- They have no owner. The invoice has an owner; the lines belong to the invoice.
- They are not trashed separately. Removing a line removes it from the invoice on save; deleting the invoice removes its lines.

## Nesting versus linking

The choice between nesting a sub-thing and linking to it:

- **Nest** when the sub-thing is part of the parent: the lines of an invoice, the contact methods of a person, the price tiers of a product. These have no meaning apart from their parent and are not referenced elsewhere.
- **Link** when the sub-thing is a separate record the parent points at: the photographer of a photo, the exhibition a photo appears in, a product category. These have their own existence, permissions and history, and several records can reference the same one.

Two indicators: if more than one parent might point at the same sub-thing, use a link. If the sub-thing should be permissioned differently from the parent, use a link.

## Reverse-nested: the view from a nested row

A nested relationship has two sides. From the parent's side, the parent objecttype holds the list of nested rows as a field. From the nested row's side, the **reverse-nested** view exposes the parent record a row belongs to. This lets a nested row be shown on its own — for example in a search result — while still linking up to its containing record. fylr derives the reverse-nested view from the nested declaration.

## The "owned_by" name

The relationship is configured in the datamodel under a setting called `owned_by`. The name refers to which top-level objecttype the nested rows live in, not to who has access to them. It is historical: in easydb 5, nested tables were separate database tables with a foreign key to the owning table. fylr keeps the nested rows inside the parent record instead, but the setting kept its name.

One constraint follows: a nested table cannot hold a link back to a top-level record (a reverse link); the datamodel rejects it. Data that needs such a link is better modelled as a top-level objecttype with an ordinary link.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what nested rows are nested under.
- [Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md) — records nested under records, a different kind of nesting.
- [The datamodel](the-datamodel.md) — where nested tables are declared.
- [Permissions](permissions.md) — why nested rows inherit their parent's permissions.
