---
description: The parameter format of a fylr plugin's base_config, of a collection upload's config and of a custom data type's options — sections, parameter types and options, where the values arrive, secrets and localization keys.
---

# Base config parameters

A plugin's [`base_config`](../manifest.md#base_config) is a list of sections, each with its parameters. The same format describes the per-collection [`config` of a collection upload](../manifest.md#collection_upload) and the options of a [custom data type](../manifest.md#custom_types) in the datamodel and mask editors (`config.schema`, `config.mask`).

```yaml
base_config:
  - name: my_plugin_service
    require_system_right: system.config
    parameters:
      enabled:     { type: bool, default: true, position: 0 }
      endpoint:    { type: text, regex: "^https?://", placeholder: true, position: 1 }
      api_key:     { type: secret, position: 2 }
      mode:        { type: select, options: [ fast, thorough ], default: fast, position: 3 }
      timeout_sec: { type: int, min: 1, max: 600, default: 30, position: 4 }
      languages:   { type: string-list, choices: [ de-DE, en-US, fr-FR ], default: [ en-US ], position: 5 }
      notice:      { type: text-l10n, position: 6 }
      mappings:
        type: table
        position: 7
        fields:
          - { name: source, type: text }
          - { name: target, type: text }
          - { name: active, type: bool, default: true }
      advanced:
        type: form
        plugin_type: panel
        position: 8
        parameters:
          retries: { type: int, default: 3, position: 0 }
          note:    { type: text-multiline, position: 1 }
  - name: my_plugin_user
    parameters:
      api_user: { type: user }      # plugin_user.base_config: my_plugin_user.api_user
```

## Sections

| Key | Meaning |
| --- | --- |
| `name` | **Required.** The section's name, the key of its values. Its [localization keys](#localization) do not contain the plugin name, so they share one namespace with fylr's own sections and other plugins' — start the name with the plugin's name. |
| `parameters` | **Required.** A map from parameter name to [parameter](#parameters). A section without a parameter of a supported type is left out. |
| `require_system_right` | A system right a user needs to read the section's values, such as `system.config` or one of the plugin's own [system rights](../manifest.md#system_rights); `system.config` and `system.root` always suffice. Without it, every logged-in user can read the values, with `secret` values masked. |
| `unauthenticated_visible` | `true` also delivers the section to sessions without a user. |

Saving any section needs the system right `system.config`.

## Parameters

Every parameter has a `type`. These keys apply to all types:

| Key | Meaning |
| --- | --- |
| `type` | **Required.** One of the [types](#types). A parameter of another type is left out, with a warning in the server log. |
| `position` | The order in the editor, ascending. In a `table`, the fields keep the order of the list instead. |
| `default` | The value while none is saved, in the type's value format. Defaults inside a `form` apply once the form holds a value. |
| `placeholder` | `true` shows the loca key `….placeholder` in the empty field. With a `default`, the default is shown instead. |
| `show_script` | A JavaScript expression; the editor hides the parameter while it is false. `config` holds the plugin's current values as `config.<section>.<parameter>`. |
| `plugin_type` | A special editor for the parameter — see [Editors](#editors). |
| `readonly` | `true` for a `text`: the editor no longer lets the field change once a value is saved. |
| `unauthenticated_visible` | `false` hides the parameter from sessions without a user, in a section with `unauthenticated_visible: true`. |

Further keys apply to some types:

| Key | Types | Meaning |
| --- | --- | --- |
| `regex` | `text` | A regular expression the value must match. A value that does not is rejected on save with `BaseConfigRegexpNotMatching`. |
| `min`, `max` | `int` | The smallest and the largest value, checked on save. |
| `options` | `select` | The values offered. |
| `options_loca_key_prefix` | `select` | Labels the options with the loca keys `<prefix>.<option>`. |
| `options_loca_off` | `select` | `true` shows the values themselves; the value `---` becomes a divider. |
| `choices` | `string-list`, `string-list-sort`, `string-list-one` | The values offered. |
| `label_choice` | `string-list`, `string-list-sort`, `string-list-one` | Labels the choices with the loca keys `server.config.choice.system.<section>.<label_choice>.<choice>`. Without it, the values themselves are shown. |
| `minimum` | `string-list`, `string-list-sort`, `string-list-one` | How many choices the editor requires: by default 1 for `string-list-one`, 0 otherwise. |
| `fields` | `table` | The table's columns: a list of parameters, each with a `name`. |
| `parameters` | `form` | A map from parameter name to parameter. |
| `classes`, `extensions` | `file` | The file classes and file extensions allowed, checked on save. |

## Types

| `type` | Value | Editor |
| --- | --- | --- |
| `bool` | `true` or `false` | a checkbox |
| `int` | a number | a number field |
| `text` | a string | a text field |
| `text-multiline` | a string | a text area |
| `text-l10n` | a map from language to text | a text field per language |
| `text-l10n-multiline` | a map from language to text | a text area per language |
| `email` | an email address | an email field |
| `secret` | a string, see [Secrets](#secrets) | a masked field |
| `select` | one of `options`; a saved value that is not, becomes the first option | a drop-down |
| `string-list` | a list of values from `choices` | checkboxes |
| `string-list-sort` | a list of values from `choices`, in order | sortable checkboxes |
| `string-list-one` | a list of values from `choices` | radio-style checkboxes, at least one |
| `json` | a JSON object | a JSON editor |
| `table` | a list of rows, each a map from field name to value | a table |
| `form` | a map from parameter name to value | a group of fields |
| `user` | `{"_basetype": "user", "user": {"_id": <id>}}` of an existing user | a user picker |
| `file` | a file, `{"_id": <id>}` | a file upload |
| `location-select` | the name of an existing file location | a location picker |
| `tag-select` | a list of tag IDs | a tag picker |
| `tagfilter-select` | a tag filter | a tag filter editor |

A parameter of type `user` is what a callback's [`plugin_user`](../callbacks/contract.md#the-plugin-user) names as `<section>.<parameter>`.

A value that does not fit its parameter is rejected on save with `BaseConfigParse` (HTTP 400), which names it as `plugin.<plugin>.<section>.<parameter>`. A posted parameter or section the plugin does not define is ignored.

### Editors

`plugin_type` replaces the editor of a parameter:

| `type` | `plugin_type` | Editor |
| --- | --- | --- |
| `text-multiline` | `html`, `javascript`, `json`, `css` | a code editor for that language |
| `form` | `panel` | a collapsible panel |
| `text` | `date` | a date picker |
| `text` | `tag-select` | a tag picker |
| `int` | `profile_mapping_select` | a metadata mapping profile picker |
| `int` | `group_easydb_select` | a group picker |
| `int` | `right_preset_collection` | a picker for a collection right preset |
| `text`, `int` | any other value | an editor the plugin's frontend code registers with `BaseConfig.registerPlugin`, a `BaseConfigPlugin` |

## Where the values arrive

Administrators edit a plugin's sections in the base configuration under **Plugins**, and on the plugin's **config** tab in the Plugin Manager. The sections of a plugin are offered while it is enabled.

| Where | Path |
| --- | --- |
| a plugin program, in `%info.json%` | `config.plugin.<plugin>.config.<section>.<parameter>` — the plugin's own values only, defaults applied, secrets decrypted |
| `GET /api/v1/config` | `plugin.<plugin>.config.<section>.<parameter>` |
| `POST /api/v1/config` | `{"plugin": {"<plugin>": {"config": {"<section>": {…}}}}}` |
| the session | `config.base.plugin.<plugin>.config.<section>.<parameter>` |
| `GET /api/v1/config/list` | `plugin.<plugin>.defs` — the definitions, for users with `system.config` |

Next to each value is `<parameter>:info`, `{"is_default": true}` while the value is the default.

A `POST` replaces each section it carries as a whole: a parameter left out of a posted section falls back to its default.

`config.system` in `%info.json%` holds only the sections of fylr's own base configuration that are visible without a user.

## Secrets

A parameter of type `secret` holds a password or key:

* `GET /api/v1/config` shows it masked: `*****` when it is stored encrypted (with `fylr.encryptionKey` set), `***` when stored plain, an empty string when there is none.
* Posting an empty string keeps the stored value, posting `-` deletes it, and any other value replaces it. A posted section that leaves out the secret deletes it, like any parameter it leaves out.
* **From version 6.35.1**, every row of a `table` with a `secret` field carries `_row`, the position the row is stored at, in `GET /api/v1/config` and in a plugin program's `%info.json%`. Post the rows back with their `_row`, also after moving or removing rows: an empty secret then keeps the secret of the row that `_row` names. A row without `_row` is new and keeps no secret. A table posted without any `_row` pairs its rows with the stored rows by position, as before 6.35.1.
* A plugin program receives the secret decrypted.
* A collection upload callback receives `collection_config` with secrets masked, so a collection upload's `config` cannot pass a secret to its program.
* `fylr restore` leaves secrets out; they are entered again after a restore.

## Localization

The editor labels a plugin's sections with keys from the plugin's [`l10n`](../manifest.md#l10n) CSV. The keys contain the section name, but not the plugin name:

| Key | Labels |
| --- | --- |
| `server.config.group.system.plugin_<plugin>.title` | the plugin's heading in the base configuration |
| `server.config.group.system.plugin_<plugin>.introduction` | the introduction below it, in Markdown |
| `server.config.name.system.<section>` | a section |
| `server.config.name.system.<section>\|hint` | a section's description |
| `server.config.parameter.system.<section>.<parameter>.label` | a parameter |
| `server.config.parameter.system.<section>.<parameter>.label\|hint` | a parameter's description |
| `server.config.parameter.system.<section>.<parameter>.checkbox` | the text next to a `bool` checkbox |
| `server.config.parameter.system.<section>.<parameter>.placeholder` | a [`placeholder`](#parameters) |
| `server.config.option.system.<section>.<parameter>.<option>` | an option of a `select` |
| `server.config.choice.system.<section>.<label_choice>.<choice>` | a choice, with [`label_choice`](#parameters) |

Inside a `table` or `form`, the path to the parameter goes between section and parameter: `server.config.parameter.system.<section>.<form>.<parameter>.label`. Option keys do not take that path.

The heading and introduction fall back to the plugin's [`displayname` and `info`](../manifest.md#plugin).

The parameters of a collection upload's `config` are labelled with `collection_upload.parameter.<parameter>.label`.
