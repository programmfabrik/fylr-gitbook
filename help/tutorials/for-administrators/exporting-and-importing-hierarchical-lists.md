# Exporting & Importing Hierarchical Lists

## General Information

When transferring hierarchical lists from one fylr instance to another, some things need to be considered. Records in hierarchies do not need to be unique (we recommend it though). This means that you can have multiple records with the same name in one hierarchy. It also means that hierarchies cannot be build based on the name of the records itself. Instead fylr uses the globally unique system object id's to build hierarchies. This also means you can change the name of a record anytime without breaking the hierarchy. But it also makes transferring hierarchical lists from one fylr to another a bit more complicated because each fylr instance has their own unique system object id's. The following steps will guide you.

## Export

The first step is exporting the hierarchical list. We recommend going to the "Lists" and then use the 3 dot menu in the search to "Export Search".

In the popover, enable "Output CSV" on the first tab and leave the pulldown on "Without Hierarchy". If you have multi-language fields you should also enable "Export all data languages".

Click save, give the export a name and download the file.

## Import Preparations

Because every fylr has their own unique system object id's, you cannot use the system object id's from the source straight away to build the hierarchy. You need to create a new field in the data model for the old system object id and then use this migration field to create the hierarchies. So simply go to the data model, edit the object type and add a new field. This field should be unique and can be of type text or string. Don't forget to enable the field in the mask as well and commit the changes.

## Import

When the data model is prepared and the export was done, you need to use the CSV Importer to import the hierarchy. Simply open the CSV Importer and upload the CSV file. For the fields "CSV Field Names" and "Target Field Names" choose "1. Row" as well as the object type and mask on the first tab. The mapping is done automatically if the data model is identical.

Next check the import mapping in the second tab. Remove fields that you don't want to import and add the fields that couldn't be mapped. Make sure to set the "\_id\_parent" to the migration field you have created earlier. This makes sure the hierarchy is build correctly.

Click prepare and import and then it's done.

