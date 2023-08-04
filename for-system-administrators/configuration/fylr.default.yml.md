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
  db:
    driver: sqlite3
    dsn: "fylr.db"
    maxIdleConns: 10
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
    maxMem: 100mb
    addresses:
      - "http://localhost:9200"

  execserver:
    addresses:
      - http://localhost:8083/?pretty=true
    parallel: 4
    parallelHigh: 2
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
      addr: ":80"
      path: easydb-webfrontend/build
      oauth2:
        clientID: fylr-web-frontend
        internalURL: http://localhost:8080
      reverseProxy:
        api: "http://localhost:8080"
        backend: "http://localhost:8081"
    execserver:
      addr: :8083
      jobRemovalPolicy: "done"
      janitorFileAge: "24h"
      waitgroups:
        a:
          processes: 4
        b:
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
        pdftotext:
          prog: pdftotext
        magick:
          prog: magick
        ffprobe:
          prog: ffprobe
        ffmpegthumbnailer:
          prog: ffmpegthumbnailer
        node:
          prog: node
        python3:
          prog: python3
        xsltproc:
          prog: xsltproc
        # used by fylr-plugin-example (Tesseract)
        java:
          prog: java

      services:
        # this service allows to execute arbitrary binaries
        exec:
          waitgroup: a
        # plugin support
        node:
          waitgroup: a
        python3:
          waitgroup: b
        xslt:
          waitgroup: a
        # file conversion support
        convert:
          waitgroup: a
        ffmpeg:
          waitgroup: a
        inkscape:
          waitgroup: a
        soffice:
          waitgroup: a
        pdf2pages:
          waitgroup: a
        iiif:
          waitgroup: b
        metadata:
          waitgroup: a
```
{% endcode %}

