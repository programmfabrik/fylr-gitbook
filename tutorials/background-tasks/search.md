---
description: >-
  The "search" background-task module — run a saved search on a schedule and
  report how many records match, optionally by email.
---

# search

The **search** [background-task](../background-tasks.md) module runs the configured [Search Configuration](../background-tasks.md#task-parameters) and reports **how many records match** — on demand or, more usefully, on a recurring schedule.

Use it to:

* **monitor** the instance: get alerted when the number of records matching a condition changes (items missing a required field, records stuck in a state, files that failed to convert);
* run a scheduled **saved search** whose result count is delivered by email;
* validate a Search Configuration before using it in a mutating module such as [delete_objects](delete_objects.md) or [set_unset_tags](set_unset_tags.md).

## What it does

It performs the search and writes the match count to the [task log](../background-tasks.md#monitoring-and-logs) (`found N objects matching the search`). It does not change any records. Combine it with the task's **Email Notifications** option to have the summary emailed when the task completes.

With the search's **Incremental** option, only records changed since the task's last run are counted.

## Parameters

Only the [common task parameters](../background-tasks.md#task-parameters) — the **Search Configuration** and the schedule / email notification. This module has no parameters of its own.

## Permissions

Running the task needs the **Administration → Access Task Manager** system right; the search sees only the records the task's user may read.

## See also

* [Background tasks](../background-tasks.md) — creating, scheduling and monitoring tasks.
* [Building a Search Request](../../for-developers/search-requests.md) — how a search is structured.
