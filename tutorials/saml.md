---
description: How to connect fylr to a SAML authentication service.
---

# SAML

This can be used to log into fylr with users from e.g. Shibboleth and Azure ActiveDirectory.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption><p>Where to find the settings in the frontend.</p></figcaption></figure>

Background: SAML 2.0 is an [XML](https://en.wikipedia.org/wiki/XML)-based [protocol](https://en.wikipedia.org/wiki/Communications\_protocol) that uses [security tokens](https://en.wikipedia.org/wiki/Software\_token) containing [assertions](https://en.wikipedia.org/wiki/Security\_Assertion\_Markup\_Language) to pass information about a principal (usually an end user) between a SAML authority, named an [Identity Provider](https://en.wikipedia.org/wiki/Identity\_Provider), and a SAML consumer, named a [Service Provider](https://en.wikipedia.org/wiki/Service\_Provider).

fylr acts as a Service Provider and as such needs to connect to an Identity Provider. For testing and to understand the configuration workflow, you can use the public Identity Provider [https://samltest.id/](https://samltest.id/).

At some point you will need: fylr's endpoint to get the required metadata XML. It is [http://localhost/api/saml/metadata](http://localhost/api/saml/metadata) (replace _localhost_ with the domain of your fylr server, and probably http with http**s**).

## SAML with samltest.id

Follow this example to get into the workflow of configuring SAML with fylr.

First you need to generate a certificate and private key.

Background: The certificate will be entered in the fylr frontend's form fields and then be given to the Identity Provider as part of the metadata, so that requests coming from fylr are accepted. It is in addition to fylr's https certificate and not to be confused with that.

### Generate Certificate

This can be done where ever openssl is installed as a command line utility.

```bash
openssl genrsa -out private.key 1024
openssl req -new -x509 -key private.key -out publickey.cer -days 365
```

Now you can view the contents of the files `private.key` and `publickey.cer` and put that into fylr's frontend: (**Certificate** and **Key** fields)

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### Base Config

* As **URL** add [https://samltest.id/saml/idp](https://samltest.id/saml/idp) (this is the Identity Provider).
* We recommend to set the checkmark at **Log Steps**. This will write log events to debug SAML connections. In case of an error, the connection attempt is always logged.
* In **User Mapping** define how the SAML user is created in fylr. Upon each login the SAML users are mapped to fylr users. If an user already exists, an update is performed. Working with samltest.id:
  * Target: **Reference**: `%(urn:oasis:names:tc:SAML:attribute:subject-id)s`
    * By default, **Reference** is used to determine whether a user already exists in fylr or whether to create a new one; when a SAML user logs in. You may think of it as the unique ID. This default can be changed in the field **Benutzer-Update** (User Update), to e.g. use Email as the unique ID instead.
  * Target: **Display Name**: `%(displayName)s`
  * Target: **Email**: `%(mail)s`
    * <mark style="color:orange;">Note that email addresses in fylr have to be unique. The same email address cannot be used by two fylr users in any circumstances. fylr will not allow the email address to be saved a second time, preventing the login via SAML, if the email address is already present in fylr.</mark>
  * Target: **Login**: This can be used to determine the username during login, as in: The pair of username and Password used to log in. (Not used in the example with samltest.id)
* **Benutzer-Update** (User Update): Set the attribute which is used to determine whether the SAML user (logging in) already has a matching user in fylr. If it has a matching user, that user is logged in (and attributes may get overwritten with the current values in SAML). If it has no matching user in fylr yet, a new user is being created. By default, the used attribute is **Reference**. But you can choose the attributes **Email** or **Login**, instead. \
  Example: Assume that the chosen attribute for **Benutzer-Update** is Email and that Alice logs in the first time with her SAML user alice@example.com. Company policy changes and thus her email address (in SAML) changes to alice.lastname@example.com. During her next login into fylr, a new user is being created, as there is no user yet with alice.lastname@example.com. Now Alice has two user accounts in fylr and can only log in to the second one.

### Upload Metadata

Get fylr's metadata from https://FYLR.EXAMPLE.COM/api/saml/metadata (replace domain name with your instance).

Upload the downloaded metadata file to the testing service ([https://samltest.id/upload.php](https://samltest.id/upload.php)). The test system replies with _We successfully parsed and saved your metadata file. We now trust you._

### Test Connection

Now go to the fylr login page (e.g. by logging out or using a second browser or private tab) and click on **SAMLtestIdP** in the login dialog. This sends you to the login page of the Identify Provider. Login using any of the provided users (they are written on that test login page explicitly, with password). fylr will log the user in with no further rights (unless configured). Check the User Manager in fylr to see that the user record has been created.

### Group Mapping

Users of samltest.id have a `role` attribute with values like `janitor@samltest.id`. This is shown during login on samltest.id's page. We will use this attribute to demonstrate a group mapping:

Mapping goal: Every role that ends in `samltest.id` shall be autmatically member of the fylr group `testidp`.

1. In fylr-URL/configmanager > User management > SAML add into the form field `Group Mapping` the value `%(role)s` (see following screenshot).

<figure><img src="../_assets/images/fylr-saml-group-mapping-en (1).png" alt=""><figcaption><p>How to add an attribute for SAML group mapping in the fylr frontend</p></figcaption></figure>

2. In fylr-URL/groupmanager add a group named `testidp`. Give that group some system rights that are visible after logging in.
3. In this group's configuration > `AUTHENTICATION SERVICES` > below `Single-Sign-On` add an entry with Method `Regular Expression` and Input `.*samltest.id` (see following screenshot).

<figure><img src="../_assets/images/fylr-group-mapping-en (1).png" alt=""><figcaption><p>How to match a value for a group mapping in the fylr frontend</p></figcaption></figure>

4. Save. Test the login as a SAML user with a matching role. The user now has the rights given to the group `testidp`.
