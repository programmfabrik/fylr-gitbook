---
description: fylr uses OAuth2 for authentication.
---

# OAuth2

User authentication in a fylr instance is only possible by receiving an **Access Token** using one of the implemented OAuth2 flows.

## Using the Access Token

After a successful login of a user, the process will return a response that contains an `access_token`. This must be used to authenticate all following requests to the fylr API.

### Header based authentication

Include the following HTTP header in the request:

```
"authorization: Bearer <access_token>"
```

### URL based authentication

Include the following parameter in the request URL:

```
?access_token=<access_token>
```

## Configuring Client ID and Secret

The following descriptions of the different OAuth2 flows use `my-client` and `my-secret` as placeholders for configured Client IDs and Client Secrets. Replace these with the required OAuth2 client information of the fylr instance.

These need to be configured in the fylr instance.

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

The default clients in fylr are public and thus do neither need nor have a secret.



Alternatively, add the Client ID and Secret pair(s) in the [Base Configuration](for-administrators/readme/user-management/#oauth-service).



## OAuth2 Flows

All of the following flows are implemented in fylr. They offer different levels of security. Each flow requires a different amount of complexity to implement it in your client application. Depending on your needs choose your preferred implementation. We recommend using the [Authorization Code Grant](oauth2.md#authorization-code-grant) or the [Password Grant](oauth2.md#password-grant) flow.

### Authorization Code Grant

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/server-side-apps/authorization-code/](https://www.oauth.com/oauth2-servers/server-side-apps/authorization-code/)
{% endhint %}

This flow requires a **Client ID** and **Secret**, as well as a fylr **login** and **password** for each user. This flow offers a high level of security.

#### **Step 1**: client calls fylr

{% swagger path="http://fylr-instance/api/oauth2/auth" method="get" summary="Call the OAuth2 Authentication API of fylr" expanded="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter name="auth_method" type="string" required="true" in="query" %}
fixed value: `"auto"`
{% endswagger-parameter %}

{% swagger-parameter name="access_type" type="string" required="true" in="query" %}
fixed value: `"offline"`
{% endswagger-parameter %}

{% swagger-parameter name="scope" type="string" required="true" in="query" %}
fixed value: `"offline"`
{% endswagger-parameter %}

{% swagger-parameter name="response_type" type="string" required="true" in="query" %}
fixed value: `"code"`
{% endswagger-parameter %}

{% swagger-parameter name="state" type="string" required="true" in="query" %}
Client State String (min. 8 characters), for example: `"Authorization_Code_Grant_Login"`
{% endswagger-parameter %}

{% swagger-parameter name="client_id" type="string" required="true" in="query" %}
**Client ID** of the fylr Instance: `"my-client"`
{% endswagger-parameter %}

{% swagger-response status="200" description="OK" %}
This redirects to the fylr login page. The user enters **login** and **password** directly into fylr.
{% endswagger-response %}

{% swagger-response status="400" description="Error" %}
Problems with the parameters, for example an invalid **Client ID**
{% endswagger-response %}
{% endswagger %}

#### **Step 2**: callback from fylr to the local HTTP server

This flow requires to implement a local HTTP server that can handle the callback from fylr. The URL for the callback must also be included in the `fylr.yml` (`redirectURIs`) and must be tied to your Client configuration.

fylr calls

```
http://my-callback-server/oauth2/callback
```

This callback must handle a `GET` request. fylr includes these URL parameters:

{% swagger path="http://my-callback-server/oauth2/callback" method="get" summary="Call the OAuth2 Authentication API of fylr" expanded="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter name="state" type="string" required="true" in="query" %}
Client State, this is to identify the callback. Same as above
{% endswagger-parameter %}

{% swagger-parameter name="code" type="string" required="true" in="query" %}
**Authorization Code**. This needs to be stored and used in the following requests
{% endswagger-parameter %}
{% endswagger %}

#### **Step 3**: client validates Authorization Code

{% swagger path="http://fylr-instance/api/oauth2/token" method="post" summary="Call the OAuth2 Token API of fylr" expanded="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter name="grant_type" type="string" required="true" in="query" %}
fixed value: `"authorization_code"`
{% endswagger-parameter %}

{% swagger-parameter name="state" type="string" required="true" in="query" %}
Client State, same as above
{% endswagger-parameter %}

{% swagger-parameter name="client_id" type="string" required="true" in="query" %}
**Client ID** of the fylr Instance: `"my-client"`
{% endswagger-parameter %}

{% swagger-parameter name="client_secret" type="string" required="true" in="query" %}
**Client Secret** of the fylr Instance: `"my-secret"`
{% endswagger-parameter %}

{% swagger-parameter name="code" type="string" required="true" in="query" %}
**Authorization Code** from fylr callback
{% endswagger-parameter %}

{% swagger-response status="200" description="OK" %}

{% endswagger-response %}

{% swagger-response status="400" description="Error" %}

{% endswagger-response %}
{% endswagger %}

If the **Client ID**, **Secret** and the **Authorization Code** are correct, fylr will return a JSON object in the response with the following values:

| Key             | Description                                         |
| --------------- | --------------------------------------------------- |
| `access_token`  | **Access Token**                                    |
| `refresh_token` | **Refresh Token**                                   |
| `token_type`    | `"bearer"`                                          |
| `scope`         | `"offline"`, same as above                          |
| `expires_in`    | Time until the **Access Token** expires, in seconds |

### Authorization Code Grant with PKCE Code Challenge

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/oauth-native-apps/pkce/](https://www.oauth.com/oauth2-servers/oauth-native-apps/pkce/)
{% endhint %}

This is an extension of the [Authorization Code Grant](oauth2.md#authorization-code-grant) flow. To enhance the security a Proof Key for Code Exchange (PKCE) is included in the requests. All other parameters and keys are the same as in the [Authorization Code Grant](oauth2.md#authorization-code-grant) flow.

The client needs to generate a **Code Verifier** and a **Code Challenge** according to the [RFC7636](https://datatracker.ietf.org/doc/html/rfc7636) standard.

The **Code Verifier** is a random string consisting of the characters `A-Z`, `a-z`, `0-9`, `-`, `.`, `_`, `~` with a length between 43 and 128 characters.

The **Code Challenge** is the `SHA256` hash of the Code Verifier encoded in Base64-URL format.

For **Step 1**, these parameters are added to the URL:

| Parameter               | Value    | Description                  |
| ----------------------- | -------- | ---------------------------- |
| `code_challenge`        |          | Generated **Code Challenge** |
| `code_challenge_method` | `"S256"` | fixed value                  |

For **Step 3**, this parameter is added to the URL:

| Parameter       | Value | Description                 |
| --------------- | ----- | --------------------------- |
| `code_verifier` |       | Generated **Code Verifier** |

In this step, fylr (the authorization server) checks if the **Code Verifer** matches the **Code Challenge** from Step 1.

### Password Grant

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/access-tokens/password-grant/](https://www.oauth.com/oauth2-servers/access-tokens/password-grant/)
{% endhint %}

This flow can be used to directly log into fylr with the user **login** and **password**

#### **Step 1**: log into fylr with user login and password

{% swagger path="http://fylr-instance/api/oauth2/token" method="post" summary="Call the OAuth2 Token API of fylr" expanded="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter name="grant_type" type="string" required="true" in="query" %}
fixed value: `"password"`
{% endswagger-parameter %}

{% swagger-parameter name="scope" type="string" required="true" in="query" %}
fixed value: `"offline"`
{% endswagger-parameter %}

{% swagger-parameter name="client_id" type="string" required="true" in="query" %}
**Client ID** of the fylr Instance: `"my-client"`
{% endswagger-parameter %}

{% swagger-parameter name="client_secret" type="string" required="true" in="query" %}
**Client Secret** of the fylr Instance: `"my-secret"`
{% endswagger-parameter %}

{% swagger-parameter name="username" type="string" required="true" in="query" %}
fylr **Login** of the user
{% endswagger-parameter %}

{% swagger-parameter name="password" type="string" required="true" in="query" %}
fylr **Password** of the user
{% endswagger-parameter %}

{% swagger-response status="200" description="OK" %}

{% endswagger-response %}

{% swagger-response status="400" description="Error" %}
Problems with the parameters, for example an invalid **Client ID**
{% endswagger-response %}
{% endswagger %}

If the **Client ID**, **Secret** and user **login** and **password** are correct, fylr will return a JSON object in the response with the following values:

| Key             | Description                                         |
| --------------- | --------------------------------------------------- |
| `access_token`  | **Access Token**                                    |
| `refresh_token` | **Refresh Token**                                   |
| `token_type`    | `"bearer"`                                          |
| `scope`         | `"offline"`, same as above                          |
| `expires_in`    | Time until the **Access Token** expires, in seconds |

### Implicit Grant

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/single-page-apps/implicit-flow/](https://www.oauth.com/oauth2-servers/single-page-apps/implicit-flow/)
{% endhint %}

{% hint style="warning" %}
This flow works without a **Client Secret**. It is not possible to refresh or revoke the **Access Token**.

Using this flow is **not recommended**!
{% endhint %}

#### **Step 1**: request a token from fylr

{% swagger path="http://fylr-instance/api/oauth2/auth" method="get" summary="Call the OAuth2 Authentication API of fylr" expanded="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter name="response_type" type="string" required="true" in="query" %}
fixed value: `"token"`
{% endswagger-parameter %}

{% swagger-parameter name="auth_method" type="string" required="true" in="query" %}
fixed value: `"auto"`
{% endswagger-parameter %}

{% swagger-parameter name="scope" type="string" required="true" in="query" %}
fixed value: `"offline"`
{% endswagger-parameter %}

{% swagger-parameter name="access_type" type="string" required="true" in="query" %}
fixed value: `"offline"`
{% endswagger-parameter %}

{% swagger-parameter name="state" type="string" required="true" in="query" %}
Client State String (min. 8 characters), for example: `"Implicit_Grant_Login"`
{% endswagger-parameter %}

{% swagger-parameter name="client_id" type="string" required="true" in="query" %}
**Client ID** of the fylr Instance: `"my-client"`
{% endswagger-parameter %}

{% swagger-response status="200" description="OK" %}

{% endswagger-response %}

{% swagger-response status="400" description="Error" %}
Problems with the parameters, for example an invalid **Client ID**
{% endswagger-response %}
{% endswagger %}

#### **Step 2**: callback from fylr to the local callback

This flow requires to implement a local HTTP server that can handle the callback from fylr. The URL for the callback must also be included in the `fylr.yml` (`redirectURIs`) and must be tied to your Client configuration.

fylr calls

```
http://my-callback-server/oauth2/callback
```

This callback must handle a `GET` request. fylr includes these URL parameters:

{% swagger path="http://my-callback-server/oauth2/callback" method="get" summary="Call the OAuth2 Authentication API of fylr" expanded="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter name="loc_hash" type="string" required="true" in="query" %}
quoted URL parameters
{% endswagger-parameter %}
{% endswagger %}

The `loc_hash` parameter is itself a list of URL parameters that need to be unquoted and split into key value pairs:

| Key            | Description                                         |
| -------------- | --------------------------------------------------- |
| `access_token` | **Access Token**                                    |
| `token_type`   | `"bearer"`                                          |
| `scope`        | `"offline"`, same as above                          |
| `state`        | `"Implicit_Grant_Login"`, same as above             |
| `expires_in`   | Time until the **Access Token** expires, in seconds |

### Client Credential Grant

{% hint style="info" %}
External documentation: [https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/)
{% endhint %}

{% hint style="warning" %}
This flow works without a fylr user **login** and **password**. The **Access Token** can not be used to identify a specific user. All fylr api endpoints which require a authenticated user can not be used.

Using this flow is **not recommended**!
{% endhint %}

#### **Step 1**: request a token from fylr

{% swagger path="http://fylr-instance/api/oauth2/token" method="get" summary="Call the OAuth2 Token API of fylr" expanded="true" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter name="grant_type" type="string" required="true" in="query" %}
fixed value: `"client_credentials"`
{% endswagger-parameter %}

{% swagger-parameter name="state" type="string" required="true" in="query" %}
Client State String (min. 8 characters), for example: `"Implicit_Grant_Login"`
{% endswagger-parameter %}

{% swagger-parameter name="client_id" type="string" required="true" in="query" %}
**Client ID** of the fylr Instance: `"my-client"`
{% endswagger-parameter %}

{% swagger-parameter name="client_secret" type="string" required="true" in="query" %}
**Client Secret** of the fylr Instance: `"my-secret"`
{% endswagger-parameter %}

{% swagger-response status="200" description="OK" %}

{% endswagger-response %}

{% swagger-response status="400" description="Error" %}
Problems with the parameters, for example an invalid **Client ID**
{% endswagger-response %}
{% endswagger %}

If the **Client ID** and **Secret** are correct, fylr will return a JSON object in the response with the following values:

| Key            | Description                                         |
| -------------- | --------------------------------------------------- |
| `access_token` | **Access Token**                                    |
| `token_type`   | `"bearer"`                                          |
| `scope`        | `"offline"`, same as above                          |
| `expires_in`   | Time until the **Access Token** expires, in seconds |
