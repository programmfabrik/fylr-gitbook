---
description: >-
  From 6.36 fylr can keep its search index itself, in a directory of its
  server, instead of in OpenSearch or Elasticsearch.
---

# Search without OpenSearch

From **6.36**, fylr can keep its search index itself. With the address `native:<directory>` in `fylr.elastic.addresses`, fylr stores the index in that directory and answers its searches inside the fylr process: no OpenSearch or Elasticsearch has to be installed or run. Search, the API and the web frontend work the same either way.

```yaml
fylr+:
  elastic+:
    addresses:
      - "native:/fylr/files/search"
```

fylr creates the directory. A relative directory is relative to the directory of the yml file that sets it.

## What it rules out

* **One fylr per database.** The index is kept by one fylr process. A second fylr on the same database refuses to start (`For a search index in "native:", only a single backend can be used`). For several fylr servers on one database, behind a load balancer or in Kubernetes, use OpenSearch. Execservers on other machines are not affected.
* **One fylr per directory.** fylr locks the directory, another fylr pointed at it does not start (`the search index in … is in use by another fylr`). Keep the directory on a local disk of the fylr server, not on a network share.
* **No OpenSearch API.** Tools that read OpenSearch directly, like OpenSearch Dashboards or scripts on its indices, have nothing to connect to. Plugins are not affected, they search through fylr's API.
* `username`, `password` and `startupConnectTimeSec` of `fylr.elastic` do not apply.
* **A custom `fylr.elastic.settings` file** is read, but only the tokenizers and filters of the shipped `resources/indexer/index_settings.json` are known. Others do nothing, an unknown tokenizer splits a text into words of letters and digits. Compare a few searches before you switch an instance that has settings of its own.

## Linux with docker compose

The directory needs a volume of its own, or it is lost whenever the fylr container is recreated, and fylr finds nothing until a re-index. In `/srv/fylr` (see [Linux](linux-docker-compose/README.md)):

```bash
mkdir search
chown 1000 search
```

In the `fylr` service of `docker-compose.yml`:

```yaml
    volumes:
      - "/srv/fylr/search:/fylr/files/search"
```

The `opensearch` service and its entry in `depends_on` can go.

## Windows

`native:` works on Windows too, with a Windows path in single quotes:

```yaml
fylr+:
  elastic+:
    addresses:
      - 'native:C:\fylr\search'
```

The OpenSearch steps of [Windows](windows.md#opensearch) are not needed then.

## Switching an instance

The index is built from the database. To move an instance from OpenSearch to native, or back:

1. Set the address in `fylr.yml` and restart fylr. It creates an empty index: the instance runs, but every search finds nothing.
2. Start a re-index: **Re-index** on `/inspect/system/` as root, see [System](../inspect/system.md#re-index). Searches find nothing until it is done, then everything. With `blockFrontend` the users get the `reindex` status instead of empty results.
3. Delete the old index yourself. fylr does not delete it where it no longer looks: on OpenSearch these are the indices `<fylr.name>-<uuid>-…` of the instance, on native the directory.

A re-index takes about as long as with OpenSearch: in a test with 1.1 million objects, 44 minutes against 48 minutes with OpenSearch on the same machine.

## Disk, memory and backups

* The index takes about as much disk as OpenSearch's for the same objects, 8.9 GB against 9.5 GB in the test above. A re-index builds the new index next to the old one, which is deleted 30 seconds after the switch: leave room for twice the index.
* fylr's memory grows with the index: the values it sorts and aggregates on stay in memory, the rest is read from the files when needed.
* A backup does not need the index, it can always be rebuilt from the database: `fylr restore` re-indexes when it is done.
