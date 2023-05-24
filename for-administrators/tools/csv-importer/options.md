---
description: >-
  The CSV importer offers various settings and options, which will be explained
  below.
---

# Options

{% hint style="info" %}
Please also read the [general information](general-information.md) before importing data with the CSV importer.
{% endhint %}



## Import Settings <a href="#import-einstellungen" id="import-einstellungen"></a>

After uploading a file in the "CSV File" field, the following settings are available:

<table><thead><tr><th width="225.5">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>CSV File</td><td>First click on this button to select a CSV file for the import. Via the "X" you can remove the file again.</td></tr><tr><td>CSV Field Names</td><td>Select the row where the column names are located so that they are not imported as records.</td></tr><tr><td>Target Field Names</td><td>Select the row that contains the target field names so the import mapping is done automatically and they are not imported. The notation is explained in the <a href="general-information.md">general information</a>.</td></tr><tr><td>Object Type</td><td>Select the object type you want to import the data into.</td></tr><tr><td>Pool</td><td>Select the pool in which the new records should be created. The pool is set only when records are inserted. If existing records are updated via the CSV importer, the pool will not be changed. For this purpose, please use the group editor.</td></tr><tr><td>Mask</td><td>Select  the mask which should be used for the import.</td></tr><tr><td>File Upload Method</td><td><p>Select a method for uploading files. For more details please check the file upload example.</p><p><strong>Direct</strong>: The file is downloaded and then uploaded with /eas/put.</p><p><strong>URL (Remote PUT)</strong>: The file is not downloaded and /eas/put is accessed directly from the file URL. The file is downloaded from the server and uploaded. (This option is the fastest).</p><p><strong>Ignore Files</strong>: All files will be ignored and not imported.</p></td></tr><tr><td>Metadata Mapping</td><td>Select the metadata mapping that should be applied when importing files.</td></tr><tr><td>Tag Mode</td><td>Select whether tags from the CSV file should be added to existing tags or should replace existing ones when updating records.</td></tr><tr><td>Field for Updates</td><td>By selecting the default entry "- Insert New -" all rows of the CSV file will be created as new records in FYLR. Select a field here to identify existing records and update them with the contents from the CSV file. Please note that you must first select fields in the "Import Mapping" tab so that they are available in this pulldown. Select the file field if you have file names in your CSV and want to update records using the file name. In case of multilingual fields you have then the possibility to make the matching over a certain language (e.g. name#de-DE or name#en-US).</td></tr><tr><td>Append Records in Nested Fields</td><td>By default, when updating existing records in FYLR, all records in nested fields (i.e. keywords) are replaced by the content from the CSV file. With this option, in case of nested fields, the content from the CSV file will be appended to the existing records instead. Use this option, for example, to add keywords in addition to those already assigned to the record.</td></tr><tr><td>Append Records in Reverse Nested Fields</td><td>By default, when updating existing records in FYLR, all records in reverse nested fields (i.e. images) are replaced by the content from the CSV file. With this option, in case of reverse nested fields, the content from the CSV file will be appended to the existing records instead. Use this option, for example, to add images in addition to those already assigned to the record.</td></tr><tr><td>Create Linked Records</td><td>Specify whether linked records should be created during the actual import or not. If this option is switched off, all linked records must already exist in FYLR. If you click on "Prepare", a corresponding message will appear if the CSV file refers to records that could not be found in FYLR. </td></tr><tr><td>Pool for Linked Records</td><td>This option only appears if the selected object type refers to another object type for which pool management is also activated. This means that different pools can be specified for linked records.</td></tr><tr><td>Comment</td><td>Enter a comment for the CSV import, which will appear in the change history of the imported / updated records.</td></tr><tr><td>Chunk Size</td><td>Size of the processing chunks that are sent to the server. In case of very complex data models and data volumes, a timeout may occur. In this case, try using a smaller chunk size.</td></tr><tr><td>Show Display Names</td><td>If activated, the second tab "Import Mapping" for the FYLR fields will show the display names from the editor/detail. Otherwise the internal field names from the data model are used.</td></tr></tbody></table>

## Overview <a href="#informationen" id="informationen"></a>

Below the import settings, an import overview is displayed after preparing. The checkboxes are used to filter the entries in the table view.

| NAME       | DESCRIPTION                                                          |
| ---------- | -------------------------------------------------------------------- |
| Rows       | Number of rows in the CSV file                                       |
| Ready      | Number of rows ready to import                                       |
| Invalid    | Number of rows that are invalid                                      |
| Processing | Number of rows that are currently being processed                    |
| Done       | Number of rows that have been finished                               |
| Errors     | Number of rows with errors                                           |
| Warnings   | Number of rows that can be imported but for which there is a warning |
| Inserts    | Number of rows / records that would be inserted                      |
| Updates    | Number of rows / records that would be updated                       |
| Deletes    | Number of rows / records that would be deleted                       |

## &#x20;<a href="#import-mapping" id="import-mapping"></a>

## Import Mapping <a href="#import-mapping" id="import-mapping"></a>

Fields for which no mapping has been selected will not be changed when updating records that already exist in FYLR. Fields for which a mapping has been selected, but for which there is no content in the CSV file, will be emptied when updating records.



## Table View <a href="#tabellen-ansicht" id="tabellen-ansicht"></a>

In the table view you can see the data from your CSV file. After preparing and importing, additional information is automatically added (recognizable by the column names "fylr|"). What information this is, you can read at the end of this article in the "[Protocol](options.md#protokoll)" section.

## Record Preview <a href="#datensatz-vorschau" id="datensatz-vorschau"></a>

In the "Record Preview" tab you can see the data that would be imported according to the import mapping. Please note that this is only a preview of the mapped fields. When updating already existing records the result may differ.

## JSON Preview <a href="#json-vorschau" id="json-vorschau"></a>

In the "JSON Preview" tab you can see the data that would be imported according to the import mapping in the JSON structure.



## Options <a href="#aktionen" id="aktionen"></a>

The lower part of the CSV importer contains the following functions:

| BUTTON                   | DESCRIPTION                                                                                                                                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reload                   | Reloads the CSV file and discards any information already loaded by preparing it.                                                                                                                                                 |
| Download CSV             | When preparing and after saving, more information is generated, which is written back to your CSV file (see table below). With "Download CSV" you can save this file to your desktop.                                             |
| Download Import Settings | Download the configured import settings and the import mapping as a JSON file.                                                                                                                                                    |
| Upload Import Settings   | Upload the JSON file with the import settings and import mapping.                                                                                                                                                                 |
| Prepare                  | Prepares the CSV import. This includes checking the data, as well as searching for existing and linked records.                                                                                                                   |
| Insert                   | Starts the actual CSV import and inserts all new records. Already existing records will not be updated.                                                                                                                           |
| Update                   | Starts the actual CSV import and updates existing records. Not yet existing records will not be created. Note, however, that empty columns in the CSV will cause the update to empty the contents of these fields in the records. |
| Insert & Update          | Performs both inserts and updates directly one after the other.                                                                                                                                                                   |

## Protocol <a href="#protokoll" id="protokoll"></a>

After preparing and after importing certain information is generated by FYLR. These can be seen in the table view in the CSV importer or can be downloaded as a CSV file after the import.

| ROW                            | DESCRIPTION                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fylr\|row\_idx                 | Number of the row, starting with 0                                                                                                                                                                                                                                                                                                                   |
| fylr\|operation                | Action that will be performed ("insert", "update", "delete")                                                                                                                                                                                                                                                                                         |
| fylr\|status                   | Import status ("ready", "invalid", "failed", "done"). Rows with status "invalid" cannot be imported (example: wrong date format). Rows with the status "failed" were not imported correctly (example: mandatory field violation).                                                                                                                    |
| fylr\|timestamp                | Date + time when the import/update/deletion of the CSV import                                                                                                                                                                                                                                                                                        |
| fylr\|status\_text             | Contains further information about the error that occurred in the case of the status "invalid" and "failed"                                                                                                                                                                                                                                          |
| fylr\|warning\_text            | Contains more information in case of trying to import invalid JSON into custom data type fields                                                                                                                                                                                                                                                      |
| fylr\|id                       | ID of the record found in FYLR (for records created by CSV import this column remains empty)                                                                                                                                                                                                                                                         |
| fylr\|version                  | Version of the record                                                                                                                                                                                                                                                                                                                                |
| fylr\|id\_parent               | ID of the parent entry (only for hierarchical object types)                                                                                                                                                                                                                                                                                          |
| fylr\|depth                    | Depth of the record (only for hierarchical object types), starting with 0                                                                                                                                                                                                                                                                            |
| fylr\|path                     | Path of the record (only for hierarchical object types)                                                                                                                                                                                                                                                                                              |
| fylr\|eas\_ids\|file           | Contains the internal EAS id of the file uploaded via the CSV importer (see Upload files).                                                                                                                                                                                                                                                           |
| fylr\|eas\_ids\|file\|metadata | Contains the metadata taken from the file uploaded via the CSV importer (see Upload files).                                                                                                                                                                                                                                                          |
| fylr\|_object type_\|_mask_    | For all linked object types a separate column is generated. After preparing you can see whether the entries referred to already existed (an ID is displayed for them), whether they are newly created (they appear with "new") or, if the option "Create linked entries" is deactivated, whether they were not found (they appear with "searching"). |
