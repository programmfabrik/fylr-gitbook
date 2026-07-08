# event

The system data type `event` is a single entry in fylr's **event log** — a record that something happened: an object was created or updated, a user logged in, an email was sent. Events are append-only and read through the [`/api/v1/event`](../api/endpoints/api-event.md) endpoint (list and poll). Their monotonically increasing `_id` is the cursor for consuming the stream.

The event payload sits under the `event` key; a snapshot of the acting principal sits under `user`.

## Fields

| Field | Format | Description |
| --- | --- | --- |
| `_basetype` | `string` (`event`) | Fixed marker identifying this object as an event. |
| `event` | `object` | The event payload. Required: `_id`, `timestamp`. |
| `event._id` | `int64` | Server-issued, monotonically increasing event id. Used as the poll cursor. |
| `event.type` | `string` | The event type, e.g. `OBJECT_UPDATE`, `COLLECTION_INSERT`, `USER_LOGIN`, `EMAIL_SENT`. This is an open set — see the [Event Type Reference](../../for-administrators/events/event-type-reference.md). |
| `event.timestamp` | `date-time` | UTC time the event was written. |
| `event.basetype` | `string` | Basetype of the affected entity (`object`, `collection`, `user`, `group`, …). |
| `event.objecttype` | `string` | Objecttype name when `basetype` is `object`. |
| `event.schema` | `string` | Datamodel schema the event was recorded under (`user`, `system`, …). |
| `event.object_id` | `int64` | Per-objecttype object id. Omitted for system-level events. |
| `event.object_version` | `int64` | Object version at the time the event was written. |
| `event.system_object_id` | `int64` | The fylr-internal `_system_object_id` (unique across objecttypes). |
| `event.global_object_id` | `string` | Cross-objecttype identifier `<objecttype>:<object_id>`. |
| `event.info` | `object` (map) | Event-specific structured payload. The keys depend on `type` (documented per type in the Event Type Reference). |
| `event.pollable` | `bool` | Whether the event is surfaced through the long-poll / stream endpoints (versus only `/event/list`). |
| `event.remote_addr` | `string` | IP address of the request that produced the event, when available. |
| `event.user_generated_displayname` | `string` | Rendered display name of the acting user, snapshotted at event time. |
| `user` | `object` (`WhoApi`) | Snapshot of the user or group that produced the event. Omitted for system events. |

## In the API

Events are read through [`/api/v1/event`](../api/endpoints/api-event.md); the per-type meaning of the `info` keys is documented in the [Event Type Reference](../../for-administrators/events/event-type-reference.md). Consuming the stream reliably is covered under [Search and events](../concepts/search-and-events.md).
