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

Enable all event types that should store the user. Otherwise the event will not be connected to a user.

### Copy User Data to Events

Define which data of the user should be copied to the events. This is independent from the event user. If the user get's deleted or pseudonymized, this data remains in the events.

## OAuth-Service

Add pairs of Client IDs and Secrets for the [OAuth2 Authentication](./for-developers/api/oauth2#configuring-client-id-and-secret).

* **Name**: Name of the Client (used as Client ID)
* **Secret**: Client Secret, must be entered as a [Bcrypt Hash](https://bcrypt-generator.com/)
* **Redirect URIs**: List of callback URLs to the local client, needed for some OAuth2 Authentication flows

* **Expiration Time: Access Token**: Time after which the Access Token expires and needs to be refreshed, default: 24 hours
* **Expiration Time: Refresh Token**: Time after which the Refresh Token expires, default: 720 hours

## OpenID Userinfo

Select which user information should be returned over the OpenID endpoint `oauth2/userinfo`.

## LDAP



## SAML

SAML 2.0 is an [XML](https://en.wikipedia.org/wiki/XML)-based [protocol](https://en.wikipedia.org/wiki/Communications\_protocol) that uses [security tokens](https://en.wikipedia.org/wiki/Software\_token) containing [assertions](https://en.wikipedia.org/wiki/Security\_Assertion\_Markup\_Language) to pass information about a principal (usually an end user) between a SAML authority, named an [Identity Provider](https://en.wikipedia.org/wiki/Identity\_Provider), and a SAML consumer, named a [Service Provider](https://en.wikipedia.org/wiki/Service\_Provider).

fylr acts as a Service Provider and as such needs an Identity Provider. For testing purposes you can use [https://samltest.id/](https://samltest.id/). fylr's endpoint to get the required metadata XML is [http://localhost/api/saml/metadata](http://localhost/api/samlmetadata). Replace _localhost_ with the domain of your fylr server.

### Test SAML with samltest.id

First you need to generate a certificate and private key. The certificate must be then given to the Identity Provider, so that requests coming from fylr are accepted.

#### Generate Certificate

```bash
openssl genrsa -out private.key 1024
openssl req -new -x509 -key private.key -out publickey.cer -days 365
```

#### Base Config

* Copy & Paste the certificate & key into fylr's Base config > User management > SAML.
* As the Identity Provider URL add [https://samltest.id/saml/idp](https://samltest.id/saml/idp).
* We recommend to check **Log Steps**. This will write log events to debug SAML connections. In case of an error, the connection attempt is always logged.
* In **User Mapping** define how the SAML user is created in fylr. Upon each login the SAML users are mapped to fylr users. If a user already exists, an update is performed.
  * Target: Reference: `%(urn:oasis:names:tc:SAML:attribute:subject-id)s`
  * Target: Display Name: `%(displayName)s`
  * Target: Email: `%(mail)s`

#### Upload Metadata

```bash
curl -o sdp-metadata.xml http://localhost/api/saml/metadata
```

Upload the downloaded file **sdp-metadata.xml** to the testing service ([https://samltest.id/upload.php](https://samltest.id/upload.php)). The test system replies with _We successfully parsed and saved your metadata file. We now trust you._

#### Test Connection

Now go to the fylr login page and click on **SAMLtestIdP**. This sends you to the login page of the Identify Provider. Login using any of the provided users. fylr will log the user in with no further rights (unless configured). Check the User Manager in fylr to see that the user record has been created.
