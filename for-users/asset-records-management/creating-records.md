---
description: >-
  This article describes the process when creating new records and uploading new
  files.
---

# Creating Records

{% hint style="info" %}
Please note, that creating records is only possible for users with necessary permissions. Without the appropriate permissions, the option to create new records will not be available. Users needing permissions should contact their system administrator for assistance.
{% endhint %}



In the main navigation, users will find a plus (+) button. Clicking this button opens the "New Records" dialog, where files can be uploaded and records can be created.

On the right, users can upload files either by dragging and dropping them into the designated drop zone or by using the provided buttons to add files, directories, or URLs. Uploaded files can be removed, if uploaded falsely, by clicking on the little trash bin icon.



<table><thead><tr><th width="200">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td><strong>Object Type</strong></td><td>Select the appropriate object type for the records you are creating from the dropdown menu.</td></tr><tr><td><strong>Pool</strong></td><td>Choose the pool where the records will be stored.</td></tr><tr><td><strong>Mask</strong></td><td>Select the mask to be used for the records.</td></tr><tr><td><strong>Field For Files</strong></td><td>Specify the field where the files will be stored.</td></tr><tr><td><strong>Select Pools for Linked Records</strong></td><td>If your records will include links to other object types with pool management, select individual pools for each linked record that will be created by the metadata mapping.</td></tr><tr><td><strong>Metadata Mapping</strong></td><td>Choose the appropriate metadata mapping from the dropdown menu to extract metadata from the file and write it into specific fields. I no mapping is chose, the standard mapping for the pool / object type is used. If no mapping is configured, not metadata will be transferred.</td></tr><tr><td><strong>Detect Versions</strong></td><td>It allows the application to detect different versions of files with the same file name (e.g., "file.tif" &#x26; "file.jpg"). Instead of creating two records for "file.tif" &#x26; "file.jpg", only one record will be created that has these two versions of the same file.</td></tr><tr><td><strong>Detect Series</strong></td><td>Only available for data models that allow multiple files for records. It allows the application to detect series of files with the same file name (e.g.,"file-1.jpg" &#x26; "file-2.jpg" or "file 1.png" &#x26; "file 2.png"). Instead of creating two records for "file-1.jpg" &#x26; "file-2.jpg", only one record will be created that has these two files in the file field.</td></tr><tr><td><strong>Skip Duplication Check</strong></td><td>If you check this option, all duplicated assets will be uploaded anyway. This setting is persistent and applies to other uploads outside this dialog as well.</td></tr></tbody></table>

After configuring these settings and uploading the necessary files, you proceed by clicking the "Next" button at the bottom right of the dialog and continue to the actual input screen.



