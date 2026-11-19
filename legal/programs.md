---
description: >-
  The open source programs fylr runs, and what it uses each of them for.
---

# Programs fylr uses

{% hint style="info" %}
Compiled from fylr **[v6.36.0-test.3](../releases/2026/v6.36.0-test.3.md)**, published 2026-11-19, the newest release. Each release replaces this page with its own.
{% endhint %}

fylr hands much of the work on files to established open source programs: they create the previews and renditions, convert documents, read and write metadata and recognize text. fylr runs each of them as a separate program; none of them is part of the fylr binary. The fylr container image contains all of them.

## Images and vector graphics

[ImageMagick](https://imagemagick.org/) creates the previews, thumbnails and renditions of images, applies watermarks, prepares the tiles of the IIIF image server and converts between color spaces.

[libvips](https://www.libvips.org/) processes very large images with a fraction of the memory ImageMagick would need, and takes over from it where that matters.

[Inkscape](https://inkscape.org/) turns SVG and other vector graphics into raster images.

[librsvg](https://gitlab.gnome.org/GNOME/librsvg) renders SVG files for previews, for fylr itself and for ImageMagick.

[Ghostscript](https://www.ghostscript.com/) lets ImageMagick read PostScript and EPS files.

The [libheif x265 plugin](https://github.com/strukturag/libheif) lets ImageMagick and libvips write HEIC images.

## Documents and PDF

[MuPDF](https://mupdf.com/) renders the pages of PDF files for previews, counts them, and provides the text layer of a PDF for OCR.

[LibreOffice](https://www.libreoffice.org/) converts office documents — Word, Excel, PowerPoint, OpenDocument and many other formats — to PDF, from which fylr creates the previews.

The [Poppler utils](https://poppler.freedesktop.org/) extract the text and the page information of PDF files.

[Calibre](https://calibre-ebook.com/) converts EPUB and other e-book formats and reads their metadata.

[Chromium](https://www.chromium.org/) turns HTML into PDF for the PDF plugin.

## Audio and video

[FFmpeg](https://ffmpeg.org/) converts video and audio files for previews and downloads, and reads their technical metadata, such as duration, resolution and codecs.

[ffmpegthumbnailer](https://github.com/dirkvdb/ffmpegthumbnailer) takes still frames from videos for previews and contact sheets.

## Metadata, text and OCR

[ExifTool](https://exiftool.org/) reads the embedded metadata of every uploaded file — EXIF, IPTC, XMP and many more — and writes metadata into files when they are downloaded or exported.

[Apache Tika](https://tika.apache.org/) extracts text and metadata from the file formats no other program here handles.

[Tesseract OCR](https://github.com/tesseract-ocr/tesseract) recognizes the text of scanned pages and images, so it becomes searchable. All its language packs are installed.

[Saxon-HE](https://www.saxonica.com/) runs the XSLT stylesheets of the XML mappings for import and export.

[Graphviz](https://graphviz.org/) renders graph sources uploaded as assets into images.

## Plugin runtimes

[Node.js](https://nodejs.org/) runs the plugins written in JavaScript.

[Python 3](https://www.python.org/) runs the plugins written in Python.

The [OpenJDK JRE](https://openjdk.org/) is the Java runtime Apache Tika and Saxon-HE run on.

## Database, search and storage

The database and the search index run next to fylr, not inside its container image: whoever runs fylr provides them.

[PostgreSQL](https://www.postgresql.org/) is the database fylr keeps all its data in.

The backup and the restore of fylr run the [PostgreSQL client tools](https://www.postgresql.org/).

[OpenSearch](https://opensearch.org/) is the search index of fylr, and the default for new installations.

[Elasticsearch](https://www.elastic.co/), the earlier search backend, is still supported for the installations which use it.

[SQLite](https://sqlite.org/) can stand in for PostgreSQL in small and single-user installations.

[rclone](https://rclone.org/) connects the transport plugin to remote storage: S3, WebDAV and cloud drives.
