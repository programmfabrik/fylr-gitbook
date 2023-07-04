---
description: >-
  Define permissions for object types here, so user can access the lists /
  thesauri. Set custom file names for download & export or add search filter for
  fields.
---

# Object Types

## General

<table><thead><tr><th width="283.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>ID</td><td>Object type identifier. Will be assigned automatically.</td></tr><tr><td>Contact Person</td><td>Contact person of the object type. Users can access the contact person in the object type details (in "Sources" for example).</td></tr><tr><td>Description</td><td>Description of the object type. Users can access the description in the object type details (in "Sources" for example).</td></tr><tr><td>Masks</td><td>By default, all records of this object type will be rendered in all masks you created for the object type in the data model. If you, for example, only want the records to be rendered in one of the masks, disable the checkbox and drag all masks that should not be rendered for records of this object type, below the gray line.</td></tr><tr><td>XMP/IPTC/EXIF Import-Profil</td><td>Default metadata mapping which will be used when user upload a file with the standard mapping. Can be chosen when uploading files (data will be extracted from the file and written into data fields).</td></tr><tr><td>XMP/IPTC/EXIF Export-Profil</td><td>Default metadata mapping which will be used when user download a file with the standard mapping. Can be chosen when downloading files (data will be written into the file itself) or when exporting records (data will be written into a XML file then).</td></tr><tr><td>Dublin Core Export-Profil</td><td>Default Dublin Core metadata mapping which then will be used for <a href="../readme/export-and-deep-links.md#oai-pmh">OAI/PMH</a>. Mapping does not appear in the frontend when downloading or exporting records.</td></tr><tr><td>Show in Main Menu</td><td>Enter an icon from <a href="https://fontawesome.com/v4/icons/">FontAwesome</a> and the object type will then appear in the main menu with it's own search.</td></tr><tr><td>Show in filter in group "Linked object types"</td><td></td></tr></tbody></table>

### File Names for Download & Export

When **downloading** or **exporting** files, the original **file name** will be used as a default. If you want to **rename** files when downloading or exporting, you can define a file name for different languages here. You can use **static text** and **data** from the record (click on the "Show Replacements" button to see the supported **replacements**).&#x20;

Example to create the file name "PF - 3 - Title - original.jpg":

```
PF - %_system_object_id% - %objects.title% - %_asset.version%.%_asset.extension%
```



## Tags

Only **available** for object types with **enabled** **tag** **management**. By **default**, **all** [globally defined **tags**](tags-and-workflows.md) are **available** c. If you want to **disable** certain tags for specific object types, you have to enable "**Use Individual Tags**" in the lower right. You then see all the tags above and can disable individual tags or make them a default. For more details, please refer to ["Tags & Workflows"](tags-and-workflows.md).&#x20;

Tags that are "**Persistent**" globally **can't be disable** here.



## Workflows

Only **available** for object types with **enabled** **tag** **management**. By **default**, **all** [globally defined **workflows**](tags-and-workflows.md) are **available** for all object types. If you want to **disable** certain workflows for specific object types, you have to enable "**Use Individual Workflows**" in the lower right. You then can set up individual workflows. For more details, please refer to ["Tags & Workflows"](tags-and-workflows.md).&#x20;

Workflows that are "**Persistent**" globally **can't be disable** here.



## Permissions

Only **available** for object types **without** enabled **tag** **management**. Define which **user / user groups** can, for example, **view, download, edit or delete** the records of this object type.&#x20;

Please refer to [Permissions](./) for more details.



## Input & Output

**Usually** only the **current** **version** of records will be **indexed**. So if you create a record and edit it later, only this **second** version will be **available** in the **search**. The **first** version can **no** longer be **found** (old versions can only be accessed in the **change history**).

But it's also possible to tag a record as "**published**" and then keep on **working** on the record internally. Then **external guest users** for example would **see** the **published version**, while the **internal editors** work on **updated versions** of the **same record**.

If you want users to also **access** an **old** **version** of records, you can do so by following this **tutorial** (coming soon).&#x20;

{% hint style="info" %}
Please note, these settings are only available for object types with tag management and with multiple masks.&#x20;
{% endhint %}



## Field Visibility

Instead of creating masks to **hide / show fields**, you can also use the field visibility plugin to give users / user groups access to **more or less fields** in the editor or detail view. By **adding** a **field** for a specific user / group, this field will **automatically** **be hidden** for all **other** users.&#x20;

{% hint style="info" %}
Please note, that the field visibility plugin is a frontend only feature. Over the API all fields from the used mask are available (even though they might be hidden with the field visibility plugin).
{% endhint %}

<table><thead><tr><th width="220.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Internal Name</td><td>Internal name to identify the settings.</td></tr><tr><td>Fields</td><td>Select all fields that should only be visible for a specific user or user group.</td></tr><tr><td>Tag Filter</td><td>Add a tag filter, if the fields should only be visible when a record has a specific tag.</td></tr><tr><td>User / Group</td><td>Select the user and / or groups that should be able to access the specified fields.</td></tr></tbody></table>

So if you have a field "Insurance Sum" that only users of the group "Power Users" are allowed to access, add one row, select the field "Insurance Sum" and select the group "Power Users". All other users won't be able to access this field.



## Filter for Linked Object Types

If an **object type refers** to **other object types**, **filters** for these lists / thesauri can be defined here.&#x20;

### Use Case 1

If, for example, you have a list of **persons** where you, for example, **define** if the person is a **photographer or a sculptor**, you can set up a **filter**, so that **only** persons with the **type** **"Photographers"** will be shown for the **"Photographer" input field**. All **other** persons would be **hidden**. If the **same** list is also used for **other** fields (e.g. for "Artists"), the **filter** does **not** **apply** there and **all** records from the person list are **displayed**.

### Use Case 2

If, for example, you have a **hierarchical list** of categories and want users to be able to **only** **link records from the lowest level**, this can also be accomplished with a **filter**. To do this, select the **relevant field** (e.g. "Categories") and activate the checkbox "**Restrict Selectability to the Lowest Level**". Afterwards, **only** the records on the **lowest** level can be **linked** to a record in this specific field. Records with **subordinate entries** cannot be linked. This filter does **not** take effect in the **expert search**. There, records of **all** levels can still be **selected** in the specific field.

### Options

<table><thead><tr><th width="263.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Display Name</td><td>Name of the filter. Will be shown in the search.</td></tr><tr><td>Fields</td><td>Select the fields you want to filter. Only fields that are linked to an object type are available. </td></tr><tr><td>Restrict Selectability to the Lowest Level</td><td>Enable if only the lower levels in a hierarchical list should be selectable. If enabled, records with subordinate records can not be linked. See <a href="object-types.md#use-case-2">use case 2</a>.</td></tr><tr><td>Filter</td><td>Use the expert search to filter the records of the connected object type. This search will automatically be applied to the selected field(s).</td></tr></tbody></table>

{% hint style="info" %}
Please note, that these filter cannot be disabled in the frontend. Only root users are able to deactivate a filter in the search and access all records of the linked object type.
{% endhint %}



## PDF Creator

Create **custom** **PDF templates**. More details coming soon.

{% hint style="info" %}
The "PDF Creator" plugin is licensed as a separate module. Please check your license agreement in case of doubt.
{% endhint %}
