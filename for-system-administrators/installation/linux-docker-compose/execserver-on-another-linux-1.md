---
description: >-
  How to outsource only processing with the tool ffmpeg (video files) to a
  separate linux
---

# ffmpeg on a separate fylr

This is a variation of the main installation method described [here](../linux-docker-compose.md#installation). So we will concentrate on the differences. ffmpeg is an example, you could equally do this with other asset processing tools used in fylr.

## Goal

1. One server with only the "execserver" part of fylr, which will be doing the heavy lifting of processing assets with **ffmpeg**, typically when big videos are uploaded.\
   We call this installation by its domain _**ff**_.example.com, here.
2. Another server with all the remaining jobs of fylr: Webfrontend, SQL, Indexing, etc.. \
   We call this installation by its domain _**main**_.example.com, here.

## On the system with ffmpeg

(We call this system _ff_.example.com)

* ensure that only _main_.example.com is allowed to reach port 8083 on _ff_.example.com (firewall, or private IP address, etc.)
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
    execserver+: # this is the local server config of ff.example.com's execserver
      # all: delete failed jobs, for preserving disk space. done: keep failed jobs, for debugging
      jobRemovalPolicy: all
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

* About backups: You will have no permanent data on this system: no assets, no database. Just a bit of configuration.

## On the main fylr system

(We call this system _main_.example.com)

* caveat: this particular case+config has not been tested by us yet, so use it as a starting point
* security: ensure that only _ff_.example.com and _main_.example.com are allowed to reach port 8080 and 8081 on _main_.example.com (firewall, or private IP address, etc.)
* pitfalls: on the hand, make sure that DNS and routing works in both execservers, in the container, to reach back to the main fylr. Also that firewalling does not block them.
* use a `fylr.yml` with these changes, the rest remains as in [the default installation](../linux-docker-compose.md#installation):

```
fylr+:
[...]
  execserver: # how to connect to the execservers (this is the "client" part)
    addresses:
      - http://ff.example.com:8083/job/ffmpeg?pretty=true
      - http://localhost:8083/?pretty=true
    parallel: 18
    parallelHigh: 10
    pluginJobTimeoutSec: 2400
    connectTimeoutSec: 120
    # the following tells the execservers how to connect back to the main fylr
    callbackBackendInternalURL: "http://main.example.com:8081"
    callbackApiInternalURL: "http://main.example.com:8080"

[...]
  services+:
[...]
    execserver+: # what the execserver at main.example.com does ("server" part)
      commands+: # the + tells fylr to use defaults unless explicitly overwritten
        ffmpeg:
          # overwritten with empty = should not be able to find ffmpeg
      services+:
        ffmpeg:
          # overwritten with empty = should not consider ffmpeg as a local service
```

* use a `docker-compose.yml` with these changes, the rest remains as in [the default installation](../linux-docker-compose.md#installation):

```
  fylr:
[...]
    ports:
      - "8080:8080" # fylr api
      - "8081:8081" # fylr backend
[...]
```
