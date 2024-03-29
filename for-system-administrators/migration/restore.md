---
description: >-
  This page describes the process of inserting a local backup of JSON payloads to a target fylr instance
---

# Insert payloads (`fylr restore`)

The `fylr restore` command performs `POST` requests to the API of the target fylr instance. It iterates over the list of payloads from the `manifest.json` file.

A basic restore command looks like this:

```
fylr restore \
  --server '<fylr url>/api/v1' \
  --login root
  --password '<cleartext>' \
  --manifest '<instance folder>/manifest.json' \
  --client-id web-client \
  --client-secret foo \
  --client-token-url '<fylr url>/api/oauth2/token' \
  --chunk 1000 \
  --timeout-min=1 \
  --file-api rput \
  --file-version original \
  --purge # --purge OR --continue
```

* `--server`, `--login` and `--password` refer to the target server
* for the `--server` parameter, include the HTTP Basic Auth: `http://<login>:<password>@<fylr url>/api/v1`
* `--chunk` defines the batch size of objects in POST requests to `api/v1/db`
  * if the objects are too big or complex, the requests might take too long and cause a timeout
  * in this case, lower this value and continue restoring with `--continue`


## Parameters

This is a complete overview of the command line parameters (run `fylr restore -h`):

```
Usage: fylr restore

Restore API backup into FYLR

Flags:
  -h, --help                                   Show context-sensitive help.

      --manifest=STRING                        Path to manifest.json.
      --base-config=STRING                     Base config to upload to the target. Only supported with --purge. By default the base config from the backup is uploaded. Use "-" to not upload
                                               a base config.
      --continue                               Set to true, to continue restoring payloads from progress.json.
      --upload-ignore-files-with-errors        Set to true, to ignore file upload errors and strip objects from them.
      --max-parallel-upload-files=4            Max number of parallel original file + its versions uploads. Defaults to 4 (0 for bulk), max is 10 (unlimited for bulk).
      --timeout-min=10                         Timeout for connections to target (minutes).
      --include-password                       Include password in user restore.
      --skip-constraints                       Skip constraints during restore.
      --file-api=STRING                        API used to upload files. Leave empty to not upload files. "put": restore tool uploads files synchronous. "rput": target server loads files
                                               from remote URLs. "rput_leave": target server stores remote URLs, no data is copied to storage. "rput" and "rput_leave" are faster, "put" might
                                               take long.
      --file-api-append-to-url-query=STRING    Append to eas urls (use this to pass an access token to fylr backends). ? or & is prefixed to this as needed.
      --file-version=STRING                    Set to version to use for upload. "original" might take long for "put". Use "preview" for test runs.
      --upload-versions                        Set to true, to not produce local preview versions, but instead upload the source versions. The upload method is used for versions the same way
                                               as for the original.
      --rename-versions=RENAME-VERSIONS,...    Rename versions before uploading. This affects uploaded rights as well as file versions. The versions need to be given in the notation
                                               "<cls>.<version>:<new version>", e.g. "image.preview:640px" would replace the "preview" version of image to "640px". If the "<new version>" is
                                               omitted, the version is removed.
  -v, --verbose                                Set to true, to show additional info.
  -n, --log-network                            Set to true, to log all network traffic.
      --log=STRING                             Set output to logfile
      --purge                                  Set to true, to purge the target and copy the datamodel. The current password of the user used for the login will be set for the system root
                                               user.
      --limit=INT                              Limit records. Set to 0 for unlimited.
      --chunk=100                              chunk size for fetching/pushing data.
      --server=STRING                          Source url (overwrites URL of source instance from config)
  -l, --login=STRING                           If --server is set, use as login. Make sure to use the system root user to connect if used together with --purge.
  -p, --password=STRING                        If --server is set, use as password
      --client-id=STRING                       If --server is set, use as OAUTH2 client ID
      --client-secret=STRING                   If --server is set, use as OAUTH2 client secret
      --client-token-url=STRING                If --server is set, use as OAUTH2 token url
```


<!-- vvvvv --- this part was auto generated: 2024-03-19 16:10:46 (UTC) --- vvvvv -->



### `--manifest`

Manifest file that has been created by the `backup` command.

* this parameter is **mandatory**!
* type: `string`


### `--server`

API Url of the target instance. The Url must include the API base endpoint, for fylr this is `<target url>/api/v1`.

* this parameter is **mandatory**!
* type: `string`


### `--login`

Username of the user in the target instance. It should be a user with root rights or sufficient read rights.

* this parameter is **mandatory**!
* type: `string`


### `--password`

Password of the user in the target instance.

* this parameter is **mandatory**!
* type: `string`


### `--purge`

Defines the mode of the restoring (purge or continue)
If this is `true`, the complete restore starts from the beginning, and the target instance is purged.
The parameters `--purge` and `--continue` are mutually exclusive. Exactly one of the two must be `true`.

* this parameter is **mandatory**!
* type: `bool`
* default: `false`


### `--continue`

Defines the mode of the restoring (purge or continue)
If this is `true`, the restore continues from the last point in the `progress.json` file, if a previous restore run was interrupted.
The parameters `--purge` and `--continue` are mutually exclusive. Exactly one of the two must be `true`.

* this parameter is **mandatory**!
* type: `bool`
* default: `false`


### `--base-config`

Path to a specific base config file. Defaults to `<instance folder>/base_config.json` from the backup.

* type: `string`


### `--skip-constraints`

Skip constraints during restore.

* type: `bool`
* default: `false`


### `--include-password`

Include user password hashes. If this option is `true`, the restore tool checks if there is at least one user where a password hash is present. This is done by checking the `has_passwords` flag in the `manifest.json`. If this value is `false`, the restore will stop with an error.

Make sure that the source instance is configured to output the user passwords, and repeat the backup. See [https://docs.easydb.de/en/sysadmin/configuration/easydb-server.yml/available-variables/](https://docs.easydb.de/en/sysadmin/configuration/easydb-server.yml/available-variables/) under `include_passwords` for the settings in an easydb5 source instance.

* type: `bool`
* default: `false`


### `--chunk`

The upload batch size for objects to the target instance. Can be used to control the size of the requests. It can be lowered if the requests cause timeouts or network problems.

* type: `int`
* minimum: `1`
* maximum: `1000`
* default: `100`


### `--limit`

Set this to a number bigger than `0` to limit the number of objects of each objecttype. This can be used to test or debug to only restore a small sample of the source instance.

* type: `int`
* minimum: `0`
* default: `0`


### `--file-api`

Method used to upload files. Leave empty to not upload files.
* `put`: restore tool uploads files synchronous.
* `rput`: target server loads files from remote URLs.
* `rput_leave`: target server stores remote URLs, no data is copied to storage.

`rput` and `rput_leave` are faster, `put` might take long.

* type: `string`


### `--file-api-append-to-url-query`

Append parameters to eas urls (for example, use this to pass an access token to fylr backends). `?` or `&` is prefixed to this as needed.

* type: `string`


### `--file-version`

Specify which version of the source asset is used. Default is `"original"` which might take long for `--file-api=put`. Use `"preview"` for test runs with smaller assets.

* type: `string`
* default: `"original"`


### `--upload-versions`

Set to `true`, to not produce local preview versions, but instead upload the source versions. The upload method `--file-api` is used for versions the same way as for the original.

* type: `bool`
* default: `false`


### `--rename-versions`

Rename versions before uploading. This affects uploaded rights as well as file versions.
The versions need to be given in the notation `"<cls>.<version>:<new version>"`, e.g. `"image.preview:640px"` would replace the `"preview"` version of class `image` to `640px`.
If the `<new version>` part is omitted, the version is removed.

* type: `string`


### `--max-parallel-upload-files`

Maximum number of parallel uploads of original files and their versions. Defaults to `4` (`0` for bulk). The maximum is `10` (unlimited for bulk).

* type: `int`
* minimum: `0`
* maximum: `10`
* default: `4`


### `--upload-ignore-files-with-errors`

Set to `true` to ignore file upload errors and strip objects from them.

* type: `bool`
* default: `false`


### `--client-id`

If the target instance uses OAuth2 for user authentication, this is the configured Client ID.

* type: `string`


### `--client-secret`

If the target instance uses OAuth2 for user authentication, this is the configured Client Secret. Can be kept empty if the instance is public.

* type: `string`


### `--client-token-url`

If the target instance uses OAuth2 for user authentication, this is the OAuth2 callback endpoint of the instance. For fylr this is `<source url>/api/oauth2/token`.

* type: `string`


### `--verbose`

Set to `true` to log debugging info.

* type: `bool`
* default: `false`


### `--log-network`

Set to `true` to log the requests and responses.

* type: `bool`
* default: `false`


### `--log`

If this is a valid file path, the log output is written to this file. If this is empty (default), the log output is written to `stdout` instead.

* type: `string`


<!-- ^^^^^ --- this part was auto generated --- ^^^^^ -->

