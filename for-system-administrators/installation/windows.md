# Windows

Running fylr.exe

## Download fylr.exe

* Go to the newest release in [https://docs.fylr.io/releases](https://docs.fylr.io/releases)
* Download `fylr_v6.`X.Y`_windows_amd64.zip` and unpack.

It contains:

* `fylr.exe` fylr native for Windows amd64
* `fylr.yml` a starting configuration already adjusted with Windows path syntax and for the following instructions.
* `fylr.example.yml` most configuration parameters. Look here for reference.
* `fylr.default.yml` compiled-in default values.
* `LICENSE` legal information on who may use fylr.
* `utils/` some tools for asset processing. (More need to be downloaded, see below)
* `webfrontend/` The static webfrontend files.
* `resources/` more files for fylr, e.g. translations.

## Windows path length

The shorter the path of your fylr installation directory, the less likely your installation will fail processing files due to exceeding the [length limit](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry). So prefer `C:\fylr` over `C:\user\adam doe\Desktop\software-project\fylr-v6.4.0\unpacked`. Fylr newer than v6.3.1 will try to use only short internal file names, but every little bit helps. Same for Libre Office installation (more about that below).

## Get the dependencies

Bare bone minimum: Elasticsearch

### Elasticsearch

What we tested:

* Download from [https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html)
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

With default settings, 11,7 GB free RAM _was_ enough. Tweaking java settings, even only 2 or 3 GB for Java _should_ be enough.

### Start with minimal dependencies

You are now ready to start fylr, although most asset processing tools are still missing: (no previews)

```
.\fylr.exe server
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

### Postgresql

* We installed 15.2 from [https://www.enterprisedb.com/downloads/postgres-postgresql-downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
* We started pgadmin and created a role "fylr" (with LOGIN and INHERIT, the defaults), with password "fylr"; and a database "fylr" owned by role "flyr".
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

* Stop fylr.exe and elasticsearch. Optionally check that java / openjdk is stopped alongside elasticsearch.
* Remove the directory `data` and elasticsearch's data/\*
* Start elasticsearch as shown at the beginnig.
* If you use postgres, remove and recreate the database.

### Magick.exe and convert.exe and composite.exe

* We downloaded `ImageMagick-7.1.0-61-portable-Q16-HDRI-x64.zip` from [https://imagemagick.org/script/download.php#windows](https://imagemagick.org/script/download.php#windows)
* We put the three mentioned tools from the download into the utils directory which is parallel to fylr.exe

Hint from the [download page](https://imagemagick.org/script/download.php#windows):

> If you have any problems, you likely need vcomp120.dll. To install it, download Visual C++ Redistributable Package(https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads).

### Exiftool.exe

We downloaded: Windows Executable: exiftool-12.56.zip on [http://exiftool.sourceforge.net](http://exiftool.sourceforge.net)

We have put exiftool(-k).exe from the download into the utils directory

We renamed it to exiftool.exe as recommended on exiftool.sourceforge.net.

### Ffmpeg.exe and ffprobe.exe

We downloaded ffmpeg-n5.1.2-12-g7268323193-win64-gpl-5.1.zip from [https://github.com/BtbN/FFmpeg-Builds/releases](https://github.com/BtbN/FFmpeg-Builds/releases)

We suggest you avoid the LGPL version as testing showed it has less features (x264 and x265).

We have put ffmpeg.exe and ffprobe.exe into the utils directory.

In fylr.yml we configured it as now visible in the comments there.

### Un-commenting in fylr.yml

Now was a good time to go through fylr.yml and turn a whole range of comments into non-comments:

* blocks mentioning all the above tools (magick.exe, ...)
* blocks mentioning fylr\_metadata.exe, fylr\_pdf2pages.exe, fylr\_iiif.exe. They are included in the zip file you unpacked earlier, but had to be comments until now because they depended on 3rd party tools not included in fylr...zip.
* An example of such a block: Original state:

```
#         pdf2pages:
#           waitgroup: a
#           commands:
#             fylr_pdf2pages:
#               env:
#                 - FYLR_CMD_FYLR_METADATA=.\\fylr_metadata.exe
#                 - FYLR_CMD_MAGICK=.\\magick.exe
#                 - FYLR_CMD_EXIFTOOL=.\\exiftool.exe
#               prog: "utils\\fylr_pdf2pages.exe"
#             fylr_metadata:
#               env:
#                 - FYLR_CMD_EXIFTOOL=.\\exiftool.exe
#               prog: "utils\\fylr_metadata.exe"
```

* advised state to integrate the mentioned 3rd party tool:

```
        pdf2pages:
          waitgroup: a
          commands:
            fylr_pdf2pages:
              env:
                - FYLR_CMD_FYLR_METADATA=.\\fylr_metadata.exe
                - FYLR_CMD_MAGICK=.\\magick.exe
                - FYLR_CMD_EXIFTOOL=.\\exiftool.exe
              prog: "utils\\fylr_pdf2pages.exe"
            fylr_metadata:
              env:
                - FYLR_CMD_EXIFTOOL=.\\exiftool.exe
              prog: "utils\\fylr_metadata.exe"
```

Lines are made comments by adding `#` in front of the line, so remove the hash AND one space to use commented lines as config. Check that each indentation level is two spaces. (No tab characters, just space characters)

### Node

We downloaded node-v16.17.0-win-x64.7z from [https://nodejs.org/dist/v16.17.0/](https://nodejs.org/dist/v16.17.0/)

We put just node.exe into the utils folder parallel to fylr.exe.

In fylr.yml we configured it by converting the comment block mentioning node.exe into non-comments.

### Python

We donwloaded "Windows embeddable package (64-bit)" at [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) (explained [here](https://docs.python.org/3/using/windows.html#windows-embeddable))

We unpacked the whole package as the folder "python3" inside the utils folder.

In fylr.yml we configured it by converting the comment block mentioning python.exe into non-comments.

### Java

For extracting text from pdfs in the fylr\_example plugin and for the API test suite, the "metadata" service in fylr.yml needs a "java" command.

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

We "installed" `LibreOfficePortable_7.4.5_MultilingualStandard.paf.exe` from [https://www.libreoffice.org/download/portable-versions/](https://www.libreoffice.org/download/portable-versions/) so that `LibreOfficePortable.exe` was in `C:\LibreOfficePortable`.

Fair warning: If you make your installation path too long, libre office will not work.

Example for too long: `C:\Users\Klaus Thorn\Desktop\pf\fylr_v6.2.4_windows_amd64\utils\LibreOfficePortable\`.

### Inkscape

We installed Inkscape 1.2 via its default Installer.

We added Inkscape's `bin` directory to the Windows System PATH as in [https://de.mathworks.com/matlabcentral/answers/94933-how-do-i-edit-my-system-path-in-windows#answer\_104285](https://de.mathworks.com/matlabcentral/answers/94933-how-do-i-edit-my-system-path-in-windows#answer\_104285)

We closed and opened a new window for `fylr.exe server` so that the new PATH is knwon to the window.

We tested Inkscape integration by uploading a svg file into fylr and check whether a preview is generated.



## Start fylr as a service

After testing, you may want to switch to

```
fylr.exe server --service install
```
