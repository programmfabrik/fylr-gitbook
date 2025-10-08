---
description: Supported major versions and upgrading between versions
---

# PostgreSQL versions

## Supported PostgreSQL versions

fylr is tested with PostgreSQL 15, 16 and 17.

The newest recommended version is part of our [installation documentation](installation/linux-docker-compose.md), in [docker-compose.yml](https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/docker-compose.yml)

## Upgrade between major versions

1. Make sure you have enough storage for the old postgres data directory and a copy for the new postgres version, e.g. compare \
   `du -sh /srv/fylr/postgres/pgdata` to \
   `df -h /srv/fylr/postgres/pgdata`. \
   Also consider the needed storage for another dump, by looking at the size at your currently saved dumps, e.g. `ls -lh /srv/fylr/sqlbackups/`.
2. Stop fylr, e.g. `docker compose stop fylr`.
3. Refer to PostgreSQL documentation on how to upgrade, e.g. [https://www.postgresql.org/docs/current/upgrading.html](https://www.postgresql.org/docs/current/upgrading.html)
   * For example use `pg_dumpall` of the _older_ PostgreSQL version (15) :\
     `pg_dumpall -U fylr > /mnt/dump_all.sql`
   * At the appropriate step, we renamed the old data directory by: \
     `mv /srv/fylr/postgres/pgdata /srv/fylr/postgres/pgdata_old` \
     The new `pgdata` directory was then automatically created by the new PostgreSQL.
   * We instructed `docker compose` to use a newer major PostgreSQL version by changing  [docker-compose.yml](https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/docker-compose.yml) , e.g. from `image: postgres:15` to `image: postgres:16`.
   * Importing the data by e.g.: `psql -d fylr -U fylr -f /mnt/dump_all.sql`
   * The following Errors, while restoring, can be caused by [docker-compose.yml](https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/docker-compose.yml) and in that case be safely ignored: `role "fylr" already exists` and `database "fylr" already exists`.
4. Start fylr, e.g.  `docker compose up -d fylr`.

