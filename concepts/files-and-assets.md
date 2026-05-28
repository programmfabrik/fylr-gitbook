# Files and assets

Some objecttypes carry a file. A Photo carries a photograph; an Article carries the laid-out PDF; a Music Track carries an audio file. This page describes how fylr handles the file side of a record.

## Records and files are separate

A record holds metadata: title, author, date, captions, links to other records. A file is the image, video or document that goes with it. fylr keeps the two separate. The metadata is small, edited often, and indexed for search; the file is large, read more than written, and runs through a production pipeline that takes time. A record references a file; the file is held in fylr's asset store.

Because they are separate, a record can have its file replaced — a re-scan, a corrected colour profile, a higher-resolution upload — without affecting its metadata or history.

## An upload becomes an asset

When a file is uploaded, fylr stores it, identifies it, and prepares it for use. The original file together with everything fylr derives from it is an **asset**.

An upload goes through these steps:

1. **Upload.** fylr stores the **original** — the unaltered bytes as uploaded — and records the uploader, the time, the original filename, and the file's hash.
2. **Classification.** fylr assigns the file a **class** (see below), which determines how the rest of the pipeline treats it.
3. **Production.** fylr derives a set of **versions** from the original: a thumbnail for grid views, a preview for the detail page, a larger image for zooming, a poster frame for video, and so on. The set produced is set by the instance's configuration.
4. **Metadata extraction.** For images, fylr reads dimensions, DPI, colour profile and camera model; for audio and video, duration and codec; for documents, page count.
5. **Attachment.** The asset is linked to the record, which then exposes the asset and its versions.

## Original, version, variant, rendition

- **Original** — the file as uploaded. fylr does not modify it.
- **Version** — a file derived from the original, such as a thumbnail, preview, zoom image or poster frame. An asset has several versions. Each version has a status while it is being produced.
- **Variant** — a rendering of the original prepared for download, in a particular resolution and format.
- **Rendition** — any file that is not the original. Versions and variants are both renditions.

A photograph might have one original (a 90 MB TIFF), several versions for display (a 200 px thumbnail, a 1024 px preview, a tiled zoom image), and several variants for download (full-size JPEG, web-sized JPEG, print-ready PDF).

When a record carries more than one asset, one is marked **preferred**. The preferred asset represents the record in galleries, search results and exports.

## Classes

A file's **class** is its broad category: image, video, audio, document, office, or other. The class is not the MIME type. The MIME type is specific (`image/jpeg`, `application/pdf`); the class is the category fylr treats the file as. Several MIME types map to one class — `image/jpeg`, `image/png` and `image/tiff` all map to image — and the class determines which production pipeline runs.

The class is also used in permissions: a grant can restrict uploads to specific classes ("images and audio, not documents") without listing individual MIME types.

## When the record changes

Saving a record does not move its asset. Editing the caption, adding a tag, or changing a link leaves the file untouched.

Replacing the file follows one of two paths:

- **Replace** — the asset is swapped for a new one; the old asset is no longer linked.
- **New version of the original** — the original is updated, for example with a cropped or rotated file, and the renditions are produced again.

When a record is moved to the [trash](records-and-objecttypes.md), its assets stay available, so an undelete restores the file too. When a record is purged, its assets are released for cleanup.

Cleanup is the work of the **janitor**, a background process that removes assets no record references, drains the trash on schedule, and reclaims storage. Until the janitor runs, the underlying files remain on disk.

## Stored or referenced

By default fylr copies an uploaded file into its own storage. This lets it produce renditions, apply watermarks, serve the file under its own URLs, and keep the file available if the source goes offline.

A second mode keeps the file where it already is — for example a video on a CDN or an image at another institution's image server. In this mode fylr keeps a reference rather than a copy and does not produce renditions; the record points at the external URL. fylr then cannot guarantee the file's availability or produce its own renditions of it.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what files attach to.
- [Permissions](permissions.md) — class-based and per-rendition limits on uploads and downloads.
- [Collections and publishing](collections-and-publishing.md) — how files are exposed through publishing, IIIF and WebDAV.
- [FOR ADMINISTRATORS](../for-administrators/) — configuring which versions are produced and which classes are allowed.
