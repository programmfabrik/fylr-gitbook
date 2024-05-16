---
description: Step by step tutorial on how to generate JSON Payloads
---


# Using the JSON Importer

This is a step by step tutorial on how to generate JSON Payloads, that can be imported into **fylr** using the [JSON importer](../README.md) in the frontend.

The importer reads a [manifest](steps.md#1-import-manifest) that defines the import and loads a list of payloads. Each payload is stored in a file. Each payload contains tge definition of the API endpoint, and a list if JSON objects that define basetypes or user objects. Mixed types in payloads are not allowed. All payloads are then posted to the API in the order of the payload list.

This tutorial uses an [example datamodel](datamodel.md#datamodel-to-download) that covers most (but not necessarily all) aspects of importing payloads.

Here, we will focus on the structure of the payloads. However, the payload files can be generated using any sources and tools that allow the output of valid JSON files. Each source material needs specialized tools to convert the data into payloads.

All steps of the tutorial can be found [here](steps.md).

### Names used in this tutorial

* *Basetypes*:
    * Basetype objects like tags, users, groups or pools
    * These always have the same structure and are not defined in the datamodel
* *Objects*, *User objects*, *Record*:
    * Objects defined in the datamodel (by the user), that contain the actual data
    * Here, objects means *user objects*, in contrast to *basetype objects*

### The general steps

#### 1. Write the [Import Manifest](steps.md#1-import-manifest)

* The import manifest is read by the importer and contains information about the payload URI and batch size, and most important, a list of all payload files
* The filenames of all payloads that are generated have to be added to the payload list in the order in which they have to be imported

#### 2. Create payloads for [basetypes](steps.md#2-payloads-for-basetypes)

* [Tags](steps.md#tags)
* [Groups](steps.md#groups)
* [Users](steps.md#users)
* [Pools](steps.md#pools)

#### 3. Create payloads for [user objects](steps.md#3-payloads-for-user-objects)

These are actual **fylr** objects that contain data

* [Simple objects](steps.md#simple-linked-objects) that are linked in main objects
* [Main objects](steps.md#main-objects) that link to simple objects

#### 4. Collections

Import [collections](steps.md#4-collections) and collection objects

#### 5. Update imported objects (optional)

If necessary, [update imported objects](steps.md#5-updating-of-imported-objects) to link to objects that could not be referenced in the first import round.

#### 6. Start import process

Load the manifest in the JSON Importer and [start the migration](steps.md#6-starting-the-migration)

### Important things to consider

* The order of importing is important!
    * Every object that is referenced by another object, must have already imported in a different payload, otherwise a database error can be caused
    * Every parent of a hierarchical basetype or object must have been imported before
        * Hierarchical objects must be imported level by level
        * This means the payloads have to be sorted to represent a breadth first search of the hierarchical tree
    * Linked objects that are referenced must have been imported before

* Masks should not be used for importing, since values might be ignored if they are not enabled in the mask
    * Always use `"_mask": "_all_fields"` so that all fields are imported without any limitations

{% hint style="info" %}
The easiest way to see how a payload is formatted, is to capture the POST/PUT request that is sent by the frontend when a basetype or object is saved. In a browser, open the developer console and find the network tab to see the requests.

Save an object in the editor in the frontend, and find the request that is performed. The body of the post request contains an object JSON represantation, which has exactly the same structure as the objects in the payloads that are used here.
{% endhint %}

### Using lookups instead of IDs

Every object is identified by the `_id`. If you reference a basetype or object in another basetype or object, you need to know its ID, so that they can be linked. These IDs are assigned in the server to any new inserted object.

Since during migration, the IDs are not known yet, you need to use lookups. All basetypes have a unique field `reference`, that is used to find the object using a lookup, instead of referencing it by ID.

For user objects, you can use any unique (and not empty) text/string field for referencing the object, or you add an extra field in the datamodel, that can be used as a reference.


### Basic payload structure

Each payload file must contain a JSON object with the following structure:

```json
{
  "import_type": "db",
  "objecttype": "bilder", // only needed for import_type "db"
  "objects": []
}
```

All Payloads must define an `import_type` and an array of objects. Each object in the array defines a single basetype or user object. The import type specifies the API endpoint. For `db`, which is the endpoint for user objects, you also must specify the `objecttype`.

* Tags:
    * import type: `tags`
    * array name: `tags`

* Groups:
    * import type: `group`
    * array name: `groups`

* Users:
    * import type: `user`
    * array name: `users`

* Pools:
    * import type: `pool`
    * array name: `pools`

* Collections:
    * import type: `collection`
    * array name: `collections`

* User Objects:
    * import type: `db`
    * array name: `objects`
    * `objecttype` must be set

