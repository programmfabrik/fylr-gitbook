---
description: >-
  How to apply metadata exports when exporting and downloading records from fylr
  by default
---

# Default export metadata mappings

For a pool or an objecttype it's possible to set default export profiles, as seen in the **general** tab of in rights mangement, at the pool or objecttype:

The setting at the pool allows forwarding the setting set at the objecttype.

For both, the options look like:

* Import Profile: used by default when importing
* Export Profile: used by default when exporting and downloading
* Dublin Core Export Profile: used when accessing data using [oai.md](../../../for-administrators/plugins/protocols/oai.md "mention")

For selection all metadata mappings created in Administration > Metadata Mappings will be shown at the according selectors.

The **system right "Export metadata"** allows user/groups to include metadata when exporting or downloading records.&#x20;

| Standard Profile Only | `Standard`                                          | Inherits setting from objecttype or pool (if configured).                  |
| --------------------- | --------------------------------------------------- | -------------------------------------------------------------------------- |
| Standard              | All user mappings                                   | Provides all standard user mapping options.                                |
| Original              | All user mappings + "unchanged"                     | Includes standard options plus the ability to retain original values.      |
| Remove                | All user mappings + "unchanged/original" + "delete" | Includes all previous options plus a specific flag to delete the metadata. |



