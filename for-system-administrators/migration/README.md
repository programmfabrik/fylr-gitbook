---
description: This section describes the migration process using the API.
---

# Migration

The migration is performed by loading a backup from a source instance (**easydb5** or **fylr**) using the `fylr backup` command and later restoring it to a target instance (**fylr** only) using the `fylr restore` command.

The migration is based on JSON payloads, which contain basetypes and records stored in a way that the payloads can be used as the body of POST requests to the API of the target instance.

A central element of each backup is the `manifest.json` file, which contains information about the source instance. It also contains filenames (relative paths) to datamodel and base configuration files, and most important, the list of all payloads in a specific order.

The JSON files in the backup can later be used for multiple restore runs, against multiple target instances.

## Requirements

`backup` and `restore` are sub commands of `fylr`. Make sure to always use the latest **fylr** version.

For all following descriptions of commands, `fylr` refers to a local binary.
