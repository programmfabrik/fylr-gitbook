---
description: fylr uses OAuth2 and OpenID Connect for authentication.
---

# OAuth2

User authentication in a fylr instance is done by obtaining an **Access Token** through one of the implemented OAuth2 flows. fylr is also an **OpenID Connect (OIDC)** provider: requesting the `openid` scope additionally returns an `id_token`, and the instance exposes a [UserInfo endpoint](#openid-connect) and an [OIDC discovery document](#openid-connect).

{% hint style="info" %}
The exact request and response of every endpoint below — `/api/oauth2/auth`, `/api/oauth2/token`, `/api/oauth2/revoke`, `/api/oauth2/introspect`, `/api/oauth2/userinfo` — is also available as interactive reference panels under [API → Endpoints → /api/oauth2](endpoints/api-oauth2.md).
{% endhint %}

## Using the Access Token

After a successful login, the response contains an `access_token`. Send it with every following request to the fylr API in one of these ways:

**`Authorization` header (recommended):**

```
Authorization: Bearer <access_token>
```

**URL query parameter:**

```
?access_token=<access_token>
```

**`X-Fylr-Authorization` header** — a fallback for Safari, which can strip the `Authorization` header on cross-origin redirects:

```
X-Fylr-Authorization: Bearer <access_token>
```

An access token is valid for **24 hours** (86400 seconds) by default; the lifetime is configurable in the base configuration.

## Configuring Client ID and Secret

The descriptions of the OAuth2 flows below use `my-client` and `my-secret` as placeholders for configured Client IDs and Client Secrets. Replace these with the OAuth2 client information of your fylr instance.

Configure the pair(s) of Client ID and Secret in the [config file](../../for-system-administrators/configuration/fylr.example.yml.md) `fylr.yml`:

{% code title="" %}
```yaml
fylr:
  services:
    api:
      oauth2Server:
        clients:
          my-client:
            secret: 'my-secret'
            redirectURIs:
              - http://my-callback-server/oauth2/callback
```
{% endcode %}

The default clients in fylr are **public** and thus neither need nor have a secret. A public client must omit `client_secret`.

Alternatively, add the Client ID and Secret pair(s) in the [Base Configuration](for-administrators/readme/user-management/#oauth-service).

## Scopes

fylr understands four scopes, passed as a **space-separated** list in the `scope` parameter (e.g. `openid offline`):

| Scope | Meaning |
| --- | --- |
| `offline` | Requests a **refresh token** (the OIDC alias `offline_access` works too). Without it no refresh token is issued. Only the Authorization Code and Password grants can return one. |
| `openid` | Marks an [OpenID Connect](#openid-connect) request: the token response then also contains an `id_token`. |
| `read`, `write` | Accepted labels only — they do **not** govern API access. What a user may do is decided by fylr's per-user / per-pool **ACL rights**, not by the token scope. |

A client with no `scopes` configured may request any of the four; a scope outside the client's allowed set is rejected. The `scope` value in the token response **echoes the scopes that were granted** (for example `read write openid offline`), it is not a fixed value.

## OAuth2 Flows

fylr implements the **Authorization Code**, **Password**, **Client Credentials** and **Refresh Token** grants. We recommend the [Authorization Code Grant](#authorization-code-grant) (with [PKCE](#authorization-code-grant-with-pkce-code-challenge) for public clients) or the [Password Grant](#password-grant).

{% hint style="warning" %}
The **Implicit Grant** (`response_type=token`) was **removed in fylr 6.33.0**. `/api/oauth2/auth` now accepts only `response_type=code`; a request with `response_type=token` is rejected.
{% endhint %}

### Authorization Code Grant

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/server-side-apps/authorization-code/](https://www.oauth.com/oauth2-servers/server-side-apps/authorization-code/)
{% endhint %}

This flow requires a **Client ID** (and a **Secret** for confidential clients), and a fylr **login** and **password** for each user. It offers a high level of security.

#### **Step 1**: client calls fylr

<mark style="color:blue;">`GET`</mark> `fylr-instance/api/oauth2/auth`

**Query Parameters**

| Name | Type | Description |
| --- | --- | --- |
| `response_type`<mark style="color:red;">\*</mark> | string | fixed value: `"code"` |
| `client_id`<mark style="color:red;">\*</mark> | string | **Client ID**, e.g. `"my-client"` |
| `state`<mark style="color:red;">\*</mark> | string | Client state string (min. 8 characters), e.g. `"Authorization_Code_Grant_Login"` |
| `scope` | string | Space-separated [scopes](#scopes). Include `offline` to receive a refresh token, `openid` to receive an `id_token`. |
| `auth_method` | string | Login method (see [auth\_method](#auth_method) below). Defaults to `auto`. |
| `redirect_uri` | string | Callback URL; must match a `redirectURIs` entry of the client. Required if the client has more than one. |

{% tabs %}
{% tab title="200 OK" %}
This redirects to the fylr login page. The user enters **login** and **password** directly into fylr.
{% endtab %}

{% tab title="400 Error" %}
Problems with the parameters, for example an invalid **Client ID**. The endpoint returns an error description explaining what is wrong.
{% endtab %}
{% endtabs %}

#### `auth_method`

`auth_method` selects the login method. It is **optional** and accepts a single value or a comma-separated list of methods, tried in order:

| Value | Meaning |
| --- | --- |
| `easydb` | Login + password against the fylr user database — the typical choice, and the fallback for unrecognized values. |
| `ldap` | LDAP login (if an LDAP connection is configured). |
| `email`, `collection`, `action_code` | Email-link, collection-share and action-code logins. |
| `saml` | SAML single sign-on. |
| `anonymous` | Guest login (requires guest access to be enabled). |
| `auto` | The default. A server-side selector used by the web app: anonymous when guest login is enabled and no `login` is supplied, otherwise password login. |

For an interactive end-user login, use `easydb` (or omit the parameter).

#### **Step 2**: callback from fylr to the local HTTP server

This flow requires a local HTTP server that can handle the callback from fylr. Its URL must be listed in `fylr.yml` (`redirectURIs`) for the client.

fylr calls `my-callback-server/oauth2/callback` as a `GET` request with these parameters:

| Name | Type | Description |
| --- | --- | --- |
| `state`<mark style="color:red;">\*</mark> | string | Client state, identical to Step 1 |
| `code`<mark style="color:red;">\*</mark> | string | **Authorization Code** — store it for the next step |

{% hint style="info" %}
If the callback redirects to a **cross-origin** destination, that destination must be allow-listed in `fylr.services.webapp.loginAllowRedirects` (new in 6.33.0). Same-origin destinations and the configured `externalURL` work without extra configuration.
{% endhint %}

#### **Step 3**: exchange the Authorization Code for a token

<mark style="color:green;">`POST`</mark> `fylr-instance/api/oauth2/token`

**Body Parameters** (`application/x-www-form-urlencoded`)

| Name | Type | Description |
| --- | --- | --- |
| `grant_type`<mark style="color:red;">\*</mark> | string | fixed value: `"authorization_code"` |
| `code`<mark style="color:red;">\*</mark> | string | **Authorization Code** from the callback |
| `client_id`<mark style="color:red;">\*</mark> | string | **Client ID** |
| `client_secret` | string | **Client Secret** — omit for public clients |
| `redirect_uri` | string | Same `redirect_uri` as in Step 1, if one was used |

{% tabs %}
{% tab title="200 OK" %}
fylr returns a JSON object:

| Key | Description |
| --- | --- |
| `access_token` | **Access Token** |
| `token_type` | `"bearer"` |
| `scope` | The granted scopes, e.g. `"read write openid offline"` |
| `expires_in` | Seconds until the **Access Token** expires |
| `refresh_token` | **Refresh Token** — only when the `offline` scope was granted |
| `id_token` | OpenID Connect **ID Token** (RS256 JWT) — only when the `openid` scope was granted |
{% endtab %}

{% tab title="400 Error" %}
Problems with the parameters, for example an invalid **Client ID** or an expired code.
{% endtab %}
{% endtabs %}

### Authorization Code Grant with PKCE Code Challenge

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/oauth-native-apps/pkce/](https://www.oauth.com/oauth2-servers/oauth-native-apps/pkce/)
{% endhint %}

This is an extension of the [Authorization Code Grant](#authorization-code-grant) that adds a Proof Key for Code Exchange (PKCE), so a public client can use the flow securely without a client secret. All other parameters and keys are the same.

The client generates a **Code Verifier** and a **Code Challenge** per [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636):

- The **Code Verifier** is a random string of `A-Z`, `a-z`, `0-9`, `-`, `.`, `_`, `~`, 43–128 characters long.
- The **Code Challenge** is the `SHA256` hash of the Code Verifier, Base64-URL encoded.

For **Step 1**, add to the URL:

| Parameter | Value | Description |
| --- | --- | --- |
| `code_challenge` | | Generated **Code Challenge** |
| `code_challenge_method` | `"S256"` | fixed value |

For **Step 3**, add to the body:

| Parameter | Value | Description |
| --- | --- | --- |
| `code_verifier` | | Generated **Code Verifier** |

fylr checks that the **Code Verifier** matches the **Code Challenge** from Step 1.

### Password Grant

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/access-tokens/password-grant/](https://www.oauth.com/oauth2-servers/access-tokens/password-grant/)
{% endhint %}

Log directly into fylr with a user **login** and **password**.

<mark style="color:green;">`POST`</mark> `fylr-instance/api/oauth2/token`

**Body Parameters** (`application/x-www-form-urlencoded`)

| Name | Type | Description |
| --- | --- | --- |
| `grant_type`<mark style="color:red;">\*</mark> | string | fixed value: `"password"` |
| `username`<mark style="color:red;">\*</mark> | string | fylr **login** of the user |
| `password`<mark style="color:red;">\*</mark> | string | fylr **password** of the user |
| `client_id`<mark style="color:red;">\*</mark> | string | **Client ID** |
| `client_secret` | string | **Client Secret** — omit for public clients |
| `scope` | string | Space-separated [scopes](#scopes); include `offline` for a refresh token |

{% tabs %}
{% tab title="200 OK" %}
Same response as the Authorization Code Grant: `access_token`, `token_type` (`"bearer"`), `scope`, `expires_in`, plus `refresh_token` (with `offline`) and `id_token` (with `openid`).
{% endtab %}

{% tab title="400 Error" %}
Invalid **Client ID**, or wrong user **login** / **password**.
{% endtab %}
{% endtabs %}

**Example (CURL)**:

```bash
curl 'fylr-instance/api/oauth2/token' \
  --data-urlencode 'grant_type=password' \
  --data-urlencode 'scope=offline' \
  --data-urlencode 'client_id=my-client' \
  --data-urlencode 'username=Login' \
  --data-urlencode 'password=Password'
```

### Refresh Token Grant

When a token response contained a `refresh_token` (i.e. the `offline` scope was granted), exchange it for a fresh access token without asking the user to log in again.

<mark style="color:green;">`POST`</mark> `fylr-instance/api/oauth2/token`

**Body Parameters** (`application/x-www-form-urlencoded`)

| Name | Type | Description |
| --- | --- | --- |
| `grant_type`<mark style="color:red;">\*</mark> | string | fixed value: `"refresh_token"` |
| `refresh_token`<mark style="color:red;">\*</mark> | string | The refresh token |
| `client_id`<mark style="color:red;">\*</mark> | string | **Client ID** |
| `client_secret` | string | **Client Secret** — omit for public clients |

The response is a new `access_token` (and a new `refresh_token`), with the same fields as above.

### Client Credentials Grant

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/)
{% endhint %}

{% hint style="warning" %}
The behaviour of this grant **changed in fylr 6.33.0**.
{% endhint %}

As of 6.33.0 the client-credentials grant returns a token for the **anonymous user** bound to the browser client — so a public frontend can obtain an anonymous session without any user credentials. This requires **guest access** to be enabled in the base configuration (`login.guest`); with guest access off the request is rejected and a warning is written to the fylr log. Anonymous logins are recorded as `USER_LOGIN` / `USER_LOGIN_FAILED` events.

<mark style="color:green;">`POST`</mark> `fylr-instance/api/oauth2/token`

**Body Parameters** (`application/x-www-form-urlencoded`)

| Name | Type | Description |
| --- | --- | --- |
| `grant_type`<mark style="color:red;">\*</mark> | string | fixed value: `"client_credentials"` |
| `client_id`<mark style="color:red;">\*</mark> | string | **Client ID** |
| `client_secret` | string | **Client Secret** — omit for public clients |

The response contains `access_token`, `token_type` (`"bearer"`), `scope` and `expires_in`. This grant does not return a refresh token.

## OpenID Connect

fylr is also an **OpenID Connect** provider. Request the `openid` scope (alongside `offline` etc.) and the token response additionally contains an **`id_token`** — a JWT signed with `RS256`.

**Discovery document** — a public, unauthenticated metadata document served at the server root (not under `/api`):

<mark style="color:blue;">`GET`</mark> `fylr-instance/.well-known/openid-configuration`

It advertises the issuer and the absolute URLs of the authorization, token, introspection, revocation and userinfo endpoints, plus the supported response types, grant types, scopes and claims — so an OIDC client can configure itself automatically. See the [discovery reference panel](endpoints/api-well-known.md).

**UserInfo endpoint** — returns claims about the user identified by the bearer access token:

<mark style="color:blue;">`GET`</mark> / <mark style="color:green;">`POST`</mark> `fylr-instance/api/oauth2/userinfo`

It requires a valid access token and returns `sub` plus whatever claims (email, display name, …) are enabled in the base-config `openid.userinfo` allow-list.

## Revoking a token (Logout)

Revoke an access or refresh token ([RFC 7009](https://datatracker.ietf.org/doc/html/rfc7009)). This is what the web app uses to log out; a `USER_LOGOUT` event is recorded for the token's user.

<mark style="color:green;">`POST`</mark> `fylr-instance/api/oauth2/revoke`

**Body Parameters** (`application/x-www-form-urlencoded`)

| Name | Type | Description |
| --- | --- | --- |
| `token`<mark style="color:red;">\*</mark> | string | The access or refresh token to revoke |
| `token_type_hint` | string | Optional: `access_token` or `refresh_token` |

Per RFC 7009 the endpoint returns `200` even for an unknown token.

## Token Introspection

Inspect the state of a token ([RFC 7662](https://datatracker.ietf.org/doc/html/rfc7662)).

<mark style="color:green;">`POST`</mark> `fylr-instance/api/oauth2/introspect`

**Body Parameters** (`application/x-www-form-urlencoded`)

| Name | Type | Description |
| --- | --- | --- |
| `token`<mark style="color:red;">\*</mark> | string | The token to introspect |
| `token_type_hint` | string | Optional: `access_token` or `refresh_token` |

The response reports `active` (boolean) and, when active, `scope`, `client_id`, `sub`, `exp`, `iat` and `token_type`.
