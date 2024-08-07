---
description: >-
  For a migration or during testing, you might want to overwrite one fylr
  instance with data from another fylr or easydb, or just wipe a fylr
  installation to a clean state.
---

# Purge a fylr instance

As purging is a destructive intervention, many safety barriers have to be turned off before the purge can be done. These barriers protect data and assets in a productive fylr from being deleted.

## What a purge does

* replace the SQL database with a fresh one, erasing the data model, data, rights management
* reset configuration that was done in the web frontend ("[Base Configuration](../for-administrators/readme/)" etc.) to defaults or to the settings done in fylr.yml
* optionally, throw away all assets (and of course preview versions generated from them), if `Allow Purge` is chosen in the location manager. In the location manager `Allow Purge` is per location.
* after the purge, fylr uses other sub-directories inside your storage locations. Example:
* before purge: `/srv/fylr-7efd8b2b-afda-499a-b1e1-b90f6a5f426a`
* after purge: `/srv/fylr-e66a5fe2-05f4-4c99-a5c9-3f93e57405f5`

What a purge does not:

* change the configuration that is done in the configuration file **fylr.yml**
* if you do not allow purging of storage, your assets and preview version will remain on disk but are not used any more by fylr

## Allow purge

1. Make sure you have in your **fylr.yml**: `allowpurge: true`. Example:

```
fylr+:
  allowpurge: true

[...the rest of the file is omitted here...]
```

2. Allow purge in the fylr frontend, if not already set: Navigation bar - Cogwheels/**Administration** - **Base Configuration** - **Development** - **Purge**:

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption><p>the lower checkbox is optional, depending on whether you want to preserve the stored files</p></figcaption></figure>

3. If you want to purge storage: Allow per location: Navigation bar - Cogwheels/**Administration** - **Location Manager**: `Allow Purge` for those locations that you want to purge

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

## Start the purge

1. Surf to the inspect Web Frontend of fylr, by entering the URL of your fylr an adding `/inspect/`.

So if your fylr is available at [https://fylr.example.com](https://fylr.example.com) then surf to [https://fylr.example.com/inspect/](https://fylr.example.com/inspect/).

2. Click **System** and there click the `Purge...` button: (at the bottom)

<figure><img src="../.gitbook/assets/image (2) (2).png" alt=""><figcaption><p>The inspect web frontend at /inspect/system/</p></figcaption></figure>
