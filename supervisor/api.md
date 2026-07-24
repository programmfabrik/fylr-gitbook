# Management API

Everything the UI does goes through the JSON management API under `/api` on the management listener. With `basic_auth_user`/`basic_auth_pass` set, every request needs HTTP basic auth. Errors come back as `{"error": "…"}` with a meaningful status code; asynchronous work (backups, restores, copies) answers `202` and is polled through its list endpoint.

Two companion references:

* the OpenAPI description shipped in-repo at `internal/supervisor/apidocs/fylr-supervisor-openapi.yml`,
* the apitest suites under `test/supervisor/api/` — executable, always-green examples for every endpoint listed here, runnable against a throwaway supervisor via `test/supervisor/run.sh`.

## Fleet & health

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/healthz` | Liveness probe |
| GET | `/api/fleet` | Fleet summary (dashboard header) |
| GET | `/api/logs` | The supervisor's own log, filterable (`q`, `level`, `date`, `instance`, `limit`) |

## Settings

| Method | Path | Purpose |
| --- | --- | --- |
| GET/PUT | `/api/settings` | All control-DB settings ([reference](settings.md)); PUT validates and applies live |
| GET/PUT | `/api/limits` | Fleet rate limits |
| GET/PUT | `/api/managed-baseconfig` | Fleet-wide managed base config (email server) |

## Instances

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/instances` | List with live status |
| POST | `/api/instances` | Create (+ start); `copy_from_id` seeds a full copy |
| GET | `/api/instances/{id}` | Single view; `?probe_login=1` probes the child's license login gate |
| PATCH | `/api/instances/{id}` | Edit (host, auth, replicas, binary, storage, license, …) |
| DELETE | `/api/instances/{id}` | Remove; `?drop_db=true` drops the database |
| POST | `/api/instances/{id}/start` · `/stop` | Desired-state changes |
| POST | `/api/instances/{id}/hibernate` · `/wake` | Force hibernation / wake |
| GET | `/api/instances/{id}/logs` | The instance's parsed server log |
| GET | `/api/instances/{id}/insights` | Content statistics, index state, event charts |
| PUT | `/api/instances/{id}/limits` | Per-instance rate-limit override |
| PUT | `/api/instances/{id}/managed-baseconfig` | Per-instance base-config override |
| POST | `/api/instances/{id}/root-access` | Mint a one-time root login URL (`target`: `frontend` or `inspect`) |

## Storage locations

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/storage-backends` | List incl. usage and the disk location |
| POST | `/api/storage-backends` | Create (kind `s3` or `file`) |
| PUT | `/api/storage-backends/{id}` | Update; the disk location only allows directory changes |
| DELETE | `/api/storage-backends/{id}` | Delete an unused location |

## Backups

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/backups` | The store catalog with job status |
| POST | `/api/backups` | Pull a backup from a source (`engine`: `api` or `db`) |
| POST | `/api/backups/{name}/restore` | Restore into an existing (`instance_id`) or new (`new_instance`) instance |
| GET | `/api/backups/{name}/log` | Backup / restore phase log (`?file=restore`) |
| DELETE | `/api/backups/{name}` | Remove from the store |

## Binaries

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/binaries` | Registry contents |
| PUT | `/api/binaries/{name}` | Push a build (body = binary; `?version=`, `?aliases=`, `?sha256=` repoint, `?managed=true&host=` standing instance) |
| DELETE | `/api/binaries/{name}` | Remove a name |

## Certificates

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/certs` | Per-host certificate state |
| POST | `/api/certs/inspect` | Name the hosts inside a PEM |
| PUT | `/api/certs/{host}` | Store a manual certificate (`cert_pem`, `key_pem`) |
| DELETE | `/api/certs/{host}` | Remove a manual certificate |

## Licenses

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/licenses` | Stored licenses incl. validation problems and usage |
| POST | `/api/licenses` | Upload (signature verified) |
| DELETE | `/api/licenses/{id}` | Delete an unused license |

## Abuse shield

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/strikes` | Current per-IP strikes and bans |
| DELETE | `/api/strikes/{ip}` | Forgive an IP / lift its ban |

## Infrastructure

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/cluster/machine` | Host snapshot + time series |
| GET | `/api/cluster/opensearch` | Shared-cluster health |
| GET | `/api/cluster/postgres` | Connections + per-DB sizes |
| GET | `/api/cluster/execserver` | Shared execserver status |
| GET | `/api/cluster/execserver/log` | Its log |
