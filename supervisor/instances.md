# Instances

An instance is one fylr tenant: its own PostgreSQL database (or SQLite file), its own OpenSearch indices, its own files, reachable under its own hostname through the router. The dashboard lists the fleet with live status, memory, CPU and content statistics; the per-instance page adds charts, endpoints and a log viewer.

## Creating an instance

<figure><img src="../.gitbook/assets/supervisor/sv-new-instance.png" alt=""><figcaption><p>Creating an instance: copy from an existing one — with the consent line spelling out what will be copied — and choose its storage</p></figcaption></figure>

The two decisions at create time:

* **Copy from instance** — seeds the new instance as a **full copy** of an existing one: database and all files. The consent line under the select shows the source's object count, file count and file bytes before you commit. Sources whose files live on the machine's disk are hard-linked (instant, no extra space); sources keeping files on an S3 location are copied through their API, so the bytes are stored again locally. The copy runs with the source's encryption key, root password and license, and appears as a `seed-…` entry on the [Backups page](backups.md) with full logs. A disk-headroom preflight refuses copies the machine cannot hold.
* **Storage** — where new originals, renditions and backups land: the machine's **disk** location or a configured S3 location, inherited from the fleet default unless overridden. New locations can be added right from the dialog. See [Storage](storage.md).

Everything else — database backend (PostgreSQL for production, SQLite for tiny tests), replica count, followed [binary](binaries.md), execserver, host — has sensible defaults. The instance starts serving right after creation.

## The instance page

<figure><img src="../.gitbook/assets/supervisor/sv-instance-detail.png" alt=""><figcaption><p>Instance detail: status tiles, charts, endpoints — and one-click root access to frontend and /inspect</p></figcaption></figure>

Operation lives on the detail page: start/stop, hibernate, **Frontend (root) ↗** and **Inspect (root) ↗** (one-time root logins minted by the supervisor — no password juggling), plus tabs for the admin and system-admin views and the instance's parsed server log. Setup lives in the editor (Edit button): host, access credentials, license, storage, email server and rate-limit overrides — fleet-inherited concerns default to "inherit".

Edits that a child bakes in at startup (host, basic auth, replica count) apply through a **zero-downtime rolling restart**: new replicas come up and are confirmed serving before the old ones retire. Rate limits and storage assignments apply live.

## Replicas

An instance can run several replica processes over the same database and indices, load-balanced round-robin with sticky sessions. Rolling restarts walk the replicas one by one, so a fleet upgrade never takes an instance down.

## Hibernation

Idle instances are stopped to free memory and woken by the next request for their host — the visitor sees a boot page for a few seconds. Idle means: no successful requests, empty work queues and cold CPU; background noise (scanner probes, failed logins) deliberately does not keep an instance awake. The idle window is a fleet setting with a per-instance override ("never hibernate" for production tenants). A hibernated instance can also be woken manually or by a restore.

## Logs

Every instance's server log is parsed into a filterable table (level, day, full-text) with the client IP as its own column — request lines carry the real client address as seen by the router, so "who is hammering this instance" is one click (the IP filters the log). The supervisor's own log has a per-instance column too, so one instance's slice of supervisor events (wakes, rolls, storage pushes) is equally filterable.
