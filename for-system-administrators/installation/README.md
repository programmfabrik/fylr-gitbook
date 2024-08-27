---
description: >-
  As a Go program, fylr supports many platforms. For some installation
  scenarios, we prepare instructions and tools:
---

# Installation

{% hint style="info" %}
Please note: We do all of our automated and manual software testing based on Linux servers. There is no dedicated testing on Windows and almost no testing on Kubernetes.
{% endhint %}

## Linux

* Instructions and Requirements: [Linux](linux-docker-compose.md)
* Uses docker-compose.
* 3rd party tools for thumbnails are pre-packaged.
* If unsure, use this method when installing yourself.
* We offer maintenance contracts and hosting contracts for this variant. Contanct us at e.g. support@programmfabrik.de.

## Windows

* Instructions and Requirements: [Windows](windows.md)
* We provide a list of 3rd party tools for thumbnails but not the tools themselves.
* Some of our partners offer maintenance contracts for this variant.

## Kubernetes

* Instructions: See our [helm chart](https://github.com/programmfabrik/fylr-helm/blob/main/charts/fylr/README.md).
* Uses helm charts and Linux containers.
* Needs helm and a kubernetes cluster.
* 3rd party tools for thumbnails are pre-packaged.
* We offer no support for this variant, just bugfixes for your reports to support@programmfabrik.de.

## Topics for all variants

### Troubleshooting

[fylr log messages that can be ignored](../symptom-and-solution/log-messages-that-can-be-ignored.md)
