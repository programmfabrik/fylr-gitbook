# pool

The system data type `pool` is the **primary container a live object lives in**. Pools form a tree; permissions, tags, transitions and some settings are granted on a pool and inherited down its sub-pools. Pools are managed through the [`/api/v1/pool`](../api/endpoints/api-pool.md) endpoint. See [Pools](../concepts/pools.md) for the concept.

The mutable pool data sits under the `pool` key; the tree, ACL and other read-only or system fields sit at the top level.

## Fields

| Field | Format | Description |
| --- | --- | --- |
| `_basetype` | `string` (`pool`) | Fixed marker identifying this object as a pool. |
| `pool` | `object` | The mutable pool data. |
| `pool._id` | `int64` | Server-issued id. Required for updates. |
| `pool._version` | `int64` | Object version. |
| `pool._id_parent` | `int64` | Parent pool id; null or absent for a root pool. Re-parenting requires `bag_create` on the target parent. |
| `pool.lookup:_id_parent` | `object` (`LookupByReference`) | Resolve the parent pool from a `reference`. |
| `pool.reference` | `string` | Optional unique reference. |
| `pool.name` | `LocaValue` | Localized pool name. |
| `pool.shortname` | `LocaValue` | Localized short name. |
| `pool.description` | `LocaValue` | Localized long description. |
| `pool.comment` | `string` | Free-text comment. |
| `pool.contact` | `object` (`WhoApi`) | Pool contact principal (a user or a group). |
| `pool.is_system_pool` | `bool` | Read-only marker for built-in system pools; cannot be set through the API. |
| `pool.watermark` | `object` (`WatermarkApi`) | Watermark configuration for produced image variants. |
| `pool.caption` | `object` (`CaptionByFieldApi`) | Per-field caption configuration. |
| `pool.janitor_policy` | `object` (`JanitorPolicyApi`) | Retention / clean-up policy for this pool. |
| `pool.custom_data` | `object` (map) | Custom-data values. |
| `pool.mapping_dc_export` | `string` \| `int64` | Dublin-Core export metadata mapping (reference or id). |
| `pool.mapping_image_export` | `string` \| `int64` | Image-export metadata mapping. |
| `pool.mapping_image_import` | `string` \| `int64` | Image-import metadata mapping. |
| `_owner` | `object` (`WhoApi`) | The pool's owner. |
| `_level` | `int` | Depth in the pool tree: `0` for a root pool, `+1` per descent. |
| `_path` | `array<PoolApi>` | Ancestor pools from root to parent (in `standard` format), for breadcrumbs. |
| `_has_children` | `bool` | At least one sub-pool exists. |
| `_acl` | `array<RightApi>` | ACL grants held on this pool. |
| `_private_acl` | `bool` | The pool's ACL is private (does not inherit from the parent). |
| `_generated_rights` | `object` (`GeneratedRightsApi`) | Read-only: the requesting user's rights on this pool. |
| `_tags` | `array<Tag>` | Tag definitions declared on this pool. |
| `_private_tags` | `bool` | Tags are private (not inherited by sub-pools). |
| `_compiled_tags` | `array<Tag>` | The effective merged tag set (own plus inherited). |
| `_transitions` | `array<TransitionApi>` | Workflow transitions declared on this pool. |
| `_private_transitions` | `bool` | Transitions are private (not inherited by sub-pools). |
| `_standard_masks` | `object` (map) | Per-objecttype default mask preference: objecttype id → ordered list of mask ids. |
| `_created_at` / `_updated_at` | `date-time` | Create / last-update timestamps. |

## In the API

Pools are read and written through [`/api/v1/pool`](../api/endpoints/api-pool.md). What inherits down the pool tree, and how ACL and tags combine, is described under [Pools](../concepts/pools.md) and [Permissions](../concepts/permissions.md).

`LocaValue` is a localized object keyed by language, e.g. `{ "de-DE": "…", "en-US": "…" }`.
