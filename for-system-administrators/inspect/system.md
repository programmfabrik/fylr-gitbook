---
description: >-
  The /inspect/system dashboard — re-index and purge the instance, and inspect
  the janitor, queues, execserver, backups, locations and runtime status.
---

# System

The **System** page (`/inspect/system/`) is the maintenance dashboard for a running instance. It surfaces the runtime state and hosts the two most consequential actions — **re-index** and **purge**.

{% hint style="danger" %}
Re-index and purge are **instance-wide** and, on the backend port, **unauthenticated**. Keep the backend port on a private network. In the browser (webapp port) they require `system.root`.
{% endhint %}

## Actions

### Re-index

Rebuilds the search index for every object from the database. Reachable as `GET /inspect/system/?reindex=1`; add `&blockFrontend=1` to put the instance into the `reindex` status — only `/inspect/` stays reachable — until the new index is built and switched in. Use it after a change that alters what is indexed (the release notes call these out) or to recover a corrupted index.

### Purge

`POST /inspect/system/purge` **permanently wipes all data** — objects, datamodel, users, configuration, everything. The button appears only when `fylr.allowpurge` and the base-config purge flag are both set, but the endpoint itself has no auth on the backend port. There is no undo.

## Status & subpages

The dashboard also links the read-only runtime views:

| Subpage | Shows |
| --- | --- |
| `system/janitor/` | the clean-up janitor's state — file deletion, trash draining, idle-user archiving |
| `system/queues/` | the file and index job queues |
| `system/execserver/` | the connected execservers and their services |
| `system/locations/` | the storage locations and their status |
| `system/backups/` | the on-disk backups |
| `system/console/` (+ `/stream`) | a live server-log console |
| `system/status/` | server statistics |

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [Files and version production](../files-and-version-production.md) — the file queues in depth.
* [Backups & Restore](../backup.md).
