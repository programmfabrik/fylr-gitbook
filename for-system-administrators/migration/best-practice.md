---
description: >-
  This page gives an overview of best practice, use cases and recommended parameters for the backup and restore tools
---

# Best Practice

Here we describe multiple use cases and scenarios for the backup and restore tools. We want to provide examples and recommended parameters settings. This is based on experience with different migrations. Since the backup and restore processes are always different and are depending on the size and complexity of the data, and also on the technical limitations of the source and target instances, the recommended parameters are not definitive.

The following use cases and examples are a starting point to find the best settings for each migration. The most important distinction is between testing a migration and performing a full migration that is intended for productive use.

Test migrations are done to prepare for a final productive migration. The focus is on the content of the data and the datamodel. They should be fast, and so the actual files in the records are not copied. For most test migrations, it is not necessary to include any files, but it is enough to just use small preview images. This makes the restore process faster and also saves disk space.

{% hint style="warning" %}
The source instance should not be changed or even disconnected during test migrations!
{% endhint %}

In a backup no actual files are included, but instead the URLs to files are part of the records and are referenced and used during restoring. Until the final migration is finished and all files and their versions have been copied to the target instance, these URLs need to be reachable, otherwise no files can be copied and will be missing!

Productive migrations include the complete data, as well as all files. The files are then copied to the target system, and are then indpendent from the source system. Make sure there is enough disk space on the target system to store all files!

* For *test* migrations:
  * [Restoring without any files](#restoring-without-any-files)
  * [Restoring with preview images](#restoring-with-preview-images)
  * [Restoring with remote images (no copying of files)](#restoring-with-remote-images-no-copying-of-files)
  * [Backup of a subset of records](#backup-of-a-subset-of-records)
  * [Restoring of a subset of records](#restoring-of-a-subset-of-records)

* For *productive* migrations:
  * [Backup and restoring including user passwords](#backup-and-restoring-including-user-passwords)
  * [Restoring with files (all files are copied)](#restoring-with-files-all-files-are-copied)
<!--
  * [Full migration](#full-migration)
-->

## Restoring without any files

This is the fastest migration, all files in all basetypes and records are skipped and will not be included in the target instance. Only the data will be imported in the target instance. This saves time during the upload, and also there are no file conversions happening in the background after the restore process is done.

This is achieved by simply **not setting** the [`--file-api`](restore.md#file-api) parameter in `fylr restore`. Then the empty default is used, which means that no files are imported.

All other file related parameters can just be ignored in this case, since they are obsolete if no files are uploaded. This includes `--file-version`, `--upload-versions`, `--rename-versions` or `--max-parallel-upload-files`.

The minimal command for restoring payloads from `instance folder` into the remote instance `fylr url` (after it has been purged) is:

```
fylr restore \
  --server '<fylr url>/api/v1' \
  --login 'root'
  --password '<cleartext>' \
  --client-id '<client id>' \
  --client-secret '<client secret>' \
  --client-token-url '<fylr url>/api/oauth2/token' \
  --manifest '<instance folder>/manifest.json' \
  --purge
```

## Restoring with remote images (no copying of files)

If you want to see files in the target instance during testing, but don't want to copy any files yet, **fylr** can store the URL to the files. In the frontend these files are then loaded directly from the source instance and are displayed.

This is done by setting the `--file-api` parameter to `rput_leave`. This means that the files will be "left" in the source instance (instead of copying actual data), and are only referenced by their URL.

<!--
todo

* werden bei rput_leave versionen berechnet?
* hat upload-versions irgendeinen einfluss?

-->


```
fylr restore \
  --server '<fylr url>/api/v1' \
  --login 'root'
  --password '<cleartext>' \
  --client-id '<client id>' \
  --client-secret '<client secret>' \
  --client-token-url '<fylr url>/api/oauth2/token' \
  --manifest '<instance folder>/manifest.json' \
  --file-api rput_leave \
  --purge
```


## Restoring with preview images

If files should actually be stored in the target instance, this is done by setting the [`--file-api`](restore.md#file-api) parameter to `put` or `rput`.

If **`put`** is used the files are loaded by the `fylr restore` tool and then uploaded to the target instance.

With **`rput`** the URL to a file is sent to the target instance, and the target **fylr** uses the URL to load the file from the source instance in the background. This is faster and also recommended generally.

By default the uploaded file version is the `"original"` version of the file. From this original file, other file versions (like `"preview"`) are calculated in the target instance. Depending on the size of the original files, the upload time and the conversion time that follows, can be quite long.

This time can be saved by using another file version that has a smaller resolution (for images) or which is a preview image for other files. This smaller file will then be used instead of the original file, so the upload and conversion speed is increased and the total restore time can be significantly lower.

```
fylr restore \
  --server '<fylr url>/api/v1' \
  --login 'root'
  --password '<cleartext>' \
  --client-id '<client id>' \
  --client-secret '<client secret>' \
  --client-token-url '<fylr url>/api/oauth2/token' \
  --manifest '<instance folder>/manifest.json' \
  --file-api rput \
  --file-version preview \
  --purge
```

## Backup of a subset of records

For productive migrations, the full set of records from a source instance is stored in the backup files. The amount of records that are loaded from the source can be limited to a specific limit per objecttype. Also the requested records can be filtered by the name of the objecttype.

The [`--limit`](backup.md#limit) parameter can be used to set the upper limit of records that are requested per objecttype. Set a number bigger than `0` to limit the records. By default the limit is `0` which means all records are requested. The limit is applied to all objecttypes.

To only backup a set of objecttypes with the [`--include`](backup.md#include) parameter a regular expression can be passed. Only records where the name of the objecttype matches the regex are requested, other objecttypes are ignored. By default this parameter is an empty string, which means it is ignored.


<!--
todo clarify:

* does --include only apply to objecttypes that are in search?

-->


`--limit` and `--include` can be combined to control the content and amount of a test backup. For example, if only a maximum of 100 records of objecttypes `asset` and `document` should be included in the backup, the command would look like this:

```
fylr backup \
  --server '<source-url>/api/v1/' \
  --login 'root' \
  --password '<cleartext>' \
  --dir '<instance folder>/' \
  --limit 300 \
  --include '^asset|document$' \
  --purge
```

{% hint style="warning" %}
Any non-empty string is used as a regular expression. There is no validation before. This means it is possible that the regular expression is invalid, or that no records match at all.
{% endhint %}

## Restoring of a subset of records

To only restore a part of existing payloads, the number of records which are uploaded to the target can also get an upper limit. Use the [`--limit`](restore.md#limit) parameter to set number bigger than `0`. By default this value is `0` which means all records are restored.

To only restore a maximum of 100 records of each objecttype, use a command like this:

```
fylr restore \
  --server '<fylr url>/api/v1' \
  --login 'root'
  --password '<cleartext>' \
  --client-id '<client id>' \
  --client-secret '<client secret>' \
  --client-token-url '<fylr url>/api/oauth2/token' \
  --manifest '<instance folder>/manifest.json' \
  --limit 100 \
  --purge
```

## Backup and restoring including user passwords

If you want to perform a migration including the user password (saved as hash values in the payloads), this needs specific parameters to enable this feature, as well as some preparation in the source instance.

If the source instance is an easydb5, the API will not include any user passwords, if this is not explicitly enabled. On how to configure this, see the [easydb5 documentation](https://docs.easydb.de/en/technical/api/user/#returning-password-hashes). During the backup, if for any user there is a password hash, the backup tool will store the flag `"has_passwords": true` in the `manifest.json` file. This value is later checked by the restore tool. If you plan to restore with passwords, make sure that the easydb5 actually returns password hashes in user payloads.

The restore tool will **not** upload password hashes by default. To enable this feature, set the [`--include-password`](restore.md#include-password) parameter to `true`.

{% hint style="warning" %}
If you set `--include-password true`, and in the manifest file the flag `"has_passwords"` is `false`, the restore tool will fail with an error message, which includes information about the missing password hashes.
{% endhint %}

The check in the restore tool is a helper to avoid problems with missing passwords after a productive migration. The check makes sure that the user payloads have not been loaded without passwords undetected.

```
fylr restore \
  --server '<fylr url>/api/v1' \
  --login 'root'
  --password '<cleartext>' \
  --client-id '<client id>' \
  --client-secret '<client secret>' \
  --client-token-url '<fylr url>/api/oauth2/token' \
  --manifest '<instance folder>/manifest.json' \
  --include-password \
  --purge
```

## Restoring with files (all files and versions are copied)

Uploading the original file version and converting it to the different configured file versions after the migration, which can take a lot of time, it is possible to copy the file versions as well. File versions that already have been produced by the source instance can be uploaded to the target system and be used directly. This is applied to all versions with the same name in the source and target instance.

This is enabled by setting the [`--upload-versions`](restore.md#upload-versions) parameter to `true`. The file versions are uploaded by name and are stored in the target instance. They are uploaded in the same way as the original files. The upload method that has been defined with `--file-api` is used for all files and versions.

{% hint style="warning" %}
File versions are identified by the name. Since the file versions are depending on the configuration of each instance, only versions with the same name are copied.
{% endhint %}

{% hint style="warning" %}
Before a migration, also check that versions with the same name are actually configured in the same way in both instances. There is no validation, the restore tool will upload versions by name to the target instance, and the target fylr will store the files without checking if they actually match the configuration.
{% endhint %}


```
fylr restore \
  --server '<fylr url>/api/v1' \
  --login 'root'
  --password '<cleartext>' \
  --client-id '<client id>' \
  --client-secret '<client secret>' \
  --client-token-url '<fylr url>/api/oauth2/token' \
  --manifest '<instance folder>/manifest.json' \
  --file-api rput \
  --file-version original \
  --upload-versions \
  --rename-versions 'video.full_hd:1920p,image.small_obsolete:' \
  --purge
```

### Renaming file versions

As described above, versions are identified and shared between instances only by their name. Since the name is an arbitry identifier, it is possible that the configuration between two instances is different. Two versions might have the same configuration and would produce the same file, but have a different name. If you still want to use these file versions from the source instance, the restore can replace the version name before uploading the file. The target fylr instance will store the file under the new version name.

The [`--rename-versions`](restore.md#rename-versions) parameter can be used to define one or more renamings of versions, also the upload of specific versions can be skipped. The parameter is a string with a specific format.

The structure of the parameter is the following:

One or more terms in the form of `<cls>.<version>:<new version>`. The file version of the file class `<cls>`, which is named `<version>` in the source instance, is renamed to `<new version>` in the target instance

For example: in the source, there is the `video` class version `full_hd`, which should be used in the target fylr as well. But in the target instance, the same file version is configured under the name `1920p`. So the term for this is `video.full_hd:1920p`.

Also there is the term to ignore a file version in the from `<cls>.<version>:`. Since `<new version>` is empty, the restore tool knows to skip this version completly. To ignore an `image` class version with the name `small_obsolete`, write a term `image.small_obsolete:`.

These terms are comma separated. The complete parameter for this example would be:

```
--rename-versions 'video.full_hd:1920p,image.small_obsolete:'
```


<!-- ## Full migration -->

<!-- todo -->


<!-- # Known problems and solutions -->

<!-- todo -->
