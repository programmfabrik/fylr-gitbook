---
description: How to spread one fylr over two linux servers
---

# execserver on another linux

This is a variation of the main installation method described [here](../linux-docker-compose.md#installation). So we will concentrate on the differences.

## Goal

1. One server with only the "execserver" part of fylr, which will be doing the heavy lifting of processing assets, for example generating preview thumbnails. So it should have some CPU cores.\
   We call this one _**exec**_.example.com, here.
2. Another server with all the remaining parts of fylr, doing Webfrontend, SQL, Indexing, etc.. \
   We call this one _**main**_.example.com, here.

## On the system with the execserver

(We call this system _exec_.example.com)

* ensure that only _main_.example.com is allowed to reach port 8083 on _exec_.example.com (firewall, or private IP address, etc.)
* use a `fylr.yml` like this: (which disables all parts except execserver)

```
fylr+:
  logger+:
    timeFormat: "2006-01-02 15:04:05Z07"

  db:

  plugin:

  elastic:

  execserver: # no need to configure the client here, as this fylr is the execserver

  services+:
    execserver+: # this is the execserver
      # all: delete failed jobs, for preserving disk space. done: keep failed jobs, for debugging
      jobRemovalPolicy: done
      addr: :8083

    api:

    backend:

    webapp:

```

* use such a `docker-compose.yml` : (no postgreSQL, no Indexer)

```
services:
  fylr:
    image: docker.fylr.io/fylr/fylr:latest
    hostname: fylr.localhost
    container_name: fylr
    restart: always
    ports:
      - "8083:8083" # access for main fylr
    networks:
      - fylr
    volumes:
      - "/srv/fylr/config/fylr:/fylr/config"
    logging:
      driver: "journald"

networks:
  fylr:
```

* About backups: You will have no permanent data on this system, like: no assets, no database. Just a bit of configuration.

## On the system without the execserver

(We call this system _main_.example.com)

* ensure that only _exec_.example.com is allowed to reach port 8080 and 8081 on _main_.example.com (firewall, or private IP address, etc.)
* use a `fylr.yml` with these changes, the rest remains as in [the default installation](../linux-docker-compose.md#installation):

```
[...]
  execserver: # the following tells fylr where the execserver is
    addresses:
      - http://exec.example.com:8083/
    # without the + suffix this block replaces the shipped one, so these
    # two shipped values are repeated here
    pluginJobTimeoutSec: 2400 # the longest a plugin callback may run
    connectTimeoutSec: 120    # the longest a job waits for a free execserver slot
    # where the execserver calls back to the main fylr: fylr runs in a
    # container here and cannot see the address main.example.com itself
    callbackBackendOwnURL: "http://main.example.com:8081"

  services+:
    execserver: # this empty yaml branch with no leaves disables the execserver

[...]
```

There is no worker count to configure on _main_.example.com: from 6.35 one file dispatcher sizes itself from the slots of the connected execserver, and the execserver sizes its pool to its own CPUs (`slots`, see [performance tuning](../../configuration/performance-tuning.md)).

`connectTimeoutSec` is how long a job waits for a free slot, not a connection timeout. A file job that gets no slot in that time goes back into the file queue and is tried again a minute later, as often as it takes; a request whose client waits for the job, such as a plugin callback, fails with an error instead.

`callbackBackendOwnURL` is taken verbatim, port included. The API address handed to plugins takes its host from it and its port from the API listener, here `http://main.example.com:8080`. Before 6.35 this was set with `callbackBackendInternalURL` and `callbackApiInternalURL`; from 6.35 these two keep only scheme and port, never the host, see [Updating the execserver to 6.35](../updating-the-execserver-to-6.35.md).

* use a `docker-compose.yml` with these changes, the rest remains as in [the default installation](../linux-docker-compose.md#installation):

```
  fylr:
[...]
    ports:
      - "8080:8080" # fylr api
      - "8081:8081" # fylr backend
[...]
```
