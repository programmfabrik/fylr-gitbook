# group

The system data type `group` is a **group of users** — the unit permissions and system rights are granted to. A user's rights come from the groups they belong to. Groups are managed through the [`/api/v1/group`](../api/endpoints/api-group.md) endpoint.

The mutable group data sits under the `group` key; rights, ACL and other read-only or system fields sit at the top level.

## Fields

| Field | Format | Description |
| --- | --- | --- |
| `_basetype` | `string` (`group`) | Fixed marker identifying this object as a group. |
| `group` | `object` | The mutable group data. |
| `group._id` | `int64` | Server-issued numeric id. Required for updates. |
| `group._version` | `int64` | Object version; incremented on each update. |
| `group.reference` | `string` | Optional unique reference (a stable string id used instead of `_id`). |
| `group.name` | `string` | Internal name of the group (unique). |
| `group.displayname` | `LocaValue` | Localized display name. |
| `group.comment` | `string` | Free-text comment, admin-facing. |
| `group.category_a` / `_b` / `_c` | `string` | Optional category labels A / B / C. |
| `group.type` | `string` (`easydb` \| `system`) | Group type. Defaults to `easydb`; `system` groups are internal and cannot be created or changed through the API. |
| `group.frontend_prefs` | `object` (map) | Arbitrary frontend-only preferences. |
| `group.lookup:_id` | `object` (`LookupByReference`) | Resolve `_id` from a `reference` server-side. |
| `_system_rights` | `object` (`SystemRightsApi`) | The system rights granted to the group's members. |
| `_acl` | `array<RightApi>` | ACL grants held on this group object. |
| `_generated_rights` | `object` (`GeneratedRightsApi`) | Read-only: the current session user's rights on this group. |
| `_two_fa_required` | `bool` | Members must pass a second factor at login (when two-factor authentication is enabled). |
| `_ip_subnet_filter` | `array<string>` | CIDR entries restricting the networks members may log in from. |
| `_ip_subnet_filter_exclude` | `bool` | Invert the meaning of `_ip_subnet_filter` (treat the list as blocked instead of allowed). |
| `_auth_method_group_maps` | `object` (`AuthMethodGroupMapsApi`) | Mappings from external authentication (LDAP / SAML / OAuth) onto this group. |
| `_pseudonymization` | `object` (`GroupPseudoApi`) | Pseudonymization configuration for the group's members. |
| `_automatic_auth` | `object` (`AutomaticAuthApi`) | Automatic-authentication descriptor (one-time token, expiry). |
| `_owner` | `object` (`WhoApi`) | The group's owner. |
| `_created_at` / `_updated_at` | `date-time` | Create / last-update timestamps. |

## In the API

Groups are read and written through [`/api/v1/group`](../api/endpoints/api-group.md). System rights and ACL semantics are described under [Permissions](../concepts/permissions.md).

`LocaValue` is a localized object keyed by language, e.g. `{ "de-DE": "…", "en-US": "…" }`.
