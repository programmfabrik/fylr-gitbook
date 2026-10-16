# Token not found

{% hint style="info" %}
This page describes fylr **up to 6.34.x**. Since fylr 6.35 the `GET /token` / `PUT /job` handshake no longer exists: a job reaches the execserver over the same [slot broker](../../for-developers/execserver.md) connection that was granted its slot, so neither a load balancer nor an execserver restart can cause this error any more. In 6.35 it only appears when a job arrives more than 10 seconds after its slot was granted — an extremely overloaded machine or network.

fylr and an execserver of different versions fail differently: a 6.35 fylr cannot connect to an older execserver and logs `No execserver reachable, jobs are requeued until one connects. Check fylr.execserver.addresses`; an older fylr against a 6.35 execserver logs `Service unknown` for `…/token/<service>`. Upgrade the execserver together with fylr — see [Updating the execserver to 6.35](../installation/updating-the-execserver-to-6.35.md). The `tokenResponseSendServerIP` setting the solutions below name is removed in 6.35.
{% endhint %}

## Symptoms

* File versions (previews as well as large versions like `huge` and `full`) sporadically fail to produce. Metadata extraction may fail as well.
* The file worker and the events (`FILE_PRODUCE_ERROR`) show errors like:

```
"Error": "Token not found"
```

```
metadata read: unable to run file metadata job: ...
```

* The errors correlate with load: the more file production is going on, the more of them appear.
* A manual resync of the affected versions (for example via `/inspect/files`) usually succeeds.

## Cause

fylr sends every job to the execserver in two steps: `GET /token/{service}` reserves a worker slot and answers with a one-time token, then `PUT /job/{service}` sends the job presenting that token. The token is valid for 10 seconds and is held in the memory of the execserver process that issued it.

`Token not found` means the job request arrived at an execserver process that does not hold the token:

* **Most common:** several execserver instances run behind a single load-balanced address (for example a Kubernetes Service), and the token and job requests were routed to different instances. A per-connection load balancer keeps both on one instance only as long as fylr reuses the connection; under parallel load requests get fresh connections.
* The execserver restarted between the two requests (crash, out-of-memory kill, redeployment). Tokens do not survive a restart. Check the restart count of the execserver container/pod.
* Rarely: more than 10 seconds passed between the two requests (extreme overload of the machine or the network).

## Solutions

* If several execserver instances run behind one load balancer: set `tokenResponseSendServerIP` on each instance to its own, directly reachable IP address. The token response then carries that address, and fylr sends the job straight to the instance that issued the token; the next token request goes through the balanced address again.

```yaml
fylr+:
  services+:
    execserver+:
      tokenResponseSendServerIP: "10.42.11.29" # this instance's own IP
```

In Kubernetes, inject the pod IP via the downward API in the execserver deployment. The fylr pods must reach the execserver pod IPs directly on the execserver port.

```yaml
env:
  - name: FYLR_SERVICES_EXECSERVER_TOKENRESPONSESENDSERVERIP
    valueFrom:
      fieldRef:
        fieldPath: status.podIP
```

* Alternatively, skip the load balancer and list every execserver instance individually in `fylr.execserver.addresses` — fylr then balances by itself.
* If the errors coincide with execserver restarts, solve the restarts (memory limits, timeouts) first.
* To verify the routing, set the fylr server log level to `trace` and search the log for `Connection to execserver`: the token request and the following job request of the same job must show the same `RemoteAddr`.
