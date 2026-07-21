---
description: The unified callback contract — the info map every callback receives, the access tokens to call back into the fylr API, the plugin_user mechanism, and the error format.
---

# The callback contract

Callbacks run server-side and frequently need to call back into the fylr API — to read the base config, load or write objects, or search. For this, every callback receives the same set of context fields, the **callback contract**, independent of which hook runs.

## Where the contract fields live

* For **db\_pre\_save**, **transition\_db\_pre\_save**, **collection upload** and the **export** hooks, the payload carries the hook's own data next to the contract fields, which live under the `info` key: `info.api_url`, `info.api_user_access_token`, …
* For **extensions** the request body is streamed to STDIN as-is, so the contract fields are only available via the `%info.json%` argument.
* Any callback can *additionally* receive the `info` map as a command argument by passing `%info.json%` in its `exec` args — it is substituted as an inline JSON string (parse `process.argv[n]` directly; it is not a file path).

## The `info` map

| Property | Presence | Description |
| --- | --- | --- |
| `api_url` | always | Base URL to call back into the API. Append `/api/v1/…` to reach an endpoint. |
| `external_url` | always | The configured external URL of the fylr instance — for building links meant for humans. |
| `api_user_access_token` | always¹ | OAuth2 access token to call the API **as the user the current API call runs as**. |
| `api_user` | when a user context exists | The current API user (the `who`). |
| `request` | when the hook runs inside an HTTP request | Information about the triggering request: `url`, `host`, `method`, `query`, `header`. |
| `config` | plugin callbacks² | `config.system` — the base config visible to the plugin — and `config.plugin.<plugin-name>` — the plugin's own base-config additions, decrypted. |
| `plugin_user_access_token` | only if `plugin_user` is configured | Access token of the configured **plugin user** (see below). |
| `plugin_user` | only if `plugin_user` is configured | The plugin user (the `who`) for `plugin_user_access_token`. |

¹ For [workflow webhooks](../../../for-administrators/readme/workflow-webhooks.md) the token is removed from the payload unless the webhook enables *include access token*.
² Workflow webhooks run without a plugin, so their payload has no `config` key.

Individual hooks add more keys — for example the transition action's `info` object ([transition\_db\_pre\_save](transition-db-pre-save.md)), `file` / `collection` / `collection_config` ([collection upload](collection-upload.md)), or `export` / `transport` / `plugin_action` ([export](export.md), [export\_transport](export-transport.md)).

## Access tokens

A callback always gets a token for the **current API user**, and *additionally* a token for the **plugin user** when one is configured — never one *or* the other.

{% hint style="info" %}
**These tokens are unbound and short-lived.** fylr binds a browser session token to the browser via the `fylr-browser-id` cookie, so a plugin replaying such a token server-side — without that cookie — would be rejected by session binding. For a browser-bound session fylr therefore mints a fresh, **session-binding-free** token for the callback; tokens of regular API clients are already unbound and are passed through. Freshly minted tokens are revoked once the callback returns — treat them as valid only for the duration of the callback and do not persist them.
{% endhint %}

## The plugin user

By default a callback acts as the user who triggered the API call — with that user's permissions. When a callback needs its *own*, well-defined set of permissions (for example to write objects the triggering user cannot), the manifest entry declares a **plugin user**:

```yaml
callbacks:
  db_pre_save:
    callbacks:
      write_linked:
        plugin_user:
          base_config: "user.api_user"   # <section>.<parameter> in the plugin's base_config
        exec: { … }

# the referenced base-config addition — a parameter of type "user"
base_config:
  - name: user
    parameters:
      api_user:
        type: user
```

`base_config` names a parameter of type `user` in the plugin's own base-config additions, as `<section>.<parameter>`. The administrator selects the acting user there in the base configuration. At run time fylr issues an unbound token for that user and passes it as `plugin_user_access_token` / `plugin_user`. If no user is configured, or the configured user is the calling user, the plugin user falls back to the current API user (both tokens are then equal).

The plugin user is supported on `db_pre_save` step callbacks, `transition_db_pre_save`, collection-upload `objects` callbacks, `export` callbacks and [extensions](../extensions.md).

## Calling back into the API

```javascript
// read the payload, then load the base config over the API
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", async () => {
  const payload = JSON.parse(input); // { info: {…}, objects: […] }
  const info = payload.info;

  // prefer the plugin user, if one is configured
  const token = info.plugin_user_access_token ?? info.api_user_access_token;

  const config = await fetch(`${info.api_url}/api/v1/config`, {
    headers: { Authorization: `Bearer ${token}` },
  }).then((r) => r.json());

  console.log(JSON.stringify({ objects: [] }));
});
```

{% hint style="warning" %}
**export — backwards compatibility:** the export payload additionally contains a legacy `api_callback` map (`{ "token", "url" }`) equivalent to `info.api_user_access_token` + `info.api_url`. It is kept so existing export plugins keep working; **new export plugins should use the contract fields above.**
{% endhint %}

## Errors

A callback signals an error in one of two ways:

* **Exit with a non-zero exit code.** If STDOUT contains an API-error JSON (see below, without the `error` wrapper), that error is used; otherwise a generic error naming the failed callback is reported.
* **Exit zero and return the API-error JSON under a top-level `error` key** in the response body:

```json
{
  "error": {
    "code": "my_plugin.validation.failed",  // defined in the plugin's l10n
    "parameters": { "field": "title" },     // values for the localized message
    "realm": "api",
    "statuscode": 400
  }
}
```

An API error returned either way is passed to the API client **as-is** — with the plugin's error code, parameters and status code — so a plugin can produce first-class, localized validation errors:

```javascript
// reject the save with a localized validation error
console.log(JSON.stringify({
  code: "validation.plugin.error",
  statuscode: 400,
  parameters: { field: "title" },
}));
process.exit(1);
```

Any other failure (non-zero exit without an error JSON, invalid or empty response body) is wrapped in a generic error naming the failed runner. What an error does to the running operation is described on each hook's page.

## See also

* [Callbacks overview](README.md) — how a callback program is executed.
* [manifest.yml → errors](../manifest.md#errors) — the API-error JSON in detail.
* [`/api/v1/config`](../../api/README.md) — the API the tokens are used against.
