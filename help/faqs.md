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

<details>

<summary>How to ensure a user can only upload a file in a given field, not other potential file fields?</summary>

Disallow the group to “Upload Files” into given fields **or** create a mask that excludes the other fields where we don’t want users to upload files to.

</details>

## Collections

<details>

<summary>How do I let users create collections themselves?</summary>

Make sure to assign the right "**Create Collections**" under "**Access Search**" in the **System Rights** tab of the **user** / the **group** you want to be able to create collections themselves

</details>

<details>

<summary>I want to share a collection with a specific user, but I don't see their name in the list of available users. </summary>

If the users you want to share the collection with are not visible in the user pulldown, you're missing permissions to see them. Ask your administrator to give you access to these users. They need to edit the group you want to share the collection with (let's say "Group A") and add your group (let's say "Group B") to the permissions and assign the right "View Users" and/ or "View Group".

</details>



## Search

<details>

<summary>How do I find records with empty / missing values for a given field?</summary>

First make sure your object type is enabled in the resources. Then open the expert search and find the field you want to search for. Next to the label, click the icon to search for records where this field has no data. Start the search and if needed, add more search terms or use the filters.

</details>

