---
description: How to enable and setup guest access to a fylr instance
---

# Enabling guest access

A fylr instance by default is only accessible for users with login credentials. However it is possible to configure an instance so any user can access and browse its contents without the need of creating or having a user account.

#### Enabling guest access

In the base configuration under access, enable the checkbox for **Guest Access**.

{% hint style="info" %}
Here you could also setup custom labels for the user login or setup self registration.
{% endhint %}

With this flag enabled, the instance is now publicly available and any user with knowledge of the URL can navigate to the instance without the need to login. In fylr those users are part of the group **Anonymous Users.**&#x20;

See also [#allow-guest-access](../../../for-administrators/readme/access.md#allow-guest-access "mention")

#### Provide content permissions to Anonymous Users

To actually see and browse content in a fylr instance the anonymous user group needs permissions defining what they can see and interact with.

Provide the user with the required permissions to interact with your instance:&#x20;

* **System Rights** (what features are available?)
  * set in Rights Management > Groups: Anonymous User > Tab: "System Rights"
  * The permission of **Frontend features** define what parts of the UI the anonymous user gets access to (Search, download, export, printing, collections etc.). Select the appropriate features required for the guest accessing your instance.
* **Permissions** (what content is available?)
  * set in Rights Management > Pools or Object Type > in Tab "Permissions"
  * Set at minimum the following permissions:
    * **View Records:** what Object Types is the anonymous user allowed to see?
    * **Allowed Masks:** what masks should the guest be able to see?
    * **View Versions:** to see media content of files uploaded, define what versions are allowed to be shown to the anonymous user

{% hint style="info" %}
If your Object Type isn't poolmanaged, you won't have to select explicit Object Types since your configuring inside the Object Types permissions already.

Linked object types used in your main Object Type need explicit permissions to be seen.
{% endhint %}

{% hint style="warning" %}
**Be careful** with which permissions are assigned to the Anonymous User Group - no authentication is needed. **Any user with the URL can access the instance and act with the permissions assigned.**
{% endhint %}

Read more about [permissions](../../../for-administrators/permissions/ "mention")

