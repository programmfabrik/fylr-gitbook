---
description: How the software components work together
---

# Architecture

fylr is build on top of open source technologies:

* PostgreSQL
* OpenSearch (but also with Elasticsearch)
* Media processing tools: libvips, exiftool, ffmpeg, etc., see below

As a Go program, fylr runs on Linux, [on Windows](installation/windows.md) and on MacOS.

Under Linux it is usually deployed in our containers, via [docker](installation/#linux) or [kubernetes](installation/helm.md) :

<figure><img src="../.gitbook/assets/fylr-arch.svg" alt=""><figcaption></figcaption></figure>
