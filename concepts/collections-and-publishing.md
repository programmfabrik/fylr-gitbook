# Collections and publishing

Two threads come together on this page: a way for users to **gather** records they care about (collections), and a way to **expose** those records to the outside world (publishing). The two are separate features and you can use either without the other, but they meet often enough — a curator picks 30 photos into a collection and then publishes them as a press kit — that they belong on one page.

## Collections

A **collection** is a user-curated grouping of records. The closest analogy is a folder: a named container the user puts things into. The mechanics are different from a [pool](pools.md) in three important ways.

- **Records can sit in many collections at once.** A photograph already lives in exactly one pool, but it can also belong to the "Best of 2025" collection, to the "Press kit, March" collection, and to a colleague's "candidates for review" collection. Collections don't move records; they just gather references to them.
- **A collection can mix objecttypes freely.** A press kit collection might contain photographs, the press release Article, and a Person record for the spokesperson. The pool of each of those records doesn't change.
- **Collections are made by users.** Where pools are an administrative structure laid out once and changed rarely, collections are a workspace feature — anyone with permission to create them can.

Collections form a tree of their own (each user has their own top-level collection at the root of the user's sub-tree; sub-collections sit underneath), but the tree is mostly a UI convenience, not the structural backbone that the pool tree is.

A collection has its own permissions: who can see it, who can edit it, who can add or remove members. Granting access to a collection lets recipients see the records the collection contains, even if they wouldn't otherwise have direct access to those records — sharing a collection is one of the main ways material moves between people inside the instance.

## System collections

Every instance has a few collections it doesn't let you delete. The **root collection** at the top of the tree exists so the tree has a root; every user gets a personal top-level collection underneath the root the first time they log in, which is also a system collection — it's where their own sub-collections hang.

System collections behave like ordinary collections for read and use, but they can't be removed. The flag marking a collection as a system collection isn't user-editable.

## Pin-protected collections

A collection can be **pin-protected**: a four-digit (or longer) code the recipient has to enter once before fylr will let them see the contents. The pin is set by the owner when sharing; recipients enter it once and fylr remembers that they've passed it for that collection.

The pin is not a substitute for permissions. It is a **second factor** for sharing, on top of the ACL: even a recipient with permission to read the collection has to enter the pin before the contents render. The intended use case is sharing with people whose account already exists but who need an extra friction step for sensitive material — a contract collection, a yet-unreleased catalogue.

## Presentations

A **presentation** is a collection used as a slideshow rather than a list. The records inside the collection become the slides; an ordering and per-slide annotations live alongside the collection's contents. The collection itself isn't a different basetype — it is still a collection — it just carries presentation data on the side, and the UI knows to render it as a slideshow when that data is present.

This is why "what's the difference between a collection and a presentation" is usually a question about UI affordance, not data shape: a presentation is a collection with slide settings attached, and converting one into the other is a matter of adding (or removing) those settings.

## Publishing

Where collections gather records for users _inside_ the instance, **publishing** exposes records to viewers _outside_ it.

A **publication** is a single recorded act of exposing some material: this record (or this collection's records) is being made available at this public URL by this pipeline.

The shape of a publication:

- **The source.** Which record (and, by extension, which collection if the record _is_ a collection) is being published.
- **The collector** — the pipeline that produces the publication. `pdf_creator` produces a PDF; `gallery` produces a public gallery web page; other collectors can be added by plugins.
- **The public URL** the collector emits. This is what an external viewer types into their browser.
- **The deep-link URL back into fylr** — for users with an account, the same publication carries a link that opens the source record in the editor.

Publications are recorded objects (basetype `publish`); they can be listed, audited, and revoked. Revoking a publication unsets its public URL — external viewers who have the URL get a not-found from then on.

A handful of common collectors ship with fylr (PDF, gallery, share-link). Plugins add their own, and a publication carries its collector's name so the UI can offer the right management interface for it.

## Deep links

A **deep link** is a public URL that exposes a single record's data directly — typically an XML representation, accessible without an account. Set up on a record (or via a publication), it lets external systems pull the record's metadata over HTTP the same way they'd pull from any other web resource.

Deep links don't carry their own per-link permissions: once a deep link exists, anyone with the URL can read what it returns. The control point is whether the deep link is published in the first place. If an instance needs per-recipient access, an authenticated API call or a pin-protected collection is the right tool — not a deep link.

## WebDAV access

A collection can be **exposed as a WebDAV folder**: a network drive an operating system can mount, with the collection's records (and especially their files) appearing as files inside that drive.

Two kinds of WebDAV access are available per collection:

- **Read-and-write WebDAV** turns the collection into a mountable folder. Files can be copied out, copied in, edited, renamed; fylr keeps the underlying records in sync.
- **Hotfolder WebDAV** is write-only — files dropped into the folder create new records in the collection, but the folder doesn't expose existing contents back to the user. Used as an upload drop zone for batch workflows.

WebDAV is gated by the collection's ACL: only users with the right permissions on the collection are allowed to mount it. The URL fylr exposes per collection is per-user; sharing the URL doesn't share the access.

## IIIF

For image assets, fylr also speaks **IIIF** — the International Image Interoperability Framework. IIIF is a public standard for image servers used widely by museums, libraries and archives; consuming clients include Mirador, Universal Viewer, and most institutional viewer software.

When fylr serves an image over IIIF, the URL is recognisable to any IIIF viewer and the image becomes pannable, zoomable and croppable inside that viewer without further configuration. The IIIF URL on an image asset is what you'd hand to a partner institution running their own viewer.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what collections collect, what publications expose.
- [Files and assets](files-and-assets.md) — where IIIF and WebDAV ultimately serve from.
- [Permissions](permissions.md) — collection ACLs and the collection-bag rights.
- [FOR USERS → Collections & Presentations](../for-users/quick-access/collections-and-presentations.md) — the user-facing guide to working with collections.
