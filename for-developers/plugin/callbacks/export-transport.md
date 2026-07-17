---
description: The export_transport callback — deliver a finished export with a plugin. Transports on the export, the payload with decrypted options, the response, and events.
---

# export\_transport

An `export_transport` callback **delivers a finished export** — to an FTP server, a WebDAV share, an external API, wherever. Transports run after the export (and a possible [export callback](export.md)) have finished, **once per configured transport**.

## Transports on the export

Transports are part of the **export definition**, submitted in its `_transports` array:

```json
{
  "export": {
    "name": "delivery",
    "_transports": [
      {
        "plugin": "fylr_example:copy_file",
        "options": { "url": "https://target.example.com/inbox", "pw:secret": "…" }
      }
    ]
  }
}
```

| Field | Description |
| --- | --- |
| `plugin` | `"<plugin-name>:<procedure>"` — an entry under `callbacks.export_transport` in the [manifest](../manifest.md). Empty for a plain download transport (no plugin runs). |
| `options` | Free-form configuration for the transport. Stored encrypted; keys prefixed `pw:` are treated as secrets. |
| `email` | Optional — fylr sends a notification mail after the transport. |

The manifest side:

```yaml
callbacks:
  export_transport:
    copy_file:
      exec:
        timeoutSec: 60
        service: "node"
        commands:
          - prog: "node"
            stdin:  { type: body }
            stdout: { type: body }
            args:
              - { type: "value", value: "%_exec.pluginDir%/server/export_transport/copy_file.js" }
```

## The payload

The transport plugin receives the same payload as an [export plugin](export.md#the-payload), plus the transport:

| Property | Description |
| --- | --- |
| *all properties from **export*** | Including the `export` object — on STDIN as `{ "export": … }` when the command declares `stdin: { type: body }`, otherwise inside `%info.json%`. |
| `transport` | The transport object, with `options` **decrypted** — including `pw:`-prefixed secrets. |

## The response

The transport reports whether it succeeded and may add log lines to the event fylr writes; nothing else is read back:

| Property | Description |
| --- | --- |
| `_state` | **Required** — `done`, `done_with_warnings` or `failed`. |
| `_transport_log` | `[]string`, merged into the transport event. |

A **failed transport does not abort the export** — the export itself degrades to `done_with_warnings`, and fylr writes an `EXPORT_TRANSPORT_FAILED` event (successful transports write `EXPORT_TRANSPORT_FINISH`), each carrying the `_transport_log` — see the [event type reference](../../../for-administrators/events/event-type-reference.md).

## Example

Send the export's files to the URL configured in the transport options:

```javascript
// server/export_transport/copy_file.js (sketch — full version in the fylr example plugin)
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", async () => {
  const { export: exp } = JSON.parse(input); // stdin: { export: … }
  const info = JSON.parse(process.argv[2]);  // %info.json% — carries transport
  const opts = info.transport.options;

  const log = [];
  for (const file of exp._files) {
    // … download via info.api_url, upload to opts.url …
    log.push(`sent ${file.export_file_internal.path} to ${opts.url}`);
  }

  console.log(JSON.stringify({ _state: "done", _transport_log: log }));
});
```

The full implementation ships with the [fylr example plugin](https://github.com/programmfabrik/fylr-plugin-example) (`callbacks.export_transport.copy_file`).

## See also

* [export](export.md) — post-process the export before it is delivered.
* [Export](../../export.md) — the export system itself.
* [The callback contract](contract.md) — `info` fields, tokens, errors.
