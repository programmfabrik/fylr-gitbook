---
label: Plugin Conventions and Standards
description: >-
  Conventions and standards for building, naming, localizing, and releasing fylr
  plugins, including README requirements.
---

# Plugin Conventions and Standards

## Build

* The `build` folder must be cleaned before building using `make clean`.
* `make build` generates the build folder as the basis for the ZIP file.
* The ZIP must contain a single top-level folder named exactly like the plugin name as defined in the manifest (enforced by fylr: `/<plugin-name>/manifest.yml`).
* The manifest must be inside that top-level folder and must be named `manifest.yml` (YAML, enforced by fylr).
* A build info file `build-info.json` must be placed next to the manifest
  * fylr reads these fields:
    * `repository`
    * `rev`
    * `release`
    * `lastchanged`
    * `builddate`
  * At a minimum it must include the git commit id (`rev`) and the release tag (`release`)
  * fylr treats the file as optional, but for our plugins it is required.

## Naming

* Repositories are named:
  * `fylr-plugin-*`
  * `fylr-plugin-custom-data-type-*` (for custom data types)
* Plugin names are free, but fylr enforces the pattern `^[a-z][a-z0-9\-_]*[a-z0-9]$`:
  * lower case letters and digits only, with `-` and `_` allowed, starting with a letter and not ending with `-` or `_`
  * We use `-` and lower case letters
  * For custom data types, we advise starting the name with `custom-data-type-`.
* The manifest inside the ZIP must be named `manifest.yml`
  * Outside the build it does not matter, but we follow the convention of using `manifest.master.yml` as the source; the build renders it to `manifest.yml`.

## Localization (l10n)

* The plugin is free to decide how to handle localization keys.
* It can however use the built-in l10n CSV support fylr offers: the manifest field `plugin.l10n` points to the CSV file inside the plugin, and fylr serves the merged localization of all enabled plugins at `/api/v1/plugin/bundle/l10n/<lang>.json`.
* A Google Sheet is the recommended setup for managing translations.

## Release

* GitHub must be used to [create releases](release.md#github-release-workflow) and [set release tags](release.md#include-the-github-release-tag-in-build-info)
* Pre-releases are allowed
* The release workflow must [build the ZIP file](release.md#zip-archive-structure)
* For private repositories, the release must [copy the ZIP to GitHub Pages](release.md#release-of-private-plugins-to-github-pages)
* Release tags follow semver:
  * `v2.34.1`
  * or with a suffix like `v2.34.0-test.1` for pre-releases (the `-suffix` is what marks it as a pre-release)

## Readme

Every plugin repository must include a `README.md` that covers at minimum:

* **How to setup**:
  * If a ZIP file is available via URL, include it in the Readme so it can be copied into the fylr Plugin Manager
  * The URL should always link to the latest release, in the form `https://github.com/<orgranization>/<plugin>/releases/latest/download/<plugin>.zip`
* **How to configure**:
  * describe all configuration options the plugin exposes with their expected values and any defaults
  * e.g. base configuration, system object types, pool settings
* **How to use**:
  * describe the end-user workflow
  * how to invoke the plugin
  * what it does
  * any prerequisites or limitations
