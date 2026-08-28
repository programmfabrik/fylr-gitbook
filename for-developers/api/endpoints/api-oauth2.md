# /api/oauth2

OAuth2 **authorization endpoint** (RFC 6749 §3.1). This is where the browser web-app logs a user in. It authenticates the end user — by password (`auth_method=easydb`, the default; also `ldap`, `email`, `collection`), anonymously (`anonymous`, when guest login is enabled), via SAML, or with an action code — and returns an authorization `code` by redirecting back to the client's `redirect_uri`.

Served at `/api/oauth2/auth` — **not** under `/api/v1`. No prior access token is required.

### Session binding (anti-hijacking)

Since fylr 6.34.0, an access/refresh token issued to the browser via this endpoint is bound to the browser's long-lived, HttpOnly `fylr-browser-id` cookie (a "Stay logged in" cookie is bound the same way). That cookie must then accompany the `Authorization: Bearer` token on every API request; a token presented from a different browser — i.e. without the matching cookie — is rejected as invalid (`InvalidToken`), so a stolen bearer token on its own cannot be replayed. Binding is silent and always on.

**API clients are not affected:** a token obtained at `/oauth2/token` via the password or client-credentials grant is issued **unbound** when the request carries no `fylr-browser-id` cookie — such integrations keep working unchanged. A login whose token is consumed on a different origin than the fylr itself — a third-party OAuth client (a cross-origin `redirect_uri`) or a cross-server *webOnly* frontend — is likewise issued an unbound token, since that origin's requests would not carry the cookie.

### `GET /oauth2/auth` — Begin an authorization request (interactive login).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/oauth2/auth" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /oauth2/auth` — Submit the login form / authorization request.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/oauth2/auth" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /oauth2/token` — Issue an access token.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/oauth2/token" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /oauth2/revoke` — Revoke a token (logout).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/oauth2/revoke" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /oauth2/introspect` — Introspect a token.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/oauth2/introspect" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /oauth2/userinfo` — Get claims for the access-token user.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/oauth2/userinfo" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /oauth2/userinfo` — Get claims for the access-token user (form POST).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/oauth2/userinfo" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
