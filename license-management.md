---
description: >-
  Overview of fylr licenses and how they define the capabilities of a fylr
  installation.
---

# License

For all installations a fylr license is required, except for [cases explained below](license-management.md#fylr-with-an-invalid-or-no-license).

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

### Plugin capabilities

From fylr **6.35.0**, the license can also determine which **plugins** an instance is allowed to **enable**, through a plugin capability map in the license:

* A plugin the license **names and grants** can be enabled normally.
* A plugin the license **names without granting** it is **force-disabled** at runtime, and enabling it over the API or the [Plugin Manager](for-administrators/plugin-manager/README.md) is refused (`PluginNotLicensed`). Its stored `enabled` flag and configuration are **preserved**, so the plugin re-enables by itself once the license grants it again.
* Plugins the license does **not name at all** stay **unrestricted**.

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

How long a fylr version can be used depends on the license type — _subscription_ or _buy_ — and, for buy licenses, on when the running binary was released.

### Subscription licenses

A subscription license is purely time-based. fylr can be used until the license **end date**, followed by a **two-month grace period** (see [below](#grace-period)). The age of the fylr binary no longer plays a role — a subscription is not affected by how old the running fylr version is.

### Buy licenses

A buy license does not expire in time — fylr can be used indefinitely. Its end date is instead a **cutoff for binaries**: a fylr binary **released up to the end date runs indefinitely**, while a binary **released after the end date is refused** as _too new_ and will not run. To move to a newer fylr version, the buy license has to be renewed.

### Grace period

When a license reaches its end date, fylr does not stop immediately. It enters a **two-month grace period** (end date + 2 months) during which it keeps running normally. Only once the grace period is over does fylr fall back to [limited functionality](#fylr-with-an-invalid-or-no-license).

The license validation reports the end of the grace period as the **grace to** date (end date + two months), which the [License Management](for-administrators/readme/license-management.md) view shows next to the end date.

### Warning emails

Administrators (configured in the base config email section) receive warning emails so an expiring license never comes as a surprise. All dates in these mails use the DD.MM.YYYY notation.

* **Paid period ending** — 30, 7 and 1 day before the end date.
* **Grace period ending** — during the grace period: weekly starting eight weeks before the grace end, then daily in the last week before it.
* **License expired** — once the grace period is over.
* **Binary too new** (buy licenses) — when a binary released after the license end date is deployed.

In case of expiration fylr runs with a limited functionality (see below). Please contact our team to help you if you find yourself in that situation.

## fylr with an invalid or no license

If you don't have a license key at all, or don't have a valid license key, you can start a fylr instance, nevertheless.

fylr can be used without or with an expired license if **one** of the following applies:

* The external URL `fylr.externalURL` is set to _localhost_ or ends in _.localhost_. This is aimed at development of fylr and of plugins.
* The fylr user account **root** is used. This makes sure that you can always reach the part of fylr where to uplaod licenses. Other users can only log into localhost (see above).

In case of an expired license, no data ist lost.

If you cancel the subscription contract, you will not be able to use fylr from the cancellation/end date.

If you cancel a contract, which grants you the right to get fylr updates, which is linked to a license purchase (buy), you will not be able to use further updates. However, you are allowed to continue using all fylr versions, which were released before the cancelation / end date, since the license was bought.

## Next step: Download, install and test

To download, install and test fylr see these pages:

* Find the latest [fylr release](releases/) to download it
* [fylr Installation](for-system-administrators/installation/)
* [upload your fylr license](for-administrators/readme/license-management.md#upload-your-license)

