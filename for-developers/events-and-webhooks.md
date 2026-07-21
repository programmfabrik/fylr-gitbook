---
description: >-
  Build integrations on fylr — pull the event stream, receive a real-time
  WebSocket push, get an outbound workflow webhook, or run a synchronous plugin
  callback. When to use each.
---

# Events and Webhooks

fylr records what happens — an object created, a user logged in, a backup finished — in its **event log**. There are four ways to build an integration on top of that, from a client that polls on its own schedule to a hook that runs inside fylr's own transaction:

| Way | Direction | Delivery | Use it when |
| --- | --- | --- | --- |
| [`/event/poll`](#pull-poll-the-event-stream) | pull | durable, immediate | a client reconciles state on its own schedule and must not miss events |
| [`/event/list`](#pull-poll-the-event-stream) | pull | durable, filtered | you need rich filters or a CSV export of events |
| [`/event/stream`](#push-the-websocket-stream) | push | real-time, not durable | a live UI that can tolerate a dropped event |
| [Workflow webhook](#push-outbound-workflow-webhooks) | push | outbound HTTP | notify (or gate) on a workflow transition of records |
| [Plugin callback](#synchronous-plugin-callbacks) | synchronous | in-transaction | validate or enrich an object as it is saved |

## Pull: poll the event stream

`GET /api/v1/event/poll/{fromEventId}` returns the pollable events **after** a cursor. The cursor is the event `_id`: the query is `id > fromEventId ORDER BY id`, run once and returned immediately — it is **not** a long-poll. To read from the beginning, call `/event/poll/0`.

* `fromEventId` — the required path segment; the largest `_id` you have already seen.
* `limit` — query param, default `25`; values `≤ 0` or `> 1000` are forced to `1000`.

The response is a plain array of [event](system-data-types/event.md) objects. Advance by taking the largest `event._id` from the batch and passing it as the next `fromEventId`:

```bash
# first call — from the start
curl -H "Authorization: Bearer $TOKEN" \
  "https://fylr.example.com/api/v1/event/poll/0?limit=100"

# next call — from the last id you saw
curl -H "Authorization: Bearer $TOKEN" \
  "https://fylr.example.com/api/v1/event/poll/4711?limit=100"
```

Only events flagged **pollable** are returned (most object, user, group, pool, tag, collection, transition, datamodel and index events; login/download/export/file-produce events generally are not). The per-type flag is listed in the [Event Type Reference](../for-administrators/events/event-type-reference.md).

`POST /api/v1/event/list` (also `GET`) is the richer alternative: it filters by `type`, `basetype`, `object_id`, `user_id`, date range and more, sorts, pages, and can return CSV. It answers with a `{ count, limit, offset, objects }` wrapper.

Polling needs an authenticated session; `/poll` requires any user, `/list` requires the `system.api.event` (get) right.

## Push: the WebSocket stream

`GET /api/v1/event/stream` upgrades to a **WebSocket** and pushes each new pollable event as JSON in real time. A client "subscribes" simply by opening the socket.

This channel is **not durable**: events are held in an in-memory buffer per listener and are **dropped if the client cannot keep up**. Use it for live UIs; use `/event/poll` when you must not miss an event. (Streamed events also omit the top-level acting `user`; where that matters, the id is carried inside the event's `info`.)

## Push: outbound workflow webhooks

A **workflow webhook** is fylr calling **out** to your server when a [workflow transition](concepts/tags-and-transitions.md) runs on records. It is not driven by the event log — it is a **Webhook** action on a transition.

* Configure the endpoints in the base config (a `webhooks` table: `name`, `url`, `secret`, `timeout`, `send_authorization_header`, `include_access_token`), then reference one by `name` from a transition's Webhook action.
* **Modes:** `after_commit_async` (the default — fire-and-forget notification after the save commits) or `pre_save` (synchronous, runs before the save and can modify or abort it — the same contract as the `db_pre_save` plugin callback).
* fylr sends a JSON `POST` of `{ info, objects }`. With a `secret` the body is HMAC-signed in `X-Hub-Signature` / `X-Hub-Signature-256`; `send_authorization_header` adds a bearer token. The async outcome is itself logged as a `WEBHOOK` or `WEBHOOK_ERROR` event.

The full configuration and payload reference is on [Workflow Webhooks](../for-administrators/readme/workflow-webhooks.md).

## Synchronous plugin callbacks

For logic that must run **inside** the save — validate a value, compute a field, block a bad write — a [plugin callback](plugin/callbacks/README.md) (`db_pre_save`, `transition_db_pre_save`, `export`, …) is the tightest coupling: it runs in the request's transaction, receives the objects, and returns the modified ones. See [Plugin → Callbacks](plugin/callbacks/README.md).

## See also

* [event (system data type)](system-data-types/event.md) — the shape of an event.
* [Event Type Reference](../for-administrators/events/event-type-reference.md) — every event type, its trigger, its `info` keys, and whether it is pollable.
* [`/api/v1/event`](api/endpoints/api-event.md) — the endpoint reference.
* [Workflow Webhooks](../for-administrators/readme/workflow-webhooks.md) — configuring outbound webhooks.
