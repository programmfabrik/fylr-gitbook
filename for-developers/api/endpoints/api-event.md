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
