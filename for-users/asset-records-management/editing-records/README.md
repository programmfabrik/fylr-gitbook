---
description: This article describes the different ways of editing existing records in fylr.
---

# Editing Records

{% hint style="info" %}
Please note, that editing records is only possible for users with necessary permissions. Without the appropriate permissions, the option to edit records will not be available. Users needing permissions should contact their system administrator for assistance.
{% endhint %}



There are basically two different modes when it comes to editing existing records:

<table><thead><tr><th width="257">MODE / EDITOR</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Single Mode / Single Editor</td><td>This allows you to edit one record at a time.</td></tr><tr><td>Group Mode / Group Editor</td><td>This allows you to edit multiple records at a time.</td></tr></tbody></table>

And three different editors:

<table><thead><tr><th width="188">EDITOR</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Sidebar Editor</td><td>Editor that opens on the right side of the search. Only allows editing one record at a time. You can switch from the sidebar editor to the full screen editor at any time.</td></tr><tr><td>Full Screen Editor</td><td>Editor that covers the entire screen. Only allows editing one record at a time. You can switch from the full screen editor to the sidebar editor at any time.</td></tr><tr><td>Popover Editor</td><td>Small editor that opens when editing records of linked object types / lists / thesauri.</td></tr></tbody></table>

## How To Access

You can access the editor by using the context menu in the search. Simply right-click on a record and go to "Edit" and then choose either "In Sidebar" or "In Full Screen". You can also switch from the detail view to the editor by clicking the little edit icon in the upper right. And once you're in the sidebar editor, you can switch to the full screen editor by clicking on the expand button in the upper right.

For the group editor, you first have to select at least two records of the same object type. Then the "Group Editor" option in the context menu of a record is available. If there are multiple object types in the selection, you have to choose which object type you want to edit. For more information please refer to the [group editor](group-editor.md).

The popover editor is only available in list fields. So whenever the field requires the user to choose from a list, you can - if you have the appropriate permissions - edit the record of the list by right-clicking on it and choosing "Edit Record" from the options.



## General Structure

Usually the editors consist of 5 parts:

<table><thead><tr><th width="169">PART</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Header</td><td></td></tr><tr><td>Asset Browser</td><td>The asset browser is the part of the editor where a preview image is shown. Not available for object types without files.</td></tr><tr><td>Standard Info</td><td>Above the input fields, the so called "Standard Info" of the record is shown. It usually consists of a title for the record and system information (such as pool and ID).</td></tr><tr><td>Input Fields</td><td>The input fields allow you to enter your data. They are based on the data model and are therefore fully customizable by administrators.</td></tr><tr><td>Footer</td><td>The footer shows some technical information such as the date the record was created and last updated.</td></tr></tbody></table>

## General Features

