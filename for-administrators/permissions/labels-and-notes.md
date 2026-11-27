---
description: >-
  A label and a note on every permission entry, a filter line and a compact
  view keep long lists of permissions readable.
---

# Labels and Notes

{% hint style="info" %}
Available from version 6.36.0.
{% endhint %}

Every entry in the permissions of a pool, group, user, object type or tag, and in the permissions of a record in the editor, can have a **label** and a **note**. A label marks the entries that belong together, for example all entries for one exhibition or one project. A note says what a single entry is for.

Labels and notes grant nothing. They are saved with the permissions, but do not change what a user or group may do.

## Label and Note

The **label** has its own column between **Active** and the user or group. Its select offers the labels of the base configuration, one label per entry.

The **note** has its own column too, a text field you type in directly.

Label and note are saved together with the permissions of the pool, group, user, object type, tag or record. Whoever may edit these permissions may also set the label and the note. There is no separate right for them.

An entry stores which label it has, not the label's name. If you rename a label, or change its icon or color, every entry with that label shows the change.

## Filter line

The line above the entries narrows the list down. It does not change the entries:

* **User or group** (left): shows only the entries of the selected user or group. While a user or group is selected, **+** adds an entry that already has it.
* **Search** (middle): finds entries by the name of their user or group, the name of their label and the text of their note.
* The **count** (right) shows how many of the entries are visible.

A new entry added with **+** stays visible, even if it does not match the filter. Choosing a user or group or searching does not count as a change, so **Save** stays disabled.

## Full and compact view

The two buttons at the right of the filter line switch between the full and the compact view:

* **Full**: the permissions and the tag filter of each entry are listed below its buttons.
* **Compact**: these lists are hidden, and the buttons show how many permissions and tags are set.

fylr keeps the choice for each user.

## Managing the labels

The labels are a list in the base configuration, under [General > Tags & Labels > Permission Labels](../readme/general.md#permission-labels). Each label has a name, which can be entered per language, an icon and a color. The icon and the color are picked like those of a tag: a built-in one, or one of the [Custom Icons](../readme/general.md#custom-icons) and [Custom Colors](../readme/general.md#custom-colors) of the same block.

Users with the system right **Manage Base Configuration** or **Full Access to the System** can also edit the list from any permissions table: **Edit Labels…** is the last entry of the label select. Saving there saves only the labels, and the entries show the changes right away. Users without this right can pick a label but cannot change the list.

Every logged-in user can read the list of labels. It is not shown without a login.

The sharing dialog of a collection has no labels, notes or filter line.

## In the API

The label and the note are kept in the `custom_data` of the permission entry, under `webfrontend`. See [Permissions](../../for-developers/concepts/permissions.md) in the concepts.
