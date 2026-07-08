---
description: Callback reference for fylr plugins — the hooks fylr runs during its own API calls (db pre-save, transitions, webhooks, export, export transport), the unified contract, and how to call back into the API.
---

# Callbacks

**Callbacks** are predefined hooks in fylr's API. When fylr handles a save, a transition or an export, it runs the plugin program you registered for that hook, hands it the relevant data, and reads back the plugin's result. Each hook has its own input and output format — this page is the reference.

Callbacks are registered under `callbacks` in the [manifest](manifest.md), using the same [`exec` map](manifest.md#the-exec-map) as extensions.

| Callback | Runs | Purpose |
| --- | --- | --- |
| `db_pre_save` | on `POST /api/v1/db`, before objects are written | validate or modify objects before they are saved |
| `transition_db_pre_save/<type>` | inside a configured transition | the transition's own pre-save hook |
| `webhook_db_pre_save` | on a webhook-driven save | pre-save hook for webhook saves |
| `export/<procedure>` | after `POST /api/v1/export/<id>/start` | post-process an export |
| `export_transport` | after an export finishes, per transport | deliver the export somewhere |

## Errors

A callback signals an error by exiting non-zero, or by writing an [API-error JSON](manifest.md#errors) wrapped under a top-level `error` key (in which case a zero exit code is fine).

## Calling back into the API

Most callbacks run server-side in the file-worker tool chain and frequently need to call back into the fylr API — to read the base config, load or write objects. For this, every callback receives the same set of fields, the **unified callback contract**, independent of which hook runs:

| Property | Presence | Description |
| --- | --- | --- |
| `api_url` | always | Base URL to call back into the API. Append `/api/v1/…` to reach an endpoint. |
| `api_user_access_token` | always | OAuth2 access token to call the API **as the user the current API call runs as**. |
| `api_user` | always | The current API user (the `who`). |
| `plugin_user_access_token` | only if configured | Access token of the configured **plugin user**. Present only if the manifest entry declares a `plugin_user`. If the plugin user resolves to the current API user, it equals `api_user_access_token`. |
| `plugin_user` | only if configured | The plugin user (the `who`) for `plugin_user_access_token`. |
| `api_tx_url` | only inside a save transaction | Base URL for the [transactional `/db` surface](#writing-inside-the-save-transaction-api_tx_url): calls back **into the open write transaction** the callback runs in. Present for the `db_pre_save` family, absent for extensions and exports. |

A callback therefore always gets a token for the **current API user**, and *additionally* a token for the **plugin user** when one is configured — never one *or* the other.

{% hint style="info" %}
**These tokens are unbound and short-lived.** fylr binds a browser session token to the browser via the `fylr-browser-id` cookie, so a plugin replaying the user's own token server-side — without that cookie — would be rejected by session binding. fylr therefore hands the plugin freshly issued, **session-binding-free** tokens that work for the cookieless server-to-server callback and are revoked once the callback returns. Treat them as short-lived; do not persist them.
{% endhint %}

**Where the fields live in the payload**

* For **extensions** the payload *is* the info map, so the fields are at the top level: `api_user_access_token`, `api_url`, …
* For **db\_pre\_save**, **transition\_db\_pre\_save** and **export** the payload also carries the hook's own data (the object list, the export object), so the contract fields live under the `info` key: `info.api_user_access_token`, `info.api_url`, …

Using them from a callback program:

```javascript
// load the base config as the plugin user, if one is configured
const info = JSON.parse(fs.readFileSync(process.argv[process.argv.length - 1], "utf8")).info;
const token = info.plugin_user_access_token ?? info.api_user_access_token;

const cfg = await fetch(`${info.api_url}/api/v1/config`, {
  headers: { Authorization: `Bearer ${token}` },
}).then((r) => r.json());
```

{% hint style="warning" %}
**export — backwards compatibility:** the export payload additionally contains a legacy `api_callback` map (`{ "token", "url" }`) equivalent to `info.api_user_access_token` + `info.api_url`. It is kept so existing export plugins keep working; **new export plugins should use the unified contract fields above.**
{% endhint %}

## Writing inside the save transaction: `api_tx_url`

A `db_pre_save` callback runs **while the save's write transaction is open**. A call to the regular `api_url` therefore arrives on a *separate* database connection:

* it cannot see the uncommitted data of the save it is part of, and
* on a **single-writer backend (SQLite)** it cannot write at all while the save's transaction holds the write lock — such a write fails with `423 DatabaseLockError`.

For this, callbacks of the `db_pre_save` family (`db_pre_save`, `transition_db_pre_save/<type>`, `webhook_db_pre_save`) additionally receive `info.api_tx_url`: a base URL whose requests are executed **inside the very transaction the callback runs in**. It is a drop-in for `api_url` — append the same `db/…` paths — but deliberately scoped to the transactional `/db` surface:

| Method & path | Purpose |
| --- | --- |
| `POST {api_tx_url}/db/<objecttype>` | insert / update objects |
| `GET {api_tx_url}/db/<objecttype>/<mask>/<id>` | load an object (sees the transaction's uncommitted state) |
| `DELETE {api_tx_url}/db/<objecttype>` | delete objects |

Everything that is not part of the save itself — config, search, files — has no business inside the transaction; use `api_url` for those.

**Semantics**

* Only the tokens handed to *this* callback (`api_user_access_token`, `plugin_user_access_token`) are accepted on `api_tx_url`. The URL is valid only while the callback runs and is revoked when it returns.
* Writes join the save's transaction via a savepoint: they become visible to the rest of the save immediately, and they **commit or roll back together with the surrounding save**. If the save fails after your callback returned, your writes are rolled back with it.
* `api_tx_url` behaves identically on PostgreSQL and SQLite. Plugins that must run on both backends can simply prefer it for writes from a `db_pre_save` callback.

A robust pattern for existing plugins — try the regular API first, fall back to the transaction on a lock error:

```python
resp_text, statuscode = post_to_api(api_url, 'db/linked_object', token, payload)
if statuscode == 423:
    # single-writer backend: the save's transaction holds the write lock —
    # retry INSIDE that transaction
    api_tx_url = info.get('api_tx_url')
    if api_tx_url:
        resp_text, statuscode = post_to_api(api_tx_url, 'db/linked_object', token, payload)
```

## `db_pre_save`, `transition_db_pre_save/<type>`, `webhook_db_pre_save`

This callback runs for each `POST /api/v1/db` request (or inside a configured transition). It can validate or modify the objects before they are written.

* In group mode the payload consists of all individual objects loaded from the database.
* Each object includes the currently stored object under the top-level key `_current`, if available.
* Each object carries a `_callback_context` at the top level. **`_callback_context.hash` must be returned** in the response to update the object — **only returned objects are updated**.
* Returned objects only update the user values, comment, pool, tags and rights. Other fields — especially any ids — are not updated.
* The callback receives reverse and bidirectional linked objects at the top level of the object list. The callback must deal with them, or not return them. For bidirectional objects, returning only one side can lead to incomplete objects.
* The `_all_fields` mask is used to render the JSON for the plugin; the plugin must return the data using `_all_fields`. `_callback_context.original_mask` holds the mask used in the posted object.
* For **inserted** objects ids are not yet set, so `_uuid`, `_global_object_id`, `_system_object_id` and `<object>._id` are unset; `<object>._id_parent` may be `0` for an as-yet-unknown parent (e.g. in a reverse-hierarchy context).
* For transitions the `transition.type` is `<plugin-name>:<transition-type>`.
* `db_pre_save` uses a `steps` list to run multiple callbacks in order; each step can filter by objecttype.

Example — set a comment on every saved `bilder` object:

```javascript
// set_comment.js
const fs = require("fs");
const payload = JSON.parse(fs.readFileSync("/dev/stdin", "utf8")); // objects from %_input.url%

const objects = payload.objects.map((o) => ({
  // echo back the hash so fylr applies the update
  _callback_context: { hash: o._callback_context.hash },
  _objecttype: o._objecttype,
  _mask: "_all_fields",
  _comment: "reviewed by the set_comment plugin",
  bilder: o.bilder, // user values, unchanged
}));

process.stdout.write(JSON.stringify({ objects }));
```

The matching manifest entry is shown in [manifest.yml → full example](manifest.md#full-example).

## `export/<procedure>`

Called by `POST /api/v1/export/<id>/start` **after** the regular export has run. The export must set `produce_options.plugin` to `<plugin-name>:<procedure>`, and `<procedure>` must be an entry under `callbacks.export` in the manifest.

The frontend part of the plugin sets:

```json
{ "export": { "produce_options": { "plugin": "fylr_example:demo" } } }
```

which runs the manifest entry:

```yaml
export:
  demo:
    plugin_user:
      base_config: "user.api_user"   # path in the base config
    exec:
      service: "node"
      commands:
        - prog: "node"
          stdin:  { type: body }     # since 6.28.0 the export JSON is sent on stdin
          stdout: { type: body }
          args:
            - { type: "value", value: "export_demo.js" }
            - { type: "value", value: "%info.json%" }
```

Behaviour:

* The payload carries general info (base config in `info.config`) and the `info.export` object.
* The plugin writes back the `export` object and may modify it.
* `export.files` are read back, but only their internal representation `export._files[n].export_file_internal`. Set `hidden = true` there to keep a file out of the export API.
* The plugin must set `export._state` to `done`, `done_with_warnings` or `failed`. `failed` produces an `EXPORT_FAILED` event; the others produce `EXPORT_FINISH`.
* An `export._plugin_log` (`[]string`) is merged into that event.
* The plugin can create its own file entries; fylr calls back into the plugin per file, passing `export.files[n].export_file_internal.plugin_action` as `info.plugin_action`. Additional plugin files are created on the fly.

### Payload (`%info.json%`)

| Property | Description |
| --- | --- |
| `info.config.system` | Base config of the instance. |
| `info.request` | Information about the request. |
| `export` | The export in API format, enhanced with internal information. Since 6.28.0, present only if the command does **not** read `stdin` from `body`. |
| `export._files[n].export_file_internal` | Internal information per file. |
| `plugin_action` | Set when the request is for a plugin-exported file. |
| `info.api_user_access_token`, `info.api_url`, `info.api_user`, `info.plugin_user_access_token`, `info.plugin_user` | The [unified callback contract](#calling-back-into-the-api). |
| `api_callback` | **Backwards compatibility only** — `{ "token", "url" }`, equivalent to `info.api_user_access_token` + `info.api_url`. |

### Return payload

Return everything from `info.export` under `export` (omit the `info` level). It is written back to the database as is, with only a few checks. `info.export._log` is read-only and need not be returned.

| Property | Description |
| --- | --- |
| `_state` | New export status: `done`, `done_with_warnings`, or `failed`. |
| `_plugin_log` | `[]string` merged into the event fylr writes after the plugin ran. |

Per-file, in `export._files[n].export_file_internal`:

| Property | Description |
| --- | --- |
| `hidden` | `true` hides the file from the external export API (the plugin still sees it). |
| `path` | Path appended to `/api/v1/export/[n]/file`. |
| `content_type` | Content-Type shown over the API (the actually-sent type is auto-detected). |
| `plugin_action` | Custom action string passed back to the plugin when the file is requested. |

## `export_transport`

Runs after the regular export finishes, once **per transport**. The transport plugin receives the same payload as an `export` plugin plus a `transport` object:

| Property | Description |
| --- | --- |
| *all properties from **export*** | |
| `transport` | The transport object, with everything needed for the transport. |
| `transport.options` | Configuration settings for the transport. |

### Return payload

The transport reports whether it succeeded and may add information to the event fylr writes; nothing else needs to be returned.

| Property | Description |
| --- | --- |
| `_state` | New status: `done`, `done_with_warnings`, or `failed`. |
| `_transport_log` | `[]string` merged into the event fylr writes after the plugin ran. |

## See also

* [manifest.yml](manifest.md) — register callbacks, the `exec` map.
* [Extensions](extensions.md) — custom API endpoints (as opposed to hooks).
* [Anatomy of a Record](../record-json.md) — the object JSON a `db_pre_save` callback receives and returns.
* [Events and webhooks](../events-and-webhooks.md) — the push/pull integration alternatives to synchronous callbacks.
