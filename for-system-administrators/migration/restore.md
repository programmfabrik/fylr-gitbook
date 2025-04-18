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
Usage: fylr restore [flags]

Restore API backup into FYLR

Flags:

-h, --help                    Show context-sensitive help.
-v, --verbose                 Set to true, to show additional info.
-n, --log-network             Set to true, to log all network traffic.
    --server=STRING           Source url (overwrites URL of source instance from config)
-l, --login=STRING            If --server is set, use as login. Make sure to use the system root user to connect if used together with --purge.
-p, --password=STRING         If --server is set, use as password
    --client-id=""            If --server is set, use as OAUTH2 client ID
    --client-secret=""        If --server is set, use as OAUTH2 client secret
    --client-token-url=""     If --server is set, use as OAUTH2 token url
    --insecure                Set to true, to not verify the server's certificate chain and host name
    --log=STRING              Set output to logfile
    --purge                   For backup: set to true, to purge the target directory. For restore: set to true, to purge the target and copy the datamodel. The current password of the user used for the login will be set for the system root user.
    --continue                Set to true, to continue.
    --verify                  If set, verify payloads of an existing backup (same what --continue does at the beginning).
    --chunk-size=100          chunk size for fetching/pushing data.
    --include-events=""       Comma separated list of event types. Use "-" to skip backup/restoring of events. Empty string will backup/restore all known event types.
    --max-parallel=1          Maximum numbers of parallel workers. 0 uses the number of available CPUs. This creates more load on the source / target system. Defaults to "1" (only one parallel process).
    --manifest=STRING         Path to manifest.json.
    --base-config=STRING      Base config to upload to the target. Not supported with --continue. By default the base config from the backup is uploaded. Use "-" to not upload a base config.
    --datamodel=STRING        Datamodel to upload to the target. Not supported with --continue. By default the datamodel from the backup is uploaded. Use "-" to not upload a datamodel.
    --upload-ignore-files-with-errors Set to true, to ignore file upload errors and strip objects from them. Not available in rput_bulk modes.
    --max-parallel-upload-files=4 Max number of parallel original file + its versions uploads. Defaults to 4 (0 for bulk), max is 100.
    --timeout-min=10          Timeout for connections to target (minutes).
    --include-password        Include password in user restore.
    --skip-constraints        Skip constraints during restore.
    --file-api=""             API used to upload files. Leave empty to not upload files. "put": restore tool uploads files synchronous. "rput": target server loads files from remote URLs. "rput_leave": target server stores remote URLs, no data is copied to storage. "rput" and "rput_leave" are faster, "put" might take long.
    --file-api-access-token="" Use this to pass an access token to fylr backends. This is needed to load files from fylr source instances. It appends the "access_token" query parameter to the remote url of files, and removes the "x-fylr-signature" query parameter.
    --file-version=""         Set to version to use for upload. "original" might take long for "put". Use "preview" for test runs.
    --upload-versions         Set to true, to not produce local preview versions, but instead upload the source versions. The upload method is used for versions the same way as for the original.
    --rename-versions=,...    Rename versions before uploading. This affects uploaded rights as well as file versions. The versions need to be given in the notation "<cls>.<version>:<new version>", e.g. "image.preview:640px" would replace the "preview" version of image to "640px". If the "<new version>" is omitted, the version is removed.
```


<!--

part below was auto generated
source: https://docs.google.com/spreadsheets/d/1JXKxGe6RaIGCpS8JY12qrnlESxDCm9dz8EmeeWmK57U/export?format=csv&gid=1408589219
timestamp: 2025-04-14 10:48:35 (UTC)

-->



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

Defines the mode of the restoring (purge or continue).

If this is `true`, the complete restore starts from the beginning, and the target instance is purged.

{% hint style="warning" %}
The parameters `--purge` and `--continue` are mutually exclusive. Not both can be `true`.
{% endhint %}

* type: `bool`
* default: `false`


### `--continue`

Defines the mode of the restoring (purge or continue).

If this is `true`, the restore continues from the last point in the `progress.json` file, if a previous restore run was interrupted.

{% hint style="warning" %}
The parameters `--purge` and `--continue` are mutually exclusive.
{% endhint %}

* type: `bool`
* default: `false`


### `--base-config`

Path to a specific base config file. Defaults to `<instance folder>/base_config.json` from the backup.

{% hint style="info" %}
To not upload a base configuration to the target instance, specify `--base-config=-`
{% endhint %}

{% hint style="warning" %}
This parameter is not allowed in combination with `--continue`.
{% endhint %}

* type: `string`
* default: `base_config.json`


### `--datamodel`

Path to a specific datamodel file. Defaults to `<instance folder>/datamodel.json` from the backup.

{% hint style="info" %}
To not upload a datamodel to the target instance, specify `--datamodel=-`
{% endhint %}

{% hint style="warning" %}
This parameter is not allowed in combination with `--continue`.

Trying to upload a datamodel without `--purge` will not work, if there is already a datamodel on the target instance!

Only use `--datamodel=-` if the target instance already has a matching datamodel!
{% endhint %}

* type: `string`
* default: `datamodel.json`


### `--skip-constraints`

Skip constraints during restore.

* type: `bool`
* default: `false`


### `--include-password`

Include user password hashes. If this option is `true`, the restore tool checks if there is at least one user where a password hash is present. This is done by checking the `has_passwords` flag in the `manifest.json`. If this value is `false`, the restore will stop with an error.

{% hint style="warning" %}
If the source is an **easydb5**: make sure that the source instance is configured to output the user passwords, and repeat the backup. See [https://docs.easydb.de/en/sysadmin/configuration/easydb-server.yml/available-variables/](https://docs.easydb.de/en/sysadmin/configuration/easydb-server.yml/available-variables/) under `include_passwords` for the necessary settings in the source instance.

For a **fylr** source instance this is not necessary, since the password hashes are always returned over the API.
{% endhint %}

* type: `bool`
* default: `false`


### `--include-events`

Comma separated list of event types.

{% hint style="info" %}
Use `--include-events=-` to skip restoring of events.

If this parameter is unset, all events are restored which have a type that is known in fylr. All other events from the backup are ignored.
{% endhint %}

* type: `string`
* default: `""`


### `--chunk`

{% hint style="warning" %}
**Deprecated!** This parameter is removed in fylr in version **v6.18.0**.
{% endhint %}

The upload batch size for objects to the target instance. Can be used to control the size of the requests. It can be lowered if the requests cause timeouts or network problems.

{% hint style="warning" %}
This parameter was renamed to `--chunk-size`
{% endhint %}

* type: `int`
* minimum: `1`
* maximum: `1000`
* default: `100`


### `--chunk-size`

{% hint style="info" %}
This parameter is available in fylr from version **v6.18.0**.
{% endhint %}

The upload batch size for objects to the target instance. Can be used to control the size of the requests. It can be lowered if the requests cause timeouts or network problems.

* type: `int`
* minimum: `1`
* maximum: `1000`
* default: `100`


### `--limit`

{% hint style="warning" %}
**Deprecated!** This parameter is removed in fylr in version **v6.17.0**.
{% endhint %}

Set this to a number bigger than `0` to limit the number of objects of each objecttype. This can be used to test or debug to only restore a small sample of the source instance.

* type: `int`
* minimum: `0`
* default: `0`


### `--file-api`

Method used to upload files. Leave empty to not upload files.
* `put`: restore tool uploads files synchronous.
* `rput`: target server loads files from remote URLs.
* `rput_leave`: target server stores remote URLs, no data is copied to storage.

{% hint style="info" %}
`rput` and `rput_leave` are faster, `put` might take long.
{% endhint %}

* type: `string`


### `--file-api-access-token`

Use this to pass an access token to fylr backends. This is needed to load files from fylr source instances. It appends the `access_token` query parameter to the remote url of files, and removes the `x-fylr-signature` query parameter.

* type: `string`


### `--file-version`

Specify which version of the source asset is used. Default is `"original"` which might take long for `--file-api=put`.

{% hint style="info" %}
Use `"preview"` for test runs with smaller assets.
{% endhint %}

* type: `string`
* default: `"original"`


### `--upload-versions`

Set to `true`, to not produce local preview versions, but instead upload/link the source versions.

The upload method `--file-api` is used for versions the same way as for the original file.

{% hint style="info" %}
* If `put` or `rput` is used, the versions are copied from the source instance, but no versions are produced
* If `rput_leave` is used, the versions are linked by URL, and no files are copied to the target instance and no versions are produced
{% endhint %}

* type: `bool`
* default: `false`


### `--rename-versions`

Rename versions before uploading. This affects uploaded rights as well as file versions.

{% hint style="info" %}
The versions need to be given in the notation `"<cls>.<version>:<new version>"`, e.g. `"image.preview:640px"` would replace the `"preview"` version of class `image` to `640px`.

If the `<new version>` part is omitted, the version is removed.
{% endhint %}

* type: `string`


### `--max-parallel`

{% hint style="info" %}
This parameter is available in fylr from version **v6.18.0**.
{% endhint %}

Maximum numbers of parallel workers.

{% hint style="info" %}
`0` uses the number of available CPUs.

Defaults to `1` (only one parallel process).
{% endhint %}

{% hint style="warning" %}
This creates more load on the target system.
{% endhint %}

* type: `int`
* minimum: `0`
* default: `1`


### `--max-parallel-upload-files`

Maximum number of parallel uploads of original files and their versions. Defaults to `4` (`0` for bulk). The maximum is `10` (unlimited for bulk).

* type: `int`
* minimum: `0`
* maximum: `10`
* default: `4`


### `--timeout-min`

Timeout for connections to target in minutes.

{% hint style="info" %}
Increase this value if you notice timeouts or related network problems when uploading payloads or files to the target system.
{% endhint %}

* type: `int`
* minimum: `1`
* default: `10`


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

If the target instance uses OAuth2 for user authentication, this is the OAuth2 callback endpoint of the instance.

For fylr this is `<source url>/api/oauth2/token`.

* type: `string`


### `--verify`

{% hint style="info" %}
This parameter is available in fylr from version **v6.18.0**.
{% endhint %}

Set to `true` to verify payloads of an existing backup.

{% hint style="info" %}
This is the same what is done at the beginning if `--continue` is used.
{% endhint %}

* type: `bool`
* default: `false`


### `--insecure`

Set to `true` to skip the certificate check for the connection to the target instance.

{% hint style="warning" %}
Only use this option if you can trust the remote server!
{% endhint %}

* type: `bool`
* default: `false`


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


<!--

part above was auto generated

-->

