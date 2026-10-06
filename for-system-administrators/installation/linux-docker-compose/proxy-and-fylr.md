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
From fylr **6.35.0**, a proxy *in front of* fylr must be listed in `fylr.trustedProxies`, or every request looks like it came from the proxy.
{% endhint %}

fylr takes the client's address from the connection it is talking to. A reverse proxy, a container network, a Kubernetes ingress or a load balancer in front of fylr forwards the real client in the `x-real-ip` or `x-forwarded-for` header, and fylr reads these headers **only** from a peer listed in `fylr.trustedProxies`, as single addresses or CIDRs:

```yaml
fylr:
  trustedProxies:
    - "192.168.1.10"   # a reverse proxy on another host
    - "10.42.0.0/16"   # the pod network a Kubernetes ingress connects from
```

As an environment variable: `FYLR_TRUSTEDPROXIES='["192.168.1.10","10.42.0.0/16"]'`.

The list is **empty by default**. Two cases need no entry: a request arriving from loopback is always trusted, and so is fylr's own internal hop between its listeners, so a proxy on the same host works as before. A proxy in a Docker container connects from the gateway of its docker network (`docker network inspect <network>`, field `Gateway`); list that address, see [multiple fylrs in one Linux](multiple-fylrs-in-one-linux.md).

From a listed peer the client is `x-real-ip`, else the last entry of `x-forwarded-for`, the address the proxy saw; entries before it come from the caller. A proxy that only appends to `x-forwarded-for` (Apache, HAProxy) must remove `x-real-ip`, or it passes on one sent by the caller. With several proxies in a row, the one next to fylr must set `x-real-ip` to the client address.

A missing entry has consequences that are easy to miss: users lose the groups an IP-subnet filter grants them (a filter set to *exclude* puts them in the opposite group instead), the failed-login lockout counts every user against the proxy's address, and the audit log records the proxy. When a peer that is not listed sends one of those headers, fylr logs a warning naming the peer, once an hour, so the case shows up in the log.

List only addresses that nothing but the proxy can connect from: a listed peer may *name* the address that IP-filtered group membership, the lockout counter and the audit entries are keyed on.

{% hint style="info" %}
`fylr.trustProxyHeaders: true`, a single switch that development builds of 6.35 read, never shipped in a release and has no effect. `fylr config check` reports it as an unknown key; list the proxy in `fylr.trustedProxies` instead.
{% endhint %}
