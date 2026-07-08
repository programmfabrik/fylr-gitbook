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
