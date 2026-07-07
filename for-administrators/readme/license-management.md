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

The licensing system includes an automated warning service to prevent disruption to your fylr instance.

#### Automatic Emails

Warnings are sent via email before the license **end date**:

* **30 days**, **7 days** and **1 day** before the end date.

Once the end date has passed, fylr enters a two-month [grace period](../../license-management.md#grace-period) and keeps reminding you that it is running out:

* **weekly**, starting eight weeks before the grace period ends, and
* **daily** during the last week before the grace period ends.

A separate notice is sent once the grace period is over, and — for _buy_ licenses — when a fylr binary released after the license end date is deployed (_binary too new_). All dates in these mails use the DD.MM.YYYY notation.

By default, notifications are sent to the **Administrator Email(s)** defined in **Base Configuration** > **Email.** Additional recipients can be added to the license provided by programmfabrik.

{% hint style="info" %}
To add additional recipients after receiving your license, please **contact programmfabrik support.**
{% endhint %}
