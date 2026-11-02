# /download

The download endpoint is used to deliver binary file data. It delivers data for original files as well as renditions. These URL to the files should be taken from the responses of `/api/db` or `/api/search`.

### `GET /eas/download/{fileId}/{hash}/{version}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `HEAD /eas/download/{fileId}/{hash}/{version}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}" method="head" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /eas/download/{fileId}/{hash}/{version}/{zippath}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}/{zippath}" method="get" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `HEAD /eas/download/{fileId}/{hash}/{version}/{zippath}`

{% openapi src="../../../../.gitbook/assets/fylr-openapi.yml" path="/eas/download/{fileId}/{hash}/{version}/{zippath}" method="head" %}
[fylr-openapi.yml](../../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### When the storage fails

From **6.36.0**, a download, an IIIF or zoom tile and a rendering made on the fly that cannot get the file from its storage answer `502`, whatever the storage answered. A `403` of the storage is no `403` of this instance, so a client can tell a refused storage from missing rights.

* `StorageRefused`: the storage answered with an error other than `404`. `parameters` carries `fileid`, `location` (the id of the storage location, `remote` for a file left at a URL), `storagestatus` and `storagemessage`, what the storage said, cut to 256 characters.
* `StorageUnreachable`: the storage gave no answer or broke off, or its location is not connected. `parameters` carries `fileid`, `location` and `reason`.

A `404` of the storage answers `404 ResourceNotFound`. No answer quotes the URL of the source.

### Paths inside a ZIP

The `{zippath}` form reads one entry out of a ZIP stored as an original or a version — a page of a `pages.zip`, a file of an archive — without downloading the whole ZIP, range requests included. The ZIP is read on demand: no special version and no particular extension is required, and holding `asset_show` on the record is enough. It works for files in any connected storage location, S3 included; a file that is not stored in a location — one left at its remote URL via `leave_on_remote` — fails with `ZipPathNotSupported`, the endpoint's one restriction.

A directory listing of a ZIP (from **6.35.0**) reports each entry's `mod_time` from the extended UTC timestamp where the archive carries one, instead of the legacy MS-DOS field, and directory entries carry a `mod_time` as well; `size` stays omitted for directories.
