---
description: The manifest.yml that describes a fylr plugin — its keys, the exec map, and the URL replacements a plugin program receives.
---

# manifest.yml

Every plugin has a `manifest.yml` at its root. It names the plugin, declares its frontend assets, and registers what the plugin adds to fylr — [extensions](extensions.md) (custom API endpoints), [callbacks](callbacks.md) (hooks), and additions to the base config.

## Top-level keys

| Key | Purpose |
| --- | --- |
| `plugin` | Identity and frontend assets (see below). |
| `base_url_prefix` | Path prefix under which the plugin's frontend assets are served. |
| `extensions` | Custom API endpoints the plugin adds — see [Extensions](extensions.md). |
| `callbacks` | Hooks into fylr's API (db pre-save, transitions, export, …) — see [Callbacks](callbacks.md). |
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

Both `extensions` and `callbacks` describe **how fylr runs the plugin program** with the same `exec` map. fylr runs it through the [execserver](../execserver.md) file-worker tool chain, so the program is any executable the execserver has a `service` for (`node`, `python`, …).

```yaml
exec:
  service: "node"          # an execserver service
  commands:
    - prog: "node"
      stdin:
        url: "%_input.url%"   # fylr serves the input data at this URL …
      stdout:
        method: "POST"        # … and the program POSTs its result back here
        url: "%_output.url%"  # (POST is the default)
      args:
        - type: "value"
          value: "dump_info.js"
        - type: "value"
          value: "%info.json%"
```

A command can also read its input from, or write its result to, the request **body** directly by setting `stdin: { type: body }` / `stdout: { type: body }` instead of a URL.

### URL replacements

fylr substitutes these placeholders in the `exec` map before running the program:

| Replacement | Description |
| --- | --- |
| `%_input.url%` | URL of an HTTP endpoint serving the **input** data for this call. Map it to STDIN, or read it directly. |
| `%_output.url%` | URL to write the **result** back to. Map it to STDOUT, or write to it directly. |
| `%info.json%` | A map of **context** about the call: the requested URL and its parsed query, the HTTP headers, the plugin's base config (as returned by `/api/config`), and — since 6.17 — the configured languages. Individual callbacks add more keys. |

## Errors

To signal an error, a plugin program either **exits with a non-zero exit code**, or writes an API-error JSON. When wrapped under a top-level `error` key, a zero exit code is fine:

```json
{
  "error": {
    "code": "error.code",   // defined in the plugin's l10n
    "err": "error string",
    "params": {},            // values for the localized message
    "realm": "api"           // used by the frontend for display
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
          stdin:  { url: "%_input.url%" }
          stdout: { url: "%_output.url%" }
          args:
            - { type: "value", value: "dump_info.js" }
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
              stdin:  { url: "%_input.url%" }
              stdout: { url: "%_output.url%" }
              args:
                - { type: "value", value: "set_comment.js" }
                - { type: "value", value: "%info.json%" }

# extra base config — here a plugin user the callbacks can act as
base_config:
  - name: user
    parameters:
      api_user:
        type: user
```

## See also

* [Extensions](extensions.md) — add custom API endpoints.
* [Callbacks](callbacks.md) — hook into db saves, transitions, export.
* [Custom Data](../customdata.md) — plugins that add custom data types.
* [Plugin Conventions and Standards](conventions.md) and [Packaging and Release](release.md).
