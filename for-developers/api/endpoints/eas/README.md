# /api/v1/eas

Fetch the [file](https://docs.fylr.io/for-developers/system-data-types/file)
renderings for several files at once. The file `ids` are passed as a JSON
array in the query; the response is a map keyed by file `ID`. A file is shown
if the user holds `RIGHT_ASSET_SHOW` or `RIGHT_ASSET_DOWNLOAD` on the original
or on at least one of its versions. There is no blanket login gate: an
unauthenticated request is served via the `deep_link` system user if deep
linking is enabled. Use `GET /eas/{fileId}` to address a single file.

Differs from easydb 5: easydb 5 requires an authenticated user on
`GET /eas` ("The user must be authenticated."); **fylr** has no login
gate here — a missing token is served as the anonymous `deep_link`
user, and a denied request is `403` (`InsufficientRights`), never
`401`.

### `GET /eas/{fileId}` — Get information about a file. The file is shown if the caller holds `RIGHT_ASSET_SHOW` or `RIGHT_ASSET_DOWNLOAD` on the original or any version.
{% swagger src="../fylr-openapi.yml" path="/eas/{fileId}" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `POST /eas/{fileId}` — Change information about a file. The caller must be allowed to produce the file (its uploader, or a user with write access to a linked object).
{% swagger src="../fylr-openapi.yml" path="/eas/{fileId}" method="post" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}

### `GET /eas` — Get information about a file.
{% swagger src="../fylr-openapi.yml" path="/eas" method="get" %}
[fylr-openapi.yml](../fylr-openapi.yml)
{% endswagger %}
