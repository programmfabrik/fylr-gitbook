# Nested and reverse-nested tables

Picture an objecttype as a spreadsheet: each record is a row, each field is a column. Sometimes a single cell needs to hold a table of its own — a list of rows with their own columns. fylr offers two ways to do this, **nested** and **reverse-nested**. They look alike in the interface — a table inside a record — but differ in where the rows live and whether they exist on their own.

## Nested

A **nested** table is a sub-spreadsheet living inside a record, with its own columns and rows. Its rows have no identity of their own: no Object ID, no version. They are created, updated and deleted together with the record that contains them, and cannot be addressed or searched on their own — only as part of that record.

An invoice with its line items, a person with their contact methods: the lines and the contact methods are nested rows. They belong to the one record and have no meaning apart from it.

In easydb 5, nested rows were held in a separate database table. fylr keeps them inside the containing record's data instead.

A nested table can itself contain nested tables, to any depth.

## Reverse-nested

A **reverse-nested** table also appears as a table inside a record, but its rows are records of a separate objecttype.

That separate objecttype has a forward link to the containing objecttype, and in the datamodel that link is marked as **reverse**. The containing objecttype then shows, as a reverse-nested table, all the records that link to it.

Because the rows are records of their own objecttype, they have their own Object ID and version and can be addressed, searched and edited independently — unlike nested rows.

The reverse marking makes the containing record the **master**: it manages the lifecycle of the records that link to it. Deleting the containing record deletes the records that reverse-link to it, even though those records live in another objecttype and can otherwise be used on their own.

A museum **object** and its **resources** is a real example of this. A resource is a record of its own objecttype — a photograph or scan of the object, carrying its own description, viewpoint, reproduction type, licence, rights-holder and credit line — that links back to the object. Each resource can be searched and edited on its own, but deleting the object deletes its resources.

Reverse-nested tables can also be nested.

## Reverse-hierarchical

A related form applies within a [hierarchy](hierarchies-and-polyhierarchies.md). A **reverse-hierarchical** field shows, on a parent record, its children — the records that link back to it through the parent reference. The parent owns its children, and the structure can repeat to any depth.

The ownership pattern is the same one reverse-nested uses: a record owns the records of another objecttype that link to it with a reverse marking. Reverse-hierarchical is that pattern applied to the parent-child links of a hierarchy.

## Nested, reverse-nested, or a plain link

Three ways one record can hold or reach another:

- **Nested** — the rows are part of this record. No independent identity, no separate lifecycle, not addressable on their own. Use it for parts of the record: invoice lines, contact methods, price tiers.
- **Reverse-nested** — the rows are records of another objecttype that link back to this one, and this record owns their lifecycle. Independently usable, but deleted with their master. Use it when the related records are real objects in their own right but should not outlive the record they belong to.
- **Plain link** — a forward reference to an independent record with no ownership. The linked record lives on its own and is unaffected when the linking record is deleted. Use it for shared references: the photographer of a photo, a product's category.

## In the API

In record JSON ([`/db`](../api/endpoints/api-db.md)), the three forms look different:

- **Nested rows** are arrays under keys of the form `_nested:{objecttype}__{field}` inside the record's content, sent and saved together with the record.
- **Reverse-nested records** appear under keys of the form `_reverse_nested:{objecttype}:{link field}`, each entry a record of the other objecttype with its own envelope.
- **A plain link** is a field whose value is the linked record, carried with its own `_objecttype` and `_mask`.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — the rows and columns these tables are built from.
- [Hierarchies and polyhierarchies](hierarchies-and-polyhierarchies.md) — parent-child links between records, which reverse-hierarchical fields display.
- [The datamodel](the-datamodel.md) — where nested and reverse links are declared.
- [Permissions](permissions.md) — nested rows take their containing record's permissions; reverse-nested records carry their own.
