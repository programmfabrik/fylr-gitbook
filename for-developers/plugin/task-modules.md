---
description: >-
  Plugin task modules add background tasks to fylr's task manager: imports,
  exports, synchronisation and checks that run on a schedule.
---

# Task modules

A **task module** adds a background task to fylr's task manager. A task is the configured instance of a module: its parameters, a start time and optionally a schedule. fylr starts the task when it is due and runs the plugin program on the [execserver](../execserver.md), as the owner of the task.

Plugins can provide task modules from fylr 6.36.0.

Typical uses are imports from and exports to third-party systems, synchronisation, and checks of the data.

## Defining a task module

The manifest's `task_modules` lists the modules. A module is offered in the task manager as `<plugin>.<name>`, e.g. `fylr_example.set_field`.

```yaml
task_modules:
  - name: set_field
    kind: search
    displayname:
      de-DE: Feld setzen
      en-US: Set a field
    description:
      en-US: Sets a field of the objects found to a value.
    params:
      - name: field
        type: text
        mandatory: true
        displayname:
          en-US: Field
      - name: value
        type: text
    exec:
      service: "python3"
      commands:
        - prog: "python3"
          stdin:  { type: body }
          stdout: { type: body }
          args:
            - { type: "value", value: "%_exec.pluginDir%/server/tasks/set_field.py" }
    check:
      service: "python3"
      commands:
        - prog: "python3"
          stdin:  { type: body }
          stdout: { type: body }
          args:
            - { type: "value", value: "%_exec.pluginDir%/server/tasks/check.py" }
```

| Key | |
| --- | --- |
| `name` | Lower case letters, digits and `_`, starting with a letter. Unique within the plugin. |
| `kind` | `search` or `custom`, see below. |
| `displayname`, `description` | Per language. Shown in the task manager. |
| `params` | The parameters of a task, in the format of [base config parameters](manifest/base-config.md). `mandatory: true` refuses a task without a value. |
| `exec` | Runs the task, see [the exec map](manifest.md#the-exec-map). |
| `check` | Optional. Checks the parameters when a task is saved. |
| `debug` | `true` marks a module for development and testing. |

A manifest whose `task_modules` break these rules is not loaded. A module of `kind: search` must not declare the parameters fylr adds to it.

## The two kinds

### `kind: search`

fylr owns the loop. It adds three parameters in front of the module's own:

* `search` (mandatory): the search whose objects the plugin processes, a search request as for `POST /api/v1/search`, plus `incremental`: a run after the first one only finds objects changed since the previous run started, and leaves out objects this task saved itself.
* `set_unset_tags`: tags fylr sets or removes on each object the plugin processed.
* `set_unset_tags_on_error`: tags fylr sets or removes on each object the plugin refused or fylr could not save.

fylr runs the search with the rights of the task owner and calls the exec once per page of up to 100 objects, sorted by `_system_object_id`. The plugin answers per object. fylr then saves, with the rights of the task owner, each object the plugin changed, and sets the tags. **The plugin does not write itself.**

`state.custom` of the task holds `updated` and `failed` of the run. While a run pages, it also holds `search.after`, the last `_system_object_id` done: a run that ends early (error, cancel, timeout) leaves it, and the next run goes on after that object.

### `kind: custom`

One call per run. The plugin does the work itself through the [fylr API](../api/README.md), as the task owner: imports, exports to third-party systems and anything else. The task's `state.custom` is handed in and can be replaced by the plugin, for example to remember how far an import got.

## Input

fylr writes a JSON document to STDIN (`stdin: { type: body }`):

```json
{
  "info": {
    "api_url": "http://fylr.internal:8081",
    "external_url": "https://fylr.example.com",
    "api_user_access_token": "…",
    "api_user": { "user": { "_id": 4, "…": "…" } },
    "config": { "…": "the base config of the plugin" },
    "task": {
      "_id": 12,
      "task_module": "fylr_example.set_field",
      "kind": "search",
      "description": "…",
      "params": { "field": "title", "value": "…", "search": { "…": "…" } },
      "state": { "…": "state.custom of the task" },
      "run_started_at": "2026-11-02T20:30:00Z",
      "last_run_at": "2026-11-01T20:30:00Z",
      "user": { "user": { "_id": 4, "…": "…" } }
    }
  },
  "objects": [ { "…": "kind search: the objects of the page" } ]
}
```

* `info` is also available as the `%info.json%` argument.
* `params` hold the values of the task, with the defaults of the manifest; `secret` parameters are decrypted.
* `api_user_access_token` is an access token of the task owner. It is revoked when the run ends and lives at most as long as any access token (base config `oauth2.expirations`, 24 hours by default). Use it with `api_url` to [call back into the API](callbacks/contract.md#calling-back-into-the-api). Never send it to a third party.
* `objects` (kind `search` only) are rendered as `POST /api/v1/search` renders them with `format: long`.

## Output

The program writes **one JSON object per line** to STDOUT (`stdout: { type: body }`). fylr reads the lines as they arrive and writes each into the task log at once, so a running task shows its progress. Flush after every line (in Python `print(..., flush=True)`). A line that is not a JSON object goes into the log as text.

| Key | |
| --- | --- |
| `msg`, `level` | A log entry. `level` is `debug`, `info` (default), `warning` or `error`. |
| `status_percent` | Kind `custom`: the progress of the run, `0` to `100`. Kind `search` computes it from the count of the search. |
| `state` | Kind `custom`: the new `state.custom` of the task, stored at once. |
| `error` | The run fails with this message, status `error`. Kind `search`: nothing of the current page is saved. |
| `_system_object_id` | Kind `search`: this line answers for that object of the page. |
| `status` | With `_system_object_id`: `ok` (default) or `error`. `error` counts the object as failed and sets `set_unset_tags_on_error`; `msg` is the reason. |
| `object` | With `_system_object_id`: the object, changed, in the form it came in. Leave it out for an object you did not change. |

A program that exits with an error code fails the run as well, but with a generic message; write an `error` line to say why.

```python
import json, sys

def out(**line):
    print(json.dumps(line), flush=True)

inp = json.load(sys.stdin)
params = inp["info"]["task"]["params"]
for obj in inp["objects"]:
    data = obj[obj["_objecttype"]]
    if data.get(params["field"]):
        out(_system_object_id=obj["_system_object_id"], status="error", msg="has a value")
        continue
    data[params["field"]] = params["value"]
    out(_system_object_id=obj["_system_object_id"], object=obj, msg="set")
```

### How fylr saves an object of kind `search`

* The object is saved as the version after the one the plugin got. If someone saved the object in between, the save fails and the object counts as failed.
* The answer must be the object it was sent for: same `_objecttype`, `_system_object_id` and `_id`.
* The save uses the mask of the object as sent, with the rights of the task owner. An object the owner may not change counts as failed.
* `_comment` of the new version is `task <id> module "<module>": <msg>`.
* An object the plugin answers `ok` without `object` is saved only if `set_unset_tags` changes its tags.
* An object without an answer counts as failed.

## The check

If the module has a `check`, fylr runs it when a task is saved, after its own checks: the types, `mandatory`, the options of a `select` parameter, and the parameters with a `plugin_type` of `search`, `set-unset-tags` or `create-object`, which fylr checks like those of its own modules.

The check gets `{"info": {...}}` on STDIN like a run, with `task` holding `_id` (`0` for a new task), `task_module`, `kind` and `params`; it gets no access token. It answers one JSON document:

```json
{ "errors": [ { "param": "count", "msg": "must be between 1 and 100" } ] }
```

An empty list accepts the parameters. Otherwise the save is refused with the code `TaskParamRejected`, naming the first `param` and its `msg`. A check that does not answer this document, or fails, refuses the save with `TaskParamsCheckFailed`.

The check is part of the save request: without a `timeout` in its exec it gets `fylr.execserver.pluginJobTimeoutSec` (30 seconds by default).

## Running time, cancel and timeout

* An `exec` without a `timeout` runs as long as the task: a cancel in the task manager or the task's `task_timeout_sec` end the program.
* The execserver ends a program that shows no progress (no output, no file growth, no CPU) for `fylr.services.execserver.stallTimeoutSec` (600 seconds by default). Write a log line now and then while you wait for a third-party system, or set `stallTimeout` in the exec.

## When the plugin is not there

A task of a module whose plugin is disabled, not licensed or removed stays. A run fails with a message naming the reason, e.g. `task module "fylr_example.set_field" is not available: plugin "fylr_example" is disabled`. Once the plugin runs again, so do its tasks.

## Example

The [fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example) has a module of each kind in `server/tasks/`:

* `import_dummy` (`custom`): creates objects from the records of a dummy source, remembers the last record in `state.custom`.
* `export_search` (`custom`): posts the objects of a search to an endpoint.
* `set_field` (`search`): sets a field of each object found.
* `check.py`: the check of all three.
