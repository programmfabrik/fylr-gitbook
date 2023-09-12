---
description: Backup a fylr instance, to later restore it into an empty fylr instance.
---

# Backup

You need access to the command line.

In this example we call the instances "old" and "new" and the linux servers running them: "old server" and "new server". But you can also think of the new server as a backup server.

### prepare old server

Check that you have access to the SQL backups: In the case of an installation via docker-compose, the access is a mounted volume (e.g. in the [docker-compose.yml](../\_assets/docker-compose.yml) of our installation [instructions](https://docs.fylr.io/for-system-administrators/installation/linux-docker-compose)):

```
services:
  postgresql:
    volumes:
      - "/srv/fylr/sqlbackups:/mnt"
```

### backup

1. Save a consistent copy of the SQL data on the old server: (This may have been already done automatically)

```
docker exec postgresql pg_dump -U fylr -v -Fc -f /mnt/fylr.pg_dump fylr
```

This SQL does include datamodel, objects, users, groups, user rights, base configuration.&#x20;

(But not assets, logs.)

2. Copy the assets from old server to new server (we assume file based assets, not s3 based):

```
rsync -a --numeric-ids old-server:/srv/fylr/assets/* /srv/fylr/assets
```

_... executed on the new server, as all the following commands._

3. Also get the dump of the SQL to the new server, here an example using scp:

```
scp old-server:/srv/fylr/sqlbackups/fylr.pg_dump /srv/fylr/sqlbackups/
```

4. We recommend to also copy the configuration of the old server, even if the new server may need a somewhat different configuration:

```
scp old-server:/srv/fylr/config/fylr/fylr.yml /srv/fylr/config/fylr/fylr.yml.oldserv
```

Now you have all data for a restore on the new server.





***

## restore

1. install fylr on the new server, as described in our [installation instructions](https://docs.fylr.io/for-system-administrators/installation/linux-docker-compose), _<mark style="background-color:yellow;">**but only start postgresql:**</mark>_

```
docker-compose up -d postgresql
```

Make sure that the postgresql DB and elasticsearch indices are empty from previous attempts on the new server so that there is no collision of data.

2. import the sql-dump on the new server:&#x20;

```
docker exec -it postgresql pg_restore -U fylr -v -d fylr /mnt/fylr.pg_dump
```

3. start fylr and elasticsearch on the new server:

```
docker-compose up -d
```

4. You may need to force a re-index in Elasticsearch: surf to `/inspect/system/` on the new server, so e.g. `https://new-server.example.com/inspect/system/` and click a Reindex button.
