# Exporting

## General Info



## Export Dialogue



### Files

#### File Fields

Here you find all the fields that contain files. All files are grouped by object type and field and for each field you see all the filetypes that would be exported with a count.&#x20;

If you uncheck something here, no files and no links to files will be exported. If you want to include URLs in your XML or CSV file but not export the actual files, you have to leave the checkboxes enabled here and disable the settings in the next paragraph.

#### Files



#### URLs

When exporting CSV, Excel or XML files, you may want to include urls to the files associated with a record. By default, no URLs will be exported, so make sure to choose something from the following pulldowns.

For the original file you can choose from the following:

<table><thead><tr><th width="251.4453125">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>No</td><td>No URL will be exported.</td></tr><tr><td>Original</td><td>The URL of the original file will be exported.</td></tr><tr><td>Current Original</td><td>The URL of the preferred visible version of the file will be exported. For example, if you have rotated or cropped an image, this edited version is referred to as the "Current Original", while the unmodified file is referred to as the "Original". For files that have not been edited in fylr, the current original and the original are identical.</td></tr><tr><td>Original + Current Original</td><td>The URL of both the original file and the current original will be exported.</td></tr></tbody></table>



The groups "Small", "Medium" and "Huge" can contain no, one or multiple renditions. Please refer to your file worker settings to see which group contains which renditions.



### Data



### Advanced

Additional settings include:

<table><thead><tr><th width="199.94921875">OPTION</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>Batch Size</td><td>Define how many files are exported into a single folder. The default value is 100. You can set the batch size to Unlimited to export all records into one folder, or choose Custom to define a specific number per folder.</td></tr><tr><td>File Name</td><td>Define how the exported files are named. Use the standard template (which is configured by the administrator), keep the original file name, or enter a custom file name.</td></tr><tr><td>Embed Linked Records</td><td></td></tr><tr><td>Linked Files</td><td></td></tr><tr><td>Include Metadata</td><td>Activate this checkbox, if you wish to include all file metadata in JSON and XML exports.</td></tr><tr><td>Inheritance</td><td>In hierarchical records, fields inherited from superordinate records are exported by default. Deactivate this checkbox if only values stored directly in the record should be exported.</td></tr><tr><td>File Variants</td><td>Activate "Export File Variants" to include all additional file variants uploaded for a record in the export.</td></tr><tr><td>Range</td><td>If you wish to only export new and modified records in scheduled exports, please activate this checkbox. By default all records from your search, collection, selection are always exported.</td></tr><tr><td>Mask</td><td>Select a mask which should be used for exporting the data. If nothing is selected, the best mask is used.</td></tr></tbody></table>



### Scheduler

Exports can be scheduled so they run automatically. Just click on the little clock icon in the right bottom and choose a preset or define a custom schedule.



### Transport

Exports can be automatically send via email or delivered to a FTP or WebDav server. Just click on the little truck icon in the right bottom and add a transport to your export.&#x20;



## Export Manager

The export manager lets you access your previous exports. It's located in the header of the application on the left. You can download, edit, delete and restart your exports and check the status of longer running exports.

