# Files and assets

Some kinds of record stand alone — a Person, a Department, an Event. Others need to carry a file: a Photo carries a photograph, an Article carries the PDF that was laid out and printed, a Music Track carries the audio file. The vocabulary fylr uses for the file side of a record is the subject of this page.

## Records and files are kept apart on purpose

A **record** is a row of metadata: title, author, date, captions, tags, the link to the photographer, the link to the exhibition. A **file** is the megabytes of pixels, video frames or PDF pages that go with it.

Keeping the two apart matters because their lifecycles differ. The metadata is small, edited often, and indexed for search; the file is large, mostly read, and gets pushed through a production pipeline that can take seconds or minutes. Separating them lets fylr index, cache, and permission them on different paths and lets the same record swap its file (a re-scan, a corrected colour profile, a higher-resolution upload) without losing its history.

The mental model: a record _references_ a file. The file lives in fylr's asset store; the record carries a pointer to it.

## An upload becomes an asset

When a file is uploaded, fylr accepts it, gives it an internal identifier, and starts a pipeline that prepares it for use. That whole bundle — the **original** file plus everything fylr derives from it — is an **asset**.

The lifecycle of an upload looks like this:

1. **Upload.** The file arrives. fylr stores the **original** — the unaltered bytes the user uploaded — and records who uploaded it, when, the filename it arrived with, and the file's hash.
2. **Classification.** fylr decides what kind of file it is and assigns it an **EAS class** (see below). The class drives the rest of the pipeline.
3. **Production.** fylr produces a family of **versions** from the original — a small thumbnail for grid views, a medium-sized preview for the detail page, a large image for zoom-and-pan, an audio waveform, a poster frame for video. Which versions get produced is decided by the instance's configuration.
4. **Metadata extraction.** For images, fylr reads dimensions, DPI, colour profile, camera model. For audio and video, duration and codec. For office documents, page count.
5. **Attachment.** The asset is now linked to the record. The record's API responses and UI views include a pointer to the asset and to each of its produced versions.

A museum cataloguer uploading the photograph _"Strandkorb, Sylt, 1928"_ to its Photo record triggers exactly this sequence: the TIFF is stored as the original, classified as an image, and the thumbnail and preview versions are queued for production. By the time the cataloguer next looks at the record, the previews are ready and the file appears in the gallery.

## Original, version, variant, rendition

These four words name closely related things and are easy to mix up.

- **Original.** The unaltered file as it was uploaded. fylr never edits the original.
- **Version.** A separately produced file derived from the original — typically a thumbnail, a preview, a zoom-image, a poster frame. A single asset has many versions. Each carries a status (still being produced, ready, failed) while the pipeline runs.
- **Variant.** A different rendering of the original prepared for download — different resolutions and formats. Variants are what gets handed out when a user clicks "download".
- **Rendition.** The umbrella term: any file that isn't the original. Versions and variants are both renditions.

A photograph might therefore have one original (a 90 MB TIFF), a handful of versions for fylr's own UI (a 200 px thumbnail, a 1024 px preview, a tile pyramid for zoom), and several variants for download (full-size JPEG, web-sized JPEG, print-ready PDF).

When a record carries more than one asset, one of them is marked **preferred**. The preferred asset is the one the record is represented by in galleries, search hits and exports — the one shown when something has to pick "the" file for the record.

## EAS classes

The **EAS class** is fylr's coarse category for a file: `image`, `video`, `audio`, `document`, `office`, `other`. It is _not_ the MIME type — the MIME type tells you the file is `image/jpeg` or `application/pdf`; the class tells you fylr should treat it as an image or as a document. Several MIME types map onto the same class (`image/jpeg`, `image/png`, `image/tiff` all map to `image`), and the class is what decides which production pipeline runs and which renditions get produced.

The class also gates permissions. A permission grant can restrict uploads to one or more classes — "may upload images and audio, but not documents" — without having to enumerate every MIME type.

## What happens when the record changes

A record can be saved many times without the asset moving. Editing the caption, adding a tag, changing the photographer link — none of those touch the file.

Replacing the file is itself an edit, and follows one of two paths the cataloguer chooses:

- **Replace.** The asset on the record is swapped for a new one. The old asset is no longer linked.
- **New version of the asset.** The original is updated — the cropped, rotated or colour-corrected file becomes the new original — and the renditions are produced afresh.

When a record is **deleted** (soft-deleted into the trash), its assets are kept available alongside it: if the record is undeleted, the file is still there. When a record is **purged** from the trash, its assets are released for cleanup.

The cleanup itself is the job of fylr's **janitor**, a background process that removes assets no record references any more, drains the trash on schedule, and reclaims storage. Until the janitor runs, the underlying files are still on disk — useful for forensic recovery, but it means storage doesn't shrink the instant a record is purged.

## Stored, or only referenced

For most uploads fylr copies the file into its own storage so it can produce renditions, watermark them, serve them under its own URLs, and survive the source going offline. That is the default.

A second mode exists for files that should stay where they already live — a hosted video on a CDN, a public-domain image at a museum's IIIF endpoint. In this "leave the file in place" mode fylr keeps a pointer rather than a copy and skips rendition production: the record references the external URL directly. The trade-off is that fylr can no longer guarantee the file's availability or produce its own thumbnails for it.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what files attach to.
- [Permissions](permissions.md) — class-based and per-rendition restrictions on uploads and downloads.
- [Collections and publishing](collections-and-publishing.md) — how files are exposed via publish artifacts, IIIF and WebDAV.
- [FOR ADMINISTRATORS](../for-administrators/) — configuring which versions are produced and which classes are allowed.
