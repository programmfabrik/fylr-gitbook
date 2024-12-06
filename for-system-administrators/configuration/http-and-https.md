---
description: Variants of how to use fylr with and without TLS certificate
---

# HTTP and HTTPS

{% hint style="info" %}
We did not test these exact examples, please use them as a starting point.
{% endhint %}

## Automated HTTPS Certificate

Let fylr get an certificate for you and renew it automatically:

In `fylr.yml`:

```
fylr+:
  externalURL: "https://database.example.com"
  services+:
    webapp+:
      addr: ":443"
      tls:
        # forwardHttpAddr defines an address a http listener is started
        # to forward requests to fylr.services.webapp.addr, the (port of the)
        # webserver.
        #forwardHttpAddr: "" # if letsencrypt: use port 443 for letsencrypt challenge_type=tls-alpn-01
        forwardHttpAddr: ":80" # use port 80 (and if letsencrypt: for letsencrpyt challenge_type=http-01)

        letsEncrypt:
          # use your email address, example.com will we rejected by Letsencrypt
          email: you@example.com

          # Highly recommended: use useStagingCA: true until you successfully got a
          # certificate. (Which means: no connection problems) Then set it to false
          # and get a real certificate by restarting fylr.
          # useStagingCA sets the staging server of Let's Encrypt which has a higher
          # quota than the production server. However, these certificates are for
          # testing purposes only. They are not signed for official use, so browser
          # will recognise them as being insecure.
          useStagingCA: false

          # Optional: get additional certificates for the given domains.
          additionalDomains:
           - "www.database.example.com"
           
    api+:
      oauth2Server+:
        clients+:
          fylr-web-frontend+:
            redirectURIs:
              - https://database.example.com/oauth2/callback
```

{% hint style="info" %}
We did not test this exact example, please use it as a starting point.
{% endhint %}

## You provide the HTTPS certificate

1. Put your certificate and private key in the same directory as `fylr.yml`, in this example the file names are `crt.pem` and `key.pem`.
2. If you need additional certificates of a certificate chain, like intermediate certificates, put them into `crt.pem`, as well. In our test worked to put the most specific certificate first (like for fylr.example.com) and then follow with the certificate that was used to sign the first one (and then the certificate that was used to sign the second one).
3. In `fylr.yml`:

```
fylr+:
  externalURL: "https://database.example.com"
  services+:
    webapp+:
      addr: ":443"
      tls:
        certFile: "/fylr/config/crt.pem"
        keyFile: "/fylr/config/key.pem"
    api+:
      oauth2Server+:
        clients+:
          fylr-web-frontend+:
            redirectURIs:
              - https://database.example.com/oauth2/callback
```

{% hint style="info" %}
We did not test this exact example, please use it as a starting point.
{% endhint %}

##

## You provide the service that does HTTPS

We do not recommend this. Using additional proxies and services in front of fylr often leads to hard to debug problems where we cannot help.

In `fylr.yml`:

```
fylr+:
  externalURL: "https://database.example.com"
  services+:
    webapp+:
      addr: ":80"
      tls:
    api+:
      oauth2Server+:
        clients+:
          fylr-web-frontend+:
            redirectURIs:
              - https://database.example.com/oauth2/callback
```

{% hint style="info" %}
We did not test this exact example, please use it as a starting point.
{% endhint %}

## No HTTPS

Recommended only for internal use.

In `fylr.yml`:

```
fylr+:
  externalURL: "http://database.example.com"
  services+:
    api+:
      oauth2Server+:
        # disable the check whether a redirect URL is secure
        allowHttpRedirects: true
        clients+:
          fylr-web-frontend+:
            redirectURIs:
              - http://database.example.com/oauth2/callback
    webapp+:
      addr: ":80"
      tls:
```

{% hint style="info" %}
We did not test this exact example, please use it as a starting point.
{% endhint %}

## No HTTPS and domain is localhost

This is the default.



## Further reading

Related topic: [Multiple DNS domains and changing DNS domains](dns-domains.md)
