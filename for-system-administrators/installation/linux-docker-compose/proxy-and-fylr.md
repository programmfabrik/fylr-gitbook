# proxy and fylr

If you want the fylr host to reach the Internet by a proxy, then configure this proxy for …

* **Container management software**

Please refer to your container management documentation. To get you started, here an example for docker with systemd:

In `/etc/systemd/system/docker.service.d/proxy.conf`

```
[Service]
Environment="http_proxy=http://your.proxy:80/"
Environment="https_proxy=http://your.proxy:80/"
```

```
systemctl daemon-reload
systemctl restart docker.service
```

* **docker-compose.yml**

Add the proxy settings to the opensearch variable `OPENSEARCH_JAVA_OPTS`

```
services:
  opensearch:
    image: opensearchproject/opensearch:2.12.0
    environment:
      - "OPENSEARCH_JAVA_OPTS=-Xms2g -Xmx2g -Dhttp.proxyHost=your.proxy -Dhttp.proxyPort=80 -Dhttps.proxyHost=your.proxy -Dhttps.proxyPort=80 "
```

Map the proxy settings into the fylr container

```
  fylr:
    image: docker.fylr.io/fylr/fylr:latest
    environment:
      HTTP_PROXY: 'http://your.proxy:80'
      HTTPS_PROXY: 'http://your.proxy:80'
      NO_PROXY: 'opensearch, localhost, your.fylr.domain'
```

## Trusting a proxy for the client address

{% hint style="warning" %}
From fylr **6.35.0**, a proxy *in front of* fylr has to be declared, or every request looks like it came from the proxy.
{% endhint %}

fylr takes the client's address from the connection it is talking to. A reverse proxy, a container network, a Kubernetes ingress or a load balancer in front of fylr forwards the real client in the `x-real-ip` or `x-forwarded-for` header — and fylr uses that forwarded identity **only** when

```yaml
fylr:
  trustProxyHeaders: true
```

is set. It is **off by default**, and it says that fylr is reached *only* through such a proxy. Two cases need no change: a request arriving from loopback is always believed, and so is fylr's own internal hop between its listeners — a proxy on the same host therefore works as before.

Leaving the setting off behind a proxy anywhere else has consequences that are easy to miss: users lose the groups an IP-subnet filter grants them (a filter set to *exclude* puts them in the opposite group instead), the failed-login lockout counts every user against the proxy's address, and the audit log records the proxy. While the setting is off and a request carries one of those headers, fylr logs a warning naming the peer, once an hour, so the case shows up in the log.

Leave it off where fylr can also be reached directly: the setting decides whether a caller may *name* the address that its IP-filtered group membership, its lockout counter and its audit entries are keyed on.
