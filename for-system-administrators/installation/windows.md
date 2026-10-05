---
description: How to install fylr on Microsoft Windows
---

# Windows

There are two ways to install fylr on Windows:

* The fully automated installer made by Attention Solutions: [https://attention.dk/docs/att/doku.php?id=winfylr:start](https://attention.dk/docs/att/doku.php?id=winfylr:start) - needs a paid subscription with Attention Solutions.
* fylr directly from the developer Programmfabrik GmbH, with the 3rd party tools downloaded by yourself. The rest of this page guides you through this.

## Download fylr.exe

* Go to the newest release in [https://docs.fylr.io/releases](https://docs.fylr.io/releases)
* Download `fylr_v6.`X.Y`_windows_amd64.zip` and unpack.

It contains:

* `fylr.exe` fylr native for Windows amd64.
* `fylr.yml` a starting configuration already adjusted with Windows path syntax and for the following instructions.
* `fylr.example.yml` most configuration parameters. Look here for reference.
* `fylr.default.yml` compiled-in default values. Just as a copy for you to look them up.
* `LICENSE` legal information on who may use fylr.
* `README.md` pointing to this page.

Up to 6.34 the archive also contained an `easydb-plugins` folder. From 6.35 plugins come from the plugin manager; updating an installation from 6.34 is described in [Updating a self-installation to 6.35](README.md#updating-a-self-installation-to-6.35).

## Windows path length

The shorter the path of your fylr installation directory, the less likely your installation will fail processing files due to exceeding the [length limit](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry). So prefer `C:\fylr` over `C:\user\jane doe\Desktop\software-project\fylr-v6.17.0\unpacked`. fylr newer than v6.3.1 will try to use only short internal file names, but every little bit helps. Same for Libre Office installation (more about that below).

## Get the dependencies

Bare bone minimum: Elasticsearch or OpenSearch

The versions named below are the ones tested. Other versions should also be fine, unless a section names a minimum.

### OpenSearch

OpenSearch is the default and recommended indexer.

Install OpenSearch as described in [https://opensearch.org/docs/latest/install-and-configure/install-opensearch/windows/](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/windows/) (tested with version 3.6.0, downloaded and unzipped):

* Disable security and let OpenSearch listen only on localhost, which protects it, in `opensearch-3.6.0\config\opensearch.yml`:

```
network.host: 127.0.0.1
plugins.security.disabled: true
```

* Raise one limit for fylr in `opensearch-3.6.0\config\jvm.options`:

```
-Dopensearch.xcontent.depth.max=10000
```

* Install the one plugin fylr needs:

```
opensearch-3.6.0> .\bin\opensearch-plugin install analysis-icu
```

* Start OpenSearch:

```
opensearch-3.6.0> .\opensearch-windows-install.bat
```

### Elasticsearch

Elasticsearch was the default until 2023. OpenSearch is recommended instead, especially for a new instance or when Elasticsearch causes problems.

If you use Elasticsearch, use version `7.17`: versions `8.5` and newer have a <mark style="background-color:red;">problem</mark> indexing the letters _Q_ and _W_, of all things. The steps below were tested with `8.6.1`:

* Download from [https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html)
* Unpack the official Windows release file `elasticsearch-8.6.1-windows-x86_64.zip`.
* Disable security in `elasticsearch-8.6.1\config\elasticsearch.yml`:

```
xpack.security.enabled: false
```

* Get the analysis-icu plugin from [https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html) for offline installation (for 8.6.1: https://artifacts.elastic.co/downloads/elasticsearch-plugins/analysis-icu/analysis-icu-8.6.1.zip).
* Unpack it into `elasticsearch-8.6.1\plugins\analysis-icu\` (no further subfolders).
* Start Elasticsearch, for example in a Windows PowerShell:

```
.\elasticsearch-8.6.1\bin\elasticsearch.bat
```

Elasticsearch then listens on the default address `http://localhost:9200`, which is also configured in `fylr.yml`.

### Start fylr with minimal dependencies

To test or start with minimal effort, edit `fylr.yml` to use no 3rd party tools for the moment:

```
fylr+:
  [...]
  services+:
  [...]
    execserver+:

      commands:
        fylr:
          prog: fylr.exe
```

Then start fylr in the folder where `fylr.exe` is. Most asset processing tools are still missing, so there are no previews yet:

```
.\fylr.exe server -c fylr.yml
```

Output lines with `WRN` can usually be ignored.

Harmless Errors known to appear are e.g.

* `Error occurred in NewIntrospectionRequest` and `Accepting token failed`, when a browser tries to use old credentials.

#### Access the web frontend

Browse [http://localhost](http://localhost)

Default login credentials are:

* **Username**: _root_
* **Password**: _admin_

### More than bare bone minimum

For a full installation, install all of the following and add a command for each tool to `fylr.yml`, see [Configure the tools in fylr.yml](windows.md#configure-the-tools-in-fylr.yml).

### PostgreSQL

* Install PostgreSQL from [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) (tested with 15.2).
* In pgAdmin, create a role "fylr" (with LOGIN and INHERIT, the defaults) with the password "fylr", and a database "fylr" owned by role "fylr".
* Un-comment these lines in `fylr.yml`, that is, turn the comments into configuration:

```
    driver: postgres
    dsn: "host=localhost port=5432 user=fylr password=fylr dbname=fylr sslmode=disable"
```

* Disable the lines configuring sqlite by turning them into comments:

```
    #driver: sqlite3
    #dsn: "data\\sqlite.db"
```

* For a consistent state, also do the next step: cleanup.

#### cleanup

If you want to go back to a fresh state between two test runs:

* Stop fylr.exe and the indexer (opensearch or elasticsearch). Optionally check that java / openjdk is stopped alongside elasticsearch.
* Remove the directory `data` and elasticsearch's `data/*` .
* Start elasticsearch as shown at the beginning.
* If you use PostgreSQL, remove and recreate the database.

### pdf tools

* Download the newest release zip (tested with `Release-26.02.0-0.zip`) from [https://github.com/oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases) (_not_ xpdf-tools from https://www.xpdfreader.com).
* fylr only uses `pdfinfo.exe` from poppler: PDF text extraction is done by tika, PDF page rendering by mupdf's mutool (both below).
* Unpack the release and configure the path to `pdfinfo.exe` in `fylr.yml`, or add the containing directory to the PATH.

### magick.exe (ImageMagick)

* Download the newest portable archive (tested with `ImageMagick-7.1.2-26-portable-Q16-HDRI-x64.7z`) from [https://imagemagick.org/script/download.php#windows](https://imagemagick.org/script/download.php#windows)
* Put `magick.exe` from the download into `C:\fylr\utils`. It is the only ImageMagick binary fylr needs; compositing etc. run as subcommands of `magick.exe`. (`convert.exe` and `composite.exe` are not used by fylr and are no longer part of current ImageMagick anyway.)

**Use a current ImageMagick, and fylr v6.34.0 or newer.** Version traps around ImageMagick:

* Current ImageMagick no longer accepts the deprecated `magick convert` command form. fylr up to v6.33 called ImageMagick that way, so previews fail with ``NoDecodeDelegateForThisImageFormat `convert'``. fylr v6.34.0 and newer calls `magick` in the modern form, which works with old and new ImageMagick 7.
* ImageMagick Windows builds from before mid-2024 embed a libheif older than 1.18, which cannot decode HEIC photos taken by newer iPhones (iOS 18 and later): previews fail with `Too many auxiliary image references`. To check what your magick.exe embeds, run the following — the version in parentheses is the libheif version and must be 1.18 or newer:

```
C:\fylr\utils> .\magick.exe -list format | findstr /i heic
     HEIC  HEIC      rw+   High Efficiency Image Format (1.22.2)
```

* **Writing** HEIC (a custom rendition, crop-tool file variant or produce request with `format=heic`, available since fylr 6.34.2) additionally needs a libheif with an HEVC encoder (x265). The official fylr docker image ships the `libheif-plugin-x265` package. On Windows the embedded libheif of the ImageMagick build must be able to encode HEVC: if reading HEIC works but producing a HEIC fails, the embedded libheif lacks the encoder.

Hint from the [download page](https://imagemagick.org/script/download.php#windows):

> If you have any problems, you likely need vcomp140.dll. To install it, download Visual C++ Redistributable Package(https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads).

### Exiftool.exe

Download the newest 64-bit Windows Executable (tested with `exiftool-13.59_64.zip`) from [https://exiftool.org](https://exiftool.org).

Put the contents of the zip — exiftool(-k).exe and (in newer packages) the `exiftool_files` folder next to it — into `C:\fylr\utils`, and rename exiftool(-k).exe to exiftool.exe, as the ExifTool install notes recommend.

### Ffmpeg.exe and ffprobe.exe

Download a current release build (tested with `ffmpeg-n8.1-latest-win64-gpl-8.1.zip`) from [https://github.com/BtbN/FFmpeg-Builds/releases](https://github.com/BtbN/FFmpeg-Builds/releases). Avoid the LGPL version: it lacks features such as x264 and x265.

Put ffmpeg.exe and ffprobe.exe into `C:\fylr\utils`.

### Node

Download the current LTS version (tested with `node-v24.18.0-win-x64.7z`) from [https://nodejs.org/en/download](https://nodejs.org/en/download) and put just node.exe into `C:\fylr\utils`.

### Python

Download the "Windows embeddable package (64-bit)" from [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) (explained [here](https://docs.python.org/3/using/windows.html#windows-embeddable)) and unpack the whole package as the folder "python3" inside `C:\fylr\utils`.

### Java

To extract information from assets, fylr needs a "java" command. Install Java and make sure the command `java` starts it: it has to be in the system environment variable PATH, which the Java installation usually takes care of.

### Saxon

This replaces _xsltproc_ since fylr v6.19.

Download **SaxonJ-HE 12.5** from [https://www.saxonica.com/download/java.xml](https://www.saxonica.com/download/java.xml) and unpack it, here to `C:\fylr\utils\saxon\saxon-he-12.5.jar`. Configure it in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        saxon:
          prog: java
          args:
            - "-jar"
            - "C:\\fylr\\utils\\saxon\\saxon-he-12.5.jar"
```

### Ghostscript

From 6.35 fylr renders EPS, AI and PS with Ghostscript itself and calls it as `gs`.

Download `Ghostscript 10.05.0 for Windows (64 bit)` (tested version) from [https://ghostscript.com/releases/gsdnld.html](https://ghostscript.com/releases/gsdnld.html) and install it, here to `C:\Program Files\gs\gs10.05.0`. The installer adds the `bin` directory to the system `%PATH%`.

Copy `gswin64c.exe` to `gs.exe`, so that fylr and other programs find it in the `%PATH%`:

```
PS C:\Program Files\gs\gs10.05.0\bin> dir
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----    Mi, 12.03.2025     13:58          93696 gs.exe
-a----    Mi, 12.03.2025     13:58          93696 gswin64c.exe
```

Instead of the copy, the program can be named in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        gs:
          prog: "C:\\Program Files\\gs\\gs10.05.0\\bin\\gswin64c.exe"
```

A command declared there whose program is missing keeps fylr from starting, so add it once Ghostscript is installed.

Up to fylr 6.34, `.eps` previews went through `ps2pdf` and [Inkscape](windows.md#inkscape), which also needed `C:\Program Files\gs\gs10.05.0\lib` in the system path.

### Libreoffice

Install LibreOffice ([https://de.libreoffice.org/donate/dl/win-x86\_64/24.8.4/de/LibreOffice\_24.8.4\_Win\_x86-64.msi](https://de.libreoffice.org/donate/dl/win-x86_64/24.8.4/de/LibreOffice_24.8.4_Win_x86-64.msi)) and configure it in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        soffice:
          prog: "C:\\Program Files\\LibreOffice\\program\\soffice.exe"
```

The portable version works as well (tested with `LibreOfficePortable_7.4.5_MultilingualStandard.paf.exe` from [https://www.libreoffice.org/download/portable-versions/](https://www.libreoffice.org/download/portable-versions/), installed to `C:\LibreOfficePortable`); configure the path to its `soffice.exe` in `fylr.yml`.

Fair warning: If you make your installation path too long, LibreOffice will not work. Too long, for example: `C:\Users\Jane Doe\Desktop\pf\fylr_v6.2.4_windows_amd64\utils\LibreOfficePortable\`.

### Inkscape

Install Inkscape 1.4 with its default installer. From 6.35 fylr uses it for SVG and WMF, and [Ghostscript](windows.md#ghostscript) for the PostScript family; up to 6.34, version 1.4 was needed for `.eps` previews via `ps2pdf` and Inkscape.

Add Inkscape's `bin` directory to the Windows system `%PATH%`:

1. In the Windows Start Menu, type `env`, then select `Edit the system environment variables`.
2. Click the `Environment Variables...` button.
3. In the lower section titled `System variables`, select the line starting with `Path`.
4. Click `Edit...`.
5. In the new window, click `New` and paste `C:\Program Files\Inkscape\bin`.
6. Click `OK`.
7. Close and open a new window for `fylr.exe`, so that the window, and with it fylr, knows the new `%PATH%`.

To test the integration, upload an SVG file into fylr and check that a preview is generated.

### tika

Download the newest tika-app jar file (tested with `tika-app-3.3.1.jar`) from [https://tika.apache.org/download.html](https://tika.apache.org/download.html) and configure it in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        tika:
          prog: java
          args:
            - "-jar"
            - "C:\\fylr\\utils\\tika-app-3.3.1.jar"
```

### tesseract

From [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki) download and start the installer (tested with `tesseract-ocr-w64-setup-5.5.0.20241111.exe`, 64 bit):

* In the installer dialogs, choose all languages and script data.
* Install to `C:\fylr\utils\tesseract`.
* Configure it in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        tesseract:
          prog: "C:\\fylr\\utils\\tesseract\\tesseract.exe"
```

### mupdf tools

Download the Windows build (tested with `mupdf-1.25.2-windows.zip`) from [https://mupdf.com/releases](https://mupdf.com/releases), unpack it into `C:\fylr\utils\mupdf\` and configure it in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        mutool:
          prog: "C:\\fylr\\utils\\mupdf\\mutool.exe"
```

mutool must be built with ICC color management, or CMYK PDFs render with oversaturated colors. A build without it prints `warning: ICC support is not available` when it renders a PDF:

```
C:\fylr\utils\mupdf> .\mutool.exe draw -o check.png any.pdf
```

### dot

from [https://www.graphviz.org/download/](https://www.graphviz.org/download/)

### calibre

from [https://calibre-ebook.com/download\_windows](https://calibre-ebook.com/download_windows)

### libvips

Optional but recommended. fylr requires libvips 8.16 or newer.

On [https://www.libvips.org](https://www.libvips.org/), follow `Download` and `Windows binaries` and download the newest `vips-dev-w64-all-`X.Y.Z`.zip` (tested with [vips-dev-w64-all-8.18.3.zip](https://github.com/libvips/build-win64-mxe/releases/download/v8.18.3/vips-dev-w64-all-8.18.3.zip)). Use the `all` variant — it includes the loaders (e.g. HEIF) that fylr benefits from.

Unpack it, here to `C:\fylr\utils\vips-dev-8.18`, and configure it in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        vips:
          prog: "C:\\fylr\\utils\\vips-dev-8.18\\bin\\vips.exe"
```

### chrome

**Optional**. Needed only to render PDFs — the **PDF Creator** plugin (`pdf-creator`), installed from the plugin manager. The Linux distribution brings its own Chromium; under Windows you supply the browser.

* Install the browser **Chrome**
* configure the location of chrome in `fylr.yml`:

```
fylr+:
  env:
    SERVER_PDF_CHROME: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
```

{% hint style="info" %}
Up to fylr 6.34 the Windows `fylr.yml` installed the **PDF Server** (`server-pdf`) for this, and it did the rendering. PDF Creator renders the PDF itself from version 1.1.0, so 6.35 no longer installs `server-pdf` — and switches it off where both are enabled, because the two declare the same custom events. See [PDF Creator and the PDF Server](../../plugins/disk-to-url-migration.md#pdf-creator-and-the-pdf-server).
{% endhint %}

## Configure the tools in fylr.yml

All tools together in `fylr.yml`:

* _**before**_, the tools in `fylr.yml` look like this (minimal, no 3rd party tools):

```
fylr+:
  [...]
  services+:
  [...]
    execserver+:

      commands:
        fylr:
          prog: fylr.exe
      
```

* _**after**_ adding the tools (use the paths valid on _your_ installation):

```
fylr+:
  env:
    SERVER_PDF_CHROME: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
  [...]
  services+:
  [...]
    execserver+:
      commands:
        fylr:
          prog: fylr.exe
        # ffmpegthumbnailer: not under Windows. ffmpeg is used instead as a fallback
        soffice:
          prog: "C:\\Program Files\\LibreOffice\\program\\soffice.exe"
        magick:
          prog: "C:\\fylr\\utils\\magick.exe"
        vips:
          prog: "C:\\fylr\\utils\\vips-dev-8.18\\bin\\vips.exe"
        exiftool:
          prog: "C:\\fylr\\utils\\exiftool.exe"
        ffmpeg:
          prog: "C:\\fylr\\utils\\ffmpeg.exe"
        ffprobe:
          prog: "C:\\fylr\\utils\\ffprobe.exe"
        node:
          prog: "C:\\fylr\\utils\\node.exe"
        python3:
          #prog: "C:\\fylr\\utils\\python3\\python.exe"
          # is searched in PATH variable:
          prog: "python.exe"
        pdfinfo:
          prog: "C:\\fylr\\utils\\poppler-pdf\\Library\\bin\\pdfinfo.exe"
        java:
          prog: java.exe
        inkscape:
          prog: inkscape.exe
        saxon:
          prog: java
          args:
            - "-jar"
            - "C:\\fylr\\utils\\saxon\\saxon-he-12.5.jar"
        dot:
          prog: "C:\\fylr\\utils\\Graphviz\\bin\\dot.exe"
        tika:
          prog: java
          args:
            - "-jar"
            - "C:\\fylr\\utils\\tika-app-3.3.1.jar"
        tesseract:
          prog: "C:\\fylr\\utils\\tesseract\\tesseract.exe"
        mutool:
          prog: "C:\\fylr\\utils\\mupdf\\mutool.exe"
        ebook-meta:
          prog: "C:\\fylr\\utils\\Calibre2\\ebook-meta.exe"
        ebook-convert:
          prog: "C:\\fylr\\utils\\Calibre2\\ebook-convert.exe"
```

Check that each indentation level is **two** spaces. (No tab characters, just space characters).

***

## Start fylr as a service

After testing, you may want to switch to

```
fylr.exe server -c fylr.yml --service install
```
