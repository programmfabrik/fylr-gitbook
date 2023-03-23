---
description: >-
  In this section you find most settings possible in fylr.yml and explanations as comments
---

# fylr.yml
{% code title="fylr.yml" lineNumbers="true" %}
```yaml
## - Some of the regexs to check for versions might require modifications
## - All relative paths described in the file are relative to cmd/fylr unless otherwise
##    stated
## - All ports described in the file are formatted to work with Golang net/http package
##
## Multiple config files can be parsed (use -c ... -c ... -c ...).
##   The following rules apply:
##   - For maps the whole map is replaced, unless the key which holds the map
##     ends ins a plus. If it ends in a minus, values are removed from a map.
##   - For slices the whole slice is replace. If the key ends in a +, values are
##     are appended, if it ends in a "-" values are removed. If it ends in "<",
##     values are prepended.
##   - Other values are overwritten
##
## To set the externalURL and the sqlite database name in a minimum fylr.yml one could do:
##
## ---fylr.yml---
##   fylr+
##     externalURL: "http://localhost"
##     db+:
##       dsn: mysqlite.db
## --------------
##
## The "+" on the top level and for "db" is needed to tell fylr to merge the map
## rather than overwriting it. If the .yml uses "fylr" instead (no "+") the
## default config will be replaced.
##
## Environemnt allows to overwrite the fylr.yml All variables are read in
## upper-case. For the path to deeper variables, use "_" as separator. Supported
## types: string, []string. To fill []string, use a JSON array.
##
## Example: FYLR_DB_DSN="host=localhost port=5432 user=fylr dbname=test"
## FYLR_DB_DRIVER="postgres"
##
## Use --env-prefix on the command line to overwrite the FYLR_ default

# All config is below "fylr"
fylr:

  # name of the instance (mandatory). Its used as prefix for the bucket
  # names and elastic indexes. The name must match regexp [a-z][a-z0-9\-_]*[a-z0-9].
  # So, all small letters, start with a letter, followed by small letter, a number, dash or
  # underscores, ending in letter or number. Must be between 3 and 32 bytes.
  name: "myfylr"

  # public external url of the server. This url needs to be fully qualified
  externalURL: "http://localhost"

  # encryptionKey is used to AES-encrypt sensitive information before writing it
  # to the database. It must be 32 bytes long. Default is empty.
  encryptionKey: ""

  # for development only
  debug:
    # skip term creation
    skipTerms: false
    # don't announce plugins bundle on /api/plugin
    noPluginsBundle: false
    # simulate local status
    localStatus: "" # purge, reindex, startup, ready
    # this setting skips the sometime expensive permission check
    # on the /api/eas/download endpoint. However, there is still
    # some security left, the link is checked against a valid hash
    # of the file which needs to be provided.
    easDownloadSkipCheckRights: false


  # tempDir is used by api/system/backup and the export to during a TAR
  # production. With no tempDir given the system defaults temp dir is used. This
  # tempDir gets not cleaned up automatically by FYLR.
  tempDir: _tmp_workdir

  # Settings for the "logger" (we use https://github.com/rs/zerolog)
  logger:
    # Set to "json" or "console". Default: "console"
    format: "console"
    # Set zerolog log level: trace, debug, info, warn, error, fatal, panic
    # default to "info".
    level: "info"
    # timeFormat is the Go representation to format the time in the log output.
    # zerolog's time keeping resolution is always set to milliseconds by FYLR.
    # Use "", "UNIXMS" or "UNIXMICRO" to output a unix timestamp (json format only).
    # Defaults to ""
    timeFormat: ""
    # turn off color for zerolog's underlying ConsoleWriter
    # format: "console" only.
    noColor: false
    # add hostname to log output
    addHostname: false

  # data is stored in a database, FYLR supports sqlite & postgres
  db:
    # driver: sqlite3
    # dsn: "../../_data/sqlite/fylr.db"
    driver: postgres
    # specify a PostgreSQL user owning the given db (with LOGIN and INHERIT, which are defaults for CREATE USER anyway).
    dsn: "host=localhost port=5432 user=fylr password=fylr dbname=fylr sslmode=disable"
    # https://golang.org/pkg/database/sql/#DB.SetMaxOpenConns, default: 0
    # This has to be at 4 + execserver.parallel + elastic.parallel. Two of these
    # connections will be dedicated to a separate connection pool managing
    # the sequences (Postgres only)
    maxOpenConns: 10
    # https://golang.org/pkg/database/sql/#DB.SetMaxIdleConns, default: 0
    # This has to be not more than maxOpenConns
    maxIdleConns: 0
    # The init block is used to pre-fill the database when its created or purged.
    init:
      # Path to base config file. If set, on a fresh install or after a purge this
      # file is used and preloaded into the base config. The format of the file is
      # JSON in API format. Defaults to "", which starts with an empty base
      # config. The empty base config uses defaults which are defined in
      # resources/baseconfig/baseconfig.yml. Unset keys (from a partial base
      # config file), are set to their defaults.
      configFile: ""

      # Inline base config. Works like configFile but used the inlined
      # baseconfig setting in this .yml file. Runs after configFile, so everything
      # in config overwrites settings from configFile. Default is empty.
      config: null

      # To setup a purgeable system with default storage locations
      # locfile & locs3, configure the following. The location_default map
      # accepts location ids as well as names:
      #
      # config:
      #   system:
      #     config:
      #       purge:
      #         allow_purge: true
      #         purge_storage: true
      #       location_defaults:
      #         originals: locfile
      #         versions: locs3
      #         backups: locfile

      # preconfigure locations for empty databases
      locations:
        # the location's name can be any string which you choose
        #
        # Inside the storage location fylr will create a structure like this:
        #
        # [prefix/]fylr-UUID/originals
        # [prefix/]fylr-UUID/versions
        # [prefix/]fylr-UUID/backups
        #
        # The driver "file" will create directories inside the configured
        # top level directory but never remove them. So, if you use purge
        # a lot, FYLR will leave empty directories on disk.
        locfile:
          # The kind is either "file" or "s3" (see below)
          kind: file
          # Each location can configure a prefix which will
          # be attached before the file to be created
          prefix: "apitest/"
          # Set to true if files in this location can be
          # purged by FYLR (if the purge api call is used)
          allow_purge: true
          # Set to true if that storage location allows its download URLs to be
          # exposed. For the kind "file" storage backend this is a dangerous
          # setting and should be used for development purposes only. Default to
          # false.
          allow_redirect: false
          config:
            file:
              dir: "_files"
        locs3:
          kind: s3
          prefix: "apitest/"
          allow_purge: true
          config:
            s3:
              bucket: apitest
              endpoint: "127.0.0.1:9000"
              accesskey: "minioadmin"
              secretkey: "minioadmin"
              region: "us-east-1"
              ssl: false

  # DEPRECATED, will be removed in next version
  # files are stored in S3. Buckets are created by FYLR automatically
  s3:
    endpoint: "127.0.0.1:9000"
    accessKeyID: "minio"
    secretAccessKey: "minio123"
    bucketLocation: "us-east-1"
    bucketName: fylr-census-dev
    ssl: false
    # allowPurge controls if a purge also purges the storage
    # or not. Defaults to false
    allowPurge: false

  plugin:
    # load plugins at startup. the loader crawls the given directories
    # and loads given files for plugin config files, ending in ".yml".
    # "*" and "?" are allowed as placeholders, unmatched directories or
    # files are silently skipped.
    paths:
      - ../../../easydb-plugins
      - ../../../fylr-plugins/fylr_example
    urls:
      - https://github.com/programmfabrik/fylr-plugin-formula-columns/releases/download/v0.1.2/fylr-plugin-formula-columns.zip
    # defaults is a map setting defaults for the plugin registration.
    # This is configured as map with the plugin name as key.
    defaults:
      # default for fylr_example plugin
      fylr_example:
        # enable, set to false to disable the plugin, defaults to true
        enabled: false
        # update_policy: automatic, always, never, defaults to automatic
        update: "never"

  # set to true to allow /api/settings/purge. dont use on production systems!
  allowpurge: true

  # path to resources, that are all files needed by FLYR during runtime (inspect, pages, etc..)
  # the default path is relative to the FLYR binary, not the current working directory
  resources: ""

  # elastic is the indexer for FYLR
  elastic:
    # logger used for the elastic client
    # "Text": TextLogger prints the log message in plain text.
    # "Color": ColorLogger prints the log message in a terminal-optimized plain text.
    # "Curl": CurlLogger prints the log message as a runnable curl command.
    # "JSON": JSONLogger prints the log message as JSON.
    logger: ""
    # Where to find the Elastic search index settings. If you provide your own
    # file make sure to base it on the default
    # resources/index/index_settings.json which is included in the distribution.
    settings: ""
    # number of parallel workers to index documents, default to 1, set to 0 to disable
    parallel: 1
    # number of objects per job passed to the indexer process
    objectsPerJob: 100
    # limit of payloads sent to Elastic
    maxMem: 100mb
    # fielddata (debug feature). if set to true, fields are mapped including their fielddata
    # in the reverse index. with that, the inspect view of the indexed version of
    # the object shows a per field list of stored terms. This can be useful for debugging
    # of analyzer settings.
    fielddata: false
    # addresses of the elastic servers
    addresses:
      - "http://localhost:9200"
    # username
    username: ""
    # password
    password: ""

  # Client configuration of execserver is used
  # for syncing of files, metadata generation and plugin execution
  execserver:
    # number of parallel file workers, default to 1, set to 0 to disable
    parallel: 1
    # addresses of the execserver. they are tried in round robin.
    # if a server reports to be busy, the next server is tried.
    # if the server URL contains a /job/{service} path it is only used for the given service
    # example to only match service "node": http://localhost:8083/job/node?pretty=true
    addresses:
      - http://localhost:8083/?pretty=true
    # pluginJobTimeoutSec sets the maximum seconds a callback
    # is allowed to run. Defaults to 30 seconds.
    pluginJobTimeoutSec: 30
    # connectTimeout sets the maximum seconds the server will wait
    # until a worker gets a job. Defaults to 60 seconds.
    connectTimeoutSec: 60
    # callbackBackendInternalURL will be included in execserver jobs, this is
    # used for plugin installation (loaded from the backend into the execserver)
    # and progress updates.
    callbackBackendInternalURL: "http://localhost:8081"
    # callbackApiInternalURL will be presented to execserver plugin jobs. This
    # can be used by plugins to call back into the API.
    callbackApiInternalURL: "http://localhost:8080"


  # services which will be started. It is possible to configure a standalone
  # execserver or webapp. backend & server can only be configured together.
  services:
    # service "server" serves the API & oauth2
    api:
      # address of the api listener (with authentication)
      # if omitted, this server is not started
      addr: :8080
      # for tls support ("addr" only), provide a cert and key file
      tls:
        certFile: ""
        keyFile: ""

      # oauth2 server settings
      oauth2Server:
        # This secret is used to sign authorize codes, access and refresh
        # tokens. If unset, a random string is used. If multiple fylr server are
        # serving the same instance, the signingSecret needs to be configured.
        # The format is a 32-byte string.
        signingSecret: ""
        # allowHttpRedirects will disable the check whether a redirect URL is
        # secure. If set to true, this setting http urls are allowed to be used
        # for redirects. Default: false.
        allowHttpRedirects: false
        # map with pre-configured client, use for the webapp
        clients:
          web-client:
            # secret must be given as bcrypt hash
            secret: $2y$04$81xGNnm8PS1uiIzjbos6Le3NzFaNB0goNqnBpOx7S/EyrayzJCNAq # foo
            # this must point to the public URL or the webapp (/oauth2/callback)
            redirectURIs:
              - http://localhost/oauth2/callback
            # the scopes this client needs to be granted
            # offline is mandatory to issue refresh tokens
            # others will be used in rights management
            scopes:
              - "read"
              - "write"
              - "offline"
            # public, set to true if this client is publicly known
            public: false

    # service backend is used by the execserver as callback to
    # get installed plugins and to update progress during execution
    backend:
      # address of the server listener
      # if omitted, this server is not started
      addr: :8081
      # for tls support ("addr" only), provide a cert and key file
      tls:
        certfile: ""
        keyfile: ""
      # configure inspect to provide the /inspect endpoint
      # this endpoint doesnt have authentication, so handle
      # with care.
      inspect:
        # backup: if configured /inspect can be used to backup / restore
        # instances. The backup storage is on disk.
        backup:
          # disk path to backup. each backup gets its own subdirectory
          path: /tmp/backups
    # oauth2 client + web client

    webapp:
      # listener for the webapp
      addr: ":80"
      # For tls support ("addr" only), provide a cert and key file
      tls:
        certFile: ""
        keyFile: ""
        # Automatic certificate management can be enabled using the "letsencrypt"
        # property. With this setting, fylr automatically retrieves and renews
        # an certificate for the domain of fylr.externalURL.
        letsEncrypt:
          # email is used to register the certifcate with Let's Encrypt
          email: emailer@fylr.io
          # forwardHttpAddr defines an address a http listener is started
          # to forward requests to fylr.services.webapp.addr (the port of the)
          # webserver. Typically you use ":80" for the forward http and ":443"
          # for the main listener.
          forwardHttpAddr: ":80"
          # useStagingCA sets the staging server of Let's Encrypt which has a higher
          # quota than the production server. However, these certificates are for
          # testing purposes only. They are not signed for official use, so browser
          # will recognise them as being insecure.
          useStagingCA: false

      # javascript files for the webapp
      path: ../easydb-webfrontend/build
      # oauth2 client configuration to connect to
      # server. This must match the configuration above.
      oauth2:
        # clientID used to connect to oauth2 server
        clientID: web-client
        # clientSecret must be provided in clear
        clientSecret: foo
      # optional reverse proxy. redirect endpoint
      # /api and /inspect to target
      reverseProxy:
        api: "http://localhost:8080"
        backend: "http://localhost:8081"
      # http basic auth for all access to the webfrontend
      basicAuth:
        root: admin
      # Optional redirect. The requested path & query & hash is matched against
      # the "from" and redirected to "to" using the given statuscode as http
      # status. Variables can be replaced and take the form of "{...}". The
      # variables can contain a-z and A-Z characters and match all characters
      # (non-greedy til the next) given character. Variables at the end match
      # until the end of the URL.
      redirects:
        - from: "/easydb?myeasydb4ID={sid}"
          to: "/#/detail/{sid}"
          statuscode: 301

    # service execserver executes binaries and used by FYLR
    # to generate previews, execute plugins and to get metadata
    # of files.
    execserver:
      # addr of the execserver listener
      # if omitted no server is started
      addr: :8083

      # tokenResponseSendServerIP is the IP which can be used by
      # a client to send a job to. This IP is sent back to the client
      # in the token response
      tokenResponseSendServerIP: ""

      # Mandatory path to a directory the execserver - can work in. The
      # execserver will create a sub-directory per job and leave the space to
      # the worker. After the work is done, the sub-directory is removed. At
      # startup directories cache, job, plugin are deleted. Make sure that these
      # directories do not get deleted by the OS or other processes. The
      # subdirectories get cleaned by a built-in janitor process.

      # Defaults to fylr.tempDir
      tempDir: ""

      # jobRemovalPolicy can be "none", "done", "all". "none" never removes job
      # files after the job ran. However, these files are removed by the
      # janitor. "done" removes succesful jobs and leaves errornous job files
      # for inspection. "all" removes all job files after they ran. Defaults to
      # "done".
      jobRemovalPolicy: "done"

      # janitorFileAge sets the age for files before they are removed. https://pkg.go.dev/time#ParseDuration
      # is used to parse this value. Minimum duration is one minute. Defaults to "24h".
      janitorFileAge: "24h"

      waitgroups:
        a:
          processes: 4
        b:
          processes: 2
        c:
          processes: 4
      services:
        node:
          waitgroup: b
          commands:
            node:
              prog: "node"
        convert:
          waitgroup: a
          commands:
            convert:
              prog: "convert"
              env:
                - "OMP_NUM_THREADS=1"
              # if startupCheck is omitted, fylr only checks if it is in PATH
              # an empty startupCheck will execute the prog without any arguments
              startupCheck:
                # args are optional
                args:
                  - "-version"
                # If a regexp is given, the stdout of the command is checked against it
                regex: "Version: ImageMagick 7..*?https://imagemagick.org"
            composite:
              prog: "composite"
              env:
                - "OMP_NUM_THREADS=1"
              startupCheck:
                args:
                  - "-version"
                regex: "Version: ImageMagick 7..*?https://imagemagick.org"
            fylr_metadata:
              # For the blurhash production a maximum size can be set via env.
              # Settings this to "-" turns the blurhash off. Blurhash needs to
              # be calculated in RAM so the bigger the image is to produce a
              # blurhash, the more RAM is needed. More info about blurhashes can
              # be found here: https://blurha.sh/. The default for this setting
              # is unlimited.
              env:
                - FYLR_METADATA_BLURHASH=1g
              prog: "utils/fylr_metadata/fylr_metadata"
        ffmpeg:
          waitgroup: a
          commands:
            ffmpeg:
              prog: ffmpeg
              startupCheck:
                args:
                  - "-version"
                regex: "ffmpeg version 5[\\.0-9]+ Copyright"
            ffprobe:
              prog: ffprobe
              startupCheck:
                args:
                  - "-version"
                regex: "ffprobe version 5[\\.0-9]+ Copyright"
            convert:
              prog: "convert"
              env:
                - "OMP_NUM_THREADS=1"
              startupCheck:
                args:
                  - "-version"
                regex: "Version: ImageMagick 7..*?https://imagemagick.org"
            composite:
              prog: "composite"
              env:
                - "OMP_NUM_THREADS=1"
              startupCheck:
                args:
                  - "-version"
                regex: "Version: ImageMagick 7..*?https://imagemagick.org"
            fylr_metadata:
              prog: "utils/fylr_metadata/fylr_metadata"
            ffmpegthumbnailer:
              prog: ffmpegthumbnailer
              startupCheck:
                args:
                - "-v"
                regex: "ffmpegthumbnailer version: 2\\..*"
        soffice:
          waitgroup: c
          commands:
            soffice:
              prog: soffice
              startupCheck:
                args:
                  - "--headless"
                  - "--invisible"
                  - "--version"
                regex: "LibreOffice 7[.0-9]+"
            convert:
              prog: "convert"
              env:
                - "OMP_NUM_THREADS=1"
              startupCheck:
                args:
                  - "-version"
                regex: "Version: ImageMagick 7..*?https://imagemagick.org"
            composite:
              prog: "composite"
              env:
                - "OMP_NUM_THREADS=1"
              startupCheck:
                args:
                  - "-version"
                regex: "Version: ImageMagick 7..*?https://imagemagick.org"
            fylr_metadata:
              prog: "utils/fylr_metadata/fylr_metadata"
        metadata:
          waitgroup: a
          commands:
            fylr_metadata:
              prog: "utils/fylr_metadata/fylr_metadata"
            ffprobe:
              prog: ffprobe
              startupCheck:
                args:
                  - "-version"
                regex: "ffprobe version 4[\\.0-9]+ Copyright"
        pdf2pages:
          waitgroup: a
          commands:
            fylr_pdf2pages:
              # fylr_* utils use other programs to do their job. These
              # programs must be either found in the $PATH of the OS or
              # passed in by environment in the form of FYLR_CMD_<prog>
              # The <prog> is the program name (upper case)
              #
              # pdf2pages needs
              #   - fylr_metadata
              #   - magick
              env:
                - FYLR_CMD_FYLR_METADATA=../../utils/fylr_metadata/fylr_metadata
              prog: "utils/fylr_pdf2pages/fylr_pdf2pages"
            fylr_metadata:
              # fylr_metadata needs
              #   - exiftool
              prog: "utils/fylr_metadata/fylr_metadata"
        xslt:
          waitgroup: a
          commands:
            xsltproc:
              prog: "xsltproc"
        iiif:
          waitgroup: a
          commands:
            fylr_iiif:
              # fylr_iiif needs
              #   - magick
              prog: "utils/fylr_iiif/fylr_iiif"
              startupCheck:
                args:
                  - "-version"
                regex: "Version v*"
```
{% endcode %}
