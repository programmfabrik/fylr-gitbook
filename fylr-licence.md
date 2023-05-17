---
description: This page describes the management of fylr licences and licence files.
---

# fylr Licence

## fylr licence management

The fylr server comes with a license management. Once you have acquired a fylr license, you will be given a license file. This license file has to be entered into the fylr base configuration.

The license determines

* how many production instances can be used
* how many test instances can be used
* whether you licensed the edition workgroup, department or organization
* which other fylr add-ons, plugins or extensions, can be used

_**All fylr license editions grant you the right to use the system with an unlimited number of user/user accounts - read and write accounts - and unlimited data**_. How ever this can be treated differently in the fylr Cloud.

## Licence Overview

<table><thead><tr><th>License edition</th><th data-type="number">Production instances</th><th data-type="number">Test instances</th><th>Additional Features</th></tr></thead><tbody><tr><td>Workgroup</td><td>1</td><td>0</td><td>All main fylr features</td></tr><tr><td>Department</td><td>1</td><td>0</td><td> + Authentication/ Single Sign-On</td></tr><tr><td>Organization</td><td>1</td><td>1</td><td> + Authentication/ Single Sign-On, Performance <br><br> + Kubernetes Installation (Horizontal Scaling)</td></tr></tbody></table>

## Add-Ons

These add-ons, which are either plug-ins or extensions, are available:

* Extension - Add 1 test/staging instance
* Extension - Add 1 production and 1 test/staging instance (License edition Department or Organization needed. Limit of a maximum of 5 production instances in License edition Department)
* Plugin - (CI-Hub)-Integration to Adobe and/or Office
* Plugin - CMS Typo3, WordPress or Drupal, each
* Plugin - Connect to external tagging service
* Plugin - The fylr server can be used the fylr mobile app, too

## The Licence file

The license file also contains

* a list of allowed external URLs (fylr.externalURL), which can be used to access the fylr server / instance
* the information, whether it's a "subscription" license, or a license purchase ("buy") a start and an end date, wherein the licence is valid

The licenses files are signed.

Please note, that there is no connection to a central licence server established, to check your licence. In fact there is no such a service. The license file check works offline, the license management does not include any online component.

If needed the licence file can limit a fylr instance to read-only capabilities.

## fylr with an invalid or no licence

If you don't have a license key at all, or don't have a valid license key, you can start a fylr instance, nevertheless. fylr can be used without or an expired license as follows:

* if the list of allowed external URLs (fylr.externalURL) is set to "localhost" only or ends in ".localhost"

AND

* if the user is the main administrator (system:root)

If fylr runs with an expired or invalid license, other users than main administrator (system:root) cannot login to the system.

If you cancel a contract, which grants you the right to get fylr updates, which is linked to a license purchase ("buy"), you will not be able to use updates any longer. However you are allowed to continue using all fylr version, which were released before the cancelation / end date, since the license was bought.

## Next step: Download, install and test

To download, install and test fylr see these pages.

* Find the latest [fylr release](releases/) to download it
* [fylr Installation](for-system-administrators/installation/)
