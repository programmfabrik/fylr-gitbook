---
description: the instance-wide AI settings, and the request log
---

# AI Configuration

The **AI configuration** app (black menu → **AI configuration**) has three tabs: the [providers](providers.md), the settings below, and the log. It needs the `system.root` right.

These settings are not in the base configuration because they need live feedback from the providers — which embedding models are on offer, which model can be the assistant — and that list changes as providers are enabled and disabled.

## Embeddings

An embedding is a vector: a record's text turned into numbers, so that two records that mean similar things sit close together. fylr stores one vector per record and puts it into the index, which is what makes [semantic search](semantic-search.md) possible.

<table data-header-hidden><thead><tr><th width="230"></th><th></th></tr></thead><tbody>
<tr><td><strong>Embed objects</strong></td><td>Whether records are embedded at all.</td></tr>
<tr><td><strong>Embedding model</strong></td><td>The model, as <code>&lt;provider&gt;/&lt;model&gt;</code>. Only embedding models of enabled providers are offered; the dimension follows from the model.</td></tr>
<tr><td><strong>Data languages</strong></td><td>Which languages of a record's text are embedded. Empty means the first data language. Embedding six translations of the same sentence costs six times as much and helps nothing, so pick the languages your users actually search in.</td></tr>
</tbody></table>

{% hint style="warning" %}
Changing the model, its dimension or the languages invalidates every stored vector and the index mapping. Saving therefore asks to **rebuild the index**; until that has run, semantic search works with what is still there.
{% endhint %}

## Semantic search

<table data-header-hidden><thead><tr><th width="230"></th><th></th></tr></thead><tbody>
<tr><td><strong>Offer semantic search</strong></td><td>Whether the <code>semantic</code> search element may be used at all. Off means the API refuses it and the chat says so.</td></tr>
<tr><td><strong>Neighbours per search (k)</strong></td><td>How many nearest records a vector search returns. A k-NN search always returns k records, however unlike they are — see the note below.</td></tr>
<tr><td><strong>Minimum similarity</strong></td><td>A floor between 0 and 1. With a floor, the search returns every record above it instead of the k nearest, which is what turns "the 20 closest" into "everything that actually matches". 0 keeps all k.</td></tr>
<tr><td><strong>Search assistant</strong></td><td>A completion model that turns a chat request into a retrieval query before searching. Empty means the chat searches the words as typed.</td></tr>
</tbody></table>

{% hint style="info" %}
A pure vector search has no notion of "no match": ask for k neighbours and you get k, the last of them arbitrarily unrelated. Either give it a floor, or use the hybrid search, whose fusion with the word-based side is its own cut.
{% endhint %}

## The log

The **Log** tab lists what fylr sent and what it cost: the time, the user, the type of request (`tagging`, `field_prompt`, `search`, `embed`), the model, the subject, the tokens in and out, and the status. Every AI call in fylr writes such a row, including the ones a background job made — see [Queue, log and costs](operations.md).
