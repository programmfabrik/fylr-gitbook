---
description: >-
  The "metadata" background-task module — re-apply a metadata mapping to the
  files of a set of records, in bulk and on a schedule.
---

# metadata

The **metadata** [background-task](../background-tasks.md) module re-reads the metadata embedded in a record's file (XMP / IPTC / EXIF) and writes it into the record's fields through a [metadata mapping](../../for-administrators/metadata-mapping.md) — across every record a search matches, on demand or on a schedule.

Use it to:

* apply a metadata mapping that has **changed** to records that were saved before the change;
* periodically **ingest** metadata from files that are updated outside fylr;
* **back-fill** fields from file metadata across an existing set of records.

## What it does per record

For each record the search returns, the task:

1. takes the file in the configured **Field for Files** (the preferred variant);
2. loads that file's metadata;
3. applies the selected **Metadata Mapping** (or the objecttype's standard image-import mapping), extracting values into the record's fields;
4. saves the record as a **new version** — replacing existing field values only when **Overwrite Values** is enabled;
5. optionally **sets or unsets tags** (the `set_unset_tags` step runs after the mapping).

Records whose file field holds no file, or for which no mapping applies, are skipped and noted in the [task log](../background-tasks.md#monitoring-and-logs).

## Task Parameters

Configure an existing metadata mapping to be applied on a configured search result.

| Parameter            | Description                                                                       |
| -------------------- | --------------------------------------------------------------------------------- |
| **Object Type**      | Apply only to the specified object type                                           |
| **Pool**             | Used when creating linked records with pool management during metadata mapping    |
| **Mask**             | Define which mask to use for the task                                             |
| **Field for Files**  | If multiple file fields exist, specify which one to use as source for your prompt |
| **Metadata Mapping** | Select the metadata mapping to be applied                                         |

The module `set_unset_tags` is supported after running the metadata task.

Beyond these, the [common task parameters](../background-tasks.md#task-parameters) apply — in particular **Overwrite Values** (replace non-empty fields; with it off, only empty fields are filled) and the search's **Incremental** option (process only records changed since the task's last run, and skip the ones this task itself edited — ideal for a recurring schedule).

## Permissions

Running the task needs the **Administration → Access Task Manager** system right, and the task's user needs the datamodel permissions to read the matched records and to save the changes.

## See also

* [Background tasks](../background-tasks.md) — creating, scheduling and monitoring tasks.
* [Metadata Mapping](../../for-administrators/metadata-mapping.md) — how a mapping extracts metadata from files.
