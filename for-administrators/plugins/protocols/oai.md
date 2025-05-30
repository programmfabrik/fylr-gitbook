---
description: >-
  The OAI/PMH endpoint allows accessing records in the OAI/PMH (XML) format
---

# OAI/PMH

The Open Archives Initiative Protocol for Metadata Harvesting (OAI/PMH) was first developed in the late 1990's as a standard for harvesting metadata from distributed metadata/data repositories. The current version of the OAI/PMH standard is 2.0 as of June 2002, with minor updates in December 2008.

More information about the standard can be found here: [http://www.openarchives.org/](http://www.openarchives.org/OAI/openarchivesprotocol.html)


## Configuration

OAI/PMH is configured in the base configuration tab ["Export and OAI/PMH"](/for-administrators/readme/export-and-deep-links.md#oai-pmh). In order to use it, first enable it using the checkbox and then fill in the nessary fields.

## Rights Management

The OAI endpoint is accessible without any authenticated Access Token, however it is protected by the rights management. Internally, the [System User](/for-administrators/permissions/user.md#system-user) `oai_pmh` is used to apply the rights. When the endpoint is called, the rights this user has are deciding which records are available.

Make sure that the `oai_pmh` user has the necessary read rights on all masks and objects which should be exposed over the OAI endpoint. Since the OAI endpoint is read only, all rights that allow writing have no effect. The rights can be applied in pools or objecttypes, just like for any other user or group.


### Identify

```
?verb=Identify
```

This returns information about the OAI/PMH endpoint.

Example:

```xml
<Identify>
    <repositoryName>fylr</repositoryName>
    <baseURL>[...]/api/v1</baseURL>
    <protocolVersion>2.0</protocolVersion>
    <earliestDatestamp>2024-08-01T08:38:07Z</earliestDatestamp>
    <deletedRecords>persistent</deletedRecords>
    <granularity>YYYY-MM-DDThh:mm:ssZ</granularity>
</Identify>
```

fylr provides the information configured in the base configuration tab "OAI/PMH" to identify the repository. The granularity offered is `"YYYY-MM-DDThh:mm:ssZ"` and the `deletedRecord` policy is set to `"persistent"`.

If the endpoint is called without any `verb`, the fallback is `Identify` and this information is shown.

## API

The OAI/PMH can be accessed under:

<mark style="color:blue;">`GET`</mark> `/api/v1/oai`

The parameters are defined in the external documentation: [Protocol Requests and Responses](https://www.openarchives.org/OAI/openarchivesprotocol.html#ProtocolMessages).


## Repository

The repository consists of all user objects that can be seen by the system user "OAI/PMH". That means, that the rights management settings allow to control which objects are offered via OAI/PMH.

The objects are identified by their UUID. The identifier format depends on the settings in the base configuration:

* If an optional namespace is specified, the identifier format is: `oai:<namespace>:<uuid>`
* If no namespace is specified, the identifier format is: `oai:<uuid>`

To get a single or multiple records, use

```
?verb=GetRecord&identifier=oai:...
```

or

```
?verb=ListRecords
```


## Metadata Formats

The easydb always disseminates all available formats to all objects. To get all available metadata formats, use

```
?verb=ListMetadataFormats
```

### Default XML Format

```
?metadataPrefix=easydb
```

The default metadata format that is always provided by fylr is the `easydb` export format. This format is basically an XML representation of the object in the given mask and it is very similar to the JSON representation that is normally used by the API.

### Dublin Core

```
?metadataPrefix=oai_dc
```

As per OAI/PMH standard, [Dublin Core](https://www.dublincore.org) is offered as the Metadata format `oai_dc`. It is possible to define mapping profiles for Dublin Core under "Profile" > "Dublin Core". These mapping profiles work like any other metadata mapping profile, so they can be configured per objecttype and pool.

The OAI/PMH will use the configured profile to generate the Dublin Core representation for the object. If no profile is configured, a minimal representation is returned.


### XSLT Formats

```
?metadataPrefix=xslt-<prefix>
```

Besides those two formats, more formats can be defined using the base configuration, tab "Export and OAI/PMH", table "XSLT formats".

There is a column "Name (OAI/PMH prefix, name in Deep-Links with /api/objects)" that is used to identify the XSLT file. The prefix must be conform to the standard and unique. Notice that `oai_dc` and `easydb` are already used. This prefix is used to format the metadata prefix: `xslt-<prefix>`.

To enable the XSLT file to be used as a Metadata Format for OAI/PMH, enable the Checkbox "Use for OAI/PMH". Make sure that you use XSLT files that output valid XML when activating them for OAI/PMH. Optionally, you can specify a namespace and a schema for the Metadata Format.

{% hint style="warning" %}
XSLT scripts must omit the XML declaration to allow valid XML to be returned!
{% endhint %}

Since the OAI/PMH endpoint merges multiple XML, it is important that the XML which is generated by the XSLT does not include the XML declaration `<?xml version="1.0"?>` in the first line.

To avoid this, define the output format of the XSLT as

```xml
<xsl:output method="xml" omit-xml-declaration="yes"/>
```

## Sets

fylr supports the following types of sets.

To get a list of all available sets, use

```
?verb=ListSets
```


### Objecttypes

All objecttypes.

Example for all objects of objecttype `sample_object`:

```xml
<setSpec>objecttype:sample_object</setSpec>
```

### Pools

All pools that the user "OAI/PMH" can see (`bag_read` right).

Example for all objects in the Standard Pool:

```xml
<setSpec>pool:1:2</setSpec>
```

### Collections

All collections that the user "OAI/PMH" can see (`bag_read` right).

Example:

```xml
<setSpec>collection:1:3</setSpec>
```

### Combination of pools and objecttypes

All combinations of pool managed objecttypes and pools that the user "OAI/PMH" can see (`bag_read` right)

Example for all objects of objecttype `sample_object` in the Standard Pool:

```xml
<setSpec>objecttype_pool:sample_object:pool:1:2</setSpec>
```

### Tagfilters

All names of tagfilters that have been configured in the base configuration. All sets based on tagfilters have the prefix `tagfilter:`

Example for all objects that are found by the Tagfilter `sample_tagfilter`:

```xml
<setSpec>tagfilter:sample_tagfilter</setSpec>
```
