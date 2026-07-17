---
description: The transition_db_pre_save callback — a plugin action inside a workflow transition. Registering callbacks, wiring them into a transition, the payload, and error behavior.
---

# transition\_db\_pre\_save

A `transition_db_pre_save` callback is a **plugin action of a workflow transition**. While [db\_pre\_save](db-pre-save.md) runs on *every* save, a transition callback runs only when a save matches a configured transition — a specific objecttype, operation and user set. The administrator decides *where* the callback runs; the plugin provides *what* it does.

## Registering callbacks

Transition callbacks are a named map in the [manifest](../manifest.md) — no steps, no filters (the transition itself is the filter):

```yaml
callbacks:
  transition_db_pre_save:
    set_comment:
      exec:
        service: "node"
        commands:
          - prog: "node"
            stdin:  { type: body }
            stdout: { type: body }
            args:
              - { type: "value", value: "%_exec.pluginDir%/server/set_comment.js" }
    check:
      plugin_user:               # optional — act as a configured user
        base_config: "user.api_user"
      exec: { … }
```

## Wiring a callback into a transition

Transitions are managed in the frontend's workflow configuration or over [`/api/v1/transitions`](../../api/README.md). A transition defines *when* it matches — `type` (`resolve`, `reject`, `exit_resolve`, `exit_reject`, `process`), `operations` (`INSERT`, `UPDATE`, `DELETE`), `objecttype_ids` and `who` — and a list of `actions`.

A plugin callback is selected by using **`"<plugin-name>:<callback-name>"` as the action's `type`**. The action's `info` object is free-form and is handed to the callback:

```json
{
  "type": "resolve",
  "operations": ["INSERT", "UPDATE"],
  "objecttype_ids": [17],
  "who": [{ "_basetype": "user", "user": { "_id": 1 } }],
  "actions": [
    {
      "type": "fylr_example:set_comment",
      "info": { "comment": "checked by workflow" }
    }
  ]
}
```

The action types `email`, `set_tags`, `webhook` and `change_owner` are reserved for fylr's built-in actions — every other `type` value is resolved as `<plugin>:<callback>` against the loaded plugins' `transition_db_pre_save` maps.

## The payload

The payload is **identical to [db\_pre\_save](db-pre-save.md#the-request-payload)** — `{ "info": …, "objects": … }` with `_callback_context`, `_current`, the `_all_fields` rendering and all response rules. `objects` contains the objects that matched the transition. Two differences:

* The **action's `info` object is merged into the payload's `info`** — in the example above the callback sees `info.comment == "checked by workflow"`. This is how one callback serves several transitions with different parameters.
* The callback runs **after** the regular `db_pre_save` steps of all plugins, still before the save, inside the same write transaction.

The [response rules](db-pre-save.md#the-response) are the same: echo `_callback_context.hash`, use `_all_fields`, return only changed objects, `{ "objects": [] }` for "no changes".

## Errors

An [error returned by the callback](contract.md#errors) **rejects the save** — the transition acts as a gate. A plugin-authored API error (code, parameters, statuscode) is passed to the client verbatim, so the frontend can show a localized message explaining *why* the workflow rejected the object; any other failure surfaces as the generic `DbPreSaveFailed` error naming the plugin.

## Example

The [fylr example plugin](https://github.com/programmfabrik/fylr-plugin-example) registers `fylr_example:set_comment` (manifest above). The program reads the action's `info` for its parameter:

```javascript
// server/set_comment.js — shared by db_pre_save, transitions and webhooks
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", () => {
  const payload = JSON.parse(input); // { info, objects }
  const comment = payload.info.comment; // ← the transition action's info

  if (comment === undefined) {
    console.log(JSON.stringify({ objects: [] })); // nothing to do
    return;
  }

  const objects = payload.objects.map((obj) => ({
    ...obj,
    _mask: "_all_fields",
    _comment: comment,
  }));
  console.log(JSON.stringify({ objects }));
});
```

## See also

* [db\_pre\_save](db-pre-save.md) — payload and response rules in detail.
* [Workflow Webhooks](../../../for-administrators/readme/workflow-webhooks.md) — the same transition hook over plain HTTP, without a plugin.
* [The callback contract](contract.md) — `info` fields, tokens, `plugin_user`, errors.
