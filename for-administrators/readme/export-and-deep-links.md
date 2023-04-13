---
description: >-
  In this section you can make settings for so-called deep links, IIIF and the
  OAI/PMH interface or upload XSLT files for exports.
---

# Export & Deep Links

## Use system object ID (instead of UUID)

If enabled the URL of the detail view uses the system object ID instead of the UUID.

## Deep Link Settings

If enabled, deep links can be used to access records in the system. The deep link releases are technically solved via the API interface `/api/objects`.

{% hint style="info" %}
Please note: you have to assign permissions to the system user "Deep Link" so the links are working. Users also need the system right "Deep Links" to access the links in the detail view.
{% endhint %}

{% hint style="info" %}
For more information on the deep links, please click here.
{% endhint %}

### Access by ID

Allows direct access by object ID.

{% hint style="info" %}
Caution: Because these object IDs are continually assigned, it can be a security risk to unblock this option. A user who is made aware of a deep link can guess further deep links. For all deep links, however, the  system user "Deep Link" must have access to the objects for them to work.
{% endhint %}

### Access by Column

Allows access by specific values in object columns.

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

Technical name.

In the Deep-Link interface, this XSLT can be applied by using `format/xslt/<xslt-name>`.

In the OAI/PMH interface, this is used as a metadata format (`metadataFormat=<name>`).

### Display Name

The display name will be shown in the export settings.

### Description

Description of the format (optional).

### Use for deep links with /api/v1/objects

Allow this XSLT to be used in the Deep-Link interface.

### Use for OAI/PMH

Allow this XSLT to be used in the OAI/PMH interface.

{% hint style="info" %}
Please note: since the OAI/PMH standard requires XML, make sure that the XSLT produces valid XML. Otherwise a internal parsing error can occur in the OAI/PMH plugin.
{% endhint %}

### Schema (only OAI/PMH)

XML Schema. Used for the namespace (`xmlns`) of the exported records.

### Namespace (only OAI/PMH)

XML Namespace. Used as the namespace of the exported records.

## OAI/PMH

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) is a protocol developed for harvesting metadata descriptions of records in an archive so that services can be built using metadata from many archives. An implementation of OAI-PMH must support representing metadata in Dublin Core, but may also support additional representations.

Enable OAI/PMH to let others harvest your data that's stored in FYLR.

More information about the standard can be found here: http://www.openarchives.org/

### Repository Name

Name of the OAI / PMH repository.

This information will be provided by the `Identify` verb as `repositoryName`

### Namespace

Freely definable OAI Identifier Namespace.

Objects can be requested using `oai:<namespace>:<uuid>` in the URL.

### Maximum Number of Records for ListRecords

Limit the number of records per page for the verb `ListRecords`.

### Embed Linked Records

As for the XML Export, linked objects are not loaded and embedded in the XML Document:

* If the option "All" is selected, all linked objects are loaded and embedded during the export.
* If "Not included in main search" option is selected, all linked objects that are not included in the main search are loaded.
* If "None" is selected, no linked objects are loaded, but only the standard is exported.

### Depth of Linked Records (1-9)

When linked objects are loaded and merged, this depth defines how many levels of linked objects are loaded (`1` - `9`). See [above](#depth-of-linked-records-1-9).

### TAG-SETS

Tagfilters can be used to specify more sets for OAI/PMH. Each tagfilter specifies a set. If a tagfilter set is requested, all records are returned where the tagfilter matches.

Tagfilter sets have the prefix `tagfilter:`, for example `<setSpec>tagfilter:sample_tagfilter</setSpec>` for all records that match the tagfilter `sample_tagfilter`.

To get a list of all available sets, use the verb `listSets`. (see http://www.openarchives.org/OAI/openarchivesprotocol.html#ListSets)

#### Set Name

Technical name of the set.

#### Tag Filter

Definition of the tag filter.

### Administrator Email

This information will be provided by the `Identify` verb as `adminEmail`.
