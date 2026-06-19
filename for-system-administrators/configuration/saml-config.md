---
description: >-
  connect your SAML-compatible authentication provider to fylr, for example
  shibboleth
---

# SAML config

## First: The easy part

Please read through our [fylr-SAML tutorial](../../tutorials/auth/saml/), we describe the basics there and guide you through the steps once. Then come back here for the advanced topics only.

## Renewal of the identity provider metadata in fylr

This is also relevant for new **certificates** of the IdP, which are part of the metadata.

fylr only fetches metadata from the configured **IdP metadata URL** at the following events:

* fylr starts



* SAML section in Base Config is changed and saved, this applies to the following fields:\
  `URL`, `Cert`, `Key`, `SignRequest`, `ServiceProviderEntityID`, `IdentityProviderEntityID`, `Debug`  <br>
