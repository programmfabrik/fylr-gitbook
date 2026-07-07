---
description: Plugin extensions add custom HTTP API endpoints to fylr, served under the plugin's base URL.
---

# Extensions

An **extension** adds a custom HTTP endpoint to fylr. Each key in the manifest's `extensions` map becomes an endpoint under the plugin's base URL:

```
https://<fylr-server>/api/v1/plugin/extension/<plugin-name>/<extension-name>
```

For example, the `fylr_example` plugin's `dump/info` extension is reachable at `…/plugin/extension/fylr_example/dump/info`. **All HTTP methods** are available, and an access token is required (as the `access_token` URL parameter, or an `Authorization: Bearer …` / `X-Fylr-Authorization: Bearer …` header).

## Defining an extension

The `exec` map is the same as for [callbacks](callbacks.md) — it tells fylr how to run the plugin program (see [the exec map](manifest.md#the-exec-map)).

```yaml
extensions:
  dump/info:
    exec:
      service: "node"
      commands:
        - prog: "node"
          stdin:  { url: "%_input.url%" }
          stdout: { url: "%_output.url%" }
          args:
            - { type: "value", value: "dump_info.js" }
            - { type: "value", value: "%info.json%" }
```

## The plugin program

The program receives the request context as `%info.json%` (the requested URL, its parsed query, the HTTP headers, the plugin's base config, and the [callback tokens](callbacks.md#calling-back-into-the-api) to call back into the API). It writes its response to `%_output.url%`.

```javascript
// dump_info.js — echo the request info back to the caller
const fs = require("fs");
const info = JSON.parse(fs.readFileSync(process.argv[2], "utf8")); // %info.json%

const body = JSON.stringify({ you_requested: info.request, query: info.query }, null, 2);

// POST the response back to fylr; headers set here are copied to the API response
fetch(info["_output.url"] ?? process.env.OUTPUT_URL, {
  method: "POST",
  headers: { "Content-Type": "application/json", "x-fylr-response-status": "200" },
  body,
});
```

Calling it:

```bash
curl -H "Authorization: Bearer $TOKEN" \
  "https://fylr.example.com/api/v1/plugin/extension/fylr_example/dump/info"
```

## Writing the response

The plugin returns data through the provided `/writer` endpoint (`%_output.url%`):

* **Writing to `%_output.url%` directly** — every HTTP header sent to that endpoint is copied onto the extension's API response, and the response status can be set with the special header `x-fylr-response-status`.
* **Writing to STDOUT** — no custom headers or status. If the program returns **less than 2048 bytes**, fylr checks the exit code; a non-zero exit sets the response status to `500`.

fylr adds timing information to the response headers.

On error, fylr tries to parse an [API-error JSON](manifest.md#errors); if a `statuscode` is given and headers have not been flushed yet (which happens once the 4&nbsp;KB buffer fills), that status is used:

```json
{
  "code": "error.code",
  "error": "error string",
  "params": {},
  "realm": "api",
  "statuscode": 400
}
```

## See also

* [manifest.yml](manifest.md) — the `exec` map and URL replacements.
* [Callbacks](callbacks.md) — hooks that run inside fylr's own API calls.
* [`/api/v1/plugin`](../api/endpoints/plugin/README.md) — the plugin management and extension endpoints.
