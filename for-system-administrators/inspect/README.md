---
description: >-
  /inspect is fylr's backend introspection and maintenance console — HTML
  dashboards and JSON dumps of the config, data model, objects, index, queues
  and system state, plus the home of several maintenan
---

# The /inspect Backend

`/inspect` is fylr's built-in **operations console**: a set of HTML dashboards and JSON dumps that show a running instance's configuration, data model, objects, search index, queues, sessions and system state — and that drive maintenance actions such as re-indexing, term recalculation and backup / restore.

## Two ports, two auth models

/inspect is reachable on two ports with very different access rules:

* **Backend port — no authentication.** The backend port mounts /inspect directly, with no login gate (it also serves `/metrics`, `/debug/pprof/`, `/healthz`). It is meant to run on a **private network only** — never expose it publicly.
* **Webapp port — session + `system.root`.** The public webapp port reverse-proxies /inspect behind a session check: the logged-in user must hold the **`system.root`** right, otherwise the request is redirected to `/login`. This is how an administrator reaches /inspect in a browser.

So administrators use /inspect through the **webapp URL** (needs `system.root`); monitoring or tooling on a trusted host can hit the **backend port** directly.

## HTML dashboards or JSON

Every dump renders an **HTML dashboard** by default, or returns **JSON** when the request sends `Accept: application/json` (or `?accept=application/json`). The JSON projection is whitelisted per page, so it may expose fewer fields than the HTML view — see [`/api/v1` → the /inspect endpoints](../../for-developers/api/endpoints/) for the documented JSON endpoints and their data.

## The home dashboard

Opening `/inspect/` shows the **instance overview**: the tools as tiles, then the details folded into sections: **Instance Info**, the **Database** (driver, version, size, roles), the **Indexer**, **Settings** and **System Config**, the **Index Names** in use, the connected **Backends**, the host **Environment** (shown when `fylr.debug.inspectShowEnvironment` is set) and the **Request Header**. A section opens and closes with a click on its heading, and the page remembers which ones are open.

**From version 6.36.0** the tiles are grouped into **Sections** and **Utilities**, and any inspect page can be a **favorite**: a section, a single objecttype, user or file, or a page with its query. The star next to a page's title adds it; the favorites are a bar under the top bar of every inspect page. There a favorite is dragged to its place, renamed with a double click (or F2; an empty name brings back the page's title) and removed with the × it shows on hover. The browser remembers the favorites. The title of a sub page names its section, followed by the rest in grey, for example **Objecttypes** `ot_b`. The top bar of every inspect page names the instance, its version, the database with its size, the indexer and the number of connected backends; in 6.35 a card at the top of the home page showed these, together with the user the page renders for.

## The tools

Each tool is a page under `/inspect/<tool>/`. The ones with settings or actions worth explaining have their own page below; the rest are straightforward "browse the X" dumps.

### Data & model

| Tool                                                             | Shows                                                        | Page                          |
| ---------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------- |
| `config`                                                         | the compiled base config                                     |                               |
| `datamodel`                                                      | objecttypes, masks, fields; **from version 6.35.0** a model explorer that draws them and what links them | [Datamodel](datamodel.md)     |
| `objects`                                                        | object dump — render an object against any datamodel version | [Objects](objects.md)         |
| `objecttypes`                                                    | objecttype list and per-type stats                           |                               |
| `files`                                                          | file-production state, filters and actions, IIIF viewer      | [Files](files.md)             |
| `collections`                                                    | the collection tree (paged, searchable)                      | [Collections](collections.md) |
| `pools`, `tags`, `transitions`, `publish`, `mappings`, `oai-pmh` | per-entity dumps                                             |                               |
| `terms`                                                          | the suggestion term list                                     |                               |
| `indexer`                                                        | search index, mappings, analyze                              |                               |
| `customdata`                                                     | custom-data-type values                                      |                               |

### Access & sessions

| Tool                                           | Shows                |
| ---------------------------------------------- | -------------------- |
| `users`, `groups`, `rights`, `presets`         | the ACL model        |
| `tokens`                                       | issued OAuth tokens  |
| `saml-sessions`                                | active SAML sessions |
| `events`, `messages`, `notifications`, `tasks` | per-entity dumps. **From version 6.35.0** an event that carries the job receipt of a produce or metadata run shows it under **Run** — the shell-quoted command line with a copy button, the arguments one per row, and stdout and stderr — and a task log links the event of each metadata recipe run as `event #<id>`. |

### System & maintenance

| Tool          | Shows / does                                                                     | Page                                        |
| ------------- | -------------------------------------------------------------------------------- | ------------------------------------------- |
| `system`      | reindex, purge, janitor, queues, execserver, topology, backups, locations, console, status | [System](system.md)                         |
| `migration`   | backup & restore in the browser                                                  | [Migration](migration.md)                   |
| `recalcterms` | rebuild the suggestion term list                                                 | [Term Recalculation](term-recalculation.md) |
| `sqlquery`    | an arbitrary-SQL console (only when enabled)                                     | [SQL Query](sql-query.md)                   |
| `license`     | license info and the expiration-mail simulator                                   | [License](license.md)                       |
| `pages`       | render page / email templates                                                    | [Pages](pages.md)                           |
| `apidocs`     | the rendered API docs and the OpenAPI spec                                       | [API Documentation](api-documentation.md)   |

## Read-only vs mutating

Most /inspect routes are **read-only** dumps. The ones that change state — and that the no-auth backend port therefore exposes to anyone who can reach it — are the System actions (`purge`, `reindex`), Term Recalculation, Migration (backup / restore), the email test send, and the SQL Query console. This is the reason the backend port must stay private; each is called out on its page.

## See also

* [Architecture](../architecture.md) — where the backend sits among the services.
* [Backups & Restore](../backup.md) and the [Migration Tool](../migration/) — the CLI behind `/inspect/migration`.
