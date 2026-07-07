---
description: >-
  The "delete_objects" background-task module — delete, purge or restore the
  records a search matches.
---

# delete_objects

The **delete_objects** [background-task](../background-tasks.md) module applies a delete action to every record the [Search Configuration](../background-tasks.md#task-parameters) matches — on demand or on a schedule.

Use it to:

* clean up records that match a rule (imports older than a date, drafts never published);
* **empty the trash** on a schedule (purge soft-deleted records);
* bulk-**restore** records from the trash.

## What it does

It runs the configured search and applies the chosen **Delete Policy** to the matched records:

| Delete Policy | Effect |
| --- | --- |
| `setnull` _(default)_ | Delete the records and **unlink** them from other records (set links that pointed at them to null). |
| `remove` | Delete the records **and** their subordinate / reverse-linked records. |
| `purge` | **Permanently** remove the records from the trash — not recoverable. |
| `undelete` | **Restore** matched, soft-deleted records from the trash. |

## Parameters

In addition to the [common task parameters](../background-tasks.md#task-parameters):

| Parameter | Description |
| --- | --- |
| **Delete Policy** | one of `setnull`, `remove`, `purge`, `undelete` (see above). |

{% hint style="warning" %}
`purge` is irreversible. Test the Search Configuration first — for example with the [search](search.md) module — to confirm it matches exactly the records you intend to remove.
{% endhint %}

## Permissions

Running the task needs the **Administration → Access Task Manager** system right, and the task's user needs the delete rights on the matched records.

## See also

* [Background tasks](../background-tasks.md) — creating, scheduling and monitoring tasks.
* [search](search.md) — count what a search matches before deleting.
