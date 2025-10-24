---
description: fylr and what to consider when changing DNS domains or using multiple domains
---

# DNS Domains

You can point **multiple** DNS Records and thus domains to your fylr.

But keep in mind:

* fylr always has only _one_ **main** DNS domain, configured in fylr.yml's `externalURL`, and fylr will redirect to this URL and use it for its image URLs.
* The domain in `externalURL` has to be part of your fylr license. Except when testing as the fylr root user or on localhost.
* If fylr shall react to additional domains besides the one main domain, make sure that these are also present in the certificate that fylr uses.&#x20;
* If you let fylr retrieve the certificate automatically, you need to configure them as `additionalDomains` in fylr.yml. See [HTTPS](http-and-https.md) for examples and details about using certificates.

### **Changes** to the main domain

* Licenses are bound to domains so make sure you have a license for the new main domain configured as `externalURL`.
* Make sure that you either have a certificate for the new domain or to let fylr automatically retrieve a certificate for the new domain. And optionally, `additionalDomains`, as mentioned above.
* When you change fylr's main domain:&#x20;
  * configured it as `externalURL` in `fylr.yml` and restart fylr
  *   you need to do a re-index: Surf to **https://**&#x66;ylr.example.co&#x6D;**/inspect/system/** (login as root)

      A re-index likely takes only minutes, but also might take hours, if you have a lot of objects.
* During that re-index, even if it is running in the background, preview images **will not be visible**. Only after the re-index the images are prepared and working, with the new domain.

