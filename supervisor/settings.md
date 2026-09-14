# Settings reference

The supervisor has two configuration surfaces: a minimal **bootstrap file** (YAML, read once at start) and the **runtime settings** in the control database, edited through **Settings** in the UI or `PUT /api/settings`. Runtime settings all apply **live** — saving never requires a supervisor restart; the two listeners rebind in place.

## Bootstrap file (fylr.yml)

Only the control-plane database connection is configured in the file — deliberately nothing else. Keys in dot notation:

| Key | Default | Meaning |
| --- | --- | --- |
| `fylr.supervisor.db.driver` | `sqlite3` | Control-DB driver. SQLite fits: the control plane is low-write and single-writer. |
| `fylr.supervisor.db.dsn` | — | Control-DB location, e.g. `/srv/fylr/control.db`. |

Everything else under `fylr.*` is fylr's ordinary configuration, inherited by every child instance — typically `fylr.elastic.addresses` for the shared OpenSearch. Remember the merge key: `fylr+:` merges into the embedded default configuration, a plain `fylr:` would replace it (see [Installation](installation.md)).

## Runtime settings (control DB)

Flat keys, one value each, as sent to `PUT /api/settings`. On first boot each missing key is seeded with its default — overridable once through an environment variable `FYLR_SUPERVISOR_<KEY>` (upper-cased key, e.g. `FYLR_SUPERVISOR_LISTEN`); afterwards the stored value always wins.

### Listeners & access

| Key | Default | Meaning |
| --- | --- | --- |
| `listen` | `:8090` | Management listener (API + UI). Rebinds live. |
| `router` | `:8091` | Public host-routing listener (HTTP). Empty disables routing. |
| `router_tls` | *(empty)* | Public TLS listener, e.g. `:443`. Empty disables TLS. |
| `management_host` | *(empty)* | Serve the management UI through the public router under this host (forced HTTPS). |
| `trusted_proxies` | *(empty)* | Comma-separated IPs/CIDRs whose `x-real-ip` / `x-forwarded-for` the router believes. Empty = the connection peer is the client. |

Who may use that listener is not a setting: management users, their two-factor and the API tokens live in their own tables and are managed under **Access** — see [Management access](access.md). The former `basic_auth_user` / `basic_auth_pass` keys are retired; an existing credential is adopted as the first user at boot.

### Provisioning

| Key | Default | Meaning |
| --- | --- | --- |
| `data_dir` | `instances` | Root directory holding each instance's files, configs and logs. |
| `port_range` | `20000-21000` | Loopback ports leased to child replicas and the shared execserver. |
| `postgres_admin_dsn` | *(empty)* | Keyword-form DSN of a role that can `CREATE DATABASE`; required for PostgreSQL instances. |
| `default_binary` | `<default>` | Registry name instances without an own selection follow; repointing it is the fleet upgrade. |
| `binary_keep_days` | `30` | Registry GC: unreferenced artifacts older than this are removed. `0` = off. |
| `execserver_cpus` | `auto` | CPU cap of the shared execserver's worker pool. |
| `managed_master_id` | *(empty)* | Instance (by id) whose database and files seed every newly created managed branch instance. |
| `managed_storage_id` | *(empty)* | Storage location stamped onto new managed instances (creation-time only). |
| `managed_execserver` | *(empty = shared)* | Execserver preset stamped onto new managed instances (creation-time only): empty/`shared` or `own`. |
| `managed_log_level` | *(empty = fylr default)* | Log level (`fylr.logger.level`) baked into the config of newly created instances (creation-time only): empty, `trace`, `debug`, `info`, `warn` or `error`. |
| `log_ingest_level` | *(empty = everything)* | What the log ingester stores from the fleet's log files: empty (everything the children write — their own log level decides that), a level as a floor, or `off` to stop ingesting (the files stay, the UI tails them). |
| `log_keep_per_source` | `50000` | Rows kept per source (supervisor, execserver, each instance): a chatty instance ages out its own history, nobody else's. |

### Shared OpenSearch

Children get wired to this cluster; changing it rolls running instances gently.

| Key | Default | Meaning |
| --- | --- | --- |
| `opensearch_addresses` | *(empty)* | Comma-separated addresses, e.g. `http://localhost:9200`. |
| `opensearch_user` | *(empty)* | Username; empty = no authentication. |
| `opensearch_pass` | *(empty)* | Password (write-only in the API). |

### Fleet behaviour

| Key | Default | Meaning |
| --- | --- | --- |
| `hibernate_after` | *(empty = off)* | Idle window before an instance hibernates (e.g. `30m`, minimum `30s`); per-instance override in the editor. |
| `default_license_id` | *(empty)* | Fleet default license inherited by instances without an own selection. |
| `default_storage_id` | *the disk location* | Fleet default storage location; seeded to the machine's disk location at first boot. |
| `backup_dir` | `backups` | The central backup store — one subdirectory per backup. |
| `plugin_dir` | *(empty)* | Directory of unpacked fylr plugins rendered into every child configuration. |

### ACME (on-demand certificates)

| Key | Default | Meaning |
| --- | --- | --- |
| `acme_enabled` | *(empty = off)* | Obtain certificates on demand at the first HTTPS request per host. |
| `acme_email` | *(empty)* | Account email for the CA. |
| `acme_ca` | *(Let's Encrypt)* | ACME directory: production/staging, ZeroSSL, Buypass or a custom URL. |
| `acme_eab_key_id` | *(empty)* | External Account Binding key id, for CAs that require it. |
| `acme_eab_hmac_key` | *(empty)* | The matching EAB HMAC key. |

The fleet-wide **rate limits** and the **managed base config** (currently: the email server pushed into inheriting instances) are not settings keys — they are edited on their own Settings tabs and served by `/api/limits` and `/api/managed-baseconfig`.
