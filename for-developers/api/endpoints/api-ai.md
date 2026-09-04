---
description: the AI endpoints, and the tools a model can be given
---

# /api/v1/ai

**From version 6.36.0.** These are the endpoints behind the [assistant](../../../for-users/assistant/README.md): one completion call, a catalogue of tools, and the instance-wide settings.

Two things are worth knowing before the reference.

**fylr composes nothing.** `POST /ai/complete` sends what it is given — the system framing, the conversation, the tools — and adds what only the server can: the model, the provider credentials, the record's files if the policy allows them, and the audit row. The framing lives in the caller, which is why the assistant pane can be replaced without touching the backend.

**fylr does not run the model's tools.** It answers with the model's `tool_calls` and the caller runs each one through `POST /ai/tools/{name}`. That call happens **in the caller's own session**, so a tool sees exactly what that user may see. The model never touches the API and never holds a credential.

## The loop

```
POST /ai/complete   { system, messages, tools: [...] }
   → { tool_calls: [ { id, name, input } ] }

POST /ai/tools/search_objects   { query: "...", terms: "..." }
   → { result: { hits: [...] } }

POST /ai/complete   { messages: [ ..., tool_result ] }
   → { text: "..." }
```

The caller decides what to do between the steps: ask the user before running a tool that changes something, run a tool in the browser rather than on the server, or stop.

## The tools

`GET /ai/tools` hands out the catalogue with a JSON Schema per tool. Two flags decide how a caller treats one:

<table data-header-hidden><thead><tr><th width="120"></th><th></th></tr></thead><tbody>
<tr><td><code>write</code></td><td>The tool changes something. fylr checks the rights regardless — the flag is there so a caller can ask the user first, not as the security boundary.</td></tr>
<tr><td><code>client</code></td><td>The tool moves the window rather than the data: opening a record, switching the view, putting a search into the search bar. The browser runs it; the server refuses it.</td></tr>
</tbody></table>

What the catalogue holds today:

| Tool | | |
| --- | --- | --- |
| `search_objects` | reads | Finds records, or lists them by age when the request names no subject. |
| `find_similar` | reads | The records whose picture looks like another record's. |
| `count_objects` | reads | How many a search would find, without running it in front of anyone. |
| `search_fields` | reads | What a search can be narrowed by, and which objecttypes are in the main search rather than the lists. |
| `get_objects` | reads | Records by id — their texts and the ids of their files. |
| `find_user` | reads | A user by email or login. |
| `create_collection` | **changes** | A collection under the user's own top level. |
| `add_to_collection` | **changes** | Puts records into one. |
| `share_collection` | **changes** | Shares one, with a notification mail. |
| `search_in_app` | window | Puts a search into the search bar and runs it. |
| `apply_facet` / `clear_filters` | window | Ticks and unticks the filter tree. |
| `list_facets` | window | What the result on screen is made of, and how much of it. |
| `set_sort` | window | Orders it by relevance or by age. |
| `switch_view` | window | Moves to the main search or to the lists. |
| `open_object` / `show_collection` | window | Shows one record or one collection. |
| `ask_user` | window | Asks which of two readings of a request to act on. |
| `look_closer` | window | Asks for a larger rendition of the record's files and answers again. |

The window tools are the assistant's own; a different caller implements the ones it has a window for and leaves the rest out of `tools`.

## What a tool answers with

A tool that changes the screen answers with the screen: `records_on_screen`, and `active_filters` listing everything still narrowing it. That is deliberate — a model that is only told "done" will describe what it meant to do, and a number it cannot check is a number it will invent.

## Endpoints

### `POST /ai/complete` — One completion, with tools.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/ai/complete" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /ai/config` — The AI policy that applies here.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/ai/config" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /ai/tools` — The tool catalogue.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/ai/tools" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /ai/tools/{name}` — Run one tool.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/ai/tools/{name}" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `POST /ai/tag` — Tag one file now.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/ai/tag" method="post" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `GET /system/ai/settings` — Read the AI settings.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/system/ai/settings" method="get" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

### `PUT /system/ai/settings` — Write the AI settings.

{% openapi src="../../../.gitbook/assets/fylr-openapi.yml" path="/system/ai/settings" method="put" %}
[fylr-openapi.yml](../../../.gitbook/assets/fylr-openapi.yml)
{% endopenapi %}

## Rights

`/ai/complete`, `/ai/tools` and `/ai/tag` need a session, and everything they do is bounded by that session's rights. `/system/ai/settings` and the provider endpoints need `system.root`.
