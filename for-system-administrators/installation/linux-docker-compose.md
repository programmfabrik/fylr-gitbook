# Linux

How to install fylr on a Linux Server via docker compose

## Requirements

* A domain name (like **fylr.example.com**), but not just a subpath (like **example.com/fylr**).
* A port (typically 443) to do https.
* Either an HTTPS certificate. Or Port 443 or Port 80 for registering and renewing a certificate with letsencrypt. Or the decision to operate fylr with HTTP only (insecure for passwords etc.).

### Hardware

* 16 GB of RAM to get going. Add memory if you need to answer more than a few simultaneous requests, or to generate more than a few preview images simultaneously.
* Start with 4 CPU cores and then adjust to your use case.
* amd64 Architecture, for this method.
*   #### Storage <a href="#network-storage" id="network-storage"></a>

    40 GB for container images. (default `/var/lib/docker`)\
    Ca. 100 GB for temporary file systems of containers. (default `/var/lib/docker`)\
    Ca. two times the storage space of you assets. So if you want to manage 1 TB of assets with fylr, have another 1 TB for preview images. If you tend to have big assets, you might need much less, as the previews then are much smaller in comparison to your assets.\
    Add fast storage for database and indices: 4% of what your assets need. So for 1 TB of assets have 40 GB. Most installations need a lot less than 4%.
*   #### Network Storage <a href="#network-storage" id="network-storage"></a>

    At most, put assets, previews and database dumps on network storage. Do not put other data on network storage as features may collide (e.g. overlay file system by docker).\
    If you use network storage then we recommend the NFS protocol. \
    CIFS can also work, but we have seen performance problems on some Windows servers without remedy and even data corruption - thus we do not support CIFS/SMB. Also NFS on a Windows server has been observed to have poor performance compared to Linux servers.

### Software

* The below mentioned containers are linux containers, so you need a linux server or linux virtual machine.
* fylr requires a running container engine. In this instructions, we use docker. So install docker according to its documentation: [how to install docker](https://docs.docker.com/engine/install/#server).
* We are regularly testing fylr with PostgreSQL 17. Customers with problems and PostgreSQL 14 (or even earlier versions) may be asked to upgrade PostgreSQL first.

The following commands assume a Debian or Ubuntu server and a bash shell.

* Get docker compose to use our provided example. Apparmor is required for docker in newer Debian and Ubuntu Versions:

```bash
apt-get install docker-compose-plugin apparmor
```

* currently (2023-06), docker needs a restart before it is really up and running:

```bash
systemctl restart docker.service
```

* Memory setting needed for the indexer: (opensearch or elasticsearch)

```bash
echo "vm.max_map_count=262144" >> /etc/sysctl.d/99-memory_for_indexer.conf
sysctl -p /etc/sysctl.d/99-memory_for_indexer.conf
```

* Indexer developers strongly recommend to disable swap. If you do not want to disable it on the whole system, at least make sure that the index does not use swap. We recommend to disable swap globally.

## Installation

Let us assume that you will install fylr in `/srv/fylr`:

```bash
mkdir /srv/fylr ; cd /srv/fylr
```

Create the following directories for the persistent data:

```bash
mkdir -p config/fylr postgres assets backups sqlbackups indexer migration
chown 1000 assets backups indexer migration
chown  999 postgres sqlbackups
```

The download is done below, with `docker compose`

## Configuration

We suggest that you use our example configuration as a starting point:

```bash
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/fylr.yml -o config/fylr/fylr.yml
```

Edit `config/fylr/fylr.yml` and replace strings with `EXAMPLE`.

If unsure about wasting your quota with letsencrypt, start with `useStagingCA: true`. A staging certificate will not be enough, though. Even some components of fylr will not trust each other. So do not use the frontend without a valid certificate (`useStagingCA: false`).

## Download

### docker compose

Much of the setup is encapsulated in a yaml file for docker compose. Get it and use it like this:

(We still assume that you are in the `/srv/fylr` directory.)

```bash
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/docker-compose.yml -o docker-compose.yml

docker compose up -d postgresql opensearch ; docker compose logs -f opensearch
```

`Ctrl` + `c` stops the display of new messages. We suggest you stop checking new messages when opensearch is done with its startup. Either when it quiets down or when you catch the message `Cluster health status changed` \[...] `reason: [shards started`.

So now postgres and opensearch are running.

Download and start fylr:

`docker compose up -d fylr; docker compose logs -f fylr`

fylr outputs `INF 🤓 FYLR started`\[...] when it managed to start and the Web-Frontend is online. Again, `Ctrl` + `c` stops the display of new messages.

We recommend to set `restart: always` for fylr in `docker-compose.yml` and restart fylr with:

```bash
docker compose up --force-recreate --no-deps -d fylr
```

### Result

You can now surf to your fylr webfrontend.

Default login is `root` with password `admin`. Please replace with a secure password: Click on `root` in the upper left corner.

### automate SQL dumps and update installation

To have consistent and complete snapshots of your SQL data, we strongly recommend:

```bash
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/maintain -o maintain
chmod a+x maintain
```

create a cron job like `/etc/cron.d/fylr-sql-backup-and-update`:

```
#MAILTO=you@example.com
PATH=/bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin

#m h  dom m dow user command

43 23  *  *  *  root /srv/fylr/maintain backup && /srv/fylr/maintain update

35 12  *  *  7  root /srv/fylr/maintain cleanup
```

With this setup you will find nightly sql dumps and pg\_dump's log files in `/srv/fylr/sqlbackups`.

Log files of the cron job will go to `/var/log/fylr-maintain.log`.

You can change the maintain script's config in `/etc/default/fylr`, using bash syntax.

## Keep log messages

The most important step to not throw away log messages with each container re-creation is already done in the above downloaded `docker-compose.yml`: it uses `logging:` `driver: journald`.

You additionally can configure [journald](https://www.freedesktop.org/software/systemd/man/latest/journald.conf.html) to your use case.

As an example, we do:

```
mkdir /etc/systemd/journald.conf.d
vi /etc/systemd/journald.conf.d/local_limits.conf
```

and in `local_limits.conf`:

```
# do not fill the entire disk
SystemKeepFree=10G
# keep for ...
MaxRetentionSec=2month
# rotate files after ...
MaxFilesSec=1day

# no other limits, but hardcoded maximum file size is 4G
SystemMaxUse=0
SystemMaxFileSize=0
SystemMaxFiles=0
# no rate limits
RateLimitIntervalSec=0
RateLimitBurst=0
```

Load the changes:

```
systemctl restart systemd-journald.service
```

Aspects to consider if  your logs need to be 100% reliable (usually overkill)

* hardcoded maximum file size is capped to 4G in compact mode (which is enabled by default), source: [https://www.freedesktop.org/software/systemd/man/journald.conf.html](https://www.freedesktop.org/software/systemd/man/journald.conf.html)
* this is using the default “blocking” mode

## Troubleshooting

* `docker compose` needs to be executed in the directory with the `docker-compose.yml`.
* When docker cannot start containers with errors refering to `shim, OCI, apparmor`: `apt-get install apparmor apparmor-utils; systemctl restart docker`
* When the indexer does not work, make sure you used `sysctl` as shown above.

Many messages can be safely ignored, see [here](../symptom-and-solution/log-messages-that-can-be-ignored.md).

Trouble with reachability, network, redirects:

* If you set your firewall rules to Allow, does the problem (e.g. `400 Bad Request`) go away?
* Does your network use a private IP range that overlaps with docker networks?
* Ubuntu may use `ufw` as Firewall, but there are problems in combination with docker. Consider to use `shorewall` > 5.0.6 instead (https://shorewall.org/Docker.html).

Assets are not processed, previews are not generated:

* Look into the URL path /inspect/files, so e.g. https://your-fylr-domain/inspect/files and look for status: `failed` and `error`. Click on the IDs and e.g. `Show details` to search for error messages.

If the indexer plugin `analysis-icu` is not installed you will get errors like:

> Unable to create index "..." error="Unknown char\_filter type \[icu\_normalizer]

### More messages for debugging

```
fylr+:
  logger+:
    # trace, debug, info, warn, error, fatal, panic
    # defaults to "info"
    level: "debug"
```

## Further reading

* [multiple fylrs in one linux](linux-docker-compose/multiple-fylrs-in-one-linux.md)
* [migrate a whole fylr into another](https://github.com/programmfabrik/fylr-install/blob/main/docker/further-reading/migrate-fylr-2-fylr.md)
* [Import an easydb into fylr](https://github.com/programmfabrik/fylr-install/blob/main/customization/restore-easydb5.md)
* [Use a customized Web-Frontend](https://github.com/programmfabrik/fylr-install/blob/main/customization/webfrontend.md)
