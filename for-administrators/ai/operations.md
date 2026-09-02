---
description: how AI work is scheduled, what is recorded, and where to look
---

# Queue, log and costs

## The queue

AI work that is not a user waiting for an answer goes through the `ai_queue`: tagging a file after an upload, embedding a record after it changed, filling a field in bulk. The queue survives restarts, retries what failed, and keeps the load on a provider bounded.

Two lanes:

* **Interactive** — what a user is waiting for. The chat holds a small number of slots per provider and answers `429` when they are all busy, instead of queueing a person behind a bulk run.
* **Bulk** — everything else, worked through a few jobs at a time.

`/inspect/system/ai-queue/` shows the queue: the running dispatcher, the counts by status, the newest jobs, and the stored vectors. Over the API, `GET /api/v1/ai/queue` lists jobs with their status, and a single job can be cancelled or retried.

An indexing run that finds records whose text changed queues their embeddings automatically. Turning embeddings on for the first time therefore means: save the settings, rebuild the index, and let the queue work through it.

## The log

Every call fylr makes is a row in `ai_request`: what it was for, which provider and model, which user, which subject, the tokens in and out, the status, and — for a failure — the error. Nothing is deleted when a job is retried; the row of the failed attempt stays.

Read it in the **Log** tab of the AI configuration, or over `GET /api/v1/system/ai/request/list`.

Which means costs are answerable: the log is the bill in the making, per model and per user.

## What to check when something is wrong

<table data-header-hidden><thead><tr><th width="290"></th><th></th></tr></thead><tbody>
<tr><td>The assistant says no model is permitted</td><td>The pool's or objecttype's <code>ai_config</code> — either not enabled, or its models are not enabled on the provider.</td></tr>
<tr><td>Nothing is tagged after an upload</td><td><code>ai_tagging.enabled</code>, and whether the file has a picture at all. Audio has none.</td></tr>
<tr><td>A semantic search is refused</td><td>Embeddings or semantic search are off in the <a href="configuration.md">AI configuration</a>.</td></tr>
<tr><td>A semantic search finds nothing sensible</td><td>Whether the records are embedded (the queue, and the vector count in the inspect page), and whether the index was rebuilt after the model changed.</td></tr>
<tr><td>Requests fail with HTTP 401 or 403</td><td>The provider's key, in the AI configuration. <strong>Test connection</strong> tells you in one click.</td></tr>
<tr><td>The chat is busy</td><td>All interactive slots for that provider are in use. It is a fair queue, not an error.</td></tr>
</tbody></table>

## The API

| | |
| --- | --- |
| `POST /api/v1/ai/complete` | One completion: a conversation, optionally with files and tools. Answers with the text, the tool calls, and the tokens. |
| `POST /api/v1/ai/queue` | Queue field prompts for records; `GET` lists them. |
| `POST /api/v1/ai/tag` | Tag one file now. |
| `GET /api/v1/ai/config` | What is permitted here: the models for a pool or objecttype, and whether semantic search is on. |
| `GET /api/v1/ai/tools`, `POST /api/v1/ai/tools/{name}` | The tool catalogue, and running one in the caller's session. |
| `GET`/`PUT /api/v1/system/ai/settings` | The instance-wide settings. |
| `GET`/`POST /api/v1/system/ai/provider/…` | The providers. |
