# Installation

The supervisor ships inside the regular fylr binary — there is no separate package. A machine that can run fylr can run a fleet.

## Requirements

* The fylr binary (Linux amd64/arm64, macOS, Windows).
* PostgreSQL with a role that may `CREATE DATABASE` (the *admin DSN*) — each instance gets its own database `fylr_<name>`.
* OpenSearch, shared by all instances (each instance uses its own index set, prefixed with the instance name).
* DNS pointing the instance hostnames at the machine, typically a wildcard record like `*.example.com`.

SQLite-backed instances work without PostgreSQL and are meant for tests and tiny setups.

## Bootstrap configuration

The supervisor's YAML holds **only** the control-DB connection; the shared OpenSearch can be inherited by every child from the same file. Everything else is a runtime setting in the control database (see the [settings reference](settings.md)):

```yaml
# supervisor.yml
fylr+:
  # inherited by every child instance:
  elastic:
    addresses: ["http://localhost:9200"]

  supervisor:
    db:
      driver: sqlite3
      dsn: /srv/fylr/control.db
```

```sh
fylr supervisor -c supervisor.yml
```

On first boot the supervisor seeds its settings with defaults (management listener `:8090`, router `:8091`, data dir `instances`, port range `20000-21000`) and creates the **disk** storage location pointing at `<data_dir>/{name}/_files`. Open `http://localhost:8090/` for the dashboard, then set the PostgreSQL admin DSN under **Settings → Provisioning**.

For unattended setups every seeded default can be overridden at first boot through environment variables named `FYLR_SUPERVISOR_<SETTING>`, e.g. `FYLR_SUPERVISOR_LISTEN=:9000`. A stored value always wins afterwards — the control DB stays the single source of truth.

## systemd

The unit needs one non-obvious property: `KillMode=process`. Child instances and the shared execserver deliberately survive a supervisor restart (the reconciler re-adopts them), so only the main process may be killed:

```ini
[Unit]
Description=fylr supervisor
After=network-online.target postgresql.service opensearch.service

[Service]
User=fylr
WorkingDirectory=/srv/fylr
ExecStart=/srv/fylr/bin/fylr supervisor -c /srv/fylr/supervisor.yml
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Deploying a new supervisor binary is a plain binary swap plus `systemctl restart fylr-supervisor`: running children keep serving and are re-adopted; they load the new binary only on their own next start or roll.

## Management access

The management listener serves the UI and API, guarded by HTTP basic auth once `basic_auth_user`/`basic_auth_pass` are set (recommended — without them the API is open). The UI can additionally be served through the public router under a dedicated hostname (`management_host` setting, forced HTTPS), and the router answers it on `supervisor.<zone>` for every DNS zone the fleet serves — the `supervisor` host label is reserved for this.
