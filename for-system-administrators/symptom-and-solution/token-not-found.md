# Token not found

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

* **Most common:** several execserver instances run behind a single load-balanced address (for example a Kubernetes Service), and the token and job requests were routed to different instances. See [Scaling the execserver](../installation/scaling-the-execserver.md).
* The execserver restarted between the two requests (crash, out-of-memory kill, redeployment). Tokens do not survive a restart. Check the restart count of the execserver container/pod.
* Rarely: more than 10 seconds passed between the two requests (extreme overload of the machine or the network).

## Solutions

* If several execserver instances run behind one load balancer: configure `tokenResponseSendServerIP` on each instance so that fylr can send the job directly to the instance that issued the token. In Kubernetes, inject the pod IP via the downward API. Both are described in [Scaling the execserver](../installation/scaling-the-execserver.md).
* Alternatively, skip the load balancer and list every execserver instance individually in `fylr.execserver.addresses` — fylr then balances by itself.
* If the errors coincide with execserver restarts, solve the restarts (memory limits, timeouts) first.
* To verify the routing, set the fylr server log level to `trace` and search the log for `Connection to execserver`: the token request and the following job request of the same job must show the same `RemoteAddr`.
