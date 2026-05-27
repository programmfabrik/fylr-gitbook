# Files and assets

**Status: stub.** Part of the [Concepts](README.md) section.

## What this page covers

The relationship between **records** (which carry your data) and **files** (the photos, PDFs, audio you upload). Why fylr stores both originals and a family of derived files. The vocabulary the asset pipeline uses.

## Questions this page answers

- Why are files separate from records? What's the lifecycle of an upload?
- **Original** vs **version** vs **variant** vs **rendition** — what each one means and when fylr produces it.
- Where do thumbnails come from? Who controls which versions get generated?
- What happens to file versions when the record's version increments? When the record is deleted?
- What is an **EAS class**? How is it different from a MIME type?
- How does fylr decide whether to copy an uploaded file into its own storage or leave it where it was hosted?

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what files attach to.
- [Permissions](permissions.md) — the per-class / per-version upload limits in ACL grants.
- [FOR ADMINISTRATORS → File Worker](../for-administrators/) — configuring which versions get produced.
