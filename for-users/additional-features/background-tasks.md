---
description: >-
  Run long-running operations on many records — bulk metadata updates, deletes,
  and tagging — in the background while you continue working.
---

# Background Tasks

Some operations in fylr touch many records at once. Re-applying a metadata mapping to thousands of files, deleting a search result with all its links, or setting a tag on every record in a pool can each take several minutes. Background tasks let you start such an operation, walk away, and come back to a finished result instead of holding a browser tab open.

A task runs on the server. You can close the browser, log out, or work on something else while it runs. The Task Manager shows the progress of every task you started and keeps each finished task as a receipt with its log.

## Where to find the Task Manager

The Task Manager opens from the icon in the tray area of the fylr header bar (top right, next to your user menu). The button is only visible to users who have permission to run tasks. The window that opens lists every task you have created, newest first, with five columns: Module, Title, Status, Started, Finished, and Next Run.

To dismiss the window, click outside of it or close it with the X. The task itself keeps running on the server.

## Creating a task

Click the plus button at the bottom of the Task Manager. A dialog opens with two fields you always fill in:

* **Module** — which kind of operation the task will perform. The available modules are described below.
* **Title** — a short description so you can recognise the task later. The title only helps you keep your tasks apart; it has no effect on what the task does.

Below those two fields the dialog rebuilds itself depending on the module you picked. Each module has its own parameters — for example, the *Delete Objects* module asks for a search and a delete policy, the *Metadata* module asks for a mapping. Fill in the parameters, then click **Save**.

A new entry appears in the Task Manager list. The task is queued and will start as soon as the server has capacity. You can close the dialog and the Task Manager — the task keeps running.

## Available modules

### Metadata

Re-applies a configured metadata mapping to a set of records. Use this after a mapping has changed, after a configuration import, or after a basetype change, to bring records back in line with the new mapping.

The module asks for:

* **Mapping** — the configured metadata mapping to apply.
* **Search** — limits the task to a subset of records. Leave empty to run over everything the mapping applies to.
* **Set/Unset Tags** — optionally adds or removes tags as part of the mapping pass.
* **Merge Values** / **Override Values** — controls whether values from the mapping are merged into existing values or replace them outright.

### Delete Objects

Bulk-deletes records that match a search. This is the same delete that the right-click menu offers for a single record — except a task can apply it to hundreds of thousands at once and walks the link graph safely.

The module asks for:

* **Search** — defines which records to delete.
* **Delete Policy** — controls what happens to records that link to the records you are deleting:
  * **Delete** also deletes subordinate or reverse-linked records.
  * **Unlink** removes the links and leaves the linking records intact.

{% hint style="warning" %}
A bulk-delete with the wrong search filter can affect many more records than you intended. Run the same search in the normal Search view first to confirm the result set before starting the task.
{% endhint %}

### Set / Unset Tags

Adds or removes tags on every record matching a search. Useful for adopting a new tagging convention, or cleaning up tags from an old workflow without opening each record individually.

The module asks for:

* **Search** — which records to act on.
* **Tags to set** and **Tags to unset** — the tags to add to or remove from each matching record.

## Reading the task list

| Column | What it shows |
| --- | --- |
| Module | Which module the task uses. |
| Title | The description you entered when you created the task. |
| Status | Where the task is in its life cycle — *queued*, *running*, *finished*, or *failed*. |
| Started | When the task actually began executing on the server. Empty if the task is still queued. |
| Finished | When the task ended. Empty if the task is still running. |
| Next Run | For tasks that are scheduled to repeat, when they will run next. *Now* means the task is queued and waiting for capacity. |

Click a row to open the task's details: the parameters you supplied, the records it touched, and the log of what happened. The log is the place to look if a task ended with status *failed* — fylr writes the error message into the log so you can decide whether to fix the input and run the task again.

## Deleting old tasks

Tasks accumulate over time. Select a finished task and click the minus button at the bottom of the Task Manager to delete it. The task receipt is removed; the records the task already acted on are not affected.

Tasks that are still queued or running cannot be deleted from the list directly. Open the task's details and use **Cancel** there instead.

## Required Permissions

The following permissions control who can see and run background tasks.

Available under a user's or group's **System Rights**.

Permission **Access Tasks** (`system.task`):

* Allows users to open the Task Manager and see their own tasks.
* Without this permission the Task Manager icon is hidden from the header bar entirely.

Each module additionally requires whatever permission the underlying operation would require if performed manually. For example, the *Delete Objects* module is only useful to users who would be allowed to delete the matched records one by one — the task does not bypass record-level permissions.

{% hint style="info" %}
Tasks are user-specific. You only see tasks you created. Administrators (`system.root`) can see and manage every user's tasks.
{% endhint %}

<br>
