---

---

# Payloads for basetypes

Basetype payloads should always be imported first since they are referenced in most user objects. There is no strict order of the basetypes, but you have to consider that they can reference each other. Since circular references between basetypes are possible, importing of second versions of the basetypes might be needed (update migration).

Possible, but not exclusive, references between basetypes:

* Tags:
    * do not reference other basetypes
    * can be referenced by all other basetypes by tagfilter based rights management
    * tags, users, groups as part of the rightsmanagement

* Groups:
    * tags, users, groups as part of the rightsmanagement

* Users:
    * can reference groups (as being inside a group)
    * tags, users, groups as part of the rightsmanagement

* Pools:
    * hierachical, so pools reference other pools as a parent
    * tags, users, groups as part of the rightsmanagement

----

## Tags

Tags belong to tag groups. We add a tag "Public Access" to a new tag group "Tag Group 1". To reference this tag later, it will get the reference `"public"`.

The tag group and the tag(s) inside the group are stored in one JSON object. The object is added to the array of the payload:

```json
{
  "import_type": "tags",
  "tags": [
    {
      "taggroup": {
        "displayname": {
          "en-US": "Tag Group 1"
        },
        "reference": "taggroup1",
        "type": "checkbox"
      },
      "_tags": [
        {
          "tag": {
            "displayname": {
              "en-US": "Public Access"
            },
            "displaytype": "facet",
            "enabled": true,
            "frontend_prefs": {
              "webfrontend": {
                "color": "green",
                "icon": "fa-eye"
              }
            },
            "is_default": false,
            "reference": "public",
            "sticky": false,
            "type": "individual"
          }
        }
      ]
    }
  ]
}
```

Save this file as `basetype-tags.json` and add this filename to the payload list in the manifest.


----

## Groups

We create a group, to which migrated users will be assigned. Any user who is in this group, will have the right to use the search function in the frontend, and manage collections.

The group will be named "Migrated Users", and it will get the reference `"migrated_users"`.

The group payload is:

```json
{
  "import_type": "group",
  "groups": [
    {
      "_basetype": "group",
      "group": {
        "_version": 1,
        "displayname": {
          "en-US": "Migrated Users"
        },
        "reference": "migrated_users"
      },
      "_system_rights": {
        "system.search": {
          "has_own_collections": true,
          "show_fixed_searches": false
        }
      }
    }
  ]
}
```

Save this file as `basetype-groups.json` and add this filename to the payload list in the manifest.


----

## Users

Add a test user and assign it to the group "Migrated Users".

We name the user "Max Mustermann", with the easydb login `"mustermann"` and the password `"password123"`. The reference of the user will be `"mustermann"`.

To add the new user to the group "Migrated Users", use the lookup `"lookup:_id"` for the group reference `migrated_users`.

The user payload is:

```json
{
  "import_type": "user",
  "users": [
    {
      "_basetype": "user",
      "user": {
        "type": "easydb",
        "login": "mustermann",
        "first_name": "Max",
        "last_name": "Mustermann",
        "reference": "mustermann",
        "_version": 1
      },
      "_password": "password123",
      "_groups": [
        {
          "_basetype": "group",
          "group": {
            "lookup:_id": {
              "reference": "migrated_users"
            }
          }
        }
      ]
    }
  ]
}
```

Save this file as `basetype-users.json` and add this filename to the payload list in the manifest.


----

## Pools

Any empty easydb always contains two system pools:

* "All pools" (reference: `"system:root"`)
    * "Default pool" (reference: `"system:standard"`) (child of `system:root`)

All pools have to be inserted into this hierarchy. Any new pool needs to have a parent.

For this tutorial, we create a new pool "Migrated Objects" and use "All pools" as the parent pool. To reference it later, set the reference to `"migrated_objects"`.

Instead of setting the parent pool using `"_id_parent": 1`, we have to use the lookup to let the server find the ID of "All pools". The lookup is done by replacing `"_id_parent": 1` with

```json
"lookup:_id_parent": { "reference": "system:root" }`
```

Add the pool JSON object to a pool payload. This payload is defined as:

```json
{
  "import_type": "pool",
  "pools": [
    {
      "_basetype": "pool",
      "pool": {
        "lookup:_id_parent": {
          "reference": "system:root"
        },
        "_version": 1,
        "reference": "migrated_objects",
        "name": {
          "en-US": "Migrated Objects"
        }
      }
    }
  ]
}
```

Save this file as `basetype-pools.json` and add this filename to the payload list in the manifest.

