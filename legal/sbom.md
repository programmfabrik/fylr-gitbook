---
description: >-
  The SBOMs of fylr: what a release is made of, fylr and the third-party
  software in it, for security scans.
---

# SBOM

{% hint style="info" %}
Compiled from fylr **[v6.36.0](../releases/2026/v6.36.0.md)**, the newest release. Each release replaces this page with its own.
{% endhint %}

A release lists what it is made of, fylr and the third-party software in it, as a Software Bill of Materials (SBOM) in CycloneDX 1.6 (JSON), which security scanners such as Trivy or Grype read. The ones of v6.36.0:

* [fylr_v6.36.0_sbom_image.cdx.json](https://s3.eu-central-1.wasabisys.com/fylr-releases/v6.36.0/fylr_v6.36.0_sbom_image.cdx.json): the container image: fylr, the programs it runs and the packages of its operating system.
* [fylr_v6.36.0_sbom_binary.cdx.json](https://s3.eu-central-1.wasabisys.com/fylr-releases/v6.36.0/fylr_v6.36.0_sbom_binary.cdx.json): the downloads: the fylr binary with what it links, and the web frontend inside it.

Releases before fylr 6.36 have no SBOM. From 6.36 on, the page of each release under [Releases](../releases/README.md) lists its two SBOMs among its downloads.
