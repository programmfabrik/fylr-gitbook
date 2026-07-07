---
description: >-
  /inspect is fylr's backend introspection surface — HTML dashboards and JSON
  dumps of the config, data model, objects, index, queues, migration and more,
  and the home of several maintenance actions. What it exposes and its two auth
  models.
---

# The /inspect Backend

`/inspect` is fylr's built-in introspection surface: a set of HTML dashboards and JSON dumps that show a running instance's configuration, data model, objects, search index, queues, sessions and system state — and that drive maintenance actions such as re-indexing, term recalculation and backup / restore.

## Two ports, two auth models

/inspect is reachable on two ports with very different access rules:

* **Backend port — no authentication.** The backend port mounts /inspect directly, with no login gate (it also serves `/metrics`, `/debug/pprof/`, `/healthz`). It is meant to run on a **private network only** — never expose it publicly.
* **Webapp port — session + `system.root`.** The public webapp port reverse-proxies /inspect behind a session check: the logged-in user must hold the **`system.root`** right, otherwise the request is redirected to `/login`. This is how an administrator reaches /inspect in a browser.

So: administrators use /inspect through the **webapp URL** (needs `system.root`); monitoring or tooling on a trusted host can hit the **backend port** directly.

## HTML dashboards or JSON

Every dump renders an **HTML dashboard** by default, or returns **JSON** when the request sends `Accept: application/json` (or `?accept=application/json`). The JSON projection is whitelisted per page, so it may expose fewer fields than the HTML view.

## What's there

### Configuration & data model

| Tool | Shows |
| --- | --- |
| `/inspect/config/` | the compiled base config |
| `/inspect/datamodel/` | objecttypes, masks, fields |
| `/inspect/objects/` | object dump — render an object against any datamodel version |
| `/inspect/files/` | [file-production](../files-and-version-production.md) state, IIIF viewer |
| `/inspect/collections/`, `/pools/`, `/tags/`, `/objecttypes/`, `/transitions/`, `/publish/`, `/mappings/`, `/oai-pmh/` | per-entity dumps |
| `/inspect/terms/` | the suggestion [term list](concepts/search-and-events.md#suggestions-and-terms) |
| `/inspect/indexer/` | search index, mappings, analyze (the elastic-indices overview needs `inspectEnableElasticIndices`) |

### Access & sessions

| Tool | Shows |
| --- | --- |
| `/inspect/users/`, `/groups/`, `/rights/`, `/presets/` | the ACL model |
| `/inspect/tokens/` | issued OAuth tokens |
| `/inspect/saml-sessions/` | active SAML sessions |
| `/inspect/events/`, `/messages/`, `/notifications/`, `/tasks/`, `/customdata/` | per-entity dumps |

### System & maintenance

| Tool | Shows / does |
| --- | --- |
| `/inspect/` | instance home — DB version/size, backends (host env only if `inspectShowEnvironment`) |
| `/inspect/system/` | system dashboard; **re-index** (`?reindex=1`) and **purge** buttons |
| `/inspect/system/janitor/` | the clean-up janitor's state |
| `/inspect/system/queues/`, `/execserver/`, `/locations/`, `/backups/`, `/console/`, `/status/` | runtime status |
| `/inspect/recalcterms/` | **Term Recalculation** |
| `/inspect/migration/` | **Backup & Restore** (incl. the rename-versions table and the target-instance token step) |
| `/inspect/license/` | license info and the expiration-mail simulator |
| `/inspect/sqlquery/` | an arbitrary-SQL console — registered only when `inspectEnableSqlQuery` is set |

### API docs

| Tool | Shows |
| --- | --- |
| `/inspect/apidocs/` | the rendered API documentation |
| `/inspect/apidocs/spec/spec.json` | the OpenAPI **3.1** document |
| `/inspect/apidocs/spec/spec-gitbook.yml` | the OpenAPI **3.0** document (for GitBook's swagger renderer) |

## Read-only vs mutating

Most /inspect routes are **read-only** GET dumps. The ones that change state — and that the no-auth backend port therefore exposes to anyone who can reach it — are:

* `POST /inspect/system/purge` — **destructive**: wipes all data (the UI button is gated by `fylr.allowpurge` + a base-config flag, but the endpoint itself is unauthenticated on the backend port);
* `GET /inspect/system/?reindex=1` — starts a full re-index;
* `POST /inspect/recalcterms` — starts a term recalculation;
* `POST /inspect/migration` — backup / restore / upload;
* `GET /inspect/pages/sendmail`, `GET /inspect/license/validate?send=1` — actually send an email;
* `/inspect/sqlquery/` — runs the SQL you enter.

This is the reason the backend port must stay private.

## Exporting the API spec

The spec is served at `/inspect/apidocs/spec/spec.json` (3.1) and `/inspect/apidocs/spec/spec-gitbook.yml` (3.0). To expose it on the **public API without a login**, enable the base-config flag **`system.openapi_spec_endpoint.active`** — then `GET /api/v1/system/openapi/spec.json` returns the same OpenAPI 3.1 document anonymously (otherwise that endpoint requires `system.root`).

## See also

* [Files and version production](../files-and-version-production.md) — the `/inspect/files` operations view.
* [Backups & Restore](../for-system-administrators/backup.md) and the [Migration Tool](../for-system-administrators/migration/README.md) — the `/inspect/migration` actions.
* [Search and events](concepts/search-and-events.md#suggestions-and-terms) — what Term Recalculation rebuilds.
