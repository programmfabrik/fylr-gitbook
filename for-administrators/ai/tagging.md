---
description: what the AI writes about an uploaded file, and how it reaches your fields
---

# Tagging files

When a record that references a file is saved, fylr can send a picture of that file to an AI provider and ask what is in it. The answer is stored **with the file**, in its metadata, and is offered to the [metadata mapping](../metadata-mapping.md) like any other metadata source.

Storing it with the file rather than in a record's fields matters: the same file used by three records carries its description once, the description survives when someone edits the record, and a mapping decides which of it ends up in which field.

## What is produced

The `ai` metadata group of the file, visible in the asset browser's info tab and under `/inspect/files/`:

| Field | |
| --- | --- |
| `title` | A short title, per data language. |
| `description` | One or two factual sentences, per data language. |
| `keywords` | One entry per concept, each translated into every data language — this maps onto linked keyword records. |
| `keywords_text` | The same keywords joined, per language, for a plain text field. |
| `categories` | Broad subject classes — nature, vehicle, artwork, architecture — per concept and language. |
| `categories_text` | The categories joined, per language. |
| `visible_text` | Text legible in the picture — a sign, a label, a number plate — verbatim, in whatever language it is in. |

Categories are the coarse layer above the keywords. A caption saying "a snow-covered peak resembling the Matterhorn" never contains the word *nature*, so a search for nature pictures has nothing to hold on to; the category line gives it exactly that. It is also what the word-based half of the [hybrid search](semantic-search.md) matches against.

## Which files are tagged

Any file fylr can show a picture of: images, and the previews it produces for PDFs and videos. Audio has no picture and is skipped — the job ends as an error in the log, which is the honest record of "there was nothing to look at".

The picture sent is the produced **preview**, or **small**, not the original — unless a pool's policy explicitly allows the original.

## Configuration

Tagging is configured with the `ai_tagging` block, resolved from the most specific place down: the pool, then its parents, then the objecttype, then the base configuration (**Base Configuration → Services → ai\_tagging**). A pool can therefore switch tagging on and inherit the prompts from above.

<table data-header-hidden><thead><tr><th width="230"></th><th></th></tr></thead><tbody>
<tr><td><code>enabled</code></td><td>Whether files are tagged on save.</td></tr>
<tr><td><code>provider</code></td><td>The provider, optionally with its model: <code>claude</code> or <code>claude/claude-opus-4-8</code>.</td></tr>
<tr><td><code>keyword_count</code> / <code>category_count</code></td><td>How many keywords and categories to ask for.</td></tr>
<tr><td><code>system_prompt</code>, <code>title_prompt</code>, <code>description_prompt</code>, <code>keywords_prompt</code>, <code>categories_prompt</code></td><td>What to ask for. Empty falls back to fylr's own prompts, which ask for factual, archival descriptions and forbid invention.</td></tr>
</tbody></table>

The result is recorded per configuration: two pools with different prompts produce two records of the same file, both visible in the log, and the file's `ai` group holds the most recent one.

## Getting it into your fields

The mapping profile **AI** (`ai.yml`) offers every field above as a mapping source. Map them onto your objecttype's fields once — title onto a title, keywords onto linked keyword records, and so on — and then either

* let the metadata mapping run when a file is attached, or
* run a **metadata task** over a set of records to write the values in bulk.

Nothing is written to a record without a mapping. Tagging on its own only fills the file's metadata.

## Doing it by hand

`POST /api/v1/ai/tag` with a file id tags one file immediately, `force=true` even when a result already exists. That is the door for a re-run after the prompts changed.
