# API

The Supervisor's JSON management API. Everything the web UI does goes through these endpoints.

## Base URL and authentication

The API is served under `/api` on the private management listener (`listen` setting, default `:8090`) and — when the `management_host` setting is set — through the public router under that host, e.g. `https://supervisor.example.com/api`.

All endpoints use HTTP basic auth with the `basic_auth_user` / `basic_auth_pass` settings; while `basic_auth_user` is empty, authentication is disabled. Errors use a single JSON envelope:

```json
{ "error": "<message>" }
```

The OpenAPI specification is maintained in the fylr repository (`internal/supervisor/apidocs/fylr-supervisor-openapi.yml`) and can be downloaded here:

{% file src="../../.gitbook/assets/fylr-supervisor-openapi.yml" %}
fylr Supervisor OpenAPI 3.0 specification
{% endfile %}

## Health

Liveness probe.

### `GET /healthz` — Liveness probe

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/healthz" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Instances

The fleet: create, inspect, edit, delete instances; start/stop, hibernate/wake; per-instance logs, metrics and overrides.

### `GET /fleet` — Fleet summary

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/fleet" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /instances` — List instances

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /instances` — Create an instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /instances/{id}` — Get one instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `PATCH /instances/{id}` — Edit an instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}" method="patch" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `DELETE /instances/{id}` — Delete an instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}" method="delete" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /instances/{id}/start` — Start an instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/start" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /instances/{id}/stop` — Stop an instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/stop" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /instances/{id}/hibernate` — Hibernate an instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/hibernate" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /instances/{id}/wake` — Wake a hibernated instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/wake" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /instances/{id}/logs` — Instance log tail

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/logs" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /instances/{id}/insights` — Instance insights

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/insights" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Binaries

A docker-registry-style store of fylr binaries: immutable sha256-identified artifacts, movable names (branches, release tags, aliases like `latest`). Instances follow a name; repointing a name rolls its running followers onto the new artifact.

### `GET /binaries` — List the binary store

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/binaries" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `PUT /binaries/{name}` — Push a binary / repoint a name

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/binaries/{name}" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `DELETE /binaries/{name}` — Delete a binary name

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/binaries/{name}" method="delete" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Backups & restore

The central backup store. Backup and restore are separate actions: a backup pulls a remote fylr into the store, a restore pushes a catalog entry into an existing or new instance. Only a restore purges its target.

### `GET /backups` — List backups

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/backups" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /backups` — Backup from a server

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/backups" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /backups/{name}/restore` — Restore a backup into an instance

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/backups/{name}/restore" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /backups/{name}/log` — Backup / restore log tail

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/backups/{name}/log" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `DELETE /backups/{name}` — Delete a backup

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/backups/{name}" method="delete" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Storage backends

Named file backends (S3 buckets, shared directories) assigned to instances as storage locations.

### `GET /storage-backends` — List storage backends

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/storage-backends" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /storage-backends` — Create a storage backend

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/storage-backends" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `PUT /storage-backends/{id}` — Update a storage backend

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/storage-backends/{id}" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `DELETE /storage-backends/{id}` — Delete a storage backend

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/storage-backends/{id}" method="delete" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Licenses

Centrally stored fylr licenses, routed to instances.

### `GET /licenses` — List licenses

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/licenses" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /licenses` — Upload a license

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/licenses" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `DELETE /licenses/{id}` — Delete a license

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/licenses/{id}" method="delete" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Certificates

Manual TLS certificates for the public router (ACME handles the rest).

### `GET /certs` — List certificates

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/certs" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `PUT /certs/{host}` — Store a manual certificate

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/certs/{host}" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `DELETE /certs/{host}` — Delete a manual certificate

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/certs/{host}" method="delete" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `POST /certs/inspect` — Inspect a PEM certificate

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/certs/inspect" method="post" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Rate limits

Request rate limits enforced by the public router.

### `PUT /instances/{id}/limits` — Set an instance's rate-limit override

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/limits" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /limits` — Get fleet rate limits

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/limits" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `PUT /limits` — Set fleet rate limits

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/limits" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Managed base config

Base-config values managed centrally and pushed into instances; managed values are locked in the instance's own base-config editor.

### `PUT /instances/{id}/managed-baseconfig` — Set an instance's managed base-config override

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/instances/{id}/managed-baseconfig" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /managed-baseconfig` — Get the fleet managed base config

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/managed-baseconfig" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `PUT /managed-baseconfig` — Set the fleet managed base config

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/managed-baseconfig" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Settings

Supervisor settings (control-DB backed, applied live).

### `GET /settings` — Get supervisor settings

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/settings" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `PUT /settings` — Update supervisor settings

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/settings" method="put" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Cluster

Shared infrastructure panes — OpenSearch, PostgreSQL, execserver, host machine.

### `GET /cluster/opensearch` — OpenSearch pane

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/cluster/opensearch" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /cluster/postgres` — PostgreSQL pane

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/cluster/postgres" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /cluster/execserver` — Execserver pane

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/cluster/execserver" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

### `GET /cluster/machine` — Machine pane

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/cluster/machine" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}

## Supervisor log

The supervisor's own log.

### `GET /logs` — Supervisor log

{% openapi src="../../.gitbook/assets/fylr-supervisor-openapi.yml" path="/logs" method="get" %}
[fylr-supervisor-openapi.yml](../../.gitbook/assets/fylr-supervisor-openapi.yml)
{% endopenapi %}
