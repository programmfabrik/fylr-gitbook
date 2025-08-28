---
description: frequently asked questions
---

# FAQs

## Keyboard Shortcuts

The following shortcuts are available to all users for faster navigation and efficiency.&#x20;

{% hint style="info" %}
The user account needs the permissions to execute the underlying function.
{% endhint %}

| Shortcut                                | Description                         |
| --------------------------------------- | ----------------------------------- |
| **Ctrl / Option / Command + N**         | Create new record                   |
| **Ctrl / Option / Command + A**         | Select all records                  |
| **Ctrl / Option / Command + D**         | Open download popover for selection |
| **Ctrl / Option / Command + E**         | Open expert search                  |
| **Ctrl / Option / Command + S**         | Save                                |
| **Shift + Ctrl / Option / Command + E** | Open export popover for selection   |

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

<details>

<summary>How do I let a user only upload a certain type of file to a specific field, e.g. only images?</summary>

Depending on if you manage an Object Type by itself or if you are using pool management, you find the solution to this problem inside the Rights Management section of Fylr.&#x20;

You can provide the right "Upload File" to groups/ users and define, which field in which Object Type should only have a certain type of File.&#x20;

The options for a field are: Image, Office, Video, Audio, Unknown

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

<details>

<summary>How do I enable / disable searching in documents?</summary>

Fylr only searches in a document if "full text" is enabled in the mask for the file field. Disabling excludes this field from the search.

</details>

## For Administrators

<details>

<summary>An API-Script suddenly started failing</summary>

Did you recently create [Messages](https://docs.fylr.io/for-administrators/messages), that users had to confirm after logging in? Login with your API users credentials and confirm the messages, the API-Script should work as usual afterwards.

</details>

<details>

<summary>Emails are not sent</summary>

After setting up the requirements for the mail server in the "Email" section of the base configuration, make sure to enable "Email Notifications" in the base configurations "Services".

</details>

<details>

<summary>I added a new field to an object type and cannot see it in the fylr UI</summary>

After adding a new field to an object type, saving and committing the new datamodel are required.  Additionally a reindex is required to update the Index with the new column.

If you still don't see a field in frontend of fylr, you probably forgot to **enable the new field in the masks**. For this field in your mask of choice, select the desired visibility options and define interactive elements. Again, saving, committing and a reindex are required.

</details>
