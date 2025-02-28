---
description: How to connect fylr to a SAML authentication service.
---

# SAML

This can be used to log into fylr with users from e.g. Shibboleth and Azure ActiveDirectory.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption><p>Where to find the settings in the frontend.</p></figcaption></figure>

### Background

SAML 2.0 is an [XML](https://en.wikipedia.org/wiki/XML)-based [protocol](https://en.wikipedia.org/wiki/Communications_protocol) that uses [security tokens](https://en.wikipedia.org/wiki/Software_token) containing [assertions](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) to pass information about a principal (usually an end user) between a SAML authority, named an [Identity Provider](https://en.wikipedia.org/wiki/Identity_Provider), and a SAML consumer, named a [Service Provider](https://en.wikipedia.org/wiki/Service_Provider).

fylr acts as a Service Provider and as such needs to connect to an Identity Provider. For testing and to understand the configuration workflow, you can use the public Identity Provider [https://mocksaml.com](https://mocksaml.com).

## SAML with mocksaml.com

Follow this example to get into the workflow of configuring SAML with fylr.

First you need to generate a certificate and private key.

Background: The certificate will be entered in the fylr frontend's form fields and then be given to the Identity Provider as part of the metadata, so that requests coming from fylr are accepted. It is in addition to fylr's https certificate and not to be confused with that.

### Generate Certificate

This can be done where ever openssl is installed as a command line utility.

```bash
openssl genrsa -out private.key 2048
openssl req -new -x509 -key private.key -out publickey.cer -days 365
```

When asked for `Common Name (e.g. server FQDN or YOUR name)` answer with `fylr.example.eu` if your fylr is at [https://fylr.example.eu](https://fylr.exemple.eu).

Now you can view the contents of the files `private.key` and `publickey.cer` and put that into fylr's frontend: (**Certificate** and **Key** fields) as in this screenshot:

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption><p>screenshot of the form fields for certificate and key</p></figcaption></figure>

### Base Config

* As **URL** add [https://mocksaml.com/api/saml/metadata](https://mocksaml.com/api/saml/metadata) ("_metadata URL_**"** of the Identity Provider).
* We recommend to set the checkmark at **Log Steps**. This will write log events to debug SAML connections. In case of an error, the connection attempt is always logged.
* In **User Mapping** define how the SAML user is created in fylr. Upon each login the SAML users are mapped to fylr users. If an user already exists, an update is performed. Working with mocksaml.com:
  * Target: **Reference**: `%(email)s`
  * Target: **Email**: `%(email)s`

### Test Connection

Now go to the fylr login page (e.g. by logging out or using a second browser or private tab) and click on _**SAML Login**_ in the login dialog. This sends you to the login page of the Identify Provider. Login using any name and password (as written on that test login page). fylr will log the user in with no further rights (unless configured). Optionally check the User Manager in fylr to see that the user record has been created (you can only view this as a privileged user, e.g. root).

## What you might need with other providers

mocksaml.com is simplified. Here are some details you might need in a real world scenario.

* Target: **Login**: This can be used to determine the username during login, as in: The pair of username and Password used to log in. Example value: `%(login)s`. Or `%(sAMAccountName)s`. Has to match an attribute name that is actually present in your IDP's data.
* Target: **Display Name**:  Example value: `%(displayName)s`. Has to match an attribute name that is actually present in your IDP's data.
* Target: **Email**: <mark style="color:orange;">Note that email addresses in fylr have to be unique. The same email address cannot be used by two fylr users under any circumstances. fylr will not allow the email address to be saved a second time, preventing the login via SAML, if the email address is already present in fylr.</mark>
* Target: **Reference**: Make sure this is adjusted to your data. Do not just copy and paste. It can be very different from the above simple example. Another example:\
  `%(urn:oasis:names:tc:SAML:attribute:subject-id)s`
  * By default, **Reference** is used to determine whether a user already exists in fylr or whether to create a new one as a SAML user logs in. You may think of it as the unique ID.&#x20;
* **Benutzer-Update** (**User Update**): Set the attribute which is used to determine whether the SAML user (who is logging in) already has a matching account in fylr. If it has a matching account, that user is logged in (and attributes may get overwritten with the current values in SAML). If it has no matching account in fylr yet, a new one is being created. By default, the used attribute is **Reference**. But you can choose the attributes **Email** or **Login**, instead. \
  Example: Assume that the chosen attribute for **Benutzer-Update** is `Email` and that Alice logs in the first time with her SAML user alice@example.com. Company policy changes and thus her email address (in SAML) changes to alice.lastname@example.com. During her next login into fylr, a new user is being created, as there is no user yet with alice.lastname@example.com. Now Alice has two user accounts in fylr and can only log in to the second one.

More topics that you might need with other identity providers:

### fylr SAML Metadata

fylr's metadata URL is [https://FYLR.EXAMPLE.COM/api/saml/metadata](https://fylr.example.com/api/saml/metadata) (replace domain name with the one from your instance). You might need to give this URL to your Identity provider or you might have to call this URL yourself and then give the downloaded XML to your Identity provider.

### Signed AuthnRequest

Checkbox:  ☑︎ **Sign requests** (default off)

Some environments have the requirement that the SPs (in this case fylr) must sign the authentication requests.

Needs at least fylr v6.12.0.

### Group Mapping

Users of production Identity providers often have an attribute that groups user accounts together and can be used to give permissions in fylr to a whole group. We will assume an attribute called `role` to demonstrate a group mapping:

Mapping goal of the following example: Every role that ends in the letters `samltest.id` shall be automatically member of the fylr group `testidp`.

1. In fylr-URL/configmanager > `User management` > `SAML` add into the form field `Group Mapping` the value `%(role)s` (see following screenshot).

<figure><img src="../_assets/images/fylr-saml-group-mapping-en (1).png" alt=""><figcaption><p>How to add an attribute for SAML group mapping in the fylr frontend</p></figcaption></figure>

2. In fylr-URL/groupmanager add a group named `testidp`. Give that group some system rights that are visible after logging in.
3. In this group's configuration > `AUTHENTICATION SERVICES` > below `Single-Sign-On` add an entry with Method `Regular Expression` and Input `.*samltest.id` (see following screenshot).

<figure><img src="../_assets/images/fylr-group-mapping-en (1).png" alt=""><figcaption><p>How to match a value for a group mapping in the fylr frontend</p></figcaption></figure>

4. Save. Test the login as a SAML user with a matching role. The user now has the rights given to the group `testidp`.
