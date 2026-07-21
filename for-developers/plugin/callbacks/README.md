---
description: Callback reference for fylr plugins — the hooks fylr runs during its own API calls, how a callback program is executed, and how data flows in and out.
---

# Callbacks

**Callbacks** are predefined hooks in fylr's API. When fylr handles a save, a workflow transition, a collection upload or an export, it runs the plugin program registered for that hook, hands it the relevant data, and reads back the plugin's result. Each hook has its own input and output format — the sub-pages of this section are the reference, one page per hook:

| Hook | Registered under (manifest) | Runs |
| --- | --- | --- |
| [db\_pre\_save](db-pre-save.md) | `callbacks.db_pre_save` | on every `POST /api/v1/db` save, before objects are written |
| [transition\_db\_pre\_save](transition-db-pre-save.md) | `callbacks.transition_db_pre_save.<name>` | as an action of a workflow transition, before the save |
| [Collection upload](collection-upload.md) | `collection_upload.<name>` (top level) | when files are uploaded into a collection (hotfolder, WebDAV, `/api/v1/eas?collection=…`) |
| [export](export.md) | `callbacks.export.<procedure>` | after an export has produced its files |
| [export\_transport](export-transport.md) | `callbacks.export_transport.<procedure>` | once per transport, after an export has finished |

All hooks share one [callback contract](contract.md) — the `info` map with API URLs and access tokens, the `plugin_user` mechanism, and the error format.

{% hint style="info" %}
**Workflow webhooks** are the plugin-less relatives of these hooks: an HTTP endpoint configured in the base configuration receives the same pre-save payload from a workflow transition — no plugin required. Older versions of this documentation listed them as a manifest callback named `webhook_db_pre_save`; there is no such manifest key. See [Workflow Webhooks](../../../for-administrators/readme/workflow-webhooks.md).
{% endhint %}

## How a callback program runs

Every callback (and every [extension](../extensions.md)) is described by the same [`exec` map](../manifest.md#the-exec-map) in the manifest. fylr runs the program through the [execserver](../../execserver.md): the `service` names the runtime (`node`, `python3`, `exec` for standalone binaries, …), and `commands` lists the programs to run.

* Commands run **sequentially** in a **transient working directory**; the chain stops at the first failing command. The plugin's own files are *not* in that directory — reference them with the `%_exec.pluginDir%` placeholder.
* The **payload arrives on STDIN** when the command declares `stdin: { type: body }`.
* The **response is read from STDOUT** when the command declares `stdout: { type: body }`.
* The **context** (`info` map) can additionally be passed as a command argument with the `%info.json%` placeholder — it is substituted as an **inline JSON string**, not a file path.
* STDERR is not part of the response — programs use it for diagnostics.

```yaml
exec:
  service: "node"
  commands:
    - prog: "node"
      stdin:  { type: body }    # the callback payload, as JSON
      stdout: { type: body }    # the callback response, as JSON
      args:
        - type: "value"
          value: "%_exec.pluginDir%/server/my_callback.js"
```

{% hint style="warning" %}
Older plugins and older versions of this documentation used `stdin: { url: "%_input.url%" }` and `stdout: { url: "%_output.url%" }`. fylr does **not** substitute these placeholders — declare `stdin`/`stdout` with `{ type: body }` as shown above.
{% endhint %}

## Timeouts

A callback job must finish within the configured plugin job timeout — `fylr.execserver.pluginJobTimeoutSec`, default **30 seconds**. A single callback can override this in its manifest entry with `exec.timeout` (a duration string such as `"120s"`) or per command with `timeoutSec`. Waiting for a free execserver slot is bounded separately by `fylr.execserver.connectTimeoutSec` (default 60 seconds).

```yaml
callbacks:
  export:
    md5_sums:
      exec:
        timeoutSec: 120        # this export procedure may take longer
        service: "node"
        commands: [ … ]
```

## Errors

A callback signals an error by exiting non-zero, or by writing an [API-error JSON](../manifest.md#errors) wrapped under a top-level `error` key (in which case a zero exit code is fine). The [callback contract](contract.md#errors) page describes the format; each hook's page describes what an error does to the running operation (a pre-save error aborts the whole save, an export error fails the export, …).

## A minimal callback plugin

`manifest.yml` — register one `db_pre_save` step:

```yaml
plugin:
  name: my_plugin
  displayname:
    en-US: "My Plugin"

callbacks:
  db_pre_save:
    steps:
      - name: "touch every saved object"
        callback: touch
    callbacks:
      touch:
        exec:
          service: "node"
          commands:
            - prog: "node"
              stdin:  { type: body }
              stdout: { type: body }
              args:
                - type: "value"
                  value: "%_exec.pluginDir%/server/touch.js"
```

`server/touch.js` — read the payload, change nothing:

```javascript
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", () => {
  const payload = JSON.parse(input); // { info: {…}, objects: […] }
  console.error(`called for ${payload.objects.length} object(s)`); // diagnostics on STDERR
  console.log(JSON.stringify({ objects: [] })); // empty list: nothing changed
});
```

## Read next

* [The callback contract](contract.md) — the `info` map, access tokens, `plugin_user`, errors.
* [db\_pre\_save](db-pre-save.md) — validate or modify objects on every save.
* [transition\_db\_pre\_save](transition-db-pre-save.md) — hook into workflow transitions.
* [Workflow Webhooks](../../../for-administrators/readme/workflow-webhooks.md) — the same hooks over plain HTTP, without a plugin.
* [Collection upload](collection-upload.md) — participate in hotfolder / WebDAV / collection uploads.
* [export](export.md) and [export\_transport](export-transport.md) — post-process and deliver exports.
* [manifest.yml](../manifest.md) — the `exec` map and placeholders in detail.
