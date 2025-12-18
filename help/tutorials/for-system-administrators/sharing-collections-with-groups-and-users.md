---
description: How to share collections with other fylr groups and users
---

# Sharing collections with groups and users

{% hint style="info" %}
Permissions for a user or group to see other users or groups can be assigned to both in the same way: Rights Management > select **user** or **group** > Tab: Permissions.

In the following tutorial permissions are assigned to groups only; the steps are identically applicable for  a user.
{% endhint %}

## Sharing collections with other users or groups

### Prerequisites for user sharing the collection

To share a collection with another group, the **sharing user needs permission to see other users**, to select them as recipients:

1.  System Rights > Frontend features > Allow Sharing to Users/Groups

    <figure><img src="../../../.gitbook/assets/Screenshot 2025-08-25 at 14.31.13.png" alt="" width="563"><figcaption></figcaption></figure>
2.  In rights management, in the **Permission Tab of a group or user**, add a permission row for the sharing group to allow finding the recipients using the Add-Icon <img src="../../../.gitbook/assets/Screenshot 2025-08-20 at 15.28.24.png" alt="" data-size="line">.

    <figure><img src="../../../.gitbook/assets/Screenshot 2025-08-25 at 14.35.36.png" alt="fylr group manager defining permissions for the &#x22;Editors&#x22; group to see members of group &#x22;Readers&#x22; and the group."><figcaption><p>fylr group manager defining permissions for the "Editors" group to see members of group "Readers" and the group.</p></figcaption></figure>
3. The sharing user needs permission to grant access to object types or masks.
   1.  in the rights management of the according location (object type / pool), the sharing user needs to be allowed **to grant access to the permission**.

       <figure><img src="../../../.gitbook/assets/Screenshot 2025-08-25 at 14.50.20.png" alt=""><figcaption><p>Group "Editors" has the permission to "View &#x26; Edit Records" of object type "Media". Additionally, the permission is grantable to the group, meaning members <strong>can grant the permission to other users</strong>.</p></figcaption></figure>





### Minimal requirements for the invited collection user

For the invited user the origin of view permissions can be split between:

* content permissions configured in Rights Management > your Pool or in RM > Object Type:
* permissions granted only to records in collections: configure the viewership rights in a **collection preset** or **grant custom permissions while sharing the collection.**



#### Minimal sharing setup:

If the object type you want to share is pool managed, find the Permission settings in Rights Management > Pools, in the Permissions Tab.

If the object type is not pool managed, find the same Permissions Tab in Rights Management > Object Types.

* at least a mask must be allowed for the recipients, so the user has visible fields they can see
* if we do not want recipients of the shared collection to see records which are not in the collection itself, we cannot allow the user to **View records** here.



Depending on the sharing user, they can choose a **collection preset** defining viewership rights or grant custom permissions while sharing the collection.

* the recipients group needs permissions to see the shared content inside the collection
  * in the sharing dialogue of the collection / permission preset allow the following permissions
    * **View Records**, **View Collection**



