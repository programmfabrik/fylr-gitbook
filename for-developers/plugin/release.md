---
label: Packaging and Release of Plugins
description: >-
  How a fylr plugin is packaged into a ZIP, released on GitHub, and installed
  in fylr from its release URL.
---

# fylr Plugins: Packaging and Release

A plugin reaches a fylr instance as a **ZIP**: uploaded in the [Plugin Manager](../../for-administrators/plugin-manager/README.md), or — the normal case — fetched by fylr from a **release URL**, which it re-checks so the plugin updates itself when a new release appears.

Building that ZIP is the job of **[`fylr-build-plugin`](https://github.com/programmfabrik/fylr-build-plugin)**. A plugin repository keeps only a thin `Makefile` shim; `make zip` calls the tool, which compiles the sources, assembles the build tree and writes the archive.

{% hint style="info" %}
The tool's README is the reference for everything about the build itself — `build.yml`, bundles, npm dependencies, cross-compiled Go programs, sealing. This page covers what the **result** has to look like and how it is published. [fylr-plugin-example](https://github.com/programmfabrik/fylr-plugin-example) is the working example of both.
{% endhint %}

## ZIP archive structure

fylr enforces one thing about the archive: it must contain a **single top-level folder named exactly like the plugin**, as defined by `plugin.name` in the manifest, and the manifest must sit inside it as `manifest.yml`.

* `fylr-plugin-example.zip`
  * `fylr_example/`
    * `manifest.yml`
    * `build-info.json`
    * `README.md`
    * `server/`, `webfrontend/`, `l10n/`, … as the plugin needs them

That folder is exactly what `fylr-build-plugin build` assembles into `build/<plugin.name>/`, so the ZIP is the build tree and nothing else. fylr serves the plugin's resources from within the ZIP, unpacking files on the fly.

### How the ZIP is named

The archive is **always `<repository>.zip`** — named after the repository, not after the plugin. This is hard-wired in the build tool: no flag, no environment variable, no per-repo exception.

It matters because the install URL is then derivable without looking anything up:

```
https://github.com/<organization>/<repository>/releases/latest/download/<repository>.zip
```

`plugin.name` is deliberately not used: the two diverge often enough — `fylr-plugin-scancode-display` ships the plugin `fylr-scancode-display`, `fylr-plugin-custom-data-type-k10plus` ships `custom-data-type-gvk` — that a manifest-derived asset name would sit at a URL that disagrees with itself. The name inside the ZIP is unaffected; it stays the plugin name, which fylr requires.

{% hint style="warning" %}
If a plugin's asset name ever has to change, keep publishing the old name alongside the new one. Instances that stored the old URL update from it, and would otherwise stop receiving updates silently.
{% endhint %}

## The release workflow

A release is cut by **publishing a release on the GitHub release page**, with a tag of the form `vX.Y.Z`. The workflow reacts to that:

```yaml
on:
  release:
    types:
      - published
      - edited
```

Two ready-made workflows live in the build tool's [`templates/`](https://github.com/programmfabrik/fylr-build-plugin/tree/main/templates) — copy the one that matches the repository into `.github/workflows/release.yaml`:

| Template | For | Result |
| --- | --- | --- |
| `release-public.yaml` | a **public** repository | the ZIP is attached to the GitHub release; fylr installs from `releases/latest/download/<repo>.zip` |
| `release-private.yaml` | a **private** repository | additionally published to GitHub Pages under an unguessable per-repo UUID URL |

**A public repository needs no GitHub Pages.** Pages is the private variant, and it exists for one reason: fylr cannot fetch a private repository's release assets, so the artifact has to be served from somewhere reachable without credentials.

Either template becomes a **sealed** release by switching `make zip` to `make seal` — sealing uses a public key only, so no secrets go into CI.

### Which steps are always needed

The build always needs **Go**, because the tool runs through `go run`, and the two steps that do the actual work:

```yaml
      - name: Build and package
        run: make zip
        env:
          RELEASE_TAG: ${{ github.event.release.tag_name }}

      - name: Attach plugin zip to the release
        uses: softprops/action-gh-release@v3
        with:
          files: |
            build/*.zip
```

Everything else is conditional on what the plugin contains. The tool checks each external tool only for the step that needs it and fails with an actionable message:

| Step | Needed when |
| --- | --- |
| `actions/setup-node` + `npm install -g coffeescript@1.12.7` | the plugin has CoffeeScript sources |
| `npm install -g sass` | the plugin has SCSS |
| `actions/setup-go` | always — the build tool itself is a Go program; also compiles Go server extensions |

The attach step uploads `build/*.zip` rather than a named file, so the workflow never restates the naming rule.

### The release tag

The tag must be `vX.Y.Z` (`v1.2.3`), optionally with a pre-release suffix such as `v1.2.3-test.1`.

It has to reach the build, because it is written into `build-info.json` as `release` and shown by the plugin manager. The workflow puts it in the environment as `RELEASE_TAG`; the plugin's `Makefile` translates that into the tool's `-release` flag:

```makefile
RELEASE_FLAGS = $(if $(RELEASE_TAG),-release "$(RELEASE_TAG)")
```

The tool itself reads no environment variables — every input is a flag, and this shim is where the workflow's env becomes one.

## Releasing a private plugin to GitHub Pages

The `release-private.yaml` template does the publishing, but the repository has to allow it once:

1. Open the repository settings: `https://github.com/programmfabrik/<repository>/settings`
2. Configure Pages:
   1. Select "Pages"
   2. Under "Build and deployment" select Source "**GitHub Actions**"
3. Configure environments:
   1. Select "Environments"
   2. Select "**github-pages**"
   3. Click "(+) Add deployment branch or tag rule"
      1. Select "Ref type: Tag"
      2. Enter "Name pattern:" `v*.*.*`
      3. "Add Rule"

The published URL is then

```
https://programmfabrik.github.io/<repository>/<repository>-<UUID>-latest.zip
```

where the UUID is a fixed random string chosen once per repository, so the URL is stable across releases but not guessable. That is the URL to give the plugin manager, and the one the marketplace catalog carries.

## Installing from the URL

Enter the URL in the [Plugin Manager](../../for-administrators/plugin-manager/README.md) under **plus → URL**, or — for a plugin in the marketplace — install it from there and fylr resolves the URL itself.

{% hint style="info" %}
fylr cannot use any kind of authentication when loading a plugin. The URL must be reachable directly, which is why private repositories go through Pages.

See also [Network access in restricted setups](../../for-administrators/plugin-manager/README.md#network-access-in-restricted-setups) for the hosts a firewalled instance has to allow.
{% endhint %}
