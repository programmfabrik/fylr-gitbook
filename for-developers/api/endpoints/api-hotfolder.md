# /api/v1/hotfolder

A **drop-only** ingest share at `/api/v1/hotfolder`, distinct from the
read/write `/api/v1/WebDAV` mount above. Where `/WebDAV` maps WebDAV
operations onto collections live, the hotfolder is a real on-disk
staging directory (the API service's `WebDAVHotfolderPath`) served by
the Go standard-library `webdav.Handler`. You **drop files in**; a
background crawler imports each one into the matching collection and
deletes it. You do **not** read a collection's records back through it.

**Layout.** The on-disk directory holds one sub-directory per
collection, named by the collection UUID, created automatically for
every collection that accepts objects (`objects_allowed`). A file is
therefore dropped at
`/api/v1/hotfolder/{collectionUuid}/<...>/<filename>`. A file placed at
the top level (no collection UUID) is ignored.

**Ingestion.** A single crawler walks the directory and imports a file
only once it has settled — its size and modification time must be
unchanged for a configurable delay (15 s by default) — so half-written
uploads are not grabbed. Empty files, dot-files and `hotfolder.log` are
skipped; when both a JPEG and a non-JPEG of the same name are pending,
the non-JPEG is imported first. On import the file is renamed to
`IMPORTING-<name>`, uploaded into the collection identified by the UUID
(creating a record / linked file, exactly as a `PUT` on the `/WebDAV`
mount would), then deleted. The path below the collection UUID is kept
as the stored file path; files in sub-directories are imported flat. A
failed import is renamed to `ERROR-<name>` with a `<name>.log` beside
it. Every attempt is appended as a TSV row to `hotfolder.log` inside the
collection's directory, with columns `date`, `user`, `path`, `file`,
`size`, `system_object_id`, `file_eas_id`, `status`, `msg`.

**Enablement.** Served only when `webdav.hotfolder = true`, a hotfolder
path is configured, and the instance runs a **single backend**;
otherwise every request returns 503 with `code: WebdavNotEnabled`. This
gate is independent of `webdav.read_write_access`.

**Authentication.** As with `/WebDAV`, the share performs **no client
authentication** — connect as guest and send no credentials. The import
runs server-side as the owner of the target collection.

Being a stdlib `webdav.Handler` it accepts the full WebDAV method set,
but only `PUT` (drop a file) and `MKCOL` (create a sub-directory) do
anything meaningful; `GET` / `PROPFIND` expose the on-disk staging area
(files still pending, plus any `IMPORTING-` / `ERROR-` markers and
`hotfolder.log`), never the collection's actual contents.

### `GET /hotfolder/{collectionUuid}/{path}` — Read the on-disk staging area (not the collection's objects).
{% swagger src="./fylr-openapi.yml" path="/hotfolder/{collectionUuid}/{path}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `PUT /hotfolder/{collectionUuid}/{path}` — Drop a file into the collection's hotfolder for ingestion.
{% swagger src="./fylr-openapi.yml" path="/hotfolder/{collectionUuid}/{path}" method="put" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
