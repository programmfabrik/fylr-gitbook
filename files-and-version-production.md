---
description: >-
  This page gives a overview over the file handling and file version production
  in fylr. Different file states and actions are explained in a how-to for the
  /inspect/files page.
---

# Files and version production

{% hint style="warning" %}
This page is a work in progress and not complete.
{% endhint %}

## `/inspect/files` page


Open `<fylr url>/inspect/files`. The page shows a list of all files and their children. For each original file which has been uploaded, or is inserted via URL, children are calculated in the background. The number of children depends on recipes which are triggered by file types and other file meta data. Each original and child file has different states which show what is done in the background, and also give information about errors.


## File States

Automatic changes between different states, which are done by internal workflows, are done in order. Internal states ("Status") are grouped into API states ("Status API").

<table>
    <thead>
        <tr>
            <th align="center">Step</th>
            <th>Status</th>
            <th>Status API</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">1</td>
            <td>
                <code>pending</code>
            </td>
            <td>
                <code>pending</code>
            </td>
            <td>The file is in the queue, but has not yet been picked up by any file worker</td>
        </tr>
        <tr>
            <td align="center">2</td>
            <td>
                <code>processing</code>
            </td>
            <td>
                <code>processing</code>
            </td>
            <td>A worker is processing the file.</td>
        </tr>
        <tr>
            <td align="center">2</td>
            <td>
                <code>pending_produce_internal</code>
            </td>
            <td>
                <code>processing</code>
            </td>
            <td><!-- todo --></td>
        </tr>
        <tr>
            <td align="center">2</td>
            <td>
                <code>pending_manual_produce_internal</code>
            </td>
            <td>
                <code>processing</code>
            </td>
            <td><!-- todo --></td>
        </tr>
        <tr>
            <td align="center">2</td>
            <td>
                <code>pending_original_produce_internal</code>
            </td>
            <td>
                <code>processing</code>
            </td>
            <td><!-- todo --></td>
        </tr>
        <tr>
            <td align="center">2</td>
            <td>
                <code>pending_metadata_internal</code>
            </td>
            <td>
                <code>processing</code>
            </td>
            <td><!-- todo --></td>
        </tr>
        <tr>
            <td align="center">3</td>
            <td>
                <code>sync</code>
            </td>
            <td>
                <code>sync</code>
            </td>
            <td>
                <p>Processing of the file in file workers is done. Further information are still calculated for the database.</p>
                <p>Files in this state can be exported.</p>
            </td>
        </tr>
        <tr>
            <td align="center">3</td>
            <td>
                <code>pending_copy_internal</code>
            </td>
            <td>
                <code>sync</code>
            </td>
            <td><!-- todo --></td>
        </tr>
        <tr>
            <td align="center">3</td>
            <td>
                <code>pending_move_internal</code>
            </td>
            <td>
                <code>sync</code>
            </td>
            <td><!-- todo --></td>
        </tr>
        <tr>
            <td align="center">3</td>
            <td>
                <code>pending_checksum</code>
            </td>
            <td>
                <code>sync</code>
            </td>
            <td>Files in this state can be exported.</td>
        </tr>
        <tr>
            <td align="center">4</td>
            <td>
                <code>done</code>
            </td>
            <td>
                <code>done</code>
            </td>
            <td>
                <p>The file and all children have been successfully converted.</p>
                <p>Files in this state can be exported.</p>
            </td>
        </tr>
        <tr>
            <td align="center">4</td>
            <td>
                <code>error</code>
            </td>
            <td>
                <code>failed</code>
            </td>
            <td>There was an error during conversion. See <a data-mention href="files-and-version-production.md#errors-and-solutions">#errors-and-solutions</a> or more information and possible solutions.</td>
        </tr>
    </tbody>
</table>


## File Actions

The following actions can be manually performed on files. Each action changes the state of the file. Depending on the current state of a file, not all actions can be performed, and not all states can be reached.

To perform an action, select files and optionally their children, and select one of these actions from the dropdown menu:

### Resync

Internal name: `resync`

Resync originals and reproduce versions.

If the file is an original, resync will update automatically produced versions as necessary. File metadata is calculated only if it hasn't been produced yet. It does not repair versions in state `error`. Only versions in state `done` are considered for reproducing.

If the file is a version, it is rendered again, even if it is in state `error` already.

Resync on the entire search result is only allowed with an active filter and no parents and children selected.

### Resync with metadata

Internal name: `resync_force_metadata`

Resync files with metadata. This works like "Resync", but forces the calculation of the metadata. This involves copying the file into the exec server directory which is slower than using the normal "Resync" action.

### Resync with metadata (incl. request only)

Internal name: `resync_force_metadata_incl_request_only`

Resync files with metadata including request only recipes. This works like "Resync" but includes metadata recipes which are marked as request only.

### Copy/Move & Produce

Internal name: `copy_move_produce`

Files which are stored remotely ("Remote Url" is set), can be copied into fylr storage using this action.

The "Produce Versions" flag is set and existing versions are deleted. With that, fylr starts rendering versions as defined in the produce configuration. This action can only be applied to originals.

### Copy/Move

Internal name: `copy_move`

Files which are stored remotely ("Remote Url" is set), can be copied into fylr storage using this action. This action works like `copy_move_produce` but without producing versions.

This action can be applied to versions as well as to originals.

### Produce Versions

Internal name: `produce_versions`

Remove all children of an original and resync to produce auto-generated versions.

Originals will be set to produce versions. This action works for all originals which are in a fylr storage location and have metadata. All versions (auto generated and not) will be deleted prior to the action.

If originals or versions are in the file queue, this action cannot be performed.

### Check file checksums

Internal name: `checksum`

Checks the integrity of files that have been copied during a [restore](/for-system-administrators/migration/restore.md) process. It parses the file reference which can include a `sha224` or `sha256` checksum that was read from the source instance, and compares it to the checksum of the local file.


## File Queue

Open `<fylr url>/inspect/system/queues/?queue=file`. The table shows queued file jobs as well as file jobs which are currently worked on. Each job is defined by a file in a specific state and the current action.

During the background processing of all file jobs, the queue can grow. This is because original files will produce a number of versions (depending on the recipe). Each new version creates new jobs, so once a single original file job is picked up by a file worker, for each file version which is to be produced, the queue will grow by the number of new jobs. The total number of jobs in the queue is always fluctuating, but should genereally get lower over time.


## File Locations

fylr can copy files to the local file system (location: `local`), or display files which are only stored with a URL (location: `remote`), and are then linked using this URL. Files which are on `remote` can be copied to `local` using the actions [`copy_move`](#copymove) or [`copy_move_produce`](#copymove--produce). The location of the file will then be changed. It is not possible to change a file location from `local` to `remote`.

In the file overview in the `/inspect/files` page, the files can be filtered by different locations:

* `local (without from remote)`:
  * show all files which only are stored locally and which do not have been copied from a remote URL
* `local (from remote)`:
  * show all files which are stored locally and which have been copied from a remote URL
* `remote`:
  * show all files which are not stored locally and which are only linked by a remote URL
* configured local locations:
  * filter by specific `local` locations, they are defined in the [Location Manager](/for-administrators/location-manager.md)


## Errors and solutions

{% hint style="warning" %}
This block is a work in progress and not yet complete.
{% endhint %}
