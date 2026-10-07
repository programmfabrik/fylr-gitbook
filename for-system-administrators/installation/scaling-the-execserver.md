---
description: How to run more than one execserver instance
---

# Scaling the execserver

The execserver does the heavy lifting of asset processing (preview production, metadata extraction, plugin execution). It is the part of fylr that benefits most from horizontal scaling. How to split the execserver onto its own server is described in [execserver on another linux](linux-docker-compose/execserver-on-another-linux.md) — this page describes how to run **several** execserver instances correctly.

## How fylr talks to the execserver

Since fylr 6.35, fylr drives each execserver over a single **fylr-initiated websocket** — the *slot broker*. fylr connects out to every configured execserver address; an execserver is configured with no fylr address. fylr parks a want for each job on the execservers that run its service, the execserver with a free slot offers it, and the job is sent over that same socket, so a job always reaches the instance that offered the slot — there is no instance-affinity problem to configure around. The protocol is described on the [Exec server](../../for-developers/execserver.md) page, the full design in the [slot broker white paper](../../for-developers/concepts/white-papers/execserver-slot-broker.md).

For job data the execserver is stateless: it fetches its inputs via URLs, streams results back and keeps nothing between jobs.

{% hint style="warning" %}
The broker is the **only** transport as of fylr 6.35. The legacy `GET /token` / `PUT /job` handshake and the `tokenResponseSendServerIP` setting are removed — an execserver without a broker connection receives no work, so **execserver and fylr must be upgraded together**. On fylr up to 6.34.x, load-balanced setups instead needed `tokenResponseSendServerIP` (see [Token not found](../symptom-and-solution/token-not-found.md)). What to change in an existing installation is on [Updating the execserver to 6.35](updating-the-execserver-to-6.35.md).
{% endhint %}

There are two supported ways to run multiple instances:

## Several execservers, addressed individually

List every instance in the client configuration of the fylr server. fylr opens one broker connection per address and spreads the parked jobs across every instance that announces the needed service — instances on specialised hardware (for example ffmpeg-only workers) are picked automatically for exactly the services they declare.

```yaml
fylr+:
  execserver+:
    addresses:
      - http://exec1.example.com:8083/
      - http://exec2.example.com:8083/
```

## Several execservers behind one load balancer

If the instances share a single balanced address (for example a Kubernetes Service in front of multiple execserver pods), this works out of the box since fylr 6.35: fylr finds the pods behind the address itself. It opens connections to the address in quick succession — the balancer hands each to some pod — keeps every connection that reached a pod not yet in its pool and closes the duplicates (each execserver announces a unique instance id), until a run of connections reaches only pods it already knows. It does this at startup, again at rest every 30 seconds (less often while nothing new turns up), and sooner when jobs back up: a backlog that persists behind the address for five seconds makes fylr look again, so a pod added by an autoscaler picks up work within seconds. One fylr keeps up to 32 execservers per address in its pool.

No per-pod addressing is needed: no `tokenResponseSendServerIP`, no downward-API pod IPs, no headless service. fylr only ever dials the one address the operator published.

{% hint style="info" %}
Rolling restarts are safe: on shutdown an execserver **drains** — it stops accepting new jobs and lets running jobs finish (up to `drainTimeoutSec`, default 20 s). Jobs still running at the deadline are handed back as "stopped, retry later": a file job goes back into the file queue.
{% endhint %}
