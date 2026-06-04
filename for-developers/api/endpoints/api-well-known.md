# /.well-known

OpenID Connect **discovery document** (provider metadata). A public, unauthenticated document advertising fylr's OAuth2 / OpenID Connect issuer and endpoints so that OIDC clients can configure themselves.

Served at the server root (`/.well-known/openid-configuration`) — **not** under `/api/v1`. The endpoint URLs it returns are absolute, built from the instance's configured external URL (`fylr.externalURL`), and point at `/api/oauth2/*`.

The route is not method-restricted: any HTTP method returns the same metadata document with status `200`.

### `GET /.well-known/openid-configuration` — Fetch the OpenID Connect provider metadata.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/.well-known/openid-configuration" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
