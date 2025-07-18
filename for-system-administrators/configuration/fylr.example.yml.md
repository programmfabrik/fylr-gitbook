---
description: >-
  Most settings possible in fylr.yml and explanations as comments
---

# fylr.example.yml

This is NOT a coherent fylr.yml, do not use for an installation; use [this](https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/\_assets/fylr.yml) instead.

If you start your hierarchy in fylr.yml with `fylr+:` instead of `fylr:`, then defaults are used where not explicilty overwritten. Defaults see [fylr.default.yml](fylr.default.yml.md)

{% code title="fylr.yml" %}
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
##   fylr+:
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

  # Name of the instance (mandatory). It is used as prefix for the bucket
  # names and elastic indexes. The name must match regexp [a-z][a-z0-9\-_]*[a-z0-9]:
  # All small letters, start with a letter, followed by small letter, a number, dash or
  # underscores, ending in letter or number. Must be between 3 and 32 bytes.
  name: "myfylr"

  # Public external url of the server. This url needs to be fully qualified. If
  # you change this url for an existing database, a re-index is needed to update
  # all object caches (which store the URL). This re-index can be started from
  # /inspect/system.
  #
  # This URL has to be part of your license, except testing as root or on localhost.
  #
  # fylr will redirect all incoming requests to this externalURL, unless there is
  # a reverse proxy source matching in fylr.services.webapp.reverseProxy.custom.
  externalURL: "http://localhost"

  # The license file can also be uploaded into the fylr webfrontend as root.

  # licenseFile (default: none). Path to license file. This is used as default
  # if nothing is set in the baseconfig. This setting is mutually exclusive with
  # fylr.license.
  licenseFile: "license.json"

  # license: Inline JSON of license.  This is used as default if nothing is set
  # in the baseconfig. This setting is mutually exclusive with fylr.licenseFile.
  license: "<JSON>"

  # encryptionKey is used to AES-encrypt sensitive information before writing it
  # to the database. It must be 32 bytes long. Default is empty.
  encryptionKey: ""

  # stdErrFile redirects all output to stderr to the given file when fylr is run
  # as a server. If the file cannot be created for writing, fylr will not start.
  # The file path is relative to fylr's working directory.
  stdErrFile: ""

  # for development only
  debug:
    # Skip term creation
    skipTerms: false
    # Don't announce plugins bundle on /api/plugin
    noPluginsBundle: false
    # Simulate local status
    localStatus: "" # purge, reindex, startup, ready
    # This setting skips the sometime expensive permission check
    # on the /api/eas/download endpoint. However, there is still
    # some security left, the link is checked against a valid hash
    # of the file which needs to be provided.
    easDownloadSkipCheckRights: false
    # Allow management of indices in Elasticsearch cluster, such as
    # viewing and deleting an index.
    # The indices visible there are not limited to those associated
    # to the fylr instance.
    inspectEnableElasticIndices: false
    # Outputs object loader timing and load depth information. This setting can also
    # be set in the base config.
    logTimings: true
    # Set to true to disable loading standard from cache. This can help to
    # investigate indexer problems.
    objectLoadDisableCache: false
    # indexerSingleMode sets the request to single mode instead of bulk mode,
    # set this to true to more easily debug index requests. Default: false.
    indexerSingleMode: false
    # indexerDebug can be set to output statistics & memory allocation information
    # during object indexing. Defaults to false.
    indexerDebug: false
    # indexerNestedNotIncludeInRoot can be set to not include nested documents
    # in the root document. If set, queries are wrapped into the nested index
    # if they are not already inside a "type": "nested". This is for development
    # purposes only. If you change this option, a re-index is required.
    indexerNestedNotIncludeInRoot: false
    # janitorEnableObjectAndFileRemoval can be set to run the janitor file removal
    # procedure. This will be enabled by default in 6.23.0 and is in 6.22.0 as
    # an experimental feature.
    janitorEnableObjectAndFileRemoval: false

  # optional, set environment. This can be used to set FYLR_CMD_* inside the fylr.yml
  env:
    # FYLR_CMD_PG_DUMP: ./services/bin/pg_dump

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
    # example values and their effect:
    #  "2006-01-02 15:04:05" a template (recommended. 1 to 6 mark the fields)
    #   see https://pkg.go.dev/time#example-Time.Format for details
    #  "" results in time only (console format) or seconds since 1970 (json format)
    #  "UNIXMS" milliseconds since 1970 (json format only)
    #  "UNIXMICRO" microseconds since 1970 (json format only)
    # Defaults to ""
    timeFormat: "2006-01-02 15:04:05Z07"
    # turn off color for zerolog's underlying ConsoleWriter
    # format: "console" only.
    noColor: false
    # add hostname to log output
    addHostname: false
    # add remote addr to log output
    addRemoteAddr: false
    # wrong password log level, set the level for wrong password output
    wrongPasswordLevel: debug

  # data is stored in a database, FYLR supports sqlite & postgres
  db:
    # driver: sqlite3
    # dsn: "../../_data/sqlite/fylr.db"
    driver: postgres

    # specify a PostgreSQL user owning the given db (with LOGIN and INHERIT, which are defaults for CREATE USER anyway).
    dsn: "host=localhost port=5432 user=fylr password=fylr dbname=fylr sslmode=disable"

    # https://golang.org/pkg/database/sql/#DB.SetMaxOpenConns default: 100 At
    # least: 4 + execserver.parallel + execserver.parallelHigh +
    # elastic.parallel. Two of these connections will be dedicated to a separate
    # connection pool managing the sequences. The recommended setting for this
    # is 100. It is not recommended to set it to 0 (unlimited), as this can
    # possibly open too many connections for the OS to handle. Also, since each
    # request to the API will query the database at least once, this setting
    # doubles as a rate throttler. (Postgres only)
    maxOpenConns: 100

    # https://golang.org/pkg/database/sql/#DB.SetMaxIdleConns, default: 0
    # This has to be not more than maxOpenConns
    maxIdleConns: 10

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
      # baseconfig setting in this .yml file. Runs after configFile, so
      # everything in config overwrites settings from configFile. Default is
      # empty.
      config: null

      # location_defaults map accepts location ids as well as names:
      config:
        system:
          config:
            location_defaults:
              originals: mys3
              versions: mys3
              backups: myfile
      # To setup purgeable locations:
      #       purge:
      #         allow_purge: true
      #         purge_storage: true

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
        myfile:
          # The kind is either "file" or "s3" or "azure" (see below)
          kind: file
          # Each location can configure a prefix which will
          # be attached before the file to be created
          prefix: "apitest/"
          # Set to true if files in this location can be
          # purged by FYLR (if the purge api call is used)
          allow_purge: true
          # For "file" storage backend allow_redirect is a dangerous
          # setting and should be used for development purposes only.
          # Default is the safe false.
          allow_redirect: false
          config:
            file:
              dir: "_files"
        mys3:
          kind: s3
          prefix: "apitest/"
          allow_purge: true
          # Set allow_redirect to true to expose download URLs directly to the s3 provider.
          # Default is false.
          # false uses fylr URLs instead, which might be less performant.
          allow_redirect: false
          config:
            s3:
              bucket: apitest
              endpoint: "127.0.0.1:9000"
              accesskey: "minioadmin"
              secretkey: "minioadmin"
              region: "us-east-1"
              ssl: false
        myazure:
          kind: azure
          allow_purge: true
          config:
            azure:
              # The name of the container is required. It is created if it doesn't exist.
              container: fylr
              # You can provide a connection string OR the single settings account_name, account_key and endpoint_suffix
              connection_string: "DefaultEndpointsProtocol=https;AccountName=azure;AccountKey=l/fnF4kp...==;EndpointSuffix=core.windows.net"
              account_name: "azure"
              account_key: "l/fnF4kp..."
              # optional endpoint suffix (default to core.windows.net)
              endpoint_suffix: "core.windows.net"

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
    # default defines the generic default for new plugins. Plugins are new when they are inserted into the database.
    default:
      enabled: false
      update_policy: "automatic"
    # defaults is a map setting defaults for the plugin registration.
    # This is configured as map with the plugin name as key.
    defaults:
      # default for fylr_example plugin
      fylr_example:
        # enable, set to false to disable the plugin, defaults to true
        enabled: false
        # update_policy: automatic, always, never, defaults to automatic
        update: "never"

  # Set to true to allow /api/settings/purge. dont use on production systems!
  allowpurge: true

  # Optional path to resources, that are all files needed by FLYR during runtime
  # (inspect, pages, etc..) If unset, fylr uses binary embedded resources (so no
  # resource folder needed in that case). Defaults to embedded. Resources are
  # overloaded, if the given directory tree doesn't contain the resource
  # requested, fylr uses the embedded resource. To see what files are loaded
  # from where use "fylr resources".
  resources: ""

  # Elastic is the indexer for FYLR
  elastic:
    # Logger used for the elastic client
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
    # maxMem is the cut-off JSON size in bytes for objects sent to the indexer. Defaults to 100MB.
    maxMem: 100mb
    # maxHeapAlloc is the maxium allocation of heap memory during indexing of
    # user objects (not base types). fylr tries to keep the heap memory below
    # this value. If fylr sees twice the heap size used, it runs the Go garbage
    # collector and outputs a warning. In such a case, the maxHeapAlloc should
    # be set to a higher value or the datastructure of the indexed objects need
    # to be looked at. On capable systems we recommend 4G, defaults to 1G.
    maxHeapAlloc: 1g
    # fielddata (debug feature). if set to true, fields are mapped including their fielddata
    # in the reverse index. with that, the inspect view of the indexed version of
    # the object shows a per field list of stored terms. This can be useful for debugging
    # of analyzer settings.
    fielddata: false
    # addresses of the elastic servers, see https://godoc.org/github.com/elastic/go-elasticsearch#Config for details.
    addresses:
      - "http://localhost:9200"
    # username
    username: ""
    # password
    password: ""
    # startupConnectTimeSec. Number of seconds fylr tries to reach the indexer at startup. If the indexer cannot be reached fylr
    # will not start and exit. fylr will try every 5 seconds to ping the indexer. Defaults to 50.
    startupConnectTimeSec: 50

    # metadataFulltextLimit. Number of bytes to limit indexed fulltext. For files we might index fulltext information. This
    # parameter limits the number of bytes to which the fulltext is indexed. This is per language for localised fields. Defaults to "1mb".
    # The format is a human readable format like "100mb" or "100kb".
    metadataFulltextLimit: "1mb"


  # Client configuration of execserver is used
  # for syncing of files, metadata generation and plugin execution
  execserver:
    # number of parallel file workers, default to 2, set to 0 to disable.
    parallel: 2
    # number of parallel file workers only taking high priority tasks. Currently
    # producing of all standard versions is a high priority task.
    parallelHigh: 2
    # addresses of the execserver. they are tried in round robin.
    # if a server reports to be busy, the next server is tried.
    # if the server URL contains a /job/{service} path it is only used for the given service
    # example to only match service "node": http://localhost:8083/job/node?pretty=true
    addresses:
      - http://localhost:8083/?pretty=true
    # the maximum a callback is allowed to run
    pluginJobTimeoutSec: 2400
    # the maximum the server will wait until a worker gets a job
    connectTimeoutSec: 120
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
      # if omitted, this server is not started.
      addr: ":8080"

      # for tls support ("addr" only), provide a cert and key file
      tls:
        certFile: ""
        keyFile: ""

      # hotfolder path, if set this folder will be created by fylr (if not
      # exists).
      webDAVHotfolderPath: "_hotfolder"

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
        # The default clients are built into the web app and other apps.
        # They are public and thus do neither need nor have a secret.
        # see https://docs.fylr.io/for-system-administrators/configuration/fylr.default
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

    # service backend is used for /inspect and by the execserver as callback
    # to get installed plugins and to update progress during execution
    backend:
      # address of the server listener
      # if omitted, this server is not started
      addr: :8081
      # for tls support ("addr" only), provide a cert and key file
      tls:
        certFile: ""
        keyFile: ""
      # provide the /inspect URL endpoint
      inspect+:
        # backup: if configured, /inspect/migration can be used to migrate
        # instances.
        backup+:
          # Path is needed if you want to use /inspect/migration of this
          # instance. Disk path to backup. Is created if not present. Each
          # backup gets its own subdirectory.
          path: /tmp/migration

    # oauth2 client + web client
    webapp:
      # listener for the webapp
      addr: ":80"
      # For tls support ("addr" only), provide a cert and key file
      tls:
        # certFile contains the certificate in pem Format and optionally intermediate chain certificates below in the same file.
        certFile: "server.crt"
        keyFile: "server.key"

        # forward requests to fylr.services.webapp.addr (the port of the) webserver.
        # Typically you use ":80" for the forward http and ":443" for webapp.addr.
        # Default is "" (off)
        # With letsEncrypt configured below, this is used for:
        #forwardHttpAddr: ""    # use port 443, letsencrypt challenge_type=tls-alpn-01
        #forwardHttpAddr: ":80" # use port  80, letsencrpyt challenge_type=http-01
        forwardHttpAddr: ":80"

        # Automatic certificate management can be enabled using the "letsencrypt"
        # property. With this setting, fylr automatically retrieves and renews
        # an certificate for the domain of fylr.externalURL.
        letsEncrypt:
          # email is used to register the certificate with Let's Encrypt
          email: you@example.com

          # useStagingCA sets the staging server of Let's Encrypt which has a higher
          # quota than the production server. However, these certificates are for
          # testing purposes only. They are not signed for official use, so browser
          # will recognise them as being insecure.
          useStagingCA: false

          # additionalDomains can be given to get additional certificates for the given
          # domains.
          # additionalDomains:
          # - "www.database.de"

      # javascript files for the webapp
      path: ../easydb-webfrontend/build
      # oauth2 client configuration to connect to
      # server. This must match the configuration above.
      oauth2:
        # clientID used to connect to oauth2 server
        clientID: web-client
        # clientSecret must be provided in clear
        clientSecret: foo
        # Optional setting of the URL used to build the token url which is used
        # for server to server communication to exchange the auth code for a
        # token defaults to fylr.externalURL
        # Needs to be set to the port of fylr.services.api.addr
        internalURL: "http://localhost:8080/"

      # The reverse proxy can be used to redirect requests to the api
      # and the backend and also for custom servers behind fylr.
      reverseProxy+:
        # The webapp can redirect request to /api and /inspect to the respective
        # backend services fylr.services.api and fylr.services.backend if
        # configured in the reverseProxy.
        #
        # For /api the webapp has a special mode where itself is serving the
        # requests. This saves time during the request as it is not passing the
        # request onto the api server but serving this internally. To activate
        # this mode, the keyword "bind" must be set in reverseProxy.api. This is
        # also the default. These requests will be logged as "webapi".
        api: "http://localhost:8080"

        # The backend serves the /inspect pages and is used to store and
        # retrieve files from file based storage locations. It is recommended to
        # proxy /inspect to the backend server so that users can access /inspect
        # through the regular fylr url and port. When served through the reverse proxy,
        # a root login is required to access.
        backend: "http://localhost:8081"

        # Custom map for reverse proxy endpoints.
        # fylr uses https://pkg.go.dev/net/http/httputil#NewSingleHostReverseProxy.
        # Before the : give a path prefix like /system2 or a domain as //example.com/.
        # After the : give the URL of the existing content, may contain :port.
        custom:
          # show http://localhost:81/system2 at https://externalURL/system2
          "/system2": "http://localhost:81"
          # you may need to replace localhost if fylr runs in a container

          # the next line shows http://1.2.3.4:81/ at https://example.com
          "//example.com/": http://1.2.3.4:81/
          # you need the https certificat for example.com, e.g. with additionalDomains

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
      # env can be set for all programs started by the execserver
      # this is overwritten by the env set for the specific command and by the
      # os environment
      env:
        - FYLR_METADATA_BLURHASH=1g
        # set env to set threads used by ffmpeg for mp4
        - FYLR_CONVERT_VIDEO_MP4_THREADS=2
        # overwrite to use a different binary, defaults to "chromium" for the PDF plugin
        - SERVER_PDF_CHROME=chromium

      # common command defintion for all services. Also used to set FYLR_CMD_<PROG> environment
      # for helper programs which are started by "fylr SUBCOMMAND". Like "exiftool" or "magick"
      commands:
        exiftool:
          prog: exiftool
        magick:
          prog: magick
          args:
            # %_exec.binDir% is replaced with the directory the binary is in
            - more

      services:
        node:
          waitgroup: b
          commands:
            node:
              prog: "node"
        python3:
          waitgroup: b
          commands:
            python3:
              prog: "python3"
        convert:
          waitgroup: a
          commands:
            fylr_convert:
              prog: "fylr"
              args:
                - "convert"
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
              prog: "fylr"
              args:
                # %_exec.binDir% is replaced with the directory the binary is in
                - "metadata"
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
              env:
                - FYLR_METADATA_BLURHASH=1g
              prog: "fylr"
              args:
                - "metadata"
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
              env:
                - FYLR_METADATA_BLURHASH=1g
              prog: "fylr"
              args:
                - "metadata"

        metadata:
          waitgroup: a
          commands:
            fylr_metadata:
              env:
                - FYLR_METADATA_BLURHASH=1g
              prog: "fylr"
              args:
                - "metadata"

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
              #   - exiftool
              #   - magick
              prog: "fylr"
              args:
                - "pdf2pages"

            fylr_metadata:
              env:
                - FYLR_METADATA_BLURHASH=1g
              prog: "fylr"
              args:
                - "metadata"
        xslt:
          waitgroup: a
          commands:
            saxon:
              prog: "saxon"
        iiif:
          waitgroup: a
          commands:
            convert:
              prog: convert
            fylr_iiif:
              prog: "fylr"
              args:
                - "iiif"
```
{% endcode %}
