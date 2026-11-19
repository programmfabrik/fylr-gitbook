---
description: >-
  What fylr is made of: the third-party software it ships, the license of
  each, and the SBOMs of a release.
---

# Third-party software

{% hint style="info" %}
Compiled from fylr **[v6.36.0](../releases/2026/v6.36.0.md)**, the newest release. Each release replaces these pages with its own.
{% endhint %}

fylr is built from third-party software: libraries compiled into the fylr binary and into the web frontend, and programs a fylr installation runs.

* [Legal notices](legal-notices.md): the license of fylr, and the license texts and copyright notices of the third-party software it contains, as fylr shows them under *About*. A release ships them as `LEGAL.md`, next to `LICENSE`.
* [Programs](programs.md): the open source programs fylr runs, and what for.

## SBOM

A release lists what it is made of as a Software Bill of Materials, in CycloneDX 1.6 (JSON). The ones of v6.36.0:

* [fylr_v6.36.0_sbom_image.cdx.json](https://s3.eu-central-1.wasabisys.com/fylr-releases/v6.36.0/fylr_v6.36.0_sbom_image.cdx.json): the container image: fylr, the programs it runs and the packages of its operating system.
* [fylr_v6.36.0_sbom_binary.cdx.json](https://s3.eu-central-1.wasabisys.com/fylr-releases/v6.36.0/fylr_v6.36.0_sbom_binary.cdx.json): the downloads: what the fylr binary links, and the web frontend inside it.

Every release has its SBOMs among the downloads on its page under [Releases](../releases/README.md), these on the page of [v6.36.0](../releases/2026/v6.36.0.md).
