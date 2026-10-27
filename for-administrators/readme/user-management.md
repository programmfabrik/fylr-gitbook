---
description: >-
  In this section you can add a LDAP or SAML authentication, configure a OAuth
  service or define what should happen when deleting a user.
---

# User Management

<div align="left"><figure><img src="../../.gitbook/assets/image (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

## User Management

### Handling When Deleting Users

Define what should happen, when someone deletes a user in the user management.

| OPTION  | DESCRIPTION                                                                                                                                                    |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ask     | When someone clicks on the minus to delete a user, they'll be asked if the user should be archived or deleted.                                                 |
| Archive | When someone clicks on the minus to delete a user, the user will be archived. Archived users can't access the system but can be un-archived by administrators. |
| Delete  | When someone clicks on the minus to delete a user, the user will be deleted. Deleted users can't access the system.                                            |

{% hint style="warning" %}
Please note, that in both cases "Archive" and "Delete", the collections of the users will be deleted and cannot be restored.
{% endhint %}

### Store User in Events

Enable all event types that should store the user. Otherwise the event will not be connected to a user.

### Copy User Data to Events

Define which data of the user should be copied to the events. This is independent from the event user. If the user get's deleted or pseudonymized, this data remains in the events.

### New User Notification

From fylr **6.36.0** an email goes to the recipients when fylr creates a user in one of the selected ways. A way can be selected once it is set up:

| OPTION            | DESCRIPTION                                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Self-Registration | Someone sends the registration form. The email goes out right away, before the new user has confirmed the address. Selectable while [user registration](access.md#allow-user-registration) is allowed. |
| First SAML Login  | Someone logs in through [SAML](#saml) for the first time. Selectable while SAML has an IdP metadata URL.                                                                                                 |
| First LDAP Login  | Someone logs in through [LDAP](#ldap) for the first time. Selectable while LDAP has a connection with a URL.                                                                                             |

**Recipients** are the email addresses that get the email. The list is shown once one of the ways is selected.

The email names the user (name, login, email address), the way they came in and the groups the SAML or LDAP group mapping gave them, and links to the user in the user management. Users that an administrator creates or that a restore brings in are not reported. Nothing is sent while the [server address](email.md#server-address) or the [sender address](email.md#from) of the email configuration is empty.

## OAuth-Service

Add pairs of Client IDs and Secrets for the [OAuth2 Authentication](../../for-developers/api/oauth2.md#configuring-client-id-and-secret).

* **Name**: Name of the Client (used as Client ID)
* **Secret**: Client Secret, must be entered as a [Bcrypt Hash](https://bcrypt-generator.com/)
* **Redirect URIs**: List of callback URLs to the local client, needed for some OAuth2 Authentication flows
* **Expiration Time: Access Token**: Time after which the Access Token expires and needs to be refreshed, default: 24 hours
* **Expiration Time: Refresh Token**: Time after which the Refresh Token expires, default: 720 hours

## OpenID Userinfo

Select which user information should be returned by the `oauth2/userinfo` endpoint. (The section keeps its "OpenID" name for the conventional endpoint path; fylr is not an OpenID Connect provider.)

***

## LDAP

This big topic has [its own page](../../tutorials/ldap.md) in our Tutorials.

## SAML

This big topic has [its own page](../../tutorials/auth/saml/) in our Tutorials.
