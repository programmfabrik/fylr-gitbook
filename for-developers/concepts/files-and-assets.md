# Files and assets

Many objecttypes carry files: a Photo carries a photograph, an Article carries the laid-out PDF, a Music Track carries an audio file. In fylr a file is a data type, like text or a number — a field of that type holds files, and an objecttype can have as many file fields as it needs.

## Records and files are separate

A record holds metadata: title, author, date, captions, links to other records. A file is the image, video or document itself. fylr keeps the two separate. The metadata is small, edited often, and indexed for search; the file is large, read more than written, and runs through a production pipeline that takes time. A record references its files; the files are held in fylr's file store.

Because they are separate, a record can have a file replaced — a re-scan, a corrected colour profile, a higher-resolution upload — without affecting its metadata or history.

## A file field holds a list of files

A file field's value is not a single file but a **list** of files, called its **variants**. One field can hold several at once — the front and back of a postcard, several scans of one page. Exactly one variant is the **preferred** one, which fylr uses wherever it needs a single image to stand for the record: the thumbnail in a result grid, the preview on the detail page, an avatar. When a field holds one file, that file is the preferred variant.

The file field itself holds only the files. It carries no description of each file beyond the file's own technical data. Descriptive information about a particular file — a caption, a photographer, a usage right — is held in ordinary fields next to it.

## Many files per object

A single file field suits a small, fixed set of files. To hold many files per object, each with its own description, [nested tables](nested-and-reverse-nested.md) are used: each row of the nested table has a file field together with descriptive fields.

A museum's record for a vase might have a nested table of photographs — each row one photograph with its caption, photographer and date — and a separate nested entry holding the loan agreement as a document. The vase is one record; its ten photographs and its contract are nested rows under it, each carrying its own file. This is the usual way a single object accumulates many files without crowding them into one cell.

## Original and renditions

Each variant is an uploaded **original** together with everything fylr derives from it. On upload, fylr:

1. stores the **original** — the unaltered bytes — and records the uploader, the time, the original filename and the file's hash;
2. assigns it a **class** (see below), which determines how it is processed;
3. produces a set of **renditions** — a thumbnail for grids, a preview for the detail page, a larger image for zooming, a poster frame and a smaller copy for video;
4. extracts technical metadata: dimensions, DPI and colour profile for images; duration and codec for audio and video; page count for documents.

A **rendition** is a rendering derived from the original. It can be a smaller image, a smaller video, or a different format altogether — a PDF generated from an office document, for example. The original is never modified; renditions are produced from it, and each has a status while it is produced.

(In fylr, _version_ is not a file term. A version is a [record's](records-and-objecttypes.md) version; the files derived from an original are renditions.)

Which renditions are produced is set by a **produce configuration**: a set of **recipes**, each selected by file class and other file metadata, that defines what to derive from an original. fylr ships a **default produce configuration**; an instance can define its own in its base configuration, and recipes can be set per objecttype and per pool, so different kinds of record produce different renditions. The mechanics — recipe states, the production queue, reproducing renditions — are covered in [Files and version production](../../for-system-administrators/inspect/files.md).

## Classes

A file's **class** is its broad category: image, video, audio, document, office, or other. The class is not the MIME type. The MIME type is specific (`image/jpeg`, `application/pdf`); the class is the category fylr treats the file as. Several MIME types map to one class — `image/jpeg`, `image/png` and `image/tiff` all map to image — and the class determines which production pipeline runs. The class is also used in permissions: a grant can restrict uploads to specific classes without listing individual MIME types.

## Replacing a file

Saving a record does not move its files. Editing the caption, adding a tag or changing a link leaves the files untouched. Replacing a file follows one of two paths:

- **Replace a variant** — a file in the list is swapped for a new one.
- **Replace the original** — the original is updated, for example with a cropped or rotated file, and its renditions are produced again.

When a record is moved to the [trash](records-and-objecttypes.md), its files stay available, so an undelete restores them. When a record is purged, its files are released for cleanup by the **janitor**, a background process that removes files no record references, drains the trash on schedule, and reclaims storage. Until the janitor runs, the underlying files remain on disk.

## Copied or referenced

Where the original is held is chosen at upload, independently of whether renditions are produced.

- **Copied into fylr's store** (the default). fylr copies the original into its own storage and holds it from then on.
- **Referenced at a remote URL.** The original stays where it already is — a video on a CDN, an image at another institution's server — and fylr holds a reference to it rather than a copy. A referenced file can exceed the usual upload size limits, since fylr is not storing it; fylr checks that the reference is reachable.

Producing renditions is a separate choice. fylr can produce renditions whether the original is copied or referenced — fetching a referenced original from its URL when it needs to — or it can hold a file and produce none. Because a referenced original is not held by fylr, its continued availability depends on the remote host.

## In the API

Files ride inside record JSON and are served by the [`/eas` endpoints](../api/endpoints/eas/README.md):

- A file field's value is a list of file objects; the preferred variant carries `preferred: true`. Each file object holds the file's `class` and its extracted `technical_metadata`.
- A naming trap: the file API addresses the renditions of an original as the file's **versions** — a download URL is [`/eas/download/{fileId}/{hash}/{version}`](../api/endpoints/eas/download.md), where `{version}` names the rendition to fetch. This is unrelated to a record's `_version`.
- An upload that copies the file into fylr's store goes to [`/eas/put`](../api/endpoints/eas/put.md); a file referenced at a remote URL is registered with [`/eas/rput`](../api/endpoints/eas/rput.md).
- Renditions can be produced on demand through [`/eas/produce`](../api/endpoints/eas/produce.md).

## See also

- [Records and objecttypes](records-and-objecttypes.md) — what files attach to.
- [Nested and reverse-nested tables](nested-and-reverse-nested.md) — how an object holds many files, each with its own metadata.
- [Permissions](permissions.md) — class-based and per-rendition limits on uploads and downloads.
- [Collections and publishing](collections-and-publishing.md) — how files are exposed through publishing, IIIF and WebDAV.
- [FOR ADMINISTRATORS](../../for-administrators/) — configuring which renditions are produced and which classes are allowed.
