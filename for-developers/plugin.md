---
label: Plugin
description: >-
  Plugins extend fylr with custom data types, custom API endpoints, custom
  frontend snippets and callbacks into fylr's own API calls.
---

# Plugin

Plugins extend fylr through a **callback system** that runs plugin programs in the file-worker tool chain. A plugin is a `manifest.yml` plus an arbitrary tree of resource files; it can add:

* **[Extensions](plugin/extensions.md)** — custom HTTP API endpoints under the plugin's base URL.
* **[Callbacks](plugin/callbacks.md)** — hooks fylr runs during its own API calls (db pre-save, transitions, export, export transport).
* **[Custom data types](customdata.md)** — new field types.
* **Frontend snippets** — JavaScript / CSS loaded into the web frontend.
* **Base-config additions** — extra configuration parameters (for example a plugin user).

fylr must be told to load a plugin in **`fylr.yml`** — either an individual plugin or a directory of plugins. Plugins may be packed into a [`.zip` file](plugin/release.md); fylr serves the resources from within the ZIP, unpacking files on the fly.

## How it fits together

A plugin program is run by the [execserver](execserver.md): fylr serves the program its **input** at `%_input.url%` and the **context** at `%info.json%`, and the program writes its result to `%_output.url%` (or uses STDIN / STDOUT). The [`exec` map](plugin/manifest.md#the-exec-map) in the manifest wires this up, and is the same for extensions and callbacks.

Because callbacks run server-side, they can [call back into the fylr API](plugin/callbacks.md#calling-back-into-the-api) using short-lived tokens fylr hands them.

## Read next

* **[manifest.yml](plugin/manifest.md)** — the plugin descriptor: keys, the `exec` map, URL replacements.
* **[Extensions](plugin/extensions.md)** — add custom API endpoints.
* **[Callbacks](plugin/callbacks.md)** — hook into db saves, transitions and export.
* **[Custom Data](customdata.md)** — add custom data types.
* **[Plugin Conventions and Standards](plugin/conventions.md)** — build, naming, localization.
* **[Packaging and Release](plugin/release.md)** — the ZIP structure and GitHub release workflow.

## Managing plugins

Administrators install and enable plugins in the [Plugin Manager](../for-administrators/plugin-manager/README.md); the [`/api/v1/plugin`](api/endpoints/plugin/README.md) endpoint manages them over the API.
