---
description: fylr and what to consider when using/changing DNS domains
---

# DNS Domains

You can point multiple DNS Records and thus domains to your fylr.

But keep in mind:

* fylr always has only one main DNS domain, typically configured in fylr.yml's `externalURL`, and fylr will redirect to this URL and use it for image URLs.
* If fylr shall react to additional domains besides the one main domain, make sure that these are also present in the one certificate that fylr uses.&#x20;
* If you let fylr retrieve the certificate automatically, you need to configure them as `additionalDomains` in fylr.yml. See [HTTPS](http-and-https.md) for examples and details about using certificates.

Changes to domains:

* When you change fylr's main domain, so after changing fylr.yml and restart, you need to do a re-indexation, which might take hours, if you have a lot of objects. It can be found in the inspect-Interface (https://fylr.example.co&#x6D;**/inspect/** )  behind the **System**-button.
* Licenses are bound to domains so make sure you have a license for the new main domain configured as `externalURL`.
* Make sure that you either have a certificate for the new domain or to let fylr automatically retrieve a certificate for the new domain. And optionally, `additionalDomains`, as mentioned above.

