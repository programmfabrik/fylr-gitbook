---
description: >-
  In this section you find the default settings, used if you start fylr.yml with fylr+:
---

# fylr.yml
{% code title="fylr.yml" lineNumbers="true" %}
```yaml
# The default fylr yml is used if the config file "" is requested.
# It's built into the fylr binary.
fylr:
  name: "fylr"
  externalURL: "http://localhost"

  logger:
    format: "console"
    level: "info"
    timeFormat: "2006-01-02 15:04:05Z07"
  db:
    driver: sqlite3
    dsn: "fylr.db"
    maxIdleConns: 10
    maxOpenConns: 90
    init:
      config:
        system:
          config:
            # purge:
            #   allow_purge: true
            #   purge_storage: true
            location_defaults:
              originals: file
              versions: file
              backups: file
      locations:
        file:
          kind: file
          # allow_purge: true
          # allow_redirect: false
          config:
            file:
              dir: "files"

  elastic:
    parallel: 4
    objectsPerJob: 100
    metadataFulltextLimit: 1mb
    maxMem: 100mb
    maxHeapAlloc: 1g
    addresses:
      - "http://localhost:9200"

  execserver:
    addresses:
      - http://localhost:8083/?pretty=true
    parallel: 18
    parallelHigh: 10
    pluginJobTimeoutSec: 2400
    connectTimeoutSec: 120
    callbackBackendInternalURL: "http://localhost:8081"
    callbackApiInternalURL: "http://localhost:8080"

  services:
    api:
      addr: :8080
      oauth2Server:
        clients:
          fylr-web-frontend:
            public: true
            scopes:
              - "read"
              - "write"
              - "offline"
          fylr-mobile-app:
            public: true
            redirectURIs:
              - "fylr.app.scheme:///"
            scopes:
              - "read"
              - "write"
              - "offline"
          ci-hub:
            public: true
            redirectURIs:
              - "https://live.ci-hub.com/api/v1/auth/login/fylr"
              - "https://dev.ci-hub.com/api/v1/auth/login/fylr"
              - "https://stage.ci-hub.com/api/v1/auth/login/fylr"
              - "https://ci-hub.net/api/v1/auth/login/fylr"
              - "https://api.ci-hub.com/auth/login/fylr"
              - "https://identity.ci-hub.com/auth/login/fylr"
              - "https://ci-hub.azurewebsites.net/api/v1/auth/login/fylr"
              - "https://ci-hub-beta.azurewebsites.net/api/v1/auth/login/fylr"
              - "https://ci-hub-test.azurewebsites.net/api/v1/auth/login/fylr"
              - "http://localhost:8080/api/v1/auth/login/fylr"
            scopes:
              - "read"
              - "write"
              - "offline"
          santa-cruz:
            public: true
            redirectURIs:
              - "https://fylr.linkrui.com/oauth"
              - "https://stage-fylr.linkrui.com/oauth"
            scopes:
              - "read"
              - "write"
              - "offline"
    backend:
      addr: :8081
    webapp:
      addr: :80
      # path: easydb-webfrontend/build
      oauth2:
        clientID: fylr-web-frontend
        internalURL: http://localhost:8080
      reverseProxy:
        api: "bind"
        backend: "http://localhost:8081"
    execserver:
      addr: :8083
      jobRemovalPolicy: "done"
      janitorFileAge: "24h"
      waitgroups:
        # video / office conversion
        slow:
          processes: 2
        # convert / image
        medium:
          processes: 6
        # plugins / metadata etc.
        fast:
          processes: 10

      # common environment to be used for all program exec
      env:
        - FYLR_METADATA_BLURHASH=10M

      commands:
        fylr:
          prog: fylr
        exiftool:
          prog: exiftool
        ffmpeg:
          prog: ffmpeg
        inkscape:
          prog: inkscape
        soffice:
          prog: soffice
        ebook-convert:
          prog: ebook-convert
        ebook-meta:
          prog: ebook-meta
        pdftotext:
          prog: pdftotext
        mutool:
          prog: mutool
        tika:
          prog: tika
        tesseract:
          prog: tesseract
        saxon:
          prog: saxon
        magick:
          prog: magick
        ffprobe:
          prog: ffprobe
        ffmpegthumbnailer:
          prog: ffmpegthumbnailer
        node:
          prog: node
        dot:
          prog: dot
        python3:
          prog: python3
        # used by fylr-plugin-example (Tesseract)
        java:
          prog: java

      services:
        # this service allows to execute arbitrary binaries
        exec:
          waitgroup: fast
        # plugin support
        node:
          waitgroup: fast
        python3:
          waitgroup: fast
        xslt:
          waitgroup: fast
        # file conversion support, also used by video thumbmnail which
        # is calling "fylr convert" which then calls ffmpeg
        convert:
          waitgroup: medium
        ffmpeg:
          waitgroup: slow
        inkscape:
          waitgroup: slow
        soffice:
          waitgroup: slow
        pdf2pages:
          waitgroup: slow
        iiif:
          waitgroup: fast
        dot:
          waitgroup: fast
        metadata:
          waitgroup: fast
```
{% endcode %}
