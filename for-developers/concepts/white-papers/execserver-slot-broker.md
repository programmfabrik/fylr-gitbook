# Execserver slot broker

Replace both polling loops with a fylr-initiated websocket per execserver instance — and retire the token handshake, `tokenResponseSendServerIP`, and the "Token not found" incident class with it.

| Before | This design |
| --- | --- |
| One `SELECT` per second per file worker, even when idle. One `GET /token` per second per waiting job, against _every_ configured execserver, for up to `connectTimeoutSec`. Slot handshake breaks behind load balancers. | Zero execserver requests while idle. One message per state change. The execserver picks exactly one taker per free slot — by priority, across all connected fylr servers. No instance-affinity problems left to patch. |

{% hint style="info" %}
Design document, July 2026, implemented starting with fylr 6.34. Tracked internally as ticket #80119. A few details below are marked where the implementation refined the original proposal.
{% endhint %}

## Problem

The execserver + client system ran on two polling loops:

* **DB polling.** Every file worker (`fylr.execserver.parallel` + `parallelHigh` goroutines) ran `SELECT … FOR UPDATE SKIP LOCKED LIMIT 1` on `file_queue` every second, even when the system was idle.
* **Execserver busy-polling.** A job that found all execservers busy re-polled `GET /token/{service}` on _every_ configured address once per second until `connectTimeoutSec` expired, then requeued +1 min.

On top of that, the 2-phase token handshake — `GET /token` reserves an in-memory, single-use token with a 10 s TTL; `PUT /job` redeems it — is **instance-local**: with several execserver replicas behind one address, the PUT can reach a different instance than the token issuer → `Token not found`. `tokenResponseSendServerIP` (re-addressing the PUT to the issuing pod's IP) and the `Connection: close` re-balance hack are patches on this weakness. Multi-replica execservers run in customer-managed Kubernetes clusters — the replacement must work with **zero cluster-side tuning**.

## The slot broker

Configuration stays exactly as is: fylr.yml lists `execserver.addresses`; the execserver never learns fylr addresses. Because only fylr knows the peers, the channel is fylr-initiated — which makes presence trivial.

{% hint style="success" %}
**Key inversion.** Connecting _is_ the registration; the connection dropping _is_ the goodbye. Crash-safe, no registration state, no TTL cleanup — and the traffic direction (outbound from fylr) matches the previous polling, so existing firewall and NAT topologies keep working.
{% endhint %}

Each fylr opens one persistent websocket per execserver instance (`GET /broker` on the execserver). The execserver keeps a **want-book** per waitgroup — in-memory, keyed by connection, volatile by design: a reconnecting fylr simply re-registers its parked wants.

When a slot frees, the execserver picks the taker in this order: highest `priority` class first, then **round-robin across connections** within that class, then FIFO within a connection. Priority stays global — an interactive job beats background work regardless of origin — but within a class, slots are dealt like cards: a fylr with one parked want is served next even if a sibling parked a hundred wants ahead of it. Exactly one fylr is offered each slot — **no thundering herd, by construction**. An idle execserver grants an incoming `WANT` instantly: a parked want _is_ the standing "got work for me?" ask.

{% hint style="success" %}
**New capability.** Cross-instance priority scheduling. Previously `file_queue` priority only ordered pickup within one fylr; at the execserver, a background resync and an interactive user request scrummed equally in the 1 s retry loop. With the want-book, an interactive job on fylr B beats a background job on fylr A for the next ffmpeg slot.
{% endhint %}

## Protocol

All control traffic is multiplexed over the one socket. A slot's life alternates directions:

`WANT` (fylr → exec) → `OFFER` (exec → fylr) → `JOB` (fylr → exec) → `DONE` (exec → fylr)

| Direction | Message | Meaning |
| --- | --- | --- |
| exec → fylr | `HELLO {instance_id, services, waitgroups, clients}` | Snapshot on connect, re-sent when its content changes (e.g. the connected-client count); also kills the per-job 404 service probing. |
| fylr → exec | `WANT {job_id, service, priority}` | A worker is parked needing a slot. |
| fylr → exec | `UNWANT {job_id}` | Got a slot elsewhere / gave up (requeue). |
| exec → fylr | `OFFER {job_id}` | A slot has been reserved for that job. |
| fylr → exec | `JOB {job_id, job}` | Acceptance: the job JSON (previously a URL query parameter on the PUT) rides the socket. |
| fylr → exec | `DECLINE {job_id}` | Surplus offer (another execserver was faster); slot freed in milliseconds. |
| exec → fylr | `DONE {job_id, receipt}` | Job receipt / error. |
| both | ping / pong | Liveness, half-open detection. |

## Job data and streams

The execserver cannot pull _the work itself_: a `file_queue` entry fans out into several exec calls for different services, and an exec call carries streams plus a response consumer inside a fylr worker goroutine. What it pulls is **a taker for a free slot**. The job JSON travels in the `JOB` message; all bulk bytes flow **execserver → fylr**.

{% hint style="success" %}
**The asymmetry that makes it bullet-proof.** Execserver → fylr reachability is already mandatory for every deployment (`callbackBackendInternalURL`; inputs are fetched by URL). Fylr → _specific-execserver-instance_ reachability — what `tokenResponseSendServerIP` tried to manufacture — was never guaranteed. The design moves all affinity onto the guaranteed direction.
{% endhint %}

The body-mode call sites (stdin from the PUT body / stdout to the response body: IIIF tiles, on-demand rendition downloads, XSLT export, datamodel graph, metadata, plugin callbacks) switch to **one-time pipe endpoints** on the fylr backend: the execserver GETs stdin from an in-pipe and PUTs stdout to an out-pipe, each URL served exactly once, the random id being the credential — the same trust model as the other backend callback URLs.

A mid-stream failure becomes: the execserver aborts its stream request and sends `DONE` with the error. The receipt carries the decisive stderr line and a capped stdout prefix, so a structured error a command wrote (plugins report errors that way) survives to the caller; the execserver commits a stream only once the output outgrows a 4000-byte buffer, exactly like the HTTP transport's response buffering, so a command that fails with a small output never masquerades as an empty success.

## What gets deleted

Because reservation, job delivery and receipt all ride the instance-pinned socket, and streams flow in the guaranteed direction, no fylr → execserver request needs instance affinity any more:

* The token machinery — 10 s TTL, cleanup goroutine, `Token not found` / wrong-service errors
* `tokenResponseSendServerIP` and `TokenResponse.ServiceURL` (after deprecation, see migration)
* The `Connection: close` re-balance hack
* The 1 s busy-retry loop against every execserver address
* The "Token not found" incident class — structurally, instead of mitigated

## Replicas behind one address

One websocket through a load balancer reaches one pod, so the other pods' want-books would never see that fylr. The fix needs no config change: fylr resolves the configured hostname and opens one socket **per DNS A record**, re-resolving periodically to track scale-up/down; the boot-generated `HELLO.instance_id` dedupes connections. In Kubernetes that means pointing the address at a headless service. Single-host deployments see no change at all. (This fan-out is a planned extension; a load-balanced address currently behaves like one instance.)

## Multiple fylr servers, one instance

Horizontal fylr scaling — several fylr servers sharing one database and the same execserver pool — needs no fylr-to-fylr coordination, because each shared resource keeps exactly one arbiter:

* **Queue items → Postgres.** Claiming stays `FOR UPDATE SKIP LOCKED`: each `file_queue` item is claimed by exactly one fylr, which then registers the `WANT`s for it.
* **Slots → the want-book.** A fylr cannot grab slots at all — it can only express demand (`WANT`); assignment is always execserver-initiated, one `OFFER` per freed slot. Grants go priority-first, then round-robin across connections, so within a priority class every connected fylr gets an equal share of slots no matter how many wants each has parked. The execserver never needs to know which connections belong to the same instance — the connection is the unit of fairness.

Cross-fylr priority is emergent: a high-priority job claimed by fylr B outranks fylr A's earlier background wants at the execserver, something the token protocol could not express at all.

**Claim fairness.** Round-robin grants alone don't spread the _fylr-side_ work (feeding streams, processing responses, reindexing): if one fylr's dispatcher wakes first and claims the whole queue, its siblings idle even though slot allocation stays "fair" — all the parked wants are simply its own. So claiming is bounded to a share: `HELLO` carries the execserver's connected-client count, and each fylr's exec-bound admission becomes `ceil(capacity / clients)` plus a small pipelining headroom, summed over instances. Five fylrs on a 40-slot pool claim at most ~10 items each; when a fylr drops off, the count falls and the survivors' shares grow — self-healing, no configuration.

Claimed-but-parked items stay cheap (a goroutine, a book entry, a claimed row). Claims carry a **heartbeat**: a crashed fylr's claims go stale and are requeued by any surviving fylr after a threshold, so no item is stranded — the startup sweep alone provably cannot catch this case, because the dead server's backend registration keeps its claims looking fresh. Several distinct instances (separate databases) sharing one execserver pool behave identically — fairness is per connection, and the want-book neither knows nor cares about database boundaries.

## Failure matrix

| Failure | Handled by |
| --- | --- |
| fylr crashes with parked wants | Its socket closes → execserver drops that connection's book entries. |
| fylr crashes with claimed queue items | Claim heartbeat goes stale → a surviving fylr requeues the orphans. |
| Execserver crashes | Parked jobs keep waiting on the other execservers; the reconnect re-registers current wants. |
| `OFFER` never answered (conn drop) | Offer timeout → next candidate. |
| Two `OFFER`s for one job race | First wins; the loser gets `DECLINE` immediately. |
| No slot within `connectTimeoutSec` | Unchanged: requeue with `start_after` +1 min — just silent while waiting instead of polling. |
| Old execserver (no `/broker`) | fylr falls back to polling for that address. |
| Old fylr, new execserver | Legacy `GET /token` still served; it returns 503 while the want-book is non-empty, so legacy clients cannot steal slots from parked jobs. |

Every failure collapses onto two primitives: connection lifetime, and — during migration, for the legacy path — the existing token TTL.

## Companion fix: the file dispatcher

Slot events say nothing about queued work, so the DB side gets its own fix. With `parallel` / `parallelHigh` gone, the worker pool collapses into **one dispatcher goroutine per fylr server**: it claims queue items in priority order as long as admission allows — exec-bound work up to the claim share described above, local-bound work (`sync`, `checksum`, `copy_move`) on a semaphore derived from `NumCPU` — and hands each item to its own goroutine. The dispatcher never blocks on a slot itself, so the starvation scenario behind `parallelHigh` cannot occur; a fraction of the local slots stays reserved for high-priority work as an internal concern of that semaphore, not configuration.

The original proposal added Postgres LISTEN/NOTIFY and a 15–30 s fallback poll; the implementation deliberately keeps a plain **1 s poll** instead — one cheap indexed query per fylr per second replaces one query per worker per second, and the operational simplicity beats the last increment of idle silence. The dispatcher also maintains the claim heartbeats and requeues orphaned claims of crashed siblings.

## No more worker-pool configuration

`fylr.execserver.parallel` sized a static pool of file workers, each carrying one queue item synchronously — including _blocking_ inside the slot wait. The knob therefore conflated two unrelated bounds, and `parallelHigh` existed only because a fully-blocked pool starves interactive work. The broker dissolves both, so the keys are gone:

* **Exec-bound concurrency derives from the pool itself.** The `HELLO` snapshot carries each execserver's waitgroups, process counts and connected-client count, so fylr computes admission from actual capacity. The execserver's `waitgroups.processes` — which already exists, and lives where the CPUs are — is the _single_ source of truth for exec concurrency. No execserver connected → nothing exec-bound is claimed at all (previously: workers claimed, failed, requeued).
* **Local-bound actions size themselves off the machine.** A semaphore derived from `NumCPU` bounds them with no configuration.
* **Priority lanes are subsumed.** Parked wants don't occupy workers, so a high-priority job simply registers a higher-priority `WANT` and takes the next slot.

What remains in fylr.yml: `addresses`, the callback URLs, and the timeouts.

## Migration

1. **(done)** Execserver: `/broker` endpoint, want-book, job-over-ws. fylr: broker client with per-address fallback to polling. Mixed fleets degrade gracefully in both directions.
2. **(done)** Body-mode call sites converted to pipe endpoints; the legacy token path exists only for old peers.
3. **(next major release)** Delete the legacy token path, `tokenResponseSendServerIP`, and the `parallel` / `parallelHigh` keys.

## Future extension: queue position

"3 video jobs running, 7 waiting — you are number 11." Unanswerable before: the line was a scrum of independent 1 s retry loops, so there was nothing to count. The want-book is the first time the line exists as a data structure, which turns position into a queryable fact:

* **Running + waiting live at the execserver.** A `QUERY {job_id}` → `POSITION {job_id, running, ahead, capacity}` message pair answers on demand: slots in use in the waitgroup, and — by replaying the grant rule (priority → round-robin → FIFO) over the current book — how many wants precede this one.
* **Unclaimed items live in the DB.** Claim-share bounding means some competitors may not be parked anywhere yet; fylr merges the DB count into the reported position.
* **ETA, optionally.** The execserver already keeps per-service job statistics; a rolling mean runtime turns position into "roughly N minutes". Always an estimate, never a promise — show the position as the hard number, the time as a hint.

***

_Design by Claude on behalf of Martin Rode, Programmfabrik. Tracked internally as ticket #80119, July 2026._
