# Endpoints

The fylr HTTP/JSON API. Most endpoints live under the **`/api/v1`** base path —
for example `/api/v1/collection` or `/api/v1/search`. The OAuth2 / OpenID
Connect endpoints under `/api/oauth2` and the `.well-known` discovery document
are the exceptions; each lists its own full path.

**Authentication.** Calls are authenticated with an access token. Present it as
an `Authorization: Bearer <token>` header, or — as fallbacks — the
`access_token` query parameter or an `X-Fylr-Authorization: Bearer <token>`
header (a workaround for Safari, which overwrites `Authorization`). A request
without a valid token runs as an anonymous session; endpoints that require a
user then answer `401`.

Each page below documents one endpoint group, with an interactive panel per
operation generated from the OpenAPI specification (`fylr-openapi.yml`). Pages
are grouped by the first path segment; larger groups — collection, eas, system,
config, plugin — carry subpages.

## All endpoints

* [/api/v1/collection](collection/README.md)
* [/api/v1/config](config/README.md)
* [/api/v1/db](api-db.md)
* [/api/v1/db_info](api-db_info.md)
* [/api/v1/eas](eas/README.md)
* [/api/v1/event](api-event.md)
* [/api/v1/export](api-export.md)
* [/api/v1/group](api-group.md)
* [/api/v1/hotfolder](api-hotfolder.md)
* [/api/v1/l10n](api-l10n.md)
* [/api/v1/mask](api-mask.md)
* [/api/v1/message](api-message.md)
* [/api/v1/oai](api-oai.md)
* [/api/oauth2](api-oauth2.md)
* [/api/v1/objects](api-objects.md)
* [/api/v1/objecttype](api-objecttype.md)
* [/api/v1/plugin](plugin/README.md)
* [/api/v1/pool](api-pool.md)
* [/api/v1/publish](api-publish.md)
* [/api/v1/right](api-right.md)
* [/api/v1/schema](api-schema.md)
* [/api/v1/search](api-search.md)
* [/api/v1/settings](api-settings.md)
* [/api/v1/suggest](api-suggest.md)
* [/api/v1/system](system/README.md)
* [/api/v1/tags](api-tags.md)
* [/api/v1/task](api-task.md)
* [/api/v1/transitions](api-transitions.md)
* [/api/v1/user](api-user.md)
* [/api/v1/WebDAV](api-webdav.md)
* [/.well-known](api-well-known.md)
* [/api/v1/xmlmapping](api-xmlmapping.md)
