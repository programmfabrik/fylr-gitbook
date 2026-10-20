# /api/v1/event

Read, write and subscribe to **events**. fylr writes events for many server-side mutations (object insert/update, collection changes, file deletes, email sends, ...). This endpoint exposes the event log.

### `POST /event` — Write a single user event.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /event/poll/{fromEventId}` — Fetch pollable events newer than an event id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event/poll/{fromEventId}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /event/stream` — WebSocket stream of new events.

From **6.35.0** the access token may travel in the websocket handshake instead of the URL: offer `fylr.auth.bearer.<token>` — the token base64url-encoded without padding — as an entry of the `Sec-WebSocket-Protocol` header, next to the real subprotocol `fylr.event.v1`, which the server echoes back. A browser cannot set request headers on a websocket handshake, so this is the only way a web client authenticates without putting the token into the URL and its logs. The token is read only from an actual handshake, before the upgrade; an unauthenticated handshake is refused with `401` and answered with the JSON error `WebsocketUpgradeFailed`. The `access_token` query parameter keeps working.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event/stream" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /event/{eventId}` — Retrieve a single event by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event/{eventId}" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /event/{eventId}` — Delete a single event by id.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event/{eventId}" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /event/list` — List events (paginated, with filters).

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event/list" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /event/list` — Bulk-write events.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event/list" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `DELETE /event/list` — Bulk-delete events.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/event/list" method="delete" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}
