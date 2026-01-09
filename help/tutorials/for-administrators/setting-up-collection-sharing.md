---
description: >-
  This tutorial explains how to configure fylr so that users or user groups can
  share collections with other users, groups, or external recipients.
---

# Setting Up Collection Sharing

## **Prerequisites for the Sharing User**

Before a user can share a collection with others, they must have the appropriate **permissions** configured. These are set in three main steps:

### **1. Allow Sharing**

To enable a user to share collections:

* Navigate to: **Users or Groups → \[**_**Select the User or Group**_**] → System Rights → Frontend Features**.
* Enable the following options depending on the desired functionality:
  * **Allow Sharing to Users/Groups** – enables sharing with internal users or groups.
  * **Enable Sharing Links for External Access** – allows sharing with external recipients (skip step 2 if this is enabled).
  * **Create Email User** – allows creating external email users for sharing (skip step 2 if this is enabled).

### **2. Allow Finding Recipients**

To allow a user to select other users or groups when sharing collections:

* Navigate to: **Users or Groups → \[**_**Select the User or Group**_**] → Permissions Tab**.
* Add a new **permission row** for the sharing group.
* Select the **user or group** that should be accessible.
* Assign **at least "Read" permissions** for the records.

{% hint style="info" %}
If **User A** should be able to share collections with **User B**, you must edit **User B** (or the group they belong to) and add **User A** (or the group User A belongs to) in the permissions tab. This ensures that User A can find and share collections with User B.
{% endhint %}

### **3. Allow Granting Access**

To share records with other users, the sharing user must be authorized to **grant permissions**. This requires the **Granable** permission for all access rights the user intends to assign to others for the records in the collection:

* Go to: Rights Management > Pools > \[_Select Pool_] > Permissions Tab

## **Requirements for the Invited User/Group**

Invited users must have the **minimum required permissions** to view the shared content.

If the **object type is pool-managed**, configure permissions under

* Rights Management → Pools → \[Select the Pool] → Permissions.

If the **object type is not pool-managed**, configure permissions under

* Rights Management → Object Types → \[Select the Object Type] → Permissions.

At least **one mask** must be granted for the users or groups that should be able to receive shared collections (for email users use the system group "Users Invited by Email", and for the link for external access use the system group "Anonymous Collection Users"). This is required so users can **see fields** when viewing records.&#x20;

{% hint style="info" %}
If you want users to **access records only through the shared collection** and not see records outside of it, do **not** grant the "**View Records"** permission at the pool or object type level.
{% endhint %}

## **Sharing the Collection**

When sharing a collection, the recipient must be **granted at least the following permissions**:

* View Records
* View Collection

These permissions can be assigned in one of the following ways:

* **Using a collection preset**, which applies a predefined set of permissions configured by an administrator.
* **Granting custom permissions directly in the sharing dialog**. This option is only available to users who have the system permission "**Allow to Set Custom Sharing Permissions"**.
