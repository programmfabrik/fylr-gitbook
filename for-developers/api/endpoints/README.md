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
