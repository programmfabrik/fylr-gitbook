---
description: Here you find some frequently asked questions.
---

# FAQs

{% hint style="info" %}
Currently work in progress
{% endhint %}



## Upload

<details>

<summary> I have multiple files that belong together. How do I upload them?</summary>

First, you have to make sure your data model allows the upload of multiple files for one record (the upload field has to be in a repeatable/nested field). Then you can either name your files the same (with a numbering at the end, for example "file-1.jpg" & "file-2.jpg" or "file 1.png" & "file 2.png") and upload them together with "[Detect Series](../for-users/asset-records-management/creating-records.md#upload-area-and-settings)" enabled. Or, you can skip the upload screen and upload the files in the upload field of that empty record. In both cases you get one record with multiple files.

</details>

<details>

<summary>I want to upload new files to existing records. How do I do that?</summary>

You either have to search and edit the record you want to add the files to and then upload them by adding one new repeatable upload field where you then upload them from your computer. Or, you have to use the so called [upload collections](../tutorials/how-to-set-up-the-hotfolder-and-file-system-connect/setting-up-an-upload-collection.md) to add new files to existing records automatically by matching them using the file names.

</details>

<details>

<summary>What's the difference between "Detect Versions" and "Detect Series"?</summary>

When "[Detect Versions](../for-users/asset-records-management/creating-records.md#upload-area-and-settings)" is enabled in the uploading process, files with the same file name but different file types (for example: "file.tif" & "file.jpg") will be uploaded as different variants together in one upload field, whereas with "[Detect Series](../for-users/asset-records-management/creating-records.md#upload-area-and-settings)" files with the same file name and a numbering (for example: "file-1.jpg" & "file-2.jpg" or "file 1.png" & "file 2.png") will be uploaded into the same nested upload field. Both settings will create just one record instead of records for each uploaded file.

</details>

