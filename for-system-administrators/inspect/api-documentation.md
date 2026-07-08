---
description: >-
  The /inspect/apidocs tool — the rendered API reference and the downloadable
  OpenAPI spec, optionally exported anonymously.
---

# API Documentation

The **API Documentation** page (`/inspect/apidocs/`) renders this instance's API reference and serves the machine-readable OpenAPI spec.

## The spec

| Endpoint | Format |
| --- | --- |
| `/inspect/apidocs/spec/spec.json` | OpenAPI **3.1** (JSON) |
| `/inspect/apidocs/spec/spec-gitbook.yml` | OpenAPI **3.0** (YAML, for GitBook's swagger renderer) |

The spec reflects the **running instance**, including the datamodel `/db/<objecttype>` paths for its own object types.

## Anonymous export

By default the spec requires `system.root`. To let integrators fetch it **without a login**, enable the base-config flag **`system.openapi_spec_endpoint.active`** — then `GET /api/v1/system/openapi/spec.json` returns the OpenAPI 3.1 document anonymously (the same document, mounted on the public API surface).

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [API](../../for-developers/api/README.md) — the published API reference.
