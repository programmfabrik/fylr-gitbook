---
description: Fulfill requirements for Hotfolder
---

# How To Set Up As System Administrator

## File System Connect

In contrast to `Hotfolder`, the method `File System Connect` does not need preparation by the system administrator. It uses no real files system directory but relies only on webdav.&#x20;

## Hotfolder

In a typical installation of fylr, this is already done. But in some instances this still has to be done. There is no harm in trying to use Hotfolder without this step first and if fylr refuses to give you the hotfolder URL and points out this requirement instead, you know that this needs to be done.&#x20;

You need access to the configuration of fylr, typically a file called `fylr.yml` and you need to restart fylr to make it re-read its configuration.

Entry in the configuration that needs to be set, with some hierarchy above the entry for orientation:

```
fylr+:
  services+:
    api+:
      webDAVHotfolderPath: "/srv/hotfolder"
```

The path given needs to make sense in the container filesystem hierarchy.&#x20;

Typically, the path is mapped to the outside of the container to the server file system, for either space requirements or persistence. The [docker-compose.yml](../../\_assets/docker-compose.yml) given in our [installation instructions](../../for-system-administrators/installation/linux-docker-compose.md) does this implicitly by mapping an outside directory to `/srv` inside the container.
