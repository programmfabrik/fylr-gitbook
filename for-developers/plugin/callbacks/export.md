---
description: The export callback — post-process an export with a plugin. Trigger via produce_options.plugin, the payload, the write-back rules, plugin-produced files, and events.
---

# export

An `export` callback **post-processes an export**: after fylr has produced the export's files, the plugin runs and can rework them, add its own files, write a log, and set the export's final state. Typical uses: packaging into a custom delivery format, generating manifests or checksums, converting metadata.

## Trigger

The export selects the plugin in its `produce_options`:

```json
{ "export": { "produce_options": { "plugin": "fylr_example:md5_sums" } } }
```

`plugin` is `"<plugin-name>:<procedure>"`, and `<procedure>` must be an entry under `callbacks.export` in the [manifest](../manifest.md). The reference is validated when the export is **saved** — an unknown plugin or procedure rejects the export definition.

```yaml
callbacks:
  export:
    md5_sums:
      plugin_user:                 # optional — act as a configured user
        base_config: "user.api_user"
      exec:
        timeoutSec: 120            # exports may exceed the 30 s default
        service: "node"
        commands:
          - prog: "node"
            stdin:  { type: body }
            stdout: { type: body }
            args:
              - { type: "value", value: "%_exec.pluginDir%/server/export/md5_sums.js" }
```

The callback runs inside the background export job — started by `POST /api/v1/export/<id>/start` (which returns immediately) — **after** the regular export has produced its files, and only if the export produced anything.

## The payload

| Property | Description |
| --- | --- |
| `info` | The [callback contract](contract.md) — `config.system` (base config), `config.plugin.<name>`, `api_url`, tokens. |
| `export` | The export in API format, enhanced with internal information. Since 6.28.0, present only if the command does **not** read `stdin` from `body` (see hint). |
| `export._files[n].export_file_internal` | Internal information per file. |
| `plugin_action` | Empty for the export run; set when the request is for a plugin-produced file (see below). |
| `api_callback` | **Backwards compatibility only** — `{ "token", "url" }`, equivalent to `info.api_user_access_token` + `info.api_url`. |

{% hint style="info" %}
**Since 6.28.0** — when the command declares `stdin: { type: body }`, the export JSON is streamed to STDIN as `{ "export": … }` and is **omitted from `%info.json%`**. Large exports no longer have to fit into a command-line argument; new plugins should read the export from STDIN.
{% endhint %}

## The response

Return the modified **export object itself as the top-level JSON document** — note the asymmetry: the payload wraps it (`{ "export": … }` on STDIN), the response does not. It is written back with only a few checks; ids and version must match the original export.

| Property | Description |
| --- | --- |
| `_state` | **Required** — new export status: `done`, `done_with_warnings` or `failed`; any other value is an error. |
| `_plugin_log` | `[]string`, merged into the event fylr writes after the export (see below). |

Per-file, in `export._files[n].export_file_internal`:

| Property | Description |
| --- | --- |
| `hidden` | `true` hides the file from the export API (plugins still see it). |
| `path` | Path appended to `/api/v1/export/<id>/file/`. |
| `content_type` | Content-Type shown over the API. |
| `plugin_action` | Marks the file as **plugin-produced** and is passed back to the plugin when the file is requested. |

## Plugin-produced files

A file entry whose `export_file_internal.plugin_action` is set is not stored — it is **produced on the fly** by the plugin. When a client requests such a file, fylr re-runs the export callback synchronously within the download request, with:

* `plugin_action` — the stored action string, so one procedure can serve several files;
* `info.request` — the client's HTTP request.

Whatever the plugin writes to STDOUT **is the file body**, streamed to the client.

## Events

After the plugin has run, fylr writes the export event: `EXPORT_FINISH` for `done` / `done_with_warnings`, `EXPORT_FAILED` for `failed` or any error — each carrying the returned `_plugin_log`. See the [event type reference](../../../for-administrators/events/event-type-reference.md).

## Example

Add an `md5.txt` listing to every export:

```javascript
// server/export/md5_sums.js (sketch — full version in the fylr example plugin)
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", () => {
  const { export: exp } = JSON.parse(input); // stdin: { export: … }

  // … download the produced files via info.api_url, compute checksums …

  exp._files.push({
    export_file_internal: {
      path: "md5.txt",
      content_type: "text/plain",
      plugin_action: "md5_txt", // produced on the fly by this plugin
    },
  });
  exp._state = "done";
  exp._plugin_log = ["md5.txt added"];

  console.log(JSON.stringify(exp)); // the response is the bare export object
});
```

The full implementation — including serving `plugin_action` requests — ships with the [fylr example plugin](https://github.com/programmfabrik/fylr-plugin-example) (`callbacks.export.md5_sums`).

## See also

* [Export](../../export.md) — the export system itself.
* [export\_transport](export-transport.md) — deliver a finished export somewhere.
* [The callback contract](contract.md) — `info` fields, tokens, `plugin_user`, errors.
