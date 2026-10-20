---
label: Plugin
description: >-
  Plugins extend fylr with custom data types, custom API endpoints, custom
  frontend snippets and callbacks into fylr's own API calls.
---

# Plugin

Plugins extend fylr through a **callback system** that runs plugin programs on the [execserver](execserver.md). A plugin is a `manifest.yml` plus an arbitrary tree of resource files; it can add:

* **[Extensions](plugin/extensions.md)** — custom HTTP API endpoints under the plugin's base URL.
* **[Callbacks](plugin/callbacks/README.md)** — hooks fylr runs during its own API calls (db pre-save, transitions, collection uploads, export, export transport).
* **[Custom data types](customdata.md)** — new field types.
* **Frontend snippets** — JavaScript / CSS loaded into the web frontend.
* **[Base-config additions](plugin/manifest/base-config.md)** — configuration parameters an administrator sets (for example a plugin user).
* **[File-processing recipes](plugin/setup-produce-plugin.md)** — cookbooks and versions for the file worker.
* **[System rights](plugin/manifest.md#system_rights)** and **[event types](plugin/manifest.md#custom_events)** of its own.

A finished plugin is delivered as a [`.zip` file](plugin/release.md) and installed in the [Plugin Manager](../for-administrators/plugin-manager/README.md) — from the marketplace, from a release URL, or by uploading the ZIP. fylr serves the resources from within the ZIP.

While you are **writing** one, point `plugin.paths` in **`fylr.yml`** at the directory you build into and fylr loads it from there — see [Load Custom Plugins](../for-system-administrators/configuration/custom-plugin.md).

## How it fits together

A plugin program is run by the [execserver](execserver.md): fylr streams the program its **input** on STDIN, passes the **context** as the `%info.json%` argument, and reads the result from STDOUT. The [`exec` map](plugin/manifest.md#the-exec-map) in the manifest wires this up, and is the same for extensions and callbacks.

Because callbacks run server-side, they can [call back into the fylr API](plugin/callbacks/contract.md#calling-back-into-the-api) using short-lived tokens fylr hands them.

## Debugging frontend plugins

The JavaScript and CSS of **all** enabled plugins is served to the web frontend concatenated into a single bundle (`/api/v1/plugin/bundle.js`, `bundle.css`). This is efficient in production, but it has one consequence while developing: **a JavaScript error thrown while one plugin's code is evaluated aborts the rest of the bundle.** Every plugin whose code comes after the failing one in the bundle is then silently not loaded — including plugins you did not touch. A typical symptom is that a [custom data type](customdata.md) stops being recognised in the data model editor and masks (`Unsupported Column Type in Mask`, the field shows `(attrs.undefined missing) (plugin not loaded)`), even for plugins that were working before — because a single broken plugin earlier in the bundle took them all down with it.

To find the culprit, set this in **`fylr.yml`** and restart fylr:

```yaml
fylr:
  debug:
    # Serve each plugin's frontend code separately instead of as one
    # concatenated bundle. A broken plugin then only breaks itself, and
    # the browser console names the file it failed in.
    noPluginsBundle: true
```

With `noPluginsBundle: true`, fylr stops announcing the bundle and the frontend loads each plugin's frontend files on their own, so one plugin's error no longer affects the others and the browser console points at the specific plugin that failed. Turn it off again for production.

{% hint style="info" %}
The console error from the bundle is the quickest signal: the **first** `Uncaught …` error that names `bundle.js` is the failing plugin. Look it up by the line number, or disable plugins one at a time in the [Plugin Manager](../for-administrators/plugin-manager/README.md) (reloading after each) until the other plugins reappear.
{% endhint %}

## Read next

* **[manifest.yml](plugin/manifest.md)** — the plugin descriptor: keys, the `exec` map, URL replacements.
* **[Extensions](plugin/extensions.md)** — add custom API endpoints.
* **[Callbacks](plugin/callbacks/README.md)** — hook into db saves, transitions, collection uploads and export.
* **[Custom Data](customdata.md)** — add custom data types.
* **[Plugin Conventions and Standards](plugin/conventions.md)** — build, naming, localization.
* **[Packaging and Release](plugin/release.md)** — the ZIP structure and GitHub release workflow.

## Managing plugins

Administrators install and enable plugins in the [Plugin Manager](../for-administrators/plugin-manager/README.md); the [`/api/v1/plugin`](api/endpoints/plugin/README.md) endpoint manages them over the API.
