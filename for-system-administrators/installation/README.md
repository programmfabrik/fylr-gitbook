---
description: >-
  As a Go program, fylr supports many platforms. For some installation
  scenarios, we prepare instructions and tools:
---

# Installation

{% hint style="info" %}
Please note: We do all of our automated and manual software testing based on Linux servers. There is no dedicated testing on Windows and almost no testing on Kubernetes.
{% endhint %}

## Linux

* Instructions and Requirements: [Linux](linux-docker-compose.md)
* Uses docker-compose.
* 3rd party tools for thumbnails are pre-packaged.
* If unsure, use this method when installing yourself.
* We offer maintenance contracts and hosting contracts for this variant. Contact us at e.g. [support@programmfabrik.de](mailto:support@programmfabrik.de).

## Windows

* Instructions and Requirements: [Windows](windows.md)
* We provide a list of 3rd party tools for thumbnails but not the tools themselves.
* Some of our partners offer maintenance contracts for this variant. Ask us for more at [support@programmfabrik.de](mailto:support@programmfabrik.de).

## Kubernetes

* Instructions: See our [helm chart](https://github.com/programmfabrik/fylr-helm/blob/main/charts/fylr/README.md).
* Requirements:
  * Uses Helm charts and Linux containers.
  * Needs Helm and a Kubernetes cluster.
* Features:
  * Third-party tools for thumbnails are pre-packaged.
  * A fylr instance can be started as many times as desired. Load balancing is handled externally (e.g., by a load balancer), not by fylr itself. All instances run in parallel, equally privileged, and share a common database.
  * A fylr instance can also be configured to act only [as an execution server](https://github.com/programmfabrik/fylr-helm/tree/main/charts/execserver#as-stand-alone-execserver). In such cases, its fylr.yml does not configure an API/web server, and it does not require a database. fylr servers notify the execution server when they have jobs to process. Horizontal scaling is most beneficial in this configuration.
* Licensing Notes: You need the fylr edition Organization to run fylr in a kubernetes environment.
* Monitoring: Every fylr instance shows how many others are currently connected in parallel.
* Support: We offer no support for this variant, only bug fixes for issues reported to [​support@programmfabrik.de](mailto:support@programmfabrik.de).

## Topics for all variants

### Software Versions

* We are regularly testing fylr with **Opensearch 3** and **PostgreSQL 18** and recommend them with fylr. Customers with problems and earlier versions may be asked to upgrade first.

### Download binaries

From fylr **6.34.0**, the downloadable macOS, Windows and Linux binaries are compiled without cgo: they are **statically linked** and use the pure-Go SQLite driver, so they run on any host of their platform without a C toolchain or extra system libraries. The official **Docker image is unchanged** — it keeps cgo and the C-based SQLite driver — and PostgreSQL deployments are unaffected either way.

### Updating a self-installation to 6.35

This is for fylr run from the downloadable archives or [built from source](from-source.md) on Linux, macOS or [Windows](windows.md), with the third-party tools installed by you. The Docker image and the Helm chart bring these changes with them. For Windows, the steps are listed in [Updating from 6.34 to 6.35](windows.md#updating-from-6.34-to-6.35).

**Ghostscript renders EPS, AI and PS.** fylr runs Ghostscript itself, as `gs`; Inkscape is left with SVG and WMF. Without Ghostscript these files get no previews. On Linux install the `ghostscript` package, on macOS `brew install ghostscript` (Homebrew's ImageMagick does not bring it along). On Windows the program is called `gswin64c.exe`, see [Ghostscript](windows.md#ghostscript).

**The archives no longer contain the plugins.** The `easydb-plugins` folder is gone: the upgrade converts the enabled plugins to their marketplace releases, which fylr then downloads, see [Disk to URL plugin migration](../../plugins/disk-to-url-migration.md). Remove the `easydb-plugins` entries from `plugin.paths` in your `fylr.yml` and delete the folder; otherwise fylr warns about the old copies at every start and brings back the plugins the upgrade removed.

**Check `fylr.yml` before the restart.** `fylr config check fylr.yml` names the keys 6.35 no longer knows or ignores, among them several execserver settings, see [Updating the execserver to 6.35](updating-the-execserver-to-6.35.md). The `fylr.yml` of the Windows archive was corrected in 6.35. If yours started from an earlier one, take over:

* `db+:` instead of `db:` — a bare `db:` drops the connection pool defaults,
* delete a `services:` line under `execserver+:` that has nothing below it — it replaces the shipped service list with an empty one, so the execserver converts nothing and runs no plugin,
* `update_policy` instead of `update` in the per-plugin entries under `plugin.defaults`; `plugin.default`, the setting for all new plugins, already uses `update_policy`.

`fylr config check` warns about the first two and reports `update` as an unknown key.

**Building from source needs Go 1.27.**

**Coming from 6.34.0**, two patch releases changed the tool requirements:

* **mutool needs ICC color management** (6.34.1); without it, CMYK PDFs render with oversaturated colors. Debian's and Ubuntu's `mupdf-tools` are built without it, Homebrew's `mupdf-tools` has it. A build without it prints `warning: ICC support is not available` when it renders a PDF:

  ```bash
  mutool draw -o /tmp/check.png any.pdf
  ```

  On Debian and Ubuntu build mutool the way the Docker image does:

  ```bash
  sudo apt-get install build-essential pkg-config curl
  curl -fsSL -o mupdf.tar.gz https://mupdf.com/downloads/archive/mupdf-1.28.0-source.tar.gz
  mkdir mupdf && tar -xzf mupdf.tar.gz -C mupdf --strip-components=1
  make -C mupdf -j"$(nproc)" HAVE_X11=no HAVE_GLUT=no tools
  sudo install -m 0755 mupdf/build/release/mutool /usr/local/bin/mutool
  ```

  Previews produced before keep their colors until the files are produced again.
* **Writing HEIC** (6.34.2) needs libheif with its x265 encoder: the `libheif-plugin-x265` package on Debian and Ubuntu; Homebrew's `libheif` includes it; for Windows see [ImageMagick](windows.md#magick.exe-imagemagick).

### Troubleshooting

[fylr log messages that can be ignored](../symptom-and-solution/log-messages-that-can-be-ignored.md)
