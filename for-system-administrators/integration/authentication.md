fylr can use the following authentication services (a.k.a. SSO - Single Sign On) to:
* Authenticate user logins. Then your users can log into fylr with their existing credentials.
* Apply group membership for rights management.
* Retrieve user records: email address, display name, etc..

## LDAP

fylr can be connected to multiple LDAP servers. With or without TLS. Typically, a bind user (a.k.a. machine user) is used to allow the connection.

## SAML

fylr can be connected to e.g. Shibboleth IDPs and Microsoft Azure Active Directory via SAML.

## Shibboleth

Shibboleth IDentityProviders can be connected via SAML to fylr, which then is a ServiceProvider.

## Active Directory

Microsoft Active Directory, as used in a Local Area network, can be connected via LDAP.

Microsoft Azure Active Directory can be connected via SAML to fylr.

## Kerberos

Kerberos is not supported by fylr. But if it is used in an Active Directory, LDAP can be connected instead.

