# /logout

Logs the browser that sends the request out of the web app and redirects it. Served at the server root (`/logout`) — **not** under `/api/v1`. The web app sends the browser here to log out; see [OAuth2](../oauth2.md#logging-out-the-browser-logout) for how it fits the token flows.

The request needs no access token: the browser is identified by its `fylr-browser-id` cookie.

### `GET /logout` — Log the browser out and redirect.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/logout" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
