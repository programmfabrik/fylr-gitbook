# Linux

How to install fylr on a Linux Server via docker-compose

## Requirements

* A domain name (like **fylr.example.com**), but not just a subpath (like **example.com/fylr**).
* A port (typically 443) to do https.
* Either an HTTPS certificate. Or Port 443 or Port 80 for registering and renewing a certificate with letsencrypt. Or the decision to operate fylr with HTTP only (insecure for passwords etc.).

### Hardware

* 16 GB of RAM to get going. Add memory if you need to answer more than a few simultaneous requests, or to generate more than a few preview images simultaneously.
* Start with 4 CPU cores and then adjust to your use case.
* 40 GB for docker images.
* Double the storage space of you assets. So if you want to manage 1 TB of assets with fylr, have another 1 TB for preview images. If you tend to have big assets, you might need much less, as the previews then are much smaller in comparison to your assets.
* Add fast storage for database and indices: 4% of what your assets need. So for 1 TB of assets have 40 GB. Most installations need a lot less than 4%.
* amd64 Architecture, for this method.

### Software

* The below mentioned containers are linux containers, so you need a linux server or linux virtual machine.
* fylr requires a running container engine. In this instructions, we use docker. So install docker according to its documentation: [how to install docker](https://docs.docker.com/engine/install/#server).

The following commands assume a Debian or Ubuntu server and a bash shell.

* Get docker-compose to use our provided example. Apparmor is required for docker in newer Debian and Ubuntu Versions:

```bash
apt-get install docker-compose apparmor
```

* currently (2023-06), docker needs a restart before it is really up and running:

```bash
systemctl restart docker.service
```

* Memory setting needed for elasticsearch:

```bash
echo "vm.max_map_count=262144" >> /etc/sysctl.d/99-memory_for_elasticearch.conf
sysctl -p /etc/sysctl.d/99-memory_for_elasticearch.conf
```

## Installation

Let us assume that you will install fylr in `/srv/fylr`:

```bash
mkdir /srv/fylr ; cd /srv/fylr
```

Create the following directories for the persistent data:

```bash
mkdir -p config/fylr postgres assets backups sqlbackups elasticsearch
chown 1000 assets backups elasticsearch
chown  999 postgres sqlbackups
```

## Configuration

We suggest that you use our example configuration as a starting point:

```bash
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/fylr.yml -o config/fylr/fylr.yml
```

Edit `config/fylr/fylr.yml` and replace strings with `EXAMPLE`.

If unsure about wasting your quota with letsencrypt, start with `useStagingCA: true`. A staging certificate will not be enough, though. Even some components of fylr will not trust each other. So do not use the frontend without a valid certificate (`useStagingCA: false`).

### docker-compose

Much of the setup is encapsulated in a docker-compose yaml file. Download and use it like this:

We still assume that you are in the `/srv/fylr` directory.

```bash
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/docker-compose.yml -o docker-compose.yml

docker-compose up
```

`Ctrl` + `c` stops the services again.

If you are satisfied, we recommend to set `restart: always` for fylr in `docker-compose.yml` and let it run in the background with:

```bash
docker-compose up -d
```

### Result

You can now surf to your fylr webfrontend.

Default login is `root` with password `admin`. Please replace with a secure password: Click on `root` in the upper left corner.

### automate SQL dumps and updates of fylr and postgresql

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

Elasticsearch cannot be updated automatically due to missing support by the elasticsearch team (no tags like `latest`).

## Troubleshooting

* `docker-compose` needs to be executed in the directory with the `docker-compose.yml`.
* When docker cannot start containers with errors refering to `shim, OCI, apparmor`: `apt-get install apparmor apparmor-utils; systemctl restart docker`
* When elasticsearch does not work, make sure you used `sysctl` as shown above.

Many messages can be safely ignored, see [here](log-messages-that-can-be-ignored.md).



Trouble with reachability, network, redirects:

* If you set your firewall rules to Allow, does the problem (e.g. `400 Bad Request`) go away?
* Does your network use a private IP range that overlaps with docker networks?
* Ubuntu may use `ufw` as Firewall, but there are problems in combination with docker. Consider to use `shorewall` > 5.0.6 instead (https://shorewall.org/Docker.html).

Assets are not processed, previews are not generated:

* Look into the URL path /inspect/files, so e.g. https://your-fylr-domain/inspect/files and look for status: `failed` and `error`. Click on the IDs and e.g. `Show details` to search for error messages.

If the elasticsearch plugin `analysis-icu` is not installed you will get errors like:

> Unable to create index "..." error="Unknown char\_filter type \[icu\_normalizer]

### More messages for debugging

```
fylr+:
  logger:
    # trace, debug, info, warn, error, fatal, panic
    # defaults to "info"
    level: "debug"
```

## Further reading

(NOT DONE YET)

* [migrate a whole fylr into another](https://github.com/programmfabrik/fylr-install/blob/main/docker/further-reading/migrate-fylr-2-fylr.md)
* [Import an easydb into fylr](../migration/easydb5-to-fylr.md)
* [Use a customized Web-Frontend](../configuration/custom-webfrontend.md)
