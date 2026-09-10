---
description: What to change in the configuration and in the deployment before restarting on 6.35
---

# Updating the execserver to 6.35

fylr 6.35 changes two things about the execserver at once: how fylr talks to it
— a fylr-initiated websocket, the *slot broker*, instead of the job token an
execserver polled for — and how its concurrency is sized: one auto-balanced CPU
pool instead of manually sized waitgroups.

Most installations need **no new setting**. What does need attention is a
handful of settings that stop working, and the deployment step that the two
sides now have to be moved together.

## 1. Move fylr and the execserver in one step

{% hint style="warning" %}
The broker is the **only** transport as of 6.35. A fylr and an execserver of
different versions exchange no jobs at all — there is no mixed-version
fallback, and no fallback to the old `GET /token` / `PUT /job` handshake, which
is removed.
{% endhint %}

Where the execserver runs inside the fylr process, this happens by itself.
Where it runs on its own — a separate host, a separate container, a pool of
pods — that machine has to be updated in the same maintenance window as fylr.
The same applies in the other direction: moving back moves both sides back.

Nothing is lost while the two sides are apart. A job whose execservers are all
unreachable is put back on the file queue right away and picked up when an
execserver connects again; fylr starts and serves without any execserver.

## 2. Check the configuration before you restart

`fylr config check` reads the configuration exactly the way the server does and
names the keys that no longer exist, without starting anything:

```bash
fylr config check fylr.yml
```

```
deprecated key "fylr.execserver.parallelHigh" (from fylr.yml): worker counts are automatic now, the key is ignored
unknown key "fylr.execserver.tokenResponseSendServerIP" (from fylr.yml): fylr has no such setting, it has no effect
["fylr.yml"]: 1 unknown key(s), 1 deprecated key(s)
```

The exit code is non-zero when a key is unknown, so the command can guard the
restart. See [checking the configuration](../configuration/check.md) for the
other two places the same list appears.

These are the execserver settings to look for:

| Setting | In 6.35 | What to do |
| --- | --- | --- |
| `fylr.execserver.tokenResponseSendServerIP` | removed — reported as an **unknown key** | Delete it. fylr learns the address an execserver reaches it on from the broker connection itself. |
| `fylr.execserver.parallelHigh` | **deprecated**, ignored | Delete it. Worker counts are derived from the connected execservers' capacity. |
| `fylr.execserver.parallel` | ignored — except the value `0` | Delete it, **unless** it is `0`: that still switches file processing off on this fylr, which is how an API-only node is configured. It is not reported, because `0` is a supported value. |
| `fylr.execserver.callbackBackendInternalURL`, `fylr.execserver.callbackApiInternalURL` | still override scheme and port, never the host | Neither is required any more. If one of them names a **host** — a Kubernetes Service, a load balancer in front of several fylr replicas — that host is now ignored; keep the setting only for a proxy in front of the listener that changes scheme or port. Where NAT sits between fylr and the execserver, `fylr.execserver.callbackBackendOwnURL` is the verbatim override. |
| `fylr.services.execserver.waitgroups` and the per-service `waitgroup:` keys | **deprecated**, ignored | Delete them. Every service runs on the one pool; to hold a service back, give it a `maxSlots` (next section). |
| per-service `commands:` blocks, and `workDir` | **deprecated**, ignored | Define each command once, under `fylr.services.execserver.commands`; `workDir` never had an effect. |
| a `/job/<service>` path on an `fylr.execserver.addresses` entry | **refused** at startup | Delete the path. Which services an execserver runs is what it announces itself; a dedicated execserver lists its services (next section). |
| `?pretty=true` on an `fylr.execserver.addresses` entry | ignored | Delete it; the broker strips the query. |

{% hint style="info" %}
A callback has to reach the **exact** fylr process that created the job: the
job's stdin/stdout pipe lives in that process's memory, and so does the open
write transaction behind a plugin's `api_tx_url`. A balanced address in one of
the callback settings was never a working configuration; from 6.35 it fails
visibly at connect time — the
[fleet topology page](../inspect/system.md#fleet-topology) reports it — instead
of landing on a sibling replica later, inside a job.
{% endhint %}

## 3. Decide how concurrency is sized

Every service draws from **one pool of slots**. A slot is a unit of admission,
not a core: a job holds one while it runs, and a command that leased a
temporary CPU allocation for a subprocess — `fylr convert` does this around
FFmpeg — holds more. Each service is classified *light* or *heavy* from the
runtime the execserver measures for it, and heavy jobs — long conversions,
ffmpeg, LibreOffice, ImageMagick — may never occupy the last `fastReserve`
slots. Short interactive work (metadata, plugins, IIIF) therefore always finds
a slot, however busy the conversions are. A service that has not been measured
often enough yet counts as *unknown* and is capped at `unknownShare` of the
pool until its first jobs classify it.

These are the shipped defaults; set a key only to change it:

```yaml
fylr+:
  services+:
    execserver+:
      slots: 0            # pool size, 0 = GOMAXPROCS: the core count, or the container's CPU limit
      fastReserve: -1     # slots only light jobs may take, -1 = a quarter of the pool, 0 = none
      heavyThreshold: 10s # a service slower than this counts as heavy
      unknownShare: 0.5   # pool share a service may use before it has samples
```

On a small container, `slots` may be set *above* the CPU limit so that short
jobs overlap their downloads and uploads instead of waiting on each other: a
2-CPU pod with `slots: 6` runs six jobs at once, one slot staying reserved for
light work. Behind a load balancer with several execservers set
`fastReserve: 0` — fylr parks a job on every execserver and takes the first
free slot, so the fleet is the headroom, and a reserve per pod only idles
slots.

### Holding one service back, and dedicated execservers

The per-service isolation of earlier versions — a waitgroup of its own — is one
key now, `maxSlots`: the most slots a service holds at once, jobs and temporary
CPU allocations together.

```yaml
fylr+:
  services+:
    execserver+:
      services+:
        ffmpeg:
          maxSlots: 2
```

An execserver that should run only some services lists exactly those: the
shipped `services` block is complete, `services+:` adjusts it, and a service
name with nothing behind it removes that service. Which execserver runs a
service is what it announces when it connects, so the `/job/<service>` path
filter on an address is not needed and is refused at startup.

The `waitgroups` block and the per-service `waitgroup:` keys are reported by
`fylr config check` as deprecated and are ignored — there is no manual mode
any more.

## 4. Give the execserver a temp directory that survives a restart

The balancer keeps a per-service runtime profile and snapshots it to
`<tempDir>/balance_seed.json` every few minutes, so a restarted execserver does
not relearn every service from zero. The snapshot is written **only when a temp
directory was configured** — `fylr.tempDir` or `fylr.services.execserver.tempDir`.
Without one the execserver uses the system temp directory and writes no
snapshot.

```yaml
fylr+:
  tempDir: /var/lib/fylr/tmp
```

In a container the directory has to be a volume to outlive the container. Note
that the snapshot is a prior, not a verdict: a restored service still counts as
unknown until its first live job confirms the profile. It is discarded when it
was written on a different operating system or architecture, or with a
different pool size, and a service the snapshot has not seen for a week ages
out of it.

Losing the snapshot costs nothing but a few minutes of deliberately
conservative scheduling after a restart.

## 5. Load-balanced and Kubernetes deployments

Several execserver instances behind one address work out of the box in 6.35 —
see [Scaling the execserver](scaling-the-execserver.md). What to remove and
what to add:

* **Remove the per-pod addressing.** `tokenResponseSendServerIP`, a headless Service, pod IPs from the downward API, L4 session affinity: none of it is needed. fylr dials the one published address and opens further connections to it while jobs back up, until it has found the whole fleet.
* **Point the readiness probe at `/readyz`.** It answers `200` while the execserver takes work and `503` from the moment it starts draining, so a terminating pod leaves the load balancer's endpoints before it exits. Without this a fylr still opens fresh connections to it, and the jobs granted there come straight back as "stopped, retry later".
* **Point the liveness probe at `/healthz`.** It answers `200` as long as the process runs, draining included — a liveness probe on `/readyz` would restart the container and cut the drain short.
* **Give the pod room to drain.** On `SIGTERM` the execserver stops granting slots and lets running jobs finish for `drainTimeoutSec` (default 20 s); a job still running at the deadline is answered with a retryable receipt that the client requeues on its own. `terminationGracePeriodSeconds` has to be comfortably above `drainTimeoutSec`, or the drain is killed halfway through.

```yaml
readinessProbe:
  httpGet: { path: /readyz, port: 8083 }
livenessProbe:
  httpGet: { path: /healthz, port: 8083 }
terminationGracePeriodSeconds: 45
```

## 6. After the restart

* The startup log states the pool the execserver decided on — its slots, the fast reserve, the heavy threshold.
* `/inspect/system/execserver/` lists the connected fylr servers, the balancer's caps — pool size, fast reserve, heavy threshold, and what is in flight against each of them — and per service its learned class and its mean runtime. It is where you check that the balancer's beliefs match the machine.
* [`/inspect/system/topology/`](../inspect/system.md#fleet-topology) shows the whole installation on one page: every fylr, every execserver, the load balancer when there is one, and the jobs moving between them — including a callback address that would not come back to the right replica.
* `/metrics` carries `fylr_execserver_jobs_done`, `fylr_execserver_jobs_failed` and `fylr_execserver_jobs_running`, labelled by service, for the long-term view.
