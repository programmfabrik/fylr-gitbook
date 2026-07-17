---
description: The db_pre_save callback — validate or modify objects on every POST /api/v1/db save, before they are written. Steps, filters, the object payload, the response rules, skip_plugins.
---

# db\_pre\_save

A `db_pre_save` callback runs for **every** `POST /api/v1/db` request, before the objects are written. It can validate the objects, modify them, or reject the whole save with an error. Typical uses: filling computed fields, enforcing validation rules a datamodel cannot express, or creating additional objects over the API as a side effect of a save.

## When it runs

`db_pre_save` runs **inside the request's write transaction**:

1. Object-access rights are checked.
2. **`db_pre_save` steps run** — of every enabled plugin, in order (see below).
3. Matched [workflow-transition](transition-db-pre-save.md) actions run.
4. Datamodel constraints are checked.
5. Save rights (create / write / delete) are checked.
6. The objects are written.

Notably, the callback runs **before** the constraint and save-right checks — whatever the plugin returns still has to pass them. If the callback fails, the whole request is rolled back; no objects of that request are saved.

## Registering steps

`db_pre_save` is registered in the [manifest](../manifest.md) with a `steps` list and a `callbacks` map. Each step names a callback and can filter by objecttype; the split lets several steps reuse one callback:

```yaml
callbacks:
  db_pre_save:
    steps:
      - name: "set comment"            # display name of the step
        callback: set_comment          # references the callbacks map below
        filter:
          type: objecttype
          objecttypes:
            - bilder
      - name: "fill sequence number"   # a step without filter runs for every save
        callback: insert_sequence
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
      insert_sequence:
        plugin_user:                   # optional — act as a configured user
          base_config: "user.api_user"
        exec: { … }
```

* **Filter**: the only filter type is `objecttype` — the step runs when at least one object of the save matches `objecttypes`, and the callback receives **only the matching objects**. A step without a `filter` runs for every save.
* **Order**: a plugin's steps run in manifest order. Steps of different plugins run plugin by plugin; a plugin that others depend on runs first. There is no numeric priority.
* A step is **silently skipped** when its plugin is disabled, when its `callback` name is not found, or when no object matches its filter.

## The request payload

The callback receives one JSON document (on STDIN with `stdin: { type: body }`):

```json
{
  "info":    { "…": "the callback contract fields" },
  "objects": [ { "…": "the objects being saved" } ]
}
```

* `info` carries the [callback contract](contract.md) — `api_url`, tokens, `request` (the triggering HTTP request), `config` (base config + the plugin's own config).
* `objects` are the objects being saved, rendered with the **`_all_fields` mask**, including empty fields.

Each object additionally carries:

| Key | Description |
| --- | --- |
| `_callback_context.hash` | A unique, server-generated id for this object **in this call**. Echo it back to modify the object. |
| `_callback_context.original_mask` | The mask of the original request (the objects themselves are rendered with `_all_fields`). |
| `_current` | The currently stored version of the object, fully rendered — `null` / absent when the object is new. Compare against it to detect what the save changes. |

Further payload properties:

* **Inserted objects** have no ids yet: `_uuid`, `_global_object_id`, `_system_object_id` and `<objecttype>._id` are unset. `<objecttype>._id_parent` may be `0` for an as-yet-unknown parent (e.g. in a reverse-hierarchy context).
* **Reverse and bidirectional linked objects** that are part of the save appear as separate top-level entries of `objects`, each with its own `_callback_context.hash` and `_current`. The callback must deal with them — or not return them. For bidirectional objects, returning only one side can lead to incomplete objects.
* In **group mode** (bulk updates addressing many objects at once) the payload consists of the individual objects loaded from the database — the callback always sees concrete objects.

## The response

The callback answers (on STDOUT with `stdout: { type: body }`):

```json
{ "objects": [ … ] }
```

The rules:

* **Only returned objects are updated** — return the objects you changed, matched by their echoed `_callback_context.hash`. Objects you do not return stay exactly as posted.
* Return `{ "objects": [] }` to signal *no changes* — this is the normal "nothing to do" answer.
* Every returned object must use the **`_all_fields` mask** (`"_mask": "_all_fields"`) and echo a non-empty, unique `_callback_context.hash` that was part of the request.
* A returned object **replaces** the posted object wholesale — fylr re-reads it as if the plugin's JSON had been the request. Return the object as you received it, with only the intended modifications; do not drop fields. Changed values, `_comment`, `_tags`, `_pool`, `_acl` and `_owner` all take effect; on insert a plugin can also set `_uuid`. The later pipeline steps (constraints, save rights) still apply to the result.
* **An empty response body is an error** — always return at least `{ "objects": [] }`.

To reject the save, return an [error](contract.md#errors) instead. The API client receives the plugin's error code, parameters and status code verbatim; any other failure (timeout, crash, invalid JSON) surfaces as the generic `DbPreSaveFailed` error naming the plugin. Either way **the whole request is rolled back**.

## Skipping the callbacks

`POST /api/v1/db?skip_plugins=1` saves without running any `db_pre_save` callbacks. This requires the **`system.root`** system right; fylr's own restore uses it to replay backups verbatim.

## Example

Set a comment on every saved `bilder` object, prefixing a value from the plugin's base config — the manifest entry is shown [above](#registering-steps):

```javascript
// server/set_comment.js
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", () => {
  const payload = JSON.parse(input); // { info, objects }

  // a value the administrator configured for this plugin
  const suffix =
    payload.info.config?.plugin?.my_plugin?.config?.comment?.value ?? "";

  const objects = payload.objects.map((obj) => ({
    ...obj, // keep the object intact — only returned objects are updated, wholesale
    _mask: "_all_fields",
    _comment: `reviewed by my_plugin ${suffix}`.trim(),
  }));

  console.log(JSON.stringify({ objects }));
});
```

For a real-world implementation — including calling back into the API to read config and write additional objects — see the [fylr example plugin](https://github.com/programmfabrik/fylr-plugin-example) and the [sequence plugin](https://github.com/programmfabrik/fylr-plugin-sequence).

## See also

* [The callback contract](contract.md) — `info` fields, tokens, `plugin_user`, errors.
* [transition\_db\_pre\_save](transition-db-pre-save.md) — the same hook, but only for matched workflow transitions.
* [Anatomy of a Record](../../record-json.md) — the object JSON the callback receives and returns.
