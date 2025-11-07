---
description: >-
  how to install fylr "in place" on an easydb5 server and migrate easydb's
  content to fylr using easydb's assets files directly from disk, without
  needing to transfer them
---

# Migration with map to local storage

This method can save time and does not need a separate server. easydb5 is only needed to extract metadata, but not to extract asset files, which are used from storage directly as is.

The following example migrates all from <mark style="color:blue;">https://easydb.example.com</mark> to <mark style="color:blue;">https://fylr.example.com</mark>. (IP address 1.2.3.4)

## Checks and Requirements

The server should have enough **RAM** available (at least 8 GB free when easydb is running, more is recommended during image preview generation).



<details>

<summary>Is there enough free storage?</summary>

* for doubling the indexes and SQL-DB of easydb (fylr will have its own)
* for doubling the preview images of easydb (fylr is recommended to generate its own)
* 20+ GB for fylr container versions

</details>

<details>

<summary>A DNS subdomain for fylr</summary>

Have a DNS entry, in our example _fylr.example.com_, pointing to the same IP address as the easydb (in our example _easydb.example.com_).

</details>

<details>

<summary>Prevent name collisions</summary>

Check indexes will not collide _**by name**_ between eaydb5 and fylr:

```bash
docker exec easydb-server curl http://easydb-elasticsearch:9200/_cat/indices
```

<p align="right">... good if they do not start with "fylr".</p>

</details>

<details>

<summary>Allow passwords to be transferred</summary>

In standard configuration, easydb does not output account passwords for migration, as a security feature. To make a full migration, you have to change that setting temporarily, at least for the step "_extract metadata"_ ("backup"). The setting in easydb5 is:&#x20;

```yaml
server:
  api:
    user:
      include_password: true
```

... e.g. in `easydb-server.yml` . For more information see [http://docs.easydb.de/en/technical/api/user/#returning-password-hashes](http://docs.easydb.de/en/technical/api/user/#returning-password-hashes)

</details>

## 1. fylr installation

To save resources like RAM, we use easydb's infrastructure

To save resources like RAM, we use easydb's infrastructure

<details>

<summary>1.a use docker compose for fylr installation</summary>

```bash
apt-get install docker-compose-plugin
mkdir /srv/fylr ; cd /srv/fylr
mkdir -p config/fylr assets backups migration postgres sqlbackups
chown 1000 assets backups migration
chown  999 postgres sqlbackups
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/fylr.yml -o config/fylr/fylr.yml
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/maintain -o maintain
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/docker-compose.yml -o docker-compose.yml
chmod a+x maintain
vi docker-compose.yml # see below for content
docker compose up -d; docker compose logs -f
```

Stop outputting log messages with `Ctrl`-`c` if seen enough

</details>

<details>

<summary>1.b edit <code>/srv/fylr/docker-compose.yml</code></summary>

Make Opensearch just comments. change the network to `easydb_default`, change fylr port and check the volume paths, left of the `:`, so .e.g. `/srv/easydb/eas/lib/assets/orig`.\
So that you have:

<pre><code>services:
  # opensearch:
  # [...not shown here: more opensearch as comments ...]
  
<strong>  postgresql:
</strong>    image: postgres:18
    container_name: postgresql
    restart: always
    shm_size: 1g
    environment:
      POSTGRES_DB: 'fylr'
      POSTGRES_USER: 'fylr'
      POSTGRES_PASSWORD: 'fylr'
      PGDATA: /var/lib/postgresql/data/pgdata
    volumes:
      - "/srv/fylr/postgres:/var/lib/postgresql/data"
      - "/srv/fylr/sqlbackups:/mnt"
    command: >
      -c work_mem=64MB
      -c maintenance_work_mem=32MB
      -c max_wal_size=512MB
      -c max_connections=100
    networks:
      - easydb_default
    logging:
      driver: "journald"
      
  fylr:
    image: docker.fylr.io/fylr/fylr:latest
    hostname: fylr.localhost
    container_name: fylr
    restart: always
    ports:
      - "127.0.0.1:91:91"
    networks:
      - easydb_default
    volumes:
      - "/srv/easydb/eas/lib/assets/orig:/mnt/orig_early:ro"
      - "/srv/easydb/eas/lib/assets/dest:/mnt/dest_early:ro"
      - "/srv/fylr/config/fylr:/fylr/config"
      - "/srv/fylr/assets:/srv"
      - "/srv/fylr/backups:/fylr/files/backups"     # /inspect/system/backups/ and /backupmanager
      - "/srv/fylr/migration:/fylr/files/migration" # /inspect/migration/
    logging:
      driver: "journald"

networks:
  easydb_default:
    external: true
</code></pre>

</details>

<details>

<summary>1.c Adjust <code>/srv/fylr/config/fylr/fylr.yml</code></summary>

```yaml
fylr+:
  allowpurge: true
  externalURL: "https://fylr.example.com"
[...]
  elastic+:
    addresses:
    - "http://easydb-elasticsearch:9200"
[...]
  services+:
    webapp+:
      addr: ":91"
      tls:
```

... and of course unique `encryptionKey` and `signingSecret` .

</details>

<details>

<summary>1.d Start postgres and fylr</summary>

```bash
docker compose up -d; docker compose logs -f
```

Stop outputting log messages with `Ctrl`-`c` if seen enough

</details>

1.e Allow purging fylr in the Frontend, see the screenshot under **2.** [here](../../../tutorials/purge-a-fylr-instance.md#allow-purge).

## 2. Apache and https certificate for fylr

<details>

<summary>2.a Assuming certbot with LetsEncrypt is OK for you, do...</summary>

Add a minimal VirtualHost for the fylr to your Apache configuration:

```
<VirtualHost 1.2.3.4:80>
    ServerName fylr.example.com
</VirtualHost>
```

... replace the IP Address 1.2.3.4 and of course the domain name.

Install and use certbot: _(unless you have another method to obtain a https-certificate for fylr)_

```
apache2ctl graceful
apt install snapd
snap install --classic certbot
certbot --apache # in the shown choice: select the fylr domain
```

After certbot improved your Apache configuration, add the configuration to show fylr:

```
<VirtualHost 1.2.3.4:80>
    ServerName fylr.example.com

RewriteEngine on
RewriteCond %{SERVER_NAME} =fylr.example.com
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

<VirtualHost 1.2.3.4:443>
    ServerName fylr.example.com

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:91/
    ProxyPassReverse / http://127.0.0.1:91/

SSLCertificateFile /etc/letsencrypt/live/fylr.example.com/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/fylr.example.com/privkey.pem
Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
```

Make sure that you have the correct number of virtual hosts: 4 (easydb 80, easydb port 443, fylr 80, fylr 443) across all Apache config files. Certbot creates an additional config file and double VirtualHosts (e.g. a fifth one) can cause hard to find errors.

Make sure to now also use explicit  **IP address** (not `*`) and **ServerName** in the easydb configuration for apache:

```
<VirtualHost 1.2.3.4:80>
    ServerName easydb.example.com

[...]

<VirtualHost 1.2.3.4:443>
    ServerName easydb.example.com 
```

</details>

2.b Log into your fylr (https://fylr.example.com) as root with password admin.

2.c Change the password of root to a secure one.

2.d Check that fylr is at least Version 6.26.0

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

## 3. Extract metadata from easydb5

3.a. Surf to https://fylr.example.co&#x6D;**/inspect/migration**

3.b. expand the Paragraph **`Create backup`** (by clicking the triangle)

<details>

<summary>3.c. Fill in at least the following values:</summary>

* `URL of server` : Fill in your equivalent of `https://easydb.example.com`
* `Login`: `root`
* `Password`: password of easydb's root account
* `OAuth2`: uncheck this box, it is only needed to extract from fylr
* `Max Parallel`: To not slow your easydb down, choose a number that is half or less of the available CPU cores.
* `Purge`: you can leave this on, it does not affect easydb or fylr. (It was added to overwrite backup files, but currently it creates a new backup anyway)

</details>

Click **`Backup`** . This can take from one minute to several hours depending on your data.

See [here](../../../for-system-administrators/migration/inspect.md) for more information.

## 4. Inject metadata into fylr

4.a. Surf to https://fylr.example.co&#x6D;**/inspect/migration** (log in as root)

4.b. expand the Paragraph **`Restore backup`** (by clicking the triangle)

<details>

<summary>4.c. Fill in at least the following values:</summary>

* `Backup` : choose the backup that you created above
* `URL` : Fill in your equivalent of `https://fylr.example.com`
* `Login`: `root`
* `Password`: password of fylr's root account
* `File Mode`: choose `Use files from source - rput_leave (bulk)`
* `File Version`: use the default `original`
* `Copy file preview versions`: Enable this box.
* `Include Password`: Can be turned off for test runs. When turned on, passwords are included. But for that, the above backup has to be made with a less secure easydb configuration active. See [http://docs.easydb.de/en/technical/api/user/#returning-password-hashes](http://docs.easydb.de/en/technical/api/user/#returning-password-hashes)
* `Include Events`: Turn on if you want to transfer the events that were recorded in easydb. Considered not needed unless you know you want it.
* `OAuth2`: This box has to be enabled.
* `OAuth2 Client Id`: leave the default fylr-web-frontend
* `Max Parallel`: To not slow your easydb down, choose a number that is half or less of the available CPU cores.
* `Purge or Continue`: `Purge` This will overwrite fylr's contents with easydb, which is the whole point.\
  `Continue` is useful if your previous attempt aborted with a timeout or network error and should be continued.

</details>

Click **`Restore`** . This can take from a few minutes to many hours depending on your data.

* It will continue if you close your browser.
* You can come back to it via **https://**&#x66;ylr.example.co&#x6D;**/inspect/migration**
* And also directly via **https://**&#x66;ylr.example.co&#x6D;**/inspect/migration/**&#x6D;ymigrationname

See [here](../../../for-system-administrators/migration/inspect.md#restore) for more information.

When the restore/inject is done, a reindex will be done for fylr, so it will take a while until you can see the data in the webfrontend https://fylr.example.com.

## 5. Teach fylr where to find easydb assets on disk

<details>

<summary>5.a Collect the URL prefixes of all easydb's partitions</summary>

Look into **https://**&#x66;ylr.example.co&#x6D;**/inspect/files/** (log in as root)

* Click on a version (the `Version` column has `small` or `full` or others but not `ORIGINAL`) file on it's ID
  * note the field `Remote URL`, it might contain e.g. `https://easydb.example.com/eas/partitions-inline/2/0/1270/1270/4839d32e5c8ecca1`
* Click an original (`Version` column has `ORIGINAL`) file on it's ID
  * Also for this asset note the field `Remote URL`, it might contain e.g. `https://easydb.example.com/eas/partitions-inline/1/0/1270/1270/acda0f0f5982bb64`
* Next you need to cut off the last parts of the Remote URLs in your notes, so that only the URL prefix remains, which is what you need. The prefix ends before the single zero. So in our example the prefixes are:

```
https://easydb.example.com/eas/partitions-inline/2/ (for Versions and)
https://easydb.example.com/eas/partitions-inline/1/ (for Originals)
```

*   Count the number of partitions in **https://**&#x65;asydb.example.co&#x6D;**/servermanager**\
    For that you have to choose easydb Asset Server (EAS) at the top.\


    <figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
* Continue searching through different files as above until you have the URL prefix for each partition (but often there are just two).

</details>

<details>

<summary>5.b Configure the locations</summary>

Surf to **https://**&#x66;ylr.example.co&#x6D;**/locationmanager** (log in as root)

Create the following two:

* Fylr location `EAS originals`
  * `Read Only`
  * Directory (in container) `/mnt/orig_early`
  * Remote Url Prefix example: https://easydb.example.com/eas/partitions-inline/1/
* Fylr location `EAS versions`
  * Directory (in container) `/mnt/dest_early`
  * Remote URL Prefix example: https://easydb.example.com/eas/partitions-inline/2/
  * If you have enough free storage space to double all preview versions, then set this location to `Read Only`. Then none of them will be deleted. Otherwise set it as Default Location for `versions` . Then easydb previews will be deleted as they are replaced with fylr previews. `Read Only` is safer, especially if you still want to use easydb, and thus recommended.

</details>

<details>

<summary>5.c Let fylr use the asset files of easydb5 directly from disk, without asking easydb</summary>

* Go to **https://**&#x66;ylr.example.co&#x6D;**/inspect/files/**
* search with `Location`=`remote`
* Choose Action `Map to local storage` and `Search result`, not `Selected`. Click the button `Action` at the right.
* Now the easydb is not used by fylr any more. (But elasticsearch is still used by fylr)

</details>

**This was the central step.** fylr is now independent from easydb and easydb can be turned off. (after testing fylr of course. And Elasticsearch is still used by fylr)

## 6. Adjust previews to fylr standards

As previews from easydb are different from fylr previews, it is recommended to replace easydb previews with fylr previews. This will be done in the background while you can already work with fylr. Although this whole step is optional, you should do it if you encounter problems. When seeking support from the developer you will likely be asked to do this step to come to a clean coherent state.

<details>

<summary>6.a Produce fylr previews</summary>

* Surf to **https://**&#x66;ylr.example.co&#x6D;**/inspect/files/** (login as root)
* In the drop down menu  `Version`  choose  `original`  and click the `Search` button.
* In the drop down menu `Action` choose `produce versions` .
* To the right select the round button below `Search result` (not below `Selected`).
* Click the `Action` button.

</details>

<details>

<summary>6.b Check whether all previews have been replaced</summary>

* Is the File queue empty at **https://**&#x66;ylr.example.co&#x6D;**/inspect/system/queues/?queue=file** ?\
  At the top it would show something like:\
  &#xNAN;_`There are 18 parallel and 10 parallel high priority only file workers active. The queue`` `**`contains 0 total entries`**`.`_
* Surf to **https://**&#x66;ylr.example.co&#x6D;**/inspect/files/** (login as root)
  * In the drop down menu  `location`  choose  `EAS versions`  and click the `Search` button.
  * The Search shows zero results when all have been replaced.

</details>

<details>

<summary>6.c Remove easydb preview versions to regain storage (optional)</summary>

* At first just remove the location `EAS versions`  in the location manager
* Next, remove fylr's access to them (e.g. remove it from `/srv/fylr/docker-compose.yml` and recreate the container).&#x20;
* Check that the fylr webfrontend still shows previews, an https://fylr.example.com.
* Then, when all is still working, you can delete them to free storage capacity.

</details>

## 7. Remove easydb

This step is optional but recommended, as easydb lifetime and support will end before fylr's.

<details>

<summary>7.a Replace easydb PostgreSQL and Indexer</summary>

See the [default fylr installation](../../../for-system-administrators/installation/linux-docker-compose.md#installation) for the missing pieces and adjust `docker-compose.yml` and `fylr.yml`.

</details>

<details>

<summary>7.b Remove Apache</summary>

See the [default fylr installation](../../../for-system-administrators/installation/linux-docker-compose.md#installation) and adjust `docker-compose.yml` and `fylr.yml`. for default ports and certificate.

```
systemctl stop apache2
systemctl disable apache2
systemctl mask apache2
/srv/fylr/maintain fylr-recreate
cd /srv/fylr
docker-compose logs -f fylr
```

</details>

**7.c Change fylr domain**

In case you want to change fylr's domain to the former domain of easydb, see [here](../../../for-system-administrators/configuration/dns-domains.md#changes-to-the-main-domain).
