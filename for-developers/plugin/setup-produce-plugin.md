---
label: Setting up a plugin to produce file versions
description: >-
  How to setup fylr to call an external HTTP service provided by a plugin to generate file renditions
---

# Setting up a plugin to produce file versions

How to make fylr call an external HTTP service for a rendition.

Assumed to exist already:

* a **conversion service** running under a known URL, for example `http://converter:8000/convert`
* a **produce plugin**, meaning a plugin that ships a cookbook whose recipe calls that URL and that takes the URL as a recipe parameter

Two names are used throughout: the **produce plugin** is the piece installed in fylr, and the **conversion service** is the HTTP endpoint it calls. They are separate things and they usually run in separate places.

fylr's official example plugin, [fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example), carries working produce recipes and is the reference to compare against whenever something below does not match what you see. The [Further reading](#further-reading) section says which files to look at.

Everything else is set up in the base configuration under [File worker > Preview configuration](#id-3.-open-the-renditions-editor)

## What lives where

The split matters, because it decides what you can change in the frontend and what needs a plugin release:

| Thing | Defined in | Changeable in the frontend |
| --- | --- | --- |
| the cookbook and its recipes | plugin (or fylr's built-ins) | no |
| what the command line looks like | plugin | no |
| which recipe parameters exist | plugin | no |
| **which classes and extensions exist** | base config | yes |
| **which versions are produced** | base config | yes |
| **the parameter values, including the endpoint URL** | base config | yes |

So the conversion service's address is base config data. Moving the service to another host or port is a base config edit, not a plugin change and not a restart.

## 1. Install and enable the plugin

Install the plugin in the plugin manager, then make sure it is **enabled**. With `fylr.plugin.default.enabled: false` a freshly installed plugin comes up disabled, and a disabled plugin contributes no cookbooks.

The recipe is now addressable as `<plugin>:<cookbook>:<recipe>`. fylr's built-in recipes have no plugin part and are just `<cookbook>:<recipe>`. You need that exact string in step 3.

Do this **before** step 3: the base config validates recipe names on save, and an unknown recipe is a hard save error.

**Check whether the plugin already brings its own configuration.** A plugin may ship a produce config of its own, declared as `fas_config.produce_config` in its manifest, and fylr merges that into the compiled configuration for every enabled plugin. If it does, the class and the version exist the moment the plugin is enabled and there is nothing to do in the renditions editor. [fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example) works this way through `fas_config/custom_produce.yml`.

The merge is additive: plugin versions are appended to what the base config defines, they do not replace it. Two consequences are worth knowing. Versions contributed by a plugin do not appear as editable entries in the renditions editor, so their parameters, including the endpoint URL, can only be changed in the plugin. And a plugin claiming an extension that another class already claims makes the whole configuration fail to compile, because extensions must be unique across all classes.

## 2. Check reachability from the execserver, not from your machine

The recipe's command runs in the **execserver**, not in the fylr server and certainly not in your browser. The endpoint you type into the base config is resolved there.

* execserver as its own container: `127.0.0.1` is the *execserver's* loopback. Use the service name on the shared docker network, and put the conversion service on that network.
* execserver on the same host as everything else: `127.0.0.1:<port>` is fine.

A URL that answers from your terminal proves nothing about the execserver. If in doubt, get a shell in the execserver container and curl it from there.

## 3. Open the renditions editor

**Base configuration > File worker > Preview configuration**

That editor is a view onto one JSON document, the same document you would POST to `/api/v1/config` as `system.config.produce_config.value`. Its top level is a map of **classes**, and each class holds upload rules and a list of **versions**.

Two ways in:

* **extend an existing class** if the file type is already accepted on upload (a JPEG, a PDF) and you only want one more rendition produced for it. Add a version to that class and stop.
* **add a new class** if the file type is in no class yet. An extension that belongs to no class is refused at upload time with `Filetype "xyz" is unknown and not allowed`, so the class has to come first.

## 4. Class settings (new class only)

| Field | Meaning |
| --- | --- |
| class name | free, lowercase; it is the key of the class, and it is what the recipe's `class` must match |
| `uploadenabledextensions` | every extension the class accepts on upload. Must be **unique across all classes**: no extension may appear in two classes |
| `uploadmaxfilesize` | for example `2gb` |

## 5. Add the version

A **version** is one rendition produced from the upload. Fields worth setting:

| Field | Meaning |
| --- | --- |
| `name` | unique per class, no leading or trailing spaces, not empty |
| `extensions` | which uploads this version is produced for. Must all appear in the class's `uploadenabledextensions`, and must all be supported by the recipe. **Empty means every extension**, which is usually not what you want |
| `recipename` | the `<plugin>:<cookbook>:<recipe>` string from step 1 |
| `params` | the recipe's parameters. **This is where the conversion service URL goes** |
| `group` | `preview`, `thumbnail` or `huge`: how the frontend groups it in download and URL selections |
| `standard` | include it in `_standard.eas` lists, meaning it becomes part of the normal payload delivered with the asset |
| `displayname` | per-language label |
| `sourceversion` | produce from another version instead of from the original. Leave empty for the original |
| `rightsmanagement`, `watermark` | flags the server and frontend act on |

Parameter values are checked against the recipe's declared type, ranges and select options **at save time**. A typo in a number range or an option is a save error, not a runtime surprise.

If different extensions of one class need different recipes, add **several version entries with the same `name`**, each with its own extensions and recipe. That is supported, but `standard`, `rightsmanagement`, `watermark` and `group` must be identical on all of them.

## 6. Save, and read the error if it fails

The save runs the full produce config check. The messages are precise; these are the ones you will actually hit:

| Message | Cause |
| --- | --- |
| `uses an unknown recipe "…"` | plugin not installed, not enabled, or the recipe string is misspelled |
| `misses upload enable for extension "…"` | the extension is on the version but not in the class's `uploadenabledextensions` |
| `Extension "…" is also defined in "…"` | two classes claim the same extension |
| `doesn't support the class "…"` | the recipe's `class` is not the class you put it under |
| `doesn't support the extension "…"` | the extension is not in the recipe's extension list |
| `contains an invalid version "…"` | empty version name or surrounding whitespace |
| `contains contradicting settings for version "…"` | same version name twice with differing `standard`, `rightsmanagement`, `watermark` or `group` |
| `Mandatory parameter '…' missing`, `Value '…' is higher than maximum …`, `Unsupported param value '…'` | parameter values rejected against the recipe's declaration |
| `unknown source version "…"` | `sourceversion` names a version that does not exist in this class |

Note the asymmetry: on **save** an unsupported extension is rejected, while on **load** (server start, plugin gone) the same situation is handled leniently and the extension, possibly the whole version, is silently dropped with a warning in the log. So a version that quietly stops being produced after a plugin was disabled is expected behaviour, and the log is where it says so.

## 7. Verify

Upload a matching file. The new version should appear on the asset.

If it does not, look for a [`FILE_PRODUCE_ERROR`](/for-administrators/events/event-type-reference.md#file_produce_error) event. It carries the job receipt: the full command line, stdout and stderr. For a conversion service the usual causes are, in order of likelihood:

1. the endpoint is not reachable *from the execserver* (see [step 2](#id-2.-check-reachability-from-the-execserver-not-from-your-machine))
2. the service answered 4xx or 5xx and the recipe did not turn that into a non-zero exit, so the error page gets stored as the rendition and the version exists but is garbage
3. the service returned a different format than the version's file extension claims

## 8. Later changes

* **Conversion service moved**: edit the endpoint parameter on the version and save. No plugin change, no restart.
* **Endpoint per version**: each version carries its own parameters, so two versions of the same class can point at two different services.
* **Existing assets** are not re-produced by a base config change. Renditions are produced on upload, so changing the config affects new uploads and existing files need an explicit re-produce.
* **Removing the plugin** while the config still references its recipe stops the version from being produced, dropped on load with a warning. Clean the version out of the base config rather than leaving a dangling reference.

## Scope, once more

A recipe produces a **version (rendition) attached to an uploaded file**. It never creates a new asset. If the conversion service is supposed to turn an upload into a separate asset of its own, this is the wrong hook entirely: that is a server-side plugin callback uploading through `/api/v1/eas`.

If the goal is not a rendition at all but metadata extracted from the file, the hook is a metadata recipe (class `_metadata`) rather than a version. [fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example) has several of those.

## Further reading

[fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example) is the official example plugin and covers the plugin side of everything above:

| File | What it shows |
| --- | --- |
| `manifest.yml`, section `fas_config` | how a plugin registers its cookbooks and, optionally, its own produce config |
| `fas_config/cookbook_grayscale.yml` | two produce recipes in one cookbook: one calling a binary that exists in the execserver image, one running a script shipped with the plugin through `%_exec.pluginDir%`. A recipe calling a conversion service has the same shape and differs only in the command |
| `fas_config/custom_produce.yml` | a plugin shipping its own produce config, so the class and version exist as soon as the plugin is enabled |
| `fas_config/cookbook_metadata_example.yml`, `fas_config/cookbook_metadata_pdf2text.yml` | metadata recipes, including request-only ones that run lazily when a mapping asks for them |

The recipes there run their converter inside the execserver instead of calling out to an HTTP service. That is the other way to build a produce plugin, and it avoids the reachability question in step 2 entirely, at the price of the converter having to exist in the execserver image or travel with the plugin.
