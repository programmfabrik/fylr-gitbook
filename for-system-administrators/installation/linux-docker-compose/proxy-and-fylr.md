# proxy and fylr

If you want the fylr host to reach the Internet by a proxy, then configure this proxy for …

* **Container management software**

Please refer to your container management documentation. To get you started, here an example for docker with systemd:

In `/etc/systemd/system/docker.service.d/proxy.conf`

```
[Service]
Environment="http_proxy=http://proxy.lda.stk.lsa-net.de:80/"
Environment="https_proxy=http://proxy.lda.stk.lsa-net.de:80/"
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
