---
description: >-
  Configure webhooks that workflow (transition) actions call when records are
  inserted, updated or deleted — either asynchronously after the save, or
  synchronously before the save to modify the records.
---

# Workflow Webhooks

A **workflow webhook** is an HTTP endpoint that **fylr** calls from the **webhook** action of a workflow (transition).

Each webhook is defined once in the [base configuration](#configuration), and can be used in one or more workflow actions.

## Usage

See [Workflows](../permissions/tags-and-workflows.md#workflows) on how to setup workflows. Create a new workflow (or extend an existing) one, and select one of the configured workflows as the webhook [**action**](../permissions/tags-and-workflows.md#action).

When the workflow fires, **fylr** sends an HTTP `POST` with a JSON body containing the affected records to the configured URL. Depending on the action's **callback** setting, the webhook either runs *after* the records are saved (and cannot change them) or *before* they are saved (and may modify them). See [Callback modes](#callback-modes).

The configured webhook targets can be any external endpoint which is capable of receiving POST requests with JSON data. The handling of the data is out of the scope of fylr, for more info see external documentation, e.g. [https://en.wikipedia.org/wiki/Webhook](https://en.wikipedia.org/wiki/Webhook). It is also possible to use fylr as the webhook target, in this case the fylr API must be [extended by a plugin](../../for-developers/plugin/extensions.md) to handle the webhook data.


## Configuration

Each row in the table defines one webhook.

### Name

The technical name of the webhook. This is the name you select in the workflow **Webhook** action. Names must be unique.

### URL

The absolute `http(s)` URL **fylr** posts to. The request is always a `POST` with `Content-Type: application/json`.

### HMAC Secret

Optional shared secret. If set, **fylr** signs the request body and sends the signature in two headers so the receiver can verify the payload was not tampered with:

* `X-Hub-Signature: sha1=<hmac-sha1 of the body>`
* `X-Hub-Signature-256: sha256=<hmac-sha256 of the body>`

Both are keyed with the secret. Leave empty to send no signature.

A receiver verifies (at least) the SHA-256 signature over the **raw request body**:

```python
import hashlib, hmac

def verify(headers, body: bytes, secret: str) -> bool:
    got = headers.get("X-Hub-Signature-256", "")
    want = "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(got, want)
```

### Timeout

Request timeout in seconds. `0` (the default) means no explicit timeout. For a `pre_save` webhook this is the time the **save waits** for the webhook to respond, so keep it short.

### Send Authorization Header

If enabled, **fylr** adds an `Authorization: Bearer <access token>` HTTP header to the request. Use this when the webhook URL is served by **fylr** itself (or another service that authenticates against **fylr**), so the call is authenticated as the current user.

### Include Access Token

If enabled, the access token of the current user is included in the JSON body under `info.api_user_access_token`, so the webhook can call **back** into the **fylr** API (e.g. to load or write records). If disabled, the token is omitted from the payload.

{% hint style="info" %}
**Send Authorization Header** controls the HTTP `Authorization` *header* of the outgoing request; **Include Access Token** controls whether the token is part of the JSON *body*. They are independent.
{% endhint %}

## Callback modes

The **callback** of a workflow **Webhook** action selects *when* the webhook runs and *what* **fylr** does with its response. It is set on the action, not here in the base configuration.

### `after_commit_async` (default)

* Runs **after** the records have been committed, asynchronously.
* The webhook receives the saved records but **cannot modify them** — its response body is not applied. The outcome is recorded as an event: [`WEBHOOK`](../events/event-type-reference.md) on success, or [`WEBHOOK_ERROR`](../events/event-type-reference.md) on failure (a transport error or an HTTP status outside `2xx`). The response body, if any, is stored in the event for inspection.
* Because the save is already committed, a webhook failure does **not** roll it back.

Use this mode for fire-and-forget notifications and external side effects.

### `pre_save`

* Runs **synchronously inside the save**, before the records are committed.
* **fylr** posts the records and **waits for a JSON response** describing the records to write. The webhook may return them modified — the changes are saved in the same transaction — return them unchanged, or abort the save with an error. See [Response (`pre_save`)](#response-pre_save).
* Any failure — an unreachable endpoint, a non-`2xx` status, a malformed or empty response body, or a returned `error` — **aborts the whole save**, and the client receives an error.

Use this mode to enrich or validate records *as part of* the save.

{% hint style="info" %}
`pre_save` blocks the save until the webhook answers (up to **Timeout**). It is only suitable for fast, synchronous work. For slow processing — for example an external AI service — use `after_commit_async` and update the record with a separate API call when the work is done.
{% endhint %}

## Request payload

For both modes **fylr** posts a JSON object:

```json
{
  "info": { "api_url": "…", "api_user_access_token": "…", "api_user": { … } },
  "objects": [
    { "_objecttype": "…", "_mask": "_all_fields", "_callback_context": { "hash": "…" }, "…": "…" }
  ]
}
```

* `info` carries the [callback contract](../../for-developers/plugin/callbacks/contract.md) — the API base URL and, **if Include Access Token is enabled**, an access token for calling back into **fylr**.
* `objects` are the affected records rendered with the `_all_fields` mask. Each carries a `_callback_context.hash` used to match the record on the way back.

## Response (`pre_save`)

A `pre_save` webhook **must** return a JSON object:

```json
{
  "objects": [ "…" ],
  "upload_log": [ "…" ],
  "error": { "code": "my.error.code", "realm": "api", "statuscode": 400 }
}
```

* `objects` — the records to update. Each must carry back the **same** `_callback_context.hash` it was sent with and use the `_all_fields` mask. Only records whose hash matches are updated; a returned record replaces the posted one, so return it as received with only the intended changes — see [db\_pre\_save → the response](../../for-developers/plugin/callbacks/db-pre-save.md#the-response).
* `error` *(optional)* — an [API-error envelope](../../for-developers/plugin/callbacks/contract.md#errors). If present, the save is aborted and this error is returned to the client.
* `upload_log` *(optional)* — file-upload log entries.

{% hint style="warning" %}
**To make no changes, return `{"objects": []}`** — an empty array is the "not modified" signal, and the save proceeds normally.

The response must be **valid JSON**. An **empty body** cannot be parsed and fails the save with `Error unmarshal db_pre_save: EOF`. A webhook that has nothing to change must still return `{"objects": []}`, never an empty response.
{% endhint %}

For the full callback contract — shared with `db_pre_save` plugin callbacks — see [Plugins → Callbacks](../../for-developers/plugin/callbacks/README.md).
