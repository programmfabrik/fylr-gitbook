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

* [/api/collection](collection/README.md)
* [/api/config](config/README.md)
* [/api/db](api-db.md)
* [/api/db_info](api-db_info.md)
* [/api/eas](eas/README.md)
* [/api/event](api-event.md)
* [/api/export](api-export.md)
* [/api/group](api-group.md)
* [/api/hotfolder](api-hotfolder.md)
* [/api/l10n](api-l10n.md)
* [/api/mask](api-mask.md)
* [/api/message](api-message.md)
* [/api/oaipmh](api-oaipmh.md)
* [/api/oauth2](api-oauth2.md)
* [/api/objects](api-objects.md)
* [/api/objecttype](api-objecttype.md)
* [/api/plugin](plugin/README.md)
* [/api/pool](api-pool.md)
* [/api/publish](api-publish.md)
* [/api/right](api-right.md)
* [/api/schema](api-schema.md)
* [/api/search](api-search.md)
* [/api/settings](api-settings.md)
* [/api/suggest](api-suggest.md)
* [/api/system](system/README.md)
* [/api/tags](api-tags.md)
* [/api/task](api-task.md)
* [/api/transitions](api-transitions.md)
* [/api/user](api-user.md)
* [/api/webdav](api-webdav.md)
* [/.well-known/openid-configuration](api-well-known.md)
* [/api/xmlmapping](api-xmlmapping.md)
