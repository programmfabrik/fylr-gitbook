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

The `exec` map is the same as for [callbacks](callbacks/README.md) — it tells fylr how to run the plugin program (see [the exec map](manifest.md#the-exec-map)).

```yaml
extensions:
  dump/info:
    exec:
      service: "node"
      commands:
        - prog: "node"
          stdin:  { type: body }    # the request body
          stdout: { type: body }    # the response body
          args:
            - { type: "value", value: "%_exec.pluginDir%/server/dump_info.js" }
            - { type: "value", value: "%info.json%" }
```

## The plugin program

The program receives the request context as `%info.json%` (the requested URL, its parsed query, the HTTP headers, the plugin's base config, and the [callback tokens](callbacks/contract.md#calling-back-into-the-api) to call back into the API). It writes its response to STDOUT.

```javascript
// dump_info.js — echo the request info and body back to the caller
const info = JSON.parse(process.argv[2]); // %info.json% — an inline JSON string

let body = ""; // the request body arrives on STDIN (stdin: { type: body })
process.stdin.on("data", (d) => (body += d));
process.stdin.on("end", () => {
  // STDOUT is the response (stdout: { type: body })
  console.log(JSON.stringify({ you_requested: info.request, body }, null, 2));
});
```

Calling it:

```bash
curl -H "Authorization: Bearer $TOKEN" \
  "https://fylr.example.com/api/v1/plugin/extension/fylr_example/dump/info"
```

## Writing the response

With `stdout: { type: body }`, whatever the program writes to **STDOUT is streamed to the API client as the response body** (with the response's `Content-Type` forwarded). The response status is `200`; custom response headers cannot be set.

On error — a non-zero exit code, or an [API-error JSON](manifest.md#errors) written by the program — fylr answers with the error's `statuscode` (default `500`) and sets the `X-Execserver-Error` header, plus `X-Fylr-Error-Code` / `X-Fylr-Error` when an API-error JSON was given:

```json
{
  "code": "error.code",
  "error": "error string",
  "parameters": {},
  "realm": "api",
  "statuscode": 400
}
```

## See also

* [manifest.yml](manifest.md) — the `exec` map and placeholders.
* [Callbacks](callbacks/README.md) — hooks that run inside fylr's own API calls.
* [`/api/v1/plugin`](../api/endpoints/plugin/README.md) — the plugin management and extension endpoints.
