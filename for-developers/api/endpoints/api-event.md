# /api/v1/event

Read, write and subscribe to **events**. fylr writes events for many
server-side mutations (object insert/update, collection changes,
file deletes, email sends, ...). This endpoint exposes the event log.

### `POST /event` — Write a single user event.
{% swagger src="./fylr-openapi.yml" path="/event" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /event/poll/{fromEventId}` — Fetch pollable events newer than an event id.
{% swagger src="./fylr-openapi.yml" path="/event/poll/{fromEventId}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /event/stream` — WebSocket stream of new events.
{% swagger src="./fylr-openapi.yml" path="/event/stream" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /event/{eventId}` — Retrieve a single event by id.
{% swagger src="./fylr-openapi.yml" path="/event/{eventId}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /event/{eventId}` — Delete a single event by id.
{% swagger src="./fylr-openapi.yml" path="/event/{eventId}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /event/list` — List events (paginated, with filters).
{% swagger src="./fylr-openapi.yml" path="/event/list" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /event/list` — Bulk-write events.
{% swagger src="./fylr-openapi.yml" path="/event/list" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /event/list` — Bulk-delete events.
{% swagger src="./fylr-openapi.yml" path="/event/list" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
