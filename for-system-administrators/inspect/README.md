---
description: >-
  /inspect is fylr's backend introspection and maintenance console — HTML
  dashboards and JSON dumps of the config, data model, objects, index, queues
  and system state, plus the home of several maintenance actions.
---

# The /inspect Backend

`/inspect` is fylr's built-in **operations console**: a set of HTML dashboards and JSON dumps that show a running instance's configuration, data model, objects, search index, queues, sessions and system state — and that drive maintenance actions such as re-indexing, term recalculation and backup / restore.

## Two ports, two auth models

/inspect is reachable on two ports with very different access rules:

* **Backend port — no authentication.** The backend port mounts /inspect directly, with no login gate (it also serves `/metrics`, `/debug/pprof/`, `/healthz`). It is meant to run on a **private network only** — never expose it publicly.
* **Webapp port — session + `system.root`.** The public webapp port reverse-proxies /inspect behind a session check: the logged-in user must hold the **`system.root`** right, otherwise the request is redirected to `/login`. This is how an administrator reaches /inspect in a browser.

So administrators use /inspect through the **webapp URL** (needs `system.root`); monitoring or tooling on a trusted host can hit the **backend port** directly.

## HTML dashboards or JSON

Every dump renders an **HTML dashboard** by default, or returns **JSON** when the request sends `Accept: application/json` (or `?accept=application/json`). The JSON projection is whitelisted per page, so it may expose fewer fields than the HTML view — see [`/api/v1` → the /inspect endpoints](../../for-developers/api/endpoints/README.md) for the documented JSON endpoints and their data.

## The home dashboard

Opening `/inspect/` shows the **instance overview**: the **Database** (driver, version, size, roles), the **Indexer** (OpenSearch/Elasticsearch host and status), **Settings** and **System Config**, the **Index Names** in use, the connected **Backends**, the **License**, and — when `fylr.debug.inspectShowEnvironment` is set — the host **Environment** and request headers.

## The tools

Each tool is a page under `/inspect/<tool>/`. The ones with settings or actions worth explaining have their own page below; the rest are straightforward "browse the X" dumps.

### Data & model

| Tool | Shows | Page |
| --- | --- | --- |
| `config` | the compiled base config | |
| `datamodel` | objecttypes, masks, fields | |
| `objects` | object dump — render an object against any datamodel version | |
| `objecttypes` | objecttype list and per-type stats | |
| `files` | file-production state, filters and actions, IIIF viewer | [Files and version production](../../files-and-version-production.md) |
| `collections` | the collection tree (paged, searchable) | |
| `pools`, `tags`, `transitions`, `publish`, `mappings`, `oai-pmh` | per-entity dumps | |
| `terms` | the suggestion term list | |
| `indexer` | search index, mappings, analyze | |
| `customdata` | custom-data-type values | |

### Access & sessions

| Tool | Shows |
| --- | --- |
| `users`, `groups`, `rights`, `presets` | the ACL model |
| `tokens` | issued OAuth tokens |
| `saml-sessions` | active SAML sessions |
| `events`, `messages`, `notifications`, `tasks` | per-entity dumps |

### System & maintenance

| Tool | Shows / does | Page |
| --- | --- | --- |
| `system` | reindex, purge, janitor, queues, execserver, backups, locations, console, status | [System](system.md) |
| `migration` | backup & restore in the browser | |
| `recalcterms` | rebuild the suggestion term list | |
| `sqlquery` | an arbitrary-SQL console (only when enabled) | |
| `license` | license info and the expiration-mail simulator | |
| `pages` | render page / email templates | |
| `apidocs` | the rendered API docs and the OpenAPI spec | |

## Read-only vs mutating

Most /inspect routes are **read-only** dumps. The ones that change state — and that the no-auth backend port therefore exposes to anyone who can reach it — are the System actions (`purge`, `reindex`), Term Recalculation, Migration (backup / restore), the email test send, and the SQL Query console. This is the reason the backend port must stay private; each is called out on its page.

## See also

* [Architecture](../architecture.md) — where the backend sits among the services.
* [Backups & Restore](../backup.md) and the [Migration Tool](../migration/README.md) — the CLI behind `/inspect/migration`.
