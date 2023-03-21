---
description: >-
  In this section you find settings that affect the access of the fylr
  installation. Like opening the instance for anonymous users and password
  policy.
---

# Access

## General

### Allow guest access

Allows anonymous access. When activated, the fylr instance can be accessed without having a user account.

{% hint style="info" %}
Please note: when activated, the user group "Anonymous Users" need the system right "Access to Search" and permissions to the data. Using pools and tags, you can either give them access to all the data or just parts of it.
{% endhint %}

### Login Info Text

This text will be shown on the login page above the login fields.



## Password

### Hint for Unsupported Passwords

This message is displayed when a user sets a password and it does not meet the password requirements.

### Password Requirements

Use regular expressions to define requirements for passwords.



## Registration

### Allow user registration

Shows a "Sign Up" button when guests / anonymous users access fylr.

{% hint style="info" %}
Please note: this option requires that "Allow Guest Access" is enabled. The user group "Anonymous Users" also need the system right "Create Users".
{% endhint %}

### Registration Info Text

This text will be shown on the registration page above the input fields.&#x20;

### Form

Define which fields should be available for the users who want to sign up. For each field you have the following options:

| OPTION     | DESCRIPTION                           |
| ---------- | ------------------------------------- |
| Show       | Field will be shown and is optional.  |
| Don't Show | Field won't be shown.                 |
| Required   | Field will be shown and is mandatory. |

### Groups

Select groups that should be automatically assigned to a user who registers. Apart from these groups, users who sign up, are automatically assigned to the system group "Self-registered Users".
