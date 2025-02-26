# Windows

Running fylr.exe

## Download fylr.exe

* Go to the newest release in [https://docs.fylr.io/releases](https://docs.fylr.io/releases)
* Download `fylr_v6.`X.Y`_windows_amd64.zip` and unpack.

It contains:

* `fylr.exe` fylr native for Windows amd64.
* `fylr.yml` a starting configuration already adjusted with Windows path syntax and for the following instructions.
* `fylr.example.yml` most configuration parameters. Look here for reference.
* `fylr.default.yml` compiled-in default values. Just as a copy for you to look them up.
* `LICENSE` legal information on who may use fylr.
* A folder with plugins.

## Windows path length

The shorter the path of your fylr installation directory, the less likely your installation will fail processing files due to exceeding the [length limit](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry). So prefer `C:\fylr` over `C:\user\adam doe\Desktop\software-project\fylr-v6.17.0\unpacked`. Fylr newer than v6.3.1 will try to use only short internal file names, but every little bit helps. Same for Libre Office installation (more about that below).

## Get the dependencies

Bare bone minimum: Elasticsearch or OpenSearch

### OpenSearch

OpenSearch is our default and recommendation.

We installed OpenSearch as described in [https://opensearch.org/docs/latest/install-and-configure/install-opensearch/windows/](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/windows/)

* Version 2.11 (Version 2.12.0 works from fylr v6.9.0 onwards, make sure you set a strong initial password for admin, the OpenSearch user)
* We disabled security and let it explicitly listen only on localhost, thus protecting it:

```
network.host: 127.0.0.1
plugins.security.disabled: true
```

* We installed the one needed plugin:

```
opensearch-2.11.0> .\bin\opensearch-plugin install analysis-icu
```

### Elasticsearch

Elasticsearch has been the default until 2023. Now we recommend OpenSearch instead.

What we tested:

* Download from [https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html)
* We recommend Elasticsearch `7.17`.
* If you start a new instance or have problems with ElasticSearch, we recommend OpenSearch, see above.
* Since writing the next lines, we found a <mark style="background-color:red;">problem</mark> with Versions `8.5` and newer, about indexing letters _Q_ and _W_, of all things. Thus our recommendation for Elasticsearch `7.17`. The remainder of the text still mentions `8.6.1`, to stay true to what we actually did under Windows.
*   Unpack official windows release file elasticsearch-8.6.1-windows-x86\_64.zip

    Other Versions should also be fine. This is true for all the below mentioned tools.
* Disable security with ...

```
xpack.security.enabled: false
```

... in elasticsearch-8.6.1\config\elasticsearch.yml

* Got the analysis-icu plugin from [https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html) for offline installation (it was https://artifacts.elastic.co/downloads/elasticsearch-plugins/analysis-icu/analysis-icu-8.6.1.zip)
* Unpacked into `elasticsearch-8.6.1\plugins\analysis-icu\` (no further subfolders).
* Start, for example in a Windows powershell:

```
.\elasticsearch-8.6.1\bin\elasticsearch.bat
```

Elasticsearch then used the default address `http://localhost:9200`, which is also configured in `fylr.yml`.

### Start fylr with minimal dependencies

Edit fylr.yml to not use any 3rd part tools for the moment if you want to test/start with minimal effort:

```
 fylr+:
  [...]
  services+:
  [...]
    execserver+:

      commands:
        fylr:
          prog: fylr.exe
      services:
```

You are now ready to start fylr, although most asset processing tools are still missing: (no previews)

```
.\fylr.exe server -c fylr.yml
```

... in the folder where fylr.exe is.

Output lines with `WRN` can usually be ignored.

Harmless Errors known to appear are e.g.

* `Error occurred in NewIntrospectionRequest` and `Accepting token failed`, when a browser tries to use old credentials.

#### Access the web frontend

Browse [http://localhost](http://localhost)

Default login credentials are:

* **Username**: _root_
* **Password**: _admin_

### More than bare bone minimum

For a full installation it is recommended to install all of the following and un-comment them in `fylr.yml`.

"Un-comment" = turning the comments into configuration.

### PostgreSQL

* We installed 15.2 from [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
* We started pgadmin and created a role "fylr" (with LOGIN and INHERIT, the defaults), with password "fylr"; and a database "fylr" owned by role "fylr".
* We un-commented these lines in fylr.yml:

```
    driver: postgres
    dsn: "host=localhost port=5432 user=fylr password=fylr dbname=fylr sslmode=disable"
```

* And we disabled the lines configuring sqlite, by turning them into comments:

```
    #driver: sqlite3
    #dsn: "data\\sqlite.db"
```

* For a consistent state we also did the next step: cleanup.

#### cleanup

If you want to go back to a fresh state between two test runs:

* Stop fylr.exe and the indexer (opensearch or elasticsearch). Optionally check that java / openjdk is stopped alongside elasticsearch.
* Remove the directory `data` and elasticsearch's `data/*` .
* Start elasticsearch as shown at the beginning.
* If you use PostgreSQL, remove and recreate the database.

### pdf tools

* We downloaded [Release-23.08.0-0.zip](https://github.com/oschwartz10612/poppler-windows/releases/download/v23.08.0-0/Release-23.08.0-0.zip) from [https://github.com/oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases/tag/v23.08.0-0) (_not_ xpdf-tools from https://www.xpdfreader.com)
* We unpacked its contents and configured the path to pdftotext.exe, pdftoppm.exe and pdfinfo.exe in fylr.yml. Alternatively, we tested successfully to add the containing directory of those tools to the PATH.

### magick.exe and convert.exe and composite.exe

* We downloaded `ImageMagick-7.1.0-61-portable-Q16-HDRI-x64.zip` from [https://imagemagick.org/script/download.php#windows](https://imagemagick.org/script/download.php#windows)
* We put the three mentioned tools from the download into `C:\fylr\utils`.

Hint from the [download page](https://imagemagick.org/script/download.php#windows):

> If you have any problems, you likely need vcomp120.dll. To install it, download Visual C++ Redistributable Package(https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads).

### Exiftool.exe

We downloaded: Windows Executable: exiftool-12.56.zip on [http://exiftool.sourceforge.net](http://exiftool.sourceforge.net)

We have put exiftool(-k).exe from the download into `C:\fylr\utils`.

We renamed it to exiftool.exe as recommended on exiftool.sourceforge.net.

### Ffmpeg.exe and ffprobe.exe

We downloaded ffmpeg-n5.1.2-12-g7268323193-win64-gpl-5.1.zip from [https://github.com/BtbN/FFmpeg-Builds/releases](https://github.com/BtbN/FFmpeg-Builds/releases)

We suggest you avoid the LGPL version as testing showed it has less features (x264 and x265).

We have put ffmpeg.exe and ffprobe.exe into `C:\fylr\utils`.

### Node

We downloaded node-v16.17.0-win-x64.7z from [https://nodejs.org/dist/v16.17.0/](https://nodejs.org/dist/v16.17.0/)

We put just node.exe into `C:\fylr\utils`.

### Python

We donwloaded "Windows embeddable package (64-bit)" at [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) (explained [here](https://docs.python.org/3/using/windows.html#windows-embeddable))

We unpacked the whole package as the folder "python3" inside `C:\fylr\utils`.

### Java

For extracting information from assets, fylr needs a "java" command. We made sure to have java installed and that it can be started by the command `java` (for that, it has to be in the system environment variable PATH, which already was the case after java installation).

### Xsltproc

We installed xsltproc.exe by

* installling the chocolatey package manager as in [https://docs.chocolatey.org/en-us/choco/setup](https://docs.chocolatey.org/en-us/choco/setup)
* installing xsltproc with chocolatey as in [https://community.chocolatey.org/packages/xsltproc#install](https://community.chocolatey.org/packages/xsltproc#install)
* test that xsltproc is running:

```
xsltproc.exe --version
Using libxml 20903, libxslt 10128 and libexslt 817
```

### Ghostscript

We downloaded `Ghostscript 10.0.0 for Windows (64 bit)` from [https://ghostscript.com/releases/gsdnld.html](https://ghostscript.com/releases/gsdnld.html)

We used its default installation (`C:\Program Files (x86)\gs\gs10.00.0` or `C:\Program Files\gs\gs10.00.0`)

```
-a----         9/21/2022   3:09 PM          86528 gs.exe
-a----         9/21/2022   3:09 PM          86528 gswin32c.exe
```

We then copied `gswin32c.exe` to `gs.exe` so that `convert.exe` is able to find it in %PATH%.

We tested ghostscript integration by uploading a pdf file into fylr and checking whether a preview is generated (showing the first page of the pdf).

### Libreoffice

We installed LibreOffice ([ https://de.libreoffice.org/donate/dl/win-x86\_64/24.8.4/de/LibreOffice\_24.8.4\_Win\_x86-64.msi](https://de.libreoffice.org/donate/dl/win-x86_64/24.8.4/de/LibreOffice_24.8.4_Win_x86-64.msi))

and configured in fylr.yml:

```
fylr+:
  services+:
    execserver+:
      commands:
        soffice:
          prog: "C:\\Program Files\\LibreOffice\\program\\soffice.exe"
```

\
As an alternative we successfully tested `LibreOfficePortable_7.4.5_MultilingualStandard.paf.exe` from [https://www.libreoffice.org/download/portable-versions/](https://www.libreoffice.org/download/portable-versions/) to `C:\LibreOfficePortable`.

Fair warning: If you make your installation path too long, libre office will not work.

Example for too long: `C:\Users\Klaus Thorn\Desktop\pf\fylr_v6.2.4_windows_amd64\utils\LibreOfficePortable\`.

We then configured the path to `soffice.exe` in `fylr.yml`.

### Inkscape

We installed Inkscape 1.2 via its default Installer.

We added Inkscape's `bin` directory to the Windows System PATH as in [https://de.mathworks.com/matlabcentral/answers/94933-how-do-i-edit-my-system-path-in-windows#answer\_104285](https://de.mathworks.com/matlabcentral/answers/94933-how-do-i-edit-my-system-path-in-windows#answer_104285)

We closed and opened a new window for `fylr.exe server` so that the new PATH is known to the window.

We tested Inkscape integration by uploading a svg file into fylr and check whether a preview is generated.

### tika

We downloaded from [https://tika.apache.org/download.html](https://tika.apache.org/download.html) the jar file `tika-app-2.9.2.jar`.

We configured in fylr.yml:

```
fylr+:
  services+:
    execserver+:
      commands:
        tika:
          prog: java
          args:
            - "-jar"
            - "C:\\fylr\\utils\\tika-app-2.9.2.jar"
```

### tesseract

From [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki) we downloaded and started the installer `tesseract-ocr-w64-setup-5.5.0.20241111.exe` (64 bit)

* In the installer dialogs we chose all languages and script data
* We installed to `C:\fylr\utils\tesseract`
* We configured in `fylr.yml`:

```
fylr+:
  services+:
    execserver+:
      commands:
        tesseract:
          prog: "C:\\fylr\\utils\\tesseract\\tesseract.exe"
```

### mupdf tools

We downloaded `mupdf-1.25.2-windows.zip` from [https://mupdf.com/releases](https://mupdf.com/releases) and unpacked it into `C:\fylr\utils\mupdf\` .

In `fylr.yml we` configured:

```
fylr+:
  services+:
    execserver+:
      commands:
        mutool:
          prog: "C:\\fylr\\utils\\mupdf\\mutool.exe"
```

### dot

from [https://www.graphviz.org/download/](https://www.graphviz.org/download/)

### calibre

from [https://calibre-ebook.com/download\_windows](https://calibre-ebook.com/download_windows)

## Tools in fylr.yml

Now was a good time to go to the last part in fylr.yml and replace minimal 3rd party tools config into explicit tools config:

* before:

```
fylr+:
  [...]
  services+:
  [...]
    execserver+:

      commands:
        fylr:
          prog: fylr.exe
      services:
      
```

* after:

<pre><code><strong>fylr+:
</strong><strong>  [...]
</strong><strong>  services+:
</strong><strong>  [...]
</strong>    execserver+:
      commands:
        fylr:
          prog: fylr.exe
        # ffmpegthumbnailer: not under Windows. ffmpeg is used instead as a fallback
        soffice:
          prog: "C:\\LibreOfficePortable\\LibreOfficePortable.exe"
        magick:
          prog: "C:\\fylr\\utils\\magick.exe"
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
        pdftotext:
          prog: "C:\\fylr\\utils\\poppler-pdf\\Library\\bin\\pdftotext.exe"
<strong>        pdfinfo:
</strong>          prog: "C:\\fylr\\utils\\poppler-pdf\\Library\\bin\\pdfinfo.exe"
        java:
          prog: java.exe
        inkscape:
          prog: inkscape.exe
        xsltproc:
          prog: "C:\\ProgramData\\chocolatey\\bin\\xsltproc.exe"
        dot:
          prog: "C:\\fylr\\utils\\Graphviz\\bin\\dot.exe"
        tika:
          prog: java
          args:
            - "-jar"
            - "C:\\fylr\\utils\\tika-app-2.9.2.jar"
        tesseract:
          prog: "C:\\fylr\\utils\\tesseract\\tesseract.exe"
        mutool:
          prog: "C:\\fylr\\utils\\mupdf\\mutool.exe"
        ebook-meta:
          prog: "C:\\fylr\\utils\\Calibre2\\ebook-meta.exe"
        ebook-convert:
          prog: "C:\\fylr\\utils\\Calibre2\\ebook-convert.exe"
</code></pre>

Check that each indentation level is two spaces. (No tab characters, just space characters).

***

## Start fylr as a service

After testing, you may want to switch to

```
fylr.exe server -c fylr.yml --service install
```
