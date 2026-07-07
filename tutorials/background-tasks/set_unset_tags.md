---
description: >-
  The "set_unset_tags" background-task module — set or remove tags on the
  records a search matches.
---

# set_unset_tags

The **set_unset_tags** [background-task](../background-tasks.md) module sets or removes [tags](../../for-developers/concepts/tags-and-transitions.md) on every record the [Search Configuration](../background-tasks.md#task-parameters) matches — on demand or on a schedule.

Use it to:

* **bulk-tag** the result of a search (mark everything matching a rule);
* keep a tag in sync on a schedule (add a "needs review" tag to newly imported records, remove a "new" tag after a while);
* drive downstream automation — a [tag filter](../../for-developers/concepts/tags-and-transitions.md) or a workflow reacts to the tag the task sets.

## What it does

For each record the search returns, it applies the configured tag changes — **setting** the tags to add and **unsetting** the tags to remove — and saves the record as a new version. Records the task's user may not edit are skipped and noted in the [task log](../background-tasks.md#monitoring-and-logs).

## Parameters

In addition to the [common task parameters](../background-tasks.md#task-parameters):

| Parameter | Description |
| --- | --- |
| **Set / unset tags** | the tags to set and the tags to unset on each matched record. |

## Permissions

Running the task needs the **Administration → Access Task Manager** system right, and the task's user needs the rights to edit the matched records and to set the tags.

## See also

* [Background tasks](../background-tasks.md) — creating, scheduling and monitoring tasks.
* [Tags and transitions](../../for-developers/concepts/tags-and-transitions.md) — what tags are and how workflows react to them.
