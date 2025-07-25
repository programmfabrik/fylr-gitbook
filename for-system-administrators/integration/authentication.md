# Authentication

fylr can use the following authentication services (a.k.a. SSO - Single Sign On) to:

* Authenticate user logins. Then your users can log into fylr with their existing credentials.
* Apply group membership for rights management.
* Retrieve user records: email address, display name, etc..

### LDAP

fylr can be connected to multiple LDAP servers. With or without TLS. Typically, a bind user (a.k.a. machine user) is used to allow the connection. See [our tutorial](../../tutorials/ldap.md).

### SAML

fylr can be configured to be a Service Provider against a SAML IDP.\
In other words: fylr can be connected to e.g. Shibboleth IDPs and Microsoft Azure Active Directory via SAML. See [our tutorial](../../tutorials/auth/saml/).

### Shibboleth

Shibboleth IDentityProviders can be connected via SAML to fylr, which then is a ServiceProvider. See [our tutorial](../../tutorials/auth/saml/).

### Active Directory

Microsoft Active Directory, as used in a Local Area network, can be connected via LDAP. See [our LDAP-tutorial](../../tutorials/ldap.md).

Microsoft Azure Active Directory can be connected via SAML to fylr. See [our SAML-tutorial](../../tutorials/auth/saml/).

### Kerberos

Kerberos is not supported by fylr. But if it is used in an Active Directory, LDAP can be connected instead. See [our LDAP-tutorial](../../tutorials/ldap.md).

### OpenID

We don’t support authentication against OpenID IDPs yet.

### OAuth

fylr is usually configured to accept multiple OAuth2 clients and you can add more (fylr in the server role).\
\
We don’t support authentication against OAuth IDPs yet (fylr in the client role).
