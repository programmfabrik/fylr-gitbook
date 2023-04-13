---
description: >-
  In this section you can add a LDAP or SAML authentication, configure a OAuth
  service or define what should happen when deleting a user.
---

# User Management

## User Management

### Handling When Deleting Users

Define what should happen, when someone deletes a user in the user management.

| OPTION  | DESCRIPTION                                                                                                                                                    |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ask     | When someone clicks on the minus to delete a user, they'll be asked if the user should be archived or deleted.                                                 |
| Archive | When someone clicks on the minus to delete a user, the user will be archived. Archived users can't access the system but can be un-archived by administrators. |
| Delete  | When someone clicks on the minus to delete a user, the user will be deleted. Deleted users can't access the system.                                            |

### Store User in Events

Enable all event types that should store the user. Otherwise the event will not be connected to a user.&#x20;

### Copy User Data to Events

Define which data of the user should be copied to the events. This is independent from the event user. If the user get's deleted or pseudonymized, this data remains in the events.



## OpenID Userinfo





## OAuth-Service



## LDAP



## SAML



