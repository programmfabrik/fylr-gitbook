---
description: >-
  This page describes the process of creating a local backup of JSON payloads from a source instance
---

# Create payloads (fylr backup)

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

{% hint style="warning" %}
Not all events will be migrated from easydb5 to fylr, because they have no purpose in fylr. Also, some events need to be changed.

For a complete overview, see [below](#migration-of-events-differences-between-easydb5-and-fylr)
{% endhint %}


## Parameters

This is a complete overview of the command line parameters (run `fylr backup -h`):

```
Usage: fylr backup [flags]

Backup ez5 or FYLR via API

Flags:

-h, --help                      Show context-sensitive help.
-v, --verbose                   Set to true, to show additional info.
-n, --log-network               Set to true, to log all network traffic.
    --server=STRING             Source url (overwrites URL of source instance from config)
-l, --login=STRING              If --server is set, use as login. Make sure to use the system root user to connect if used together with --purge.
-p, --password=STRING           If --server is set, use as password
    --client-id=""              If --server is set, use as OAUTH2 client ID
    --client-secret=""          If --server is set, use as OAUTH2 client secret
    --client-token-url=""       If --server is set, use as OAUTH2 token url
    --insecure                  Set to true, to not verify the server's certificate chain and host name
    --log=STRING                Set output to logfile
    --purge                     For backup: set to true, to purge the target directory. For restore: set to true, to purge the target and copy the datamodel. The current password of the user used for the login will be set for the system root user.
    --continue                  Set to true, to continue.
    --verify                    If set, verify payloads of an existing backup (same what --continue does at the beginning).
    --chunk-size=100            chunk size for fetching/pushing data.
    --include-events=""         Comma separated list of event types. Use "-" to skip backup/restoring of events. Empty string will backup/restore all known event types.
    --max-parallel=1            Maximum numbers of parallel workers. 0 uses the number of available CPUs. This creates more load on the source / target system. Defaults to "1" (only one parallel process).
-d, --dir=STRING                Target directory.
    --compression=0             0: no compression, 1: speed, 9: best.
    --all-versions              Set to true, to request all versions of an object.
    --include=""                Filter regexp to include objecttypes.
    --maximum-count=0           Limit records. Set to 0 for unlimited.
    --retry-max-count=10        Number of retries for failed requests with network problems.
    --retry-sleep-between=30    Wait time in seconds between retries for failed requests.
    --pretty                    Output pretty JSON.
```


<!--

part below was auto generated
source: https://docs.google.com/spreadsheets/d/1JXKxGe6RaIGCpS8JY12qrnlESxDCm9dz8EmeeWmK57U/export?format=csv&gid=0
timestamp: 2025-04-14 10:48:35 (UTC)

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

{% hint style="warning" %}
**Deprecated!** This parameter is removed in fylr in version **v6.18.0**.
{% endhint %}

The target size for objects in payloads. The effective size of the generated payloads is limited by `--chunk`.

* type: `int`
* minimum: `1`
* maximum: `1000`
* default: `100`

### `--chunk`

{% hint style="warning" %}
**Deprecated!** This parameter is removed in fylr in version **v6.18.0**.
{% endhint %}

The requested size for objects from the source instance. Can be used to control the size of the responses. It can be lowered if the requests cause timeouts or network problems.

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

The requested size for objects from the source instance. Can be used to control the size of the responses. It can be lowered if the requests cause timeouts or network problems.

* type: `int`
* minimum: `1`
* maximum: `1000`
* default: `100`

### `--limit`

{% hint style="warning" %}
**Deprecated!** This parameter is removed in fylr in version **v6.18.0**.
{% endhint %}

Set this to a number bigger than `0` to limit the number of objects of each objecttype. This can be used to test or debug, and can be combined with `--include` to only backup a small sample of the source instance.

{% hint style="warning" %}
This parameter was renamed to `--max-count`
{% endhint %}

* type: `int`
* minimum: `0`
* default: `0`

### `--max-count`

{% hint style="info" %}
This parameter is available in fylr from version **v6.18.0**.
{% endhint %}

Set this to a number bigger than `0` to limit the number of objects of each objecttype. This can be used to test or debug, and can be combined with `--include` to only backup a small sample of the source instance.

* type: `int`
* minimum: `0`
* default: `0`

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
This creates more load on the source system.
{% endhint %}

* type: `int`
* minimum: `0`
* default: `1`

### `--compression`

GZIP compression level.

If `0` is selected, there is no compression and the payloads are stored as `.json` files. If a value bigger than `0` is selected, the payloads are stored as compressed `.json.gz` files.

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

### `--include`

If this is a valid non empty regex string, only objecttypes are backupped where the internal objecttype name matches the regex.

* type: `string`

### `--include-events`

Comma separated list of event types.

{% hint style="info" %}
Use `--include-events=-` to skip backup of events.

If this parameter is unset, all events are backupped
{% endhint %}

{% hint style="warning" %}
Specific event types, which are irrelevant for the migration, are never in the backup, even if they are specifically requested.

For now, this includes `OBJECT_INDEX`, `SESSION_INVALID`, `FRONTEND_ERROR` and `COLLECTION_OWNER_RIGHTS_ERROR`, but this might be extended in the future.
{% endhint %}

* type: `string`
* default: `""`

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

### `--insecure`

Set to `true` to skip the certificate check for the connection to the source instance.

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

### `--pretty`

{% hint style="info" %}
This parameter is available in fylr from version **v6.17.0**.
{% endhint %}

Set to `true` to save the data in a prettified JSON.

* type: `bool`
* default: `false`


<!--

part above was auto generated

-->


## Migration of events: differences between easydb5 and fylr

Events of the following types are either not migrated at all, or they will automatically be changed to be imported into fylr.

All event types which are not mentioned here, will be migrated without any type changes.

The event info block will be migrated without any changes. IDs which relate to objects, files, etc., and which are not part of the event info block, are automatically replaced during the restore process.


<!--

part below was auto generated
source: https://docs.google.com/spreadsheets/d/1FkbU1t-WuDQ6YSRKUu2VYR8Hdg3x6ZPBntFFmI4VUM4/export?format=csv&gid=0
timestamp: 2025-04-14 10:48:35 (UTC)

-->



### Event Type `API_CALL`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `API_PROGRESS`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `COLLECTION_OWNER_RIGHTS_ERROR`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `CUSTOM_TYPE_UPDATER_START`

The event type will be changed from `CUSTOM_TYPE_UPDATER_START` to `CUSTOM_DATA_TYPE_UPDATER` in fylr.



### Event Type `CUSTOM_TYPE_UPDATER_RESPONSE`

The event type will be changed from `CUSTOM_TYPE_UPDATER_RESPONSE` to `CUSTOM_DATA_TYPE_UPDATER` in fylr.



### Event Type `CUSTOM_TYPE_UPDATER_RESPONSE_ERROR`

The event type will be changed from `CUSTOM_TYPE_UPDATER_RESPONSE_ERROR` to `CUSTOM_DATA_TYPE_UPDATER_ERROR` in fylr.



### Event Type `CUSTOM_TYPE_UPDATER_RESPONSE_FAILED`

The event type will be changed from `CUSTOM_TYPE_UPDATER_RESPONSE_FAILED` to `CUSTOM_DATA_TYPE_UPDATER_ERROR` in fylr.



### Event Type `SCHEMA_COMMIT`

The event type will be changed from `SCHEMA_COMMIT` to `DATAMODEL_COMMIT` in fylr.



### Event Type `EXPORT_ASSET`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `EXPORT_OBJECT`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `ASSET_EXPORT_TRANSPORT_DOWNLOAD`

The event type will be changed from `ASSET_EXPORT_TRANSPORT_DOWNLOAD` to `EXPORT_TRANSPORT` in fylr.



### Event Type `EXPORT_STOPPED`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `DOWNLOAD_EXPORT`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `ASSET_DOWNLOAD`

The event type will be changed from `ASSET_DOWNLOAD` to `FILE_DOWNLOAD` in fylr.

The basetype of this event will be changed from `asset` to `file` in fylr.



### Event Type `ASSET_EXPORT_DOWNLOAD`

The event type will be changed from `ASSET_EXPORT_DOWNLOAD` to `FILE_DOWNLOAD` in fylr.

The basetype of this event will be changed from `asset` to `file` in fylr.



### Event Type `SUGGEST_INDEX_DONE`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `SUGGEST_INDEX_FAILED`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `JANITOR_SESSION_PURGE`

The event type will be changed from `JANITOR_SESSION_PURGE` to `JANITOR` in fylr.



### Event Type `MAPPING_DELETE`

The basetype of this event will be set to `mapping` in fylr. In easydb5, there was no basetype for this event type.



### Event Type `MAPPING_INSERT`

The basetype of this event will be set to `mapping` in fylr. In easydb5, there was no basetype for this event type.



### Event Type `MAPPING_UPDATE`

The basetype of this event will be set to `mapping` in fylr. In easydb5, there was no basetype for this event type.



### Event Type `RESOURCE_NOT_AVAILABLE`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `SERVER_START`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `SERVER_SHUTDOWN`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `SESSION_INVALID`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `SUGGEST_INDEX_DONE`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `SUGGEST_INDEX_FAILED`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `USER_CREATED`

The event type will be changed from `USER_CREATED` to `USER_INSERT` in fylr.

The basetype of this event will be set to `user` in fylr. In easydb5, there was no basetype for this event type.



### Event Type `USER_LOGIN`

The basetype of this event will be set to `user` in fylr. In easydb5, there was no basetype for this event type.



### Event Type `USER_LOGOUT`

The basetype of this event will be set to `user` in fylr. In easydb5, there was no basetype for this event type.



### Event Type `LOGIN_FAILED`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `USER_ACCEPTED_MESSAGE`

{% hint style="warning" %}
Events with this type can not be migrated to fylr at all!
{% endhint %}



### Event Type `WEBHOOK_OK`

The event type will be changed from `WEBHOOK_OK` to `WEBHOOK` in fylr.



<!--

part above was auto generated

-->

