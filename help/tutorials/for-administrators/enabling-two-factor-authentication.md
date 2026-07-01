---
description: >-
  How to enable two-factor authentication (2FA) for local fylr accounts, which
  methods are available, and what to keep in mind so users don't get locked out.
---

# Enabling Two-Factor Authentication

Two-factor authentication (2FA) adds a second step to the login: after entering their password, a user must confirm a second factor before they are signed in. In fylr this applies to **local accounts** (user types _easydb_ and _self-registered_). Users who authenticate outside of fylr — SAML, OIDC/SSO and LDAP — are handled by their identity provider and are not covered by fylr's 2FA.

fylr offers three second factors, which you enable individually:

* **Email** – a 6-digit one-time code is sent to the user's email address after the password step.
* **Authenticator app (TOTP)** – a time-based code from an app such as Google Authenticator or Microsoft Authenticator.
* **Passkey** – a WebAuthn credential confirmed by the device (fingerprint, face recognition or a security key). A passkey can also be used for passwordless sign-in.

{% hint style="info" %}
Two-factor authentication is available from fylr **6.34.0**.
{% endhint %}

## Before you start

* **License** – 2FA requires a license that includes the two-factor capability. If the **Two-factor authentication** section in the base configuration is greyed out, your license does not include it — contact Programmfabrik to have the license re-issued. Existing Department and Organization licenses may need to be re-issued to carry the capability. Unlicensed local instances have 2FA available for testing.
* **Local accounts only** – only _easydb_ and _self-registered_ users are challenged. SAML / SSO / LDAP users are not.
* **Mail server (for the email method)** – the email one-time code can only be sent if a mail server is configured. Without it, the email method is not offered. See [Email](../../../for-administrators/readme/email.md "mention").

## 1. Enable 2FA in the base configuration

Open the **Base Configuration** and go to **Access → Two-factor authentication**.

* Tick **Enabled**.
* Under **Methods**, select at least one of **Email**, **Authenticator app (TOTP)** and **Passkey**.

{% hint style="info" %}
At least one method must be selected — the configuration cannot be saved with 2FA enabled and no method. If you enable more than one method, users get a picker at login and can choose.
{% endhint %}

Enabling 2FA here only makes it _available_. It does not yet require it from anyone — that is done per group in the next step.

## 2. Require 2FA for the relevant groups

Go to **Rights Management → Groups**, select a group, and enable **Require two-factor authentication** in its settings.

Every user who is a member of at least one group with this flag set must pass a second factor at login.

{% hint style="info" %}
The **Require two-factor authentication** checkbox is disabled until 2FA is enabled in the base configuration (step 1). Enable 2FA there first, then set the flag on the groups.
{% endhint %}

See [Groups](../../../for-administrators/permissions/groups.md "mention") for how groups and memberships work.

## 3. What users experience

The first time an enforced user logs in, fylr guides them through what is needed for the enabled method(s):

* **Email** – works immediately if the user has an email address. After the password step a code is emailed and the user enters it.
* **Authenticator app (TOTP)** – on first login the user is walked through setup: they scan a QR code with their authenticator app, then enter the current code to confirm. On later logins they just enter the current code.
* **Passkey** – on first login the browser's passkey ceremony is used to create the credential (fingerprint, face recognition or a security key). On later logins the device confirms the sign-in.

With more than one method enabled, the user picks one at first login; later logins go straight to the last-used method, with a **"use a different method"** link to switch. Wrong email/TOTP codes are limited (3 attempts by default) before the user has to start the login over.

{% hint style="info" %}
**Passwordless sign-in:** when the passkey method is enabled, the login form also offers **"Sign in with passkey"** — no username or password. Because a passkey combines possession (the device) with biometrics, this counts as a full two-factor login.
{% endhint %}

## 4. Managing a user's 2FA

Open the user in **Rights Management → Users**. The user editor shows the enrollment status per method (Authenticator app / Passkey) and a **Reset** link for each. Resetting clears that enrollment; the user is walked through setup again at their next login.

Users can also see and reset their own authenticator app / passkey enrollment in their personal **settings**.

## What to watch out for

This is the part to plan for before you enforce 2FA on real accounts.

{% hint style="warning" %}
**There are no backup or recovery codes.** If a user loses their authenticator app or passkey device, they cannot get in on their own — an administrator has to **reset** their enrollment in the user editor (step 4). Make sure administrators are reachable for this.
{% endhint %}

* **`root` is always exempt.** The `system:root` user is never challenged, so it stays your recovery path if everyone else is locked out. Keep the root credentials safe and working.
* **Users without an email address, when email is the only method, are not challenged.** They log in with password only — silently. If you rely on the email method, make sure enforced users actually have an email address, or additionally enable the authenticator app / passkey so there is always a usable second factor.
* **API password login (OAuth2 password grant) cannot present a second factor.** For enforced users it is therefore **refused by default**. If you have API clients or scripts that log in with a username and password, either keep those accounts out of enforced groups (and use API tokens instead), or turn on **Allow password grant** in the Two-factor authentication section — which keeps those clients working but means their logins skip the second factor.
* **The email method needs a configured mail server** (see _Before you start_). No mail server → the email method is not offered.
* **Enrollment happens at login.** There is no self-service enrollment before the first login: TOTP and passkey are set up when the enforced user next signs in; the email method just works if an address is present.

The `USER_LOGIN` event records which second factor was used (in its `two_factor` field), so you can verify in the event log that 2FA is actually taking effect.

## Related pages

* [Access](../../../for-administrators/readme/access.md "mention") — the base-configuration section where 2FA is enabled.
* [Groups](../../../for-administrators/permissions/groups.md "mention") — where the "Require two-factor authentication" flag is set.
