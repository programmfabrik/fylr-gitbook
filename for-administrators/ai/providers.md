---
description: who fylr may talk to, and with which models
---

# AI Providers

A **provider** is one AI service fylr may send requests to. It carries the endpoint, the credentials and the list of models that are allowed to be used — nothing in fylr calls a model that is not on that list.

Providers live in the **AI configuration** app (black menu → **AI configuration**, tab **Providers**). Creating and editing them needs the `system.root` right.

## The fields

<table data-header-hidden><thead><tr><th width="180"></th><th></th></tr></thead><tbody>
<tr><td><strong>Name</strong></td><td>How the provider is addressed everywhere else, for example <code>claude</code>. A model is named <code>&lt;provider&gt;/&lt;model&gt;</code>, so the name is part of every reference.</td></tr>
<tr><td><strong>Type</strong></td><td>Which service this is: <code>anthropic</code>, <code>openai</code>, <code>ollama</code>, or the built-in <code>dummy</code>. The type decides what the provider can do and how it is addressed.</td></tr>
<tr><td><strong>API Key</strong></td><td>The key. It is stored encrypted and never leaves fylr — the API answers with <code>*****</code>. A local provider that needs none leaves it empty.</td></tr>
<tr><td><strong>Base URL</strong></td><td>Empty uses the vendor's endpoint. Set it for a local or proxied service, for example <code>http://localhost:11434</code> for Ollama.</td></tr>
<tr><td><strong>Models</strong></td><td>The models this provider may be used with, in order — the first is its default. <strong>Load models</strong> asks the service what it offers; a type that cannot report a list is filled in by hand.</td></tr>
<tr><td><strong>Enabled</strong></td><td>A disabled provider is refused everywhere, without changing any setting that names it.</td></tr>
</tbody></table>

**Test connection** sends one cheap request and reports what came back — do that before pointing a pool or the settings at a new provider.

## The types

| Type | Completion (chat, tagging) | Embeddings | Needs a key |
| --- | --- | --- | --- |
| `anthropic` | yes, with images and tools | — | yes |
| `openai` | yes | yes | yes |
| `ollama` | yes | yes | no |
| `dummy` | deterministic answers, for tests | deterministic vectors | no |

Anthropic has no embedding model, so an instance that runs everything on Claude still needs a second provider — OpenAI or a local Ollama — for the vectors.

The `dummy` type is built into fylr and talks to nothing. It answers deterministically, which is what the automated tests use; it is not meant for production.

## Where a model is chosen

A provider being enabled does not mean it is used. Every feature names its model explicitly:

* **Tagging** — the `ai_tagging` block in the base config, or a pool's / objecttype's `custom_data`.
* **Semantic search and the search assistant** — the [AI configuration](configuration.md) settings.
* **The chat in the editor** — the pool's or objecttype's `ai_config`, which lists the models permitted for the records there.

Each of those, the embedding model excepted, takes a list rather than a single model: fylr tries them in order and steps over a provider that is out of credit or rate limited. See [A model may be a chain](configuration.md#a-model-may-be-a-chain).

That way a pool can be allowed to use an expensive model while the rest of the instance is not.
