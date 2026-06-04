# /api/v1/objects

**Deep link** access to a stored object or one of its files via a
**structured path grammar** (not an opaque token). The path after
`/objects/` is an ordered sequence of selectors that **fylr** parses
segment by segment and resolves directly against the object store.

Must be enabled in the base config
(`system.deep_link_access.enabled`); when it is off every request
returns 400 with `code: DeepLinkAccessDisabled`.

No system right is required to call the endpoint and no token is
mandatory: if the request carries a valid session that user is used,
otherwise the request runs as the built-in `deep_link` system user.

**Differs from easydb 5:** there is no `auth` query parameter. easydb 5
documents an `auth` parameter to select the system user (`deep_link`,
default, or `oai_pmh`); **fylr** always uses the session user and falls
back only to the `deep_link` system user — `oai_pmh` cannot be selected
here.

Object-level rights are still enforced once the object is resolved —
a caller lacking the object read right, or (when no `mask/<name>` is
given) having no accessible mask, gets 403
`ObjectInsufficientRights`, and a missing asset-download right on a
`file/...` selector gets 403 `ObjectInsufficientAssetDownloadRight`.

Exactly **one** object selector is required:

  * `id/<system-object-id>` — requires
    `system.deep_link_access.allow_access_by_id`.
  * `uuid/<uuid>`.
  * `column/<objecttype>/<column>/<value>` — requires
    `system.deep_link_access.allow_access_by_column`. A value that
    matches more than one object is rejected.

**Differs from easydb 5:** the config keys are
`system.deep_link_access.allow_access_by_id` and
`...allow_access_by_column`. easydb 5 documents these as
`allow_access_by_ids` (plural) and `allow_access_by_unique_columns`.

Optional selectors (each at most once):

  * `mask/<mask-name>` — render through a named mask.
  * a version qualifier after an `id`/`uuid` object selector:
    `/latest` or `/version/<n>`.
  * a file selector: `file/standard/<n>`, `file/all/<n>`,
    `file/id/<n>`, or `file/column/<column>[/<nth>]`.
  * `file_browser/preferred` or `file_browser/<n>`.
  * `file_version/name/<name>` or `file_version/group/<group>`.
  * `format/<fmt>` (see below).
  * `disposition/inline` or `disposition/attachment`.

Supported `format` values: `json` (the default when no `format` and
no `file/...` selector are given), `xml_easydb`, `csv`, `html`,
`xslt/<sheet-name>` (the sheet must be enabled for `/api/objects`),
and `iiif` (only as `format/iiif/v3/manifest.json`, with no `file/...`
selector). When a `file/...` selector is present and no `format` is
given, the raw file bytes are served.

**Differs from easydb 5:** **fylr** also serves `html` and `iiif`
(`iiif/v3/manifest.json`). easydb 5 documents only `json`,
`xml_easydb`, `xslt`, and `csv`.

The response `Content-Type` is set by the chosen format or the
underlying EAS file's MIME type.

Examples:

  * `GET /api/v1/objects/id/42`
  * `GET /api/v1/objects/uuid/nes1/format/html`
  * `GET /api/v1/objects/column/keywords/keyword/Gold`
  * `GET /api/v1/objects/id/42/latest/file/all/1`
  * `GET /api/v1/objects/id/42/version/1/format/xslt/style1`
  * `GET /api/v1/objects/id/42/mask/images__all_fields/format/iiif/v3/manifest.json`

### `GET /objects/{path}` — Resolve a deep link and serve the underlying resource.
{% swagger src="./fylr-openapi.yml" path="/objects/{path}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `HEAD /objects/{path}` — Probe a deep link without downloading the resource.
{% swagger src="./fylr-openapi.yml" path="/objects/{path}" method="head" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
