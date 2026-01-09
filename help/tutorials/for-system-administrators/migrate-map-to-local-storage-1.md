---
description: >-
  How to migrate from an easydb5 server to a fylr server, using assets files on
  a common NFS share, no need to duplicate assets.
---

# Migrate with map to local storage and 2 servers

This method can save time and storage. easydb5 is only needed to extract metadata, but not to extract asset files, which are used from storage directly as is.

The following example migrates all from <mark style="color:blue;">https://easydb.example.com</mark> to <mark style="color:blue;">https://fylr.example.com</mark>.

## Checks and Requirements

The requirements of the default recommended installation apply here as well, described [here](../../../for-system-administrators/installation/linux-docker-compose.md)...

Except:

<details>

<summary>Storage for <em>original</em> assets</summary>

As the common NFS share is used, exisiting original asset files are already accounted for in storage. So you can ignore that part of the requirements in the default recommended installation.

\
You may want to have free space for future asset uploads, but that is just the same calculation as with only the easydb5.&#x20;

</details>

<details>

<summary>Storage for asset <em>versions</em></summary>

The asset versions of _easydb5_ are typically used by fylr for a while and then are replaced by _fylr_ versions, which are slightly different. How long to use them can be decided on demand, later.

For the configuration _now,_ you have two options:&#x20;

A. Use easydb5 versions **read-only**: easier, safer, but needs more storage for assets which have both easydb5 versions and fylr versions.

\
B. Delete easydb5 versions on the fly whenever fylr creates fylr versions: minimal storage needed, but harder to configure and less safety net (easydb5 cannot use the previews any more)



</details>

<details>

<summary>Allow passwords to be transferred</summary>

In standard configuration, easydb does not output account passwords for migration, as a security feature. To make a full migration, you have to change that setting temporarily, at least for the step "_extract metadata"_ ("backup"). The setting in easydb5 is:

```yaml
server:
  api:
    user:
      include_password: true
```

... e.g. in `easydb-server.yml` . For more information see [http://docs.easydb.de/en/technical/api/user/#returning-password-hashes](http://docs.easydb.de/en/technical/api/user/#returning-password-hashes)

</details>

## 1. fylr installation

A standard installation with changed storage configuration.

<details>

<summary>1.a use docker compose for fylr installation</summary>

Use the default recommended installation as described [here](../../../for-system-administrators/installation/linux-docker-compose.md). But before starting fylr, change `docker-compose.yml` as described below.

</details>

<details>

<summary>1.b edit <code>/srv/fylr/docker-compose.yml</code></summary>

* Add the below shown volume paths, without duplicating the hierarchy (so only one services:, only one fylr:, only one volumes:
* Make shure you adjust the volume paths left of the `:`,\
  so .e.g. `/srv/easydb/eas/lib/assets/orig` might by instead `/nfs/asset/orig` on your server.&#x20;
* The example below has two volumes for two easydb partitions. Your easydb may have more partitions. Create one fylr volume per easydb partition.

Example (irrelevant lines not shown):

```
services:
  fylr:
    volumes:
      - "/srv/easydb/eas/lib/assets/orig:/mnt/orig_early:ro"
      - "/srv/easydb/eas/lib/assets/dest:/mnt/dest_early:ro"
```

</details>

1.e Allow purging fylr in the Frontend, see the screenshot:<br>

<figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

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

See [here](../../../for-system-administrators/migration/inspect.md) if you want more information about this process.

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

See [here](../../../for-system-administrators/migration/inspect.md#restore) if you want more information about this process.

When the restore/inject is done, a reindex will be done for fylr, so it will take a while until you can see the data in the webfrontend https://fylr.example.com.

## 5. Teach fylr where to find easydb assets on disk

<details>

<summary>5.a Collect the "Remote URL Prefixes" of all easydb partitions</summary>

Look into **https://**&#x66;ylr.example.co&#x6D;**/inspect/files/** (log in as root)

* Click a _version file_ on it's ID number (_version file_ = the `Version` column has `small` or `full` or others but _not_ `ORIGINAL`).
  * note the content of field `Remote URL`, it might contain e.g. `https://easydb.example.com/eas/partitions-inline/2/0/1270/1270/4839d32e5c8ecca1`
* Click an original (`Version` column _has_ `ORIGINAL`) file on it's ID number.
  * Also for this asset note the content of field `Remote URL`, it might contain e.g. `https://easydb.example.com/eas/partitions-inline/1/0/1270/1270/acda0f0f5982bb64`
* Next you need to cut off the last parts of the Remote URLs in your notes, so that only the URL prefix remains, which is what you need. The prefix ends before the single zero. So in our example the prefixes are:

```
https://easydb.example.com/eas/partitions-inline/2/ (for Versions and)
https://easydb.example.com/eas/partitions-inline/1/ (for Originals)
```

*   Count the number of partitions in **https://**&#x65;asydb.example.co&#x6D;**/servermanager**.\
    For that you have to choose easydb Asset Server (EAS) at the top:<br>

    <figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
* Continue searching through different files as above until you have the URL prefix for each partition (but often there are just two).

</details>

<details>

<summary>5.b Configure the locations</summary>

Surf to **https://**&#x66;ylr.example.co&#x6D;**/locationmanager** (log in as root)

Create the following two:

* Fylr location `easydb originals`
  * **Read Only**: enable this
  * **Directory** (in container) `/mnt/orig_early`
  * **Remote URL Prefix** example: https://easydb.example.com/eas/partitions-inline/1/\
    Use here one of the prefixes you collected in 5.a.\
    \&#xNAN;_(Do not confuse this with the **Prefix** field. Use **Remote URL Prefix**.)_
* Fylr location `easydb versions`
  * **Directory** (in container) `/mnt/dest_early`
  * **Remote URL Prefix**: As above, use one of the collected Remote URL Prefixes.\
    Example: https://easydb.example.com/eas/partitions-inline/2/
  * If you have enough free storage space to double all preview versions, then set this location to `Read Only`. Then none of them will be deleted. Otherwise set it as Default Location for `versions` . Then easydb previews will be deleted as they are replaced with fylr previews. `Read Only` is safer, especially if you still want to use easydb, and thus recommended.
* In case your easydb has more than two partitions, you may have to add more fylr locations.

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
* In the drop down menu `Version` choose `original` and click the `Search` button.
* In the drop down menu `Action` choose `produce versions` .
* To the right select the round button below `Search result` (not below `Selected`).
* Click the `Action` button.

</details>

<details>

<summary>6.b Check whether all previews have been replaced</summary>

* Is the File queue empty at **https://**&#x66;ylr.example.co&#x6D;**/inspect/system/queues/?queue=file** ?\
  At the top it would show something like:\
  \&#xNAN;_` There are 18 parallel and 10 parallel high priority only file workers active. The queue`` `` `**`contains 0 total entries`**`.`_
* Surf to **https://**&#x66;ylr.example.co&#x6D;**/inspect/files/** (login as root)
  * In the drop down menu `location` choose `easydb versions` and click the `Search` button.
  * The Search shows zero results when all have been replaced.

</details>

<details>

<summary>6.c Remove easydb preview versions to regain storage (optional)</summary>

* At first remove the location `easydb versions` in the location manager. But leave the originals.
* Next, remove fylr's access to them (e.g. remove it from `/srv/fylr/docker-compose.yml` and recreate the container). But leave the originals.
* Check that the fylr webfrontend still shows previews, at https://fylr.example.com.
* Then, when all is still working, you can delete the easydb previews them to free storage capacity.\
  \
  **Warning**: Removing the preview versions of easydb should only be done if the easydb is not needed any more.\
  \
  **Warning** 2: But the easydb _**originals**_ are used by fylr, so **do never remove them**!

</details>

## 7. Remove easydb

These steps are optional but recommended, as easydb lifetime and support will end before fylr's.

Also check that you have uploaded a fylr license and tested/configured optional features that you need, e.g. Single Sign On, email sending, schema-sync via objectstore, hotfolder, etc..

<details>

<summary>7.a Replace easydb Indexer</summary>

Adjust `docker-compose.yml` to now feature Opensearch:

```
services:
  opensearch:
    [...not shown here: more opensearch details...]
```

Make sure fylr and Opensearch are in the same docker-network.

Change `fylr.yml` to use Opensearch:

```
fylr+:
[...]
  elastic+:
    addresses:
    - "http://opensearch:9200"
```

Start Opensearch and prepare its directory:

```
cd /srv/fylr
mkdir indexer
chown 1000 indexer
docker compose up -d opensearch ; docker logs -f opensearch
```

Stop outputting log messages with `Ctrl`-`c` if you have seen enough.

Restart fylr:

```
docker compose restart fylr ; docker logs -f --tail 0 fylr
```

Stop outputting log messages with `Ctrl`-`c` if you have seen enough.

Create the Indexes in Opensearch: _(might take a while!)_

Surf to **https://**&#x66;ylr.example.co&#x6D;**/inspect/** - System - `Reindex (Blocking)`

</details>

<details>

<summary>7.b Remove Apache</summary>

See the [default fylr installation](../../../for-system-administrators/installation/linux-docker-compose.md#installation) and adjust `docker-compose.yml` and `fylr.yml`. for default ports and certificate.

```
systemctl stop apache2
systemctl disable apache2
systemctl mask apache2
cd /srv/fylr
/srv/fylr/maintain fylr-recreate ; docker-compose logs -f fylr
```

Is certbot now also not needed any more? Then consider:

```
systemctl mask certbot.timer
```

</details>

**7.c Change fylr domain**

In case you want to change fylr's domain (e.g. to the former domain of easydb), see [here](../../../for-system-administrators/configuration/dns-domains.md#changes-to-the-main-domain).

**7.d Stopping easydb services**

Consider stopping all easydb services that are not needed any more (check whether you still use the indexer).

You may want to stop regular maintenance tasks for easydb, typically in `/etc/cron.d/easydb*`.
