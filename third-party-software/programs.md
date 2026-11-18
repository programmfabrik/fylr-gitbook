---
description: >-
  The external programs a fylr installation runs, what each one is used for,
  and the license it is distributed under.
---

# Programs fylr runs

Every executable and service the fylr server needs to do its job — conversion,
extraction, indexing, storage — with the license each one carries into the
container image.

Nothing in this document is linked into the fylr binary. Every program below is
forked as its own operating-system process and talks to fylr through argv, files
and exit codes, which is why copyleft tools can sit next to fylr in one image at
all. That argument holds as long as these binaries ship unmodified. What *is*
linked in is attributed separately, in `LEGAL.md`.

- **21** programs the execserver forks, plus their delegates and runtimes
- **44** packages the image installs explicitly
- **6** services fylr talks to over the network

This list describes **v6.36.0**.

Versions are those in the container image of v6.36.0; an installation that
provides these programs itself may carry different ones. The license named is
the principal license of each, taken from the Debian source package's
`debian/copyright` — several of these programs combine code under more than
one, and the authoritative text of every one of them travels inside the image
in `/usr/share/doc/<package>/copyright`.

## Images and vector graphics

| Program                                                            | Version  | What fylr uses it for                                                                                         | License                                |
|--------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [ImageMagick](https://imagemagick.org/) (`magick`)                 | 7.1.2.34 | The default raster converter: renditions, thumbnails, watermarks, IIIF tiles, color space handling            | ImageMagick License (Apache-2.0 style) |
| [libvips](https://www.libvips.org/) (`vips`)                       | 8.18.7   | The fast path for large images, used instead of ImageMagick where it wins on memory                           | LGPL-2.1                               |
| [Inkscape](https://inkscape.org/) (`inkscape`)                     | 1.4.3    | SVG and vector rasterising                                                                                    | GPL and public-domain                  |
| [librsvg](https://gitlab.gnome.org/GNOME/librsvg) (`rsvg-convert`) | 2.63.4   | SVG renditions, and ImageMagick's SVG delegate                                                                | LGPL-2+                                |
| [Ghostscript](https://www.ghostscript.com/) (`gs`)                 | 10.08.0  | ImageMagick's PostScript and EPS delegate                                                                     | AGPL-3+                                |
| [libheif x265 plugin](https://github.com/strukturag/libheif)       | 1.23.6   | HEIC encoding: libheif ships decode-only plugins by default, ImageMagick and vips write HEIC through this one | LGPL-3+ (libheif), GPL-2+ (x265)       |

## Documents and PDF

| Program                                                                    | Version       | What fylr uses it for                                                                                                                                | License                 |
|----------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| [MuPDF](https://mupdf.com/) (`mutool`)                                     | 1.28.0        | PDF page rendering, page counts and the text layer for OCR. Built from the upstream tarball because Debian's mupdf-tools has no ICC color management | AGPL-3.0                |
| [LibreOffice](https://www.libreoffice.org/) (`soffice`)                    | 26.8.2.2      | Every office format to PDF, and from there to previews                                                                                               | MPL-2.0                 |
| [Poppler utils](https://poppler.freedesktop.org/) (`pdftotext`, `pdfinfo`) | 26.07.0       | PDF text extraction and page metadata                                                                                                                | GPL-2 or GPL-3          |
| [Calibre](https://calibre-ebook.com/) (`ebook-convert`, `ebook-meta`)      | 9.18.0        | EPUB and other e-book formats                                                                                                                        | GPL-3                   |
| [Chromium](https://www.chromium.org/) (`chromium`)                         | 156.0.8078.79 | HTML to PDF for the server-pdf plugin                                                                                                                | BSD-3-Clause and others |

## Audio and video

| Program                                                                                 | Version | What fylr uses it for                                               | License                                        |
|-----------------------------------------------------------------------------------------|---------|---------------------------------------------------------------------|------------------------------------------------|
| [FFmpeg](https://ffmpeg.org/) (`ffmpeg`, `ffprobe`)                                     | 9.0.2   | All video and audio transcoding, and probing for technical metadata | GPL-3 as built by Debian (see the open points) |
| [ffmpegthumbnailer](https://github.com/dirkvdb/ffmpegthumbnailer) (`ffmpegthumbnailer`) | 2.3.1   | Video still frames for previews and contact sheets                  | GPL-2+                                         |

## Metadata, text and OCR

| Program                                                                   | Version | What fylr uses it for                                                                                                                      | License                           |
|---------------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| [ExifTool](https://exiftool.org/) (`exiftool`)                            | 13.55   | Reads and writes EXIF, IPTC and XMP on every uploaded file; the metadata backbone. libarchive-zip-perl is what lets it open office formats | Artistic or GPL-1+                |
| [Apache Tika](https://tika.apache.org/) (`tika`)                          | 2.9.2   | Fallback text and metadata extraction for formats nothing else handles                                                                     | Apache-2.0                        |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (`tesseract`) | 5.5.0   | OCR over scanned pages so their text becomes searchable; all language packs are installed                                                  | Apache-2.0                        |
| [Saxon-HE](https://www.saxonica.com/) (`saxon`)                           | 12.9    | XSLT 2.0/3.0 for the XML mapping importer and exporter. Installed with the xmlresolver 5.3.3 jars                                          | MPL-2.0 (xmlresolver: Apache-2.0) |
| [Graphviz](https://graphviz.org/) (`dot`)                                 | 14.1.2  | Renders graph sources uploaded as assets                                                                                                   | EPL-1.0                           |

## Plugin runtimes

| Program                                         | Version  | What fylr uses it for                                                                                                                                                                                                                                                                                 | License                                               |
|-------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [Node.js](https://nodejs.org/) (`node`)         | 24.22.2  | Runs JavaScript plugins                                                                                                                                                                                                                                                                               | MIT and others                                        |
| [Python 3](https://www.python.org/) (`python3`) | 3.14.7   | Runs Python plugins, and is Inkscape's own extension runtime. The listed modules are what the shipped plugins need: opencv for the example plugin, python-pptx (from pip) for PowerPoint metadata, numpy because it is compiled and a plugin cannot bring its own, the rest for HTTP and CSS handling | PSF-2.0 (modules: Apache-2.0, BSD-3-Clause, ISC, MIT) |
| [OpenJDK JRE](https://openjdk.org/) (`java`)    | 25.0.5+8 | The JVM under Tika and Saxon. Tracks the suite's default JDK so the image does not break when Debian moves on                                                                                                                                                                                         | GPL-2 with Classpath exception                        |

## Storage, search and transport

The services fylr talks to over the network. Only the client tools travel
inside our image; the servers themselves are the operator's or the cloud's
deployment.

| Component                                                                  | Version | What fylr uses it for                                                     | Shipped by us?                                                          | License                                   |
|----------------------------------------------------------------------------|---------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------|
| [PostgreSQL](https://www.postgresql.org/)                                  | 18      | The database: every record, right, mask and index state                   | no — a separate container                                               | PostgreSQL License                        |
| [PostgreSQL client tools](https://www.postgresql.org/) (`pg_dump`, `psql`) | 18.6    | Backup and restore invoke these directly                                  | yes                                                                     | PostgreSQL License                        |
| [OpenSearch](https://opensearch.org/)                                      | 3       | The search index, and the default for new installations                   | no — a separate container                                               | Apache-2.0                                |
| [Elasticsearch](https://www.elastic.co/)                                   | 7.17    | The legacy search backend, still in use at some installations             | no — the official image                                                 | Elastic License 2.0 (see the open points) |
| [SQLite](https://sqlite.org/)                                              | —       | The alternative embedded database for small and single-user installations | yes — linked into the binary, so it is attributed in LEGAL.md, not here | public-domain                             |
| [rclone](https://rclone.org/) (`rclone`)                                   | 1.75.0  | The transport plugin's remote storage backend (S3, WebDAV, cloud drives)  | yes — `go install`, copied to `/fylr/bin`                               | MIT                                       |

## Container plumbing

Present in the image but not part of fylr's own work — process supervision,
trust roots, fonts, and the handful of tools an administrator expects in a
shell.

| Component                                                                 | Version            | Role                                                                                                                                                                               | License                                                                                     |
|---------------------------------------------------------------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [s6-overlay](https://github.com/just-containers/s6-overlay)               | 3.2.1.0            | PID 1: signal handling and zombie reaping                                                                                                                                          | ISC                                                                                         |
| [ca-certificates](https://tracker.debian.org/pkg/ca-certificates)         | 20260816           | TLS trust roots, needed for SAML, OIDC and every outbound HTTPS call                                                                                                               | GPL-2+ (scripts), MPL-2.0 (Mozilla CA bundle)                                               |
| [tzdata-legacy](https://www.iana.org/time-zones)                          | 2026f              | Legacy time zone names such as Asia/Calcutta                                                                                                                                       | public-domain                                                                               |
| [fontconfig](https://www.freedesktop.org/wiki/Software/fontconfig/)       | 2.17.1             | Font configuration and lookup for every rendering tool                                                                                                                             | HPND (Keith Packard permissive)                                                             |
| [ttf-mscorefonts-installer](https://tracker.debian.org/pkg/msttcorefonts) | 3.8.1              | Microsoft core fonts, downloaded from upstream while the image is built. Caption rendering asks ImageMagick for the Arial family, and office conversion relies on the same metrics | GPL-2+ (installer); the fonts are proprietary, under Microsoft's EULA (see the open points) |
| [apt-eatmydata](https://www.flamingspork.com/projects/libeatmydata/)      | 1                  | Speeds up package installation while the image is built                                                                                                                            | MIT (Expat)                                                                                 |
| curl, jq, unzip                                                           | 8.22.0, 1.8.2, 6.0 | The container entry point downloads and unpacks plugin archives with these                                                                                                         | curl (MIT-style), MIT, Info-ZIP                                                             |
| Shell tools (`less`, `ping`, `strace`, `tar`, `xz`, `tcpdump`, `nano`)    | —                  | What an administrator expects to find in a shell                                                                                                                                   | GPL-2+/GPL-3+, BSD-3-Clause, LGPL-2.1+, 0BSD                                                |
