---
description: >-
  In this section you can make settings for so-called deep links, IIIF and the
  OAI/PMH interface or upload XSLT files for exports.
---

# Export & Deep Links

## Use system object ID (instead of UUID)

If enabled the URL of the detail view uses the system object ID instead of the UUID.&#x20;



## Deep Link Settings

If enabled, deep links can be used to access records in the system.&#x20;

{% hint style="info" %}
Please note: you have to assign permissions to the system user "Deep Link" so the links are working. Users also need the system right "Deep Links" to access the links in the detail view.
{% endhint %}

{% hint style="info" %}
For more information on the deep links, please click here.
{% endhint %}

### Access by ID



### Access by Column



### Embed Linked Records

Decide wether you want to embed linked records in the xml that can be accessed via a deep link or not. Linked records are for example persons, locations, keywords. If you want to include not only the standard text and the id of those linked records but all the data from these object types (like name and contact information of the photographer), you need to choose an option that's not "No records".

| OPTION                                                  | DESCRIPTION                                                                                                                                                                                    |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All                                                     | The data of the linked records of all object types will be included in the xml file that can be accessed via a deep link.                                                                      |
| Records not included in the main search                 | Only data of the linked records of object types that are not shown in the main search will be included in the xml file that can be accessed via a deep link.                                   |
| Records not included in the main search, unless reverse | Only data of the linked records of object types that are not shown in the main search, unless they are reverse records, will be included in the xml file that can be accessed via a deep link. |
| No records                                              | The data of the linked records will never be embedded.                                                                                                                                         |



### Depth of Linked Records (1-9)

Define how many levels of linked records should be embedded. Choose "1" if you for example want to embed all the fields from the object type "Photographer" that is linked to your images (like name, contact information, etc.). If the photographer record itself links to another object type (i.e. locations) and you want this data in the xml of the image record, choose a depth of "2".



### IIIF REQUIRED STATEMENT

#### Label

#### Value



## XSL Transformations

When exporting records as xml, a default FYLR structure is used. If you want to export data in a specific xml format, you can use XSLT. You can define multiple transformations that can be accessed in the xml export settings.

{% hint style="info" %}
Please note: FYLR currently only support XSLT 1.0.
{% endhint %}

### XSLT File

Upload a valid XSLT file.

### Name



### Display Name

The display name will be shown in the export settings.

### Description

### Use for deep links with /api/v1/objects

### Use for OAI/PMH

### Schema (only OAI/PMH)

### Namespace (only OAI/PMH)



## OAI/PMH

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) is a protocol developed for harvesting metadata descriptions of records in an archive so that services can be built using metadata from many archives. An implementation of OAI-PMH must support representing metadata in Dublin Core, but may also support additional representations.

Enable OAI/PMH to let others harvest your data that's stored in FYLR.

### Repository Name

### Namespace

### Maximum Number of Records for ListRecords

### Embed Linked Records

### Depth of Linked Records (1-9)

### TAG-SETS

#### Set Name

#### Tag Filter

### Administrator Email
