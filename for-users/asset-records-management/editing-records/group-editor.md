---
description: The group editor enables you to edit multiple records at once.
---

# Group Editor

## Working With The Group Editor

The group editor is used to modify multiple records at once. For example, if you want to add a text or keyword to x records, fix a typo in the description or change a tag. To access the group mode, you have to select the records you want to edit first. Then right-click on the selection and choose "Group Editor".&#x20;

{% hint style="warning" %}
Please note, that you need the system right "Group Editor" to be able to edit bulks of records.
{% endhint %}

{% hint style="info" %}
If you have selected records from multiple object types, you have to choose one object type to continue. Editing records from multiple object types is not supported.
{% endhint %}

{% hint style="danger" %}
Please be very careful when working with the group editor as the changes cannot be reverted.
{% endhint %}



## Structure

The group editor consists of 5 parts:

<table><thead><tr><th width="169">PART</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Header</td><td>In the header of the group editor you find a pulldown to switch the mask, an option to show the asset browser as well as the templates.</td></tr><tr><td>Selection</td><td>Access the records you have selected to be edited in group mode.</td></tr><tr><td>Input Fields</td><td>The input fields allow you to enter your data. They are based on the data model and are therefore fully customizable by administrators.</td></tr><tr><td>Asset Browser</td><td>The asset browser is the part of the editor where a preview image is shown. Not available for object types without files.</td></tr><tr><td>Footer</td><td>In the footer possible errors are shown as well as the chunk size and the delete and save buttons.</td></tr></tbody></table>



### Header

In the header you find the mask pulldown on the left where you can switch between the available masks (as defined in the data model). Please note that changing the mask will result in a reload of the page and your changes will be lost. On the right side you can open and detach the asset browser and save or load a template.



### Selection

In the left pane you see your selection of records that  you are currently editing in the group mode. You can click on each record to see its details. To remove one record from the group mode, you have to select it and click on the little minus on the bottom of the selection pane.&#x20;

If you want to use data from one specific record for all the other selected records, click on the record and then on the little copy button at the bottom of the selection pane. All data will be copied to the "Template Record" and you only have to enable the checkboxes of the fields you want to modify for all selected records.



### Input Fields

The most important thing about the group editor is, that only the fields you select will be updated, all other fields will not be modified. So make sure, that you enable the checkbox for all fields you want to update. Otherwise your changes will not be made.

The options will differ depending on the type of the input fields. The following input fields have no additional options: Pool, Owner, Parent Entry, Child Numbering, Multilingual Single-Line & Multi-Line Text Field, Date Field, Date Range Field, Date & Time Field, Integer Field, Decimal Number Field, Double Field, File Upload Field, Checkbox (Boolean), Simple Link Field, Pulldowns, Plugins.

{% hint style="warning" %}
Please note, that reverse edit fields are currently not supported in the group editor.
{% endhint %}



#### Options for Permissions

By default, entered permissions are added to already existing permissions. Other options are:

<table><thead><tr><th width="243">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Add permission(s)</td><td>Adds the permission(s) from the group editor to the already existing permission(s) of the selected records.</td></tr><tr><td>Replace all permission(s)</td><td>Replaces all permissions of the selected records with the permission(s) from the group editor.</td></tr><tr><td>Remove all permissions</td><td>Removes all permissions from the selected records without adding new permissions.</td></tr></tbody></table>



#### Options for Tags

By default, entered tags are added to already existing tags. Other options are:

<table><thead><tr><th width="239">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Add tag(s)</td><td>Adds the tag(s) from the group editor to the already existing tag(s) of the selected records.</td></tr><tr><td>Replace all tag(s)</td><td>Replaces all tags of the selected records with the tag(s) from the group editor.</td></tr><tr><td>Remove selected tag(s)</td><td>Removes the tag(s) selected in the group editor from the selected  records.</td></tr><tr><td>Remove all tag(s)</td><td>Removes all tags from the selected records without adding new tags.</td></tr></tbody></table>



#### Options for Text Fields

The default for text fields is, that the whole value get's overwritten by the input in the group editor. But you can also search for specific words in this fields and replace them by other text, and you can also append the text from the group editor to the existing text in that field.

<table><thead><tr><th width="187">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Search &#x26; Replace</td><td>When enabled, two fields will appear, allowing you to search for specific words and replace them. By default, partial matches within words are included, and the search is case-insensitive. For example, searching for “cat” would also match “Catalog”. To limit results to whole words only, enable "Full words". If you want to match words with the exact writing, enable <strong>"</strong>Consider upper and lower case letters.<strong>"</strong>.</td></tr><tr><td>Append</td><td>When enabled, the text entered in the group editor will be added to the existing value in the field of all edited records.</td></tr></tbody></table>



#### Options for Repeatable Fields

By default, the data entered in repeatable fields is added to already existing data. Other options are:

<table><thead><tr><th width="262">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Append [field] to end</td><td>This option adds the value from the selected field to the end of the existing value in the field of the selected records.</td></tr><tr><td>Prepend [field] to beginning</td><td>This option adds the value from the selected field to the beginning of the existing value in the field of the selected records.</td></tr><tr><td>Replace all</td><td>This option replaces every occurrence of the current value in the selected field across the selected records with the new value you provide. </td></tr><tr><td>Remove [field] if set</td><td>This option removes the value from the selected field only if it is currently present in the field of the selected records. For example, if you want to remove the keyword "cat" from all selected records, enter "cat" and enable this option.</td></tr><tr><td>Remove all</td><td>This option completely clears the values from the selected field in all the selected records, regardless of their current content.</td></tr><tr><td>Search &#x26; Replace</td><td>This option allows you to search for a specific value in the selected field and replace it with a new value.</td></tr></tbody></table>



### Asset Browser

Please refer to the general description of the asset browser.



### Footer

In the footer you find possible errors, for example mandatory fields. If configured in the data model, you can also enable comments so you can take notes about the things you've added. The group editor works in chunks, meaning by default 1.000 records are send to the server. With very complex data models, this can result in a timeout, then you'd need to set a lower chunk size using the pulldown in the footer.

