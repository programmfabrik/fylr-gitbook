---
description: >-
  Before using the Hotfolder or File System Connect, some preparations are
  necessary. Most settings can be made by an administrator, but in some cases
  also a system administrator is needed.
---

# Preparations Before Usage

## Hotfolder

In a **typical** installation of FYLR, this is already **done**. But in some instances this still has to be done by a **system administrator**. There is no harm in trying to use the Hotfolder without this step first and if FYLR refuses to give you the Hotfolder URL and points out this requirement instead, you know that this needs to be done.&#x20;

You need **access** to the **configuration** of FYLR, typically a file called `fylr.yml` and you need to **restart** FYLR to make it re-read its **configuration**.

Here is the entry, that **needs** to be set in the **configuration**: (with some hierarchy above the entry for orientation)

```
fylr+:
  services+:
    api+:
      webDAVHotfolderPath: "/srv/hotfolder"
```

The **path** given needs to make sense inside the _**container**_**&#x20;filesystem** hierarchy.&#x20;

Typically, the path is mapped to the outside of the container to the server file system, for space requirements or persistence. The [docker-compose.yml](../../_assets/docker-compose.yml) given in our [installation instructions](../../for-system-administrators/installation/linux-docker-compose.md) does this implicitly by mapping an outside directory to `/srv` inside the container.



## File System Connect

In contrast to `Hotfolder`, the method `File System Connect` **does not need preparation** by the **system administrator** and can be **set up** and **used directly**. It uses no real file system directory but relies only on **WebDAV**.&#x20;



## Activate Services

**Additionally** the **upload** needs to be **enabled**: Go to **Base Configuration** > **Services** and enable "**Activate Hotfolder**" and / or "**Activate File System Connect**".

<div data-full-width="false"><figure><img src="../../.gitbook/assets/Base Configuration  Services  WebDAV" alt=""><figcaption></figcaption></figure></div>

## Permissions

In order for **users** to be **able** to use the **Hotfolder** or **File System Connect**, a few **permissions** still need to be **assigned**.&#x20;

The **users** (or user groups) **need** the **system rights** "**Access Search**" with "**Create Collections**" or "**Access Quick Access Only (No Search)**" as well as "**Frontend Features > Show File System Connect URL**" (for the File System Connect). For more details please refer to the [permissions](../../for-administrators/permissions/).

**Additionally** the users (or user groups) also **need** the permission to **create new records**, **upload files** and **read permissions** to at least one **pool**. This can be defined under "**Pools**". For more details please refer to [permissions](../../for-administrators/permissions/).
