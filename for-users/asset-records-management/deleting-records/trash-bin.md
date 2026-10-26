---
description: >-
  This article describes how to find, restore and permanently delete records in
  the trash.
---

# Trash Bin

When you delete a record, fylr does not remove it right away. The record is moved to the trash, where it can be inspected, restored or permanently deleted by users who have the required permission. The trash only exists for users with the system right **Trash Access**; without it, neither the menu entry nor deleted records appear anywhere in the web frontend.

{% hint style="info" %}
The trash is available from fylr 6.22.0. The trash list sorts the most recently deleted records first and can be sorted by deletion date from fylr 6.35.0.
{% endhint %}

### Permissions

Access to the trash is controlled by the system right **Trash Access** (`system.trash_access`) and its parameter **Level**:

<table><thead><tr><th width="146.80859375">LEVEL</th><th>WHAT THE USER CAN DO</th></tr></thead><tbody><tr><td>Read</td><td>See deleted records in the trash and in search.</td></tr><tr><td>Undelete</td><td>Everything of "Read", and restore deleted records.</td></tr><tr><td>Purge</td><td>Everything of "Undelete", and permanently delete records.</td></tr></tbody></table>

Ask your system administrator if you need a higher level. Whether you may delete a record in the first place is a separate permission, see [Deleting Records](./).

### Opening the trash

Users with Trash Access find the **Trash** at the bottom of the side menu. It lists the object types of your fylr; next to each one, a counter shows how many deleted records of this type exist. Click an object type to list its deleted records. The header above the list names the object type you are looking at.

The list works like a normal search result: select a record to see it in the detail panel on the right, which marks it as deleted. Select several records to act on them together.

### Restoring records

1. Select one or more records in the trash.
2. In the detail panel, click **Restore**; for several records use the same entry in the context menu.
3. Confirm the dialog.

The records are back in their object type with the data they had when they were deleted. From fylr 6.35.0, links of a bidirectional relation that were removed on deletion stay removed after the restore.

### Deleting records permanently

1. Select one or more records in the trash.
2. Choose **Delete permanently** in the detail panel or the context menu.
3. Confirm the dialog.

{% hint style="danger" %}
Permanently deleting a record cannot be undone. Purged records can no longer be restored.
{% endhint %}

### Automatic clean-up

Administrators can let fylr empty the trash automatically. In the pool (and object type) configuration, the Janitor setting **Purge records after n days** permanently deletes records that have been in the trash for the given number of days. Without this setting, deleted records stay in the trash until a user purges them.

### Background tasks and the API

The background task `delete_objects` can also restore or permanently delete records, see [Background Tasks](../../additional-features/background-tasks.md).
