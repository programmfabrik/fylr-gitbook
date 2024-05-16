---

---

# Collections

Objects can be assgigned to new collections after the objects have been migrated. As an example, we create a collection for the Root user, where images of landscapes are stored.

The new collection will get the base user collection for Root with the reference "user:ref:system:root" as its parent:

```json
"lookup:_id_parent": {
    "reference": "user:ref:system:root"
}
```

It is important to allow adding objects to this collection by setting `"objects_allowed": true`.

The objects inside the collection are referenced in the array `_objects` next to each `collection` object. Each object is referenced by using a lookup for the `_global_object_id`, which requires the objecttype and a field-value-pair.

The objecttype of the collection object is `objekte`, and we want to reference the object where the field `inventarnummer` has the value `112233`:

```json
{
  "lookup:_global_object_id": {
    "_objecttype": "objekte",
    "inventarnummer": "112233"
  }
}
```

The payload for the collection looks like this:

```json
{
  "import_type": "collection",
  "collections": [
    {
      "_basetype": "collection",
      "collection": {
        "lookup:_id_parent": {
          "reference": "user:ref:system:root"
        },
        "_version": 1,
        "reference": "landscapes",
        "children_allowed": true,
        "objects_allowed": true,
        "displayname": {
          "de-DE": "Landschaften",
          "en-US": "Landscapes"
        },
        "type": "workfolder"
      },
      "_objects": [
        {
          "lookup:_global_object_id": {
            "_objecttype": "objekte",
            "inventarnummer": "112233"
          }
        }
      ]
    }
  ]
}
```

Save this payload as `basetype-collection-0.json` and add the filename to the manifest.

