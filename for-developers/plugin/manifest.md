---
description: The manifest.yml that describes a fylr plugin — its keys, the exec map, and the URL replacements a plugin program receives.
---

# manifest.yml

Every plugin has a `manifest.yml` at its root. It names the plugin, declares its frontend assets, and registers what the plugin adds to fylr — [extensions](extensions.md) (custom API endpoints), [callbacks](callbacks/README.md) (hooks), and additions to the base config.

## Top-level keys

| Key | Purpose |
| --- | --- |
| `plugin` | Identity and frontend assets (see below). |
| `base_url_prefix` | Path prefix under which the plugin's frontend assets are served. |
| `extensions` | Custom API endpoints the plugin adds — see [Extensions](extensions.md). |
| `callbacks` | Hooks into fylr's API (db pre-save, transitions, export, …) — see [Callbacks](callbacks/README.md). |
| `collection_upload` | Hooks into collection uploads (hotfolder, WebDAV) — see [Collection upload](callbacks/collection-upload.md). |
| `base_config` | Extra base-config parameters the plugin contributes (e.g. a plugin user). |

### `plugin`

```yaml
plugin:
  name: plugin_name                 # internal, unique plugin name
  displayname:
    en-US: "Name of the Plugin"
  l10n: l10n/loca.csv               # optional localization CSV
  webfrontend:
    url: plugin_name.js             # frontend entry point (optional)
    css: plugin_name.css            # frontend stylesheet (optional)

base_url_prefix: "webfrontend"
```

## The `exec` map

Both `extensions` and `callbacks` describe **how fylr runs the plugin program** with the same `exec` map. fylr runs it through the [execserver](../execserver.md) file-worker tool chain, so the program is any executable the execserver has a `service` for (`node`, `python3`, `exec` for standalone binaries, …).

```yaml
exec:
  service: "node"          # an execserver service
  timeout: "60s"           # optional — default is fylr.execserver.pluginJobTimeoutSec (30 s)
  commands:
    - prog: "node"
      stdin:
        type: body         # fylr streams the input data to STDIN …
      stdout:
        type: body         # … and reads the result from STDOUT
      args:
        - type: "value"
          value: "%_exec.pluginDir%/server/dump_info.js"
        - type: "value"
          value: "%info.json%"
```

`stdin: { type: body }` delivers the call's input data on STDIN; `stdout: { type: body }` makes STDOUT the response. The commands of one `exec` run sequentially in a shared, transient working directory — the plugin's own files are only reachable via `%_exec.pluginDir%`.

### Placeholders

fylr substitutes these placeholders in the `exec` map before running the program:

| Placeholder | Description |
| --- | --- |
| `%info.json%` | The **context** of the call as an **inline JSON string** (not a file path — parse the argument directly): the request, the plugin's base config, and the [callback contract](callbacks/contract.md) fields. Individual callbacks add more keys. |
| `%_exec.pluginDir%` | Absolute filesystem path of the plugin's directory. Use it to reference scripts and other plugin resources — without it, paths resolve relative to the transient per-job working directory, where the plugin's files do not exist. |
| `%_exec.workDir%` | Absolute path of the transient per-job working directory. |
| `%_exec.GOOS%`, `%_exec.GOARCH%` | Operating system and architecture of the executing execserver — for shipping per-platform binaries (`hello-%_exec.GOOS%-%_exec.GOARCH%.exe`). |

{% hint style="warning" %}
Older plugins and older versions of this documentation used `stdin: { url: "%_input.url%" }` and `stdout: { url: "%_output.url%" }`. fylr does **not** substitute these placeholders — declare `stdin`/`stdout` with `{ type: body }` instead.
{% endhint %}

## Errors

To signal an error, a plugin program either **exits with a non-zero exit code**, or writes an API-error JSON. When wrapped under a top-level `error` key, a zero exit code is fine:

```json
{
  "error": {
    "code": "error.code",      // defined in the plugin's l10n
    "parameters": {},          // values for the localized message
    "realm": "api",            // used by the frontend for display
    "statuscode": 400          // optional HTTP status for the API response
  }
}
```

When called as an [extension](extensions.md), fylr sets the `X-Execserver-Error` header on failure — unless more than 4&nbsp;KB of the response body have already been sent.

## Full example

```yaml
plugin:
  name: fylr_example
  displayname:
    en-US: "fylr Example"
  webfrontend:
    url: fylr_example.js

base_url_prefix: "webfrontend"

extensions:
  dump/info:                         # -> /api/v1/plugin/extension/fylr_example/dump/info
    exec:
      service: "node"
      commands:
        - prog: "node"
          stdin:  { type: body }
          stdout: { type: body }
          args:
            - { type: "value", value: "%_exec.pluginDir%/server/dump_info.js" }
            - { type: "value", value: "%info.json%" }

callbacks:
  db_pre_save:
    steps:
      - name: "set comment for bilder"
        callback: set_comment
        filter:
          type: objecttype
          objecttypes: [ bilder ]
    callbacks:
      set_comment:
        exec:
          service: "node"
          commands:
            - prog: "node"
              stdin:  { type: body }
              stdout: { type: body }
              args:
                - { type: "value", value: "%_exec.pluginDir%/server/set_comment.js" }

# extra base config — here a plugin user the callbacks can act as
base_config:
  - name: user
    parameters:
      api_user:
        type: user
```

## See also

* [Extensions](extensions.md) — add custom API endpoints.
* [Callbacks](callbacks/README.md) — hook into db saves, transitions, collection uploads, export.
* [Custom Data](../customdata.md) — plugins that add custom data types.
* [Plugin Conventions and Standards](conventions.md) and [Packaging and Release](release.md).
