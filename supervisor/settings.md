# Settings reference

Every supervisor setting lives in the control database and is edited through **Settings** in the UI or `PUT /api/settings`. All of them apply **live** — saving never requires a supervisor restart; the two listeners rebind in place. On first boot each missing key is seeded with its default, overridable through an environment variable `FYLR_SUPERVISOR_<KEY>` (first boot only — a stored value always wins).

| Key | Default | Meaning |
| --- | --- | --- |
| `listen` | `:8090` | Management listener (API + UI). Rebinds live. |
| `router` | `:8091` | Public host-routing listener (HTTP). Empty disables routing. |
| `router_tls` | — | Public TLS listener, e.g. `:443`. Empty disables TLS. |
| `management_host` | — | Serve the management UI through the public router under this host (forced HTTPS, requires basic auth). |
| `basic_auth_user` / `basic_auth_pass` | — | HTTP basic auth in front of the management API + UI. Empty = open. |
| `trusted_proxies` | — | Comma-separated IPs/CIDRs whose forwarded-identity headers the router believes. Empty = the connection peer is the client. |
| `data_dir` | `instances` | Root directory holding each instance's files, configs and logs. |
| `port_range` | `20000-21000` | Loopback ports leased to children and the shared execserver. |
| `postgres_admin_dsn` | — | Keyword-form DSN of a role that can `CREATE DATABASE`; required for PostgreSQL instances. |
| `opensearch_addresses` / `opensearch_user` / `opensearch_pass` | — | The shared OpenSearch children get wired to. Changing it rolls running instances. |
| `default_binary` | `<default>` | Registry name every instance without an own selection follows; repointing it is the fleet upgrade. |
| `binary_keep_days` | `30` | Registry GC: unreferenced artifacts older than this are removed. 0 = off. |
| `execserver_cpus` | `auto` | CPU cap of the shared execserver's worker pool. |
| `hibernate_after` | — | Fleet idle window before an instance hibernates (e.g. `30m`, min `30s`); empty/`off` disables. Per-instance override in the editor. |
| `default_license_id` | — | Fleet default license inherited by instances without an own selection. |
| `default_storage_id` | the disk location | Fleet default storage location; seeded to the machine's disk location at first boot. |
| `managed_master_id` | — | Instance whose database and files seed every newly created managed branch instance. |
| `managed_storage_id` | — | Storage location stamped onto new managed instances (creation-time only). |
| `managed_execserver` | shared | Execserver preset stamped onto new managed instances (creation-time only). |
| `backup_dir` | `backups` | The central backup store — one subdirectory per backup. |
| `plugin_dir` | — | A directory of unpacked fylr plugins rendered into every child config. |
| `acme_enabled` / `acme_email` / `acme_ca` / `acme_eab_key_id` / `acme_eab_hmac_key` | — | ACME configuration for on-demand certificates (Certificates page). |

The fleet-wide **rate limits** and the **managed base config** (currently: the email server pushed into inheriting instances) are edited on their own Settings tabs and served by dedicated API endpoints (`/api/limits`, `/api/managed-baseconfig`).
