# Collections and publishing

This page covers two features: gathering records into sets (collections), and exposing records to the outside (publishing). They are separate and can be used independently, but are often used together — a set of photos gathered into a collection and then published as a press kit.

## Collections

A **collection** is a user-curated set of records. It is like a folder, with three differences from a [pool](pools.md):

- A record can be in many collections at once. A photograph lives in one pool but can also be in "Best of 2025", in "Press kit, March", and in a colleague's review set. A collection gathers references to records; it does not move them.
- A collection can mix objecttypes. A press kit can hold photographs, the press-release Article, and a Person record for the spokesperson.
- Collections are made by users, where pools are an administrative structure. Anyone with permission to create collections can.

Collections form a tree, with each user's collections under their own top-level collection. The tree is an organising convenience rather than the structural backbone the pool tree is.

A collection has its own permissions: who can see it, edit it, and change its memberships. Granting access to a collection lets recipients see the records it contains, even records they would not otherwise have direct access to. Sharing a collection is a common way material moves between people in an instance.

## System collections

Some collections cannot be deleted. The **root collection** is the top of the tree. Each user gets a personal top-level collection beneath the root on first login, which holds their own collections; it too cannot be deleted. System collections are used like ordinary collections but cannot be removed.

## Pin-protected collections

A collection can be **pin-protected**: a code the recipient enters once before its contents are shown. The pin is a second step on top of permissions, not a replacement for them — a recipient with permission to read the collection still enters the pin first. It is used when sharing sensitive material with people who already have an account.

## Presentations

A **presentation** is a collection shown as a slideshow rather than a list. The records in the collection are the slides; an order and per-slide annotations are held alongside the collection. A presentation is still a collection — it carries presentation settings, and the interface shows it as a slideshow when those settings are present. Adding or removing those settings converts between the two.

## Publishing

Where collections gather records inside the instance, **publishing** exposes records outside it.

A **publication** is a single act of exposing material: a record, or a collection's records, made available at a public URL by a particular pipeline. A publication holds:

- **The source** — which record or collection is published.
- **The collector** — the pipeline that produces the publication. One produces a PDF, another a public gallery page; plugins add more.
- **The public URL** the collector produces, which an external viewer opens.
- **A link back into fylr** — for users with an account, the same publication links to the source record in the editor.

Publications are recorded and can be listed, audited and revoked. Revoking a publication removes its public URL; viewers who have the URL then get a not-found.

## Deep links

A **deep link** is a public URL that returns a single record's data directly, usually as XML, without an account. It lets an external system read a record's metadata over HTTP. A deep link has no per-link permissions: anyone with the URL can read what it returns, so the control is whether the deep link is published at all. For per-recipient access, an authenticated request or a pin-protected collection is used instead.

## WebDAV access

A collection can be exposed as a **WebDAV folder** — a network drive an operating system can mount, with the collection's records and files appearing as files. Two kinds are available per collection:

- **Read-and-write** — the collection is a mountable folder; files can be copied out, copied in, edited and renamed, and fylr keeps the records in sync.
- **Hotfolder** — write-only; files dropped in create new records in the collection, but existing contents are not exposed back. Used as an upload drop zone.

WebDAV is gated by the collection's permissions, and the URL is per user; sharing the URL does not share access.

## IIIF

For image files, fylr serves **IIIF** — the International Image Interoperability Framework, a standard used by museums, libraries and archives and supported by viewers such as Mirador and Universal Viewer. An image served over IIIF can be panned, zoomed and cropped in any IIIF viewer. The IIIF URL of an image is what is handed to a partner institution running its own viewer.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what collections gather and publications expose.
- [Files and assets](files-and-assets.md) — what IIIF and WebDAV ultimately serve.
- [Permissions](permissions.md) — collection permissions and sharing.
- [FOR USERS → Collections & Presentations](../for-users/quick-access/collections-and-presentations.md) — the user guide.
