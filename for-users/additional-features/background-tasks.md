# Background Tasks

Background tasks run operations on records **on the server** — on demand or on a schedule. Use them to clean up records matching a search, re-apply metadata mappings, set or remove tags in bulk, merge duplicate records, or get an email when a scheduled search finds something.

Because tasks run on the server, you do not have to keep the browser open: start a task, close fylr, and check the result later in the task log.

## Required Permissions

Available under a user's or group's **System Rights**:

**Access Task Manager**: Allows users to open the Tasks Manager and create, edit, run and delete background tasks.

{% hint style="info" %}
A task operates with regular record permissions. To successfully run a module, the user also needs the corresponding permissions — for example, delete rights on the affected records for the `delete_objects` module.
{% endhint %}

## Opening the Tasks Manager

Open the **Tasks Manager** from the header bar of your fylr instance.

<figure><img src="../../.gitbook/assets/Screenshot 2025-08-22 at 14.19.16.png" alt="the Background Tasks manager in the header bar"><figcaption><p>The Background Tasks manager, opened from the header bar</p></figcaption></figure>

The list shows all background tasks with the columns **Task ID**, **Module Name**, **Description**, **Created At**, **Created By**, **Status**, **Started At**, **Finished At** and **Next Run At**.

For each task, the following actions are available:

<table><thead><tr><th width="234.13671875">ACTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Run Now</strong></td><td>Starts the task immediately, regardless of its schedule.</td></tr><tr><td><strong>Edit Task</strong></td><td>Change title, description, parameters and schedule.</td></tr><tr><td><strong>View Task Log</strong></td><td>Inspect progress, results and error messages.</td></tr><tr><td><strong>Show Affected Records</strong></td><td>Oopen the records the task operates on in the search.</td></tr><tr><td><strong>Delete Task</strong></td><td>Remove the task (the records are not affected).</td></tr></tbody></table>

## Creating a Task

There are three ways to create a background task:

1. In the **Tasks Manager**, via the create button
2. From the **search**: select records and choose "**Create background task...**" from the context tools — the current search is taken over as the task's search
3. From a **collection**: choose "**Create background task**" in the collection's context menu — the collection is used as the source

### **Task Details**

<table><thead><tr><th width="146.125">FIELD</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Module</strong></td><td>The type of job the task performs (see <a href="background-tasks.md#modules">Modules</a>). The module is chosen at creation and <strong>cannot be changed afterwards</strong>.</td></tr><tr><td><strong>Title</strong></td><td>Nme of the task, shown in the Tasks Manager.Can be edited later.</td></tr></tbody></table>

### **Task Parameters**

The available parameters depend on the selected module. Most modules operate on a **Search**, which defines the target records — configured with the same options as the expert search. Enable **Incremental** on the search to run only on records changed since the task's last run — useful for a scheduled task, so it processes new and edited records instead of re-processing everything each time.

### **Scheduling & Notifications**

**Schedule Options**:

<table><thead><tr><th width="228.94140625">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>None</strong></td><td>The task is saved but does not run by itself — start it with <strong>Run now</strong> when needed.</td></tr><tr><td><strong>Run now</strong></td><td>The task runs once, immediately after saving.</td></tr><tr><td><strong>Schedule a manual time</strong></td><td>The task runs once at the configured <strong>Start At</strong> time (empty = immediately).</td></tr><tr><td><strong>Use scheduler</strong></td><td>The task runs repeatedly according to one or more <strong>Schedules</strong>.</td></tr></tbody></table>

With **Use scheduler**, configure recurring runs in the schedule editor. Presets: **Every minute**, **Every 5 / 10 / 15 / 30 minutes**, **Hourly**, **Daily**, **Weekly** — or build a **Custom Schedule** from **Day of Month**, **Weekday**, **Hour** and **Timezone**. A task can have multiple schedules; the next planned run is shown in the **Next Run At** column.

**Email**: add one or more users as recipients to send an email notification when the task is finished.

## Modules

<table><thead><tr><th width="227.875">Module</th><th>Purpose</th></tr></thead><tbody><tr><td><code>delete_objects</code></td><td>Delete all records matching a search. Also supports permanently deleting or restoring records from the trash.</td></tr><tr><td><code>metadata</code></td><td>Apply a metadata mapping to records matching a search.</td></tr><tr><td><code>search</code></td><td>Run a search and report the number of matching records.</td></tr><tr><td><code>set_unset_tags</code></td><td>Set or remove tags on records matching a search.</td></tr><tr><td><code>consolidate_objects</code></td><td>Merge duplicate records into one target record.</td></tr></tbody></table>

### **delete\_objects**

Deletes — or restores — the records matching the configured **Search**. The **Delete Policy** controls what happens:

<table><thead><tr><th width="151.8046875">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Unlink</strong> (<code>setnull</code>)</td><td>Delete the records and set links that point at them in other records to null. The default.</td></tr><tr><td><strong>Delete</strong> (<code>remove</code>)</td><td>Also delete the subordinate or reverse-linked records of the deleted records.</td></tr><tr><td><strong>Purge</strong> (<code>purge</code>)</td><td>Permanently delete the records from the trash — not recoverable.</td></tr><tr><td><strong>Restore</strong> (<code>undelete</code>)</td><td>Restore matched, soft-deleted records from the trash.</td></tr></tbody></table>

{% hint style="warning" %}
Review the search carefully before scheduling this module — every record matching the search is deleted on every run. Deleted records are moved to the trash and can be restored from there (see [deleting records](../asset-records-management/deleting-records.md)).
{% endhint %}

### **metadata**

Applies an existing **Metadata Mapping** to all records matching the **Search** — for example, to re-apply a mapping of file metadata (EXIF, IPTC, XMP) to records whose files were uploaded before the mapping existed.

Additional parameters:

<table><thead><tr><th width="212.93359375">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Override Values</strong></td><td>Allow the mapping to replace existing field values; otherwise only empty fields are filled.</td></tr><tr><td><strong>Merge Values</strong></td><td>Merge mapped values with existing ones instead of replacing them.</td></tr><tr><td><strong>Set/Unset Tags</strong></td><td>Set or remove tags on each record after it was successfully updated.</td></tr></tbody></table>

### **search**

Runs the configured **Search** and reports the number of matching records in the task log. Combined with a schedule and an email notification, this works as a recurring report — for example, a weekly check for records that are missing required information.

### **set\_unset\_tags**

Sets or removes **Tags** on all records matching the **Search** — useful for bulk (re-)tagging, for example marking all records of a pool for review.

### **consolidate\_objects**

Merges duplicate records: all references to the **Source records** are re-linked to the **Target record**.

<table><thead><tr><th width="246.59375">PARAMETER</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Source Secords</strong></td><td>Select the record(s) that should be replaced.</td></tr><tr><td><strong>Target Record</strong></td><td>Select the record that should replace the other selected record(s).</td></tr><tr><td><strong>Dry Run</strong></td><td>Only report in the task log what would change, without modifying any records.</td></tr><tr><td><strong>Delete Source Records</strong></td><td>Delete the source records after re-linking.</td></tr></tbody></table>

{% hint style="info" %}
Start with a **dry run** and check the task log before running the consolidation for real.
{% endhint %}
