---
description: This section describes the migration process between two instances using the fylr migration tool
---

# Migration Tool

{% hint style="info" %}
This page describes the complete migration between productive instances.

For using SQL dumps as backups for debugging purposes, please see [Backups & Restore (SQL)](backup.md) instead.
{% endhint %}

This page describes of the **fylr migration tool**, which is an internal part of the **fylr** binary and can be used by calling sub commands from the command line.

The migration consists of two parts: **[backup](backup.md)** and **[restore](restore.md)**. A complete migration is done by loading a backup from a source instance (**easydb5** or **fylr**) using the `fylr backup` command, and later restoring it to a target instance (**fylr** only) using the `fylr restore` command.

The migration tools use the API store JSON files with payloads. The payloads contain basetypes and records stored in a way that the content can be used as the body of POST requests to the API of the target instance.

A central element of each backup is the `manifest.json` file, which contains information about the source instance. It also contains filenames (relative paths) to datamodel and base configuration files, and most important, the list of all payloads in a specific order.

The JSON files in the backup can be used for multiple restore runs, against multiple target instances.

## Requirements

`backup` and `restore` are sub commands of `fylr`. Make sure to always use the latest **fylr** version.

For all following descriptions of commands, `fylr` refers to a local binary.
