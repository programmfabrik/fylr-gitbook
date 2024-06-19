---
description: >-
  This page describes the process of creating a local backup of JSON payloads from a source instance
---

# Create payloads (`fylr backup`)

The `fylr backup` command performs `GET` requests to the API of the source instance, until all relevant base types and records are retrieved and stored in local files.

A basic backup command looks like this:

```
fylr backup \
  --server '<source-url>/api/v1/' \
  --login 'root' \
  --password '<cleartext>' \
  --dir '<instance folder>/' \
  --compression 9 \
  --purge
```

`--server`, `--login` and `--password` refer to the source server.

{% hint style="warning" %}
`--purge` deletes a backup in `--dir` in case there is already one. All existing files in this directory are deleted!
{% endhint %}

{% hint style="warning" %}
The backup over the API only stores the data in local files. The files are only referenced by URLs. Only during restoring, the files are loaded from the source instance. Until the restore is finished, the source instance still needs to be reachable.
{% endhint %}


## Parameters

This is a complete overview of the command line parameters (run `fylr backup -h`):

```
Usage: fylr backup

Backup ez5 or FYLR via API

Flags:
  -h, --help                       Show context-sensitive help.

  -d, --dir=STRING                 Target directory.
      --size=100                   Size of .json files.
      --compression=0              0: no compression, 1: speed, 9: best. Only valid for default backupformat.
      --continue                   Set to true, to continue. Only valid for default backupformat.
      --purge                      Set to true, to delete the target directory and all files before the backup.
      --all-versions               Set to true, to request all versions of an object.
      --include=STRING             Filter regexp to include objecttypes.
      --retry-max-count=10         Number of retries for failed requests with network problems.
      --retry-sleep-between=30     Wait time in seconds between retries for failed requests.
      --server=STRING              Source url (overwrites URL of source instance from config)
  -l, --login=STRING               If --server is set, use as login. Make sure to use the system root user to connect if used together with --purge.
  -p, --password=STRING            If --server is set, use as password
      --client-id=STRING           If --server is set, use as OAUTH2 client ID
      --client-secret=STRING       If --server is set, use as OAUTH2 client secret
      --client-token-url=STRING    If --server is set, use as OAUTH2 token url
  -v, --verbose                    Set to true, to show additional info.
  -n, --log-network                Set to true, to log all network traffic.
      --log=STRING                 Set output to logfile
      --limit=INT                  Limit records. Set to 0 for unlimited.
      --chunk=100                  chunk size for fetching/pushing data.
```


<!--

part below was auto generated
source: https://docs.google.com/spreadsheets/d/1JXKxGe6RaIGCpS8JY12qrnlESxDCm9dz8EmeeWmK57U/export?format=csv&gid=0
timestamp: 2024-06-19 13:57:33 (UTC)

-->



### `--dir`

Target folder for the backup files. If it does not exist, it will be created. If it exists, and `--purge` is used, an existing folder is deleted and created new.

* this parameter is **mandatory**!
* type: `string`


### `--server`

API Url of the source instance. The Url must include the API base endpoint, for fylr this is `<source url>/api/v1`.

* this parameter is **mandatory**!
* type: `string`


### `--login`

Username of the user in the source instance. It should be a user with root rights or sufficient read rights.

* this parameter is **mandatory**!
* type: `string`


### `--password`

Password of the user in the source instance.

* this parameter is **mandatory**!
* type: `string`


### `--purge`

Defines the mode of the backup (purge or continue).

If this is `true`, the complete backup starts from the beginning, and an existing backup folder with the same name is purged.

{% hint style="warning" %}
The parameters `--purge` and `--continue` are mutually exclusive. Not both can be `true`.

If the target folder already exists, this parameter (or `--continue`) must be set, otherwise the backup will fail.
{% endhint %}

* type: `bool`
* default: `false`


### `--continue`

Defines the mode of the backup (purge or continue).

If this is `true`, the backup continues from the last point in the `manifest.json` file, if a previous backup run was interrupted.

{% hint style="warning" %}
The parameters `--purge` and `--continue` are mutually exclusive. Not both can be `true`.

If the target folder already exists, this parameter (or `--purge`) must be set, otherwise the backup will fail.
{% endhint %}

* type: `bool`
* default: `false`


### `--size`

The target size for objects in payloads. The effective size of the generated payloads is limited by `--chunk`.

* type: `int`
* minimum: `1`
* maximum: `1000`
* default: `100`


### `--chunk`

The requested size for objects from the source instance. Can be used to control the size of the responses. It can be lowered if the requests cause timeouts or network problems.

* type: `int`
* minimum: `1`
* maximum: `1000`
* default: `100`


### `--limit`

Set this to a number bigger than `0` to limit the number of objects of each objecttype. This can be used to test or debug, and can be combined with `--include` to only backup a small sample of the source instance.

* type: `int`
* minimum: `0`
* default: `0`


### `--compression`

GZIP compression level.

If `0` is selected, there is no compression and the payloads are stored as `.json` files.
If a value bigger than `0` is selected, the payloads are stored as compressed `.json.gz` files.

* type: `int`
* minimum: `0`
* maximum: `9`
* default: `0`


### `--all-versions`

Set to true so that all history versions of the records are requested.

{% hint style="warning" %}
Not to be confused with asset versions (see parameters for `fylr restore`)!
{% endhint %}

* type: `bool`
* default: `false`


### `--base`

{% hint style="warning" %}
**Deprecated!** This parameter is removed in fylr in version **v6.10.0**.
{% endhint %}

Set to `false` to ignore the following base types in the backup: tags, messages, transitions, right presets for collections and objects, publishings and collections. Users, groups and pools are always included in the backup.

* type: `bool`
* default: `true`


### `--user`

{% hint style="warning" %}
**Deprecated!** This parameter is removed in fylr in version **v6.10.0**.
{% endhint %}

Set to `false` to ignore all user created objects in the backup (user objects means objects based on the datamodel which have been created by users). This means, that only base types are backupped.

* type: `bool`
* default: `true`


### `--include`

If this is a valid non empty regex string, only objecttypes are backupped where the internal objecttype name matches the regex.

* type: `string`


### `--retry-max-count`

If a request fails with one of the following HTTP status codes that indicate network problems, the request is repeated for a maximum number of times: `502`: Bad Gateway, `503`: Service Unavailable, `504`: Gateway Timeout

* type: `int`
* default: `10`


### `--retry-sleep-between`

Defines the waiting time in seconds between repeated failed requests.

* type: `int`
* default: `30`


### `--client-id`

If the source instance uses OAuth2 for user authentication, this is the configured Client ID.

* type: `string`


### `--client-secret`

If the source instance uses OAuth2 for user authentication, this is the configured Client Secret. Can be kept empty if the instance is public.

* type: `string`


### `--client-token-url`

If the source instance uses OAuth2 for user authentication, this is the OAuth2 callback endpoint of the instance. For fylr this is `<source url>/api/oauth2/token`.

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


<!--

part above was auto generated

-->

