---
description: >-
  As a Go program, fylr supports many platforms. For some installation
  scenarios, we prepared instructions and tools:
---

# Installation

{% hint style="info" %}
Please note: We do all of our automated and manual software testing based on Linux servers. There is no dedicated testing on Windows and almost no testing on Kubernetes.
{% endhint %}

## Linux

* Instructions and Requirements: [Linux](linux-docker-compose.md)
* Uses docker-compose.
* 3rd party tools for preview thumbnails are pre-packaged.
* If unsure, use this method when installing yourself.
* We offer maintenance contracts and hosting contracts for this variant.

## Windows

* Instructions and Requirements: [Windows](windows.md)
* We provide a list of 3rd party tools for preview thumbnails but not the tools themselves.

## Kubernetes

* Instructions: See our [helm chart](https://github.com/programmfabrik/fylr-helm/blob/main/charts/fylr/README.md).
* Uses helm charts and Linux containers.
* Needs helm and a kubernetes cluster.
* 3rd party tools for preview thumbnails are pre-packaged.
