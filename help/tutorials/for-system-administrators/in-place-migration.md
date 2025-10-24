---
description: >-
  how to install fylr on an easydb5 server and migrate easydb's content to fylr
  using easydb's assets files directly from disk, without needing to transfer
  them
---

# In place migration

This method can save time and does not need a separate server. easydb5 is only needed to extract metadata, but not to extract asset files, which are used from storage directly as is.

The following example migrates all from <mark style="color:blue;">https://easydb.example.com</mark> to <mark style="color:blue;">https://fylr.example.com</mark>. (IP address 1.2.3.4)

## Checks and Requirements

The server should have enough **RAM** available (at least 8 GB free when easydb is running, more is recommended during image preview generation).

<details>

<summary>Is there enough free storage?</summary>

* for doubling the indexes and SQL-DB of easydb (fylr will have its own)

- for doubling the preview images of easydb (fylr is recommended to generate its own)

* 20+ GB for fylr container versions

</details>

<details>

<summary>A DNS subdomain for fylr</summary>

Have a DNS entry, in our example _fylr.example.com_, pointing to the same IP address as the easydb (in our example _easydb.example.com_).

</details>

<details>

<summary>Prevent name collisions</summary>

Check that SQL databases and indexes will not collide _**by name**_ between eaydb5 and fylr:

<pre class="language-bash"><code class="lang-bash"><strong>docker exec easydb-pgsql psql -U postgres -l
</strong></code></pre>

<p align="right">... good if there is no database named "fylr" yet.</p>

```bash
docker exec easydb-server curl http://easydb-elasticsearch:9200/_cat/indices
```

<p align="right">... good if they do not start with "fylr".</p>

</details>

## 1. fylr installation

To save resources like RAM, we use easydb's infrastructure

<details>

<summary>1.a Create a dedicated SQL database for fylr</summary>

```bash
docker exec -ti easydb-pgsql psql -U postgres
CREATE DATABASE fylr ENCODING 'UTF8';
CREATE USER fylr WITH LOGIN ENCRYPTED PASSWORD 'fylr';
GRANT ALL PRIVILEGES ON DATABASE "fylr" TO "fylr";
ALTER DATABASE fylr OWNER TO fylr;
exit
```

We suggest to include this fylr database in the easydb backup:&#x20;

Change the file `/srv/easydb/maintain` :

* add `fylr` so that you have e.g.: `DBS="eas easydb5 fylr"` .

</details>

<details>

<summary>1.b use docker compose for fylr installation</summary>

```bash
apt-get install docker-compose-plugin
mkdir /srv/fylr ; cd /srv/fylr
mkdir -p config/fylr assets backups migration
chown 1000 assets backups migration
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/fylr.yml -o config/fylr/fylr.yml
curl https://raw.githubusercontent.com/programmfabrik/fylr-gitbook/main/_assets/maintain -o maintain
chmod a+x maintain
vi docker-compose.yml # see below for content
docker compose up -d; docker compose logs -f
```

Stop outputting log messages with `Ctrl`-`c` if seen enough

</details>

<details>

<summary>1.c create <code>/srv/fylr/docker-compose.yml</code></summary>

Check the volume paths, left of the `:`, so .e.g. `/srv/easydb/eas/lib/assets/orig`.

```
services:
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
      - "/srv/easydb/eas/lib/assets/orig:/mnt/orig_old:ro"
      - "/srv/easydb/eas/lib/assets/dest:/mnt/dest_old:ro"
      - "/srv/fylr/config/fylr:/fylr/config"
      - "/srv/fylr/assets:/srv"
      - "/srv/fylr/backups:/fylr/files/backups"     # /inspect/system/backups/ and /backupmanager
      - "/srv/fylr/migration:/fylr/files/migration" # /inspect/migration/
    logging:
      driver: "journald"

networks:
  easydb_default:
    external: true
```

</details>

<details>

<summary>1.d Adjust <code>/srv/fylr/config/fylr/fylr.yml</code></summary>

```yaml
fylr+:
  allowpurge: true
  externalURL: "https://fylr.example.com"
[...]
  db:
    driver: "postgres"
    dsn: "postgres://fylr:fylr@easydb-pgsql:5432/fylr?sslmode=disable"
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

<summary>1.e Start fylr</summary>

```bash
docker compose up -d; docker compose logs -f
```

Stop outputting log messages with `Ctrl`-`c` if seen enough

</details>

## 2. Apache and https certificate for fylr

<details>

<summary>2.a Assuming you use certbot with LetsEncrypt, do...</summary>

Add a minimal VirtualHost for the fylr to your Apache configuration:

```
<VirtualHost 1.2.3.4:80>
    ServerName fylr.example.com
</VirtualHost>
```

... replace the IP Address 1.2.3.4 and of course the domain name.

Install and use certbot: _(unless you have another method to obtain a https-certificate for fylr)_

```
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

</details>

2.b Log into your fylr (https://fylr.example.com) as root with password admin.

2.c Change the password of root to a secure one.

2.d Check that fylr is at least Version 6.26.0.

## 3. Extract metadata from easydb5

3.a. Surf to https://fylr.example.co&#x6D;**/inspect/migration**

3.b. expand the Paragraph **`Create backup`** (by clicking the triangle)

<details>

<summary>3.c. Fill in at least the following values:</summary>

* `URL of server` : Fill in your equivalent of `https://easydb.example.com`

- `Login`: `root`

* `Password`: password of easydb's root account

- `OAuth2`: uncheck this box, it is only needed to extract from fylr

* `Max Parallel`: To not slow your easydb down, choose a number that is half or less of the available CPU cores.

- `Purge`: you can leave this on, it does not affect easydb or fylr. (It was added to overwrite backup files, but currently it creates a new backup anyway)

</details>

Click **`Backup`** . This can take from one minute to several hours depending on your data.

See [here](../../../for-system-administrators/migration/inspect.md) for more information.

## 4. Inject metadata into fylr

4.a. Surf to https://fylr.example.co&#x6D;**/inspect/migration** (log in as root)

4.b. expand the Paragraph **`Restore backup`** (by clicking the triangle)

<details>

<summary>4.c. Fill in at least the following values:</summary>

* `Backup` : choose the backup that you created above

- `URL` : Fill in your equivalent of `https://fylr.example.com`

* `Login`: `root`

- `Password`: password of fylr's root account

* `File Mode`: choose `Use files from source - rput_leave (bulk)`

- `File Version`: use the default `original`

* `Copy file preview versions`: Enable this box.

- `Include Password`: Can be turned off for test runs. When turned on, passwords are included. But for that, the above backup has to be made with a less secure easydb configuration active. See TODO

* `Include Events`: Turn on if you want to transfer the events that were recorded in easydb. Considered not needed unless you know you want it.

- `OAuth2`: This box has to be enabled.

* `OAuth2 Client Id`: leave the default fylr-web-frontend

- `Max Parallel`: To not slow your easydb down, choose a number that is half or less of the available CPU cores.

* `Purge or Continue`: `Purge` This will overwrite fylr's contents with easydb, which is the whole point.\
  `Continue` is useful if your previous attempt aborted with a timeout or network error and should be continued.

</details>

Click **`Restore`** . This can take from a few minutes to many hours depending on your data.

* It will continue if you close your browser.
* You can come back to it via **https://**&#x66;ylr.example.co&#x6D;**/inspect/migration**
* And also directly via **https://**&#x66;ylr.example.co&#x6D;**/inspect/migration/**&#x6D;ymigrationname

TODO: for more information see **link** page

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

* Count the number of partitions in https://easydb.example.com/servermanager
* Continue searching through different files as above until you have the URL prefix for each partition (but often there are just two).

</details>

<details>

<summary>5.b Configure the locations</summary>

Surf to **https://**&#x66;ylr.example.co&#x6D;**/locationmanager** (log in as root)

Create the following two:

* Fylr location `EAS originals`
  * `Read Only`
  * Directory (in container) `/mnt/orig`
  * Remote Url Prefix example: https://easydb.example.com/eas/partitions-inline/1/
* Fylr location `EAS versions`
  * Directory (in container) `/mnt/dest`
  * Remote URL Prefix example: https://easydb.example.com/eas/partitions-inline/2/
  * If you have enough free storage space to double all preview versions, then set this location to `Read Only`. Then none of them will be deleted. Otherwise set it as Default Location for `versions` . Then easydb previews will be deleted as they are replaced with fylr previews. `Read Only` is safer, especially if you still want to use easydb, and thus recommended.

</details>

<details>

<summary>5.c Let fylr use the asset files of easydb5 directly from disk, without asking easydb</summary>

* Go to https://fylr.example.com/inspect/files/

- search with `Location`=`remote`

* Choose Action `Map to local storage` and `Search result`, not `Selected`. Click the button `Action` at the right.

- Now the easydb is not used by fylr any more.

</details>

**This was the central step.** fylr is now independent from easydb and easydb can be turned off. (after testing fylr of course)

## 6. Let fylr produce its own previews

As previews from easydb are different from fylr previews, it is recommended to replace easydb previews with fylr previews. Maybe silently in the background while already working with fylr. Although this whole step is optional, you should do it if you encounter problems. When seeking support from the developer you will likely be asked to do this step to come to a clean coherent state.

TODO: translate to English

Auf allen originalen (filter: original), die action "produce versions" ausführen

* Go to https://fylr.example.com/inspect/files/
* Search with `Version` = `original`
* die action\*\* produce versions\*\* ausführen

When all preview versions are replaced, you can remove easydb preview versions. At first just by removing the access of fylr to them. Then, when all is still working, you can delete them to regain more storage capacity.

## 7. Remove easydb

This step is optional but recommended, as easydb lifetime and support will end before fylr's.

### Replace easydb PostgreSQL and Indexer with the ones from default fylr installation

See the default fylr installation for the missing pieces and adjust docker-compose.yml and fylr.yml.

TODO: link default install page and add some non-obvious steps

### Remove Apache

TODO: specific steps

### Change fylr domain

see TODO: link other page here
