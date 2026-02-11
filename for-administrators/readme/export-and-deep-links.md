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

### Access by ID

Allows direct access by the object ID. Example: https://\<your-fylr-url>/api/v1/objects/id/\<id>.

{% hint style="info" %}
Caution: Because these object IDs are continually assigned, it can be a security risk to enable this option. A user who is made aware of a deep link can guess further deep links. For all deep links, however, the system user "Deep Link" must have access to the records for them to work.
{% endhint %}

### Access by Column

Allows access by specific values in object type columns (they have to be unique). Example: https://\<your-fylr-url>/api/v1/objects/column/\<object-type>/\<name-of-unique-column>/\<value>.<br>

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

When IIIF is used, FYLR supports the [Presentation API 3.0](https://iiif.io/api/presentation/3.0). The manifest is assembled automatically depending on the mask requested. See [https://iiif.io/api/presentation/3.0/#requiredstatement](https://iiif.io/api/presentation/3.0/#requiredstatement) for  details. You should use the required statement for copyright information and general information about your database.

#### Label

The label of the required statement.

#### Value

The text for the required statement, this is formatted as [Markdown](https://commonmark.org) with Table, Strikethrough, Linkify and TaskList enabled.

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

In the OAI/PMH interface, this is used as a metadata format (`metadataFormat=xslt-<name>`).

### Display Name

The display name will be shown in the export settings.

### Description

Description of the format (optional).

### **Custom Content-Type**

This optional field allows you to manually define the `Content-Type` header returned by a Deeplink endpoint when an XSLT transformation is applied.

In most cases, **you do not need to set anything here**.

If the field is left empty (recommended), the system assumes that the XSLT produces **XML**.

You should only provide a custom value if:

* Your XSLT transformation does **not** produce XML (e.g., JSON, HTML, plain text), **and**
* Your consuming client strictly relies on the correct `Content-Type` header.

### Use for deep links with /api/v1/objects

Allow this XSLT to be used in the [Deep Link interface](#deep-link-settings).

### Use for OAI/PMH

Allow this XSLT to be used in the [OAI/PMH interface](#oaipmh).

{% hint style="info" %}
Please note: since the OAI/PMH standard requires XML, make sure that the XSLT produces valid XML. Otherwise an internal parsing error can occur in the OAI/PMH endpoint.
{% endhint %}

### OAI/PMH only

These settings are only relevant if the XSLT transformation is intended for use with OAI/PMH. In all other cases, these can be ignored.

#### Schema

XML Schema. Used for the namespace (`xmlns`) of the exported records.

#### Namespace

XML Namespace. Used as the namespace of the exported records.

#### XPath Query

For the OAI/PMH format, the result of the XSLT must be split into single objects, which will then each be included in the `<record>` nodes. The XPath defines the node in the *resulting XML after the XSLT* has been applied, at which each new record starts. The XPath must include the XML namespace prefix, if the XSLT includes a namespace in the output.

E.g. the resulting XML of a XSLT transformation has the following structure:

```xml
<lido:lido xmlns:lido ="http://www.lido-schema.org">
  <!-- object #0 -->
  <lido:lido>
    <lido:lidoRecID>001</lido:lidoRecID>
    <!-- [...] -->
  </lido:lido>
  <!-- object #1 -->
  <lido:lido>
    <lido:lidoRecID>002</lido:lidoRecID>
    <!-- [...] -->
  </lido:lido>
</lido:lido>
```

The XPAth to separate the distinct records is

```xml
lido:lido/lido:lido
```

This will result in the following output in the OAI/PMH endpoint for a `?verb=ListRecords` request:

```xml
<?xml version="1.0" encoding="utf-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/">
  <request verb="ListRecords" metadataPrefix="xslt-lido">/api/v1/oai</request>
  <ListRecords>
    <!-- object #0 -->
    <record>
      <header>
        <!-- [...] -->
      </header>
      <metadata>
        <lido:lido>
          <lido:lidoRecID>001</lido:lidoRecID>
          <!-- [...] -->
        </lido:lido>
      </metadata>
    </record>
    <!-- object #1 -->
    <record>
      <header>
        <!-- [...] -->
      </header>
      <metadata>
        <lido:lido>
          <lido:lidoRecID>002</lido:lidoRecID>
          <!-- [...] -->
        </lido:lido>
      </metadata>
    </record>
  </ListRecords>
</OAI-PMH>
```

### **Responsibility & Support**

Please note:

* The **content generated by an XSLT** is entirely determined by the XSLT itself.
* We **cannot provide support for invalid output** caused by custom XSLT transformations.
* The correctness and validity of the transformed data are the responsibility of maintainer who created or uploaded the XSLT.

However:

* If you need assistance **creating** an XSLT or want us to develop one for you, we are happy to help on request.

## OAI/PMH

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) is a protocol developed for harvesting metadata descriptions of records in an archive so that services can be built using metadata from many archives. An implementation of OAI-PMH must support representing metadata in Dublin Core, but may also support additional representations.

Enable OAI/PMH to let others harvest your data that's stored in FYLR.

More information about the standard can be found here: [http://www.openarchives.org/](http://www.openarchives.org/).

### Repository Name

Name of the OAI/PMH repository.

This information will be provided by the `Identify` verb as `repositoryName`

### Namespace

Freely definable OAI Identifier Namespace.

Records can be requested using `oai:<namespace>:<uuid>` in the URL.

### Maximum Number of Records for ListRecords

Limit the number of records per page for the verb `ListRecords`.

### Embed Linked Records

As for the XML export, linked records are not loaded and embedded in the XML Document:

* If the option "All" is selected, all linked records are loaded and embedded during the export.
* If "Not included in main search" option is selected, all linked records that are not included in the main search are loaded.
* If "None" is selected, no linked records are loaded, but only the standard is exported.

### Depth of Linked Records (1-9)

When linked records are loaded and merged, this depth defines how many levels of linked records are loaded (`1` - `9`). See [above](export-and-deep-links.md#depth-of-linked-records-1-9).

### TAG-SETS

Tag filters can be used to specify more sets for OAI/PMH. Each tag filter specifies a set. If a tag filter set is requested, all records are returned where the tag filter matches.

Tag filter sets have the prefix `tagfilter:`, for example `<setSpec>tagfilter:sample_tagfilter</setSpec>` for all records that match the tag filter `sample_tagfilter`.

To get a list of all available sets, use the verb `listSets` (see [http://www.openarchives.org/OAI/openarchivesprotocol.html#ListSets](http://www.openarchives.org/OAI/openarchivesprotocol.html#ListSets)).

#### Set Name

Technical name of the set.

#### Tag Filter

Definition of the tag filter.

### Administrator Email

This information will be provided by the `Identify` verb as `adminEmail`.
