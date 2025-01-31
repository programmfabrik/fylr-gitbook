---
description: >-
  Overview of fylr licenses and how they define the capabilities of a fylr
  installation.
---

# License

For all installations a fylr license is required, except for a quick peek and for development.

## License contract & Licenses

Once you have signed a fylr license contract, you will be given a fylr license. Depending on your license contract this can be one license or several licenses. This license has to be entered into the [license management](for-administrators/readme/license-management.md#upload-your-license) in the Base Configuration or has to be made part of the fylr.yml configuration.

The license contract determines:

* How many production instances can be used
* How many test instances can be used
* Whether you licensed the edition workgroup, department or organization
* Which other fylr add-ons, plugins or extensions, can be used

## License Editions

<table><thead><tr><th width="194">LICENSE EDITION</th><th width="210">INSTANCES</th><th>ADDITIONAL FEATURES</th></tr></thead><tbody><tr><td>Workgroup</td><td>1 production instance<br>0 test instance</td><td>All main fylr features</td></tr><tr><td>Department</td><td>1 production instance<br>0 test instance</td><td> + Authentication/ Single Sign-On</td></tr><tr><td>Organization</td><td>1 production instance<br>1 test instance</td><td> + Authentication/ Single Sign-On <br> + Kubernetes Installation (Horizontal Scaling)</td></tr></tbody></table>



{% hint style="info" %}
All fylr license editions grant you the permission to use the system with an unlimited number of users / user accounts (read and write accounts) and unlimited data. However this can be treated differently in the fylr cloud.
{% endhint %}

## License Add-ons

In your license contract you can choose from these license add-ons, which are either extensions or plugins:

* Extension - Add 1 test instance
* Extension - Add 1 production and 1 test instance\
  (License Edition Department or Organization needed. Limit of a maximum of 5 production instances in License Edition Department.)
* Plugin - CI-Hub-Integration for Adobe and Office products
* Plugin - CMS Typo3, WordPress or Drupal, each
* Plugin - Connect to external tagging service
* Plugin - Mobile App connectivity

## Capabilities

Based on the fylr license contract the enabled capabilities are defined in the fylr license. They extend the features of fylr.

* Authentication service LDAP & SAML
* CI-Hub-Integration for Adobe and Office products
* Mobile App connectivity
* Limit access to Read-Only

## License

The cryptographically signed license contains:

* A list of allowed domains(`fylr.externalURL`), which can be used to access the fylr server / instance
* Edition of the license
* License key
* The information, whether it's a _subscription_ license, or a _buy_ license
* A start and an end date, wherein the license is valid
* Enabled capabilities

{% hint style="info" %}
The license check works offline, the license management does not include any online component.
{% endhint %}

## fylr version expiration

A fylr version can expire for two reasons:

* The license has an expiration date set
* The binary of the fylr version is older than 1 year

In case of expiration fylr runs with a limited functionality (see below). Please contact our team to help you, if you find yourself in that situation.

This limitation does not apply if all of the following applies:

* the license is of type _buy_
* the fylr binary was released before the license expire date

{% hint style="info" %}
Administrators (configured in the base config email section) will receive an email warning 30, 5 and 1 day prior to the expiration.
{% endhint %}

## fylr with an invalid or no license

If you don't have a license key at all, or don't have a valid license key, you can start a fylr instance, nevertheless.

fylr can be used without or with an expired license if **one** of the following applies:

* The external URL `fylr.externalURL` is set to _localhost_ or ends in _.localhost_
* The fylr user account **root** is used. Other users can only log into localhost (see above).

In case of an expired license, no data ist lost.

If you cancel the subscription contract, you will not be able to use fylr from the cancellation/end date.

If you cancel a contract, which grants you the right to get fylr updates, which is linked to a license purchase (buy), you will not be able to use further updates. However, you are allowed to continue using all fylr versions, which were released before the cancelation / end date, since the license was bought.

## Next step: Download, install and test

To download, install and test fylr see these pages:

* Find the latest [fylr release](releases/) to download it
* [fylr Installation](for-system-administrators/installation/)
* [upload your fylr license](for-administrators/readme/license-management.md#upload-your-license)

