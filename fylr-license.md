---
description: This page describes the management of fylr licenses and license files.
---

# fylr License

## fylr license management

The fylr server comes with a license management. Once you have acquired a fylr license, you will be given a license file. This license file has to be entered into the fylr [base configuration](for-administrators/readme/).

The license determines

* How many production instances can be used
* How many test instances can be used
* Whether you licensed the edition workgroup, department or organization
* Which other fylr add-ons, plugins or extensions, can be used

{% hint style="info" %}
All fylr license editions grant you the permission to use the system with an unlimited number of users / user accounts (read and write accounts) and unlimited data. However this can be treated differently in the fylr cloud.
{% endhint %}

## License Editions

<table><thead><tr><th width="194">LICENSE EDITION</th><th width="210">INSTANCES</th><th>ADDITIONAL FEATURES</th></tr></thead><tbody><tr><td>Workgroup</td><td>1 production instance<br>0 test instance</td><td>All main fylr features</td></tr><tr><td>Department</td><td>1 production instance<br>0 test instance</td><td> + Authentication/ Single Sign-On</td></tr><tr><td>Organization</td><td>1 production instance<br>1 test instance</td><td> + Authentication/ Single Sign-On, Performance <br><br> + Kubernetes Installation (Horizontal Scaling)</td></tr></tbody></table>

## Capabilities

The capabilities extend the features of fylr enabled by the license:

* Authentication service LDAP & SAML
* CI-Hub-Integration for Adobe and Office products
* Mobile App connectivity
* Limit access to Read-Only

## The License file

The cryptographically signed license file contains:

* A list of allowed domains(`fylr.externalURL`), which can be used to access the fylr server / instance
* Edition of the license
* License file key
* The information, whether it's a _subscription_ license, or a license purchase (_buy_)
* A start and an end date, wherein the license is valid
* Enabled capabilities

{% hint style="info" %}
The license file check works offline, the license management does not include any online component.
{% endhint %}

## fylr with an invalid or no license

If you don't have a license key at all, or don't have a valid license key, you can start a fylr instance, nevertheless.

fylr can be used without or with an expired license if one of the following applies:

* The external URL `fylr.externalURL` is set to _localhost_ or ends in _.localhost_
* The user is main administrator (**system:root**). In this case, other users cannot log onto the system.

In case of an expired license, no data ist lost.

If you cancel a contract, which grants you the right to get fylr updates, which is linked to a license purchase (**buy**), you will not be able to use further updates. However, you are allowed to continue using all fylr versions, which were released before the cancelation / end date, since the license was bought.

## Next step: Download, install and test

To download, install and test fylr see these pages:

* Find the latest [fylr release](releases/) to download it
* [fylr Installation](for-system-administrators/installation/)
