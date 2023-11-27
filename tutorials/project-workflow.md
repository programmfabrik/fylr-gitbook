---
description: >-
  This tutorial describes what information needs to be gathered when starting a
  new project and in which order fylr should be set up.
---

# Project Workflow

## Gather Information

First, you need to gather some information from your customers. This includes the data model (which fields they need), rights management (which user groups they need), installation (amount of files, URL, ...) and migration (data that should be imported).

### Data Model

For setting up the data model, you need at least:

* Field name (how should the field be called)
* Field type (should it a single-line or multi-line field, a list, a date field, a number or an upload field)
* Multiple field (should the field be assigned to the record multiple times or not)
* List type (should it be a simple list or a hierarchical list)

Depending on the complexity and the customer's knowledge, the following information should be gathered:

* Mandatory fields
* Multi-language fields
* Fields for standard view
* Fields for text view
* Fields for table view
* Fields for full text search
* Fields for expert search
* Fields for the filter
* Splitter
* Preview versions
* Metadata mapping

### Rights Management

To set up the user groups and permissions, the following information should be gathered:

* Name of the groups
* Permissions of the groups
* Tags & Workflows
* Name of the pools
* Anonymous access?
* Self-Registration?
* Collection sharing?
* ...

### Installation

To decide on the server size and setup, gather the following information:

* Storage size of the assets&#x20;
* Number of assets
* Frontend URL
* Authentification services

### Migration

In case you're not migrating from easydb5 or start with an empty fylr, you should ask for the structure of the existing data and how it should be imported.



## Setting Up

When all the information is gathered, fylr can be set up.

### Installation

Please refer to [installation](../for-system-administrators/installation/), [configuration](../for-system-administrators/configuration/) and [backups](../for-system-administrators/backup.md) for more information and make sure to get a [license](../license-management.md).

### Base Configuration

Stuff you might want to configure:

* General > Title
* General > Logo, Favicon
* General > Background Image & Color, Marker Color
* User Management
* Languages
* E-Mail
* Export & Deep Links
* File Worker
* Services

### Data Model

When creating the data model, follow these tips:&#x20;

* Create the object types for the lists first so you can link to them.
* If you work with multiple masks, first finish one mask and then copy this mask and make the changes to prevent having to make adjustments twice.
* Use "Number of new fields" to create multiple fields at once.
* When adding new fields to existing object types make sure to activate them in the mask(s), otherwise they won't be available.
* ...

### Metadata Mapping

Once the data model is done, you can set up the metadata mapping (if needed).

* ...

### Tags & Workflows

If needed, create the tag groups and tags, so you can use them for the permissions.

For more information, please refer to ["Tags & Workflows"](../for-administrators/permissions/tags-and-workflows.md).

### Groups

In case there are groups with (almost) the same system rights, create one group with all the needed settings first and then copy this group, change the name and adjust the system rights to save some time.

If you configured anonymous access, make sure to set up the system rights for the group "Anonymous Users" (at least enable "Access Search").

If you want to use collection sharing, make sure to set up the system rights for the group "Pseudo users to see single collections" and "Users invited by e-mail" (at least enable "Access Quick Access (Without Search)").

For more information, please refer to ["Groups"](../for-administrators/permissions/groups.md).

### Object Types

Define for each object type which user group should get which permissions on this list. Please keep in mind, that groups need at least "View Records" and "Allowed Masks" to use the expert search. It could make sense, to assign these two permissions to the group "All users" and then only add the groups that should get more than just read permissions to this object type.

Use the copy & paste buttons on the bottom to copy single permissions or all permissions from one object type to another.

For more information, please refer to ["Object Types"](../for-administrators/permissions/object-types.md).

### Pools

Create the pools which are needed and set up the permissions. Permissions which apply to all pools should be set up for "All pools" (as permissions are inherited). Permissions that should be used for multiple pools (but not all) can be configured at one pool and then the pool (including the permissions) can be copied. Alternatively use the copy & paste buttons on the bottom to copy single permissions or all permissions from one pool to another.

In case you use a metadata mapping, choose the default mapping for:

* XMP/IPTC/EXIF Import Profile
* XMP/IPTC/EXIF Export Profile

In case you need watermarked version, upload a watermark file.

For more information, please refer to ["Pools"](../for-administrators/permissions/pools.md).



## Migration

...
