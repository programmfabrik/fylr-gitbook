# /api/oauth2

OAuth2 / OpenID Connect **authorization endpoint** (RFC 6749 §3.1). This is where the browser web-app logs a user in. It authenticates the end user — by password (`auth_method=easydb`, the default; also `ldap`, `email`, `collection`), anonymously (`anonymous`, when guest login is enabled), via SAML, or with an action code — and returns an authorization response (an authorization `code`, `token` or `id_token`) by redirecting back to the client's `redirect_uri`.

Served at `/api/oauth2/auth` — **not** under `/api/v1`. No prior access token is required.

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
