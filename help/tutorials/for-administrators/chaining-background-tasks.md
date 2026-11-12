---
description: >-
  Let scheduled background tasks work on what another task did, each run
  taking only the records modified since the previous one.
---

# Chaining Background Tasks

Background tasks can work on what another task did: for example, one task applies a metadata mapping to new images every night, and a second task reports by email which of them could not be described. The checkbox **Range** below the search of a task makes this work: each run takes only the records created or modified since the task's last successful run, and a record the first task saved counts as modified for the second one.

The checkbox **Range** is in the task form from fylr 6.36.0. How it works in detail is described in [Background Tasks](../../../for-users/additional-features/background-tasks.md#only-new-and-changed-records).

## Example: describe new images, report the failures

You need:

* the system right **Access Task Manager**, and the rights to edit the records and set their tags, since a task runs with the rights of its owner
* an object type with a file field and with tags enabled
* a metadata mapping for it, for example one that uses the [ai-metadata plugin](../../../tutorials/ai-metadata-plugin.md)
* a tag for the failures, here **Metadata failed**, see [Tags & Workflows](../../../for-administrators/permissions/tags-and-workflows.md)

### 1. The task that does the work

In the **Tasks Manager**, create a task with the module **Apply metadata mapping**:

| Field | Value |
| --- | --- |
| Title | Describe new images |
| Search | the object type of the images |
| Range | ticked |
| Mapping | with **Configure Mapping**, the object type of the images and the metadata mapping |
| Set/Unset Tags | remove **Metadata failed** |
| Set/Unset Tags on Failure | set **Metadata failed** |
| Schedule Options | **Use scheduler**, preset **Daily** |

Every night at 01:00, the task takes the images that were uploaded or modified since its last successful run. An image it could not describe gets the tag **Metadata failed**, an image it describes on a later run loses the tag again.

The task does not take the records it saved itself on its next run. An image that failed is tried once, and again only after someone modified the record, for example by replacing its file.

### 2. The task that follows

Create a second task with the module **Run search**:

| Field | Value |
| --- | --- |
| Title | Report new metadata failures |
| Search | the tag **Metadata failed** |
| Range | ticked |
| Schedule Options | **Use scheduler**, **Custom Schedule** with **Hour** 3 |
| Email | the users who look after the images |

Every night at 03:00, the task counts the records that have the tag and were modified since its own last successful run: the images the first task tagged that night. The email shows the task log with the count, and **Show Affected Records** on this task shows the records in the search.

### Starting the chain

The first run of each task takes its whole search. On an instance that already holds many images, the first run of the first task describes all of them. If they should stay as they are, limit the search of the first task to records created after a date.

To watch the first runs, create both tasks with the schedule option **None**, start the first one with **Run Now**, read its log, start the second one when the first one is done, and then switch both to **Use scheduler**.

## Rules for a chain

* **Tick Range on every task of the chain.** Each task remembers its own last successful run, and takes what the task before it saved because that save modified the record.
* **The search decides what a task takes from the others.** Apply metadata mapping and Set/Unset Tags leave out only their own saves. Every other change counts, made by users, imports, workflows, plugins or other tasks. Narrow the search, for example to the tag the task before sets.
* **Start the later task when the earlier one is usually done.** If the earlier task is still running, the later one takes what it saved so far. The records the earlier task saves after that, or that are not yet in the search index when the later run starts, are taken by the later task's next run, in this example a day later.
* **A failed run is taken again.** A run that ended with an error, was canceled, ran into its timeout or was interrupted by a stop of the fylr server does not count: the next run of the task takes its records again, together with those modified since. The tasks later in the chain take the saves of the failed run as usual.
