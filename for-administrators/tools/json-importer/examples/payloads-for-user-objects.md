---

---

# Payloads for user objects

Here we will create payloads for objects of different objecttypes, as well as linking these objects together using lookups.

## Simple linked objects

These objects are simple and are not linking other objects.

### Orte (`orte`)

This objecttype is hierarchic. Each field contains a link (`_id_parent`) to reference its parent. Instead of `_id_parent`, we will use `lookup:_id_parent` instead. The unique field that is used for reference is `name`. Apart from this, there are no other fields in this objecttype.

All user objects consist of meta-fields, and an object with the actual data under a key which must be the same as the value of `_objecttype`. For importing, always use the `_mask` `_all_fields`.

We will create the following hierarchical structure of places:

* Europa
    * Deutschland
        * Berlin
        * Brandenburg

There are four levels, so we need to upload the objects in four different payloads in the following order: `["Europa"]`, `["Deutschland"]` and `["Berlin", "Brandenburg"]`. So we make sure that the parent has always been imported already before it is referenced.

**Payload #1**

The structure for the user object payloads is always the following:

```json
{
  "import_type": "db",
  "objecttype": "orte",
  "objects": []
}
```

The objects have the following structure:

```json
{
  "_objecttype": "orte",
  "_mask": "_all_fields",
  "orte": {
    "_id_parent": null,
    "_version": 1,
    "name": "Europa"
  }
}
```

On top level, the `_objecttype` and `_mask` must be defined. The value of `_objecttype` is `"orte"`, so we define the object itself under the key `orte`.

In `orte`, the `_id_parent` is `null` (or it can also be not set at all), since this object is on the top level of the hierarchy and has no parent.

Every imported object must have the `_version`, since it is a object that will be newly created.

The actual data "Europa" is saved under the key `name`. The key is the same as the internal field name in the datamodel.

The complete first payload looks like this:

```json
{
  "import_type": "db",
  "objecttype": "orte",
  "objects": [
    {
      "_objecttype": "orte",
      "_mask": "_all_fields",
      "orte": {
        "_id_parent": null,
        "_version": 1,
        "name": "Europa"
      }
    }
  ]
}
```

Save this payload as `userobject-orte-level-0.json` and add the filename to the manifest.

For hierarchical objects it is good practice to include the hierarchy level in the payload filenames to make sure they are in the correct order.

**Payload #2**

Define the object that contains the name "Deutschland", which is a child of "Europa".

The complete second payload looks like this:

```json
{
  "import_type": "db",
  "objecttype": "orte",
  "objects": [
    {
      "_objecttype": "orte",
      "_mask": "_all_fields",
      "orte": {
        "lookup:_id_parent": {
          "name": "Europa"
        },
        "_version": 1,
        "name": "Deutschland"
      }
    }
  ]
}
```

The parent object is referenced by the field `name` in `lookup:_id_parent`. The only key in this object is the field name, and the value is the value of this field in the database. This feature only works, if you know that the field is set and unique for all objects of this objecttype.

Here we tell the server to use the ID of the object with `name = "Europa"` as the parent ID.

Save this payload as `userobject-orte-level-1.json` and add the filename to the manifest.

**Payload #3**

On this level, there are two objects, that both have the same parent "Deutschland". Both can be saved in the same payload, since they are not depending on each other in any way.

The complete second payload looks like this:

```json
{
  "import_type": "db",
  "objecttype": "orte",
  "objects": [
    {
      "_objecttype": "orte",
      "_mask": "_all_fields",
      "orte": {
        "lookup:_id_parent": {
          "name": "Deutschland"
        },
        "_version": 1,
        "name": "Berlin"
      }
    },
    {
      "_objecttype": "orte",
      "_mask": "_all_fields",
      "orte": {
        "lookup:_id_parent": {
          "name": "Deutschland"
        },
        "_version": 1,
        "name": "Brandenburg"
      }
    }
  ]
}
```

Save this payload as `userobject-orte-level-2.json` and add the filename to the manifest.

----

### Personen (`personen`)

This objecttype is not hierarchical, so all objects can be saved in the same payload:

```json
{
  "import_type": "db",
  "objecttype": "personen",
  "objects": [
    {
      "_objecttype": "personen",
      "_mask": "_all_fields",
      "personen": {
        "_version": 1,
        "name": "Max Mustermann",
        "adresse": "Straße 123\n45678 Stadt"
      }
    },
    {
      "_objecttype": "personen",
      "_mask": "_all_fields",
      "personen": {
        "_version": 1,
        "name": "Peter Tester"
      }
    }
  ]
}
```

Note that you can use the newline character `\n` in multiline text fields (`adresse` in first object). Also you can leave any field empty, as long as it has no `NOT NULL` constraint or any other check constraints that do not allow empty fields (missing key `adresse` in second object).

Save this payload as `userobject-personen.json` and add the filename to the manifest.

----

### Schlagwörter (`schlagwoerter`)

This objecttype is not hierarchical, so all objects can be saved in the same payload:

```json
{
  "import_type": "db",
  "objecttype": "schlagwoerter",
  "objects": [
    {
      "_objecttype": "schlagwoerter",
      "_mask": "_all_fields",
      "schlagwoerter": {
        "_version": 1,
        "name": "Stadt"
      }
    },
    {
      "_objecttype": "schlagwoerter",
      "_mask": "_all_fields",
      "schlagwoerter": {
        "_version": 1,
        "name": "Panorama"
      }
    }
  ]
}
```

Save this payload as `userobject-schlagwoerter.json` and add the filename to the manifest.

----

## Main objects

Here we create the payloads for the more complex main objects (objects that can be found in the main search). These objects can have assets, tags, pools, links to the other simple objects we created before, and have links to eachother.

### Bilder (`bilder`)

This objecttype is used to save images as well as additional information about the time and place the picture was taken, and who was the photographer.

We create an object that saves this image from [unsplash.com](https://unsplash.com/photos/pN684G33h_M):

![](https://images.unsplash.com/photo-1560930950-5cc20e80e392?w=640&q=80)

Fields that are set in the object:

**`pool`**

The pool must be specified for all objects with pool management. We want to add the new objects to the pool ["Migrated Objects"](#pools) by referencing the pool `reference` instead of the `_id`:

```json
"_pool": {
  "pool": {
    "lookup:_id": {
      "reference": "migrated_objects"
    }
  }
}
```

**`reference`**

To be later able to reference this object, use the field `reference` to set a unique value. Other than for basetypes, this field is part of the schema and must be included in the datamodel. Set the reference to "bild_01", so later you can use a lookup to [link to this object](#reverse-linking-of-bilder-in-objekte) in a `objekte` object:

```json
{
  "lookup:_id": {
    "reference": "bild_01"
  }
}
```

**`titel`**

This is a multi language field, so under the key, there is an object with language codes and the translations for each language. Here we set the title for german and english:

```json
{
  "de-DE": "Berliner Fernsehturm",
  "en-US": "Berlin TV Tower"
}
```

**`datei` (asset)**

The image is saved in the asset field `datei` in the object. During the import, the images must be hosted and are loaded over HTTP(S). You can save the images in the same server where the payloads are stored, and use the server url, or use an image from any other HTTP server.

To tell the JSON Importer which file should be uploaded to the EAS and linked in the object, you have to specify the URL of the file. The Importer will load the file from the URL and upload it. So, replace `_id` with `eas:url`:

```json
{
  "eas:url": "https://images.unsplash.com/photo-1560930950-5cc20e80e392?w=800&q=80",
  "eas:filename": "berlin-tv-tower.jpg",
  "preferred": true
}
```

{% hint style="warning" %}
There must always be one asset that is set as `"preferred": true`
{% endhint %}

To specify a filename that overwrites the filename that is associated with the URL, especially if it does not contain an actual filename, use the optional key `eas:filename`. This filename will be passed to the EAS during file upload.

**`aufnahmedatum` (date field)**

This is a date field, so under the key, there is an object with the `value` and the date representation in `YYYY-MM-DD` format:

```json
{
  "value": "2020-04-06"
}
```

**`aufnahmeort` (link to objecttype [`orte`](#orte-orte))**

This is a link to another object. Instead of linking it using the `_id`, the object is referenced in a lookup by the unique field `name` (the same as in the hierarchical lookup for the parent ID):

```json
{
  "aufnahmeort": {
    "orte": {
      "lookup:_id": {
      "name": "Berlin"
      }
    },
    ...
  }
}
```

This creates a link to the `orte` object with the `name` "Berlin".

**`personen.person` (links in nested table to objecttype [`personen`](#personen-personen))**

There are multiple links to objects of type `personen` inside a nested table. The nested table `personen` has the fields `bemerkung` and `person`. The field for the nested table in the datamodel consists of the prefix `nested:`, the objecttype name and the name of the nested table: `"_nested:bilder__personen"`.

`bemerkung` is a free text field, `person` is the link to the `personen` object.

Instead of linking it using the `_id`, the object is referenced in a lookup by the unique field `name`:

```json
{
  "person": {
    "personen": {
      "lookup:_id": {
      "name": "Max Mustermann"
      }
    },
    ...
  }
}
```

Each element in the array `"_nested:bilder__personen"` represents a row in the nested table. In this example, we will add one row to the nested table, which contains the link to `person` "Max Mustermann", and the `bemerkung` field "Fotograf".

Combined, the entry for the linked object in the nested table, looks like this:

```json
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
]
```

**`schlagwoerter.schlagwort` (links in nested table to objecttype [`schlagwoerter`](#schlagwörter-schlagwoerter))**

There are multiple links to objects of type `schlagwoerter` inside a nested table. `schlagwort` is the link to the `schlagwoerter` object.

Instead of linking it using the `_id`, the object is referenced in a lookup by the unique field `name`:

```json
{
  "schlagwort": {
    "schlagwoerter": {
      "lookup:_id": {
        "name": "Stadt"
      }
    },
    ...
  }
}
```

A second object in the nested table can be added by referencing the second object by the `name` "Panorama".

Combined, the entry for the linked objects in the nested table, looks like this:

```json
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
]
```

#### Complete Payload

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
        "_version": 1,
        "reference": "bild_01",
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
        ]
      }
    }
  ]
}
```

Save this payload as `userobject-bilder-0.json` and add the filename to the manifest.

----

### Objekte (`objekte`)

This is the other main object. It has pool management, and can have tags.

Fields that are set in the object:

**`pool`**

Add the new object to the pool ["Migrated Objects"](#pools) by referencing the pool `reference` instead of the `_id`.

**`tags`**

Tags are set in an array next the object, at the top level key `_tags`. Each object in the array is one tag. Instead of using the tag ID, reference the tag ["Public Access"](#tags) by using the lookup for the reference "public":

```
"_tags": [
  {
    "lookup:_id": {
      "reference": "public"
    }
  }
]
```

**`inventarnummer`**

This is a simple text field, the value can be assigned directly.

**`datierung` (date range field)**

This is a date range field, so under the key, there is an object with the start date (`from`) and the end date (`to`). Both values contain the date representation in `YYYY-MM-DD` format:

```json
{
  "from": "2020-04-01",
  "to": "2020-04-08"
}
```

#### Complete Payload

The complete payload for the bilder object(s) looks like this:

```json
{
  "import_type": "db",
  "objecttype": "objekte",
  "objects": [
    {
      "_mask": "_all_fields",
      "_objecttype": "objekte",
      "_tags": [
        {
          "lookup:_id": {
            "reference": "public"
          }
        }
      ],
      "objekte": {
        "_pool": {
          "pool": {
            "lookup:_id": {
              "reference": "migrated_objects"
            }
          }
        },
        "_version": 1,
        "datierung": {
          "from": "2020-04-01",
          "to": "2020-04-08"
        },
        "inventarnummer": "987654321"
      }
    }
  ]
}
```

Save this payload as `userobject-objekte-0.json` and add the filename to the manifest.

----

### Reverse linking of `bilder` in `objekte`

The objecttype `objekte` contains a reverse editable link to the objecttype `bilder`. This means, in the JSON there is nested table where multiple `bilder` objects can be linked. These linked objects can be edited directly in the `objekte` object which contains them. Escpecially, this means they can be created inline. By adding a `bilder` object inside the reverse linked table in the payload for a new `objekte` object, you can create multiple objects at the same time.

We create an object that saves this image from [unsplash.com](https://unsplash.com/photos/425Czbxtyug) inside its internal `bilder` object.

![](https://images.unsplash.com/photo-1583268426351-53cd67fefed9?w=600&q=80)

Add the `bilder` object, including the `eas:url` and other fields, directly in the reverse nested table `_reverse_nested:bilder:objekte`. This nested table can include multiple `bilder` objects, that link back to this object, and can be directly edited inside this object.

The `bilder` and `objekte` objects both need a lookup to the pool, and the top level object has a lookup for the tag.

#### Complete Payload

The complete payload for the bilder object(s) looks like this:

```json
{
  "import_type": "db",
  "objecttype": "objekte",
  "objects": [
    {
      "_mask": "_all_fields",
      "_objecttype": "objekte",
      "_tags": [
        {
          "lookup:_id": {
            "reference": "public"
          }
        }
      ],
      "objekte": {
        "_pool": {
          "pool": {
            "lookup:_id": {
              "reference": "migrated_objects"
            }
          }
        },
        "_version": 1,
        "inventarnummer": "112233",
        "datierung": {
          "from": "2020-04-01",
          "to": "2020-04-07"
        },
        "_reverse_nested:bilder:objekte": [
          {
            "_pool": {
              "pool": {
                "lookup:_id": {
                  "reference": "migrated_objects"
                }
              }
            },
            "_version": 1,
            "reference": "bild_02",
            "titel": {
              "de-DE": "Berglandschaft",
              "en-US": null
            },
            "aufnahmedatum": {
              "value": "2020-04-01"
            },
            "datei": [
              {
                "eas:url": "https://images.unsplash.com/photo-1583268426351-53cd67fefed9?w=600&q=80",
                "preferred": true
              }
            ],
            "_nested:bilder__schlagwoerter": [
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
            ]
          }
        ]
      }
    }
  ]
}
```

Save this payload as `userobject-objekte-1.json` and add the filename to the manifest.

