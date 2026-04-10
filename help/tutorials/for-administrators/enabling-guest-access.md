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

Provide the user with the required permissions to interact with your instance.&#x20;

* System Rights - frontend permissions define what features the anonymous user gets access to (search, download, export, printing, collections etc.)
* Content permissions (given in Pool or in the Object Type)
  * What object types is the anonymous user allowed to see? Assign the permission **View Records** and select the corresponding object types.&#x20;
    * ℹ️ Linked object types used in your main object type need explicit permissions!
  * What masks are they allowed to see?&#x20;
  * What version/ rendition are they allowed to see?&#x20;

See also [permissions](../../../for-administrators/permissions/ "mention")

{% hint style="warning" %}
**Be careful** with which permissions are assigned to the Anonymous User Group - no authentication is needed. **Any user with the URL can access the instance and act with the permissions assigned.**
{% endhint %}



