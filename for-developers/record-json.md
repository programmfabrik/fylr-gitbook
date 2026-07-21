---
description: >-
  The anatomy of a record in the /api/v1/db JSON — the system fields every
  record carries, the difference between _id / _system_object_id /
  _global_object_id, and how field values (linked, nested, local
---

# Anatomy of a Record

A record returned by [`/api/v1/db`](api/endpoints/api-db.md) is a JSON object with two layers:

* **system fields** — underscore-prefixed keys at the **top level** (`_objecttype`, `_system_object_id`, `_owner`, `_standard`, …);
* the record's **content** — its own fields — under a single key **named after the object type**. The record's `_id` and `_version` live inside that block.

```json
{
  "_objecttype": "person",
  "_mask": "_all_fields",
  "_system_object_id": 4711,
  "_global_object_id": "4711@fylr",
  "_uuid": "b2c3…",
  "_standard": { "1": { "text": { "en-US": "Ada Lovelace" } } },
  "_owner": { "user": { "_id": 3, "displayname": "…" } },
  "person": {
    "_id": 128,
    "_version": 4,
    "_pool": { "_basetype": "pool", "pool": { "_id": 9, "name": { "en-US": "Photos" } } },
    "name": "Lovelace",
    "first_name": "Ada"
  }
}
```

{% hint style="info" %}
Which system fields are present depends on the **context**: some appear only for hierarchical object types (`_path`, `_has_children`), only in search results (`_score`, `_sort`), or only in plugin callbacks (`_current`). The record's own fields depend on the **mask** it was rendered with.
{% endhint %}

## The three ids

fylr gives an object several ids that are easy to confuse:

| Id                  | Unique within         | Notes                                                                                                          |
| ------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| `_id`               | one **object type**   | Lives inside the objecttype block. Settable while the object is new (version 1), immutable afterwards.         |
| `_system_object_id` | one **fylr instance** | Top level. The stable id to reference an object across object types. Settable while new, immutable afterwards. |
| `_global_object_id` | **across instances**  | Top level. The `_system_object_id` plus `@<database>` (e.g. `4711@fylr`).                                      |

Use `_system_object_id` when you link or address objects; `_id` only disambiguates within a single object type.

## System fields

### Top level

| Field                             | Type            | Meaning                                                                                    |
| --------------------------------- | --------------- | ------------------------------------------------------------------------------------------ |
| `_objecttype`                     | string          | Object type name. Always present.                                                          |
| `_objecttype_display_name`        | l10n            | Localized object type name.                                                                |
| `_mask`                           | string          | Mask the record was rendered with.                                                         |
| `_mask_display_name`              | l10n            | Localized mask name.                                                                       |
| `_format`                         | string          | Render format: `standard`, `long`, `short`.                                                |
| `_system_object_id`               | int64           | Instance-wide object id.                                                                   |
| `_global_object_id`               | string          | `<_system_object_id>@<database>`.                                                          |
| `_uuid`                           | string          | System-wide unique id (with `_system_object_id`, gated by the request's system-id output). |
| `_standard`                       | object          | The display / search projection of the record (see below).                                 |
| `_owner`                          | `WhoApi`        | The object's owner (a user or a group).                                                    |
| `_create_user`                    | `WhoApi`        | The user who created the object.                                                           |
| `_created`                        | date-time       | Creation time of the first version.                                                        |
| `_last_modified`                  | date-time       | Last-modification time.                                                                    |
| `_latest_version`                 | bool            | Whether this is the object's latest version.                                               |
| `_latest_version_deleted_at`      | date-time       | Set when the latest version is soft-deleted (trashed).                                     |
| `_tags`                           | array           | Tags on the object.                                                                        |
| `_system_tags`                    | array           | System tags (only on the latest version).                                                  |
| `_acl`                            | array           | ACL grants (when the object type has ACL and rights are requested).                        |
| `_generated_rights`               | object          | The requesting user's effective rights on the object.                                      |
| `_collections`                    | array           | Collections the object is in.                                                              |
| `_comment`                        | string          | The changelog comment of this version.                                                     |
| `_changelog`                      | array           | Version history; each entry carries `current_version`.                                     |
| `_published` / `_published_count` | array / int     | Publish records for the object.                                                            |
| `_score`                          | number          | **Search only** — relevance score.                                                         |
| `_sort`                           | array           | **Search only** — the sort values, for deep pagination (`search_after`).                   |
| `_has_children`                   | bool            | **Hierarchical only** — the object has children.                                           |
| `_level` / `_path`                | int / array     | **Hierarchical only** — depth and ancestor chain.                                          |
| `_paths`                          | array of arrays | **Polyhierarchical only** — every parent path.                                             |
| `_current` / `_callback_context`  | object          | **Plugin callback only** — the currently stored object and callback context.               |

### Inside the objecttype block

| Field                             | Type   | Meaning                                                                                   |
| --------------------------------- | ------ | ----------------------------------------------------------------------------------------- |
| `_id`                             | int64  | Object id, unique within the object type.                                                 |
| `_version`                        | int64  | Object version, starting at 1, incremented per update.                                    |
| `_pool`                           | object | The object's pool, rendered as a compact pool record. The numeric id is `_pool.pool._id`. |
| `_id_parent`                      | int64  | **Hierarchical** — parent object id.                                                      |
| `_parents`                        | array  | **Polyhierarchical** — parent objects.                                                    |
| `lookup:_id`, `lookup:_id_parent` | object | **Write only** — resolve the object / its parent from a reference on save.                |

{% hint style="warning" %}
Some names that look like they should exist do not: there is no `_updated` (use **`_last_modified`**), no `_version_created_at` (use **`_created`**), and no plural `_comments` (it is **`_comment`**). `_current_version` is not an output field — it is a search filter; the per-version "is current" flag appears as `current_version` inside `_changelog` entries.
{% endhint %}

## How field values serialize

* **Linked field** (link or reverse link) — a linked value renders the **whole target object** with the same anatomy as a top-level record: `_objecttype`, `_mask`, `_system_object_id`, `_global_object_id`, `_standard`, and the `<objecttype>: { _id, _version, … }` block. A reverse-edit link also carries `_child_idx`. A soft-deleted or deferred target renders a thin wrapper (`_uuid` / `_system_object_id` / `_objecttype` plus a `_latest_version_deleted_at` or `_purged_or_deferred` marker).\
  **To write a link**, send the target with its `_system_object_id` (or `_uuid`), or a `lookup:_id` object inside the objecttype block — the lookup accepts `_system_object_id`, `_uuid`, or a custom column such as a `reference` field, optionally with `_allow_defer`.
* **Nested table** — an array of row objects. Each row carries its own fields and a `_uuid` (rows are matched by `_uuid` on update, not by an id).
* **Localized text** (`text_l10n`, `text_l10n_oneline`) — a plain map keyed by language, e.g. `{ "de-DE": "…", "en-US": "…" }`; empty renders as `{}`.
* **`_standard`** — a compact, mask-independent, localized projection of the record used for display, sorting and indexing (and embedded inside linked values). It holds up to three text/HTML slots (`"1"`, `"2"`, `"3"`, each `{ "text": {lang:…}, "html": {lang:…} }`), an `"eas"` map of display files, and a `"geo"` block.

## See also

* [Records and objecttypes](concepts/records-and-objecttypes.md) — the concept behind records.
* [Files and assets](concepts/files-and-assets.md) — how file fields serialize.
* [System Data Types](system-data-types/) — the field references for `user`, `group`, `pool`, `collection`, `message`, `publish`, `event`.
* [`/api/v1/db`](api/endpoints/api-db.md) — the endpoint that reads and writes records.
