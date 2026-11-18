---
description: >-
  What fylr is made of: the third-party software it ships, the license of
  each, and the SBOMs of a release.
---

# Third-party software

fylr is built from third-party software: libraries compiled into the fylr binary and into the web frontend, and programs a fylr installation runs. These pages describe **v6.36.0**, the newest release.

* [License terms](license-terms.md): the license of fylr and the license text of every library, as fylr shows them under *About*. A release ships them as `LEGAL.md`, next to `LICENSE`.
* [Libraries](libraries.md): the libraries and their licenses at a glance.
* [Programs](programs.md): the programs fylr runs, what for, and their licenses.

## SBOM

A release lists what it is made of as a Software Bill of Materials, in CycloneDX 1.6 (JSON). The ones of v6.36.0:

* [fylr_v6.36.0_sbom_image.cdx.json](https://s3.eu-central-1.wasabisys.com/fylr-releases/v6.36.0/fylr_v6.36.0_sbom_image.cdx.json): the container image: fylr, the programs it runs and the packages of its operating system.
* [fylr_v6.36.0_sbom_binary.cdx.json](https://s3.eu-central-1.wasabisys.com/fylr-releases/v6.36.0/fylr_v6.36.0_sbom_binary.cdx.json): the downloads: what the fylr binary links, and the web frontend inside it.

The page of every release under [Releases](../releases/README.md) links its own.
