# Execserver

## Job protocol

fylr drives each execserver over a single **fylr-initiated websocket** — the *slot broker* — instead of the former `GET /token` + `PUT /job` polling handshake. Each fylr server opens one connection per configured execserver instance (`GET /broker`). The execserver keeps an in-memory **want-book** of the slots fylr is waiting for and pushes a job onto a free slot the moment one opens, so an idle system makes no execserver requests at all.

A slot's life alternates direction over that one socket:

`WANT` (fylr → exec) → `OFFER` (exec → fylr) → `JOB` (fylr → exec) → `DONE` (exec → fylr)

| Direction | Message | Meaning |
| --- | --- | --- |
| exec → fylr | `HELLO {instance_id, services, waitgroups, clients}` | Capability snapshot on connect, re-sent when it changes. fylr parks a `WANT` only on a connection whose execserver announced that service. |
| fylr → exec | `WANT {job_id, service, priority}` | A worker is parked, needing a slot. |
| fylr → exec | `UNWANT {job_id}` | Got a slot elsewhere / gave up (requeue). |
| exec → fylr | `OFFER {job_id, token}` | A slot has been reserved for that job. |
| fylr → exec | `JOB {job_id, job}` | Acceptance — the job JSON rides the socket. |
| fylr → exec | `DECLINE {job_id}` | A surplus offer (another execserver was faster); the slot is freed at once. |
| exec → fylr | `DONE {job_id, receipt}` | Job receipt or error. |
| both | ping / pong | Liveness / half-open detection. |

```mermaid
sequenceDiagram
    autonumber
    participant F as fylr (client)
    participant X as execserver
    Note over F,X: control — one fylr-initiated websocket
    X-->>F: HELLO {instance_id, services, waitgroups, clients}
    F->>X: WANT {job_id, service, priority}
    Note right of X: parked in the want-book until a slot frees
    X->>F: OFFER {job_id, token}
    F->>X: JOB {job_id, job (+ pipe URLs)}
    Note over F,X: bulk stdin/stdout — separate HTTP pipes,<br/>pinned to the fylr replica that placed the job
    X->>F: GET /pipe/IN — stream stdin
    X->>F: PUT /pipe/OUT — stream stdout
    X-->>F: DONE {job_id, receipt}
```

Bulk stdin/stdout for body-mode jobs (IIIF tiles, on-demand rendition downloads, XSLT export, datamodel graph, metadata, plugin callbacks) flow over one-time HTTP **pipe** endpoints on the fylr backend, each served exactly once. The pipe lives in memory on the fylr replica that created the job, so its callback URL must reach that replica — and so must `api_tx_url`, whose open write transaction lives there too.

fylr resolves one callback base for itself at startup, from the address the kernel would send from towards a configured execserver, and corrects it from the live broker socket. Every callback is built from that base, so no pod addressing is configured anywhere. `callbackBackendInternalURL` and `callbackApiInternalURL` still override scheme and port — for a proxy in front of the listener — but not the host: a Kubernetes Service name in either has no effect. `callbackBackendOwnURL` is the verbatim escape hatch for NAT between fylr and the execserver.

{% hint style="warning" %}
The broker is the **only** transport as of fylr 6.35. The legacy `GET /token` / `PUT /job` endpoints, the polling fallback and `tokenResponseSendServerIP` are removed. An execserver without a broker connection to fylr receives no work, so **execserver and fylr must be upgraded together** — there is no mixed-version fallback. See [Updating the execserver to 6.35](../for-system-administrators/installation/updating-the-execserver-to-6.35.md) for what an administrator has to change.
{% endhint %}

For the full design — demand-driven connection pooling behind a load balancer, cross-instance priority scheduling and claim fairness across fylr servers — see the [Execserver slot broker white paper](concepts/white-papers/execserver-slot-broker.md).

## Fleet topology

From version 6.35.0, `/inspect/system/topology` shows the whole installation on one page: every fylr server, every execserver, the load balancer when there is one, and the work moving between them — running jobs, jobs queued behind a full waitgroup, what finished and what failed, with throughput and bytes moved. It streams over a websocket; the same data is served as JSON at `/inspect/system/topology/data`.

Each fylr registers itself on every broker connection — backend id, name, version and the callback base it announces. The execserver fetches that base and checks that the server answering is the one that registered, so a callback address pointing at a load balancer in front of several replicas is reported on the page at connect time, instead of failing later inside a job.

An address that fronts a fleet is recognised from the connection itself: fylr's socket knows what it dialled and the execserver stamps its greeting with the address it accepted on. A Kubernetes Service is therefore shown as a Service even when a single pod is behind it.

## Concurrency

By default the execserver **auto-balances** concurrency: all services share one CPU pool sized to the host, and each service is classified light or heavy by its measured runtime, so long conversions never occupy the last `fastReserve` slots and short interactive jobs (metadata, plugins, IIIF) stay responsive. Configuring an explicit `waitgroups` block restores manually sized pools. See [performance tuning](../for-system-administrators/configuration/performance-tuning.md) for the settings and [Updating the execserver to 6.35](../for-system-administrators/installation/updating-the-execserver-to-6.35.md) for the migration.

## File Queue

### Action: "metadata"

Runs `fylr_metadata`
