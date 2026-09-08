# Base fields only group edits

From **fylr 6.35.0**, `POST /api/v1/db/{objecttype}?base_fields_only=1`
can change tags or pools for several records without supplying a mask. This
allows a group edit when the records are editable through different masks.
The records' ordinary field values remain unchanged.

Use the group-edit body: an array of entries, each with an `_id` array inside
the object-type block. Supply at least one change to `_tags` or `_pool`.
For example, move two records of object type `photos` into pool 7:

```json
[
  {
    "_objecttype": "photos",
    "photos": {
      "_id": [23, 24],
      "_pool": { "pool": { "_id": 7 } }
    }
  }
]
```

Tags use the ordinary top-level `_tags` and optional `_tags:group_mode`
properties. Do not send `_mask`, ordinary fields, parent changes, `_acl`,
or `_owner`. A single-record `_id` value and the `collection` query parameter
are also rejected in this mode. Use an `_id` array even for one record.

The caller needs write permission on each record. A tag change also needs
at least one usable mask of the object type that allows tag editing and is
not a display-only objecttype maskfilter. Pool moves require the usual pool
link and unlink permissions. To propagate a pool change to reverse records,
specify `reverse_pool_changed_mode`; no supplied mask determines that policy.

The save creates a new record version, retains its ordinary field values and
returns the normal array of saved objects. Unchanged values are shared between
versions, which reduces database writes for repeated tag and pool edits.

Workflow callbacks still run. They receive `base_fields_only: true` in their
info and a payload limited to this mode's fields and system information. A
callback response attempting to change a record field or parent is rejected.
The callback and update event use the current cached standard; a record not
yet cached by indexing has the `#<id>` placeholder.

See [/api/v1/db](endpoints/api-db.md) for the complete parameter reference.
