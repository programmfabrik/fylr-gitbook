---
description: Running fylr on CockroachDB instead of PostgreSQL
---

# CockroachDB

From version 6.36.0 fylr runs on CockroachDB as well as on [PostgreSQL](postgresql-versions.md). fylr is tested with CockroachDB 26.3 on a cluster of three nodes.

## Configuration

The driver is `cockroach`, the `dsn` is a connection string like the one for PostgreSQL, see [fylr.example.yml](configuration/fylr.example.yml.md):

```yaml
fylr:
  db:
    driver: cockroach
    dsn: "host=localhost port=26257 user=fylr password=fylr dbname=fylr sslmode=verify-full sslrootcert=certs/ca.crt"
```

The user owns the database: fylr creates and changes its tables. fylr does not start when the server is not of the kind the driver names, a CockroachDB server configured as `postgres` or a PostgreSQL server configured as `cockroach`.

## Isolation level

fylr runs its transactions at READ COMMITTED. On CockroachDB that needs the cluster setting `sql.txn.read_committed_isolation.enabled`, which CockroachDB 26.3 has on by default. With the setting off, CockroachDB runs the transactions as SERIALIZABLE and fylr does not start:

```
CockroachDB runs fylr's transactions at serializable, fylr needs read committed: enable the cluster setting sql.txn.read_committed_isolation.enabled
```

The session settings fylr needs it sets on every connection itself: the isolation level, a cached sequence for each new SERIAL column, schema changes inside fylr's transactions and new tables without `schema_locked`. Before a migration fylr unlocks the tables that have `schema_locked` set.

## Purges

A purge drops and creates every table. On an instance that is purged often, a test instance for example, these cluster settings make dropped tables and finished schema jobs go quickly:

```sql
ALTER RANGE default CONFIGURE ZONE USING gc.ttlseconds = 600;
SET CLUSTER SETTING jobs.retention_time = '15s';
SET CLUSTER SETTING jobs.registry.interval.gc = '30s';
SET CLUSTER SETTING kv.range_merge.queue_interval = '50ms';
SET CLUSTER SETTING kv.range_split.by_load_merge_delay = '5s';
SET CLUSTER SETTING sql.catalog.descriptor_wait_for_initial_version.enabled = false;
```

Run each statement on its own: CockroachDB refuses `SET CLUSTER SETTING` inside a transaction. With CockroachDB's defaults a purge can wait minutes for the descriptors of the dropped tables.

## Differences to PostgreSQL

* **Server-wide locks** (configuration saves, indexing, WebDAV locks) are rows of the table `dblock` with a lease, which the holder renews every 5 seconds. A lock of a fylr process that ended without releasing it is free after at most 15 seconds.
* **Event stream**: fylr reads new events from the database twice a second and at once when it has committed events itself. An event whose transaction commits after an event with a higher id was sent is missing from the stream; `/api/v1/event/poll` returns it.
* **Backups** of the [Backup Manager](../for-administrators/backup-manager.md) read every table at one fixed timestamp.
