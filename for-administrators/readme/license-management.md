---
description: The fylr user interface to upload and display your license
---

# License Management

### License Installation & Updates

To ensure your system runs without interruption, you must upload a valid license file provided by **programmfabrik**.

* In the **Configuration Base** locate the **License Management** section
* The license must be a valid **.json** file.&#x20;
* Locate the license upload section and select the file provided to you.

For more information on licenses, please refer to [fylr Licenses](../../license-management.md).

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption><p>Where to find license management</p></figcaption></figure>

### Expiration Warnings & Notifications

The licensing system includes an automated warning service to prevent disruption to your fylr instance. The mails cover the full lifecycle of a license; see [fylr version expiration](../../license-management.md#fylr-version-expiration) for the underlying rules.

#### Automatic Emails

Four kinds of mail are sent. All dates are formatted as DD.MM.YYYY.

**Subscription licenses**

* **Paid period ending soon** — sent before the license's end date, at:
  * **30 days**
  * **7 days**
  * **1 day**
* **Grace period ending** — sent during the two-month grace period that follows the end date, at:
  * **Weekly**, starting eight weeks before grace end (8, 7, 6, 5, 4, 3, 2 weeks)
  * **Daily** during the last week before grace end (7, 6, 5, 4, 3, 2, 1 days)
* **License expired** — sent once the grace period is over and the instance has switched to limited functionality.

**Buy licenses**

* **Binary too new** — sent when a fylr binary released after the license's end date is deployed. Such a binary will not run; install a binary released on or before the end date.

#### Recipients

By default, notifications are sent to the **Administrator Email(s)** defined in **Base Configuration** > **Email.** Additional recipients can be added to the license provided by programmfabrik.

{% hint style="info" %}
To add additional recipients after receiving your license, please **contact programmfabrik support.**
{% endhint %}
