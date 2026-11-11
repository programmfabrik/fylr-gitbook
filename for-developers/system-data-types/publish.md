# publish

The system data type `publish` records that an object was **published** to an external target. fylr does not host the publication itself — it stores a reference to where the object was published and a deep link back to the source object. Publish records are managed through the [`/api/v1/publish`](../api/endpoints/api-publish.md) endpoint.

The mutable payload sits under the `publish` key; read-only system fields sit at the top level.

## Fields

| Field | Format | Description |
| --- | --- | --- |
| `_basetype` | `string` (`publish`) | Fixed marker identifying this object as a publish record. |
| `_timestamp_created` | `date-time` | UTC time the publish entry was created. |
| `publish` | `object` | The publish payload. Required on create: `system_object_id`, `collector`, `publish_uri`, `easydb_uri`. |
| `publish._id` | `int64` | Server-issued numeric id of the publish record. |
| `publish.version` | `int64` | Optional. When greater than `0`, pins the publication to that exact object version; `0` follows the current version. |
| `publish.system_object_id` | `int64` | The `_system_object_id` of the object being published. |
| `publish.collector` | `string` | The publish collector name. Must match a collector defined in the base configuration, otherwise the save is rejected with `PublishUnknownCollector`. |
| `publish.publish_uri` | `string` | URL where the published artifact can be reached. Stored verbatim; not validated. |
| `publish.easydb_uri` | `string` | Deep-link URL back to the source object inside fylr. |

## In the API

Publish records are read and written through [`/api/v1/publish`](../api/endpoints/api-publish.md). When a publish record is embedded inside another object it is flattened, with the creation time carried as `timestamp_created`.

From fylr 6.36.0, the object search finds a record by its publishings: `_published.collector`, `_published.publish_uri` and `_published.easydb_uri` hold the `collector`, `publish_uri` and `easydb_uri` of the record's publishings, `_published.timestamp_created` the time each was created and `_published_count` their number, `0` for a record without one. A record is found by any of its publishings. A text search (`match`) on one of the three texts matches the whole value, ignoring case; the mode `wildcard` matches a part of it. `in` with `null` on a `_published.` field finds the records without a publishing. The fields hold the publishings only through a mask that shows them (`system_fields.publish.output.mode` `show`): through another mask the record is searched as one without a publishing. The index follows a change of the publishings some seconds after the request, and the re-index of the update to 6.36.0 fills the fields for existing records.

```json
{
  "search": [
    { "type": "match", "mode": "wildcard", "fields": ["_published.publish_uri"], "string": "10.5072/*" }
  ]
}
```
