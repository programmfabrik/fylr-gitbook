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

### Paths inside a ZIP

The `{zippath}` form reads one entry out of a ZIP stored as an original or a version — a page of a `pages.zip`, a file of an archive — without downloading the whole ZIP, range requests included. The ZIP is read on demand: no special version and no particular extension is required, and holding `asset_show` on the record is enough. It works for files in any connected storage location, S3 included; a file that is not stored in a location — one left at its remote URL via `leave_on_remote` — fails with `ZipPathNotSupported`, the endpoint's one restriction.

A directory listing of a ZIP (from **6.35.0**) reports each entry's `mod_time` from the extended UTC timestamp where the archive carries one, instead of the legacy MS-DOS field, and directory entries carry a `mod_time` as well; `size` stays omitted for directories.
