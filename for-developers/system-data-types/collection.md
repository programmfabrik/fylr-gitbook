# collection

The system data type `collection` is a **user-managed set of objects** — a workfolder, a basket, a saved search, a share. Collections form a tree, can be shared with ACL grants, exposed over WebDAV, and published. They are managed through the [`/api/v1/collection`](../api/endpoints/collection/README.md) endpoints.

The mutable collection data sits under the `collection` key; counts, ACL, tree info and other read-only or system fields sit at the top level.

## Fields

| Field | Format | Description |
| --- | --- | --- |
| `collection` | `object` | The mutable collection data. |
| `collection._id` | `int64` | Server-issued id. |
| `collection._version` | `int64` | Object version. A new collection uses `1`; an update must send the current version + 1. |
| `collection._id_parent` | `int64` (nullable) | Parent collection, making this a sub-collection. A child always inherits the parent's `_owner`. |
| `collection.displayname` | `LocaValue` | The collection's primary label. |
| `collection.description` | `LocaValue` | Longer description. |
| `collection.reference` | `string` (nullable) | Unique reference for lookups and search. |
| `collection.shortname` | `string` (nullable) | Unique short name for search. |
| `collection.uuid` | `string` | Unique id, used for WebDAV access. |
| `collection.type` | `string` | Usually `workfolder` or `search`. Has no functional effect beyond backup id replacement. |
| `collection.pin_code` | `string` (nullable) | A pin protecting a shared collection. |
| `collection.create_object` | `object` (nullable) | Basics used when the collection creates objects (via WebDAV or `?collection=<id>`). |
| `collection.webfrontend_props` | `object` (map) | Custom frontend data; stored as-is. |
| `collection.children_allowed` | `bool` | easydb 5 compatibility flag; no effect in fylr. |
| `collection.objects_allowed` | `bool` | easydb 5 compatibility flag; no effect in fylr. |
| `collection.is_system_collection` | `bool` (read-only) | A system collection that cannot be deleted. |
| `collection.lookup:_id` / `lookup:_id_parent` | `object {reference}` | Resolve the collection or its parent by `reference`. |
| `_basetype` | `string` (`collection`) | Fixed marker identifying this object as a collection. |
| `_owner` | `object` (`WhoApi`) | The collection's owner (users only, never a group). |
| `_count` | `int64` (read-only) | Number of objects in this collection. |
| `_count_recursive` | `int64` (read-only) | Number of objects including all descendant collections. |
| `_level` | `int` (read-only) | Depth in the collection tree (a user's top level is `3`). |
| `_path` | `array<object>` (read-only) | Minimal records of the parent collections, for building the tree. |
| `_has_children` | `bool` (read-only) | Has sub-collections (independent of the caller's permissions). |
| `_has_remote_objects` | `bool` (read-only) | Contains at least one object from a foreign collection. |
| `_acl` | `array` (read-only unless sharing) | ACL grants on this collection. |
| `_private_acl` | `bool` | Private ACL — ignore the parent's ACL except a `sticky` grant. |
| `_has_acl` | `bool` (read-only) | Has an active ACL (including an inherited one). |
| `_invalid_acl` | `bool` (read-only) | Sharing is disabled because the owner lacks the rights needed to grant it. |
| `_create_object_compiled` | `object` (read-only) | The effective `create_object`, from this collection or the nearest parent that sets one. |
| `_has_pin` | `bool` (read-only) | The collection has a pin code set. |
| `_pin_ok` | `bool` (read-only) | The current user has entered the correct pin. |
| `_hotfolder_upload_urls` | `array<object {type, url}>` (read-only) | WebDAV upload URLs for the collection. |
| `_objects` | `array` (read-only) | The linked objects, as returned in a response. |
| `_created_at` / `_updated_at` | `date-time` (read-only) | Create / last-update timestamps. |

## In the API

The collection record is read and written through [`/api/v1/collection`](../api/endpoints/collection/README.md). The object list is not edited by re-saving the whole record: it is fetched with [`/list`](../api/endpoints/collection/list.md) / [`/objects`](../api/endpoints/collection/objects.md) and modified with [`/push`](../api/endpoints/collection/push.md), [`/remove`](../api/endpoints/collection/remove.md) and [`/splice`](../api/endpoints/collection/splice.md). On a full `PUT` the object list is supplied under the key `objects`, while responses return it under `_objects`.

See [Collections and publishing](../concepts/collections-and-publishing.md) for the concept.

`LocaValue` is a localized object keyed by language, e.g. `{ "de-DE": "…", "en-US": "…" }`.
