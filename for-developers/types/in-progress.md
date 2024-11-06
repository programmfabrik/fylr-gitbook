---
hidden: true
---

# in progress

### System datatypes

| Field               | Import | Export | Description                                            |
| ------------------- | ------ | ------ | ------------------------------------------------------ |
| `_standard.1`       | -      | ✓      | The attribute `text` of the standard info is exported. |
| `_system_object_id` | -      | ✓      |                                                        |

### User datatypes

#### Custom datatype

For custom datatype we support the import mapping for known fields. These known fields are fields for which a mapping is defined in the plugin's manifest.yml.

```yml
custom_types:
    example:
        mapping:
            mytext:
                type: text
            mynumber:
                type: number
```

In this example the subfield `mytext` and `mynumber` are imported for metadata imports.

The full custom data is also supported if the full JSON is provided during the import.

For export mapping FYLR supports all import fields as well as the subfield `_standard` to output the standard info of the custom data.

> A list of all available subfield names for a specific instance can be found in `/inspect/datamodel`.

## Metadata mapping

## Export

### System columns

* T: Top Level
* L: Linked Object
* P: Path / Paths / Parents
* F: FYLR only, not in easydb

| Field                            | T | L | P | F | XML Name            | XML                                                                                                                                                                                                                                                                               |
| -------------------------------- | - | - | - | - | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_created`                       | + |   |   |   |                     | `<_created>2022-06-16T07:43:19<_created>`                                                                                                                                                                                                                                         |
| `_global_object_id`              | + | + | + |   |                     | `<_global_object_id>7@4e2feccf-6ba7-4302-a2d9-b38569d275c0</_global_object_id>`                                                                                                                                                                                                   |
| `_has_children`                  | + |   |   |   |                     | `<_has_children>true</_has_children>`                                                                                                                                                                                                                                             |
| `_last_modified`                 | + |   |   |   |                     | `<_last_modified>2022-06-16T07:43:19</_last_modified>`                                                                                                                                                                                                                            |
| `_mask`                          | + | + | + |   |                     | `<_mask>object__all_fields</_mask>`                                                                                                                                                                                                                                               |
| `_objecttype`                    | + | + | + |   |                     | `<_objecttype>object</objecttype>`                                                                                                                                                                                                                                                |
| `_path`                          |   | + |   |   |                     | `<_path><!-- contains objects --></_path>`                                                                                                                                                                                                                                        |
| `_paths`                         |   | + |   |   |                     | `<_paths><_path><!-- contains objects --></_path></_paths>`                                                                                                                                                                                                                       |
| `_format`                        | + | + | + | + |                     |                                                                                                                                                                                                                                                                                   |
| `_standard.1.text`               | + | + | + |   | `_standard`         | `<_standard><de-DE>ref1 (v2)</de-DE><en-US>ref1 (v2)</en-US></_standard>`                                                                                                                                                                                                         |
| `_standard.2.text`               | + | + | + |   | `_standard-2`       |                                                                                                                                                                                                                                                                                   |
| `_standard.3.text`               | + | + | + |   | `_standard-3`       |                                                                                                                                                                                                                                                                                   |
| `_system_object_id_parent`       | + | + | + | + |                     | `<_system_object_id_parent>7</_system_object_id_parent>`                                                                                                                                                                                                                          |
| `_system_object_id`              | + | + | + |   |                     | `<_system_object_id>7</_system_object_id>`                                                                                                                                                                                                                                        |
| `_tags`                          | + |   |   |   |                     | `<_tags><tag id="1"><displayname><de-DE>on</de-DE><en-US></en-US></displayname><reference>red</reference><shortname></shortname></tag><tag id="2"><displayname><de-DE>off</de-DE><en-US></en-US></displayname><reference>green</reference> <shortname></shortname></tag></_tags>` |
| `_uuid`                          | + | + | + |   |                     | `<_uuid>uuidpersonal</_uuid>`                                                                                                                                                                                                                                                     |
| `<objecttype>._id_parent`        | + | + | + |   | `_id_parent`        | `<_id_parent>1</_id_parent>`                                                                                                                                                                                                                                                      |
| `<objecttype>._parent_child_idx` | + | + | + | + | `_parent_child_idx` | `<_parent_child_idx>0</_parent_child_idx>`                                                                                                                                                                                                                                        |
| `<objecttype>._id`               | + | + | + |   | `_id`               | `<_id>2</_id>`                                                                                                                                                                                                                                                                    |
| `<objecttype>._parents`          | + | + |   | + | `_parents`          | `<_parents><!-- contains objects></_parents>`                                                                                                                                                                                                                                     |
| `<objecttype>._pool`             | + | + | + |   | `_pool`             | `_pool id="2"><name><de-DE>Standard-Pool</de-DE><en-US>Standard pool</en-US></name><reference>system:standard</reference></_pool>`                                                                                                                                                |
| `<objecttype>._version`          | + | + | + |   | `_version`          | `<_version>1</_version>`                                                                                                                                                                                                                                                          |

### User column

| Type                  | Field           | CSV  | XML                                                                                                                                                                                                                   |
| --------------------- | --------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| string                |                 |      | `<string type="string" column-api-id="20">string</string>`                                                                                                                                                            |
| text\_oneline         |                 |      | `<text type="text_oneline" column-api-id="6">huhu</text>`                                                                                                                                                             |
| text\_l10n            |                 |      | `<locatext_multi type="text_l10n" column-api-id="21"><en-US>locatext_multi en-US</en-US><de-DE>locatext_multi de-DE</de-DE></locatext_multi>`                                                                         |
| text                  |                 |      | `<text_multi type="text" column-api-id="22">text_multi</text_multi>`                                                                                                                                                  |
| date                  |                 |      | `<date type="date" column-api-id="13">1972-06-27</date>`                                                                                                                                                              |
| datetime              |                 |      | `<datetime type="datetime" column-api-id="14">1972-06-27T05:10:00</datetime>`                                                                                                                                         |
| daterange             |                 |      | `<daterange type="daterange" column-api-id="15"><from>1972-01-01</from><to>1972-06-30</to><text></text></daterange>`                                                                                                  |
| number                |                 |      | `<number type="number" column-api-id="16">12345</number>`                                                                                                                                                             |
| integer.2             |                 |      | `<currency type="integer.2" column-api-id="12">123.45</currency>`                                                                                                                                                     |
| bool                  |                 |      | `<bool type="boolean" column-api-id="11">true</bool>`                                                                                                                                                                 |
| file                  |                 |      | `<file type="files" column-api-id="29"><files><file><!-- file info --></file></files>`                                                                                                                                |
| link                  |                 |      | `<photographer type="link" column-api-id="17"><photographer><!-- contains object --></photographer></photographer>`                                                                                                   |
| reverse\_hierarchical |                 |      | `<_reverse_nested__object__id_parent type="reverse_hierarchical" column-api-id="26"><!-- reverse objects --><object type="reverse_hierarchical" column-api-id="26">...</object></_reverse_nested__object__id_parent>` |
| reverse               |                 |      | `<_reverse_nested__asset__lk_object_id type="reverse" column-api-id="27"><!-- reverse objects --><asset type="reverse" column-api-id="27">...</asset><<_reverse_nested__asset__lk_object_id>`                         |
| custom                |                 | JSON | `<object><!-- easydb XML representation of custom data (json TO xml processing) --></object>`                                                                                                                         |
| custom                | `_standard`     |      | All export languages standard XML, merges text + l10ntext into one language map                                                                                                                                       |
| custom                | `<searchfield>` |      | Plain XML for mapped search fields, FYLR only                                                                                                                                                                         |

