# message

The system data type `message` holds a **notice shown to users** in the web frontend — a banner, modal or toast, optionally scheduled and targeted at specific groups. Messages are managed through the [`/api/v1/message`](../api/endpoints/api-message.md) endpoint.

The mutable payload sits under the `message` key; the addressed groups and read-only system fields sit at the top level.

## Fields

| Field | Format | Description |
| --- | --- | --- |
| `_basetype` | `string` (`message`) | Fixed marker identifying this object as a message. |
| `_groups` | `array<GroupApi>` | Groups the message is addressed to — only their members see it. Empty means all users. |
| `message` | `object` | The message payload. Required: `title`, `message`. |
| `message._id` | `int64` | Server-issued id. Required for updates. |
| `message._version` | `int64` | Object version. Send `1` to create; an update must send the current version + 1, otherwise the save is rejected with `VersionMismatch`. |
| `message.reference` | `string` | Optional unique reference (a stable string id used instead of `_id`). |
| `message.title` | `LocaValue` | Localized title. |
| `message.message` | `LocaValue` | Localized message body. |
| `message.confirmation` | `LocaValue` | Localized confirmation text shown on the acknowledge button. |
| `message.webfrontend_type` | `string` | How the frontend renders the message (`banner`, `modal`, `toast`, …). |
| `message.webfrontend_props` | `object` (map) | Free-form key/value pairs for the frontend. |
| `message.confirm_every_version` | `bool` | If true, a user's confirmation counts only for the exact message version. |
| `message.show_always` | `bool` | If true, the message is shown on every page load until it is confirmed or its `end_time` passes. |
| `message.client_ids` | `array<string>` | Restrict the message to specific frontend client ids. Empty means all clients. |
| `message.start_time` | `object {value: date-time}` (nullable) | When the message becomes visible (UTC, whole seconds). `null` = immediately. |
| `message.end_time` | `object {value: date-time}` (nullable) | When the message stops being visible. Must not precede `start_time`. |
| `_created_at` / `_updated_at` | `date-time` | Create / last-update timestamps. |

## In the API

Messages are read and written through [`/api/v1/message`](../api/endpoints/api-message.md).

`LocaValue` is a localized object keyed by language, e.g. `{ "de-DE": "…", "en-US": "…" }`.
