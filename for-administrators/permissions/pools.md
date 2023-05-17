---
description: >-
  Pools can be understood as folders where you can place your files or records.
  For pools, permissions can be configured so that different user groups get
  different access to the records.
---

# Pools

## Use Cases

Pools can be used to structure your files and data. This can be based on content, permissions or workflows. Some examples include:

| USE CASE    | EXAMPLE POOLS                                                                                                                                        | DESCRIPTION                                                                                                                                                                                                                                                                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content     | <ul><li>Events</li><li>Stock Photos</li><li>Icons</li><li>Videos</li><li>Documents</li><li>...</li></ul>                                             | Structure your files and data based on content to quickly select the content you are looking for. Use different object types or masks to have different data fields in each pool.                                                                                                                                                              |
| Permissions | <ul><li><p>Department 1</p><ul><li>Project 1</li><li>Project 2</li><li>...</li></ul></li><li>Department 2</li><li>Department 3</li><li>...</li></ul> | Most common use of pools. Create pools and user groups for each department, so you, for example, can specify that each department can only access their own records.                                                                                                                                                                           |
| Workflows   | <ul><li>Upload Pool</li><li>Main Pool</li><li>Archive</li><li>...</li></ul>                                                                          | Sometimes it can make sense to reflect your workflows as pools. All new files will be uploaded in the "Upload Pool" and once they're finished (all data has been entered) they can be moved to the "Main Pool". This does not have to be, but can be, combined with permissions so only records in the main pool can be accessed by all users. |



## Working with Pools

Each FYLR installation comes with the "Standard Pool". The pool can't be deleted but renamed to use it for the above mentioned purposes. Pools can be structured hierarchical, meaning you can have super- and subordinate pools. By default, permissions will be inherited by the subordinate pools (this can be disabled though, please see [below](pools.md#permissions)). You can use the system pool "All Pools" to assign permissions that should apply to all pools. This pool is only for administrative purposes though, user cannot link records to this system pool.

To create new pools, click on the plus button on the lower left. By default, the pool will be created below "All Pools". If you select a pool before clicking on the plus, you can create a new pool below the selected one. To delete a pool, select it and click the minus button. You can copy a pool by selecting it and click on "Copy" on the lower right of the pool settings. Use the filter to search for the name, description, reference and short name of pools.

{% hint style="info" %}
Please note, that right now it's not possible to change the hierarchical structure of the pools afterwards. In that case, please create a new pool in the desired level, move all records to the new pool and delete the old one.
{% endhint %}



## Pool Settings

{% hint style="info" %}
Pool settings can be extended with custom plugins.&#x20;
{% endhint %}

### General

| OPTION                                | DESCRIPTION                                                                                                                                                                                                                                               |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                                    | Pool identifier. Will be assigned automatically.                                                                                                                                                                                                          |
| Owner                                 | Owner of the pool. Will be assigned automatically.                                                                                                                                                                                                        |
| Contact Person                        | Contact person of the pool. Users can access the contact person in the pool details.                                                                                                                                                                      |
| Name                                  | Name of the pool how it's displayed for users.                                                                                                                                                                                                            |
| Description                           | Description of the pool. Users can access the description in the pool details.                                                                                                                                                                            |
| Internal Comment                      | Internal comment for the pool. Will not be shown anywhere else.                                                                                                                                                                                           |
| Reference                             | Reference of the pool. Has to be unique. Can then be used for [CSV imports](../tools/csv-importer/) or the API.                                                                                                                                           |
| Short Name                            | Short name of the pool. Has to be unique. Can then be used for [CSV imports](../tools/csv-importer/) or the API and as a deep link: `https://<your-fylr-url>/pool/<short-name-of-the-pool>` (opens your FYLR instance and preselects the specified pool). |
| Standard XMP/IPTC/EXIF Import Mapping | Default metadata mapping which will be used when user upload a file with the standard mapping. Can be chosen when uploading files (data will be extracted from the file and written into data fields).                                                    |
| Standard XMP/IPTC/EXIF Export Mapping | Default metadata mapping which will be used when user download a file with the standard mapping. Can be chosen when downloading files (data will be written into the file itself) or when exporting records (data will be written into a XML file then).  |
| Standard Dublin Core Export Mapping   | Default Dublin Core metadata mapping which then will be used for [OAI/PMH](../readme/export-and-deep-links.md#oai-pmh). Mapping does not appear in the frontend when downloading or exporting records.                                                    |
| Created                               | Date and time the pool was created.                                                                                                                                                                                                                       |
| Last Updated                          | Date and time of the last update of the pool.                                                                                                                                                                                                             |



### Watermark

Watermark settings will be inherited by subordinate pools. Meaning, if you set up a watermark for a pool, all files in subordinate pools will get a watermark version, too. This cannot be prevented.

| OPTION         | DESCRIPTION                                                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Watermark File | Upload an image that should be used as a watermark for all previews. We recommend using images with a transparent background. |
| Transparency   | Define the transparency of the watermark from 0 (no transparency) to 100 (full transparency).                                 |
| Position       | Define where the watermark image should be placed on the previews. Will be ignored if "Tiled" is enabled.                     |
| Size           | Define the size of the watermark image.                                                                                       |
| Tiled          | Enable to cover the whole preview image with the watermark file. It will be repeated in the specified size.                   |

{% hint style="info" %}
Please note, that watermarked preview images are only rendered, if they are specified in the [base configuration](../readme/file-worker.md).
{% endhint %}



### Masks

This tab is only interesting, if you work with multiple masks. If you only have one mask per object type, you can ignore the settings here.

Each object type with pool management activated will appear here. By default, all records in this pool will be rendered in all masks you created for the object type(s) in the data model. If you, for example, only want the records to be rendered in one of the masks, disable "From Superordinate Pool" (or "From Object Type" if you're working on the pool "All Pools") and drag all masks that should not be rendered for records in this pool, under the gray line.

Imagine you have the object type "Files" and one mask for images and one mask for videos and let's say, one pool for a video project where you'll never have any images. It would be a waste of storage, if there would be two documents in the ElasticSearch index for the same record as they would only be used with one mask anyway. Whereas if you work with a full mask for your editors and a reduced mask for external guests, you would want all records to be rendered in both masks.



### Tags

By default, all [globally defined tags](tags-and-workflows.md) are available in all pools. If you want to disable certain tags in specific pools, you have to enable "Use Individual Tags" in the lower right. You then see all the tags above and can disable individual tags or make them a default.&#x20;

Tags that are "Persistent" globally can't be disable here.

&#x20;

### Workflows

By default, all [globally defined workflows](tags-and-workflows.md) are available in all pools. If you want to disable certain tags in specific pools, you have to enable "Use Individual Workflows" in the lower right. You then can set up individual workflows. For more details, please refer to ["Tags & Workflows"](tags-and-workflows.md).&#x20;

Workflows that are "Persistent" globally can't be disable here.



### Permissions

Define which user / user groups can, for example, view, download, edit or delete the records in this pool.&#x20;

By default, permissions are inherited from superordinate pools. If you want to disable this for  specific pools, you have to enable "Ignore Permissions from Superordinate Pools" in the lower right. You then can set up individual permissions that only apply for this pool. Permissions that are "Persistent" on superordinate pools will still be applied to subordinate pools.

Please refer to [Permissions](./) for more details.

