---
description: How to run more than one execserver instance
---

# Scaling the execserver

The execserver does the heavy lifting of asset processing (preview production, metadata extraction, plugin execution). It is the part of fylr that benefits most from horizontal scaling. How to split the execserver onto its own server is described in [execserver on another linux](linux-docker-compose/execserver-on-another-linux.md) — this page describes how to run **several** execserver instances correctly.

## How fylr talks to the execserver

fylr sends every job to the execserver in two steps:

1. `GET /token/{service}` reserves a worker slot. The execserver answers with a one-time token, valid for 10 seconds. If all workers are busy, it answers `503` and fylr retries.
2. `PUT /job/{service}` sends the actual job, presenting that token.

The token is held in the memory of the execserver process that issued it. Because of this, **the job request must reach the same execserver instance that issued the token**. If it reaches a different instance, the job fails with [Token not found](../symptom-and-solution/token-not-found.md).

For job data the execserver is stateless: it fetches its inputs via URLs, streams results back and keeps nothing between jobs. Only the token handshake is instance-local, for those few seconds between the two requests.

There are two supported ways to run multiple instances:

## Several execservers, addressed individually

List every instance in the client configuration of the fylr server. No load balancer is needed: the addresses are tried in round robin, and if an instance reports to be busy, the next one is tried. Token and job always go to the same address, so no further configuration is required.

```yaml
fylr+:
  execserver+:
    addresses:
      - http://exec1.example.com:8083/
      - http://exec2.example.com:8083/
```

## Several execservers behind one load balancer

If the instances share a single balanced address (for example a Kubernetes Service in front of multiple execserver pods), the token request and the job request may be routed to different instances. To make this setup work, set `tokenResponseSendServerIP` on each execserver instance to its own, directly reachable IP address:

```yaml
fylr+:
  services+:
    execserver+:
      tokenResponseSendServerIP: "10.42.11.29" # this instance's own IP
```

The token response then carries the instance's own address, and fylr sends the job request directly there, bypassing the load balancer for that one request. The next token request goes through the balanced address again, so load balancing is preserved.

In Kubernetes the pod IP is not known when the `fylr.yml` is written. Since every `fylr.yml` key can be overridden by an environment variable (prefix `FYLR_`, path separated by `_`), inject the pod IP via the downward API in the execserver deployment:

```yaml
env:
  - name: FYLR_SERVICES_EXECSERVER_TOKENRESPONSESENDSERVERIP
    valueFrom:
      fieldRef:
        fieldPath: status.podIP
```

The fylr server pods must be able to reach the execserver pod IPs directly on the configured port (the default with in-cluster networking).

{% hint style="warning" %}
Without `tokenResponseSendServerIP`, the only thing keeping the token and job requests on the same instance is TCP connection reuse (a per-connection load balancer routes both to the same backend as long as the connection is reused). This mostly works while little is going on, but it is not guaranteed: under parallel production load, requests get fresh connections and jobs sporadically fail with [Token not found](../symptom-and-solution/token-not-found.md).
{% endhint %}
