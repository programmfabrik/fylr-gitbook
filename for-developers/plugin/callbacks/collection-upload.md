---
description: The collection-upload callback — a plugin participates when files are uploaded into a collection via hotfolder, WebDAV or the API, modifying the created objects and logging per-file results.
---

# Collection upload

A **collection-upload callback** lets a plugin participate when files are uploaded **into a collection** — via the [hotfolder](../../webdav.md), WebDAV, or `POST /api/v1/eas?collection=<id>`. For every uploaded file, fylr creates objects according to the collection's *create object* settings; the plugin can modify these objects before they are saved and report per-file results into the upload log. Available since fylr 6.10.0.

## Registering

Unlike the other hooks, `collection_upload` is a **top-level manifest key** (not under `callbacks:`). Each entry declares the plugin's per-collection configuration parameters and an `objects` callback:

```yaml
collection_upload:
  filename_copy:
    config:                       # parameters, configured per collection
      - name: filename_copy
        parameters:
          filename_target:
            type: text
    callbacks:
      objects:
        plugin_user:              # optional — act as a configured user
          base_config: "user.api_user"
        exec:
          service: "node"
          commands:
            - prog: "node"
              stdin:  { type: body }
              stdout: { type: body }
              args:
                - { type: "value", value: "%_exec.pluginDir%/server/objects.js" }
```

The administrator selects the plugin in the collection's upload settings — over the API that is the collection's `create_object.plugin` (`"<plugin-name>:<entry-name>"`, e.g. `"fylr_example:filename_copy"`); the values for the declared `config` parameters are stored per collection in `create_object.plugin_config`.

## The payload

The `objects` callback receives the [db\_pre\_save payload](db-pre-save.md#the-request-payload) — `{ "info": …, "objects": … }` with `_callback_context` and all response rules — where `objects` are the objects about to be created for the uploaded file. `info` carries three additional keys:

| Key | Description |
| --- | --- |
| `info.file` | The uploaded file, including e.g. `original_filename` and its technical metadata. |
| `info.collection` | The collection the file is uploaded into. |
| `info.collection_config` | The per-collection values of the parameters declared under `config` — e.g. `info.collection_config.filename_copy.filename_target`. |

## The response

The [db\_pre\_save response rules](db-pre-save.md#the-response) apply: return changed objects with their echoed hash and the `_all_fields` mask, `{ "objects": [] }` for *no changes*, or an [error](contract.md#errors) to fail the upload. Additionally the response may carry an **`upload_log`** — one entry per file result, recorded in fylr's upload protocol (e.g. the hotfolder log):

```json
{
  "objects": [ … ],
  "upload_log": [
    {
      "file": "IMG_2041.jpg",
      "filesize": 1234567,
      "status": "done",
      "msg": "title filled from filename",
      "file_eas_id": 123,
      "system_object_id": 124
    }
  ]
}
```

## Example

Copy the uploaded file's name into a configurable text field:

```javascript
// server/objects.js
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", () => {
  const payload = JSON.parse(input); // { info, objects }

  // the target column, configured per collection
  const col = payload.info.collection_config?.filename_copy?.filename_target;
  if (!col) {
    console.log(JSON.stringify({ objects: [] })); // not configured: no changes
    return;
  }

  const upload_log = [];
  const objects = payload.objects.map((obj) => {
    const filename = payload.info.file?.original_filename ?? "<no filename>";
    upload_log.push({ file: filename, status: "done", msg: `${col} set from filename` });
    return {
      ...obj,
      _mask: "_all_fields",
      [obj._objecttype]: { ...obj[obj._objecttype], [col]: filename },
    };
  });

  console.log(JSON.stringify({ objects, upload_log }));
});
```

The complete implementation ships with the [fylr example plugin](https://github.com/programmfabrik/fylr-plugin-example) (`collection_upload.filename_copy`).

## See also

* [db\_pre\_save](db-pre-save.md) — payload and response rules in detail.
* [The callback contract](contract.md) — `info` fields, tokens, `plugin_user`, errors.
* [WebDAV and hotfolder](../../webdav.md) — the upload channels that trigger this hook.
