---
description: >-
  Build the fylr binary from source and run it directly on a host (without
  Docker) — the build toolchain, the datastores, and the third-party tools the
  execserver needs.
---

# Install from Source (bare metal)

This page covers **building fylr from source** and running it **directly on a host**, without Docker. For the supported turnkey paths see [Linux (docker-compose)](linux-docker-compose.md), [Windows](windows.md) or [Kubernetes (Helm)](helm.md). The [Windows](windows.md) page's per-tool config snippets are a useful companion for wiring up the third-party tools on any bare host.

{% hint style="info" %}
Since fylr **6.34.0** the pre-built macOS/Windows/Linux binaries are statically linked (cgo-free, pure-Go SQLite) and run without a C toolchain — so building from source is only needed for development, patched builds, or unsupported platforms.
{% endhint %}

## 1. Build the binary

**Requirements**

* **Go 1.26** (see `go.mod`).
* **git** — the web frontend is a submodule.
* **Node.js + npm** and **sass** — to build the embedded web frontend.
* A **C toolchain** — the default build keeps cgo for the native SQLite driver.

**Build**

```bash
git clone https://github.com/programmfabrik/fylr.git && cd fylr
git submodule update --init --recursive     # pull the web frontend submodule
make all                                     # generate + build frontend + build ./fylr
```

`make all` runs three steps: **`generate`** (produces the generated `errors.go` and CSS — a plain `go build` will not compile without it), **`webfrontend`** (builds the SPA that is embedded into the binary via `go:embed`), and **`build`** (the Go binary). Every Go invocation requires `GOEXPERIMENT=jsonv2`, which the Makefile sets for you. The result is `./fylr`.

Granular / development targets:

| Target | Does |
| --- | --- |
| `make generate` | regenerate `errors.go` + CSS (run once on a fresh checkout) |
| `make webfrontend-ensure` | init the submodule and build the frontend if it is missing |
| `make build` | just the Go binary (generate + frontend must already exist) |
| `make server` | config + frontend + generate + build + **run** |
| `make server-fast` | same as `server` but skips `generate` |

{% hint style="warning" %}
The web frontend submodule must be initialized **and built** before compiling — `go:embed` embeds `resources/easydb-webfrontend/build`, so that directory has to exist at compile time. `make all` / `make webfrontend-ensure` guarantee this.
{% endhint %}

## 2. Run

```bash
./fylr server -c fylr.yml
```

The default login is `root` / `admin`. Configure the datastores in `fylr.yml` (or through `FYLR_*` environment variables; multiple `-c` files merge).

### Datastores

fylr needs a database and a search index. Recommended: **PostgreSQL 18** and **OpenSearch 3** (the versions the install team tests against).

```yaml
db:
  driver: postgres
  dsn: "host=localhost port=5432 user=fylr password=fylr dbname=fylr sslmode=disable"

# the search-index config block is named "elastic" even for OpenSearch
elastic:
  addresses:
    - "http://localhost:9200"
```

* Install the **`analysis-icu`** plugin in OpenSearch (index creation fails without it) and set `vm.max_map_count=262144` on the host.
* For a single-node dev instance you can use SQLite instead (`driver: sqlite3`, a file `dsn`).

With just these two, fylr boots and serves the frontend; asset previews and metadata extraction need the third-party tools below.

## 3. Third-party tools (the execserver)

The [execserver](../../for-developers/execserver.md) shells out to external programs for previews, metadata and plugins. On a bare host each must resolve on `$PATH` (or be pointed at via `fylr.services.execserver.commands` / a `FYLR_CMD_<PROG>` env var). Each execserver service runs a `startupCheck` that pins the expected tool version, so a present-but-wrong-version tool still fails.

The full set (matching the official Docker image — Debian package names):

```
imagemagick libmagickcore-7.q16-10-extra   # magick (ImageMagick 7)
libvips-tools                              # vips  (>= 8.16)
librsvg2-bin ghostscript inkscape          # SVG / EPS delegates
exiftool libarchive-zip-perl               # metadata (+ office formats)
ffmpeg ffmpegthumbnailer                   # video / ffprobe
libreoffice                                # soffice (office conversions)
mupdf-tools poppler-utils                  # mutool (PDF render), pdfinfo
tesseract-ocr-all                          # OCR
calibre                                    # EPUB
default-jre-headless libsaxonhe-java       # java (Tika), Saxon-HE (XSLT)
graphviz chromium                          # dot; HTML->PDF (server-pdf plugin)
nodejs python3                             # plugin runtimes
postgresql-client-18                       # pg_dump / psql (backup & restore)
ttf-mscorefonts-installer fontconfig       # rendering fonts
ca-certificates tzdata-legacy
```

Extra Python modules used by some plugins (`python3-requests`, `python3-requests-oauthlib`, `python3-opencv`, `python3-cssselect`, `python3-tinycss2`, …) are installed with `pip3`.

{% hint style="info" %}
**Version gotchas:** ImageMagick must be **v7** and is called as `magick` (fylr ≥ 6.34 no longer uses the deprecated `magick convert`); libvips **≥ 8.16**; the OpenSearch `analysis-icu` plugin is required; the `postgresql-client` major should match your PostgreSQL server (used for backup/restore, configurable via `FYLR_CMD_PG_DUMP`). If a program has a different name on your distribution, override it in `fylr.services.execserver.commands`.
{% endhint %}

## See also

* [Installation](README.md) — the supported install methods and recommended software versions.
* [Windows](windows.md) — per-tool download links and `execserver.commands` snippets.
* [Exec server](../../for-developers/execserver.md) — how fylr runs these tools.
* [Configuration](../configuration/README.md) — `fylr.yml` in depth.
