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
* Requirements:
  * Uses Helm charts and Linux containers.
  * Needs Helm and a Kubernetes cluster.
* Features:
  * Third-party tools for thumbnails are pre-packaged.
  * A fylr instance can be started as many times as desired. Load balancing is handled externally (e.g., by a load balancer), not by fylr itself. All instances run in parallel, equally privileged, and share a common database.
  * A fylr instance can also be configured to act only [as an execution server](https://github.com/programmfabrik/fylr-helm/tree/main/charts/execserver#as-stand-alone-execserver). In such cases, its fylr.yml does not configure an API/web server, and it does not require a database. fylr servers notify the execution server when they have jobs to process. Horizontal scaling is most beneficial in this configuration.
* Licensing Notes: You need the fylr edition Organization to run fylr in a kubernetes environment.
* Monitoring: Every fylr instance shows how many others are currently connected in parallel.
* Support: We offer no support for this variant, only bug fixes for issues reported to [​support@programmfabrik.de](mailto:support@programmfabrik.de).

## Topics for all variants

### Software Versions

* We are regularly testing fylr with **PostgreSQL 17**. Customers with problems and PostgreSQL 14 (or even earlier versions) may be asked to upgrade PostgreSQL first.

### Troubleshooting

[fylr log messages that can be ignored](../symptom-and-solution/log-messages-that-can-be-ignored.md)
