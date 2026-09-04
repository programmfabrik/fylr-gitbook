---
label: Plugin
description: >-
  Plugins extend fylr with custom data types, custom API endpoints, custom
  frontend snippets and callbacks into fylr's own API calls.
---

# Plugin

Plugins extend fylr through a **callback system** that runs plugin programs in the file-worker tool chain. A plugin is a `manifest.yml` plus an arbitrary tree of resource files; it can add:

* **[Extensions](plugin/extensions.md)** — custom HTTP API endpoints under the plugin's base URL.
* **[Callbacks](plugin/callbacks/README.md)** — hooks fylr runs during its own API calls (db pre-save, transitions, collection uploads, export, export transport).
* **[Custom data types](customdata.md)** — new field types.
* **Frontend snippets** — JavaScript / CSS loaded into the web frontend.
* **Base-config additions** — extra configuration parameters (for example a plugin user).

A finished plugin is delivered as a [`.zip` file](plugin/release.md) and installed in the [Plugin Manager](../for-administrators/plugin-manager/README.md) — from the marketplace, from a release URL, or by uploading the ZIP. fylr serves the resources from within the ZIP, unpacking files on the fly.

While you are **writing** one, point `plugin.paths` in **`fylr.yml`** at the directory you build into and fylr loads it from there — see [Load Custom Plugins](../for-system-administrators/configuration/custom-plugin.md). From fylr 6.35 that is what `plugin.paths` is for: the distribution itself no longer ships plugins on disk.

## How it fits together

A plugin program is run by the [execserver](execserver.md): fylr streams the program its **input** on STDIN, passes the **context** as the `%info.json%` argument, and reads the result from STDOUT. The [`exec` map](plugin/manifest.md#the-exec-map) in the manifest wires this up, and is the same for extensions and callbacks.

Because callbacks run server-side, they can [call back into the fylr API](plugin/callbacks/contract.md#calling-back-into-the-api) using short-lived tokens fylr hands them.

## Read next

* **[manifest.yml](plugin/manifest.md)** — the plugin descriptor: keys, the `exec` map, URL replacements.
* **[Extensions](plugin/extensions.md)** — add custom API endpoints.
* **[Callbacks](plugin/callbacks/README.md)** — hook into db saves, transitions, collection uploads and export.
* **[Custom Data](customdata.md)** — add custom data types.
* **[Plugin Conventions and Standards](plugin/conventions.md)** — build, naming, localization.
* **[Packaging and Release](plugin/release.md)** — the ZIP structure and GitHub release workflow.

## Managing plugins

Administrators install and enable plugins in the [Plugin Manager](../for-administrators/plugin-manager/README.md); the [`/api/v1/plugin`](api/endpoints/plugin/README.md) endpoint manages them over the API.
