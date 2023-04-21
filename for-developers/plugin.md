---
label: Plugin
description: >-
  Plugins can be used to extend fylr with custom data types, custom API
  endpoints, custom frontend snippets and more...
---

# Plugin

Plugins can be integrated into many API calls of FYLR using a callback system thru the file worker tool chain.

A plugin consists of a _manifest.yml_ and can include an arbritary tree of files and directory as resources.

The config **fylr.yml** needs to be configured to load each individual plugin or a directory containing multiple plugins.

Plugins may be packed into a .zip file, if they are FYLR serves the data from within the ZIP unpacking files on the fly.

Configured callbacks use replacements for specific URL to receive and send data.

![img](../reference/camera.jpg)

| Replacement     | Description                                                                                                                                                                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `%_input.url%`  | The URL pointing to an HTTP endpoint sending out the input data for the plugin. This can be mapped to STDIN or read directly by the plugin.                                                                                                                                                      |
| `%_output.url%` | The URL to write the data back to. This can be mapped to STDOUT or written directly by the plugin.                                                                                                                                                                                               |
| `%info.json%`   | A map containg context information about the current callback. This includes the URL requested, its query in a parsed form, as well as the HTTP Headers of the request. In addition it includes the base config as returned by /api/config. Individual callbacks may add additional information. |

When a plugin wants to return an error, it needs to exit with a non zero exit code. If called as an extension plugin, FYLR sets the `X-Execserver-Error` header, unless more than 4K of data have already been produce and sent out to the response body.

## Format of manifest.yml

```yml
l10n: l10n/loca.csv
webfrontend:
  l10n: l10n/
extensions:
  dump/info:
    exec:
      service: "node"
      commands:
        - prog: "node"
          stdin:
            url: "%_input.url%"
          stdout:
            method: "POST" # method to write the data back, FYLR expects "POST" (also the default)
            url: "%_output.url%"
          args:
            - type: "value"
              value: "dump_info.js"
            - type: "value"
              value: "%info.json%"
callbacks:
  transition_db_pre_save:
    set_comment:
      exec:
        service: "node"
        commands:
          - prog: "node"
            stdin:
              url: "%_input.url%"
            stdout:
              url: "%_output.url%"
            args:
              - type: "value"
                value: "set_comment.js"

  db_pre_save:
    steps:
      - name: "set comment for bilder"
        callback: set_comment
        filter:
          type: objecttype
          objecttypes:
            - bilder
    callbacks:
      set_comment:
        exec:
          service: "node"
          commands:
            - prog: "node"
              stdin:
                url: "%_input.url%"
              stdout:
                url: "%_output.url%"
              args:
                - type: "value"
                  value: "set_comment.js"
                - type: "value"
                  value: "%info.json%"

  export:
    create_pptx:
      exec:
        service: "python"
        commands:
          - prog: "python"
            stdout:
              type: body
            args:
              - type: "value"
                value: "pptx_test.py"
              - type: "value"
                value: "%info.json%"

```

| Parameter   | Description                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------- |
| `l10n`      | Path to localization file in FYLR format (CSV). The keys are merged into `/api/v1/l10n/static/<lang>.json`. |
| `callbacks` | Definition of callbacks.                                                                                    |

## Extensions

Extensions add API endpoints to the base url of the plugin. The name of the endpoint is the key in the prodived map `extensions` in the plugin manifest. The `exec` map is identical to Callbacks. The map specifies how the file worker chain is called to execute the extension.

The plugin must use the provided `/writer` endpoint (replacement `%_output.url%`) to transport data back to the request. If used directly, all http headers sent to that endpoint are copied over to the response of the extension endpoint. The http response status can be set using the special response header `x-fylr-response-status`.

If STDOUT is used to write back to the endpoint, no custom headers or status can be sent. However, if the plugin returns less than **2048** bytes, the exit code will be checked. If not **0** the status of the response is set to 500 (InternalServerError).

FYLR adds timing information to the response header.

In case of an error, fylr tries to parse errors using the api error format. If a statuscode is given and headers have not been sent out yet (which happens after the 4K buffer is full), the http status is set to the code in the error.

```json
{
  "code": "error.code", // define in l10n
  "err": "error string",
  "params": {}, // map to ender the error code localization
  "realm": "api", // this should always be "api"
  "statuscode": 400 // an optional status code
}
```

## Callbacks

Callbacks are predefined hooks in the API of FYLR. Each hook is different and might use its own format for in and output of the data.

Errors can be generated using the api error JSON format which looks like this:

```json
{
  "error": {
    "code": "error.code", // define in l10n
    "err": "error string",
    "params": {}, // map to ender the error code localization
    "realm": "api", // this default to "api" (used by the frontend for display)
  }
}
```

It is not necessary to end the plugin with an error exit code in case the error is wrapped under a top level key `error` as shown in the example.

### db\_pre\_save, transition\_db\_pre\_save/\<transition-type>, webhook\_db\_pre\_save

This callback is run for each **POST /api/db** request or inside a configured transition.

* In group mode the payload consists of all individual objects loaded from the database.
* Each object includes the object from the database in the top level key `_current`, if available.
* Each object includes a `_callback_context` on the top level. \_`callback_context.hash` must be returned in the response in order to update the object property. Only returned objects are updated.
* Returned objects only update all user values, Comment, Pool, Tags and Rights. Other fields (especially any IDs) are not updated.
* The callback receives reverse and bidirectional added objects on top level of the object list. The callback must deal with these objects, or not return them. In case of bidirectional objects, this might lead to incomplete objects if only one side of the bidi object is changed.
* The `_all_fields` mask is used to render the JSON for the plugin. The plugin must return the data using the `_all_fields` mask. `_callback_context.original_mask` contains the mask used in the posted object.
* For inserted objects, IDs are not yet set, so `_uuid`, `_global_object_id`, `_system_object_id`, `<object>._id` are unset. `<object>._id_parent` may be **0**, if it has a yet unknown parent ID (this can happen if the object was delivered in a reverse hierarchy context).
* For transitions, the corresponding `transition.type` is `<plugin-name>:<transition-type>`.
* `db_pre_save` uses a `steps` semantic to run multiple callbacks in order. A filter by objecttype can be applied to each individual step.

### export/\<procedure>

This callback is called by **POST /api/export/\<id>/start** start after regular export has run.

In order to start the plugin for the export, the export needs a `produce_options.plugin` to be set.

It takes the form of `<plugin-name>:<procedure>`. The `<procedure>` needs to be configured in `manifest.yml` in `callbacks` with an entry `export`.

As an example, the plugin (frontend part) can write

```json
{
  "export": {
    "produce_options": {
      "plugin": "fylr_example:demo"
    }
  }
}
```

This will then call a `node` programm `export_demo.js` if configured like so in the `manifest.yml`:

```yaml
export:
  demo:
    exec:
      service: "node"
      commands:
        - prog: "node"
          stdout:
            type: body
          args:
            - type: "value"
              value: "export_demo.js"
            - type: "value"
              value: "%info.json%"
```

* The plugin must receive **%info.json%** as payload. The payload consist of general info like baseconfig in `info.config` as well as the `info.export` object.
* The payload needs to write back the `export` object and can modify it.
* `export.files` are read back, but only the internal representation `export._files[n].export_file_internal`.
* Files from the list can be made invisible to the API by setting `export._files[n].export_file_internal.hidden = true`.
* The plugin must set `export._state` to `done`, `done_with_warning`, or `failed`. For `failed` the FYLR server creates a `EXPORT_FAILED` event after the read back and a `EXPORT_FINISH` event for the other cases.
* An `export._plugin_log` (\[]string]) can be passed back to merge into that event.
* The plugin can create its own file entries. Upon request the FYLR server calls again into the plugin, passing `export.files[n].export_file_internal.plugin_action` in `info.plugin_action` back to the plugin.
* Currently all additional files of the plugin need to be created on-the-fly.

#### Payload in %info.json%

| Property                                | Description                                               |
| --------------------------------------- | --------------------------------------------------------- |
| `info.config.system`                    | Base config of the instance.                              |
| `info.request`                          | Inforrmation about the request.                           |
| `export`                                | Export in API format, enhanced with internal information. |
| `export._files[n].export_file_internal` | Internal information per file.                            |
| `plugin_action`                         | Set if the request is for an plugin exported file.        |
| `api_callback.token`                    | Token to call back into the API.                          |
| `api_callback.url`                      | URL to call back into the API.                            |

#### Return payload

Almost everything received in `info.export` must be returned in `export` (so, omit the `info`-level). The export is written back to the database "as is" with only a few checks by FYLR.

`info.export._log` does not have to be sent back to FYLR, its read-only.

**Important data in the payload:**

| Property      | Description                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| `_state`      | The new status of the export. Must be one of `done`, `done_with_warnings`, `failed`.                          |
| `_plugin_log` | This is a \[]string merged into the FYLR server event which is written after the plugin ran (see text above). |

**Data in `export._files[n].export_file_internal`**

| Property        | Description                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| `hidden`        | Set to _true_ to hide this file from the external export API (plugin still sees this file)                          |
| `path`          | Path of this file. This is the path added to `/api/v1/export/[n]/file`.                                             |
| `content_type`  | Content-Type used to display over the API. The Content-Type which is actually sent to the client, is auto-detected. |
| `plugin_action` | Custom action string which is passed back into the plugin if this file is requested by the server.                  |

## export\_transport

This callback is run after the regular export has finished. It runs for each transport in a separate call.

#### Payload in %info.json%

The transport plugin receives the same payload as the **export** plugins, in addition it receives `transport`.

| Property                         | Description                                                   |
| -------------------------------- | ------------------------------------------------------------- |
| _All properties from **export**_ |                                                               |
| `transport`                      | The transport object, with all info needed for the transport. |
| `transport.options`              | Can be used for configuration settings for the transport.     |

#### Return payload

The transport is expected to tell FYLR is the transport went ok or not. In additon the plugin can provide information which is writte to the info block of the event written by FYLR.

All other information does not need to be sent back to FYLR.

| Property         | Description                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| `_state`         | The new status of the export. Must be one of `done`, `done_with_warnings`, `failed`.                          |
| `_transport_log` | This is a \[]string merged into the FYLR server event which is written after the plugin ran (see text above). |
