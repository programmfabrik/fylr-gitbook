---
description: >-
  This article describes the process of creating new records and uploading new
  files.
---

# Creating Records

{% hint style="info" %}
Please note, that creating records is only possible for users with necessary permissions. Without the appropriate permissions, the option to create new records will not be available. Users needing permissions should contact their system administrator for assistance.
{% endhint %}



In the main navigation, users will find a plus (+) button. Clicking this button opens the "New Records" dialog, where files can be uploaded and records can be created.

## **Upload Area & Settings**

SCREENSHOT

In the "New Records" dialog, users can upload files either by dragging and dropping them into the designated drop zone or by using the provided buttons to add files, directories, or URLs. Uploaded files can be removed if uploaded incorrectly by clicking on the trash bin icon.

<table><thead><tr><th width="179">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Object Type</strong></td><td>Select the appropriate object type for the records you are creating from the dropdown menu. This ensures that the records are categorized correctly.</td></tr><tr><td><strong>Pool</strong></td><td>Choose the pool where the records will be stored. This determines the location within the system where the records will reside.</td></tr><tr><td><strong>Mask</strong></td><td>Select the mask (template) to be used for the records. This template dictates the layout and structure of the record fields.</td></tr><tr><td><strong>Field For Files</strong></td><td>Specify the field where the files will be stored. This indicates which field within the record will hold the uploaded files.</td></tr><tr><td><strong>Select Pools for Linked Records</strong></td><td>If your records will include links to other object types with pool management, select individual pools for each linked record created by the metadata mapping. This is an optional setting that ensures linked records are stored in their appropriate pools.</td></tr><tr><td><strong>Metadata Mapping</strong></td><td>Choose the appropriate metadata mapping from the dropdown menu to extract metadata from the file and write it into specific fields. If no mapping is chosen, the standard mapping for the pool/object type is used. If no mapping is configured, no metadata will be transferred.</td></tr><tr><td><strong>Detect Versions</strong></td><td>This option allows the application to detect different versions of files with the same file name (e.g., "file.tif" &#x26; "file.jpg"). Instead of creating two records for "file.tif" &#x26; "file.jpg", only one record will be created that includes these two versions of the same file.</td></tr><tr><td><strong>Detect Series</strong></td><td>This setting is only available for data models that allow multiple files for records. It allows the application to detect series of files with the same file name (e.g., "file-1.jpg" &#x26; "file-2.jpg" or "file-1.png" &#x26; "file-2.png"). Instead of creating two records for "file-1.jpg" &#x26; "file-2.jpg", only one record will be created that includes these two files in the file field.</td></tr><tr><td><strong>Skip Duplication Check</strong></td><td>If you check this option, all duplicated assets will be uploaded anyway. This setting is persistent and applies to other uploads outside this dialog as well, ensuring that no duplicates are inadvertently missed.</td></tr></tbody></table>

After configuring the settings and uploading the necessary files, proceed by clicking the "Next" button at the bottom right of the dialog to continue to the actual input screen, also known as the editor.

## **Editor Screen**

The editor screen is divided into three main sections: Navigation Pane, Input Area, and Preview.

SCREENSHOT

### **Navigation Pane**

On the left side of the screen, the navigation pane displays a template record and a list of records being created. The template record can be used to enter data that applies to all the records being created. For example, entering a title in the template record will assign the same title to all records upon saving.

Users can also select a record from this list to view or modify its details. If a metadata mapping is applied, the value will be shown as a placeholder in the field and can be overwritten manually. By default, values from the template record overwrite values from the metadata mapping. To prevent this, disable "Values from the template record overwrite the metadata mapping." You can use the clipboard button to copy the values of the selected record to the template record.

Additionally, new files or directories can be uploaded, or empty records can be created by clicking the plus (+) button. Files can be removed from the editor by clicking the minus (-) button.

### **Input Area**

The middle of the screen is the main input area. Users can change the mask in the upper left if their data model and permissions allow it. Ensure all mandatory fields for all records are filled out to save the record(s). Mandatory fields are marked in red, and records with missing input are also marked with a warning triangle. Click on "Details" at the bottom to see what is preventing you from saving the record(s).

### **Preview**

When a specific record with a file is selected, a preview of the file is shown on the right. Here, users can utilize features of the asset browser such as zooming, using the video player, or downloading the file. The preview can be closed by clicking on the image icon at the top. Clicking the right arrow will disconnect the preview from the editor and expand its view. Click the left arrow to reconnect it to the editor. The width of the preview and editor can be adjusted using the drag handle.



Once all files have been uploaded and all data has been entered, create the records by clicking "Save." Note that the editor will close, and you will be directed to the search. From there, you can edit the records individually or in group mode.

## Copying Records

New records can also be created by copying existing records. You find the copy button in the 3-dot-menu of the detail view and the editor. Choose between the following options:

<table><thead><tr><th width="241">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Copy With Reverse</td><td>Copies the record with all its reverse linked records.</td></tr><tr><td>Copy Without Reverse</td><td>Copies the record without its reverse linked records.</td></tr><tr><td>Copy As Adhoc Template</td><td>Copies the record as the adhoc template so its data can be applied to new or existing records. Please note, the adhoc template will be lost after logging out.</td></tr></tbody></table>

## Importing Records

You can also create new records by using the [CSV Importer](../../for-administrators/tools/csv-importer/), the [JSON Importer](../../for-administrators/tools/json-importer/) or the [Hotfolder](../../tutorials/how-to-set-up-the-hotfolder-and-file-system-connect/).

