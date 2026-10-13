---
label: Plugin Conventions and Standards
description: >-
  How a fylr plugin repository is laid out, named, localized and released — the
  rules fylr enforces, and the build driver that produces a conforming plugin.
---

# Plugin Conventions and Standards

A fylr plugin is built by **`fylr-build-plugin`**, the build driver that knows how a plugin is put together. A plugin repository carries no build machinery of its own — no submodule, no vendored makefile include — only a thin `Makefile` shim:

```makefile
FYLR_BUILD_PLUGIN ?= go run github.com/programmfabrik/fylr-build-plugin@latest
```

{% hint style="info" %}
**The canonical reference is the tool's own README:** [fylr-build-plugin](https://github.com/programmfabrik/fylr-build-plugin) — the repository layout, `build.yml`, bundles, npm dependencies, sealing and the release workflow templates. The living example that exercises every feature is [fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example); `fylr-build-plugin init` scaffolds a new plugin with the same structure.

This page states the rules **fylr itself enforces** on the finished plugin, which is what an author has to satisfy however the plugin is built.
{% endhint %}

## Build

* `build/<plugin.name>/` is the plugin in the form fylr loads it: the manifest, `build-info.json`, and the compiled and copied files. fylr can load that folder straight from disk while you develop it — see [Load Custom Plugins](../../for-system-administrators/configuration/custom-plugin.md).
* The build folder is **generated and never committed**. Compiled JavaScript and CSS are build output; development and CI both compile from source.
* A build-info file `build-info.json` sits next to the manifest. fylr reads:
  * `repository`
  * `rev`
  * `release`
  * `lastchanged`
  * `builddate`
  * At a minimum it must carry the git commit id (`rev`) and the release tag (`release`). fylr treats the file as optional and the plugin manager displays it, so an installed plugin can be traced back to a commit and a release. For Programmfabrik plugins it is required.
* `fylr-build-plugin check` validates the assembled tree against every path the manifest references — exec programs, `plugin.l10n`, `plugin.webfrontend.*`, `fas_config` files. It runs with every build; a dangling reference is a warning, because it can be deliberate.

## Naming

* Repositories are named:
  * `fylr-plugin-*`
  * `fylr-plugin-custom-data-type-*` (for custom data types)
  * Tooling is `fylr-<verb>-plugin`, so the `fylr-plugin-` prefix stays reserved for plugins.
* Plugin names are free, but fylr enforces the pattern `^[a-z][a-z0-9\-_]*[a-z0-9]$`:
  * lower case letters and digits only, with `-` and `_` allowed, starting with a letter and not ending with `-` or `_`
  * We use `-` and lower case letters
  * For custom data types, we advise starting the name with `custom-data-type-`.
* **The manifest is `manifest.yml`, and it ships verbatim.** There is no master/generated split: the file in the repository root is copied unchanged to `build/<plugin.name>/manifest.yml`. (Older plugins kept a `manifest.master.yml` that a build rendered; that convention is gone.)
* `plugin.name` in the manifest names the build folder and the ZIP's top-level directory — which fylr enforces on install — while the **release asset is named after the repository**. The two legitimately differ: `fylr-plugin-scancode-display` ships the plugin `fylr-scancode-display`.

## Localization (l10n)

A plugin localizes through the built-in CSV support: the manifest field `plugin.l10n` points to a CSV inside the plugin, and fylr serves the merged localization of all enabled plugins at `/api/v1/plugin/bundle/l10n/<lang>.json`.

**The CSV is a Google Sheets export, committed as it comes.** The master is the "fylr localization" sheet, one tab per plugin; `fylr-build-plugin loca` pulls it. Do not edit it by hand — a hand edit is overwritten by the next pull.

The header looks like this:

```
fil,key,de-DE,R,en-US,R,da-DK,R,fi-FI,R,sv-SE,R
```

| Column | Meaning |
| --- | --- |
| `key` | The localization key. **Required** — this is the column fylr looks up. |
| `de-DE`, `en-US`, … | One column per language, headed by its language tag. The cell is the translation. |
| `fil` | The ticket a row came from. Sheet bookkeeping. |
| `R` | The "needs review" checkbox that follows each language column. Sheet bookkeeping. |

fylr's loader reads **only `key` and the `xx-XX` language columns** and ignores everything else, which is why the raw export can be committed unchanged. An empty cell falls back to the key; enter `-` to render nothing.

The conventions that apply to the sheet itself — never delete headers, never leave blank rows, do not translate anything inside `%(...)`, the `R` review flow — are described under [Localization](../localization.md).

## Release

* A release is cut **on the GitHub release page** by publishing a release; the workflow builds and publishes the artifact. See [Packaging and Release](release.md).
* Release tags follow semver:
  * `v2.34.1`
  * or with a suffix like `v2.34.0-test.1` for pre-releases (the `-suffix` is what marks it as a pre-release)
* Pre-releases are allowed.
* The release asset is `<repository>.zip` — a rule of the build tool, with no override. The install URL a plugin hands out therefore reads as one piece: `https://github.com/<organization>/<repository>/releases/latest/download/<repository>.zip`
* A **private** repository publishes to GitHub Pages instead, because fylr cannot fetch a private repository's release assets.

## Readme

The `README.md` is not only for GitHub. From fylr **6.35.0** the file next to `manifest.yml` inside the ZIP is what the Plugin Manager shows on a plugin's **README** tab, and what the marketplace shows as **more information** before installing — so it has to stand on its own, without the repository around it. `fylr-build-plugin` copies it into the ZIP and inlines its images as data URIs, because a private repository's relative image paths are unreachable from a fylr instance.

Every plugin repository must include a `README.md` that covers at minimum:

* **How to setup**:
  * If a ZIP file is available via URL, include it in the Readme so it can be copied into the fylr Plugin Manager
  * The URL should always link to the latest release, in the form `https://github.com/<organization>/<repository>/releases/latest/download/<repository>.zip`. The asset is named after the **repository**, not after the plugin — `fylr-build-plugin` names it that way and takes no override, and the marketplace catalog builds the install URL from the repository name.
* **How to configure**:
  * describe all configuration options the plugin exposes with their expected values and any defaults
  * e.g. base configuration, system object types, pool settings
* **How to use**:
  * describe the end-user workflow
  * how to invoke the plugin
  * what it does
  * any prerequisites or limitations
