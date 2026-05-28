# Files and assets

Many objecttypes carry files: a Photo carries a photograph, an Article carries the laid-out PDF, a Music Track carries an audio file. In fylr a file is a data type, like text or a number — a field of that type holds files, and an objecttype can have as many file fields as it needs.

## Records and files are separate

A record holds metadata: title, author, date, captions, links to other records. A file is the image, video or document itself. fylr keeps the two separate. The metadata is small, edited often, and indexed for search; the file is large, read more than written, and runs through a production pipeline that takes time. A record references its files; the files are held in fylr's file store.

Because they are separate, a record can have a file replaced — a re-scan, a corrected colour profile, a higher-resolution upload — without affecting its metadata or history.

## A file field holds a list of files

A file field's value is not a single file but a **list** of files. One field can hold several at once — the front and back of a postcard, multiple scans of one page. Exactly one file in the list is the **preferred** file, and fylr uses the preferred file wherever it needs a single image to stand for the record: the thumbnail in a result grid, the preview on the detail page, an avatar. When a field holds one file, that file is the preferred one.

The file field itself holds only the files. It carries no description of each file beyond the file's own technical data. Descriptive information about a particular file — a caption, a photographer, a usage right — is held in ordinary fields next to it.

## Many files per object

A single file field suits a small, fixed set of files. To hold many files per object, each with its own description, [nested tables](nested-and-reverse-nested.md) are used: each row of the nested table has a file field together with descriptive fields.

A museum's record for a vase might have a nested table of photographs — each row one photograph with its caption, photographer and date — and a separate nested entry holding the loan agreement as a document. The vase is one record; its ten photographs and its contract are nested rows under it, each carrying its own file. This is the usual way a single object accumulates many files without crowding them into one cell.

## What a file is

Each file is an uploaded **original** together with everything fylr derives from it. On upload, fylr:

1. stores the **original** — the unaltered bytes — and records the uploader, the time, the original filename and the file's hash;
2. assigns the file a **class** (see below), which determines how it is processed;
3. produces a set of derived files — a thumbnail for grids, a preview for the detail page, a larger image for zooming, a poster frame for video;
4. extracts technical metadata: dimensions, DPI and colour profile for images; duration and codec for audio and video; page count for documents.

The derived files have names:

- **Original** — the file as uploaded. fylr does not modify it.
- **Version** — a file derived from the original, such as a thumbnail, preview or zoom image. A file has several versions, each with a status while it is produced.
- **Variant** — a rendering prepared for download, in a particular resolution and format.
- **Rendition** — any file that is not the original. Versions and variants are both renditions.

## Classes

A file's **class** is its broad category: image, video, audio, document, office, or other. The class is not the MIME type. The MIME type is specific (`image/jpeg`, `application/pdf`); the class is the category fylr treats the file as. Several MIME types map to one class — `image/jpeg`, `image/png` and `image/tiff` all map to image — and the class determines which production pipeline runs. The class is also used in permissions: a grant can restrict uploads to specific classes without listing individual MIME types.

## Replacing a file

Saving a record does not move its files. Editing the caption, adding a tag or changing a link leaves the files untouched. Replacing a file follows one of two paths:

- **Replace** — a file in the list is swapped for a new one.
- **New version of the original** — the original is updated, for example with a cropped or rotated file, and the renditions are produced again.

When a record is moved to the [trash](records-and-objecttypes.md), its files stay available, so an undelete restores them. When a record is purged, its files are released for cleanup by the **janitor**, a background process that removes files no record references, drains the trash on schedule, and reclaims storage. Until the janitor runs, the underlying files remain on disk.

## Stored or referenced

By default fylr copies an uploaded file into its own store, so it can produce renditions, apply watermarks, serve the file under its own URLs, and keep it available if the source goes offline.

A second mode keeps the file where it already is — a video on a CDN, an image at another institution's image server. In this mode fylr keeps a reference rather than a copy and does not produce renditions; the record points at the external URL, and fylr cannot then guarantee the file's availability or produce its own renditions of it.

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what files attach to.
- [Nested and reverse-nested tables](nested-and-reverse-nested.md) — how an object holds many files, each with its own metadata.
- [Permissions](permissions.md) — class-based and per-rendition limits on uploads and downloads.
- [Collections and publishing](collections-and-publishing.md) — how files are exposed through publishing, IIIF and WebDAV.
- [FOR ADMINISTRATORS](../for-administrators/) — configuring which versions are produced and which classes are allowed.
