---
description: Variants to use fylr with and without TLS certificate
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
        letsEncrypt:
          # use your email address, example.com will we rejected by Letsencrypt
          email: you@example.com

          # forwardHttpAddr defines an address a http listener is started
          # to forward requests to fylr.services.webapp.addr, the (port of the)
          # webserver.
          #forwardHttpAddr: "" # use port 443 for letsencrypt challenge_type=tls-alpn-01
          forwardHttpAddr: ":80" # use port 80 for letsencrpyt challenge_type=http-01

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
2. If you need intermediate certificates, put them into `crt.pem` as well.
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



