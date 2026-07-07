---
description: >-
  The /inspect/sqlquery console — run arbitrary SQL against the fylr database.
  Disabled by default.
---

# SQL Query

The **SQL Query** console (`/inspect/sqlquery/`) runs arbitrary SQL against the fylr PostgreSQL database and shows the result. It is a debugging tool for people who know the fylr schema.

{% hint style="danger" %}
This runs whatever SQL you type — including writes and schema changes — with no safety net and, on the backend port, no authentication. Only use it on a private, non-production instance you can afford to break.
{% endhint %}

## Enabling it

The console is **not registered** unless `fylr.debug.inspectEnableSqlQuery` is set to `true` in `fylr.yml`. On a normal instance the page does not exist.

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
