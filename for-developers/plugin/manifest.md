---
description: Reference for a fylr plugin's manifest.yml — a full example, every top-level key with all its options, the exec map that runs plugin programs, and the error format.
---

# manifest.yml

Every plugin has a `manifest.yml` at its root. It names the plugin and registers everything the plugin adds to fylr: frontend assets, [extensions](extensions.md) (custom API endpoints), [callbacks](callbacks/README.md) (hooks into fylr's own API calls), base-config parameters, file-processing recipes, custom data types, system rights and event types.

fylr reads the manifest when the plugin is installed, updated or loaded. Keys fylr does not know are ignored without an error, so a misspelt key simply has no effect. A value of the wrong type, such as a plain string where a map is expected, makes the whole manifest invalid: the plugin is refused on install and disabled when it is already installed.

## Full example

Every top-level key, with the options a plugin typically sets. The sections below list all options of each key.

```yaml
plugin:
  name: my-plugin
  displayname:
    en-US: "My Plugin"
    de-DE: "Mein Plugin"
  info:
    en-US: "Checks records against an external service."
  url: https://github.com/example/fylr-plugin-my-plugin
  l10n: l10n/my-plugin.csv          # server-side localization, relative to manifest.yml
  dependencies:
    - commons-library
  webfrontend:                      # paths relative to base_url_prefix
    url: my-plugin.js
    css: my-plugin.css
    html: my-plugin.html
    l10n: l10n/                     # <lang>.json files for the frontend
  custom:
    help_url: https://example.com/help

base_url_prefix: webfrontend        # directory served at /api/v1/plugin/static/my-plugin/

base_config:
  - name: my_plugin_service
    parameters:
      enabled:
        type: bool
        default: true
        position: 0
      endpoint:
        type: text
        regex: "^https?://"
        position: 1
      api_key:
        type: secret
        position: 2
  - name: my_plugin_user
    parameters:
      api_user:
        type: user

extensions:
  status:                           # /api/v1/plugin/extension/my-plugin/status
    exec:
      service: node
      commands:
        - prog: node
          stdin:  { type: body }
          stdout: { type: body }
          args:
            - { type: value, value: "%_exec.pluginDir%/server/status.js" }
            - { type: value, value: "%info.json%" }

callbacks:
  db_pre_save:
    steps:
      - name: check objects
        callback: check
        filter:
          type: objecttype
          objecttypes: [ objects ]
    callbacks:
      check:
        plugin_user:
          base_config: my_plugin_user.api_user
        exec:
          service: node
          commands:
            - prog: node
              stdin:  { type: body }
              stdout: { type: body }
              args:
                - { type: value, value: "%_exec.pluginDir%/server/check.js" }
                - { type: value, value: "%info.json%" }
  transition_db_pre_save:
    notify:                         # transition action type "my-plugin:notify"
      exec:
        service: node
        commands:
          - prog: node
            stdin:  { type: body }
            stdout: { type: body }
            args:
              - { type: value, value: "%_exec.pluginDir%/server/notify.js" }
              - { type: value, value: "%info.json%" }
  export:
    checksums:                      # export plugin "my-plugin:checksums"
      exec:
        timeout: "2h"
        service: node
        commands:
          - prog: node
            stdin:  { type: body }
            stdout: { type: body }
            args:
              - { type: value, value: "%_exec.pluginDir%/server/checksums.js" }
              - { type: value, value: "%info.json%" }
  export_transport:
    archive:                        # transport plugin "my-plugin:archive"
      exec:
        service: python3
        commands:
          - prog: python3
            stdin:  { type: body }
            stdout: { type: body }
            args:
              - { type: value, value: "%_exec.pluginDir%/server/archive.py" }
              - { type: value, value: "%info.json%" }

collection_upload:
  set_title:                        # collection upload "my-plugin:set_title"
    config:
      - name: set_title
        parameters:
          field:
            type: text
    callbacks:
      objects:
        exec:
          service: node
          commands:
            - prog: node
              stdin:  { type: body }
              stdout: { type: body }
              args:
                - { type: value, value: "%_exec.pluginDir%/server/set_title.js" }
                - { type: value, value: "%info.json%" }

fas_config:
  produce_config: fas_config/produce.yml
  cookbooks:
    - fas_config/cookbook.yml       # recipes "my-plugin:<cookbook>:<recipe>"

custom_types:
  link:                             # datamodel type custom:base.my-plugin.link
    mapping:
      conceptName:
        type: text
      conceptURI:
        type: text_oneline
        skipTerms: true
    config:
      schema:
        - name: vocabulary
          parameters:
            value:
              type: text
      mask:
        - name: show_uri
          parameters:
            value:
              type: bool
    update:
      plugin_user:
        reference: system:root
      batch_size: 50
      expires_days: 30
      exec:
        service: node
        commands:
          - prog: node
            stdin:  { type: body }
            stdout: { type: body }
            args:
              - { type: value, value: "%_exec.pluginDir%/server/update.js" }
              - { type: value, value: "%info.json%" }

system_rights:
  - name: run_checks                # granted as plugin.my-plugin.run_checks
    parameters:
      - name: level
        type: string-list-one
        choices: [ read, write ]
      - name: pools
        type: pool-select

custom_events:
  MY_PLUGIN_CHECK_FAILED:
    user: true
```

## Top-level keys

| Key | Purpose |
| --- | --- |
| [`plugin`](#plugin) | Name, descriptions, localization, dependencies and frontend assets. |
| [`base_url_prefix`](#base_url_prefix) | The directory whose files fylr serves as the plugin's static files. |
| [`extensions`](#extensions) | Custom API endpoints — see [Extensions](extensions.md). |
| [`callbacks`](#callbacks) | Hooks into saves, transitions and exports — see [Callbacks](callbacks/README.md). |
| [`collection_upload`](#collection_upload) | Hooks into collection uploads — see [Collection upload](callbacks/collection-upload.md). |
| [`base_config`](#base_config) | Parameters the plugin adds to the base configuration — see [Base config parameters](manifest/base-config.md). |
| [`fas_config`](#fas_config) | Cookbooks and produce config the plugin adds to file processing. |
| [`custom_types`](#custom_types) | Custom data types — see [Custom Data](../customdata.md). |
| [`system_rights`](#system_rights) | System rights the plugin adds. |
| [`custom_events`](#custom_events) | Event types the plugin registers. |

A plugin has no `version` key: its version is the tag of its release, delivered as `build_info.release` by `GET /api/v1/plugin`. A `version` left in an older manifest is ignored.

### Names derived from the plugin name

fylr builds the plugin's URLs and identifiers from `plugin.name`:

| Name | Used for |
| --- | --- |
| `/api/v1/plugin/static/<plugin>/…` | the files under [`base_url_prefix`](#base_url_prefix) |
| `/api/v1/plugin/extension/<plugin>/<path>` | [extensions](#extensions) |
| `<plugin>:<name>` | transition actions, exports, export transports and collections that select a [callback](#callbacks) or a [collection upload](#collection_upload) |
| `<plugin>:<cookbook>:<recipe>` | [recipes](#fas_config) |
| `custom:base.<plugin>.<type>` | [custom data types](#custom_types) |
| `plugin.<plugin>.<right>` | [system rights](#system_rights) |
| `plugin.<plugin>.config.<section>.<parameter>` | [base config](#base_config) values |

## `plugin`

| Key | Type | Meaning |
| --- | --- | --- |
| `name` | string, **required** | The plugin's internal name: lower-case letters, digits, `-` and `_`, starting with a letter and ending with a letter or digit, at least two characters (`^[a-z][a-z0-9\-_]*[a-z0-9]$`). It is unique on the instance, and in a ZIP it equals the ZIP's top-level directory. |
| `displayname` | map language → text | The title of the plugin's section in the base configuration, and the label of its tab in metadata mapping profiles. Without it, the plugin name is used. |
| `info` | map language → text | A description in Markdown. The Plugin Manager and the About menu show it, and it introduces the plugin's section in the base configuration. |
| `url` | string | The plugin's homepage or repository, linked from the Plugin Manager and the About menu. It is not the URL the plugin is installed from. |
| `l10n` | string | The plugin's localization CSV, relative to `manifest.yml` — see [`l10n`](#l10n). |
| `dependencies` | list of plugin names | Plugins this plugin requires — see [`dependencies`](#dependencies). |
| `webfrontend` | map | Frontend assets — see [`webfrontend`](#webfrontend). |
| `custom` | map | Free-form values for the plugin's own frontend code. `GET /api/v1/plugin` delivers them unchanged, and in the frontend they are `ez5.pluginManager.getPlugin("<plugin>").getOpts().custom`. That endpoint is public, so nothing secret belongs here. |

`displayname` and `info` are maps from language to text; a plain string makes the manifest invalid:

```yaml
plugin:
  displayname:
    en-US: "My Plugin"
    de-DE: "Mein Plugin"
```

The section title and introduction in the base configuration come from the loca keys `server.config.group.system.plugin_<plugin>.title` and `….introduction`. When the plugin's `l10n` CSV does not define them, fylr fills them from `displayname` and `info`.

### `l10n`

`plugin.l10n` points to one CSV file, relative to `manifest.yml`. The first row is the header: a `key` column, an optional `package` column (which makes the key `<package>.<key>`), and one column per language, headed by its language tag such as `en-US` or `de-DE`. Other columns are ignored. A missing or unreadable file makes the plugin invalid.

fylr merges the keys of all enabled plugins into its own localization, served at `GET /api/v1/l10n/static/<lang>.json`; a plugin key replaces a fylr key of the same name. This is where the labels of the plugin's base config, system rights and event types and the messages of its errors go. See [Localization](conventions.md#localization-l10n) for how plugin CSVs are maintained.

### `dependencies`

`dependencies` lists the names (the `plugin.name`) of other plugins this plugin requires. fylr enforces the declaration:

* **Installing** the plugin is refused with `PluginDependencyNotInstalled` while a dependency is not installed. Installing through the [marketplace](../../for-administrators/plugin-manager/README.md) offers the missing dependencies for installation first.
* **Enabling** the plugin is refused with `PluginDependencyNotEnabled` while a dependency is disabled.
* A plugin that an enabled plugin depends on can not be **disabled** or **deleted** (`PluginRequiredByOthers`).
* The frontend files of all enabled plugins are combined in dependency order, so a dependency's JavaScript is loaded before its dependents'. Plugins without a dependency between them follow in the order of their names (from fylr 6.35.1; before, in reverse order). A plugin whose dependencies are unmet or cyclic is left out of the combined files.

Older plugins declare `dependencies` inside `plugin.webfrontend`. fylr treats that list exactly like `plugin.dependencies`; declare it at the `plugin` level.

### `webfrontend`

| Key | Type | Meaning |
| --- | --- | --- |
| `url` | string | The plugin's JavaScript, relative to [`base_url_prefix`](#base_url_prefix). |
| `css` | string | The plugin's stylesheet, relative to `base_url_prefix`. |
| `html` | string | The plugin's HTML templates, relative to `base_url_prefix`. |
| `l10n` | string | A directory, relative to `base_url_prefix`, with one `<lang>.json` per language: `{"en-US": {"<key>": "<text>"}}`. These are keys for the plugin's own frontend code, separate from the [`plugin.l10n`](#l10n) CSV. |
| `type_extension` | map | Settings the mask editor offers for fields of a column type: `type_extension.mask.<column type>` is a list of entries with `name`, `group` and `parameters` (in the [base config parameter format](manifest/base-config.md#parameters)). |
| `dependencies` | list | Older form of [`plugin.dependencies`](#dependencies). |

fylr combines the files of all enabled plugins into `/api/v1/plugin/bundle.js`, `/api/v1/plugin/bundle.css`, `/api/v1/plugin/bundle.html` and `/api/v1/plugin/bundle/l10n/<lang>.json`, which the web frontend loads. A file that does not exist is skipped with a warning in the server log.

From fylr 6.35.1, each plugin's JavaScript in `bundle.js` runs as a script of its own: a plugin that fails to parse or throws while loading stops only itself, the browser console names it (`Plugin "<name>" failed to load`), and the plugins after it load as before. Top-level declarations of a plugin stay visible to the plugins loaded after it, as with separately loaded files. Before 6.35.1, such a plugin stopped every plugin after it in `bundle.js`.

```yaml
webfrontend:
  type_extension:
    mask:
      eas:                         # offered for file fields
        - name: map
          group: detail
          parameters:
            show_in_map:
              type: bool
              default: true
```

## `base_url_prefix`

The directory inside the plugin, relative to `manifest.yml`, whose files fylr serves at `/api/v1/plugin/static/<plugin>/`. With `base_url_prefix: webfrontend`, the file `webfrontend/my-plugin.js` is served as `/api/v1/plugin/static/my-plugin/my-plugin.js`. The default is `build/webfrontend`; `fylr-build-plugin` requires the key whenever `webfrontend` names a `url`, `css` or `html` file.

The paths in [`plugin.webfrontend`](#webfrontend) are relative to this directory. `GET /api/v1/plugin` delivers the absolute URL of the directory as `base_url`, from which the plugin's frontend code can load further files. Static files are served without authentication while the plugin is enabled, so nothing secret belongs in this directory.

## `extensions`

```yaml
extensions:
  <path>:
    plugin_user:                  # optional
      base_config: <section>.<parameter>
    exec: { … }
```

| Key | Meaning |
| --- | --- |
| `<path>` | The endpoint `/api/v1/plugin/extension/<plugin>/<path>`. It may contain `/`, but must not start or end with one. The request path must match exactly — a sub-path of it is answered with 404 — and every HTTP method reaches the extension. |
| `plugin_user` | Runs the program with an additional token for a user picked in the plugin's base config — see [The plugin user](callbacks/contract.md#the-plugin-user). `base_config` is its only key. |
| `exec` | The program — see [The `exec` map](#the-exec-map). |

See [Extensions](extensions.md) for the request the program receives and how it answers.

## `callbacks`

```yaml
callbacks:
  db_pre_save:
    steps:
      - name: <label>
        callback: <name>
        filter:                    # optional
          type: objecttype
          objecttypes: [ <objecttype>, … ]
    callbacks:
      <name>: { plugin_user, exec }
  transition_db_pre_save:
    <name>: { plugin_user, exec }
  export:
    <name>: { plugin_user, exec }
  export_transport:
    <name>: { exec }
```

| Key | Meaning |
| --- | --- |
| `db_pre_save.steps` | The steps run on every save, in order — see [db\_pre\_save](callbacks/db-pre-save.md). |
| `db_pre_save.steps[].name` | A label for the step, used in the server's debug log. |
| `db_pre_save.steps[].callback` | The key of the callback in `db_pre_save.callbacks`. |
| `db_pre_save.steps[].filter` | Restricts the step to objects of the objecttypes in `objecttypes`; `objecttype` is the only `type`. Without a filter the step runs for every save. |
| `db_pre_save.callbacks.<name>` | A callback a step names. |
| `transition_db_pre_save.<name>` | Runs as a workflow transition action of type `<plugin>:<name>` — see [transition\_db\_pre\_save](callbacks/transition-db-pre-save.md). |
| `export.<name>` | Runs for an export whose `produce_options.plugin` is `<plugin>:<name>` — see [export](callbacks/export.md). |
| `export_transport.<name>` | Runs for an export transport whose `plugin` is `<plugin>:<name>` — see [export\_transport](callbacks/export-transport.md). It does not support `plugin_user`. |

Each callback has the same two keys as an extension: `exec` and the optional `plugin_user`. A name that is selected as `<plugin>:<name>` — a transition, export or export transport callback, and a [collection upload](#collection_upload) — starts with a lower-case letter and contains only lower-case letters, digits and `_`, at least two characters.

## `collection_upload`

```yaml
collection_upload:
  <name>:
    config:                        # optional
      - name: <section>
        parameters: { … }
    callbacks:
      objects:
        plugin_user: { base_config: <section>.<parameter> }   # optional
        exec: { … }
```

| Key | Meaning |
| --- | --- |
| `<name>` | A collection selects the upload as `<plugin>:<name>`. |
| `config` | Parameters an administrator sets per collection, in the [base config parameter format](manifest/base-config.md). The callback receives the values as `collection_config`, and `GET /api/v1/plugin` delivers the definitions under `collection_upload`. |
| `callbacks.objects` | **Required.** The program fylr runs for the uploaded files — see [Collection upload](callbacks/collection-upload.md). It is the only callback of a collection upload. |

## `base_config`

A list of sections the plugin adds to the base configuration. Each section has a `name` and `parameters`:

```yaml
base_config:
  - name: my_plugin_service
    parameters:
      endpoint:
        type: text
      api_key:
        type: secret
```

Administrators edit the values in the base configuration under **Plugins**, and on the plugin's **config** tab in the Plugin Manager. A plugin program receives them in `%info.json%` as `config.plugin.<plugin>.config.<section>.<parameter>`. All section keys, parameter types and options, the localization keys for the labels and the handling of secrets are on [Base config parameters](manifest/base-config.md).

## `fas_config`

```yaml
fas_config:
  produce_config: fas_config/produce.yml
  cookbooks:
    - fas_config/cookbook.yml
```

| Key | Type | Meaning |
| --- | --- | --- |
| `produce_config` | string | One produce config file, relative to `manifest.yml`. While the plugin is enabled, fylr merges it into the instance's produce config: the versions and upload extensions of its classes are added to those of the instance, and so is its custom metadata. The upload size limits and `uploadallowunknown` stay with the instance. |
| `cookbooks` | list of strings | Cookbook files, relative to `manifest.yml`. A cookbook is named `<plugin>:<cookbook>` and its recipes `<plugin>:<cookbook>:<recipe>`; every recipe needs a `class`. A cookbook file that is missing, or two cookbooks with the same `name`, make the plugin invalid. |

A cookbook file has the keys `name`, `description`, `homepage` and `recipes`, a map from recipe name to recipe. The cookbooks are active while the plugin is enabled. [File Version Produce Plugin](setup-produce-plugin.md) walks through a plugin that adds a recipe and the version using it.

## `custom_types`

```yaml
custom_types:
  <type>:
    mapping:
      <subfield>:
        type: <column type>
        skipTerms: true            # optional
    config:                        # optional
      schema: [ … ]
      mask: [ … ]
    update:                        # optional
      plugin_user:
        reference: <user reference>
      batch_size: <1–1000>
      expires_days: <days>
      exec: { … }
```

A custom data type is named `custom:base.<plugin>.<type>` in the datamodel. See [Custom Data](../customdata.md) for the data it stores and the updater.

| Key | Meaning |
| --- | --- |
| `mapping.<subfield>.type` | How fylr indexes and searches this subfield of the custom data: `text`, `text_oneline`, `string`, `text_l10n`, `text_l10n_oneline`, `boolean`, `number`, `integer.2`, `double`, `date`, `datetime`, `daterange` or `geo_json`. |
| `mapping.<subfield>.skipTerms` | `true` keeps the subfield out of the suggest terms; it stays searchable. |
| `config.schema` | Options of the type in the datamodel editor, as a list of sections in the [base config parameter format](manifest/base-config.md). |
| `config.mask` | Options of the type in the mask editor, in the same format. |
| `update.exec` | The updater program — see [Updates](../customdata.md#updates). Without `exec.service` the type has no updater. |
| `update.plugin_user.reference` | The `reference` of a user the updater runs as, such as `system:root`; easydb and system users only. The program receives `plugin_user` and `plugin_user_access_token`. |
| `update.batch_size` | **Required with an updater.** How many records fylr hands the program per call, 1 to 1000; a larger or negative value becomes 100. |
| `update.expires_days` | How many days an updated value stays valid before it is updated again. Default `30`. The program can set `_expires_at` per record instead. |

The updater only runs when the base config setting `custom_data_type_updater.active` is on, and only for enabled plugins.

## `system_rights`

```yaml
system_rights:
  - name: run_checks
    group: my_plugin               # optional
    comment: free text             # optional
    parameters:                    # optional
      - name: level
        type: string-list-one
        choices: [ read, write ]
```

While the plugin is enabled, each entry is a system right named `plugin.<plugin>.<name>` — here `plugin.my-plugin.run_checks` — that administrators grant to users and groups like fylr's own system rights.

| Key | Meaning |
| --- | --- |
| `name` | **Required.** The right's name within the plugin. |
| `group` | The block the right is shown in in the rights editor. Without a group, the plugin's rights share one block named after the plugin. |
| `comment` | A description. The rights editor does not show it. |
| `parameters` | A list of settings granted with the right. |
| `parameters[].name` | **Required.** The setting's name. |
| `parameters[].type` | **Required.** One of the types below. |
| `parameters[].choices` | The values for `string-list`, `string-list-one` and `string-list-one-or-zero`, from the lowest to the highest. |
| `parameters[].merge_policy` | `less` for a `bool`: the user has the setting only if all of their grants have it. |

When a user holds the right more than once — directly and through groups — fylr merges the settings:

| Parameter type | Value | Merged |
| --- | --- | --- |
| `bool` | `true` or `false` | `true` if one grant has it; with `merge_policy: less`, only if all have it |
| `int` | a number | the highest |
| `text` | a string | one of the grants' values |
| `string-list` | a list of values from `choices` | the union |
| `string-list-one` | one of `choices` | the highest in `choices` |
| `string-list-one-or-zero` | one of `choices`, or none | the highest in `choices` |
| `objecttype-select` | objecttype IDs | the union |
| `pool-select` | pool IDs; none means all pools | the union; a grant without pools means all |
| `eas-column-select` | file field IDs; none means all | the union; a grant without fields means all |
| `preview-versions` | `<class>.<version>` names | the union |

A plugin program checks the right through `GET /api/v1/user/session`: `system_rights` holds `plugin.<plugin>.<name>` with its merged settings. For a root user, `system_rights` holds only `system.root`, which stands for every right.

The rights editor labels the right with the plugin's [`l10n`](#l10n) keys:

| Key | Labels |
| --- | --- |
| `server.right.system.plugin.<plugin>.<name>` | the right |
| `server.right.system.plugin.<plugin>.<name>.parm.<parameter>` | a setting |
| `server.right.system.plugin.<plugin>.<name>.parm.<parameter>.option.<choice>` | a choice |
| `acl.right.manager.group.system.<group>` | the block of a `group` |

## `custom_events`

Event types the plugin registers, as a list of names or as a map from name to options:

```yaml
custom_events:
  - MY_PLUGIN_REPORT_SENT
  - MY_PLUGIN_SYNC_DONE
```

```yaml
custom_events:
  MY_PLUGIN_CHECK_FAILED:
    user: true
    pollable: true
```

| Option | Meaning |
| --- | --- |
| `user` | Events of this type record the acting user when the base configuration includes the group `PLUGIN` in the user setting `user_in_event_group`. That group is offered there once a plugin event type sets `user: true`. |
| `mustuser` | Events of this type always record the acting user. |
| `pollable` | Events of this type are pollable unless the posted event says otherwise. |

The names are used as they are, without the plugin name, so they must not clash with fylr's own event types or another plugin's: a clashing type is dropped with an error in the server log. The types exist while the plugin is enabled. Any logged-in user can post such an event through `POST /api/v1/event`, and the Event Manager labels it with the loca key `admin.event.manager.event.<name in lower case>`. See [Event type reference](../../for-administrators/events/event-type-reference.md#plugin).

## The `exec` map

Extensions, callbacks, collection uploads and custom data type updaters describe **how fylr runs the plugin program** with the same `exec` map. fylr runs it as a job on an [execserver](../execserver.md), so the program is any executable the execserver has a `service` for (`node`, `python3`, `exec` for standalone binaries, …).

```yaml
exec:
  service: "node"          # an execserver service
  timeout: "60s"           # optional — default is fylr.execserver.pluginJobTimeoutSec (2400 s)
  stallTimeout: "20m"      # optional — default is fylr.services.execserver.stallTimeoutSec (600 s), "0" = off
  commands:
    - prog: "node"
      stdin:
        type: body         # fylr streams the input data to STDIN …
      stdout:
        type: body         # … and reads the result from STDOUT
      args:
        - type: "value"
          value: "%_exec.pluginDir%/server/dump_info.js"
        - type: "value"
          value: "%info.json%"
```

| Key | Meaning |
| --- | --- |
| `service` | **Required.** The execserver service that runs the job. A job whose service no connected execserver offers cannot run. |
| `timeout` | How long the job may run, as a duration such as `"90s"` or `"2h"`. Without it, the job gets `fylr.execserver.pluginJobTimeoutSec`. |
| `timeoutSec` | The same in seconds; `timeout` takes precedence. |
| `stallTimeout` | How long a command may run without progress, as a duration; `"0"` turns this off. Without it, the execserver's `stallTimeoutSec` applies. |
| `commands` | **Required.** The commands, run one after another in a shared, transient working directory. The chain stops at the first failing command. |

See [Timeouts](callbacks/README.md#timeouts) for how the limits work together.

### Commands

| Key | Meaning |
| --- | --- |
| `prog` | The program: the name of a command in the execserver's configuration, or a path. |
| `args` | The program's arguments — see [Arguments](#arguments). |
| `stdin` | Where STDIN comes from — see below. |
| `stdout` | Where STDOUT goes — see below. |
| `timeoutSec` | How long this command may run, in seconds, within the job's `timeout`. |

| `stdin.type` | STDIN of the command |
| --- | --- |
| `body` | The input data of the call: the request body of an extension, the payload of a callback. One command per `exec` reads it. |
| `http` | The response to a `GET` of `stdin.url`. |

| `stdout.type` | STDOUT of the command |
| --- | --- |
| `body` | The result of the call: the response of an extension, the result of a callback. |
| `http` | Sent to `stdout.url` with `stdout.method` (default `PUT`). |
| `file` | Written to the file `stdout.file` in the working directory, where the next command can read it. |
| `s3`, `azure` | Uploaded to `stdout.url`, for example a pre-signed storage URL. |

One command per `exec` delivers the result, either through `stdout: { type: body }` or through a `file_out_stream` argument. Without either, the result is the execserver's job report as JSON. STDERR is not part of the result — programs use it for diagnostics.

### Arguments

| `type` | Adds |
| --- | --- |
| `value` | `value` as one argument. |
| `param` | `key` and `value` as two arguments, such as `--mode fast`. |
| `file_in` | `key`, if set, and the path of a file downloaded from `file.url` into the working directory as `file.name`; `file.suffix` is appended to the path, such as `[0]` for ImageMagick. |
| `file_out` | The path of the file `file.name` in the working directory. After the command, the file is uploaded to `file.url`. |
| `file_out_stream` | The path of the file `file.name` in the working directory. After the command, the file is the result of the call; it has no `file.url`. |

```yaml
args:
  - { type: value, value: "%_exec.pluginDir%/server/convert.js" }
  - { type: param, key: "--mode", value: "fast" }
  - { type: file_out_stream, file: { name: "result.zip" } }
```

### Placeholders

fylr and the execserver substitute these placeholders before running the program:

| Placeholder | Substituted in | Description |
| --- | --- | --- |
| `%info.json%` | arguments' `value`, `key` and `file.url`; `stdin.url`, `stdout.url` | The **context** of the call as an **inline JSON string** (not a file path — parse the argument directly): the request, the plugin's base config, and the [callback contract](callbacks/contract.md) fields. Individual callbacks add more keys. |
| `%_exec.pluginDir%` | `prog`; arguments' `value` and `file.name` | Absolute filesystem path of the plugin's directory. Use it to reference scripts and other plugin resources — without it, paths resolve relative to the transient per-job working directory, where the plugin's files do not exist. |
| `%_exec.workDir%` | `prog`; arguments' `value` and `file.name` | Absolute path of the transient per-job working directory. |
| `%_exec.GOOS%`, `%_exec.GOARCH%` | `prog`; arguments' `value` and `file.name` | Operating system and architecture of the executing execserver — for shipping per-platform binaries (`hello-%_exec.GOOS%-%_exec.GOARCH%.exe`). |

## Errors

To signal an error, a plugin program either **exits with a non-zero exit code**, or writes an API-error JSON. When wrapped under a top-level `error` key, a zero exit code is fine:

```json
{
  "error": {
    "code": "error.code",      // defined in the plugin's l10n
    "parameters": {},          // values for the localized message
    "realm": "api",            // used by the frontend for display
    "statuscode": 400          // optional HTTP status for the API response
  }
}
```

When called as an [extension](extensions.md), fylr sets the `X-Execserver-Error` header on failure — unless more than 4&nbsp;KB of the response body have already been sent.

## See also

* [Base config parameters](manifest/base-config.md) — the parameter format of `base_config`, collection upload `config` and custom data type options.
* [Extensions](extensions.md) — add custom API endpoints.
* [Callbacks](callbacks/README.md) — hook into db saves, transitions, collection uploads, export.
* [Custom Data](../customdata.md) — plugins that add custom data types.
* [Plugin Conventions and Standards](conventions.md) and [Packaging and Release](release.md).
