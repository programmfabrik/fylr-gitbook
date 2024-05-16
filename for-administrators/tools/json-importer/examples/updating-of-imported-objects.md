---

---

# Updating of imported objects

In some cases, it might be necessary to update objects during the migration process, for example if there are links to objects that did not exist yet at the time of the first import. In this case, it is possible to update existing objects by using lookups for the object ID, and incrementing the object version.

In this example, we want to link the first `bilder` object we created (with the reference "bild_01") to the first `objekte` object with the `inventarnummer` "987654321". For referencing the objects, we can use lookups for the IDs with fields that we know are unique and not empty in the existing objects. The direct link between these objects is from the `bilder` object to the `objekte` object, in contrast to the [reverse nested link](payloads-for-user-objects.md#reverse-linking-of-bilder-in-objekte) in the examples before.


{% hint style="info" %}
Make sure to include all values in the update of the object, that you want to save in the object. Since the server would delete all values that are not set, they need to be inlcuded.

The latest version of any imported object will define all values in the object.
{% endhint %}

## Lookup for object ID

To reference the object for the update, instead of specifying the `_id` (which was not inlcuded in the first version), use a lookup for the reference "bild_01", which was set in the first object version:

```json
"lookup:_id": { "reference": "bild_01" }
```

## Incremented version

The version can be specified directly, so you can set `"_version": 2`, if you know that this is the first update. For every update, the version must be exactly one more than the current version. Otherwise, this will cause an error.

If you do not want to keep track of object versions, you can use the JSON Importer feature which will care for setting the correct version: replace `"_version": 2` with

```json
`"_version:auto_increment": true`.
```

## Link to the `objekte` object

From the perspective of the `objekte` object, the reverse nested link has the structure of a nested table, since one `objekte` object can be referenced by multiple `bilder` objects.

On the other hand, any `bilder` object can only have one link to one `objekte` object. So from the perspective of `bilder`, it is a normal link to an `objekte` object. We know that the unique field in the `objekte` object is `inventarnummer`, and the value we specified is "987654321". So the lookup in the link is the following:

```json
"objekte": {
  "_objecttype": "objekte",
  "_mask": "_all_fields",
  "objekte": {
    "lookup:_id": {
      "inventarnummer": "987654321"
    }
  }
}
```

## Complete Payload

The complete payload for the bilder object(s) looks like this:

```json
{
  "import_type": "db",
  "objecttype": "bilder",
  "objects": [
    {
      "_mask": "_all_fields",
      "_objecttype": "bilder",
      "bilder": {
        "_pool": {
          "pool": {
            "lookup:_id": {
              "reference": "migrated_objects"
            }
          }
        },
        "lookup:_id": {
          "reference": "bild_01"
        },
        "reference": "bild_01",
        "_version:auto_increment": true,
        "titel": {
          "de-DE": "Berliner Fernsehturm",
          "en-US": "Berlin TV Tower"
        },
        "aufnahmedatum": {
          "value": "2020-04-04"
        },
        "datei": [
          {
            "eas:url": "https://images.unsplash.com/photo-1560930950-5cc20e80e392?w=800&q=80",
            "eas:filename": "berlin-tv-tower.jpg",
            "preferred": true
          }
        ],
        "aufnahmeort": {
          "_mask": "_all_fields",
          "_objecttype": "orte",
          "orte": {
            "lookup:_id": {
              "name": "Berlin"
            }
          }
        },
        "_nested:bilder__personen": [
          {
            "bemerkung": "Fotograf",
            "person": {
              "_mask": "_all_fields",
              "_objecttype": "personen",
              "personen": {
                "lookup:_id": {
                  "name": "Max Mustermann"
                }
              }
            }
          }
        ],
        "_nested:bilder__schlagwoerter": [
          {
            "schlagwort": {
              "_mask": "_all_fields",
              "_objecttype": "schlagwoerter",
              "schlagwoerter": {
                "lookup:_id": {
                  "name": "Stadt"
                }
              }
            }
          },
          {
            "schlagwort": {
              "_mask": "_all_fields",
              "_objecttype": "schlagwoerter",
              "schlagwoerter": {
                "lookup:_id": {
                  "name": "Panorama"
                }
              }
            }
          }
        ],
        "objekte": {
          "_objecttype": "objekte",
          "_mask": "_all_fields",
          "objekte": {
            "lookup:_id": {
              "inventarnummer": "987654321"
            }
          }
        }
      }
    }
  ]
}
```

Save this payload as `userobject-bilder-0-version-2.json` and add the filename to the manifest.
